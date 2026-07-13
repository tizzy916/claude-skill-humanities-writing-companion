# Contributing to humanities-writing-companion

> **Language / 语言**: **English (current)** · [中文](CONTRIBUTING.zh.md)

Contributions are welcome. This skill is an **opinionated** project — it favors *intellectual dialogue* over *surface polishing*, *engineering rigor* over *anecdotal heuristics*, and the *author's voice* over *standardized academic register*. Before contributing, please understand this stance and consider whether your proposed change is compatible with it.

**Division of labor with academic-research-skills**: This skill does **not** handle the empirical research pipeline (literature search, data collection, methodological compliance, etc.) — that is the domain of [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills). This skill focuses on writing voice, argumentative texture, and prose development in the humanities. Please confirm that a change falls within this skill's scope before proposing it.

---

## What's most valuable to contribute

### 🥇 Discipline testing (most needed)

The skill grew out of one specific humanities dissertation project, but its goal is to cover the **entire humanities** (history, philosophy, literature, cultural studies, art history, religious studies, classics, and more). The most valuable contributions are:

1. Use it for real in your own discipline / writing project
2. Report **which modules work well and which don't fit**
3. Propose **discipline-specific extensions** (e.g., Latin verification for medieval studies, material-culture analysis for art conservation, field-note handling for ethnomusicology)

See [`docs/cross-domain-testing.md`](docs/cross-domain-testing.md) for test scenarios grouped by discipline.

### 🥈 Expanding the AI-trace checklist

[`references/ai-trace-checklist.md`](references/ai-trace-checklist.md) is this skill's "defense in depth." If you discover **new unexamined expression patterns** in your own writing (not only AI clichés, but also discipline-specific formulae and the inertia that builds up from heavy theory reading), a PR to expand it is welcome.

### 🥉 Bilingual completion

SKILL.md and the README are already bilingual (SKILL.md / SKILL.zh.md / README.md / README.zh.md), but the supporting files under `references/` (ai-trace-checklist, project-management, target-reader-profile-template) and the comments in `scripts/` are currently mostly in Chinese. Translating these into English is a high-value contribution.

Translation principles:
- The Chinese cliché list in `ai-trace-checklist.md` (e.g., "值得注意的是") needs the corresponding English clichés added (e.g., "It is worth noting," "It should be noted") — not literal translations, but the **equivalent** filler phrases of English academic prose
- Where the citation quick-reference touches conventions beyond GB/T 7714, handle them according to English academic norms

### 🏅 New working modes

The skill currently has 12 working modes (A–L). If you find a high-frequency writing scenario that SKILL.md doesn't cover, you can propose a new mode. The **bar** for a new mode:

- It must be **mechanically distinct** from existing modes (not a rename or restatement of one)
- It must have **independent input requirements / output format**
- It must come with **at least one concrete use case** + its **expected effect**

### Citation-style support

The skill's citation config assumes the author selects a style during onboarding (APA / Chicago / MLA / GB/T 7714 / journal-specific). If you want deeper built-in support for a particular standard (e.g., auto-generating a reference list that complies with GB/T 7714's numeric sequential system), feel free to propose it.

### Script tooling

Extensions to the three tools in `scripts/`, or new tools — for example:

- Paragraph-coherence detection (based on repeated sentence-initial / sentence-final vocabulary)
- Concept-drift detection (contextual frequency of the same term across different chapters)
- Citation-density analysis (citation density per section, flagging anomalous passages)

New scripts must be **zero- or low-dependency** (zsh / Python 3 standard library / at most 1–2 common packages) and follow the design principles in `scripts/README.md`.

---

## Contributions that are less needed

> It's not that these contributions are "bad" — they simply diverge from the skill's design stance. Proposing them does not guarantee a merge.

- ❌ **Making the skill more "general-purpose"** — e.g., adding a "general polishing mode" or extending it to empirical social science or STEM. The skill is deliberately opinionated (**humanities** + thought-first + voice-preserving) and does not try to please every writing scenario. For an empirical research pipeline, go to [academic-research-skills](https://github.com/Imbad0202/academic-research-skills).
- ❌ **Replacing existing modules with LLM calls** — the skill describes its working modes as plain-text prompts and deliberately does **not** rely on runtime LLM calls (this is what lets it work at any entry point: Claude Agent SDK / Claude Code / Claude.ai / any SKILL.md-compatible agent).
- ❌ **"AI smart-polishing" features** — the skill's core premise is a rejection of the "AI auto-polish" narrative. Polishing should be an author-driven, dialogic process.
- ❌ **Adding paid / subscription integrations** — the skill is an open-source public good.

---

## Submission process

### Small changes (typos / doc fixes / small ai-trace-checklist additions)

Open a PR directly with a brief rationale for the change.

### Large changes (new modes / major SKILL.md revisions)

**Open an issue to discuss first.** SKILL.md and SKILL.zh.md are each ~900 lines, and every section interacts with the others — a large PR submitted cold can easily break the existing interlocking design (e.g., Mode G "blind-read checking" deliberately does *not* read `_writing-config/` files; that's by design, not an oversight).

**Bilingual coupling**: any substantive change to SKILL.md must also change SKILL.zh.md (keeping the two languages consistent). The same applies to README.md / README.zh.md. A PR that touches only one version will be asked to complete the other.

When discussing, please explain:

1. The specific writing-scenario problem you want to solve
2. Which existing module / rule falls short (ideally cite SKILL.md line numbers)
3. Which other parts of SKILL.md your change affects (interlock check)
4. How you will verify the change (how do you know it's correct?)

### Commit message style

Not strictly enforced, but recommended:

- Clearly state **which section / module** you changed
- One line on **why** you changed it
- If you changed multiple coupled spots in SKILL.md, list them

Example:

```
ai-trace-checklist: add "over-conceptualization" as a seventh unexamined pattern

Repeated real-world testing shows that AI tends to elevate everyday phrasing
into jargon ("this shows" -> "this phenomenon shows, at the epistemological
level"). This pattern does not fit any of the existing six categories, but it
appears very frequently.
```

---

## Code of Conduct

Simple principles:

- Scholarly critique is welcome; personal attacks are not
- Every disciplinary tradition deserves respect; the "my discipline is the only real scholarship" posture is not welcome
- The skill serves the author's **thinking** — any proposal that would weaken the author's cognitive agency (e.g., turning the author into a blind rubber-stamp for AI output) will not be accepted

---

## License

By contributing, you agree to release your contribution under the [CC BY-NC 4.0](LICENSE) license.

> **Note**: As of 2026-05-19, this project changed from MIT to CC BY-NC 4.0. New contributions fall under CC BY-NC 4.0 — meaning your contribution may also be used for non-commercial purposes only. If you have concerns about this, please open an issue to discuss before submitting a PR.
