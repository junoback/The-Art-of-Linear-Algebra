# 《The Art of Linear Algebra》互動式 md 化進度追蹤

> **本檔用途：** S02–S10 各章撰寫狀態、各章圖檔對映、視覺化標記計數、整體目錄。
> **不是書本內容**，書本內容在各 `ch*.md` 子檔。
> S11 會把所有 `ch*.md` 合併成最終 `BOOK.md`，並抽出全書 VizScript 彙整成 `VIZ-CATALOG.md`。

---

## 進度總覽（方案 A：整合 VizMark + VizScript 進章節 session）

| Session | 章節 | md 檔 | 描述 | VizMark | VizScript | 狀態 |
|---|---|---|---|---|---|---|
| S02 | §1 Viewing a Matrix - 4 Ways | `ch01-viewing-matrix.md` | [x] | 1 / 1 / 0 | [x] | [x] |
| S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md` | [x] | 1 / 1 / 0 | [x] | [x] |
| S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces） | `ch03-mat-vec.md` | [x] | 2 / 1 / 1 | [x] | [x] |
| S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md` | [x] | 2 / 1 / 1 | [x] | [x] |
| S06 | §5 Practical Patterns | `ch05-patterns.md` | [ ] | / / / | [ ] | [ ] |
| S07 | §6 5 Factorizations 總覽 + §6.1 A=CR | `ch06a-five.md`, `ch06b-CR.md` | [ ] | / / / | [ ] | [ ] |
| S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`, `ch06d-QR.md` | [ ] | / / / | [ ] | [ ] |
| S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`, `ch06f-USV.md` | [ ] | / / / | [ ] | [ ] |
| S10 | Foreword + Conclusion + 附錄（MapofEigenvalues / MatrixWorld） | `front-foreword.md`, `back-conclusion.md`, `appendix-*.md` | [ ] | / / / | [ ] | [ ] |
| S11 | 整合 + 校對 + 統一 + `BOOK.md` + `VIZ-CATALOG.md` | — | [ ] | — | — | [ ] |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 | （延後） | — | — | — | [ ] |

**VizMark 計數格式：** `⭐⭐⭐ × n / ⭐⭐ × n / ⭐ × n`，例如 `2/3/1`。

---

## 章節 ↔ 圖檔對映（供 S02–S10 撰寫時查表）

從 `The-Art-of-Linear-Algebra.tex` 抓出，圖檔在 `figs-png/<name>.png`，原始 EPS 在 `figs/<name>.eps`。

### §1 Viewing a Matrix - 4 Ways（S02）
- `ViewingMatrix-4Ways`

### §2 Vector × Vector - 2 Ways（S03）
- `VectorTimesVector`

### §3 Matrix × Vector - 2 Ways（S04）
- `MatrixTimesVector`
- `VectorTimesMatrix`
- `4-Subspaces`

### §4 Matrix × Matrix - 4 Ways（S05）
- `MatrixTimesMatrix`

### §5 Practical Patterns（S06）
- `Pattern12`
- `Pattern11-22`
- `Pattern3`
- `Pattern4`

### §6 The Five Factorizations of a Matrix - 總覽（S07）
- `5-Factorizations`（總圖）
- `A_CR`、`A_LU`、`A_QR`、`A_QLQT`、`A_USVT`（五張小縮圖）

### §6.1 A = CR（S07）
- `CR1`
- `CR2`

### §6.2 A = LU（S08）
- `LU1`
- `LU2`

### §6.3 A = QR（S08）
- `QR`

### §6.4 S = QΛQᵀ（S09）
- `EVD`

### §6.5 A = UΣVᵀ（S09）
- `SVD`

### 附錄與封面（S10）
- `MapofEigenvalues`
- `MatrixWorld`
- `TheFourSubspaces`

---

## 撰寫前必讀

1. `docs/book/SCHEMA.md` — 章節 md 結構與圖片描述格式
2. `docs/book/VIZ_SCHEMA.md` — VizMark 標記與 VizScript 劇本格式（含 800 字範例）
3. `docs/book/from-tex/en.md` — pandoc 從英文 .tex 轉的 md（含 LaTeX 公式原文）
4. `docs/book/from-tex/zh.md` — pandoc 從簡中 .tex 轉的 md（翻譯參考）
5. `docs/book/from-pdf/en.txt` — pdftotext 從英文 PDF 抽的純文字（補 pandoc 缺漏）
6. `docs/book/from-pdf/zh.txt` — pdftotext 從簡中 PDF 抽的純文字
7. `docs/book/figs-png/` — 50 張 PNG 圖檔（含日文/中文版的相同圖，用主名挑非 -j 的）

---

## 章節 session 撰寫流程（S02–S10 統一）

1. 抓本章 LaTeX 結構（標題、公式、圖清單）
2. 看 PNG 圖檔 → 寫四欄位描述
3. **同步**判斷視覺化機會 → 插 VizMark
4. **章末**寫每個 VizMark 對應的 VizScript（800 字細緻劇本）
5. 寫章節摘要 + 數學要點
6. 在本檔對應行勾選 `[x]` 並填 VizMark 計數
7. 更新 HANDOFF.md + CURRENT_SESSION.log

---

## VizScript 計數預估（給 S11 / S12+ 預期容量參考）

| 章節 | 預估 VizMark 數 | 預估高優先級數 |
|---|---|---|
| §1 4 ways viewing | 2–3 | 1 |
| §2 vec × vec | 2–3 | 1 |
| §3 mat × vec（含 4-subspaces）| 3–5 | 2 |
| §4 mat × mat | 3–5 | 2 |
| §5 patterns | 2–4 | 1 |
| §6 5-factorizations 總覽 | 1–2 | 1 |
| §6.1 CR | 2–3 | 1 |
| §6.2 LU | 2–3 | 1 |
| §6.3 QR | 2–3 | 1 |
| §6.4 QΛQᵀ | 2–3 | 1 |
| §6.5 UΣVᵀ | 2–3 | 1 |
| 附錄 | 1–2 | 0–1 |
| **總計** | **24–39** | **13–14** |

S12+ 從 ⭐⭐⭐ 高優先級 13–14 個劇本開始挑題目實作，每個 Tier 2 估 1.5 session → **互動式 PoC 階段需 ~20 session**。

整個專案總視野：S00–S11 + S12-S31 ≈ **約 32 session 完成全書互動化**。
