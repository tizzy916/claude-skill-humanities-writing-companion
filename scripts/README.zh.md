# scripts/ · 工程化辅助工具

> **Language / 语言**：[English](README.md) · **中文（当前）**

> 本目录的脚本对应 SKILL.md 中"工程化严谨"原则的具体落地——
> AI 自觉性是软规范，脚本是硬机制。两者结合，才能真正避免漂移和疏忽。

**v4.0 起新增引用工具链**(citation toolchain):格式转换 + Crossref 核查。

---

## 五个脚本

### 1. `ai-trace-scan.sh` · AI 痕迹与学术八股扫描

**用途**：扫描文档中 `references/ai-trace-checklist.md` 列出的高频套话，以及连接词的过度堆砌。

**用法**：
```bash
# 单文件扫描
./scripts/ai-trace-scan.sh path/to/chapter.md

# 整个论文项目目录扫描
./scripts/ai-trace-scan.sh path/to/paper/
```

**何时运行**：
- 模式 F（底稿修订）每章修订完成后
- 模式 B（章节级审读）执行前
- 完稿前的最终检查

**输出**：每条匹配的行号 + 行内容 + 频次警告

**注意**：扫描器只是"找出嫌疑"——是否真的需要改，仍需作者判断（有些"套话"在特定语境下是有意识的选择）。

---

### 2. `pending-checks.sh` · 待办标记汇总

**用途**：提取项目中所有未完成的标记（待核对的引用、待讨论的论证、AI 草稿等）。

**用法**：
```bash
# 整个项目目录
./scripts/pending-checks.sh path/to/paper/

# 单文件
./scripts/pending-checks.sh path/to/chapter.md
```

**扫描的标记**：
| 标记 | 含义 | 处理优先级 |
|------|------|-----------|
| `[待核对]` | AI 凭记忆引用 / 未核实事实 | 🔴 投稿前必须清零 |
| `❓ 待讨论` | 需要作者决定的论证选择 | 🟡 推进时处理 |
| `[AI 草稿，待作者审阅]` | AI 起草未审阅的段落 | 🟢 审阅后删除标记 |
| `>>>` | AI 起草时不确定的地方 | 🔵 起草后立即处理 |
| `[作者微调]` | 作者对 AI 建议的二次调整 | 🟣 回写到写作风格档案 |

**何时运行**：
- 每次对话开始时（了解还有什么未完成）
- 投稿前的最终清单
- 跨对话恢复时的状态摘要

---

### 3. `citation-consistency.py` · 引用格式一致性扫描

**用途**：检查全文引用格式的一致性（不是规范性）。

**用法**：
```bash
python3 scripts/citation-consistency.py path/to/paper/main.md
```

**扫描项**：
1. 括号类型混用（半角 `()` vs 全角 `（）`）
2. 引用内逗号混用（`,` vs `，`）
3. 多作者连接词不统一（`&` / `and` / `与` / `和` / `、`）
4. 同一文献被引用时姓名形式不一致（中文译名 vs 英文原姓）
5. 页码格式不统一（`p. X` / `第 X 页` 等）

**何时运行**：
- 完成一章后的局部一致性检查
- 投稿前的全文统一性核验
- 引入新文献后的回归检查

**重要边界**：
- 此脚本只检查"是否一致"，不检查"是否符合 APA / Chicago / GB/T 7714"
- 规范性检查请对照 `_writing-config/引用格式速查.md` 手动进行
- 启发式正则扫描可能有少量误报，结果需要人工复核

---

### 4. `citation-format-convert.py` · 引用格式转换(v4.0 新增)

**用途**:把 BibTeX 文献库转换为四种主流学术引用格式之一(用于投稿前的参考文献表准备)。

**支持的格式**:
- **Chicago Author-Date** —— 历史、人文学科最常用
- **MLA 9** —— 文学、语言学最常用
- **APA 7** —— 教育、心理、部分社科最常用
- **GB/T 7714 顺序编码制** —— 中文期刊国标

**用法**:
```bash
# 输出到 stdout
python3 scripts/citation-format-convert.py refs.bib --to chicago

# 输出到文件
python3 scripts/citation-format-convert.py refs.bib --to apa --out refs-apa.txt

# 按作者排序(默认)、按年份、按 key、按输入顺序
python3 scripts/citation-format-convert.py refs.bib --to mla --sort year
```

