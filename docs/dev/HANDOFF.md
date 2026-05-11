# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S03（§2 完成）
- **日期:** 2026-05-12
- **狀態:** `ch02-vec-vec.md` 完成（497 行，1 圖描述 + 2 VizMark + 2 VizScript 13 段 A-M）；驗證 ch01 範本可複用、撰寫速度穩定在 ~1h / 章；SOP_DRAFT.md 新增 §2.8「對比 / 對偶結構章節寫作模式」+ 全書視覺一致性錨點；下次 S04 從 §3 Matrix × Vector 開始（含 4-Subspaces）

---

## 專案目標（最高層）

把 Kenji Hiranabe 的《The Art of Linear Algebra》（基於 Gilbert Strang《Linear Algebra for Everyone》的圖解筆記）轉換為**互動式 Python 視覺化教材**：

- 原書中的圖解（5 大矩陣分解：CR / LU / QR / QΛQ' / UΣV'、向量/矩陣運算的 4 種觀點、特徵值地圖、Matrix World）轉成 Python 互動視覺化
- 公式可調整參數即時看到結果（互動式）
- 保留原書的「直覺優先」教學風格

---

## 當前工作狀態

### 已完成
- [x] **S00** 從 GitHub clone 原 repo、確認內容、session 管理系統初始化
- [x] **S01** 整體 md 化規劃定版（10 session 路線圖）
- [x] **S01** 機械轉換：pandoc `.tex` → md（英文 624 行 / 簡中 601 行），位於 `docs/book/from-tex/`
- [x] **S01** 機械轉換：PDF → 純文字（pdftotext 英 861 / 簡中 657 行；ghostscript txtwrite 對照版 `*-gs.txt`），位於 `docs/book/from-pdf/`
- [x] **S01** EPS → PNG 全部 50 張轉檔完成（ghostscript），位於 `docs/book/figs-png/`（共 888 KB）
- [x] **S01** 撰寫 `docs/book/SCHEMA.md`（章節格式 + 四欄位圖片描述規範）
- [x] **S01** 撰寫 `docs/book/_merged.md`（進度追蹤表 + 章節↔圖檔對映）
- [x] **S01** 工具備齊：pandoc 3.8.3、pdftotext (poppler) 26.04、ghostscript 10.0、epstopdf
- [x] **S01.5** 補規劃：撰寫 `VIZ_SCHEMA.md`（VizMark 5 型 + VizScript 13 段 A-M 格式，含 800 字範例）+ 修訂 SCHEMA.md + 重寫 `_merged.md` 路線圖（S02-S11）
- [x] **S02** §1 Viewing a Matrix - 4 Ways：`ch01-viewing-matrix.md`（418 行）— 1 圖描述 + 2 VizMark + 2 VizScript（VizScript-01 ⭐⭐⭐ + VizScript-02 ⭐⭐，各 13 段 A-M 完整）
- [x] **S02** 全書術語慣例 B 派 → A 派切換（**column = 列直立 / row = 行橫躺**，與華文主流一致）+ `SCHEMA.md` §3.1 規範更新 + SOP_DRAFT.md §2.4 教訓記錄
- [x] **S03** §2 Vector × Vector - 2 Ways：`ch02-vec-vec.md`（497 行）— 1 圖描述 + 2 VizMark + 2 VizScript（VizScript-01 ⭐⭐⭐ 外積→秩 1 矩陣 + VizScript-02 ⭐⭐ v1↔v2 對偶切換）；驗證 ch01 範本可複用、撰寫穩定 ~1h
- [x] **S03** SOP_DRAFT.md 新增 §2.8「對比 / 對偶結構章節寫作模式」+ 全書視覺一致性錨點（配色 hex / cell 尺寸 / 動畫時間統一化）+ 版本 0.4

### 進行中
- 無，S03 已收尾

