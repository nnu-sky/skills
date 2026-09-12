#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 || "$2" != "--stdin" ]]; then
  echo "用法：$0 <SSH 别名> --stdin" >&2
  exit 64
fi

host="$1"
script="$(cat)"
payload="$(printf '%s' "$script" | base64 | tr -d '\n')"

ssh "$host" "payload='$payload'; script=\$(printf '%s' \"\$payload\" | base64 -d); exec bash -lc \"\$script\""
