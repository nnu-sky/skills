#!/usr/bin/env bash
set -euo pipefail

server_key="${1:-}"
role="${2:-}"
if [[ ! "$server_key" =~ ^[A-Za-z0-9_-]+$ ]] || [[ "$role" != "admin" && "$role" != "user" ]]; then
  echo "用法：$0 <服务器键> <admin|user> [--sudo-user <用户>] -- '<远程命令>'" >&2
  exit 64
fi
shift 2

sudo_user=""
if [[ "${1:-}" == "--sudo-user" ]]; then
  if [[ $# -lt 2 ]]; then
    echo "缺少目标用户。" >&2
    exit 64
  fi
  sudo_user="${2:-}"
  shift 2
fi
if [[ "${1:-}" == "--" ]]; then
  shift
fi
if [[ $# -ne 1 || -z "${1:-}" ]]; then
  echo "用法：$0 <服务器键> <admin|user> [--sudo-user <用户>] -- '<远程命令>'" >&2
  exit 64
fi
remote_command="$1"

if [[ -n "$sudo_user" && ( "$sudo_user" == "root" || ! "$sudo_user" =~ ^[a-z_][a-z0-9_-]*[$]?$ ) ]]; then
  echo "目标用户名无效或不允许。" >&2
  exit 64
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bundled_config="${script_dir}/../assets/server-aliases.env"
default_config="${HOME}/.config/lab-codex-ops/servers.env"
config_override="${LAB_CODEX_OPS_CONFIG_FILE:-}"
secrets_file="${LAB_CODEX_OPS_SECRETS_FILE:-${HOME}/.config/lab-codex-ops/secrets.env}"
legacy_secrets_file="${HOME}/.config/server-ops/local-secrets.env"

if [[ ! -f "$bundled_config" ]]; then
  echo "缺少插件内置服务器别名映射：$bundled_config" >&2
  exit 66
fi

set -a
# shellcheck disable=SC1090
source "$bundled_config"
if [[ -n "$config_override" ]]; then
  if [[ ! -f "$config_override" ]]; then
    echo "指定的服务器别名覆盖文件不存在：$config_override" >&2
    exit 66
  fi
  # shellcheck disable=SC1090
  source "$config_override"
elif [[ -f "$default_config" ]]; then
  # shellcheck disable=SC1090
  source "$default_config"
fi
set +a

normalized_key="$(printf '%s' "$server_key" | tr '[:lower:]-' '[:upper:]_')"
role_key="$(printf '%s' "$role" | tr '[:lower:]' '[:upper:]')"
alias_var="LAB_${normalized_key}_${role_key}_ALIAS"
alias_name="${!alias_var:-}"
password_env_var="LAB_${normalized_key}_PASSWORD_ENV"
password_name="${!password_env_var:-}"
if [[ -z "$alias_name" ]]; then
  echo "服务器别名映射缺少变量：$alias_var" >&2
  exit 78
fi

error_file="$(mktemp "${TMPDIR:-/tmp}/lab-codex-ops-ssh.XXXXXX")"
trap 'rm -f "$error_file"' EXIT

ssh_options=(-o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=8)
direct_command="$remote_command"
password_command="$remote_command"
if [[ -n "$sudo_user" ]]; then
  encoded_command="$(printf '%s' "$remote_command" | base64 | tr -d '\n')"
  direct_command="encoded='$encoded_command'; command=\$(printf '%s' \"\$encoded\" | base64 -d) || exit 65; if [ \"\$(id -un)\" = '$sudo_user' ]; then exec bash -lc \"\$command\"; fi; if sudo -n -u '$sudo_user' true 2>/dev/null; then exec sudo -n -u '$sudo_user' -- bash -lc \"\$command\"; fi; exit 79"
  password_command="encoded='$encoded_command'; command=\$(printf '%s' \"\$encoded\" | base64 -d) || exit 65; if [ \"\$(id -un)\" = '$sudo_user' ]; then exec bash -lc \"\$command\"; fi; exec sudo -S -p 'LAB_CODEX_OPS_PASSWORD:' -u '$sudo_user' -- bash -lc \"\$command\""
fi

if ssh "${ssh_options[@]}" "$alias_name" "$direct_command" 2>"$error_file"; then
  exit
else
  direct_exit=$?
fi

auth_mode=""
if [[ "$direct_exit" -eq 79 && -n "$sudo_user" ]]; then
  auth_mode="key"
elif [[ "$direct_exit" -eq 255 ]] && grep -q "Permission denied" "$error_file"; then
  auth_mode="password"
else
  sed 's/[Pp]assword[^ ]*/认证信息/g' "$error_file" >&2
  exit "$direct_exit"
fi

if [[ ! -f "$secrets_file" && -f "$legacy_secrets_file" ]]; then
  secrets_file="$legacy_secrets_file"
fi
if [[ ! -f "$secrets_file" ]]; then
  echo "需要认证回退，但缺少受保护文件：$secrets_file" >&2
  exit 66
fi
secrets_mode="$(stat -c '%a' "$secrets_file" 2>/dev/null || stat -f '%Lp' "$secrets_file")"
if [[ "$secrets_mode" != "600" ]]; then
  echo "受保护文件权限必须为 600，当前为 $secrets_mode。" >&2
  exit 77
fi

set -a
# shellcheck disable=SC1090
source "$secrets_file"
set +a
if [[ -z "$password_name" ]]; then
  echo "服务器别名映射缺少有效的密码变量名。" >&2
  exit 78
fi
password="${!password_name:-}"
if [[ -z "$password" ]]; then
  echo "受保护文件缺少配置指定的密码变量。" >&2
  exit 78
fi

if python3 -c 'import pexpect' >/dev/null 2>&1; then
  max_prompts=1
  if [[ "$auth_mode" == "password" && -n "$sudo_user" ]]; then
    max_prompts=2
  fi
  export SERVER_OPS_PASSWORD="$password"
  python3 "$script_dir/password-ssh.py" --auth "$auth_mode" --max-prompts "$max_prompts" "$alias_name" "$password_command"
  unset SERVER_OPS_PASSWORD
elif command -v sshpass >/dev/null 2>&1; then
  export SSHPASS="$password"
  password_options=(-o PubkeyAuthentication=no -o PreferredAuthentications=password,keyboard-interactive -o StrictHostKeyChecking=yes -o ConnectTimeout=8 -o NumberOfPasswordPrompts=1)
  if [[ -n "$sudo_user" ]]; then
    printf '%s\n' "$password" | sshpass -e ssh "${password_options[@]}" "$alias_name" "$password_command"
  else
    sshpass -e ssh "${password_options[@]}" "$alias_name" "$password_command"
  fi
  unset SSHPASS
else
  echo "当前主机缺少 pexpect 或 sshpass，无法进行密码认证回退。" >&2
  exit 69
fi
