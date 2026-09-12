# NNU Sky Skills

可复用的 Codex skills 与插件：模型工程优化、视觉训练配方、科研写作与绘图、服务器和网络诊断。

这是共享内容的统一维护源。技能描述以任务为入口，按需读取资料；不固定模型版本、推理强度或子代理数量。已依据 2026-09-12 的 GPT-6 Astra 官方提示指导审查，详见 [适配说明](docs/gpt-6-review.md)。这表示指令与结构经过审查，不代表每项科研工作流都完成了模型行为或实机测试。

## 能力

| 插件 | 包含的 skills | 用途 |
|---|---|---|
| `gpu-training-infra` | 同名 skill | 用户明确要求时优化模型与训练代码的工程效率 |
| `vision-classification-tuning` | 同名 skill | 明确点名调用，寻找并验证视觉训练配方 |
| `research-toolkit` | `ml-paper-writing`、`nature-academic-search`、`nature-experiment-log`、`nature-figure`、`nature-paper-card`、`research-mechanism-lens`、`nature-shared` | 论文、检索、日志、科学图、精读卡、机制分析；共享资料随包安装 |
| `lab-codex-ops` | `lab-server-remote`、`server-ops`、`lab-network-mihomo`、`openwrt-luci-network` | SSH、跨账号运维、远程服务器网络、本机及路由器网络 |

`nature-shared` 是支持包；`vision-classification-tuning` 与 `research-mechanism-lens` 保留显式调用策略。普通状态查询不触发训练优化。

## 安装

需要 Git；独立技能安装需要 Python 3.9+。把仓库放在一个长期保留的目录：

```bash
git clone https://github.com/nnu-sky/skills.git
cd skills
python3 scripts/install_skills.py --all
```

该方式把 skills 链接到 `${CODEX_HOME:-~/.codex}/skills/`，后续 `git pull --ff-only` 即更新源文件。若存在同名安装，先报告冲突并退出；显式 `--replace` 会将旧目录移到 Codex 配置目录下的带时间戳备份，再创建链接。不会修改全局 `AGENTS.md`、SSH、代理或模型配置。

可只选一个技能；科研技能的 `nature-shared` 依赖会一同链接：

```bash
python3 scripts/install_skills.py --skill nature-figure
```

也可使用支持插件命令的 Codex CLI 安装一个完整插件：

```bash
codex plugin marketplace add "$PWD"
codex plugin add research-toolkit@nnu-sky-skills
```

其他插件名称见上表。插件方式与独立技能方式选择一种，避免同名能力重复加载。插件缓存不随仓库文件自动变化；拉取更新后重新执行相应 `codex plugin add`。更新后在新任务中使用。

Windows 若无创建符号链接权限，可使用插件安装，或开启系统开发者模式后使用独立安装脚本。

## 网络内容是什么

- **服务器网络诊断**：服务器连不上 GitHub、PyPI 或 Codex 时，定位 DNS、路由、代理服务还是应用配置的问题。
- **本机与路由器诊断**：电脑 Wi-Fi、系统代理与 OpenWrt/LuCI 的问题，和远程服务器分开检查。
- **[网络手册](docs/network-playbook/README.md)**：Mihomo 分流策略、示例配置与诊断方法。它是参考资料，不会因安装插件自动应用配置。

服务器地址、账号、端口、密钥与密码由使用者自己的配置提供。SSH 使用 `~/.ssh/config`；管理员回退配置见 [server-ops 配置](plugins/lab-codex-ops/skills/server-ops/references/configuration.md)。示例机器 `compute-user`、`compute-admin` 需要使用者定义。网络手册中的历史测量只说明原测试条件下的结果。

## 依赖与运行边界

技能安装不会自动安装外部服务。文献检索优先使用现有工具，无对应 MCP 时采用已提供的网页/API 路径。图表按项目选择 Python 或 R；PDF 处理、绘图与可选 MCP 的依赖在各技能内按需说明。OpenRouter 仅在用户明确指定时使用，并需要用户自行配置凭据。

安装检查不启动 GPU 训练、不连接服务器、不调用付费图像 API。LaTeX 模板是历史参考，正式投稿应取得当前会议官方模板；`natbib` 由 TeX 发行版提供。

## 维护

源码只在 `plugins/*/skills/*` 维护，独立安装链接直接使用它。不要编辑 Codex 插件缓存。原来独立的训练插件仓库保留兼容入口，后续开发以本仓库为准。

修改后运行：

```bash
python3 -m pip install pyyaml
python3 scripts/validate_repository.py
```

只验证改动相关路径。模型提示词审查与真实行为验证分开记录；不将结构校验称为模型效果验证。

## 来源与许可

保留上游作者和文件内许可证，见 [第三方说明](THIRD_PARTY_NOTICES.md)。原作者的模板和样例不因被收录就变为 NNU Sky 自有作品。个人网络配置、凭据、编译缓存与第三方 figures4papers 素材不在此共享包中。
