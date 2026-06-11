# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [4.2.0] — 2026-06-11

**Field-distilled release: everything in this version was first proven in real paper-revision practice, then folded back into the skill.**

The source material: a complete defense-feedback integration cycle on a master's thesis (17 revision dossiers, 4 execution tracks, 100% closure, actual time 55% of plan), a second paper bootstrapped on oral-history methodology, and the version-management conventions that stabilized over three months of daily use.

### Added

- **Mode L · Revision workflow (defense/external-review comment integration)** — the 12th mode. Every reviewer comment becomes an independent revision dossier (location / current text / verbatim comment / plan / draft / verification) indexed by a status-authoritative master table. 5-state status system (pending / in-progress / partial / completed / needs-rework) with a hard definition of "done" (chapter files changed AND revision log recorded). Track grouping by chapter/theme instead of linear or priority-only execution. Author-intent-first deviation rules. Full manual in new `references/revision-workflow.md` + `references/revision-workflow.zh.md`.

- **Mode D · Perspective-skill integration** — formalizes the practice of replacing generic reviewers with theorist-specific perspective skills (distilled via scholar-wendao) when a theorist is load-bearing (cited 3+ times). Three capabilities beyond the generic reviewer: precision attacks inside the concept, lineage discrimination (author depends on one school's *reading*, not "the theorist's own position"), and honest boundaries ("things this theorist never said"). Multi-skill joint review for chapters mobilizing several theorists. Field-proven: a perspective-skill self-check once surfaced a conceptual misalignment one level deeper than the advisor's own objection.

- **Multi-Agent Collaboration section** — for agent-capable environments (Claude Code, desktop agent mode). Governing principle: **diagnosis parallelizes, drafting does not.** Mode D multi-reviewer fan-out (mutually invisible reviewer agents, closer to real peer review than one AI role-playing four reviewers); Mode B chapter-parallel review with the explicit caveat that Layer-1 critique and cross-chapter consistency must stay in the main conversation; claim verification via deep-research-type tools with a 4-tier evidence system (A primary-verified / B reliable second-hand / C oral history / D unverified) where the tier governs assertion strength in the paper.

- **Pre-revision self-check SOP** (in revision-workflow reference): before executing a dossier involving a theorist, self-check the draft with the corresponding perspective skill; fix the dossier draft before executing into chapters.

- **`chapters/` multi-file structure** in project-management references — field-proven for dissertations and 50k+ character manuscripts: per-chapter revision context, chapter-level review fan-out, partial backups. File names encode physical order only, never version numbers.

- **Version naming conventions** in project-management references — "resident sources + milestone archives + versioned exports": three-segment versions mark state nodes, not everyday edits; markdown sources are the single source of truth, docx/pdf are exports; archive and export naming schemas.

- **"Scripts before manual checklists" calling convention** — in shell-capable environments, script-covered checks (cliché scan, citation consistency, pending markers) run as scripts first, with human judgment applied to results; the manual checklist is the fallback, not the default.

### Changed

- **scripts/ table in both SKILL files** now lists all five scripts (citation-format-convert.py and citation-verify.py were missing from the Chinese table since v4.0).
- **Cross-Skill Collaboration** rewritten: adds scholar-wendao/perspective skills, deep-research-type tools, citation-proofing and thesis-formatting tools (division of labor: in-process consistency here, final-format audit there), and meeting-notes tools as Mode L input.
- **Navigation, selective-loading guide, quick-triage tree, frontmatter descriptions** updated for Mode L and multi-agent collaboration in both languages.
- **scripts/ai-trace-scan.sh, scripts/pending-checks.sh**: `grep | wc -l` pipelines hardened with `|| true` so zero-match files no longer abort under `set -e` / `set -o pipefail`.
- **scripts/ai-trace-scan.sh shebang fixed to zsh** — the previous `#!/usr/bin/env bash` shebang crashed on macOS's bundled bash 3.2 (`unbound variable` when iterating the multibyte pattern array under `set -u`); the script was always documented as zsh.

### Rationale

v4.0/4.1 expanded the skill's *coverage* (modes H-K, discipline architecture). v4.2 closes the loop in the other direction: practices that emerged spontaneously during real use — revision dossiers, perspective-skill reviewers, evidence tiers for oral-history claims, chapters/ structure — were being re-invented per project from memory. Folding them into the skill makes them load-bearing infrastructure instead of tribal knowledge. This is also the skill practicing what it preaches: the interaction log's "Skill line" exists precisely so that usage experience flows back into the tool.

---

## [4.1.0] — 2026-05-19

**Discipline architecture refactor: flat 7-entry list → 3-layer architecture.**

The previous "Supported humanities disciplines" section listed seven entries (history, philosophy, literature, cultural studies, art history, religious studies, classics) as if they were at the same conceptual layer. They were not — three were L1 main disciplines, one was an L2 subfield, two were L3 cross-disciplinary fields. The set also reflected the author's own research range (history of science / technology philosophy / cultural studies) rather than the actual map of humanities scholarship.

This release restructures the discipline architecture so users from any humanities or humanities-adjacent field can find their position.

### Added

- **L1 layer · 6 main humanities disciplines**: Literature, History, Philosophy, Linguistics (new), Art studies (replacing Art history as the broader parent), Religious studies. Each gets a refined methodology rubric with 5-7 core concerns.
- **L2 layer · subfield inheritance mechanism**: subfields (e.g., 中国古代文学, 经济史, 伦理学, 艺术史, 音乐学) inherit all parent L1 concerns and may add subfield-specific overlays. Documented common subfield overlays for each L1.
- **L3 layer · 9 cross-disciplinary fields with explicit multi-inheritance**:
  - Cultural studies (← Literature + History + Sociology)
  - Classics (← Literature + History + Philosophy + Religious studies + Archaeology)
  - Intellectual history (← History + Philosophy) — *new entry*
  - History of science (← History + Science + Philosophy) — *new entry*
  - Media studies (← Literature + Cultural studies + Philosophy of technology) — *new entry*
  - Digital humanities (← any L1 + Computation) — *new entry*
  - Gender studies (← Literature + History + Cultural studies) — *new entry*
  - Postcolonial studies (← Literature + History + Cultural studies) — *new entry*
  - Environmental humanities (← Literature + History + Science) — *new entry*
- **Humanities-adjacent fields · welcomed with explicit scope notes**:
  - Communication studies (humanities-style, e.g., media ecology school: Innis / McLuhan / Postman / Carey)
  - Educational research (humanities-style, e.g., history of education, philosophy of education, critical pedagogy)
  Each comes with explicit "what we serve / what we don't serve" boundaries, inheritance chain, and field-specific overlay.
- **Fallback protocol**: for any field not on the list — author declares `object of study` + `primary method`, skill infers closest L1 + relevant overlays. Suggests refinement as project develops.

### Changed

- **Onboarding step 1 upgraded to 3-layer elicitation**: now asks separately for L1 (required), L2 (optional), L3 (optional, possibly multiple), and humanities-adjacent declaration. `_writing-config/discipline.md` schema updated.
- **Discipline routing protocol rewritten** to handle layer composition (L1-only, L1+L2, L1+L3 with multi-inheritance, adjacent-field with documented overlay). Tagged outputs in `_meta/interaction-log.md` now identify which layer each attack originates from (e.g., `[Mode D · methodology · L1 History]`, `[Mode D · methodology · L3 Intellectual history]`).
- **Mode D methodology-focus attack table** restructured: 6 L1 attack vectors + 9 L3 overlay attacks + 2 humanities-adjacent attacks. Author with `discipline.md` declaring `史学 + 哲学 + L3 思想史` now gets all three sets of attacks loaded.
- **Mode J standard arc table** restructured: 6 L1 arcs + selected L3 / adjacent arcs (incl. communication studies humanities-style arc, educational research humanities-style arc). Authors in fields with humanities-style sub-traditions now have arc templates.
- **README disciplines section** rewritten with full 3-layer table including L1 (6), L2 (examples), L3 (9), humanities-adjacent (2), and fallback protocol. Same in `README.zh.md`.

### Rationale

The previous flat seven-entry list:
- Mixed conceptual layers (L1 / L2 / L3 not distinguished) — confused users trying to declare their discipline
- Excluded fields where prose IS the argument but where the discipline is formally social science (communication studies, educational research) — these users had no entry point
- Reflected the author's own research range (history of science, technology philosophy, cultural studies) rather than the actual humanities map — newcomers from literature, linguistics, religious studies, art studies (broadly) had partial or no coverage

The 3-layer architecture with explicit multi-inheritance + humanities-adjacent welcome solves all three.

### Migration notes

- Existing `_writing-config/discipline.md` files written under v4.0.0 still work — the new schema is additive (old `discipline: history` is parsed as `L1: History`).
- Users who previously declared "literature" now get the expanded L1 Literature concerns (close reading, theoretical scaffolding, quotation-as-evidence, narrator distinction, genre, form-meaning, intertextuality). The first three were in v4.0.0; the last four are new.
- Users in communication studies / educational research who previously had no entry point should re-declare in onboarding using the new humanities-adjacent option.

---

## [4.0.0] — 2026-05-19

**Major repositioning + capability expansion. End-to-end humanities writing assistant.**

This release is a strategic refactor. Earlier versions positioned the skill as a "humanities-side companion" to academic-research-skills (ARS). v4.0 establishes the skill as an **independent end-to-end writing assistant for humanities scholars** covering the full lifecycle of a humanities paper.

### Added

- **Mode H · Research-question sharpening (Socratic)** — earliest-stage mode. Turns vague topic into sharp, write-able research question through structured Socratic dialogue. Includes humanities-specific question taxonomy (re-reading / re-construction / intervention), the "so what" test, interlocutor identification, and verb-sharpening. Output: `_writing-config/research-question.md`.

- **Mode I · Literature mapping** — organizes references the author has already read into a working camp-and-debate map. Hard rule: does NOT do literature search for the author (no citation hallucination, no replacement of irreducible reading work). Includes optional scholar-wendao integration: load-bearing scholars can be auto-suggested for perspective-skill generation. Output: `_writing-config/literature-map.md`.

- **Mode J · Plan-only outlining** — pure outline mode, no draft writing. Extracted from Mode C to enforce planning discipline. **Discipline-aware**: pulls discipline-specific standard arcs (philosophy concept-puzzle arc, history historiographical-narrative arc, literature theoretical-frame arc, etc.) from `_writing-config/discipline.md`. Output: `_writing-config/outline.md`.

- **Mode K · AI-use disclosure (humanities-journal-specific)** — generates the AI-use disclosure statement required for journal submission. Includes a humanities-specific 4-tier categorization (0: no AI / 1: proofreading-translation-format only / 2: thinking partner / 3: prose-assisted / 4: prose-substantial) and three template options (short footnote / standard methods paragraph / detailed appendix). Audits `_meta/interaction-log.md` and revision history. Warns when AI-use tier exceeds typical humanities journal policy. Output: `_meta/AI-use-statement.md`.

- **Mode D calibration (1–5 levels)** — reviewer intensity is now dialable. Level 1 (gentle reader) through Level 5 (adversarial committee member). Level 3 (peer reviewer) is the default. Author can switch levels mid-session; Concession Threshold tightens at Level 5 (3-of-5 conditions instead of default 2-of-5). Level 4–5 trigger periodic check-in prompts.

- **Mode D methodology-focus sub-mode** — attacks the methodology rather than the content of the argument. Discipline-aware: surfaces discipline-specific methodology vulnerabilities (history: source handling, anachronism; philosophy: argument form, modal scope; literature: hermeneutic circle, genre awareness; etc.). Often surfaces deeper problems than content-level attack.

- **Mode F.coach sub-mode (revision-coach)** — Mode F variant where the skill withholds the revision until the author works through 3–5 diagnostic questions at the relevant critique layer. Slower but trains the author to internalize the four-layer critique. Tagged in revision log as `[coached]`.

- **`scripts/citation-format-convert.py`** — converts BibTeX bibliography between four major humanities citation styles: Chicago (Author-Date), MLA 9, APA 7, and GB/T 7714 (顺序编码制, Chinese national standard). Zero dependencies (Python 3 stdlib only). Supports `@book`, `@article`, `@incollection`, `@inbook`, `@inproceedings`, `@thesis`. Sanity-tested against canonical examples in all four styles. Honest about limitations — not a BibLaTeX/CSL replacement, output should be checked against target journal's style guide.

- **`scripts/citation-verify.py`** — verifies in-prose citations against the Crossref API, flagging hallucinated citations (LLM made-up journal articles). Three verdicts: FOUND / FUZZY_MATCH / NOT_FOUND. Network-rate-limited to 1 req/sec for politeness. Explicitly scoped: Crossref coverage is best for English-language journal articles in indexed journals; NOT_FOUND is expected (and not a problem) for monographs, archival sources, classics, dissertations, foreign-language works — for those, the `[VERIFY]` marker workflow remains the right tool.

- **End-to-end positioning** in both READMEs: full writing lifecycle from research-question sharpening → submission disclosure, with 11 modes mapped to lifecycle stages.

### Changed

- **Removed `## Companion: academic-research-skills` section**. The skill is no longer framed as a humanities-side complement to ARS. ARS remains a designed-acknowledged influence (Concession Threshold pattern in Mode D anti-sycophancy), but is now treated as one of several lateral tools in the Comparison section rather than a designated companion.

- **Rewrote Comparison with adjacent tools** table: lateral positioning against Jenni AI, Paperpal, Yomu AI, Thesify, HyperWrite Devil's Advocate, Grammarly / DeepL Write, and generic ChatGPT / Claude. ARS removed from the table.

- **Rewrote Positioning section** in both `README.md`/`README.zh.md` and `SKILL.md`/`SKILL.zh.md` to emphasize end-to-end coverage and explicitly contrast with "not a research pipeline / not a polishing tool / not a citation manager."

- **CITATION.cff abstract** rewritten to describe all 11 modes and the citation toolchain. ARS reference retained with narrower scope ("acknowledged design influence on early versions").

- **Navigation and Selective Loading Guide** in both SKILL files updated to register new modes H/I/J/K and Mode D/F sub-modes; added task-type routing rows.

- **`scripts/README.md`** updated for the 5-script toolchain: `ai-trace-scan.sh`, `pending-checks.sh`, `citation-consistency.py`, `citation-format-convert.py`, `citation-verify.py`.

### Acknowledgment retained (not removed)

- ARS's Concession Threshold pattern (Mode D anti-sycophancy) and overall design-influence remain credited in CITATION.cff (`references`) and in the SKILL.md Cross-Skill Collaboration section. This is a design-acknowledgment, not a license-derived attribution requirement (model/pattern borrowing does not constitute CC BY-NC 4.0 "Adapted Material" — content authored independently).

### Migration notes for users

- If you used v3.0.0 expecting it to be the "writing half" of an ARS-paired workflow: v4.0 covers the whole writing-side workflow itself. You can still use ARS in parallel if you want (no breaking integration), but the v4.0 modes (H/I/J/K + enhanced D/F) replicate the writing-relevant capabilities of ARS within a humanities-specific design.
- New `_writing-config/` files: `research-question.md` (Mode H), `literature-map.md` (Mode I), `outline.md` (Mode J). Discipline routing now requires `_writing-config/discipline.md`.
- New `_meta/` file: `AI-use-statement.md` (Mode K).
- Existing v3.0.0 projects continue to work — the new modes are additive.

---

## [3.0.0] — 2026-05-19 (earlier same day)

**License change: MIT → CC BY-NC 4.0.**

### Changed

- License changed from MIT to CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International).
- Versions ≤ v2.1.0 remain under MIT and retain their original commercial-use rights for those specific versions.
- From v3.0.0 onwards, commercial use is prohibited without a separate license.
- Updated LICENSE, README badges, CITATION.cff license field, CONTRIBUTING.md.
- Added Commercial Use section to README with inquiry contact (shencong916@gmail.com).
- Author identification upgraded across CITATION.cff and .zenodo.json: `tizzy916` → `Shen, Cong` with affiliation.

---

## [2.1.0] — 2026-05-19 (earlier same day)

**ARS companion section, citation conventions, humanities discipline routing.**

### Added

- Dedicated `## Companion: academic-research-skills` section in both READMEs with division-of-labor diagram and design-lineage attribution.
- `## Supported humanities disciplines` README section: seven main disciplines + cross-disciplinary case, each with failure modes the skill watches for.
- `## Showcase · Before / After` example demonstrating four-layer critique refusing to descend below a broken foundation.
- `### Discipline routing protocol` in SKILL.md: discipline becomes a load-bearing routing variable. Onboarding step 1 upgraded to enforce explicit discipline elicitation.
- Citation section enhanced with proper BibTeX, plain-text attribution block, and "Citing companion tools" subsection for ARS attribution per its CC BY-NC 4.0 license.
- CITATION.cff: full author (Shen Cong + alias + affiliation) and ARS added as `type: software` reference.

---

## [2.0.0] — 2026-05-17

- Initial release of bilingual SKILL.md and READMEs.
- Repository renamed to `claude-skill-humanities-writing-companion`.

## [1.0.0] — 2026-05

- Initial public release as `academic-writer`.