**何时运行**:
- 投稿前准备最终参考文献表(目标期刊有特定格式要求时)
- 在投稿同一论文到不同期刊间切换时(快速重新生成)
- 模式 K (AI 使用披露) 输出前

**支持的 BibTeX 类型**:`@book`, `@article`, `@incollection`, `@inbook`, `@inproceedings`, `@thesis`, `@phdthesis`

**重要边界**:
- **不是 BibLaTeX / CSL 的替代品**——后者支持每个期刊的特异性变体,如果你的工具链可以用 BibLaTeX,优先用那个
- 此脚本服务于"飞行中"的场景:你手上有 BibTeX 库,想立即生成一份清单为某期刊准备
- **每种格式有大量微妙规则与期刊特异性变体**——输出永远要对照目标期刊的 style guide 核对,把输出当作起草而非定稿
- 仅处理参考文献**表**(reference list),不处理散文**内**的 inline 引用(那需要理解文档结构)

---

### 5. `citation-verify.py` · 引用真实性核查(v4.0 新增)

**用途**:扫描 Markdown 草稿中的所有 inline 引用,逐一在 Crossref 公共 API 中核查存在性。**主要用于捕捉 LLM 引用幻觉**(AI 凭"记忆"编造的假期刊文章引用)。

**用法**:
```bash
# 人类可读报告
python3 scripts/citation-verify.py path/to/draft.md

# 静默模式 + JSON 输出(用于 CI / 程序处理)
python3 scripts/citation-verify.py path/to/draft.md --quiet --json
```

**核查结果分三类**:
- **✓ FOUND**:Crossref 有匹配项(高置信度 ≥ 0.85)——通常可信
- **⚠ FUZZY_MATCH**:有近似匹配但不完全(0.5-0.85)——可能拼写错、年份错、或不同的同名作者著作,需要复核
- **✗ NOT_FOUND**:Crossref 无匹配——**警惕**,但**未必是幻觉**(见下方边界)

**何时运行**:
- 模式 B (章节级审读) 之后,模式 G (盲读核对) 之前
- 任何 AI 起草的章节(模式 C 输出后)
- 投稿前的最终合规检查

**重要边界**:
- **Crossref 不索引一切**。许多人文学科作品(尤其:小型大学出版社的专著、未翻译的外文著作、学位论文、档案史料、古典文献)**不在 Crossref 中**——对这些作品,"NOT_FOUND" 是预期结果,**不**代表问题
- 本脚本擅长的是捕捉 **LLM 幻觉的期刊文章引用**——那是 Crossref 覆盖最好的地方
- 对专著、档案、古典学引用,正确的工具是 `[VERIFY]` / `[待核对]` 标记协议(参见 SKILL.md),而非本脚本
- 网络请求,礼貌地限速到 1 次/秒以保护 Crossref 公益服务

---

## 安装与权限

首次使用前给 shell 脚本加执行权限：

```bash
chmod +x scripts/ai-trace-scan.sh scripts/pending-checks.sh
```

Python 脚本无需特殊安装——只依赖 Python 3 标准库。

---

## 与 SKILL.md 的对应关系

| 脚本 | 对应 SKILL.md 章节 |
|------|-------------------|
| `ai-trace-scan.sh` | 文风深层理解 · 未审视表达模式排查 |
| `pending-checks.sh` | 反馈报告 · 四级分类 + 反漂移协议 |
| `citation-consistency.py` | 多语言学术写作 · 引用格式一致性验证 + 系统性验证 · 引用完整性验证 |
| `citation-format-convert.py` | 模式 K (AI 使用披露) 前的格式准备 / 多期刊投稿切换 |
| `citation-verify.py` | 系统性验证 · 引用真实性 / `[VERIFY]` 标记协议的自动化补充 |

---

## 设计原则

1. **零依赖优先**：shell 脚本用 zsh + grep，Python 脚本只用标准库
2. **失败安全**：不存在的目录、空匹配等都返回友好提示而非崩溃
3. **可读输出**：直接给人看的报告，不需要额外解析
4. **诚实的边界**：每个脚本都明确说明"做什么 / 不做什么"——避免给作者"全勾了就没问题"的虚假确定感
