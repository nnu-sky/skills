#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
用法：
  lab-server-status.sh list
  lab-server-status.sh check <别名>
  lab-server-status.sh status <别名>
  lab-server-status.sh gpu <别名>
  lab-server-status.sh jobs <别名>
  lab-server-status.sh sessions <别名>
  lab-server-status.sh disk <别名>
  lab-server-status.sh repo <别名> <远程路径>
  lab-server-status.sh fleet

所有命令均为只读；连接参数来自本机 SSH 配置。
USAGE
}

die() {
  printf '错误：%s\n' "$*" >&2
  exit 64
}

ssh_options=(-o BatchMode=yes -o ConnectTimeout=8)
ordinary_aliases=()
if [[ -n "${LAB_SERVER_ALIASES:-}" ]]; then
  read -r -a ordinary_aliases <<< "$LAB_SERVER_ALIASES"
fi

require_alias() {
  [[ $# -ge 1 && -n "$1" ]] || die "缺少 SSH 别名"
  [[ "$1" != -* && "$1" != *$'\n'* ]] || die "SSH 别名无效"
}

remote() {
  local alias_name="$1"
  local remote_command="$2"
  ssh "${ssh_options[@]}" -- "$alias_name" "$remote_command"
}

check_host() {
  remote "$1" 'printf "host="; hostname; printf "user="; id -un; printf "uptime="; uptime -p 2>/dev/null || uptime'
}

status_host() {
  local alias_name="$1"
  remote "$alias_name" '
    printf "host="; hostname
    printf "user="; id -un
    uptime
    printf "\nGPU:\n"
    if command -v nvidia-smi >/dev/null; then
      nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu,temperature.gpu --format=csv,noheader
    else
      echo "nvidia-smi unavailable"
    fi
    printf "\nDisk:\n"
    df -hP "$HOME"
  '
}

command_name="${1:-}"
case "$command_name" in
  ''|-h|--help|help)
    usage
    ;;
  list)
    [[ $# -eq 1 ]] || die "list 不接受其他参数"
    printf '%s\n' "${ordinary_aliases[@]}"
    ;;
  check)
    shift; require_alias "$@"; [[ $# -eq 1 ]] || die "check 只接受一个别名"
    check_host "$1"
    ;;
  status)
    shift; require_alias "$@"; [[ $# -eq 1 ]] || die "status 只接受一个别名"
    status_host "$1"
    ;;
  gpu)
    shift; require_alias "$@"; [[ $# -eq 1 ]] || die "gpu 只接受一个别名"
    remote "$1" 'if command -v nvidia-smi >/dev/null; then nvidia-smi; else echo "nvidia-smi unavailable"; fi'
    ;;
  jobs)
    shift; require_alias "$@"; [[ $# -eq 1 ]] || die "jobs 只接受一个别名"
    remote "$1" 'ps -u "$(id -un)" -o pid,ppid,etime,%cpu,%mem,stat,command --sort=-%cpu 2>/dev/null | head -n 40 || ps -u "$(id -un)" -o pid,ppid,etime,%cpu,%mem,stat,command | head -n 40; if command -v squeue >/dev/null; then printf "\nSlurm:\n"; squeue -u "$(id -un)"; fi'
    ;;
  sessions)
    shift; require_alias "$@"; [[ $# -eq 1 ]] || die "sessions 只接受一个别名"
    remote "$1" 'printf "tmux:\n"; if command -v tmux >/dev/null; then tmux list-sessions 2>/dev/null || echo "none"; else echo "unavailable"; fi; printf "\nscreen:\n"; if command -v screen >/dev/null; then screen -ls 2>/dev/null || true; else echo "unavailable"; fi'
    ;;
  disk)
    shift; require_alias "$@"; [[ $# -eq 1 ]] || die "disk 只接受一个别名"
    remote "$1" 'df -hT 2>/dev/null || df -h; printf "\nInodes:\n"; df -ih; if command -v quota >/dev/null; then printf "\nQuota:\n"; quota -s 2>/dev/null || true; fi'
    ;;
  repo)
    shift; require_alias "$@"; [[ $# -eq 2 ]] || die "repo 需要别名和远程路径"
    [[ "$2" != *$'\n'* ]] || die "远程路径不能包含换行"
    printf -v quoted_path '%q' "$2"
    remote "$1" "git -C ${quoted_path} status --short --branch && printf '\\nRemotes:\\n' && git -C ${quoted_path} remote -v"
    ;;
  fleet)
    [[ $# -eq 1 ]] || die "fleet 不接受其他参数"
    [[ ${#ordinary_aliases[@]} -gt 0 ]] || die "请通过 LAB_SERVER_ALIASES 指定目标别名"
    failures=0
    for alias_name in "${ordinary_aliases[@]}"; do
      printf '\n===== %s =====\n' "$alias_name"
      if ! status_host "$alias_name"; then
        failures=$((failures + 1))
      fi
    done
    [[ "$failures" -eq 0 ]] || exit 1
    ;;
  *)
    die "未知命令：$command_name"
    ;;
esac
