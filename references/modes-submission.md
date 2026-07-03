# Pre-submission Modes · Mode G (blind reading) & Mode K (AI-use disclosure)

> Loaded on demand from SKILL.md (Mode G/K stubs). 中文版：modes-submission.zh.md

### Mode G: Blind reading (promise-delivery mechanism)

**What's unique about this mode**: AI temporarily **turns off scholarly judgment** and only mechanically checks "did the author do what they said they would do?" Borrows from Thesify's Purpose-Check design — avoid AI's subjective processing, let the author themselves see whether the paper delivered on its promises.

**"Blind" means exactly two switches, both off**: (1) scholarly judgment off — no quality evaluation; (2) author-context off — do not read `_writing-config/` files. It does *not* mean anonymity (that's blind *review*, a different thing). Note that promise-extraction and matching still involve interpretation — this mode is *more* mechanical than Mode B, not infallible; flag borderline calls as borderline.

**When to engage**:

- After a chapter draft is complete ("I just finished Chapter 3, run blind reading")
- Before final submission ("one more promise-delivery pass before submission")
- After large revisions (structural changes may have unhooked previously-delivered promises)
- Author's intuition "something's off but I can't say what" — often an implicit promise was not delivered

**Workflow**:

0. **Completeness pre-check**: blind reading assumes a draft with an ending. If the text stops mid-way or contains author-facing alternatives (A/B forks, `>>>` markers, scaffolding sections), either defer the run or mark the affected promises "not yet written — excluded" instead of ❌. Exclude AI-workflow markers (`[AI DRAFT]`, `>>>`, source-note sections) from promise extraction entirely.

1. **Extract promises** (mechanical operation):
   - Scan introduction, chapter openings, section openings
   - Find all sentences of the form:
     - "This paper will..."
     - "This chapter will explore..."
     - "This section first... then... finally..."
     - "I will argue..."
     - "Below, in three parts, I respond to this question:..."
   - Record each promise with source location (chapter / paragraph)

2. **Check delivery** (mechanical operation):
   - In conclusion / chapter end / section end, look for corresponding response
   - **Delivery may be distributed**: a chapter-opening claim can be delivered progressively across the body rather than at the end — search the whole span and cite where
   - **Don't evaluate quality** — only judge "is there a response?"
   - Partial delivery (said A, B but not C) also explicitly noted

3. **Output format**:
   ```
   === Blind Reading · [chapter] ===

   ## ✅ Promises delivered
   - Promise: "this chapter will explore the tension between X and Y" (§1 ¶2)
     Delivery: §5 ¶3-4 directly handle the tension

   ## ⚠️ Partially delivered
   - Promise: "this section answers in three parts: A, B, C" (§3 ¶1)
     Delivery: A in §3.1, B in §3.2, but no corresponding section for C

   ## ❌ Promises not delivered
   - Promise: "I will return to scholar Z's critique in the conclusion" (intro ¶5)
     Delivery: not found — conclusion does not mention Z

   ## 🤔 Implicit promises (AI inference, may be wrong)
   - Chapter-opening introduces a core concept but chapter-end never returns to it — should there be closure?
   ```

4. **Key constraints — things AI does NOT do in this mode**:

   - Does not evaluate "is this promise scholarly worthwhile" — that's Layer 1 (foundation) work
   - Does not suggest rewriting un-delivered promises — only flags the "promise-delivery gap"
   - Does not write the missing responses — leaves to author whether to add delivery or retract promise
   - Does not read `_writing-config/` files — this mode deliberately steps outside the author's "internal view"

**Why this mode is valuable**: writing over long periods causes "promise drift" — the promises in the intro get replaced by discoveries in the argumentative process, but the author doesn't feel it. Blind reading is a mirror, placing the "original promise" and "actual delivery" side by side.

**Comparison with other modes**:
- Mode B chapter review: evaluates quality
- **Mode G blind reading: only checks delivery** — narrower, more mechanical, less prone to error

---

### Mode K: AI-use disclosure (humanities-journal-specific)

Generates the AI-use disclosure statement that humanities journals increasingly require for submission. **Humanities journals have different (typically stricter) AI policies than STEM journals** — many ban AI co-authorship, restrict AI to specific functions, and require explicit tier disclosure.

**When to engage**:
- Before journal submission
- Before dissertation deposit
- When the author asks "what do I write about AI use?"

**Workflow**:

1. **Audit AI involvement** by reading:
   - `_meta/interaction-log.md` (the full record of AI-assisted moves)
   - `_meta/revision-log.md` (which revisions were AI-suggested vs. author-initiated)
   - Any reflexive-writing notes the author kept
   - The skill's mode history (which modes were actually used, esp. Mode C drafting, Mode F revision)

2. **Categorize by tier** (humanities-specific 4-tier scheme):
   - **Tier 0 · No AI involvement**: drafted, revised, and finalized without AI. (Rare in 2026.)
   - **Tier 1 · AI for proofreading / translation / formatting only**: grammar correction, translation between languages, citation format conversion. No argumentative or conceptual involvement. **Most journals accept this without question.**
   - **Tier 2 · AI as thinking partner / devil's advocate**: AI used for Socratic dialogue, devil's advocacy, brainstorming, blind reading. AI did NOT generate prose that appears in the submission. **Most humanities journals accept with disclosure.**
   - **Tier 3 · AI-assisted prose**: some prose in the submission was AI-drafted then author-revised, OR AI-suggested phrasing was incorporated. **Several humanities journals restrict or forbid this; disclosure must be specific.**
   - **Tier 4 · AI-generated prose substantial**: large sections drafted by AI, then revised. **Many top humanities journals forbid this entirely.** Mode K will warn the author.

3. **Check journal policy — never from memory.** Ask the author to paste the journal's AI policy text, or fetch it in web-capable environments. If neither is possible, say plainly that the policy could not be verified and default to the most conservative reading. Do not assert what a named journal's policy says from memory — a wrong policy claim here misleads a submission decision. Flag if the author's actual tier exceeds what the verified policy permits.

4. **Generate disclosure statement** (multiple template options):

   **Template A · short (Tier 1–2, suitable for footnote or acknowledgments)**:
   > In preparing this manuscript, I used [tool + version, e.g., Claude (Anthropic), versions used March–June 2026] for [proofreading / Socratic devil's-advocate dialogue / format consistency checks]. The AI did not generate prose that appears in this submission. The author is responsible for all arguments, evidence, and final wording.

   **Template B · standard (Tier 2–3, disclosure paragraph)**:
   > **AI use disclosure.** During the writing of this paper, I used [AI tool + version, dates of use] in the following capacities: (1) [specific use 1, e.g., Socratic dialogue on the research question]; (2) [specific use 2, e.g., devil's-advocate stress-testing in Section 3]; (3) [specific use 3, e.g., AI-trace cleanup of an earlier AI-polished version]. [If Tier 3:] In Section [X], [quantity — only at the granularity the logs support; without records, honest qualitative wording such as "portions of Section 2"] of the prose was initially AI-drafted and subsequently revised by the author. All claims, citations, and arguments are the author's responsibility.

   **Template C · detailed (Tier 3–4, paragraph + appendix)**:
   > [Template B paragraph as above, ending with:] A per-section breakdown of AI involvement is provided in Appendix [X].
   >
   > **Appendix [X] · AI involvement by section**
   >
   > | Section | AI involvement | Tier | How the author reworked it |
   > |---------|----------------|------|----------------------------|
   > | §1 Introduction | none / devil's-advocate only | 0–2 | — |
   > | §2 … | first draft AI-generated from author's oral outline | 3 | restructured, re-argued, rewritten against style profile |
   > | … | … | … | … |

5. **Placement**: humanities journals usually take Tier 1–2 disclosures as an acknowledgments note or first-page footnote; Tier 3+ goes where the verified policy says — when in doubt, acknowledgments plus a sentence in the cover letter. Dissertations: follow the institution's template; default is a dedicated declaration page.

6. **Save to** `_meta/AI-use-statement.md` (Chinese: `AI 使用披露.md`).

**Author's prompt to verify**:
- "Did I use AI for any other function you forgot to mention?"
- "Did I use AI on materials I haven't told you about (e.g., earlier drafts before this skill was used)?"
- "Am I comfortable with the level of disclosure this generates? If not, I should reduce AI use, not reduce disclosure."

**Hard constraints**:
- Do NOT under-disclose. If the author wants to soften the statement, ask: "what specifically do you want to remove? Why?" Often the answer reveals an ethical problem.
- Do NOT over-claim AI sophistication ("the AI made critical contributions"): journals will read this as the AI being a co-author, which is forbidden. Disclosure is about transparency, not flattery.
- **Tiers merge upward**: the manuscript's overall tier is the highest tier reached anywhere in it. Structural contributions without prose (Mode J outlining, Mode H question work) disclose as thinking-partner use (Tier 2).
- **"I rewrote it heavily" does not demote Tier 3 to Tier 2.** The test: was the surviving prose regenerated from the author's own restatement *without the AI draft in view*? If the AI draft served as the working base, it stays Tier 3. Genuine demotion follows actual re-drafting (Mode F's no-original branch + ai-trace-scan + re-audit), never re-wording of the statement.
- **Missing or partial logs** (pre-skill drafts, other tools): reconstruct by structured interview — walk the manuscript section by section and ask what role AI played in each; label the result as a reconstruction.
- Always remind: **the author is responsible for everything in the submission**, regardless of AI involvement tier.
