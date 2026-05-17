# Contributing to humanities-writing-companion

欢迎贡献。这份 skill 是一个**有思想立场**的项目——它倾向于"思想对话"而非"格式润色"，倾向于"工程化严谨"而非"经验启发"，倾向于"作者声音"而非"标准学术语体"。提交贡献前请先理解这套立场，看你提议的改动是否与之兼容。

**与 academic-research-skills 的分工**：本 skill 不做实证研究流水线（文献检索、数据收集、方法论合规等）——那是 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 的领地。本 skill 专注人文学科的写作声音、论证肌理、文风发展。在提议改动前请先确认它属于本 skill 的范围。

---

## 怎么贡献最有价值

### 🥇 学科测试（最需要）

skill 当前是从某个具体的人文学科论文项目里长出来的，但目标是覆盖**整个人文学科**（历史、哲学、文学、文化研究、艺术史、宗教学、古典学等）。最有价值的贡献是：

1. 在你的学科 / 论文项目里实战使用
2. 报告**哪些模块工作良好、哪些水土不服**
3. 提议**学科特定的扩展**（例如：中世纪研究的拉丁文核查、艺术保护的物质文化分析、民族音乐学的田野记录处理）

参见 [`docs/cross-domain-testing.md`](docs/cross-domain-testing.md) 中按学科分组的测试场景。

### 🥈 扩充 AI 痕迹排查清单

[`references/ai-trace-checklist.md`](references/ai-trace-checklist.md) 是这份 skill 的"防御纵深"。如果你在自己的写作中发现了**新的未审视表达模式**（不只是 AI 套话，还包括学科特定的八股、理论阅读形成的惯性），欢迎提 PR 补充。

### 🥉 双语补全

当前 SKILL.md 和 README 已有中英双语版本（SKILL.md / SKILL.zh.md / README.md / README.zh.md），但 `references/` 中的支持文件（ai-trace-checklist、project-management、target-reader-profile-template）和 `scripts/` 的注释当前以中文为主。把这些翻译成英文是高价值贡献。

翻译原则：
- `ai-trace-checklist.md` 的中文套话清单（如"值得注意的是"）需要补充对应的英文套话（如"It is worth noting"、"It should be noted"）——不是直译，而是英文学术写作中的对等套话
- 引用格式速查的部分如果涉及 GB/T 7714 之外的引用规范，按英文学术惯例处理

### 🏅 新增工作模式

skill 当前有 7 个工作模式（A-G）。如果你发现了 SKILL.md 没有覆盖的高频写作场景，可以提议新模式。新模式的**门槛**：

- 必须**机械区分**于现有模式（不是已有模式的换名/再说明）
- 必须有**独立的输入要求 / 输出格式**
- 必须给出**至少一个具体使用场景** + **预期效果**

### 引用格式支持

当前 skill 的引用配置假设作者会在 onboarding 时选择（APA / Chicago / MLA / GB-T 7714 / 期刊自定义）。如果你想让某个引用规范有更深的内置支持（例如自动生成符合 GB-T 7714 顺序编码制的参考文献列表），可以提议。

### 脚本工具

`scripts/` 目录三个工具的扩展或新工具——例如：

- 段落连贯性检测（基于句首/句尾词汇重复）
- 概念漂移检测（同一术语在不同章节的语境频率统计）
- 引用密度分析（按章节统计引用密度，标记异常段落）

新脚本必须**零依赖或少依赖**（zsh / Python 3 标准库 / 最多 1-2 个常用包），符合 `scripts/README.md` 的设计原则。

---

## 不太需要的贡献类型

> 不是这些贡献"不好"，而是它们偏离 skill 的设计立场。提了不一定会被合并。

- ❌ **把 skill 变得更"通用"**——例如加一个"通用润色模式"、扩展到实证社科或 STEM。skill 故意有立场（**人文学科** + 思想优先 + 文风保持），不试图取悦所有写作场景。要做实证研究流水线请去 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)。
- ❌ **替换现有模块为 LLM 调用**——skill 用纯文本 prompt 描述工作模式，故意**不**依赖运行时 LLM 调用（这让它能在 Agent SDK / Claude Code / Claude.ai 等任何 Claude 接入点工作）。
- ❌ **"AI 智能润色"功能**——skill 的核心是反对"AI 自动润色"叙事的。润色应该是作者驱动的对话过程。
- ❌ **添加付费/订阅集成**——skill 是开源公共物品。

---

## 提交流程

### 小改动（typo / 文档修订 / 小规模 ai-trace-checklist 扩充）

直接提 PR，简短描述改动理由即可。

### 大改动（新模式 / 大幅修订 SKILL.md）

**先开 issue 讨论**。SKILL.md 和 SKILL.zh.md 各约 900 行，每一节都和其他节有交互——直接 PR 大改动很容易破坏现有联动设计（例如：模式 G 盲读核对故意不读 `_writing-config/` 文件，这是设计而非疏忽）。

**双语联动**：对 SKILL.md 的实质修改，必须同时修改 SKILL.zh.md（保持双语一致）。同理 README.md / README.zh.md。仅修改一个版本的 PR 会被要求补全另一个。

讨论时请说明：

1. 你想解决什么具体的写作场景问题
2. 现有 skill 哪个模块/规则不够用（最好引用 SKILL.md 行号）
3. 你的改动会影响 SKILL.md 哪些其他部分（联动检查）
4. 改动后的验证方式（如何知道改对了？）

### Commit message 风格

不强制约定，但建议：

- 清晰说明**改了哪一节 / 哪个模块**
- 一句话说明**为什么改**
- 如果改了 SKILL.md 中需要联动同步的多处，列出来

例：

```
ai-trace-checklist: 新增"过度概念化"作为第七类未审视模式

在多次实测中发现，AI 倾向于把日常表达升格为术语
（"这表明" → "这一现象在认识论层面表明"）。这一模式
不属于现有六类中任何一类，但出现频率很高。
```

---

## Code of Conduct

简单原则：

- 学术性的批判欢迎，人格性的攻击不欢迎
- 不同的学科传统都值得尊重，"我学科才是真学问"的姿态不欢迎
- skill 服务于作者的**思考**，任何提议如果会削弱作者的认知主体性（例如把作者变成 AI 输出的盲签字员），都不会被接受

---

## License

提交贡献即同意按 [MIT License](LICENSE) 发布。
