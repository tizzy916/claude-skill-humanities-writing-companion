# 人文学科写作伙伴 · Humanities Writing Companion

> 一个 Claude Code / Claude Agent SDK skill，专为以长篇论证性文本为主要交付物的人文学者设计——历史、哲学、文学、文化研究、艺术史、宗教学、古典学。

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](./LICENSE)
[![Skill format: Claude Code](https://img.shields.io/badge/skill-Claude%20Code-orange)](https://docs.claude.com/en/docs/claude-code)
[![Status: stable](https://img.shields.io/badge/status-stable-green)]()

**[English README](./README.md)** · **[Skill 源文件 · 英文](./SKILL.md)** · **[Skill 源文件 · 中文](./SKILL.zh.md)**

---

## 定位

本 skill 是**人文学科一侧的写作伙伴**：服务于"文字本身就是论证"的领域——历史、哲学、文学、文化研究、艺术史、宗教学、古典学——提供以保护作者声音为核心的写作辅助。本 skill **不是**研究流水线;实证研究流水线需求请见下方 [Companion 节](#companion-academic-research-skills)。

---

## Companion: academic-research-skills

本 skill 设计为 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)(以下简称 ARS)的**人文学科一侧互补工具**。ARS 是覆盖"文献检索 → 写作 → 审稿 → 修订 → 定稿"全流程的实证研究综合套件,两者设计为并用关系。

### 分工

```
academic-research-skills (Imbad0202)         humanities-writing-companion (本 skill)
─────────────────────────────────────        ──────────────────────────────────────
实证研究流水线                                人文写作的声音
数据 → 结果 → 写作                             构思 → 论证 → 散文
引用幻觉审计                                  声音保持 + 风格学习
PRISMA / RAISE / Material Passport          魔鬼代言人 + 自反性写作
```

典型工作流:用 ARS 做文献发现、引用审计、方法论合规、流水线编排;切换到本 skill 来写真正以"论证性散文为交付物"的人文章节。

### 设计借鉴(显式署名)

本 skill 借鉴了 ARS 的若干设计模式,在此显式致谢:

- **Concession Threshold 模式**(来自 ARS 的 reviewer 模块)→ 启发了本 skill Mode D 中"让步前最低标准"的抗谄媚机制
- Companion-skill 的并列说明结构,本身也参照了 ARS 自身的 `Companion: Experiment Agent` 结构

> Based on **Academic Research Skills** by Cheng-I Wu(吳政宜) — https://github.com/Imbad0202/academic-research-skills (CC BY-NC 4.0)

### License 注意

ARS 与本 skill 现在均采用 **CC BY-NC 4.0**(本 skill 自 2026-05-19 起从 MIT 改为 CC BY-NC 4.0,详见下方 [License 节](#license))。两者协议一致,组合使用 license-stacking 平凡:均禁止商业用途,均要求 attribution。如需对两者中任一进行商业使用,请分别联系各自作者。

---

## 本 skill 严肃对待的三件事

通用 AI 写作工具不会处理人文学科的这三件事：

**1. 声音保持是核心学术价值，不是风格装饰。**
在人文学科里，作者的声音承载认识论重量：它表明作者从哪个智识传统中写作、把谁视为对话者、哪些动作是自己的而哪些是借来的。一篇被润色成"标准学术英语"的论文，丢失的就是这种信号。本 skill 帮助你写得更像自己，而不是更不像。

**2. 论证和散文是不可分离的。**
实证研究里，糟糕的写作可以毁掉一个完美的实验。但人文学科里，**写作就是论证本身**——一句疲软的话、一个含糊的概念、一个未经辩护的过渡，都是论证失败。本 skill 在"散文中的论证"层面工作。

**3. 审稿人是真实而对抗性的。**
人文审稿人不温和。一个理论概念会被测试其锋利度；一个历史断言会被测试其证据；一个哲学论证会被测试最强的反对意见。本 skill 在内部模拟这种对抗，让论文在投稿前就先遇上。

---

## 一次典型的交互

```
你：帮我看看这段。我在论福柯的全景敞视主义如何延伸到数字平台。

[skill 读取该段 + 你的写作风格档案]

伙伴：
  我注意到三件事，按优先级排序。

  🔴 基底问题：你把"全景敞视"用作平台监控的隐喻，但福柯的原初概念
     依赖于一种建筑学装置生产出特定的主体位置。平台生产的是另一种主体
     （数据主体，而不是关在牢房里的身体）。你可以选择 (a) 把这个类比
     明确为类比并讨论差异；或者 (b) 用 Zuboff 的"工具型权力"，更贴合
     数据情境。你想走哪个方向？

  🟡 论证问题：第二段从"平台收集数据"跳到"这构成了监控"，没有补上中间
     "可见性即权力"的环节。一个善意读者会跟不上。

  🟢 文风问题：你的风格档案里写"第一人称 + 破折号插入"。第三段以"本文
     认为……"开头，读起来像八股。要不要恢复第一人称？

你：走方向 (b)。改吧。

[skill 给出修订；你保留听起来像你自己的版本]
```

这就是"思想对话伙伴，而不是润色工具"在实践中的样子。

---

## 核心特性

### 四层批判模式（不是单一润色）

```
第一层 · 基底批判 — "这篇论文在学术上成立吗？"
第二层 · 结构批判 — "论证是怎样展开的？展开得好吗？"
第三层 · 段落批判 — "这一段在做什么？做好了吗？"
第四层 · 语句批判 — "这句话说对了吗？说好了吗？"
```

**严格自上而下规则**：上层未解决时不在下层花大力气。

### 魔鬼代言人 + 抗谄媚机制

模拟三种审稿人 + 一个善意困惑读者：
- 审稿人 A · 理论苛刻型
- 审稿人 B · 历史实证型
- 审稿人 C · 方法论质疑型
- 读者 D · 善意困惑型（**独到设计**：能让善意读者困惑的地方就是论证薄弱处）

**抗谄媚硬机制**：作者推回质疑时，必须满足 5 项实质条件中的 ≥2 项才让步——防止 AI 在情绪压力下提前软化。

### 文风深层学习与保持（"我手写我口"）

不只是句式偏好，还包括：
- **论证节奏**（线性 / 螺旋 / 张弛）
- **学术姿态**（批判性继承 / 对话性推进）
- **引用的修辞功能**（权威锚点 / 批判靶标 / 对话接口 / 叙事性 / 概念工具）
- **AI 痕迹排查清单**（八类未审视表达模式 ≠ AI 套话 ≠ 学术八股）

### 学科特殊维度

不同章节类型对应不同的批判策略：
- 历史叙事 · 时代错位、反事实压力测试、史料处理
- 哲学论证 · 概念推演、跨理论嫁接、最强反对意见
- 文学批评 · 细读与诠释、文体意识、形式与意义
- 文化研究 · 权力-知识框架、位置性、概括范围
- 艺术史 · 描述与诠释、来源、接受史
- 宗教学 / 古典学 · 源语严谨性、传统意识、内外位置
- 案例分析（跨学科共用）

### ADHD 友好的交互设计

- 反馈分批：每轮 3-5 项最多
- 快速胜利优先
- 跳跃跟随（话题跳跃可能是洞见信号）
- 番茄钟友好的任务单元
- 长对话每 4-5 轮给"我们现在在哪"摘要

### 自反性写作支持（独到模块）

如果作者的研究本身涉及人-AI 协作（autoethnography of AI-assisted writing），本 skill 提供六类"反思时刻"分类：

🔄 方向转变 / 🚫 拒绝 / 🎭 声音冲突 / 🔧 工具依赖 / 💡 意外洞见 / 🤖 AI 痕迹觉察

**学术依据**（在论文里可直接引用）：
- Christou (2026). *Reconfiguring Reflexivity in the Era of AI*. *Qualitative Inquiry*.
- Wiles (2025). *Recursive Cognition in Practice*. *International Journal of Qualitative Methods*.
- Panke (2025). *How Can (A)I Research This? An Autoethnographic Exploration of Generative AI*.

### 工程化基础设施

借鉴软件工程的最佳实践，服务于人文写作：
- **版本管理**：小版本 = commit / 大版本 = release / `_drafts/` = feature branch
- **修改日志**：每次修改记录 diff + reason（像 git commit message）
- **反馈报告**：Blocker / Major / Minor / Question 四级（借鉴 code review）
- **系统性验证清单**：论证完整性 / 概念一致性 / 引用完整性 / 文风一致性
- **`[VERIFY]` / `[待核对]` 硬标记**：抗引用幻觉——绝不允许进入投稿版本

### 七个工作模式（不是单一对话模式）

- **模式 A** — 段落级对话
- **模式 B** — 章节级审读
- **模式 C** — 构思 → 新内容写作（含协作式起草协议）
- **模式 D** — 魔鬼代言人
- **模式 E** — 写作瓶颈辅助（五种解冻策略）
- **模式 F** — 底稿修订（双版本对照，对抗 AI 腔调）
- **模式 G** — 盲读核对（机械检查"承诺-兑现"）

### 工程化辅助脚本

[`scripts/`](./scripts) 提供三个零依赖工具：

| 脚本 | 用途 |
|------|------|
| `ai-trace-scan.sh` | 扫描套话与连接词堆砌 |
| `pending-checks.sh` | 汇总所有 `[VERIFY]` / `[待核对]` / `❓ 待讨论` / `[AI 草稿]` 标记 |
| `citation-consistency.py` | 引用格式一致性扫描（括号 / 逗号 / 连接词 / 中英姓名 / 页码） |

---

## 支持的人文学科

本 skill 内置各学科特化的批评维度,onboarding 时声明你的学科即可激活(也会从草稿中自动检测)。**每个学科都有通用 AI 写作工具看不见的失败模式**:

| 学科 | 本 skill 重点关注 |
|---|---|
| **历史 · History** | 时代错置(把当代概念投射到过去);反事实压力测试(事情有没有可能不这样发生?);史料处理纪律(一手 vs 二手、史料内部声音);因果链透明度 |
| **哲学 · Philosophy** | 概念派生链条(这个概念从哪里来、如何被变形);跨理论移植代价(把传统 A 的概念引入传统 B 是否支付了转运成本);最强反对意见的 steel-man(反驳前先把对手论证做强) |
| **文学与文学批评 · Literature** | 文本细读 vs 解释(解释是否锚定在文本证据上?);文类意识(文类是意义的一半);形式-意义贴合(形式观察是否真的承担解释重量) |
| **文化研究 · Cultural Studies** | 权力-知识框架(谁在说话,谁被言说);位置性(作者自己的位置);概括范围(这个个案是否支持普遍主张) |
| **艺术史 · Art History** | 描述 vs 解释(分开!);来源与物质史(物件本身的生命);接受史(作品在其当下是否被这样读,还是只有现在才被这样读) |
| **宗教学与古典学 · Religious Studies & Classics** | 源语言严谨度(读原文还是只读译本?);传统意识(预设了哪个传统的解读);内部-外部位置(etic vs emic) |
| **跨学科案例分析** | 为什么是这个案例(典型 vs 例外);它能不能推广 / 推广到哪;案例叙事 vs 案例论证 |

**没看到你的子学科?** 大多数子学科(中世纪研究、思想史、科学史、民族音乐学、艺术保护……)继承自上述主要学科中的一两个。在 onboarding 时声明继承关系即可(如「我做思想史 —— 继承自历史 + 哲学」),或者开 Issue 提议新维度。

每个学科的完整批评维度在 `SKILL.md § Humanities Discipline-Specific Dimensions` 中——本表是 README 层的展示面,skill 内部承载完整 rubric。

---

## Showcase · 真实 Before / After 案例

四层批评的真实应用。作者的学位论文初稿(讨论 Stiegler 的 pharmakon 与 AI):

> **Before.** Stiegler 的 pharmakon 概念表明,技术既是毒也是药。所以 AI 也是 pharmakon。我们要谨慎使用 AI,避免落入它的负面效应。正如 Stiegler 所说,技术是一把双刃剑。

skill 的回应,自上而下,四层:

```
🔴 第 1 层 · 基础 — 论证成立性

  这一段把 pharmakon 等同于"双刃剑"。Stiegler 明确反对这种等同
  (WMLWL, p. 12):pharmakon 的治愈力与破坏力是**同时**而非交替的,
  且破坏力**与治愈力成正比**。"双刃剑"暗示的是"用户的选择"——你
  小心点就好;pharmakon 暗示的是"先于用户选择的结构性条件"。这不
  是细微差别,这是为什么 Stiegler 从 Derrida 那里借这个概念的整个
  原因。

  判断:基础已破。在修复 L1 前,不下到下面三层。

🟡 第 2 层 · 结构 — 论证展开(L1 未修复前不做)

🟢 第 3 层 · 段落(暂缓)

⚪ 第 4 层 · 句子(暂缓)
```

作者重写基础后,这段可能变成:

> **After.** 在 Stiegler 的框架中(承自 Derrida 对柏拉图《斐德罗》的解读),*pharmakon* 命名的是一种**结构性条件**而非道德选择:技术的治愈力与破坏力**不可分离且强度成正比**(Stiegler, *What Makes Life Worth Living*, 2013, p. 12)。对 LLM 而言,这意味着真正的问题不是"我们是否足够小心地使用它?"——这种提问预设了一个**完全在 pharmakon 之外**的用户。真正的问题是:*在什么样的历史-器官学配置下,pharmakon 的破坏性面向被结构性地强化?* 我将在下文论证:沿着 Stiegler 在 *Automatic Society*(2017)对数字第三持存的诊断……

变化:陈词滥调的"双刃剑"被 Stiegler 真正的概念动作替换;引用锚定在可核查的页码;结论指向下一段可以展开的具体论题。**skill 没有替作者写这个重写**——它指出基础错了、说清楚错在哪里、然后**拒绝在基础修复之前做任何句子级工作**。

> **这就是"思维伙伴,而非润色工具"的实际含义。**

---

## 安装

### 作为 Claude Code skill 安装

```bash
git clone https://github.com/tizzy916/claude-skill-humanities-writing-companion.git \
  ~/.claude/skills/humanities-writing-companion

chmod +x ~/.claude/skills/humanities-writing-companion/scripts/*.sh
```

或者作为项目级 skill（仅当前 vault / project 可用）：

```bash
git clone https://github.com/tizzy916/claude-skill-humanities-writing-companion.git \
  ./.claude/skills/humanities-writing-companion
```

### Claude Code 加载

Claude Code 启动时会自动扫描 `~/.claude/skills/` 和 `./.claude/skills/`。安装后说"我在写人文论文"或下方任意触发词即可激活。

### Claude Agent SDK 接入

`SKILL.md` 可直接加载到系统提示词中。skill 是纯文本，无运行时依赖。

### 触发词

**中文**：论文 · 写作 · 润色 · 改论文 · 帮我看看这一章 · 我手写我口 · 这个论证有没有问题 · 我写不下去了 · 审稿人会怎么攻击

**英文**："paper," "essay," "chapter," "dissertation," "argument," "thesis," "revise," "voice," "review my section," "stuck on writing," "devil's advocate"

即使随口说也触发："帮我看看这段话" · "take a look at this paragraph"

---

## 快速上手 · 三个典型场景

### 场景 1：新论文初次使用

对 Claude 说："我想写一篇关于 X 的论文。"

skill 进入 onboarding：确认引用格式、目标读者、已有写作样本，并初始化项目文件夹结构。

### 场景 2：修改已有章节

```
"帮我看看这一章"     → 模式 B（章节级审读）→ 四级反馈报告
"帮我改这段"         → 模式 A（段落级对话）→ 诊断 + 建议 + 理由
"我写不下去了"       → 模式 E（写作瓶颈）→ 五种解冻策略
```

### 场景 3：对抗 AI 腔调（双版本对照）

如果你的论文经过 AI 润色，但想恢复原始文风：

```
模式 F · 底稿修订 → 对照 AI 润色版与原始版本 → 保留改善 + 恢复声音
```

---

## 与同类工具的差异

| 工具 | 核心定位 | 与本 skill 的差异 |
|------|---------|------------------|
| **academic-research-skills (Imbad0202)** | 完整的实证研究流水线 | 流水线导向；本 skill 是写作声音导向。两者并用可全覆盖。 |
| **Jenni AI** | 实时自动续写 + 文献发现 | 本 skill 不做续写，专注思想对话 |
| **Paperpal** | 学术语言润色（理科为主） | 本 skill 是架构而非单点能力 |
| **Yomu AI** | Sourcely 文献引擎 + 段落反馈 | 本 skill 不做文献检索，假设作者自管（Zotero/Drive） |
| **Thesify** | Paper Digest + Purpose-Check | 本 skill 的模式 G 借鉴了 Purpose-Check 的设计哲学 |
| **HyperWrite Devil's Advocate** | 单点反方论证生成 | 本 skill 的魔鬼代言人是完整模式 + 抗谄媚 |

---

## 项目结构

```
humanities-writing-companion/
├── SKILL.md                          ← 主 skill 文件（英文，约 900 行）
├── SKILL.zh.md                       ← 中文镜像版
├── references/
│   ├── ai-trace-checklist.md         ← AI 痕迹排查清单（当前中文为主；英文翻译 TODO）
│   ├── project-management.md         ← 项目文件夹 + 版本管理规范
│   └── target-reader-profile-template.md  ← 目标读者档案模板
├── scripts/
│   ├── README.md                     ← 脚本使用说明
│   ├── ai-trace-scan.sh              ← AI 套话扫描（zsh）
│   ├── pending-checks.sh             ← 待办标记汇总（zsh）
│   └── citation-consistency.py       ← 引用格式一致性（Python 3）
├── README.md                         ← 英文 README
├── README.zh.md                      ← 本文件
├── LICENSE                           ← CC BY-NC 4.0
└── CITATION.cff                      ← 学术引用元数据
```

**双语状态**：SKILL.md 和 README 均有中英文版本。`references/` 文件和 `scripts/` 注释当前以中文为主，英文翻译待补。两种语言的触发词都能激活 skill（SKILL.md 的 description 字段同时处理两种语言）。

---

## 设计哲学

### "我手写我口"

学术严谨与个人表达不对立。"标准学术语体"往往意味着个性的消亡。skill 帮助作者用自己的声音说话，而不是把文字压入预制模具。

### 思想优先，格式其次

修改优先级：
1. 论证的力量
2. 概念的精确
3. 结构的有效
4. 表达的质量
5. 格式的规范

永远从上往下工作。不要在一个论证有根本缺陷的段落里纠结逗号。

### 工程化严谨，人文化表达

借鉴软件工程的最佳实践（版本管理、单元测试、code review），但服务于人文写作的特殊性。工程化不是把论文变成代码，而是让每次修改可追溯、论证质量可验证、写作过程可接续、问题分层处理。

---

## 引用本工作

如果你的研究使用了本 skill，请在方法论部分引用。

**BibTeX**:
```bibtex
@software{shen_humanities_writing_companion_2026,
  author       = {Shen, Cong},
  title        = {Humanities Writing Companion: A Claude Skill for Voice-Preserving Humanities Academic Writing},
  year         = {2026},
  url          = {https://github.com/tizzy916/claude-skill-humanities-writing-companion},
  version      = {3.0.0}
}
```

**纯文本署名**(用于 skill 元数据、页脚等):
```
Based on Humanities Writing Companion by Shen Cong
https://github.com/tizzy916/claude-skill-humanities-writing-companion
```

完整机读元数据见 [`CITATION.cff`](./CITATION.cff)(GitHub 的 "Cite this repository" 按钮会自动调用该文件)。

### 同时引用 Companion 工具

如果你在同一项目中同时使用了 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills),请同时引用两者。ARS 的署名格式(遵循 CC BY-NC 4.0):

```
Based on Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## 贡献

欢迎 issue 与 PR：
- 新的工作模式提议
- AI 痕迹排查清单的扩充
- 学科特异性示例（中世纪研究、艺术保护、民族音乐学等）
- 不同引用格式（APA / Chicago / MLA / GB/T 7714 / 期刊自定义）的支持
- `references/` 文件的英文翻译

详见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

---

## 关于作者 / About the Author

沈聪,中央美术学院实验艺术学院本科,清华大学科学史系硕士(导师 [胡翌霖](https://yilinhut.net/author/admin)),科技文创公司 [天与视界 TIANYU VISION](https://tianyu.art/) 创始人 & CEO。

本 skill 诞生于学位论文《技术自由主义》的写作过程——作者发现市面上的 AI 写作工具几乎都偏向"润色与平均化",而人文学术写作真正需要的是**反向的能力**:保护作者的学术声音、检验论证的严密性、扛住真实审稿人的对抗。所以做了这个 skill——不是替自己写,而是替自己读,在四个层级(基础严密性 / 论证展开 / 段落功能 / 句子措辞)分别提供一个真实人文学者会给出的批评。

📮 [GitHub @tizzy916](https://github.com/tizzy916) · shencong916@gmail.com · 论文、合作、纠错欢迎来信

---

## License

**[CC BY-NC 4.0](./LICENSE)**(知识共享 署名-非商业性使用 4.0 国际许可协议)——非商业用途自由使用、修改、分发,要求 attribution。

> ⚠️ **License change (v3.0.0, 2026-05-19)**:本项目从 **MIT 改为 CC BY-NC 4.0**。v2.1.0 及更早版本仍按 MIT 发布,保留原始商用权利(仅限这些特定版本)。从 v3.0.0 起,**未经单独授权禁止商业用途**。

### 商业用途 / Commercial Use

本 skill 采用 CC BY-NC 4.0 协议——**仅限非商业用途**(学术研究、教学、个人项目、开源衍生、机构内部研究流程)。

如需商业使用——嵌入付费产品、使用本 skill 提供付费咨询或编辑服务、商业 SaaS 集成、代客商业写作服务——请联系作者获取商业 license:

📮 **shencong916@gmail.com**(沈聪 · 天与视界 TIANYU VISION)

作者保留按个案授予商业 license 的权利。**在学术发表中引用本 skill 不受 license 层级影响,始终允许。**

---

## 致谢

本 skill 的方法论灵感与学术依据：

- Christou, P. A. (2026). [Reconfiguring Reflexivity in the Era of AI](https://journals.sagepub.com/doi/10.1177/10778004261445052). *Qualitative Inquiry*.
- Wiles, F. (2025). [Recursive Cognition in Practice](https://journals.sagepub.com/doi/10.1177/16094069251381709). *International Journal of Qualitative Methods*.
- Panke, S. (2025). [How Can (A)I Research This?](https://journals.sagepub.com/doi/10.1177/00224871251325065).
- Foucault, M. (1984). What is Enlightenment? — "对当下的诊断"作为方法论传统
- Stiegler, B. (2013). *What Makes Life Worth Living: On Pharmacology* — "批判药理学"

部分设计模式参考：

- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 本 skill 作为互补的上游流水线；他们的 reviewer 模块中的 Concession Threshold 模式启发了模式 D 的"让步前最低标准"
- [Voice DNA + Audience Profile 模式](https://aiblewmymind.substack.com/p/claude-skills-ai-write-like-you) — 启发了写作风格档案与目标读者档案的配对设计
- [Thesify](https://www.thesify.ai/) Purpose-Check — 启发了模式 G 盲读核对
