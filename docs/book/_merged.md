# 《The Art of Linear Algebra》互動式 md 化進度追蹤

> **本檔用途：** S02–S08 各章撰寫狀態、各章圖檔對映、整體目錄。
> **不是書本內容**，書本內容在各 `ch*.md` 子檔。
> S09 會把所有 `ch*.md` 合併成最終 `BOOK.md`。

---

## 進度總覽

| Session | 章節 | md 檔 | 狀態 |
|---|---|---|---|
| S02 | §1 Viewing a Matrix - 4 Ways | `ch01-viewing-matrix.md` | [ ] |
| S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md` | [ ] |
| S04 | §3 Matrix × Vector - 2 Ways | `ch03-mat-vec.md` | [ ] |
| S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md` | [ ] |
| S05 | §5 Practical Patterns | `ch05-patterns.md` | [ ] |
| S06 | §6 5 Factorizations 總覽 | `ch06a-five.md` | [ ] |
| S06 | §6.1 A = CR | `ch06b-CR.md` | [ ] |
| S06 | §6.2 A = LU | `ch06c-LU.md` | [ ] |
| S07 | §6.3 A = QR | `ch06d-QR.md` | [ ] |
| S07 | §6.4 S = QΛQᵀ | `ch06e-QLQ.md` | [ ] |
| S07 | §6.5 A = UΣVᵀ | `ch06f-USV.md` | [ ] |
| S08 | Foreword | `front-foreword.md` | [ ] |
| S08 | Conclusion + References | `back-conclusion.md` | [ ] |
| S08 | 附錄 Map of Eigenvalues | `appendix-map-eigenvalues.md` | [ ] |
| S08 | 附錄 Matrix World | `appendix-matrix-world.md` | [ ] |
| S09 | 合併版 | `BOOK.md` | [ ] |

---

## 章節 ↔ 圖檔對映（供 S02–S08 撰寫時查表）

從 `The-Art-of-Linear-Algebra.tex` 抓出，圖檔在 `figs-png/<name>.png`，原始 EPS 在 `figs/<name>.eps`。

### §1 Viewing a Matrix - 4 Ways
- `ViewingMatrix-4Ways`

### §2 Vector × Vector - 2 Ways
- `VectorTimesVector`

### §3 Matrix × Vector - 2 Ways
- `MatrixTimesVector`
- `VectorTimesMatrix`
- `4-Subspaces`

### §4 Matrix × Matrix - 4 Ways
- `MatrixTimesMatrix`

### §5 Practical Patterns
- `Pattern12`
- `Pattern11-22`
- `Pattern3`
- `Pattern4`

### §6 The Five Factorizations of a Matrix（總覽）
- `A_CR`、`A_LU`、`A_QR`、`A_QLQT`、`A_USVT`（五張小縮圖）

### §6.1 A = CR
- `CR1`
- `CR2`

### §6.2 A = LU
- `LU1`
- `LU2`

### §6.3 A = QR
- `QR`

### §6.4 S = QΛQᵀ
- `EVD`

### §6.5 A = UΣVᵀ
- `SVD`

### 附錄
- `MapofEigenvalues`
- `MatrixWorld`
- `TheFourSubspaces`
- `5-Factorizations`（總圖）

---

## 撰寫前必讀

1. `docs/book/SCHEMA.md` — 寫作格式規範
2. `docs/book/from-tex/en.md` — pandoc 從英文 .tex 轉的 md（含 LaTeX 公式原文）
3. `docs/book/from-tex/zh.md` — pandoc 從簡中 .tex 轉的 md（翻譯參考）
4. `docs/book/from-pdf/en.txt` — pdftotext 從英文 PDF 抽的純文字（補 pandoc 缺漏）
5. `docs/book/from-pdf/zh.txt` — pdftotext 從簡中 PDF 抽的純文字
6. `docs/book/figs-png/` — 50 張 PNG 圖檔（含日文/中文版的相同圖，用主名挑非 -j 的）

---

## 撰寫後動作

完成一章 md 後：
- 在本檔對應行勾選 `[x]`
- 在 `docs/dev/HANDOFF.md` 記錄該章完成
- 在 `docs/dev/CURRENT_SESSION.log` 加一行紀錄
