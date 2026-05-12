# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S04（§3 + 4-Subspaces 完成）
- **日期:** 2026-05-12
- **狀態:** `ch03-mat-vec.md` 完成（935 行，3 圖描述 + 4 VizMark + 4 VizScript：⭐⭐⭐ × 2 完整 13 段 / ⭐⭐ × 1 精簡 / ⭐ × 1 輪廓）；驗證「多 VizMark 章節分級寫作策略」可控篇幅；SOP_DRAFT.md 新增 §2.9 分級策略 + 版本 0.5；下次 S05 從 §4 Matrix × Matrix - 4 Ways 開始

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
- [x] **S04** §3 Matrix × Vector - 2 Ways + 4-Subspaces：`ch03-mat-vec.md`（935 行）— 3 圖描述 + 4 VizMark + 4 VizScript：
  - **VizScript-01** ⭐⭐⭐ Mv1↔Mv2 視角切換（13 段 A-M 完整 ~1000 字）
  - **VizScript-02** ⭐⭐⭐ 4-Subspaces 3D 互動（13 段 A-M 完整 ~1200 字，含 SVD 求基底 + 拖曳 x 飛行動畫 + 秩變化平面塌縮）— 全書 ⭐⭐⭐ 第一名候選
  - **VizScript-03** ⭐⭐ vM1↔vM2 左乘對偶（精簡 13 段，與 -01 共畫面）
  - **VizScript-04** ⭐ 列空間軌跡掃描（輕量輪廓）
- [x] **S04** SOP_DRAFT.md 新增 §2.9「多 VizMark 章節分級寫作策略」（⭐⭐⭐ 完整 / ⭐⭐ 精簡 / ⭐ 輪廓）+ §2.6 補 §3 耗時資料點 + 版本 0.5

### 進行中
- 無，S04 已收尾

