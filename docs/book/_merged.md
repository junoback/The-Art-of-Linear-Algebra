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
| S06 | §5 Practical Patterns | `ch05-patterns.md` | [x] | 2 / 1 / 1 | [x] | [x] |
| S07 | §6 5 Factorizations 總覽 + §6.1 A=CR | `ch06a-five.md`, `ch06b-CR.md` | [x] | 總覽 1/0/0 + CR 1/1/1 | [x] | [x] |
| S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`, `ch06d-QR.md` | [x] | LU 1/1/1 + QR 1/1/1 | [x] | [x] |
| S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`, `ch06f-USV.md` | [x] | EVD 1/1/1 + SVD **1 Tier3 + 1 Tier2 / 1 / 1** | [x] | [x] |
| S10 | Foreword + Conclusion + 3 附錄（MapofEigenvalues / MatrixWorld / TheFourSubspaces）| `front-foreword.md`, `back-conclusion.md`, `appendix-map-eigenvalues.md`, `appendix-matrix-world.md`, `appendix-four-subspaces.md` | [x] | 0+0+0 / **MatrixWorld 1** / 0 + **Map 0/1/0** + **4Sub 0/1/0** = 合計 **1 / 2 / 0**（Matrix World 旗艦 Tier 2）| [x] 3 VizScript | [x] |
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

### §6.4 S = QΛQᵀ（S09 ✅，PNG 標 **using P4**）
- `EVD`（標 `using P4`，單 pointer 指 ch05 VizScript-03）
- `A_QLQT`（縮圖，無標記）

### §6.5 A = UΣVᵀ（S09 ✅，PNG 標 **using P4**，**全書最長章 + 唯一 Tier 3 主 VizScript**）
- `SVD`（標 `using P4`，**雙 pointer 主 ch04 VizScript-02 + 副 ch05 VizScript-03**）
- `A_USVT`（縮圖，無標記）

### 附錄與封面（S10 ✅，3 張附錄 PNG **皆無 `using XX` 標記**）
- `MapofEigenvalues`（**無 using 標記** — 12 類矩陣 × 特徵值幾何位置「分類地圖」，[appendix-map-eigenvalues.md](appendix-map-eigenvalues.md) ⭐⭐ Tier 1 + pointer 指 ch06e）
- `MatrixWorld`（**無 using 標記** — 圖內標 Strang 書 section number 1.4/7.1/4.4/6.2/6.3 等，[appendix-matrix-world.md](appendix-matrix-world.md) ⭐⭐⭐ **Tier 2 旗艦** — S12+ 全書互動式教材首頁）
- `4-Subspaces`（與 ch03 同款，**無 using 標記**，[appendix-four-subspaces.md](appendix-four-subspaces.md) ⭐⭐ Tier 1 + pointer 指 ch03 V-02 + ch06f V-03）
- **散文章節（Foreword / Conclusion）：** [front-foreword.md](front-foreword.md) 0 VizMark / [back-conclusion.md](back-conclusion.md) 0 VizMark + 全書 33 個 VizScript 總覽段（S11 整合的橋樑）

### S10 PNG `using XX` 標記重核總結（HANDOFF 預估推翻）

| PNG | HANDOFF 預估 | S10 實際 | 結論 |
|---|---|---|---|
| MapofEigenvalues | 「可能標 P3」（動態系統）| **無 using 標** | 是「分類地圖」非 Pattern 套用 |
| MatrixWorld | 「無 using 標」 | **無 using 標**（圖內是 Strang section number）| 是「全書地圖」非 Pattern 套用 |
| 4-Subspaces | 「無 using 標」 | **無 using 標** | 是「基本概念圖」非 Pattern 套用 |

**S10 規律：** 附錄 PNG 是「**地圖層級 / 基本概念圖**」，與 §6 主章 PNG 標 `using PX/MMX` 不同譜系。附錄重「**整合性 + pointer 到主章**」，不重複實作主章已完成的 VizScript。

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
| 附錄 | **3 個（實際）** | **1（MatrixWorld 旗艦 Tier 2）** |
| **總計（實際 S02–S10 收尾）** | **33** | **~13–14 高優先級（2 Tier 3 旗艦 + ~10 Tier 2 主章 + 1 Matrix World 附錄旗艦）** |

S12+ 從 ⭐⭐⭐ Tier 3 旗艦 2 個（[ch04 V-02](ch04-mat-mat.md#vizscript-02) Mona Lisa MM4、[ch06f V-01](ch06f-USV.md#vizscript-01) SVD Master）+ Tier 2 主章 + Matrix World 旗艦地圖開始實作，每個 Tier 3 估 3 session、Tier 2 估 2 session → **互動式 PoC 階段需 ~28–30 session**。

整個專案總視野：S00–S11 + S12–S40 ≈ **約 38–40 session 完成全書互動化**（含技術棧 PoC 初期 ~3 session）。

---

## S10 完成里程碑（§1–§6 + 序言 + 結論 + 3 附錄 = 全書 md 化 100%）

| 項目 | 數值 |
|---|---|
| 章節 md 檔總數 | **13 個** = ch01–ch06f（9 個主章）+ front-foreword + back-conclusion + 3 個附錄 |
| 總行數（粗估）| **~8100 行** = 6824（主章）+ 1290（S10 5 檔）|
| VizScript 總數 | **36 個** = 主章 33 個（§1=2, §2=2, §3=4, §4=4, §5=4, §6 總覽=1, §6.1=3, §6.2=3, §6.3=3, §6.4=3, §6.5=4，合計 33）+ 3 附錄各 1 = **36** |
| Tier 3 旗艦數 | **2 個**（ch04 V-02 Mona Lisa + ch06f V-01 SVD Master）|
| Tier 3 候選數 | **1 個**（ch03 V-02 4 子空間，S12+ 視實作時間升級）|
| Tier 2 旗艦地圖 | **1 個**（appendix-matrix-world V-01，S12+ 全書互動式教材首頁）|
| `using XX` PNG 標記譜系完整地圖 | **CR1=P1 / CR2=P2 / LU1=無 / LU2=MM4 / QR=P1 / EVD=P4 / SVD=P4 / 3 附錄=無**（共 10 張 §6+附錄 PNG）|
| 雙 pointer VizScript | **2 個**（[ch06b V-01](ch06b-CR.md#vizscript-01) CR 對偶 + [ch06f V-01](ch06f-USV.md#vizscript-01) SVD 集大成）|
| 撰寫工期 | **S00–S10 共 11 個 session，2026-05-11 至 2026-05-12，~20h 純撰寫**（含 PNG 重核 + SOP 累積）|