### 待辦（多 session 路線圖 v2 — 方案 A 整合 VizMark+VizScript）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema（章節 / 視覺化）+ 路線圖補規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| ✅ S02 | §1 Viewing a Matrix - 4 Ways（驗證雙 Schema + A 派術語切換） | `ch01-viewing-matrix.md`（418 行，2 VizMark + 2 VizScript） |
| ✅ S03 | §2 Vector × Vector - 2 Ways（驗證 ch01 範本可複用 + 對比結構寫作模式） | `ch02-vec-vec.md`（497 行，2 VizMark + 2 VizScript） |
| **→ S04** | §3 Matrix × Vector - 2 Ways（含 4-Subspaces） | `ch03-mat-vec.md` |
| S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md` |
| S06 | §5 Practical Patterns | `ch05-patterns.md` |
| S07 | §6 5 Factorizations 總覽 + §6.1 A=CR | `ch06a-five.md`、`ch06b-CR.md` |
| S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`、`ch06d-QR.md` |
| S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`、`ch06f-USV.md` |
| S10 | Foreword + Conclusion + 附錄 | `front-foreword.md`、`back-conclusion.md`、`appendix-map-eigenvalues.md`、`appendix-matrix-world.md` |
| S11 | 整合 + 校對 + 統一 + `BOOK.md` + `VIZ-CATALOG.md` | 合併版書 + 視覺化候選池目錄 |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 PoC | （延後到 S11 後再細規劃，預估 ~20 session）|

### S04 起步建議

1. **先讀 `docs/book/SCHEMA.md` + `docs/book/VIZ_SCHEMA.md`** 複習雙規範（3 分鐘，已 internalize 可跳過）
2. **掃 `ch02-vec-vec.md` §2 對偶段 + VizScript-02 動畫腳本**抓「對比結構章節」的格式（直接複用到 §3 dot-way vs combination-way）
3. **遵 SOP §2.8 全書視覺錨點**：配色 hex 沿用（綠 `#2ca02c` / 粉紅 `#d62728` / 藍 `#1f77b4`）、cell 60×60 px、動畫 400–700ms，不要重發明
4. 從 `from-tex/en.md` 抓 §3 部分（line 69–103 附近，含 MatrixTimesVector + VectorTimesMatrix + 4-Subspaces 三張圖）+ `from-pdf/en.txt`
5. 看三張 PNG（`MatrixTimesVector.png` / `VectorTimesMatrix.png` / `4-Subspaces.png`），用 Read tool 多模態直接讀
6. 寫 `ch03-mat-vec.md`：
   - (Mv1) 行向量 × 列 = 點積方式
   - (Mv2) 列向量的線性組合方式
   - (vM1) (vM2) 左乘對偶
   - 4-Subspaces 概念引入（C(A) / N(A) / C(Aᵀ) / N(Aᵀ)）— **這是本書最重要的概念之一，可能 ⭐⭐⭐ × 2**
7. VizMark 預估：3-5 個，⭐⭐⭐ × 2（線性組合動畫 + 4-Subspaces 空間幾何）

### 工件清單（S04+ 撰寫前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式（A 派術語） |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段 A-M 格式（含 800 字範例） |
| `docs/book/_merged.md` | 章節進度追蹤 + 章節↔圖檔對映表 + VizMark 計數 |
| `docs/book/ch01-viewing-matrix.md` | **S02 成稿，A 派術語的參考範本**（單視角章節） |
| `docs/book/ch02-vec-vec.md` | **S03 成稿，對比 / 對偶結構章節範本**（多視角章節，§3 §4 §6 可複用） |
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready）|
| `docs/dev/sop/SOP_DRAFT.md` | §2.8 全書視覺一致性錨點（配色 / 尺寸 / 動畫時間）— **S04+ 直接沿用，不重發明** |

---

## 關鍵決策記錄

