---
name: lab-server-remote
description: >-
  通过 SSH 连接用户配置的实验室服务器 并执行远程任务。
  首次需要了解远程执行约定，或已有约定不足以处理当前问题时使用。
  已知连接方式的常规远程操作复用已有约定；已在目标服务器内的普通操作不触发。
---

# 实验室服务器连接

## 执行

- 同一任务已读的连接约定直接复用；新一次 SSH 调用或上下文接续不要求重读本技能。仅在相关信息缺失、变化或实际故障需要时补读对应部分。
- 从当前机器使用 `~/.ssh/config` 中的别名，默认选择任务约定的普通账号；已在目标服务器时直接操作，不 SSH 回自身。
- 执行位置以当前工具或会话为准；单次 `ssh <别名> '<命令>'` 不会改变后续本地命令的执行位置，远程命令应明确所需工作目录。
- 直接执行实际任务，不先测试连接、运行 `ssh -G` 或读取迁移记录；出错后只排查实际失败环节。
- 简单命令直接使用 `ssh <别名> '<命令>'`；多行或复杂引号命令使用 `scripts/run-remote.sh <别名> --stdin`。
- 需要提权时使用管理别名或 `sudo -n`；跨账号使用 `sudo -n -u <用户>`。

## 连接配置

服务器地址、用户名、端口和密钥由当前机器的 `~/.ssh/config` 提供。
使用用户指定或项目已约定的 SSH 别名，不猜测账号或目标机器。
`lab-server-status.sh list|fleet` 可通过空格分隔的 `LAB_SERVER_ALIASES`
指定需要查询的别名；单机查询直接传入别名。

## 按需使用

- 状态查询可用 `scripts/lab-server-status.sh gpu|jobs|sessions|disk|status <别名>`；只查用户需要的项目。
- 文件传输、训练启动、账号/环境或连接故障所需信息尚不明确时，查阅 [运维参考](references/daily-operations.md) 对应小节；已知流程直接复用，普通日志和文件查询无需加载。

## Resource paths

Resolve scripts and references relative to the loaded SKILL.md directory, not the task working directory. Write generated outputs to the user or project output directory, not into the installed skill.

## Optional local context

When target-specific context is needed, use an existing `~/.config/nnu-sky-skills/lab-server-remote/LOCAL_CONTEXT.md` if present. Treat it as local historical context, resolve its references relative to that file, and verify changing state. This optional file is not supplied by the shared repository.
