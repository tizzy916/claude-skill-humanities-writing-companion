# Humanities Writing Companion · 人文学科写作伙伴

> A Claude Code / Claude Agent SDK skill for humanities scholars whose primary deliverable is a long-form argumentative text — history, philosophy, literature, cultural studies, art history, religious studies, classics.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Skill format: Claude Code](https://img.shields.io/badge/skill-Claude%20Code-orange)](https://docs.claude.com/en/docs/claude-code)
[![Status: stable](https://img.shields.io/badge/status-stable-green)]()

**[中文版 README](./README.zh.md)** · **[Skill source · English](./SKILL.md)** · **[Skill source · 中文](./SKILL.zh.md)**

---

## Positioning

This skill is the **humanities-side companion** for academic writing: voice-preserving assistance for fields where prose IS the argument — history, philosophy, literature, cultural studies, art history, religious studies, classics. It is **not** a research pipeline. For empirical-research workflows, see the [Companion section](#companion-academic-research-skills) below.

---

## Companion: academic-research-skills

This skill is designed as the **humanities-side complement** to [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (ARS), the comprehensive empirical-research pipeline suite. The two are intended to be used together.

### Division of labor

```
academic-research-skills (Imbad0202)        humanities-writing-companion (this)
─────────────────────────────────────       ────────────────────────────────
empirical research pipeline                 humanities writing voice
data → results → write-up                   conception → argument → prose
citation hallucination audit                voice preservation + style learning
PRISMA / RAISE / Material Passport          devil's advocate + reflexive writing
```

A typical workflow: use ARS for literature discovery, citation auditing, methodology compliance, and pipeline orchestration; then switch to this skill when you sit down to write the humanities chapter where argumentative prose IS the deliverable.

### Design lineage

This skill borrows specific design patterns from ARS, with attribution:

- **Concession Threshold pattern** (from ARS's reviewer module) → inspired Mode D's "minimum standard before conceding" (anti-sycophancy)
- The companion-skill framing itself follows ARS's own structural example (`Companion: Experiment Agent`)

> Based on **Academic Research Skills** by Cheng-I Wu (吳政宜) — https://github.com/Imbad0202/academic-research-skills (CC BY-NC 4.0)

### Licensing note

ARS is licensed under **CC BY-NC 4.0** (non-commercial); this skill is **MIT**. Users combining the two should comply with the more restrictive ARS license when using the combined toolchain commercially.

---

## What this skill takes seriously

Three things generic AI writing tools do not handle for humanities:

**1. Voice preservation is a core scholarly value, not stylistic decoration.**
In humanities, the author's voice carries epistemic weight: it signals which intellectual tradition the author writes from, which interlocutors they take seriously, which moves are theirs and which are borrowed. A paper polished into "standard academic English" loses this signal. This skill helps you write more like yourself, not less.

**2. Argument and prose are inseparable.**
In empirical research, you can have a perfect experiment ruined by bad writing. In humanities, the writing IS the argument — a slack sentence, a vague concept, an unwarranted transition is an argumentative failure. This skill works at the level of argument-through-prose.

**3. The reviewer is real and adversarial.**
Humanities reviewers are not gentle. A theoretical concept will be tested for sharpness; a historical claim will be tested for evidence; a philosophical argument will be tested for the strongest counter. This skill simulates that adversary internally so the paper meets it before submission.

---

## A typical interaction

```
You: 帮我看看这段。我在论福柯的全景敞视主义如何延伸到数字平台。

[skill reads the paragraph + your style profile]

Companion:
  I notice three things, in order of priority.

  🔴 Foundation: you're using "全景敞视" as a metaphor for platform 
     surveillance, but Foucault's original concept turns on architecture 
     producing a specific subject-position. Platforms produce a different 
     subject (data subject, not body in a cell). You may want to either 
     (a) name the analogy as analogy and discuss the difference, or 
     (b) borrow Zuboff's "instrumentarian power" which fits the data case 
     more cleanly. Which direction do you want to go?

  🟡 Argument: paragraph 2 jumps from "platforms collect data" to "this 
     constitutes surveillance" without the middle step about visibility-
     as-power. A friendly reader will not follow.

  🟢 Voice: your style profile has "first-person with em-dash insertion." 
     Paragraph 3 starts with "本文认为…" which reads like cliché. Want to 
     restore the first-person?

You: 走方向 (b). 改吧。

[skill produces revision; you keep the version that sounds like you]
```

This is what "thinking partner, not polishing tool" means in practice.

---

## Core features

### Four-layer critique (not single-axis polishing)

```
Layer 1 · Foundation   "Does this paper hold up scholarly?"
Layer 2 · Structure    "How is the argument unfolding?"
Layer 3 · Paragraph    "What is this paragraph doing?"
Layer 4 · Sentence     "Is this sentence right? Well-said?"
```

**Strict top-down rule**: do not exert effort at lower layers while upper layers are unresolved.

### Devil's advocate with anti-sycophancy

Simulates three reviewers + one well-intentioned reader:
- Reviewer A · Theoretically demanding
- Reviewer B · Historically empirical
- Reviewer C · Methodologically skeptical
- Reader D · Well-intentioned but confused (**distinctive design**: places where a friendly reader gets confused are weak points in the argument)

**Anti-sycophancy hard rule**: when the author pushes back on a challenge, the AI must see at least 2 of 5 substantive conditions met before conceding — prevents premature softening under emotional pressure.

### Deep voice learning and preservation ("My hand writes my voice")

Not just sentence preferences. Also:
- **Argumentative rhythm** (linear / spiral / variable-tempo)
- **Scholarly posture** (critical inheritance / dialogical advance)
- **Rhetorical function of citation** (authority anchor / critical target / dialogue interface / narrative / conceptual tool)
- **AI-trace checklist** (8 categories of unexamined patterns ≠ AI cliché ≠ scholarly cliché)

### Discipline-specific dimensions

Different chapter types get different critique strategies:
- Historical narrative · anachronism, counterfactual stress, source handling
- Philosophical argument · conceptual derivation, cross-theoretical transplantation, strongest objection
- Literary criticism · close reading vs. interpretation, genre awareness, form and meaning
- Cultural studies · power-knowledge framing, positionality, generalization range
- Art history · description vs. interpretation, provenance, reception
- Religious studies / classics · source-language rigor, tradition awareness, insider-outsider position
- Case analysis (cross-disciplinary)

### ADHD-friendly interaction

- Feedback batched 3-5 per round
- Quick wins first
- Topic-jump support (a jump may be an insight signal)
- Pomodoro-friendly task units
- Reorientation summaries every 4-5 turns

### Reflexive writing support (distinctive module)

If your research itself involves human-AI collaboration (autoethnography of AI-assisted writing), the skill provides six categories of "reflexive moments":

🔄 Direction change · 🚫 Refusal · 🎭 Voice conflict · 🔧 Tool dependency · 💡 Unexpected insight · 🤖 AI-trace awareness

**Scholarly basis** (citable in your paper):
- Christou (2026). *Reconfiguring Reflexivity in the Era of AI*. *Qualitative Inquiry*.
- Wiles (2025). *Recursive Cognition in Practice*. *International Journal of Qualitative Methods*.
- Panke (2025). *How Can (A)I Research This? An Autoethnographic Exploration of Generative AI*.

### Engineering infrastructure

Borrowed from software engineering, in service of humanities writing:
- **Version management**: minor version = commit / major = release / `_drafts/` = feature branch
- **Revision log**: every change recorded with diff + reason (like git commit message)
- **Feedback reports**: Blocker / Major / Minor / Question tiers (from code review)
- **Systematic verification checklists**: argument completeness / concept consistency / citation completeness / style consistency
- **`[VERIFY]` / `[待核对]` hard marker**: anti-citation-hallucination — cannot enter submission version

### Seven work modes (not one)

- **Mode A** — paragraph-level dialogue
- **Mode B** — chapter-level review
- **Mode C** — conception → new content writing (with collaborative drafting protocol)
- **Mode D** — devil's advocate
- **Mode E** — writing bottleneck assistance (5 unblocking strategies)
- **Mode F** — draft revision (two-version comparison, anti-AI-cliché)
- **Mode G** — blind reading (mechanical promise-delivery check)

### Engineering helper scripts

[`scripts/`](./scripts) provides three zero-dependency tools:

| Script | Purpose |
|--------|---------|
| `ai-trace-scan.sh` | Scan clichés and transition pile-ups |
| `pending-checks.sh` | Aggregate all `[VERIFY]` / `[待核对]` / `❓ to discuss` / `[AI DRAFT]` markers |
| `citation-consistency.py` | Citation-format consistency check (brackets / commas / connectors / EN/CN names / page numbers) |

---

## Supported humanities disciplines

This skill ships with discipline-specific critique dimensions that activate when you declare your discipline at onboarding (or when the skill detects it from your draft). Each discipline has different failure modes that generic AI writing tools miss.

| Discipline | What this skill watches for |
|---|---|
| **History · 历史** | Anachronism (retrojecting modern concepts into the past); counterfactual stress (could events have gone otherwise?); source-handling discipline (primary vs. secondary, source-internal voice); causal-chain transparency |
| **Philosophy · 哲学** | Conceptual derivation chain (where does this concept come from, how is it deformed); cross-theoretical transplantation (importing concepts from tradition A into B without paying transport costs); steel-manning the strongest objection before refute |
| **Literature & literary criticism · 文学批评** | Close reading vs. interpretation (is interpretation anchored in textual evidence?); genre awareness (the genre is half the meaning); form-meaning fit (does formal observation actually carry the interpretive load) |
| **Cultural studies · 文化研究** | Power-knowledge framing (who speaks, who is spoken about); positionality (the author's own location); generalization range (does this case warrant the universal claim) |
| **Art history · 艺术史** | Description vs. interpretation (keep them separate); provenance and material history (the object's life); reception history (was the work read this way at its moment, or only now) |
| **Religious studies & classics · 宗教学与古典学** | Source-language rigor (is the original consulted, or only translation?); tradition awareness (which traditional reading is presupposed); insider-outsider position (etic vs. emic) |
| **Cross-disciplinary case studies** | Why this case (typicality vs. exception); what it can and cannot generalize to; case-as-narrative vs. case-as-argument |

**Don't see your subfield?** Most subfields (medieval studies, intellectual history, science studies, ethnomusicology, art conservation, …) inherit from one or two of these main disciplines. Either declare the inheritance at onboarding (`"I'm doing intellectual history — inherit from History + Philosophy"`) or open an Issue to propose a new dimension.

The full critique dimensions for each discipline live in `SKILL.md` § *Humanities Discipline-Specific Dimensions* — this table is the README-level surface; the skill itself carries the full rubric.

---

## Showcase: Before / After

A real example of the four-layer critique in action. Author's draft paragraph (English translation of a Chinese-language thesis chapter on Stiegler):

> **Before.** Stiegler's pharmakon concept shows that technology is both poison and remedy. AI is therefore a pharmakon as well. We must be careful in our use of AI, lest we fall into its negative effects. As Stiegler said, technology is a double-edged sword.

The skill's response, top-down, four layers:

```
🔴 Layer 1 · Foundation — Argument standing

  The paragraph claims pharmakon = "double-edged sword." Stiegler explicitly
  rejects this equivalence (WMLWL, p. 12): pharmakon is curative AND
  destructive AT THE SAME TIME, not alternately, and the destructive force
  is proportional to the curative one. "Double-edged sword" implies a
  user-choice framing; pharmakon implies a structural condition that
  precedes user choice. This is not nuance — it is the whole point of
  borrowing the concept from Derrida.

  Verdict: Foundation broken. Do not proceed to lower layers until fixed.

🟡 Layer 2 · Structure — Argument unfolding (deferred until L1 fixed)

🟢 Layer 3 · Paragraph (deferred)

⚪ Layer 4 · Sentence (deferred)
```

After the author rewrites the foundation, the same paragraph might become:

> **After.** In Stiegler's framework — extended from Derrida's reading of Plato's *Phaedrus* — *pharmakon* names a structural condition rather than a moral choice: a technology's curative force is **inseparable from and proportional to** its destructive force (Stiegler, *What Makes Life Worth Living*, 2013, p. 12). For LLMs, this means the question is not "are we careful enough in our use?" — that frame presupposes a user fully outside the pharmakon. The question is: *in what historical-organological configuration does the pharmakon's destructive face become structurally dominant?* I argue, following Stiegler's reading of digital tertiary retention in *Automatic Society* (2017), that …

What changed: a clichéd "double-edged sword" framing replaced by Stiegler's actual conceptual move, a citation anchored at a verifiable page, and a forward-pointing thesis the next paragraph can develop. The skill did not write the rewrite — it identified that the foundation was wrong, named *why*, and refused to do sentence-level work until the foundation was repaired.

> **This is what "thinking partner, not polishing tool" means in practice.**

---

## Install

### As a Claude Code skill

```bash
git clone https://github.com/tizzy916/claude-skill-humanities-writing-companion.git \
  ~/.claude/skills/humanities-writing-companion

chmod +x ~/.claude/skills/humanities-writing-companion/scripts/*.sh
```

Or as a project-level skill (vault / project only):

```bash
git clone https://github.com/tizzy916/claude-skill-humanities-writing-companion.git \
  ./.claude/skills/humanities-writing-companion
```

### Claude Code loading

Claude Code auto-scans `~/.claude/skills/` and `./.claude/skills/` on startup. After install, say "I'm working on a humanities paper" or any of the trigger phrases below.

### Claude Agent SDK

`SKILL.md` can be loaded into your system prompt directly. The skill is plain text — no runtime dependencies.

### Trigger phrases

**English**: "paper," "essay," "chapter," "dissertation," "argument," "thesis," "revise," "voice," "review my section," "stuck on writing," "devil's advocate," "reviewer attack"

**Chinese**: 论文 · 写作 · 润色 · 改论文 · 帮我看看这一章 · 我手写我口 · 这个论证有没有问题 · 我写不下去了 · 审稿人会怎么攻击

Even casual mentions trigger: "take a look at this paragraph" · 帮我看看这段话

---

## Quick start · three typical scenarios

### Scenario 1: new paper, first use

Say to Claude: "I want to write a paper on X."

The skill enters onboarding: confirms citation format, target reader, existing writing samples, and initializes the project folder structure.

### Scenario 2: revising an existing chapter

```
"Help me read this chapter"      → Mode B (chapter review) → 4-tier feedback report
"Help me revise this paragraph"  → Mode A (paragraph dialogue) → diagnose + suggest + reason
"I'm stuck"                      → Mode E (bottleneck) → 5 unblocking strategies
```

### Scenario 3: fighting AI cliché (two-version comparison)

If your paper has been through AI polishing but you want to restore the original voice:

```
Mode F · draft revision → compare AI-polished vs. original → keep improvements + restore voice
```

---

## Comparison with adjacent tools

| Tool | Core positioning | Difference from this skill |
|------|------------------|----------------------------|
| **academic-research-skills (Imbad0202)** | Full empirical research pipeline | Pipeline-oriented; this is writing-voice-oriented. Use both for full coverage. |
| **Jenni AI** | Real-time auto-completion + literature discovery | This skill doesn't auto-complete; focuses on thought-dialogue |
| **Paperpal** | Academic language polishing (STEM-leaning) | This skill is architecture, not point-tool |
| **Yomu AI** | Sourcely literature engine + paragraph feedback | This skill doesn't search literature; assumes author manages (Zotero/Drive) |
| **Thesify** | Paper Digest + Purpose-Check | This skill's Mode G is inspired by Purpose-Check design philosophy |
| **HyperWrite Devil's Advocate** | Point-tool counter-argument generation | This skill's devil's advocate is a full mode with anti-sycophancy |

---

## Project structure

```
humanities-writing-companion/
├── SKILL.md                          ← Main skill file (EN, ~900 lines)
├── SKILL.zh.md                       ← Chinese mirror (中文版)
├── references/
│   ├── ai-trace-checklist.md         ← AI-trace scan checklist (currently Chinese; EN translation TODO)
│   ├── project-management.md         ← Project folder + version management
│   └── target-reader-profile-template.md  ← Target reader profile template
├── scripts/
│   ├── README.md                     ← Script usage
│   ├── ai-trace-scan.sh              ← AI cliché scan (zsh)
│   ├── pending-checks.sh             ← Pending marker aggregation (zsh)
│   └── citation-consistency.py       ← Citation format consistency (Python 3)
├── README.md                         ← This file
├── README.zh.md                      ← 中文 README
├── LICENSE                           ← MIT
└── CITATION.cff                      ← Academic citation metadata
```

**Bilingual status**: SKILL.md and README are bilingual (EN + CN). `references/` files and `scripts/` comments are currently primarily Chinese; English translations are TODO. Both languages of trigger work either way (the description field in SKILL.md handles both).

---

## Design philosophy

### "My hand writes my voice"

Academic rigor and personal expression are not opposites. "Standard academic prose" usually means the death of individuality. The skill helps the author speak in their own voice rather than pressing their words into a prefabricated mold.

### Thought first, format second

Revision priority:
1. Force of the argument
2. Precision of concepts
3. Effectiveness of structure
4. Quality of expression
5. Format compliance

Always top-down. Do not fuss with commas in a paragraph whose underlying argument is broken.

### Engineering rigor, humanistic expression

Borrows software engineering best practices (version management, unit tests, code review) in service of humanities writing. Engineering rigor does NOT mean turning the paper into code — it means every revision is traceable, argument quality is verifiable, the writing process is resumable, and problems are processed in layers.

---

## Citation

If your research uses this skill, please cite it in the methodology section.

**BibTeX**:
```bibtex
@software{shen_humanities_writing_companion_2026,
  author       = {Shen, Cong},
  title        = {Humanities Writing Companion: A Claude Skill for Voice-Preserving Humanities Academic Writing},
  year         = {2026},
  url          = {https://github.com/tizzy916/claude-skill-humanities-writing-companion},
  version      = {2.0.0}
}
```

**Plain-text attribution** (for skill metadata, footers, etc.):
```
Based on Humanities Writing Companion by Shen Cong
https://github.com/tizzy916/claude-skill-humanities-writing-companion
```

See [`CITATION.cff`](./CITATION.cff) for full machine-readable metadata (GitHub's "Cite this repository" button will use it automatically).

### Citing companion tools

If you also use [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) in the same project, please cite both. ARS attribution format (per CC BY-NC 4.0):

```
Based on Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## Contributing

Issues and PRs welcome:
- New work-mode proposals
- Extensions to the AI-trace checklist
- Discipline-specific examples (medieval studies, art conservation, ethnomusicology, etc.)
- Additional citation-format support (APA / Chicago / MLA / GB/T 7714 / journal-specific)
- English translation of `references/` files

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## About the Author

Shen Cong — BFA, Experimental Art, Central Academy of Fine Arts (CAFA); MA, History of Science, Tsinghua University (advisor: [Hu Yilin](https://yilinhut.net/author/admin)); Founder & CEO of [Tianyu Vision](https://tianyu.art/), a sci-art studio working on scientific visualization, science communication, and sci-art convergence.

This skill came out of writing the author's own MA thesis, *Technical Liberalism*. He noticed that almost every AI writing tool on the market pulled toward **polishing and averaging** — whereas humanities scholarship needs the opposite: protecting the author's scholarly voice, stress-testing argumentative rigor, and surviving adversarial peer review. So he built this skill — not to write *for* him, but to *read* for him, delivering at each of four layers (basic rigor / argument development / paragraph function / sentence-level expression) the kind of critique a real humanities scholar would actually give.

📮 [GitHub @tizzy916](https://github.com/tizzy916) · shencong916@gmail.com · Corrections, collaboration, and conversation welcome.

---

## License

[MIT](./LICENSE) — free to use, modify, distribute.

---

## Acknowledgments

Methodological inspiration and scholarly basis:

- Christou, P. A. (2026). [Reconfiguring Reflexivity in the Era of AI](https://journals.sagepub.com/doi/10.1177/10778004261445052). *Qualitative Inquiry*.
- Wiles, F. (2025). [Recursive Cognition in Practice](https://journals.sagepub.com/doi/10.1177/16094069251381709). *International Journal of Qualitative Methods*.
- Panke, S. (2025). [How Can (A)I Research This?](https://journals.sagepub.com/doi/10.1177/00224871251325065).
- Foucault, M. (1984). What is Enlightenment? — "diagnostic of the present" as methodological tradition
- Stiegler, B. (2013). *What Makes Life Worth Living: On Pharmacology* — "critical pharmacology"

Some design patterns inspired by:

- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — the upstream pipeline this skill complements; the Concession Threshold pattern in their reviewer module inspired Mode D's "minimum standard before conceding"
- [Voice DNA + Audience Profile pattern](https://aiblewmymind.substack.com/p/claude-skills-ai-write-like-you) — inspired the style profile + reader profile pairing
- [Thesify](https://www.thesify.ai/) Purpose-Check — inspired Mode G blind reading