### 待辦（多 session 路線圖 v2 — 方案 A 整合 VizMark+VizScript）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema（章節 / 視覺化）+ 路線圖補規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| ✅ S02 | §1 Viewing a Matrix - 4 Ways（驗證雙 Schema + A 派術語切換） | `ch01-viewing-matrix.md`（418 行，2 VizMark + 2 VizScript） |
| ✅ S03 | §2 Vector × Vector - 2 Ways（驗證 ch01 範本可複用 + 對比結構寫作模式） | `ch02-vec-vec.md`（497 行，2 VizMark + 2 VizScript） |
| ✅ S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces，驗證多 VizMark 分級策略） | `ch03-mat-vec.md`（935 行，4 VizMark + 4 VizScript） |
| **→ S05** | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md` |
| S06 | §5 Practical Patterns | `ch05-patterns.md` |
| S07 | §6 5 Factorizations 總覽 + §6.1 A=CR | `ch06a-five.md`、`ch06b-CR.md` |
| S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`、`ch06d-QR.md` |
| S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`、`ch06f-USV.md` |
| S10 | Foreword + Conclusion + 附錄 | `front-foreword.md`、`back-conclusion.md`、`appendix-map-eigenvalues.md`、`appendix-matrix-world.md` |
| S11 | 整合 + 校對 + 統一 + `BOOK.md` + `VIZ-CATALOG.md` | 合併版書 + 視覺化候選池目錄 |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 PoC | （延後到 S11 後再細規劃，預估 ~20 session）|

### S05 起步建議

1. **直接從 ch03 範本套用**（與 ch02 不同：§4 有 4 個 ways，可複用本章 Mv↔vM 對偶結構 + 多 VizMark 分級策略；單章預估 700–900 行）
2. **遵 SOP §2.8 全書視覺錨點 + §2.9 分級策略**：配色 hex 沿用、cell 60×60、動畫 400–700ms；4 個 VizMark 不要每個都寫 800 字
3. 從 `from-tex/en.md` 抓 §4 部分（line 114–168 附近，含 MatrixTimesMatrix 1 張圖 + 4 種視角 MM1/MM2/MM3/MM4）
4. 看 PNG（`MatrixTimesMatrix.png` 是 §4 主圖），用 Read tool 多模態直接讀
5. 寫 `ch04-mat-mat.md`：
   - (MM1) 點積方式：$C_{ij} = \mathbf{a}^*_i \cdot \mathbf{b}_j$
   - (MM2) 列線性組合方式：$C$ 的每一直立列是 $A$ 列的線性組合（係數來自 $B$ 對應列）
   - (MM3) 行線性組合方式：$C$ 的每一橫躺行是 $B$ 行的線性組合（係數來自 $A$ 對應行）
   - (MM4) 外積之和方式：$AB = \sum_{k} \mathbf{a}_k \mathbf{b}^*_k$（**§2 (v2) 外積的直接推廣，是 §6 SVD 的鑰匙**）
6. VizMark 預估：3–4 個，⭐⭐⭐ × 1（4 視角切換動畫 — 把 (Mv1)(Mv2) 推廣到 4 視角）+ ⭐⭐ × 2（MM4 外積之和 + 維度檢核）+ ⭐ × 1（具體數值算法 walkthrough）

### 工件清單（S05+ 撰寫前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式（A 派術語） |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段 A-M 格式（含 800 字範例） |
| `docs/book/_merged.md` | 章節進度追蹤 + 章節↔圖檔對映表 + VizMark 計數 |
| `docs/book/ch01-viewing-matrix.md` | **S02 成稿，A 派術語的參考範本**（單視角章節） |
| `docs/book/ch02-vec-vec.md` | **S03 成稿，對比 / 對偶結構章節範本**（多視角章節，§3 §4 §6 可複用） |
| `docs/book/ch03-mat-vec.md` | **S04 成稿，多 VizMark + 多圖章節範本 + 4-Subspaces 標誌圖**（§4 直接套用結構） |
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready）|
| `docs/dev/sop/SOP_DRAFT.md` | §2.8 全書視覺一致性錨點 + §2.9 多 VizMark 分級策略 — **S05+ 直接沿用** |

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
| 2026-05-12 | **S03 末撤銷上條：確認 `junoback/The-Art-of-Linear-Algebra` GitHub repo 即為使用者本人（Back Kuo）的 fork，push 到 origin/main 安全** | 使用者直接授權；之後可正常 `git push` 不需再問 |
| 2026-05-12 | **S02 中途決策變更：術語慣例改採華文主流 A 派（column = 列直立 / row = 行橫躺）** | 與中國大陸、日本、多數 Python 中文文件、本書簡中譯本一致；台灣本土教科書傳統採 B 派正好相反，本書讀者若來自此背景需校準 |
| 2026-05-12 | SOP_DRAFT.md 新增「術語慣例必須在 S01 鎖死」教訓條 | S02 中途改 A 派付出整檔重寫 0.5h 成本；若拖到 S05+ 全書反轉成本會幾何級數膨脹 |
| 2026-05-12 | **S03 確立「全書視覺一致性錨點」（SOP §2.8）：配色 hex / cell 尺寸 / 動畫時間統一化** | S04+ 撰寫 VizScript 時直接套用，不重新發明，除非特殊章節（如 SVD 需要 colormap 表達 σ 大小）才允許偏離 |
| 2026-05-12 | **S03 確立「對比 / 對偶結構章節寫作模式」：§ 數學要點 加對比段 + 直覺段提煉記憶口訣** | §3（dot way vs combination way）、§4（4 ways）、§6（5 大分解）均適用同一格式，減少每章設計成本 |
| 2026-05-12 | **S04 確立「多 VizMark 章節分級寫作策略」（SOP §2.9）：⭐⭐⭐ 完整 13 段 / ⭐⭐ 精簡 / ⭐ 輪廓** | ch03 4 個 VizMark 若全寫 800 字會膨脹到 1300+ 行失焦；分級後 935 行可控。§4 後續多 VizMark 章節皆套用此策略 |
| 2026-05-12 | **S04 確立「4-Subspaces 圖是全書視覺化最高 priority 之一（⭐⭐⭐ Tier 3）」** | Strang 兩塊大餅圖是線性代數核心定理（rank-nullity / 投影 / SVD）的視覺載體；VizScript-02 估 3 session 實作，是 §6 SVD 預先鋪陳的關鍵互動 |

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

### S04 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/ch03-mat-vec.md | 新增 | **§3 章節 md：935 行**，含 3 圖描述（MatrixTimesVector / VectorTimesMatrix / 4-Subspaces）+ 4 VizMark + 4 VizScript（VizScript-01 / 02 完整 13 段 A-M / VizScript-03 精簡 / VizScript-04 輪廓）；A 派術語；新增 Mv↔vM 對偶表 + 4 子空間維度表 + 正交分解 |
| docs/book/_merged.md | 修改 | S04 標記 `[x]` 完成，VizMark 計數 `2 / 1 / 1`（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1） |
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.6 補 §3 耗時資料點（1.5h / 935 行）+ 新增 §2.9「多 VizMark 章節分級寫作策略」+ 版本 0.5 |
| docs/dev/CURRENT_SESSION.log | 修改 | S04 啟動 + 即時記錄 + 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S04 一行 |

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
| **Marimo + matplotlib + marimo.ui**（S02–S04 VizScript 首選） | 反應式 notebook、純 Python、可匯出 HTML | 較新生態系較小 |
| Streamlit + Plotly | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

**S04 新觀察：** 4-Subspaces VizScript-02 需要 3D 互動（拖曳箭頭 + 平面塌縮動畫 + 飛行軌跡），matplotlib 3D 互動性偏弱；S12+ 評估時 **Plotly 3D + Dash** 或 **Three.js + Pyodide** 可能更合適這類 ⭐⭐⭐ Tier 3 劇本。

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
| nullspace | 零空間 $\mathbf{N}(A)$ | — |
| left nullspace | 左零空間 $\mathbf{N}(A^{\mathrm{T}})$ | — |
| rank | 秩 | — |
| subspace | 子空間 | — |
| basis | 基底 | — |
| linear combination | 線性組合 | — |
| dot product / inner product | 點積 / 內積 | — |
| outer product | 外積（→ 秩 1 矩陣）| — |
| factorization | 分解 | — |
| eigenvalue / eigenvector | 特徵值 / 特徵向量 | — |
| singular value | 奇異值 | — |
| perpendicular / orthogonal | 正交 / 垂直 | — |
| orthogonal complement | 正交補 | — |

**矩陣尺寸：** $A \in \mathbb{R}^{m \times n}$ 表示 **$m$ 行 $n$ 列**（$m$ rows, $n$ columns）。$m$ = 行數、$n$ = 列數。

### 全書視覺一致性錨點（S03 確立，S04+ 沿用）

- **配色 hex：** 綠（列 / 直立）`#2ca02c`、粉紅 / 紅（行 / 橫躺）`#d62728`、藍點（個別數字 / $\mathbf{x}$ 分量）`#1f77b4`、灰填充 `#eeeeee` / 框 `#333333`、子空間半透明 alpha 0.3
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **3D 視窗尺寸（S04 新增）：** 預設 600×480 px、視角 elev=25° azim=-60°
- **動畫時間：** 視角切換 600–800ms、平行性高亮淡入 200ms、子空間維度變化 600ms、飛行軌跡 700ms、緩動 ease-in-out
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$（3D 限 $\{2, 3\}$）

