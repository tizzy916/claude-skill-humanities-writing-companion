# Cross-Domain Testing · Getting the Skill Battle-Tested in Your Field

> **Language / 语言**: **English (current)** · [中文](cross-domain-testing.zh.md)

> The skill currently grew out of one specific humanities project (in art history / philosophy / digital cultural studies). For it to truly become a **general-purpose humanities and social-science academic-writing skill**, it needs real-world feedback across different disciplines and different kinds of writing. This document explains: how you can help, and how to help most usefully.

---

## What kind of feedback we need most

### 🥇 Misfit reports (most valuable)

If you use the skill in your own discipline / paper project and find that some module **doesn't work / works poorly / gives advice that violates your discipline's conventions**, please tell us. This is far more important than "I found it useful."

Concretely, **please report in detail** if any of the following happens:

- The skill's feedback is wrong for your discipline (e.g., it suggests a mode of argument your discipline doesn't accept)
- A mode is simply unusable for your kind of writing (e.g., Mode G blind-read checking doesn't apply to empirical research)
- A "cliché" on the AI-trace checklist is in fact legitimate usage in your discipline
- The concept-introduction rules conflict with your discipline's conventions
- The citation format is incompatible with your target journal

### 🥈 Discipline-specialization proposals

If, in the course of using it, you find that some discipline needs a capability the skill doesn't cover, you can propose:

- A new critical dimension (e.g., the "participant statement vs. researcher analysis" register distinction for ethnographic research)
- A discipline-specific AI trace (e.g., cliché patterns like "significant positive correlation" in economics papers)
- A discipline-specific working mode (e.g., a "case–rule–application" structure check for legal papers)
- A discipline-specific script tool (e.g., a statistical-language consistency scan)

### 🥉 Success stories

A report that the skill worked well on your paper is also valuable — but please say **in what scenario / what specific problem it solved**, rather than a vague "it's great." Concrete success stories help other authors judge whether the skill fits them.

---

## Typical testing scenarios, grouped by discipline

> Below are suggested "entry points for testing" in several disciplines. If your discipline isn't on the list, you can design your own test scenarios based on this structure.

### History

**Scenarios most likely to expose problems**:
- Source handling (citation conventions for primary / secondary sources)
- Maintaining period context (avoiding anachronism — applying contemporary categories to historical actors)
- Stress-testing causal narrative (has temporal sequence been smuggled in as causation?)

**Suggested testing method**:
1. Take a paragraph from an already-published history paper and have the skill run Mode A paragraph-level dialogue
2. See whether the skill identifies the register difference between "narrative source material vs. analytical exposition"
3. See whether, when flagging a problem, the skill understands history's notion of the "chain of evidence"

**Known potential misfit**:
- The skill's current "foundation critique" layer (scholarly contribution / conceptual explanatory power) has a philosophical tilt, and may misjudge history's "newly discovered source" type of contribution

### Sociology / Anthropology (ethnographic strand)

**Scenarios most likely to expose problems**:
- Transcribing field notes into analytical text
- Reflexive writing (researcher reflexivity) — overlaps with the skill's reflexive-writing module
- Ethical handling of participant quotations (anonymization / pseudonyms / quotation permissions)

**Suggested testing method**:
1. Take a draft containing field material and have the skill run Mode B chapter-level review
2. See whether the skill distinguishes the two registers of "participant statement" and "researcher analysis"
3. Is the reflexive-writing module useful for anthropology's reflexivity tradition?

**Known potential misfit**:
- The skill's current "lineage-visibility principle" is a relay metaphor from the philosophical/theoretical tradition, and may not directly apply to the "field accumulation" mode of transmission in ethnography

### Literary studies / Comparative literature

**Scenarios most likely to expose problems**:
- The citation density of close reading
- Handling multilingual texts (dual citation of original + translation)
- The boundary between aesthetic judgment and argument

**Suggested testing method**:
1. Take a close-reading paragraph and have the skill assess whether its citation density is too high
2. See whether the skill handles multilingual writing (Chinese-English / Chinese-French / Chinese-Japanese, etc.) sensibly
3. Have the skill run Mode D devil's advocate, and see whether it can simulate a disciplinarily literate literary reviewer

**Known potential misfit**:
- The skill's current distinction between "analytical exposition" and "aesthetic exposition" isn't fine-grained enough — in literary studies, aesthetic judgment is itself legitimate exposition

### Philosophy (analytic tradition)

**Scenarios most likely to expose problems**:
- Formalizing arguments (making premises / inferences / conclusions explicit)
- The precision of conceptual analysis
- Handling counterexamples

**Suggested testing method**:
1. Take the core argumentative passage of an analytic philosophy paper and have the skill run the four-layer critique
2. See whether the skill's "conceptual distinction" layer meets analytic philosophy's demand for precision
3. See whether the skill identifies the informal-logic leaps of "missing steps"

**Known potential misfit**:
- The skill tends toward "dialogic advancement" (acknowledge predecessors' contributions, then critique), whereas the analytic tradition tends more toward "directly assessing the validity of the argument" — these two stances may conflict

### Law

**Scenarios most likely to expose problems**:
- Case-citation conventions (citation formats differ enormously across jurisdictions)
- The "rule–application" structure of legal reasoning
- The relative weight of doctrine vs. case-law citation

**Suggested testing method**:
1. Take an argument from a law paper and have the skill check whether its "rule identification → case analysis → rule application" structure is complete
2. See whether the skill distinguishes "legislative-purpose argument" from "textual-interpretation argument"

**Known potential misfit**:
- The skill's current citation-verification mechanism (the `[待核对]` hard marker) may not be fine-grained enough for legal case citation — a single case may carry several layers of citation requirement

### Economics / Policy studies (the boundary of the humanities and social sciences)

**Scenarios most likely to expose problems**:
- The methods statement of empirical research
- Connecting data visualizations to the main text
- The wording of policy recommendations (normative vs. descriptive)

**Suggested testing method**:
1. Have the skill process a passage of body text containing econometric results, and see whether it understands the reasonable way to express "significance"
2. See whether, in a policy-recommendation section, the skill can distinguish "empirical conclusions" from "normative claims"

**Known potential misfit**:
- The skill's current "thought-first" orientation diverges from empirical research — the core of empirical research may be data and method, not argument

### Communication studies / Media studies

**Scenarios most likely to expose problems**:
- Integrating cross-disciplinary theoretical resources (close to the skill's "theory relay" design)
- The dual-track unfolding of "concrete case + theoretical analysis" in media studies

**Suggested testing method**:
1. Take a "case + theory" paragraph from media studies and have the skill assess whether the two are balanced in proportion
2. See whether the skill's "case-analysis chapter" checklist covers the concerns of media studies

**Known potential misfit**:
- Few. This discipline is the closest to the skill's "native soil"

---

## Adaptation testing for different kinds of writing

### Degree theses (master's / doctoral)

This is exactly the type the skill assumes by default — long-form / multi-chapter / written over many months.

**Focus of testing**: cross-chapter argumentative cumulativeness, cross-session resumption, version management.

### Journal submissions (short-form)

The skill may be "over-engineered" for short-form writing — an 8,000-word paper doesn't need a reference index, a revision log, or version archiving.

**Focus of testing**: Can the skill be used in a "lightweight" way in short-form scenarios? Which modules can be skipped?

### Conference papers / Talks

The orality and time limits of conference papers are dimensions the skill hasn't considered.

**Focus of testing**: Have the skill handle a piece of writing in the dual form of "conference paper + talk script," and see whether it can distinguish the two contexts.

### Coursework (teaching scenario)

In a teaching scenario, the author is a student and the paper is the object being graded. This is a different relationship from an independent scholar writing a paper.

**Focus of testing**: Can the skill distinguish "the competence a student needs to display" from "the writing of a mature scholar"? The former may require deliberately showing off one's skill; the latter tends to hide the effort.

### Public writing / Academic blogging

The academic blog sits between "rigorous scholarship" and "readability."

**Focus of testing**: In this boundary scenario, which side does the skill lean toward? It defaults to rigor — which may make an academic blog read as too heavy.

---

## Test-report template

Please use the following template to submit a cross-domain test report (open a new topic under [Discussions / Show and tell](https://github.com/tizzy916/claude-skill-humanities-writing-companion/discussions/categories/show-and-tell)):

```markdown
# 跨学科测试报告 · [你的学科 / 写作类型]

## 测试上下文

- **学科**：[历史学 / 社会学 / 哲学 / ...]
- **写作类型**：[学位论文 / 期刊投稿 / 会议论文 / ...]
- **写作语言**：[中文 / 英文 / 中英混合 / 其他]
- **使用 skill 的时长**：[一次性试用 / 数周 / 数月]
- **Claude 模型**：[4.5 Sonnet / 4.7 Sonnet / Opus 4.7 / ...]

## 测试目的

我希望 skill 帮我做什么？

## 工作良好的部分

- [模块名]：具体场景 + 实际帮助
- ...

## 水土不服的部分

> 这一节是最有价值的。请尽量具体。

- [模块名]：具体场景 + 为什么不适用 + 在你的学科里"对的做法"应该是什么
- ...

## 建议

- 是改进现有模块？
- 还是新增学科特化模式？
- 还是 fork 出一个学科特化版本？

## 你愿意贡献吗？

- 我可以提 PR
- 我希望维护者来改
- 我只是报告，不做后续

## 其他

任何上下文、相关学科文献、可参照的同类工具
```

---

## What maintainers commit to in return

After you submit a cross-domain test report, you can expect:

- **Within 48 hours**: a maintainer will read the report through and give initial feedback (not necessarily "I'll change it," but always "I've seen it + here's what I think")
- **If it's a misfit report**: the maintainer will judge whether this is "something that should be absorbed into the main branch" or "something that should be a discipline-specialization extension," and explain the reasoning
- **If it's a disagreement at the level of design philosophy**: the maintainer will say openly "I agree / I disagree + why" — this kind of disagreement is the norm in the skill's evolution and will not be ducked

---

## A not-entirely-disinterested reminder

I have to say something counterintuitive — this skill's design is **not neutral**. It has positions (thought over format / engineering rigor / voice preservation / anti-sycophancy / reflexive self-awareness), and these positions may be wholly inapplicable in certain disciplines / certain writing traditions.

Cross-domain testing is not meant to make the skill "neutral." Its purpose is to:

1. Let the skill know **its own boundaries** — which disciplines are its comfort zone and which are not
2. Let the skill **do better within its own boundaries**
3. Let communities in disciplines beyond those boundaries **fork their own versions**

If testing in your discipline reveals that the skill is wholly unsuited to it, **that in itself is a valuable finding** — it tells everyone who wants to use the skill: "this discipline, please detour around." This kind of honest boundary-drawing is more responsible than pretending to be "general-purpose."

---

*This document will evolve as test reports accumulate. If your discipline already has a high-quality test report, you're welcome to add a "known to fit / known not to fit" summary to the document.*
