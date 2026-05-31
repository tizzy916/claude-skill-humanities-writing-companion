# Writing Project Operations Handbook

> **Language / 语言**: **English (current)** · [中文](project-management.zh.md)

> This file defines the file structure, version-management rules, and reference-management workflow for a writing project.
> It is an "operations-layer" guide — when SKILL.md touches file operations, follow this file to carry them out.

---

## 1. Project Folder Structure

Each paper or long-form piece is a self-contained project folder, located under `02 · Knowledge 知识库/Papers 论文写作/`:

```
Papers 论文写作/
├── _writing-config/                    ← 全局写作配置（跨论文共享）
│   ├── 写作风格档案.md                  ← AI 累积学习的文风记录
│   ├── 目标读者档案.md                  ← 与文风档案配对——voice 和 audience 缺一不可
│   ├── 引用格式速查.md                  ← 用户选择的引用格式参考
│   └── 学术写作检查清单.md               ← 提交前自查
│
└── [论文名]/                           ← 论文项目文件夹
    ├── [论文名].md                     ← 主稿（完整论文，单文件）
    ├── _meta/
    │   ├── 修改日志.md                  ← changelog，记录每次修改
    │   ├── 版本归档/                    ← 大版本快照
    │   ├── 写作进度.md                  ← 章节完成度追踪
    │   └── 交互记录.md                  ← 写作讨论日志
    ├── _drafts/                        ← 章节草稿、实验性片段（类似 feature branch）
    ├── _feedback/                      ← 反馈报告存档
    └── _references/
        ├── 参考文献表.md                ← 按用户选择的格式整理的文献列表
        └── attachments/                ← 电子版文献（PDF/EPUB）
```

**File-path naming note**: the directory and file names above use Chinese defaults, but English equivalents are equally valid. Use whichever matches the author's writing language — the structure is what matters, not the language of the labels.

### First-time initialization

On a user's first session, create the project folder following the structure above. Confirm:
- The paper title (used to name the folder and the main draft)
- The citation format (create the matching quick-reference file)
- Whether a draft already exists (if so, import it as v1.0)

---

## 2. Version Management

### Design philosophy

Borrow git's approach to versioning, but adapt it to the realities of academic writing:
- **Minor version = commit**: every meaningful change records its diff and reason
- **Major version = tag/release**: snapshot after completing a round of systematic revision
- **_drafts/ = feature branch**: experimental writing attempts that leave the main draft untouched

### Minor version (patch)

Trigger: a local change within a single conversation. Does not generate a snapshot file.

Record in the changelog:
```markdown
## vX.Y.Z · YYYY-MM-DD HH:MM
**修改范围**：[章节/段落位置]
**修改类型**：[论证重构/表达润色/引用修正/结构调整/新增内容]
**改动摘要**：一句话概括
**具体改动**：
> [!diff]
> - 原文：「...」
> + 修改：「...」
**修改理由**：[为什么这样改]
**验证状态**：[✅ 通过文风一致性检查 / ⚠️ 需作者确认]
```

### Major version (major)

Trigger conditions (any one):
- A chapter rewrite is complete
- The change covers more than 10% of the full text
- A complete chapter-level review has been finished and all its revisions applied
- The author explicitly asks for a version snapshot

Procedure:
1. Increment the version number (e.g., v1.5 → v2.0)
2. Copy the main draft to `_meta/版本归档/vX.Y_YYYYMMDD.md`
3. Update the `version` field in the main draft's frontmatter
4. Update the writing-progress table
5. Record a major-version summary in the changelog

### Using _drafts/

When the author wants to try an uncertain line of argument:
1. Create a new file in `_drafts/` (e.g., `_drafts/第三章_替代方案A.md`)
2. Experiment freely there
3. If the approach is adopted → merge it into the main draft and delete the draft
4. If abandoned → keep it as a record of thinking, or delete it

---

## 3. Reference Management

### Bibliographic information

All cited works are recorded in `_references/参考文献表.md`, including:
- Complete entries formatted in the citation style the user chose
- Citation-location markers (which chapters cite the work)
- Source markers for the electronic copy (📁 Drive / 📝 Vault note / ⚠️ to be obtained)
- Vault backlinks (where a corresponding reading note or concept card exists)

### Reference attachments
- Google Drive: a thematically organized e-book library (primary storage)
- Local attachments/: works cited frequently during active work

### Reference-retrieval workflow
When the user says "I need to cite 《XX》":
1. Check the reference list → 2. If a Drive marker exists, help download it → 3. Read the contents → 4. Format it into the user's configured citation style

### Bulk reference download and index building

When the author is about to begin a systematic revision, it is worth building a complete local reference library first:

1. **Extract the reference list**: pull all entries from the bibliography section of the main draft
2. **Search for each electronic copy in turn**:
   - Search Google Drive first (`google_drive_search`)
   - Then check whether the vault holds a PDF attached to a reading note
   - Mark works that cannot be obtained as ⚠️
3. **Download locally**: store every PDF found in `_references/attachments/`, following the naming rule `作者姓Year.pdf` (e.g., `Foucault1975.pdf`)
4. **Build a reference index**: create `_references/文献索引.md`; each entry holds its citation key, a one-sentence summary, core-concept keywords, the chapters that cite it, and the status of its local path
5. **Incremental updates**: update the index each time a new citation is added later

### Vault integration
- Reading notes: `[[《书名》读书笔记]]`
- Concept cards: `[[概念名]]`
- Person profiles: `[[人名]]`

---

## 4. Interaction Log

After every substantive writing discussion, append to `_meta/交互记录.md`:
- **Paper thread**: what was discussed, what decisions were made
- **Skill thread**: what needs surfaced, what improvements were made (if you are developing the skill in parallel)
- **Reflexive notes**: thoughts that could feed the paper's reflexive-critique chapter (where applicable)

### Session-state checkpoint

Before the end of any conversation with substantive progress (or when the AI senses the context may be nearing the compaction threshold), write a structured checkpoint into the interaction log. For the format, see the "Anti-Drift Protocol" section of SKILL.md.

The checkpoint exists so that, on cross-session resumption, the AI can quickly rebuild the full working context rather than relying on memory that may have been compacted away.

---

## 5. Inbox Integration

If the user's vault has an Inbox system, append a brief record to the Inbox after each edit to a paper file.

> How to decide: check whether the vault root holds a `SYSTEM.md` file. If so, read its Inbox rules and follow them. If there is no `SYSTEM.md`, or it defines no Inbox, skip this step to avoid duplicate records.

---

## 6. Export Workflow

Once the paper is finished, export according to the user's choice:
- **.docx**: invoke the docx skill
- **.pdf**: invoke the pdf skill
- **.tex**: generate a LaTeX source file (confirm the template with the user)
- Run the academic-writing checklist before exporting
