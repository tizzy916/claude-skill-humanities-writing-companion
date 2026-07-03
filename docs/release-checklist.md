# Release Checklist

> **Language / 语言**: **English (current)** · [中文](release-checklist.zh.md)

Purpose: prevent the "released locally, nothing happened online" break. Every release of this
repository walks this list top to bottom, in order — no step is optional, and no step is
"obviously done already." Replace `X.Y.Z` with the version being released.

---

## 1 · Version metadata

- [ ] `CITATION.cff`: bump `version` to `X.Y.Z` **and** set `date-released` to the release date
- [ ] `README.md` BibTeX block: `version={X.Y.Z}`
- [ ] `README.zh.md` BibTeX block: `version={X.Y.Z}` (must match the English README exactly)
- [ ] `CHANGELOG.md`: add the new `[X.Y.Z] — YYYY-MM-DD` entry at the top (Keep a Changelog format)

## 2 · Consistency sweeps

- [ ] Grep the whole repository for the **previous** version number and confirm no stale references remain (CHANGELOG history entries are the only legitimate hits):

  ```bash
  grep -rn "OLD_VERSION" --exclude-dir=.git .
  ```

- [ ] Bilingual mirror sync check — for every EN/ZH file pair, the heading counts must match:

  ```bash
  for f in README CONTRIBUTING; do
    echo "$f: $(grep -c '^#' $f.md) vs $(grep -c '^#' $f.zh.md)"
  done
  # Repeat for SKILL.md/SKILL.zh.md, scripts/README(.zh).md,
  # and every pair under references/ and docs/
  ```

## 3 · Tests

- [ ] `scripts/tests/run_tests.sh` passes with no failures

## 4 · Ship

- [ ] Commit all release changes
- [ ] Tag: `git tag vX.Y.Z` (annotated tag with a one-line release summary recommended)
- [ ] Push **including the tag**: `git push && git push --tags`

## 5 · Post-release verification (online)

- [ ] Zenodo archive check: a new version appears under the Concept DOI
      [10.5281/zenodo.20280773](https://doi.org/10.5281/zenodo.20280773), a version-specific DOI
      is minted, and the metadata (title / version / abstract) matches `CITATION.cff` and `.zenodo.json`
- [ ] Verify the GitHub release page for `vX.Y.Z`: release notes render correctly, the tag points
      at the intended commit, and the README DOI badge / "Cite this repository" button resolves
      to the latest release

> Note: the Zenodo↔GitHub integration archives on the **GitHub release event**, not on the tag
> push alone — if step 5's Zenodo check fails, first confirm a GitHub release (not just a tag)
> actually exists for `vX.Y.Z`.
