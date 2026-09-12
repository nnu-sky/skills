# 本地网络诊断

## 当前模型

- 局域网网关和 DNS 从当前路由与系统配置读取，不使用示例地址代替实测。
- 网卡名与本机地址由 DHCP 决定，不把历史接口和地址当成当前事实。
- 路由器可能负责透明代理、DNS 改写、自动节点选择和流量分流。

## Mac 侧只读检查

```bash
scutil --proxy
route -n get default
networksetup -getdnsservers Wi-Fi
scutil --dns
curl --noproxy '*' -s --max-time 8 https://www.cloudflare.com/cdn-cgi/trace
curl --noproxy '*' -o /dev/null -s -w 'openai=%{http_code} time=%{time_total}s ip=%{remote_ip} err=%{errormsg}\n' --max-time 12 https://api.openai.com/v1/models
curl --noproxy '*' -o /dev/null -s -w 'cursor=%{http_code} time=%{time_total}s ip=%{remote_ip} err=%{errormsg}\n' --max-time 12 https://api2.cursor.sh/
```

OpenAI 接口在无密钥时返回 401 代表链路可达。必须同时判断 curl 退出码、HTTP 状态、出口和耗时。

## 路由器检查

1. 确认实际运行的代理、DNS 和广告过滤组件。
2. 查看 OpenAI、ChatGPT、Codex、GitHub、Google 和 Cursor 域名的实际分流组与当前出口。
3. 检查自动组健康探针、切换阈值、出口是否频繁变化和候选是否足够。
4. 修改后重复 Mac 侧测试，并运行至少一次较长连接。

## 判断

- 短请求正常而长连接重连：优先检查长连接路径、HTTP/2 和节点质量。
- 同轮测试出口频繁变化：检查健康探针和切换阈值，不立即固定单节点。
- 普通 DNS 失败而 HTTPS 或 DoH 正常：先确认路由器是否接管 DNS，不盲改为公共 DNS。
- OpenAI 正常而 Cursor 失败：检查 Cursor 专用域名分流。
- 所有节点均不稳：用手机热点对照，区分 Mac、路由器、校园网和服务端问题。
