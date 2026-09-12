#!/usr/bin/env python3
import os
import sys

import pexpect


def main() -> int:
    args = sys.argv[1:]
    auth_mode = "password"
    max_prompts = 1
    while args and args[0].startswith("--"):
        if len(args) >= 2 and args[0] == "--auth" and args[1] in {"key", "password"}:
            auth_mode = args[1]
            args = args[2:]
        elif len(args) >= 2 and args[0] == "--max-prompts" and args[1].isdigit():
            max_prompts = int(args[1])
            args = args[2:]
        else:
            print("认证参数无效。", file=sys.stderr)
            return 64

    if len(args) != 2 or max_prompts < 1:
        print(
            f"用法：{sys.argv[0]} [--auth key|password] "
            "[--max-prompts 数量] <SSH别名> <远程命令>",
            file=sys.stderr,
        )
        return 64

    password = os.environ.pop("SERVER_OPS_PASSWORD", "")
    if not password:
        print("缺少受保护密码。", file=sys.stderr)
        return 78

    alias_name, remote_command = args
    ssh_args = ["-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=8"]
    if auth_mode == "key":
        ssh_args.extend(["-o", "BatchMode=yes"])
    else:
        ssh_args.extend(
            [
                "-o",
                "PubkeyAuthentication=no",
                "-o",
                "PreferredAuthentications=password,keyboard-interactive",
                "-o",
                "NumberOfPasswordPrompts=1",
            ]
        )
    ssh_args.extend([alias_name, remote_command])
    child = pexpect.spawn("ssh", ssh_args, encoding="utf-8", timeout=20, echo=False)

    prompt_count = 0
    timeout = 20
    while True:
        match = child.expect(
            [r"(?i)[^\r\n]*(?:password|密码)[^:\r\n]*:", pexpect.EOF, pexpect.TIMEOUT],
            timeout=timeout,
        )
        if child.before:
            sys.stdout.write(child.before)
            sys.stdout.flush()
        if match == 0:
            prompt_count += 1
            if prompt_count > max_prompts:
                child.close(force=True)
                print("认证提示次数超出预期。", file=sys.stderr)
                return 77
            child.sendline(password)
            timeout = None
        elif match == 1:
            break
        else:
            child.close(force=True)
            print("等待 SSH 认证提示超时。", file=sys.stderr)
            return 124

    child.close()
    if child.exitstatus is not None:
        return child.exitstatus
    if child.signalstatus is not None:
        return 128 + child.signalstatus
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
