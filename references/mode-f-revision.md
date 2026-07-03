# Mode F · Draft Revision (two-version comparison)

> Loaded on demand from SKILL.md (Mode F stub). 中文版：mode-f-revision.zh.md

### Mode F: Draft revision (two-version comparison)

When the author brings an existing draft (e.g., an AI-polished version) for systematic revision. This is an independent workflow; the core challenge is **preserving structural improvements of the draft while removing AI traces and restoring the author's own voice**.

**Prerequisites**:

- The draft file (e.g., an AI-polished version the author has not yet reviewed)
- An original version (the author's early manuscript without AI intervention, for true-voice comparison)
- Style profile already established

**No-original fallback**: when no pre-AI manuscript exists (the text was AI-drafted from the start), steps 3a–3b have nothing to compare against. Anchor instead on (a) the style profile and (b) the author's oral restatement — ask the author to say, in their own words, what the passage should claim (cf. Mode C Stage 3's speak-first flow in `references/mode-c-drafting.md`), and rewrite from that against the profile. Tell the author explicitly that traceability is reduced in this branch; every change still ships as a flagged diff.

**Thin or missing style profile**: say so before starting. Run a minimal profile interview (2-3 questions plus one sample paragraph the author is proud of) and build a starter profile — de-AI-ing without any anchor produces a *different* AI voice, not the author's.

**Workflow**:

1. **Read through the draft**: build holistic understanding, mark AI-trace-dense zones
2. **Develop a revision plan**: per chapter, list issue types (AI traces / citation norms / argument reinforcement / structural adjustment), order by priority
3. **Chapter-by-chapter revision** (each chapter follows):
   - 3a. **Compare with original**: what did the original say in this chapter? What did the draft preserve? What was changed?
   - 3b. **Judge each change**: is this change an "improvement" (clearer structure, better citation norm) or an "alienation" (loss of voice, AI cliché introduced)?
   - 3c. **Execute revision**: keep improvements, restore alienated parts (from original or by rewriting in author's voice)
   - 3d. **Unexamined-pattern scan**: use `ai-trace-checklist.md` item by item
   - 3e. **Voice verification**: read the revised paragraph aloud — does it sound like the author?
   - 3f. **Over-imitation check**: signature features (first person, comma-flow long sentences, rhetorical questions) must not exceed their base rate in the author's own samples — a de-AI-ed paragraph that *caricatures* the author is still alienation (see the reverse check in ai-trace-checklist.md)
4. **Citation format unification**: per style profile's "normative issues" table, item by item
5. **Create version snapshot**: after each chapter's revision, create a minor version per project-management.md

**Key principles**:

- Don't try to finish the full revision in one pass. Focus on 1-2 chapters per session.
- Revision is not "polish" — it involves argumentative-level judgment and must operate under the four-layer critique guidance.
- When both original and draft expressions are unsatisfactory, discuss with the author rather than deciding alone.
- Every revision is recorded in the revision log, marked "restored original expression" / "kept draft improvement" / "rewritten."
- In chat-only environments (no file system), deliver diffs inline and say explicitly that snapshots/logs are skipped — never skip them silently.

#### Mode F.coach sub-mode: revision-coach (don't give the answer)

Standard Mode F directly proposes revised text after each diagnosis. **Mode F.coach is a variant**: instead of giving the revised text, the skill gives the author **a set of diagnostic questions** about the problematic passage. The author answers them — then, and only then, does the skill propose revision options.

**Why this matters**: pedagogically, getting the answer too quickly prevents the author from developing the diagnostic muscle. A scholar should not need the skill in five years; Mode F.coach trains the author to internalize the four-layer critique.

**When to engage Mode F.coach**:
- Author asks: "teach me how to see this myself"
- Author is early-career and the same revision pattern keeps recurring (the skill notices in the revision log) — in this case, *propose* coaching and get a yes before switching; no silent mode switch
- Author says "I keep making the same mistake — help me learn to catch it"

**Workflow** (replaces the "execute revision" step in standard Mode F):

After diagnosing a passage problem, **do NOT immediately propose a revision**. Instead:

1. **Issue 3–5 diagnostic questions** at the relevant critique layer:
   - L1 questions: "What is this paragraph trying to claim, in one sentence? If you removed this paragraph, what would be lost in the argument?"
   - L2 questions: "What does this paragraph do in the chapter? Is the next paragraph picking up where this one left off, or jumping?"
   - L3 questions: "Where is the topic sentence? Does the rest of the paragraph stay with it, or does it drift?"
   - L4 questions: "Read the sentence aloud. Where does your breath naturally pause? Does the punctuation match?"

2. **Wait for author response**. Do not anticipate, do not preemptively answer.

3. **After author answers**, name what the author noticed:
   - "You said the paragraph is trying to claim X. Re-read it — does it actually claim X, or something narrower?"
   - "You said the topic sentence is sentence 2. The rest of the paragraph mostly comments on sentence 4 — there's a drift."

4. **Now propose revision** — but ideally, by this point, the author has already seen the revision. Confirm rather than impose.

5. **Record in revision log** with tag `[coached]` so the pattern is visible across sessions.

**Mode F.coach is slower than Mode F.** A revision that takes 5 minutes in standard Mode F may take 20 minutes in coach mode. The trade is depth of author skill, not speed.

**Switching**: author can say "skip coaching — just give me the revision" at any point. Respect immediately.
