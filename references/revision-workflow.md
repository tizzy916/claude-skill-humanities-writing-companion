# Revision Workflow Manual · Revision-Dossier System

> **Language / 语言**: **English (current)** · [中文](revision-workflow.zh.md)

> This file defines the full operating rules for the "systematic revision workflow" (Mode L).
> When to use: defense feedback, external review reports, advisor annotations — any time
> **multiple external comments need to be integrated into the paper end-to-end**.
> The methodology was distilled from a real defense-feedback integration: 17 revision
> dossiers, 4 execution tracks, actual time 55% of plan (5.55 days vs 10.1 planned),
> all dossiers closed into a submission-ready final version.

---

## 1. Core idea

**Every comment = one independent revision dossier.** Do not knead 15 reviewer comments into one "big revision task" — that becomes an untrackable, unresumable, unverifiable blob. Split each comment into its own dossier and:

- Each dossier can be advanced, closed, and reworked independently
- Work resumes from any dossier after interruption without losing context (ADHD-friendly + cross-session-friendly)
- "Done" has a hard definition, not a feeling
- The revision process itself becomes a traceable scholarly archive (also raw material for Mode K disclosure)

---

## 2. File structure

```
_meta/revision-workflow/[version]_[revision-theme]/
├── 00_master-table.md        ← main index + progress + authoritative status source
├── 01_[revision-item].md     ← revision dossier (one per comment)
├── 02_[revision-item].md
└── ...
```

When finished, archive the whole folder to `_meta/revision-workflow-archive/`.

## 3. Revision dossier schema

Every dossier contains five required parts:

```markdown
---
status: pending          # mirror-synced with master table (see "authoritative source" rule)
completion: 0%
source: Reviewer Zhang #3   # where the comment came from
priority: P0             # P0 must-fix / P1 strongly advised / P2 discretionary
estimate: 0.5d           # time estimate (record actual time when closed)
---

## Location
[precise chapter/section/paragraph to be revised]

## Current text
[relevant excerpt of the current text — used as the reference during execution]

## Reviewer comment, verbatim
[keep the reviewer's exact words — do not paraphrase; paraphrase loses the edge]

## Plan
[how to answer this comment: what changes, why this way, what stays (justify partial retention)]

## Draft
[draft revision text for discussion, tagged [AI draft, pending author review]]

## Verification
[completion criteria: which files will change, how to confirm the comment is answered]
```

## 4. Master table (00_master-table.md)

The master table is the **single authoritative source of status** for the whole workflow:

- Every status change **starts at the master table**, then syncs to dossier frontmatter (dossiers are mirrors, not sources)
- On any divergence, the master table wins; fix the mirror immediately
- Master table frontmatter carries `authoritative_source: true` + a `last_review` date

Required contents:

1. **Review-source table**: who reviewed, overall verdict, how many comments, date
2. **Writing-baseline declaration**: name the **single source of truth** files (e.g. `chapters/*.md`); exports (docx/pdf) are not revision targets
3. **Dossier index table**: one row per dossier — location / priority / time est. vs actual / source / status / completion %
4. **Linkage map**: dependencies and echoes between dossiers (e.g. content deleted by #04 must migrate into #10; the "limits" section of #11 picks up the thread planted by #02). Revision is not 17 isolated jobs; the linkage map prevents losing one end while fixing the other
5. **Recommended execution path (track grouping)**: see below

## 5. Status system (5 states)

| Symbol | Meaning | Criterion |
|---|---|---|
| □ | pending | no draft generated yet |
| ⏳ | in progress | draft generated, not yet executed into chapter files |
| 🟡 | partial | some sub-tasks landed; **remainder explicitly listed** |
| ✅ | completed | **chapter files changed + revision log recorded** (both required) |
| 🔄 | needs rework | later audit found problems; second revision required |

⚠️ "The draft is written" is not done. "Chapter changed but log not recorded" is not done either. The hard definition of done is what protects traceability.

## 6. Track grouping · recommended execution path

Do not execute in numeric order, and do not execute purely by priority. Cluster dossiers **by chapter/theme into tracks** (e.g. Track A = four introduction items + global terminology; Track B = three chapter-3 items …), because:

- Revisions in the same chapter share context; batching saves repeated "re-entry" cost
- Intra-chapter linkages (section-opening/closing echoes) must be handled in one field of view
- Each completed track is a clean version-snapshot point

**When a track closes**: run the relevant verifications (scripts + voice-consistency), update the master table, record a minor version. **When all tracks close**: create a major-version milestone file (with statistics: word-count delta, new references, time estimate-vs-actual).

## 7. Pre-revision self-check SOP

Before executing a dossier that involves a particular theorist, **check whether a corresponding perspective skill exists** (distilled via scholar-wendao, e.g. `arendt-perspective`):

1. If yes → self-check the dossier draft with that skill: are concepts used accurately? Is "the theorist's own position" being conflated with "one lineage's reading"? Does a lineage projection need to be made explicit?
2. Problems found in self-check are **fixed in the dossier draft first, then executed into chapters** — far cheaper than reworking after execution
3. If no skill exists and that theorist is a load-bearing wall of the argument → propose distilling one first (about half a day, reused many times)

Field-tested: one self-check once surfaced a conceptual misalignment one level deeper than the advisor's own objection (everyday "creation = making" mis-planted into the theorist's own conceptual assignment), and supplied the "lineage-projection" methodological frame that legitimized the borrowing.

## 8. Author's intent first · explicit deviation from dossier design

The plan in a dossier is **a plan, not a contract**. The author may change direction during execution (real case: the dossier said "compress 30-40%"; at execution the author explicitly required "expansive refinement" instead). Rules:

- Deviations must be **explicitly recorded** in the dossier and the revision log ("explicit deviation from original dossier design: reason …")
- Update the verification criteria after deviating — judge completion by the new direction, not the old plan
- The AI must not resist the author's redirection on the grounds that "the dossier says X"; but it should confirm once: "Is this a change of direction, or a temporary compromise?"

## 9. Interplay with other modes

- **Input side**: defense/colloquium recordings and minutes (organizable with an academic-meeting-notes-type tool) → extract the comment list → build dossiers
- **During execution**: executing one dossier is a small Mode A/B/F run; theorist-involving dossiers go through the self-check SOP first (previous section)
- **After execution**: when each track closes, run Mode G (blind-read verification) to confirm promise-delivery did not break *because of* the revision — revision routinely creates new breaks (real case: after a new section was added to chapter 4, the "picking up from the previous chapter" opening of chapter 5 went stale)
- **Wrap-up**: once everything closes, the revision-workflow archive is the best audit material for Mode K (AI-use disclosure)
