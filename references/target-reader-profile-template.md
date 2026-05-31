# Target Reader Profile · Template

> **Language / 语言**: **English (current)** · [中文](target-reader-profile-template.zh.md)

> This profile is paired with the "writing style profile" — voice cannot be separated from audience.
> In all critique and drafting work, the AI should consider both at once:
> - The style profile tells it "how the author speaks"
> - The target reader profile tells it "whom they are speaking to"
>
> The humanities-writing-companion skill copies this template into the paper project's
> `_writing-config/目标读者档案.md` (or the English path `_writing-config/reader-profile.md`) during onboarding, for the author to fill in incrementally.
> **No need to wait until it is "complete" — a blank slot still beats having no profile at all.**

---

## 1 · Primary readers

> Fill in only the item matching your writing context; you don't need to complete them all.

### Dissertation scenario
- **Defense committee members** (if known):
  - Member 1: [name] / discipline: [XX] / research focus: [XX] / likely concerns: [inferred from their research]
  - Member 2: …
  - Member 3: …
- **What to do when you don't know who the committee is**: list the typical committee composition for your department (e.g., "3 from the home department + 2 from outside"), and estimate by disciplinary field

### Journal submission scenario
- **Target journal**: [full title] / [abbreviation]
- **Typical reviewer profile**:
  - Disciplinary background: [the journal's mainstream discipline]
  - Stance tendency: [empirical / theoretical / critical / synthetic]
  - Journal preferences: [long-form vs. short-form / international vs. local / speculative vs. data-driven]
  - Historical rejection patterns: if you can find sample reviewer comments for this journal, distill them here

### Conference paper scenario
- **Conference**: [name / discipline / scale]
- **Expected audience**: [mostly graduate students / mostly senior scholars / interdisciplinary]
- **Talk vs. paper**: which does the conference emphasize?

---

## 2 · What the reader knows / doesn't know

### Concepts that need no explanation
> These concepts can be used directly, with no need to define or set them up in the text.
> If the reader group is known to be familiar with them, save the space for more original argumentation.

- [concept 1]
- [concept 2]
- ...

### Concepts that need explaining on first use
> These concepts must be defined or explained the first time they appear, or the reader will lose the thread.

| Concept | Mode of explanation |
|------|---------|
| [concept name] | brief parenthetical / footnote / paragraph-length development |
| [concept name] | ... |

### Concepts prone to being misread
> These concepts differ between your usage and the reader's familiar usage, and need proactive clarification.

| Concept | Your usage | Reader's common usage | Clarification strategy |
|------|---------|-------------|---------|
| [concept name] | ... | ... | distinguish proactively on first use |

---

## 3 · The reader's possible positions

> This is the concrete input for devil's advocate mode. **The more specific your entries, the more precise the attacks the AI can simulate.**

### A · Friendly reader at a professional remove
> From a related discipline but not your subfield. Will ask basic questions and need more setup.

- Main characteristics: […]
- How to accommodate them in the paper:
  - Explain concepts on first appearance
  - Give a road map at the start of each chapter
  - Avoid too much insider jargon
- **This reader corresponds to "Reader D · Well-intentioned but confused" in devil's advocate mode**

### B · Same-field reader holding a different theoretical position
> Familiar with your subfield, but coming from a competing theoretical tradition.

- Competing position 1: [position name]
  - Claim: […]
  - Will challenge your: [specific argument / concept / chapter]
- Competing position 2: [position name]
  - Claim: […]
  - Will challenge your: […]
- How to accommodate them in the paper:
  - State your position and its relation to theirs explicitly in the introduction or methodology
  - Don't pretend they don't exist
  - Respond head-on to the strongest competing position at least once
- **This reader corresponds to "Reviewer A · Theoretically demanding" in devil's advocate mode**

### C · The exacting methodology reviewer
> Cares little about your specific content; focuses on testing the internal consistency of the methodology.

- Main characteristics: […]
- Typical probing questions:
  - "How do you know?"
  - "What is your evidence?"
  - "Does your method match your claim?"
- How to accommodate them in the paper:
  - The methodology section must be detailed
  - The chain of evidence must be clear
  - No "assertion without grounds" allowed
- **This reader corresponds to "Reviewer B · Historically empirical" and "Reviewer C · Methodologically skeptical" in devil's advocate mode**

---

## 4 · Readers beyond the boundary (reaching beyond)

> This section is not required, but filling it in makes the writing more deliberate.

### People you hope will read this paper
> These are your "ideal readers." Keeping them in mind while writing makes the prose more restrained and more precise.

- [person 1]: reason [why you hope they read it]
- [person 2]: …

### Reader types you are wary of
> You don't want to be read in this way. Avoid leaving them an opening to quote you out of context.

- [type 1]: how they would misread you [specific scenario] / the countermeasure is […]
- [type 2]: …

---

## 5 · Interface with devil's advocate mode

The roles in devil's advocate mode should be made concrete based on this profile's "reader positions":

| Devil's advocate role | Corresponding source in this profile |
|----------------|---------------|
| Reviewer A · Theoretically demanding | the "strongest opponent" in reader position B |
| Reviewer B · Historically empirical | reader position C |
| Reviewer C · Methodologically skeptical | reader position C |
| Reader D · Well-intentioned but confused | reader position A |

The more specific the profile, the more precise the attacks. If a given field cannot be filled in for now, the AI should use a discipline-generic profile in devil's advocate mode, and remind the author to complete that item.

---

## Maintenance rules

- **Early in the writing**: establish a baseline version, which can be rough — "my paper is for faculty in my own department; they all know XX theory"
- **Update immediately when you get real feedback**: advisor comments, reviewer remarks, defense questions — these are the most accurate "reader-profile data"
- **No need to wait until it is "complete"**: a blank slot still beats having no profile at all
- **Update as needed**; don't try to write it all in one pass
- Reuse across papers: if the same author's multiple papers face similar reader groups, the shared parts can be retained
