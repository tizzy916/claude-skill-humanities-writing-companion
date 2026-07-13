# 发布流程清单

> **Language / 语言**: [English](release-checklist.md) · **中文（当前）**

目的：防止「本地已发版、线上没发生」的断裂。本仓库每次发版都从上到下走完这份清单，
按顺序执行——没有可跳过的步骤，也没有"显然已经做过"的步骤。把 `X.Y.Z` 替换为本次发布的版本号。

---

## 1 · 版本元数据

- [ ] `CITATION.cff`：`version` 升到 `X.Y.Z`，**并且** `date-released` 改为发布日期
- [ ] `README.md` BibTeX 块：`version={X.Y.Z}`
- [ ] `README.zh.md` BibTeX 块：`version={X.Y.Z}`（必须与英文 README 完全一致）
- [ ] `CHANGELOG.md`：在顶部新增 `[X.Y.Z] — YYYY-MM-DD` 条目（Keep a Changelog 格式）

## 2 · 一致性扫描

- [ ] 全仓 grep **上一个**版本号，确认没有残留（CHANGELOG 的历史条目是唯一合法命中）：

  ```bash
  grep -rn "OLD_VERSION" --exclude-dir=.git .
  ```

- [ ] 双语镜像同步检查——每对中英文文件的标题数必须一致：

  ```bash
  for f in README CONTRIBUTING; do
    echo "$f: $(grep -c '^#' $f.md) vs $(grep -c '^#' $f.zh.md)"
  done
  # 对 SKILL.md/SKILL.zh.md、scripts/README(.zh).md、
  # 以及 references/ 与 docs/ 下的每一对文件重复此检查
  ```

## 3 · 测试

- [ ] `scripts/tests/run_tests.sh` 全部通过、零失败

## 4 · 发布

- [ ] 提交本次发版的全部改动（commit）
- [ ] 打标签：`git tag vX.Y.Z`（建议使用带一行发版摘要的 annotated tag）
- [ ] 推送**含标签**：`git push && git push --tags`

## 5 · 发布后线上核对

- [ ] Zenodo 归档核对：Concept DOI
      [10.5281/zenodo.20280772](https://doi.org/10.5281/zenodo.20280772) 下出现新版本、
      铸出版本专属 DOI，且元数据（标题 / 版本 / 摘要）与 `CITATION.cff` 和 `.zenodo.json` 一致
- [ ] 验证 `vX.Y.Z` 的 GitHub release 页面：发布说明正常渲染、标签指向预期的 commit、
      README 的 DOI 徽章 / "Cite this repository" 按钮解析到最新版本

> 注意：Zenodo↔GitHub 集成在 **GitHub release 事件**时归档，仅推送 tag 不会触发——
> 如果第 5 步的 Zenodo 核对失败，先确认 `vX.Y.Z` 确实存在 GitHub release（而不只是一个 tag）。