### 章節撰寫速度資料點（更新版）

- **S02 §1（含 A 派切換重寫 0.5h）：** 1.5h / 418 行 / 2 VizMark
- **S03 §2（ch01 範本可複用）：** 1h / 497 行 / 2 VizMark
- **S04 §3（4 VizMark 分級策略）：** 1.5h / 935 行 / 4 VizMark — **多圖多 VizMark 章節是「~2 倍篇幅 / 1.5 倍耗時」**
- **預估後續：** §4 4 ways 1.5h / §5 patterns 1h / §6.1–§6.3 各 1.5h / §6.4–§6.5 各 2h（SVD 最複雜）

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
4. docs/book/SCHEMA.md + docs/book/VIZ_SCHEMA.md — 雙 Schema 規範（A 派術語）
5. docs/book/ch01-viewing-matrix.md（單視角範本）+ docs/book/ch02-vec-vec.md（對比結構範本）+ docs/book/ch03-mat-vec.md（多 VizMark + 多圖範本，4-Subspaces 標誌圖）
6. docs/dev/sop/SOP_DRAFT.md §2.8 全書視覺錨點 + §2.9 多 VizMark 分級策略
然後繼續「待辦」中的第一項任務（S05 §4 Matrix × Matrix - 4 Ways）。
```
