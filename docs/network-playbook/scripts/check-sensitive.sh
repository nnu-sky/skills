#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

patterns=(
  '-----BEGIN .*PRIVATE KEY-----'
  'gh[opsu]_[A-Za-z0-9_]{20,}'
  'sk-[A-Za-z0-9_-]{20,}'
  'Authorization:[[:space:]]*Bearer[[:space:]]+[A-Za-z0-9._-]+'
  '(NAIYUN_SUBSCRIPTION_URL|SUYING_SUBSCRIPTION_URL|MIHOMO_CONTROLLER_SECRET)=(https?://|[A-Za-z0-9._-]{12,})'
)

for pattern in "${patterns[@]}"; do
  if rg --hidden --glob '!.git/**' --glob '!scripts/check-sensitive.sh' --pcre2 -- "$pattern" .; then
    echo "发现疑似敏感信息，请检查后再提交。" >&2
    exit 1
  fi
done

echo "未发现已知敏感信息模式。"
