# academic-writer · Claude Skill for 人文社科学术写作

> A Claude Code / Claude Agent SDK skill that turns Claude into a thinking partner
> for humanities and social-science academic writing — not a polishing tool,
> but an interlocutor that engages with your arguments, concepts, and voice.

**人文社科学术写作的思想对话伙伴** —— 不只是润色工具，而是一个能进入作者思想内部的对话者：质疑论证前提、辨析概念精度、批判结构有效性、保持作者文风。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Skill format: Claude Code](https://img.shields.io/badge/skill-Claude%20Code-orange)](https://docs.claude.com/en/docs/claude-code)
[![Status: stable](https://img.shields.io/badge/status-stable-green)]()

---

## 它解决什么问题

主流 AI 写作工具（Jenni、Paperpal、Yomu、Grammarly 等）擅长**单点能力**——句子润色、引用检索、自动续写。但它们对人文社科学术写作有结构性不匹配：

- **润色 ≠ 思想对话**：人文论文的核心是论证而非语法
- **AI 腔调侵蚀作者文风**：均匀长句、客观化表达、过度对仗——把每个学者写成同一个"标准学术人"
- **审稿人式批判缺位**：通用工具不会问"你的核心概念有真正的解释力吗"
- **AI 谄媚**：作者一推回，AI 立刻让步——这违背了批判性反馈的本质
- **引用幻觉**：LLM 凭记忆引用文献，软规范挡不住

本 skill 把这些缺口补上，把 Claude 从"润色匠"升级为**思想对话伙伴 + 工程化基础设施**。

---

## 核心特性

### 1. 四层批判模式（不是单一润色）

```
第一层 · 基底批判 — "这篇论文在学术上成立吗？"
第二层 · 结构批判 — "论证是怎样展开的？展开得好吗？"
第三层 · 段落批判 — "这一段在做什么？做好了吗？"
第四层 · 语句批判 — "这句话说对了吗？说好了吗？"
```

**层次联动规则**：上层未解决时不在下层花大力气。

### 2. 魔鬼代言人 + 抗谄媚机制

模拟三种审稿人 + 一个善意困惑读者：
- 审稿人 A · 理论苛刻型
- 审稿人 B · 历史实证型
- 审稿人 C · 方法论质疑型
- 读者 D · 善意困惑型（**独到设计**：能让善意读者困惑的地方就是论证薄弱处）

**抗谄媚硬机制**：作者推回质疑时，必须满足 5 项实质条件中的 ≥2 项才让步——防止 AI 在情绪压力下提前软化。

### 3. 文风深层学习与保持（"我手写我口"）

不只是句式偏好，还包括：
- **论证节奏**（线性 / 螺旋 / 张弛）
- **学术姿态**（批判性继承 / 对话性推进）
- **引用的修辞功能**（权威锚点 / 批判靶标 / 对话接口 / 叙事性 / 概念工具）
- **AI 痕迹排查清单**（六类未审视表达模式 ≠ AI 套话 ≠ 学术八股）

### 4. ADHD 友好的交互设计

- 反馈分批：每轮 3-5 项最多
- 快速胜利优先：先给一两个容易执行的修改
- 跳跃跟随：作者突然换话题时不强制"先做完上一项"
- 重新定向点：长对话中定期给"我们现在在哪"的摘要

### 5. 自反性写作支持（独到模块）

如果作者的研究本身涉及人-AI 协作（autoethnography of AI-assisted writing），本 skill 提供六类"反思时刻"分类：

🔄 方向转变 / 🚫 拒绝 / 🎭 声音冲突 / 🔧 工具依赖 / 💡 意外洞见 / 🤖 AI 痕迹觉察

**学术依据**（在论文里可直接引用）：
- Christou (2026). *Reconfiguring Reflexivity in the Era of AI*. *Qualitative Inquiry*.
- Wiles (2025). *Recursive Cognition in Practice*. *International Journal of Qualitative Methods*.
- Panke (2025). *How Can (A)I Research This? An Autoethnographic Exploration of Generative AI*.

### 6. 工程化基础设施

借鉴软件工程的最佳实践：
- **版本管理**：小版本 = commit / 大版本 = release / `_drafts/` = feature branch
- **修改日志**：每次修改记录 diff + reason（像 git commit message）
- **反馈报告**：Blocker / Major / Minor / Question 四级（借鉴 code review）
- **系统性验证清单**：论证完整性 / 概念一致性 / 引用完整性 / 文风一致性

### 7. 多语言学术写作（中英混合）

区分**规范性问题**（必须统一）和**风格性特征**（应当保留）：
- 括号、逗号、连接词、人名形式 → 必须全文统一（规范）
- 引入学者时给详细身份介绍 / 保留外文原文不译（如 technê） → 应保留（风格）

### 8. 七个工作模式（不是单一对话模式）

- **模式 A**：段落级对话
- **模式 B**：章节级审读
- **模式 C**：构思 → 新内容写作（含协作式起草协议）
- **模式 D**：魔鬼代言人
- **模式 E**：写作瓶颈辅助（五种解冻策略）
- **模式 F**：底稿修订（双版本对照，对抗 AI 腔调）
- **模式 G**：盲读核对（机械检查"承诺-兑现"）

### 9. 工程化辅助脚本

[`scripts/`](./scripts) 提供三个零依赖工具：

| 脚本 | 用途 |
|------|------|
| `ai-trace-scan.sh` | 扫描套话与连接词堆砌 |
| `pending-checks.sh` | 汇总所有 `[待核对]` / `❓ 待讨论` / `[AI 草稿]` 标记 |
| `citation-consistency.py` | 引用格式一致性扫描（括号 / 逗号 / 连接词 / 中英姓名 / 页码） |

---

## 与同类工具的差异

| 工具 | 核心定位 | 与本 skill 的差异 |
|------|----------|-------------------|
| **Jenni AI** | 实时自动续写 + 文献发现 | 本 skill 不做续写，专注思想对话 |
| **Paperpal** | 学术语言润色（理科为主） | 本 skill 是架构而非单点能力 |
| **Yomu AI** | Sourcely 文献引擎 + 段落反馈 | 本 skill 不做文献检索，假设作者自管（Zotero/Drive） |
| **Thesify** | Paper Digest + Purpose-Check | 本 skill 的模式 G 借鉴了 Purpose-Check 的设计哲学 |
| **HyperWrite Devil's Advocate** | 单点反方论证生成 | 本 skill 的魔鬼代言人是完整模式 |

---

## 安装

### 作为 Claude Code skill 安装

```bash
# 克隆到 Claude Code skills 目录
git clone https://github.com/tizzy916/claude-skill-academic-writer.git \
  ~/.claude/skills/academic-writer

# 给 shell 脚本可执行权限
chmod +x ~/.claude/skills/academic-writer/scripts/*.sh
```

或者作为项目级 skill（仅当前 vault / project 可用）：

```bash
git clone https://github.com/tizzy916/claude-skill-academic-writer.git \
  ./.claude/skills/academic-writer
```

### Claude Code 加载

Claude Code 启动时会自动扫描 `~/.claude/skills/` 和 `./.claude/skills/`。安装后说"我在写论文"或类似关键词即可触发。

### Claude Agent SDK 接入

`SKILL.md` 也可作为系统提示词的一部分加载到 Agent SDK 中。skill 是纯文本，无需运行时依赖。

---

## 快速上手 · 三个典型场景

### 场景 1：新论文初次使用

直接对 Claude 说："我想写一篇关于 X 的论文。"

skill 会自动进入 onboarding：确认引用格式、目标读者、已有写作样本，并初始化项目文件夹结构。

### 场景 2：修改已有章节

```
帮我看看这一章 → 模式 B 章节级审读 → 反馈报告（4 级分类）
帮我改这段   → 模式 A 段落级对话 → 诊断 + 建议 + 理由
我写不下去了 → 模式 E 写作瓶颈辅助 → 五种解冻策略
```

### 场景 3：对抗 AI 腔调（双版本对照）

如果你的论文经过 AI 润色，但你想恢复原始文风：

```
模式 F · 底稿修订 → 对照 AI 润色版与原始版本 → 保留改善 + 恢复声音
```

---

## 项目结构

```
academic-writer/
├── SKILL.md                          ← 主 skill 文件（约 1100 行）
├── references/
│   ├── ai-trace-checklist.md         ← AI 痕迹排查清单
│   ├── project-management.md         ← 项目文件夹规范 + 版本管理
│   └── target-reader-profile-template.md  ← 目标读者档案模板
├── scripts/
│   ├── README.md                     ← 脚本使用说明
│   ├── ai-trace-scan.sh              ← AI 套话扫描（zsh）
│   ├── pending-checks.sh             ← 待办标记汇总（zsh）
│   └── citation-consistency.py       ← 引用格式一致性（Python 3）
├── README.md                         ← 本文件
├── LICENSE                           ← MIT
└── CITATION.cff                      ← 学术引用元数据
```

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

借鉴软件工程的最佳实践（版本管理、单元测试、code review），但服务于人文写作的特殊性。工程化不是把论文变成代码，而是让每次修改可追溯、论证质量可验证、写作过程可接续。

---

## 引用本工作

如果你的研究使用了本 skill，可在方法论部分引用：

```bibtex
@software{academic_writer_skill_2026,
  author       = {tizzy916},
  title        = {academic-writer: A Claude Skill for Humanities and Social-Science Academic Writing},
  year         = {2026},
  url          = {https://github.com/tizzy916/claude-skill-academic-writer},
  version      = {1.0.0}
}
```

或参见 [`CITATION.cff`](./CITATION.cff)。

---

## 贡献

欢迎 issue 与 PR：
- 新的工作模式提议
- AI 痕迹排查清单的扩充
- 跨学科示例
- 不同引用格式（APA / Chicago / MLA / GB-T 7714 / 期刊自定义）的支持

---

## License

[MIT](./LICENSE) — 自由使用、修改、分发。

---

## 致谢

本 skill 的方法论灵感与学术依据：

- Christou, P. A. (2026). [Reconfiguring Reflexivity in the Era of AI](https://journals.sagepub.com/doi/10.1177/10778004261445052). *Qualitative Inquiry*.
- Wiles, F. (2025). [Recursive Cognition in Practice](https://journals.sagepub.com/doi/10.1177/16094069251381709). *International Journal of Qualitative Methods*.
- Panke, S. (2025). [How Can (A)I Research This?](https://journals.sagepub.com/doi/10.1177/00224871251325065).
- Foucault, M. (1984). What is Enlightenment? — "对当下的诊断"作为方法论传统
- Stiegler, B. (2013). *What Makes Life Worth Living: On Pharmacology* — "批判药理学"

部分设计模式参考：
- Imbad0202 / [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — Concession Threshold 抗谄媚机制启发了模式 D 的"让步前最低标准"
- [Voice DNA + Audience Profile 模式](https://aiblewmymind.substack.com/p/claude-skills-ai-write-like-you) — 启发了写作风格档案与目标读者档案的配对设计
- [Thesify](https://www.thesify.ai/) Purpose-Check — 启发了模式 G 盲读核对