| 日期 | 決策 | 原因 |
|------|------|------|
| 2026-05-11 | 啟用跨 session 管理系統 | 使用者明確表示這是長期跨多 session 專案 |
| 2026-05-11 | 不修改原 repo 的 LaTeX/PPT 檔案 | 原檔是書的成品，互動式版本應該是新增層而非取代 |
| 2026-05-12 | 全書 md 化路線：機械轉換 + 圖片詳細描述 | 原書本質是圖解，純文字 md 無法傳達內容，需逐圖寫描述 |
| 2026-05-12 | 描述語言：繁體中文，術語括號保留英文（例：列空間 (column space)） | 使用者偏好繁中，但保留英文術語便於對照原書與通用文獻 |
| 2026-05-12 | 範圍：英文版 + 簡中版兩語並做，跳過日文版 | 使用者選擇方案 2（雙語），日文版主要差異是翻譯不影響視覺化 |
| 2026-05-12 | 圖片描述格式採四欄位 schema：視覺結構/數學內容/直覺解讀/視覺化機會（VizMark） | 後三欄位對應未來 Python 視覺化的圖形、計算、互動三層 |
| 2026-05-12 | **S01.5 補規劃**：方案 A — 章節 session 整合「描述 + VizMark + VizScript」三類工作 | 視覺化劇本品質強烈依賴對圖的深度理解，分離反而會浪費；+3 session 屬可接受比例 |
| 2026-05-12 | **VizScript 細緻度：細版 ~800 字 / 個（13 段 A-M 固定格式）** | 目標是直接餵 LLM 生 Python 程式不需補充細節，避免 S12+ 實作時來回問細節 |
| 2026-05-12 | 新增 `VIZ_SCHEMA.md` + `VIZ-CATALOG.md`（S11 產出） | VizMark 散在各章便於閱讀；VIZ-CATALOG 集中彙整供 S12+ 挑題目實作 |
| 2026-05-12 | 章節切分微調：§5 獨立 1 session、§6 拆 3 session（總覽+CR / LU+QR / QΛQᵀ+UΣVᵀ）| 視覺化工作量讓每 session 章節密度降為 ~0.7 章 |
| 2026-05-12 | git origin 是上游 junoback repo，**收工 commit 留本地不 push** ~~已撤銷 (2026-05-12 S03 末)~~ | 防誤推到別人 repo；建議 fork 或抽出獨立 repo 後再 push |
| 2026-05-12 | **S03 末撤銷上條：確認 `junoback/The-Art-of-Linear-Algebra` GitHub repo 即為使用者本人（Back Kuo）的 fork，push 到 origin/main 安全** | 使用者直接授權；S02 + S03 共 2 commit 已 push（含 `docs/dev/` session 管理檔案公開可見）。之後可正常 `git push` 不需再問 |
| 2026-05-12 | **S02 中途決策變更：術語慣例改採華文主流 A 派（column = 列直立 / row = 行橫躺）** | 與中國大陸、日本、多數 Python 中文文件、本書簡中譯本一致；台灣本土教科書傳統採 B 派正好相反，本書讀者若來自此背景需校準。`SCHEMA.md` §3.1 + `ch01` 全部已對齊 A 派；後續 S03+ 章節直接照 A 派寫 |
| 2026-05-12 | SOP_DRAFT.md 新增「術語慣例必須在 S01 鎖死」教訓條 | S02 中途改 A 派付出整檔重寫 0.5h 成本；若拖到 S05+ 全書反轉成本會幾何級數膨脹 |
| 2026-05-12 | **S03 確立「全書視覺一致性錨點」（SOP §2.8）：配色 hex / cell 尺寸 / 動畫時間統一化** | S04+ 撰寫 VizScript 時直接套用，不重新發明，除非特殊章節（如 SVD 需要 colormap 表達 σ 大小）才允許偏離 |
| 2026-05-12 | **S03 確立「對比 / 對偶結構章節寫作模式」：§ 數學要點 加對比段 + 直覺段提煉記憶口訣** | §3（dot way vs combination way）、§4（4 ways）、§6（5 大分解）均適用同一格式，減少每章設計成本 |

---

## 檔案變更追蹤

### S00 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/dev/HANDOFF.md | 新增 | Session 交接文件 |
| docs/dev/SESSION_INDEX.md | 新增 | Session 索引 |
| docs/dev/CURRENT_SESSION.log | 新增 | 即時記錄 |
| docs/dev/sop/SOP_DRAFT.md | 新增 | SOP 草稿 |

