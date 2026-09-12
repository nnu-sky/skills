---
name: nature-experiment-log
description: "在用户要求记录、整理或归档实验日志时，将实验笔记、图片或语音整理为带 YAML frontmatter 的 Markdown。普通图片解读、科研问答或单纯提供文件不触发。"
license: Apache-2.0
metadata:
  author: Jiahao8595
  hermes:
    tags: [research, experiment, logging, obsidian, automation]
    related_skills: [nature-literature-pipeline, obsidian]
---

<!-- Modified by NNU Sky, 2026-09-12: portable distribution and task-scoped instruction review; see repository THIRD_PARTY_NOTICES.md. -->


# experiment-log — 实验日志标准化

## 输入方式

仅在用户要求记录、整理或归档实验日志时使用。原始材料可以来自：

- **直接上传** — 在当前会话提交图片、音频、语音转录或文字。
- **本地材料** — 提供本地文件或文件夹路径，由 agent 读取并整理。

## 输出方式

- **本地 Markdown** — 使用用户已指定或项目已约定的日志目录，不重复确认；没有可确定的目录时，先返回可保存的 Markdown。
- **Obsidian vault** — 通过可选的 `obsidian` skill 写入 vault，并使用附带模板建立索引、异常记录和设备追踪。

核心流程不要求安装 Obsidian。

## 处理流程

1. 接收上传材料或读取相关本地文件。
2. 使用当前可用的图像理解、转录或文本解析能力提取信息，不为特定工具名称额外安装依赖。
3. 先整理已知信息，将缺失或模糊字段标为待补充；只有影响样品归属、结果解释或归档正确性的缺失才询问，不猜测实验条件或结果。
4. 复用已确定的输出方式、目录和实验或样品 ID；需要新 ID 时按已有项目约定或下述规则生成，不编造样品关系。
5. 写出 `{OUTPUT_ROOT}/实验日志/{体系}/{类型}/{exp_id}.md`。
6. 将原始附件归档到 `{OUTPUT_ROOT}/raw/experiments/YYYY.MM.DD_描述_EXPID/`，并在日志中建立引用。
7. 如启用索引模板，更新实验索引；发现异常时追加异常记录。
8. 告知用户生成文件及原始材料的具体位置。

温度记不清时保留待补充标记；样品编号不明且会导致归档错误时，先完成已知内容的整理，再询问对应关系。

## 目录结构

```
/vault/
├── raw/experiments/                       ← 原始层（归档）
│   └── YYYY.MM.DD_描述_EXPID/
│       ├── 笔记.md
│       ├── 图片/
│       └── 语音/
│
wiki/实验日志/                              ← 标准层（产出）
├── 实验索引.md
├── 异常记录.md
├── {体系A}/
│   ├── 实验类型1/
│   ├── 实验类型2/
│   └── ...
├── {体系B}/
│   └── ...
└── 公共/
    └── 设备与试剂追踪.md
```

## 实验 ID 规则

```
{体系代码}-{设备代码}-YYMMDD-{序号}
  │        │       │       └─ 当日序号（001 起）
  │        │       └─ 日期
  │        └─ 设备代码（M=马弗炉, T=管式炉, E=电化学, G=手套箱, F=可控气氛炉, B=通用）
  └─ 体系代码（自定义，如 CL / NO / OX / HY 等）
```

## 样品批次 ID 规则

```
{体系代码}-{候选编号}-B{序号}
  │        │         └─ 配盐批次序号
  │        └─ 候选配方编号
  └─ 体系代码
```

同一批样品跨多个实验时 `sample_batch` 保持一致，便于 dataview 追踪。

## 设备代码

| 代码 | 设备 | 场景 |
|------|------|------|
| M | 马弗炉 | 热处理、浸泡腐蚀 |
| T | 管式炉 | 气氛控制、脱水、热稳定性 |
| E | 电化学工作站 | CV/SWV/EIS |
| G | 手套箱 | 配盐、称量、取样 |
| F | 可控气氛炉 | 精密气氛控制 |
| B | 通用 | 干燥、清洗、制样 |

按实际设备扩展。

## 可选的 Obsidian 集成

本 skill 可以只向普通本地文件夹输出 Markdown，也可以与 [Obsidian](https://obsidian.md) vault 配合使用。Obsidian 是一个基于本地 Markdown 文件的笔记系统，配合 [Dataview](https://github.com/blacksmithgu/obsidian-dataview) 插件可实现实验数据的动态查询和仪表盘。

**为什么用 Obsidian：**
- 所有日志为纯文本 Markdown，可版本控制、可全文搜索
- YAML frontmatter 结构使 dataview 可自动生成实验列表、异常汇总、设备使用记录
- 本地存储，无云依赖性，数据安全

**安装 skill 后需在 vault 中创建以下文件：**

| 文件 | 模板 | 用途 |
|------|------|------|
| `实验日志/实验索引.md` | `templates/experiment-index.md` | Dataview 查询仪表盘 |
| `实验日志/异常记录.md` | `templates/anomaly-log.md` | 异常记录 |
| `实验日志/公共/设备与试剂追踪.md` | `templates/equipment-tracking.md` | 设备与试剂追踪 |

将模板文件复制到你的 Obsidian vault 对应位置即可使用。

## 参考示例

`references/` 目录包含三个完整的实验日志示例，覆盖常见实验类型：

| 文件 | 实验类型 |
|------|---------|
| `references/example-log.md` | 材料腐蚀浸泡实验 |
| `references/example-electrochemical.md` | 电化学表征（CV 窗口测试） |
| `references/example-thermal-stability.md` | 热稳定性实验 |

每个示例均包含完整的 YAML frontmatter 和 Markdown 正文，可直接作为模板修改使用。

## 自定义指南

- **体系代码**：按你的实验体系自定义（如 CL/NO/OR/PO）
- **实验类型**：在 `wiki/实验日志/{体系}/` 下按需创建子目录
- **YAML 字段**：模板是建议结构，可增删字段
- **设备代码**：按实际实验室设备扩展
- **输出根目录**：可以是普通本地文件夹，也可以是 Obsidian vault 根目录

## 相关文件

| 文件 | 用途 |
|------|------|
| `references/example-log.md` | 完整实验日志示例 |
| `wiki/实验日志/实验索引.md` | Dataview 仪表盘 |
| `wiki/实验日志/异常记录.md` | 异常记录格式 |
| `wiki/实验日志/公共/设备与试剂追踪.md` | 设备、试剂追踪 |
