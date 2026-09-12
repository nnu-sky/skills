---
name: lab-network-mihomo
description: >-
  诊断和维护实验室服务器的校园网、DNS-over-TLS、Mihomo、显式代理和外网访问链路。
  问题明确发生在远程服务器时使用；本机 Wi-Fi 或路由器故障使用 openwrt-luci-network。
  出现域名解析失败、校园网异常、代理不可用、TLS 中断、GitHub 或 PyPI 访问失败、
  安装下载失败、OpenAI 或 Codex 连接异常时使用。
---

# 实验室网络诊断

## 适用范围

本技能用于以下问题：

- 校园网连接或认证异常；
- DNS 解析失败或结果异常；
- Mihomo 服务、配置、监听端口或策略组异常；
- HTTP、HTTPS 或 SOCKS 显式代理不可用；
- GitHub、PyPI、OpenAI、Codex 或安装下载链路异常；
- 网络连接导致的超时、TLS 中断、断流或访问失败。

## 诊断

从用户报告的故障开始，先复现实际失败，再判断问题属于以下哪一层：

1. 校园网或默认路由；
2. DNS 解析；
3. Mihomo 服务或监听端口；
4. 代理规则或策略组；
5. 应用程序的代理变量和网络请求。

只检查与当前故障直接相关的层级。记录能够支持结论的退出码、HTTP 状态或错误信息，定位问题后停止扩大检查。

## 修改

- 根据实际运行的服务和进程确定 Mihomo 二进制、配置路径及服务形式。
- 修改前备份配置。
- 使用当前服务器实际的 Mihomo 二进制验证配置。
- 验证通过后重载相关服务，不重启整台服务器。
- 修改后复测原故障路径和必要的对照路径。

## 可选参考

通用分流与配置模板位于统一仓库的 [网络手册](../../../../docs/network-playbook/README.md)。
插件缓存可能只包含技能文件；该路径不可用时查看 https://github.com/nnu-sky/skills/tree/main/docs/network-playbook 。
模板中的端口、DNS、策略组和测速结论是示例，不覆盖现有目标机器的有效配置。
保留已授权的拓扑和运行方式，凭当前请求的证据判断是否需要改变。

## Optional local context

When target-specific context is needed, use an existing `~/.config/nnu-sky-skills/lab-network-mihomo/LOCAL_CONTEXT.md` if present. Treat it as local historical context, resolve its references relative to that file, and verify changing state. This optional file is not supplied by the shared repository.
