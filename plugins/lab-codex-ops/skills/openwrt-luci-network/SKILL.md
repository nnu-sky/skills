---
name: openwrt-luci-network
description: >-
  诊断本地 Mac、Wi-Fi、OpenWrt、LuCI、透明代理、DNS 和节点路由。
  仅当问题发生在本机或路由器，或用户明确提到本地 Wi-Fi、OpenWrt、LuCI 时使用。
---

# 本地 OpenWrt 与 Wi-Fi

## 判断当前网络

- 从当前系统代理、默认路由和 DNS 判断流量经过本机代理还是路由器；不预设 TUN、透明代理或某个组件已经启用。
- 本机或路由器网络与远程实验室服务器是不同执行环境；分别验证实际失败路径。
- 连接目标与凭据来自用户提供或已有本地配置，不猜测网关地址、登录账户或密码存储位置。

## 按需读取

| 任务 | 读取 |
| --- | --- |
| 只读判断故障在本机、路由器还是上游 | [诊断流程](references/diagnostic-workflow.md) |
| 需要登录或修改 LuCI | 先读 [LuCI 访问](references/luci-access.md)，再读诊断流程 |

## 处理原则

1. 修改路由器前先完成 Mac 侧只读检查和热点对照所需的最小测试。
2. 确认路由器实际运行的代理与 DNS 组件后再选择命令，不根据旧记忆假定是 OpenClash、PassWall 或其他组件。
3. 优先使用带健康检查的自动组，保留多个候选和故障转移，不固定节点、地区或入口 IP。
4. 避免叠加本机 Clash 与路由器透明代理。
5. 修改后同时验证短请求和较长连接，观察出口漂移、TLS 中断与重连。
6. 报告系统代理、默认路由、DNS、路由器策略组、出口、状态码和延迟，不输出 LuCI 密码。

## Optional local context

When target-specific context is needed, use an existing `~/.config/nnu-sky-skills/openwrt-luci-network/LOCAL_CONTEXT.md` if present. Treat it as local historical context, resolve its references relative to that file, and verify changing state. This optional file is not supplied by the shared repository.