### S01 + S01.5 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/SCHEMA.md | 新增 | 章節 md 結構 + 圖片四欄描述格式（S01.5 升級「互動化提示」為 VizMark 引用） |
| docs/book/VIZ_SCHEMA.md | 新增（S01.5） | VizMark 標記 + VizScript 13 段細緻劇本格式（含 800 字範例） |
| docs/book/_merged.md | 新增 / 重寫（S01.5）| 章節進度追蹤 + 章節↔圖檔對映 + VizMark 計數欄；新 S02-S11 路線圖 |
| docs/book/from-tex/en.md | 新增 | pandoc 英文 .tex → md（624 行） |
| docs/book/from-tex/zh.md | 新增 | pandoc 簡中 .tex → md（601 行） |
| docs/book/from-pdf/en.txt | 新增 | pdftotext 英文 PDF → 純文字（861 行）|
| docs/book/from-pdf/zh.txt | 新增 | pdftotext 簡中 PDF → 純文字（657 行）|
| docs/book/from-pdf/{en,zh}-gs.txt | 新增 | ghostscript txtwrite 對照版本 |
| docs/book/figs-png/*.png | 新增 | 50 張 PNG（從 EPS 轉，888 KB） |
| docs/book/*.pdf | 新增 | 5 個 PDF 副本（書本 3 語版 + 2 個附錄圖）|
| docs/dev/RETROSPECTIVE.md | 新增 | 對話反思（S00-S01） |
| docs/dev/sop/SOP_DRAFT.md | 修改 | 第二章新增工具鏈替代方案、雙語處理、不修改原 repo 規範 |

### S02 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/ch01-viewing-matrix.md | 新增 | **§1 章節 md：418 行**，含 1 圖描述 + 2 VizMark + 2 VizScript（13 段 A-M 各完整）；A 派術語 |
| docs/book/SCHEMA.md | 修改 | §3.1 術語對照表方向反轉（B 派 → A 派）+ 補 column vector / column space / row space 翻譯規則 |
| docs/book/_merged.md | 修改 | S02 標記 `[x]` 完成，VizMark 計數 `1 / 1 / 0` |
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.3 升級 VizMark 引用 / §2.4 改 A 派 + 補教訓 / 新增 §2.6 章節 session 流程 + §2.7 收工流程 |
| docs/dev/CURRENT_SESSION.log | 修改 | S02 即時記錄 + 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S02 一行 |

### S03 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/ch02-vec-vec.md | 新增 | **§2 章節 md：497 行**，含 1 圖描述 + 2 VizMark + 2 VizScript（13 段 A-M 各完整）；A 派術語；新增「對偶關係段」格式 |
| docs/book/_merged.md | 修改 | S03 標記 `[x]` 完成，VizMark 計數 `1 / 1 / 0` |
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.6 補 §2 耗時資料點 + 新增 §2.8「對比 / 對偶結構章節寫作模式」+ 全書視覺一致性錨點 + 版本 0.4 |
| docs/dev/CURRENT_SESSION.log | 修改 | S03 啟動 + 即時記錄 + 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S03 一行 |

---

## 技術筆記

### Repo 原始內容概覽
- **LaTeX 主檔**：`The-Art-of-Linear-Algebra.tex`（英文）、`-j.tex`（日文）、`-zh-CN.tex`（簡中）
- **編好的 PDF**：三種語言版本均已存在（不需重新編譯也可閱讀）
- **圖檔來源**：`Illustrations.pptx`（PowerPoint），透過 makefile 流程印成 PS → EPS → 嵌入 LaTeX
- **編譯需求**（如需重編 PDF）：MacTeX（uplatex + dvipdfmx）、psutils（psselect）、ps2eps、PowerPoint（印 PS）

### 互動式版本技術選項（S12+ 決策，目前傾向）
| 方案 | 優點 | 缺點 |
|------|------|------|
| **Marimo + matplotlib + marimo.ui**（S02/S03 VizScript 首選） | 反應式 notebook、純 Python、可匯出 HTML | 較新生態系較小 |
| Streamlit + Plotly | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

### 全書術語慣例（A 派 — 華文主流）

| 英文 | 中文 | 視覺方向 |
|---|---|---|
| matrix | 矩陣 | — |
| row | 行 | 橫躺 |
| column | 列 | 直立 |
| row vector | 行向量 | 橫躺 |
| column vector | 列向量 | 直立 |
| row space | 行空間 $\mathbf{C}(A^{\mathrm{T}})$ | — |
| column space | 列空間 $\mathbf{C}(A)$ | — |
| rank | 秩 | — |
| subspace | 子空間 | — |
| basis | 基底 | — |
| linear combination | 線性組合 | — |
| dot product / inner product | 點積 / 內積 | — |
| outer product | 外積（→ 秩 1 矩陣）| — |
| factorization | 分解 | — |
| eigenvalue / eigenvector | 特徵值 / 特徵向量 | — |
| singular value | 奇異值 | — |

**矩陣尺寸：** $A \in \mathbb{R}^{m \times n}$ 表示 **$m$ 行 $n$ 列**（$m$ rows, $n$ columns）。$m$ = 行數、$n$ = 列數。

### 全書視覺一致性錨點（S03 確立，S04+ 直接沿用）

- **配色 hex：** 綠（列 / 直立）`#2ca02c`、粉紅 / 紅（行 / 橫躺）`#d62728`、藍點（個別數字）`#1f77b4`、灰填充 `#eeeeee` / 框 `#333333`
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **動畫時間：** 視角切換 400–700ms、平行性高亮淡入 200ms、緩動 ease-in-out
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$

### S03 撰寫速度資料點

- **S02 §1（含 A 派切換重寫 0.5h）：** 1.5h / 418 行
- **S03 §2（ch01 範本可複用）：** 1h / 497 行
- **預估後續 §3-§6：** 每章 1–2h（§3 含 4-Subspaces / §6 各分解可能偏 2h）

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
4. docs/book/SCHEMA.md + docs/book/VIZ_SCHEMA.md — 雙 Schema 規範（A 派術語）
5. docs/book/ch01-viewing-matrix.md（單視角範本）+ docs/book/ch02-vec-vec.md（對比結構範本）
6. docs/dev/sop/SOP_DRAFT.md §2.8 — 全書視覺一致性錨點（配色 / 尺寸 / 動畫）
然後繼續「待辦」中的第一項任務（S04 §3 Matrix × Vector，含 4-Subspaces）。
```
