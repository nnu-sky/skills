# Mihomo 多业务分流与节点选择手册

这是一个脱敏的实验室服务器网络管理模板，目标是在不启用 TUN、不手工固定节点的前提下，用 Mihomo 原生能力完成：

- 多订阅保留与可达节点池隔离；
- 按人工智能、Google、GitHub、学术和默认外网分类；
- 每类业务使用自己的轻量目标测速；
- 直连与代理按实测决定，而不是按经验硬编码；
- 故障诊断、配置校验和安全发布。

本仓库不包含任何现网订阅地址、服务器地址、账号、密钥、控制器口令或登录文件。示例配置不能直接用于生产，必须先替换占位地址并按目标机器调整服务路径。

## 设计结论

当前推荐的七个业务组：

| 业务组 | 候选方式 | 原因 |
| --- | --- | --- |
| 人工智能 | 已验证代理来源 | 避免不可用或受限的直连出口 |
| Google | `DIRECT`＋已验证代理来源 | 由 Google 轻量目标实测决定，不预先固定代理 |
| GitHub 主站 | `DIRECT`＋已验证代理来源 | 12 个时间点中有 5 次只有直连成功 |
| GitHub Raw | `DIRECT`＋已验证代理来源 | 最近对照中两路均为 4/4 |
| GitHub codeload | `DIRECT`＋已验证代理来源 | 最近对照中两路均为 4/4 |
| 学术外网 | `DIRECT`＋已验证代理来源 | 最近对照中两路均为 4/4 |
| 默认外网 | 已验证代理来源 | 避免未知境外站点落到受限直连出口 |

单次结果不是永久结论。测试证据和调整条件见 [测试证据](docs/test-evidence.md)。

## 仓库结构

- [路由与选择](docs/routing-and-selection.md)：节点池、七组策略和规则顺序；
- [测试证据](docs/test-evidence.md)：直连与自动代理对照；
- [24 小时观察](docs/24h-monitoring.md)：低开销的小时级验证方案；
- [诊断流程](docs/diagnostic-workflow.md)：从基础网络到业务组的排查顺序；
- [示例配置](examples/mihomo.template.yaml)：完全脱敏的 Mihomo 模板；
- [安全说明](SECURITY.md)：禁止提交的敏感材料；
- `scripts/validate-template.py`：检查模板结构；
- `scripts/check-sensitive.sh`：提交前敏感信息扫描。

## 使用方式

1. 复制示例配置到受保护的本地工作文件。
2. 把两个 `example.invalid` 占位地址替换为自己的订阅入口。
3. 先验证两个来源的节点入口和关键业务；第一来源由七个业务组直接测试，第二来源分别由智能与通用两个组测试完整节点池。
4. 根据机器调整配置目录和服务单元。
5. 先执行结构检查和敏感信息扫描。
6. 再用目标机器自己的 Mihomo 二进制执行配置校验。
7. 备份现网配置，只重启 Mihomo，不重启服务器。

```bash
python3 scripts/validate-template.py examples/mihomo.template.yaml
bash scripts/check-sensitive.sh
mihomo -t -d /path/to/mihomo-home -f /path/to/mihomo.yaml
```

## 重要限制

`url-test` 只能说明测试时节点可用，不能保证节点在两次测试之间绝不抖动。这个模板不增加手动钉节点、多层故障转移或自写切换守护；发生瞬态失败时，先刷新对应业务组并重试一次。
脱敏的 Mihomo 多业务分流、节点选择与诊断手册
