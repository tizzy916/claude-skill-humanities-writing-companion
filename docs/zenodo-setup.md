# 申请 Zenodo DOI · 操作指南

> **目的**：让本 skill 在学术论文中**可被正式引用**（带永久 DOI）。
> **耗时**：首次约 5 分钟，之后每次 release 自动 mint 新 DOI。
> **前置已完成**：`.zenodo.json` 配置文件已在仓库根目录，含完整元数据。
> **操作主体**：你需要登录自己的 GitHub + Zenodo 账户做这些步骤——这些步骤涉及账户授权，工具不能代做。

---

## 一次性设置（5 分钟）

### Step 1 · 注册 / 登录 Zenodo

访问 https://zenodo.org → 用 GitHub 账户登录（推荐，省去注册流程）。

如果你有 ORCID（学术界统一作者 ID），也可以绑定——这会让 DOI 上的作者身份更权威。没有的话可以先跳过，之后绑定也可以。

### Step 2 · 授权 Zenodo 访问 GitHub

登录 Zenodo 后访问：

**https://zenodo.org/account/settings/github/**

点击 **Connect** / **Authorize** 按钮，授予 Zenodo 访问你的 GitHub 仓库列表。

### Step 3 · 在 Zenodo 中"打开" 本仓库

授权后，Zenodo 会列出你的全部 GitHub 仓库。找到 `claude-skill-academic-writer`，把右侧开关从 **OFF** 切到 **ON**。

> ⚠️ 重要：开关打开**之后**创建的 release 才会被 Zenodo 自动 archive 并 mint DOI。已经存在的 v1.0.0 release **不会**被自动处理——下一步会重新发个 release。

### Step 4 · 创建 v1.0.1 release 触发 Zenodo 处理

在本地执行：

```bash
cd ~/Desktop/claude-skill-academic-writer
git tag -a v1.0.1 -m "v1.0.1 — first Zenodo-archived release"
git push origin v1.0.1

gh release create v1.0.1 \
  --title "v1.0.1 · first Zenodo-archived release" \
  --notes "Functional changes since v1.0.0: none.

This release exists to trigger Zenodo's first archive + DOI mint. \
All future releases will receive their own DOI via the .zenodo.json config."
```

### Step 5 · 等 1-2 分钟，回 Zenodo 看 DOI

回到 https://zenodo.org/account/settings/github/，找到 `claude-skill-academic-writer` 行——会出现一个 DOI 链接（形如 `10.5281/zenodo.NNNNNNN`）。

点击进入，确认元数据正确（应该用了 `.zenodo.json` 里的内容）。

### Step 6 · 把 DOI badge 加到 README

Zenodo 会给你一段 markdown badge 代码，类似：

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.NNNNNNN.svg)](https://doi.org/10.5281/zenodo.NNNNNNN)
```

把它加到 README.md 顶部的 badge 区（在 License 和 Status badge 旁边），然后 commit + push：

```bash
git add README.md
git commit -m "docs: add Zenodo DOI badge"
git push
```

### Step 7 · 更新 CITATION.cff 加上 DOI

把 DOI 也加到 `CITATION.cff` 的字段里：

```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.NNNNNNN
    description: "Zenodo archive of v1.0.1"
```

这样 GitHub 会自动识别并在仓库右侧侧栏显示"Cite this repository"按钮，点击后能直接复制 BibTeX / APA / Chicago 等格式。

---

## 之后每次 release（自动）

只要 Zenodo 开关保持 ON，之后 `gh release create` 创建的每个 release 都会**自动**：

1. 被 Zenodo archive（保存一份不可变快照）
2. 被赋予一个新的 DOI（每个版本一个 DOI）
3. 也有一个**版本无关的 concept DOI**——总是指向最新版

你不需要重复 Step 1-3。每次 release 即可。

---

## 对论文写作的意义

未来在自己的论文中（特别是论文的"研究方法"或"工具说明"节）可以这样引用：

```
本研究使用了 academic-writer Claude Skill (tizzy916, 2026, doi:10.5281/zenodo.NNNNNNN)
作为人-AI 协作写作的辅助框架……
```

或者 BibTeX：

```bibtex
@software{academic_writer_2026,
  author    = {tizzy916},
  title     = {academic-writer: A Claude Skill for Humanities and Social-Science Academic Writing},
  year      = 2026,
  publisher = {Zenodo},
  version   = {v1.0.1},
  doi       = {10.5281/zenodo.NNNNNNN},
  url       = {https://doi.org/10.5281/zenodo.NNNNNNN}
}
```

这一引用等同于学术界对"软件作为研究输出"的认可——和引用一篇期刊论文一样正式。

---

## 常见问题

### Q1 · Zenodo 收费吗？

不收费。它由 CERN 运营，欧盟资助，对开源软件 / 学术内容免费托管 + 免费 mint DOI。

### Q2 · 删除 release 会怎样？

DOI 永久有效。Zenodo archive 不会因为 GitHub 上删除 release 而消失——这正是 DOI 的意义。

### Q3 · 我可以编辑 Zenodo 上的元数据吗？

可以。每次 archive 之后，可以在 Zenodo 网页上手动编辑（如补充作者信息、更精细的关键词）。但**文件内容不可修改**——只能新发 release 来更新。

### Q4 · `.zenodo.json` 改了会自动同步吗？

下一次 release 时同步。已经 archive 过的 release 不会回溯更新。

### Q5 · ORCID 是什么？我需要吗？

ORCID（https://orcid.org）是学术界的"作者唯一身份证"，绑定后 DOI 上你的作者身份会被全球唯一标识。建议绑定，但不绑也可以发布。

---

## 你的具体下一步

1. 打开 https://zenodo.org/account/settings/github/
2. 找到 `claude-skill-academic-writer`，开关打 ON
3. 回到本地终端，执行 Step 4 中的命令创建 v1.0.1 release
4. 等 1-2 分钟，记下你拿到的 DOI 数字
5. 告诉我你的 DOI（或贴 Zenodo 链接给我），我帮你更新 README 的 badge + CITATION.cff
