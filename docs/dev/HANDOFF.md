# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S05（§4 Matrix × Matrix - 4 Ways 完成）
- **日期:** 2026-05-12
- **狀態:** `ch04-mat-mat.md` 完成（849 行，1 圖含 4 子圖 + 4 VizMark + 4 VizScript：⭐⭐⭐ Tier 2 + ⭐⭐⭐ Tier 3（MM4 + Mona Lisa SVD demo，§6 SVD 鋪陳）+ ⭐⭐ Tier 1 + ⭐ Tier 1）；驗證「N-way 單圖章節」可控篇幅；SOP_DRAFT.md §2.6 補 §4 耗時 + 新觀察 + 版本 0.6；下次 S06 從 §5 Practical Patterns 開始

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
- [x] **S03** §2 Vector × Vector - 2 Ways：`ch02-vec-vec.md`（497 行）— 1 圖描述 + 2 VizMark + 2 VizScript；驗證 ch01 範本可複用
- [x] **S03** SOP_DRAFT.md §2.8 對比 / 對偶結構章節寫作模式 + 全書視覺一致性錨點 + 版本 0.4
- [x] **S04** §3 Matrix × Vector - 2 Ways + 4-Subspaces：`ch03-mat-vec.md`（935 行）— 3 圖描述 + 4 VizMark + 4 VizScript（⭐⭐⭐ × 2 完整 / ⭐⭐ × 1 精簡 / ⭐ × 1 輪廓）
- [x] **S04** SOP_DRAFT.md §2.9 多 VizMark 分級策略 + 版本 0.5
- [x] **S05** §4 Matrix × Matrix - 4 Ways：`ch04-mat-mat.md`（849 行）— 1 圖含 4 子圖描述 + 4 VizMark + 4 VizScript：
  - **VizScript-01** ⭐⭐⭐ Tier 2 4 視角 tab 切換（13 段 A-M 完整 ~1000 字）
  - **VizScript-02** ⭐⭐⭐ Tier 3 MM4 秩 1 累加 + Mona Lisa SVD demo + 重排序對比 + 誤差曲線（13 段 A-M 完整 ~1200 字，**§6 SVD 鋪陳全書最強候選之一**）
  - **VizScript-03** ⭐⭐ Tier 1 維度檢核（精簡 13 段）
  - **VizScript-04** ⭐ Tier 1 MM1 walkthrough（輕量輪廓）
- [x] **S05** SOP_DRAFT.md §2.6 補 §4 耗時資料點（1h / 849 行）+ 新觀察「N-way 單圖章節需拆 N 個子圖獨立段」+ 「⭐⭐⭐ 劇本可選 Tier 2 / Tier 3」 + 版本 0.6

### 進行中
- 無，S05 已收尾

### 待辦（多 session 路線圖 v2 — 方案 A 整合 VizMark+VizScript）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema（章節 / 視覺化）+ 路線圖補規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| ✅ S02 | §1 Viewing a Matrix - 4 Ways（驗證雙 Schema + A 派術語切換） | `ch01-viewing-matrix.md`（418 行，2 VizMark + 2 VizScript） |
| ✅ S03 | §2 Vector × Vector - 2 Ways（驗證 ch01 範本可複用 + 對比結構寫作模式） | `ch02-vec-vec.md`（497 行，2 VizMark + 2 VizScript） |
| ✅ S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces，驗證多 VizMark 分級策略） | `ch03-mat-vec.md`（935 行，4 VizMark + 4 VizScript） |
| ✅ S05 | §4 Matrix × Matrix - 4 Ways（驗證 N-way 單圖章節模式 + ⭐⭐⭐ Tier 2/3 選擇權） | `ch04-mat-mat.md`（849 行，4 VizMark + 4 VizScript） |
| **→ S06** | §5 Practical Patterns（P1 / P2 / P1' / P2' / P3） | `ch05-patterns.md` |
| S07 | §6 5 Factorizations 總覽 + §6.1 A=CR | `ch06a-five.md`、`ch06b-CR.md` |
| S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`、`ch06d-QR.md` |
| S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`、`ch06f-USV.md` |
| S10 | Foreword + Conclusion + 附錄 | `front-foreword.md`、`back-conclusion.md`、`appendix-map-eigenvalues.md`、`appendix-matrix-world.md` |
| S11 | 整合 + 校對 + 統一 + `BOOK.md` + `VIZ-CATALOG.md` | 合併版書 + 視覺化候選池目錄 |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 PoC | （延後到 S11 後再細規劃，預估 ~20 session）|

### S06 起步建議

1. **直接從 ch04 範本套用**（§5 Patterns 是 §4 (MM2)/(MM3)/(MM4) 的特殊配置，結構複用 §4 但每個 Pattern 描述較短；單章預估 600–800 行）
2. **遵 SOP §2.8 全書視覺錨點 + §2.9 分級策略**：配色 hex 沿用、cell 60×60、動畫 400–700ms；4–5 個 Pattern 不要每個都寫 800 字
3. 從 `from-tex/en.md` 抓 §5 部分（line 127–195 附近，含 Pattern12 / Pattern11-22 / Pattern3 三張圖）
4. **§5 重點**：每個 Pattern 都是 §4 視角的特例 — 用「對應 MM? 視角 + 特殊形狀 / 限制」格式描述
   - **(P1)** Pattern 1 = (MM2) + (Mv2) 結合：$A$ 直立列被 column scaling 矩陣（對角矩陣）右乘 → 「each column scaled by a diagonal entry」
   - **(P2)** Pattern 2 = (MM3) extension：row scaling 矩陣左乘 → 「each row scaled by a diagonal entry」
   - **(P1')** = (P1) variant：對角矩陣的元素直接乘到對應 column
   - **(P2')** = (P2) variant：對角矩陣的元素直接乘到對應 row
   - **(P3)** Pattern 3 = $X D X^{-1}$ 譜分解（解微分方程 / 遞迴方程）→ **連到 §6.4 特徵值分解**
5. 看 PNG 3 張（`Pattern12.png` / `Pattern11-22.png` / `Pattern3.png`），用 Read tool 多模態直接讀
6. 寫 `ch05-patterns.md`：
   - 數學要點段含 5 個 Pattern + 「Pattern ↔ §4 視角」對映表
   - 各 Pattern 寫精簡圖描述（每 Pattern ~30 行）
   - VizMark 預估：3 個，⭐⭐⭐ × 1（對角矩陣 column / row scaling 動畫，可看見對角元素「沿著」row/column 縮放）+ ⭐⭐ × 1（(P3) $X D X^{-1}$ 完整動畫，§6.4 鋪陳）+ ⭐ × 1（具體數值 walkthrough）
7. **隱藏難點預警**：(P3) 涉及特徵值 / 特徵向量 / 對角化，是 §6.4 的提前曝光 — 描述要點到為止，把細節推到 §6.4 寫，本章只建立「視覺直覺」即可

### 工件清單（S06+ 撰寫前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式（A 派術語） |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段 A-M 格式（含 800 字範例） |
| `docs/book/_merged.md` | 章節進度追蹤 + 章節↔圖檔對映表 + VizMark 計數 |
| `docs/book/ch01-viewing-matrix.md` | **S02 成稿，A 派術語的參考範本**（單視角章節） |
| `docs/book/ch02-vec-vec.md` | **S03 成稿，對比 / 對偶結構章節範本**（多視角章節，§3 §4 §6 可複用） |
| `docs/book/ch03-mat-vec.md` | **S04 成稿，多 VizMark + 多圖章節範本 + 4-Subspaces 標誌圖**（§4 直接套用結構） |
| `docs/book/ch04-mat-mat.md` | **S05 成稿，N-way 單圖章節範本（1 圖含 N 子圖）**（§5 §6 直接複用，§6 5 大分解每個都連回 (MM4)） |
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready）|
| `docs/dev/sop/SOP_DRAFT.md` | §2.8 全書視覺錨點 + §2.9 多 VizMark 分級 + S05 補「N-way 單圖章節」觀察 — **S06+ 直接沿用** |

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
| 2026-05-12 | **S05 確立「N-way 單圖章節寫作模式」（SOP §2.6 補）：1 張圖含 N 子圖時，圖描述段需把每個子圖拆獨立段** | ch04 Figure 4.1 是 4 子圖 (MM1/MM2/MM3/MM4) 2×2 排版，每子圖 ~15 行獨立段描述。配合 §2.9 分級策略，849 行控制良好。§6 5 大分解每個雖各有獨立圖，但每個分解內部多視角時可複用此模式 |
| 2026-05-12 | **S05 確立「⭐⭐⭐ 劇本可選 Tier 2 或 Tier 3」** | ch04 VizScript-01 (4 視角切換) 寫成 Tier 2（1.5 session）、VizScript-02 (MM4 + Mona Lisa SVD demo) 寫成 Tier 3（2.5 session）。S12+ 時間預算決定要實作幾支 Tier 3；本書全部 ⭐⭐⭐ 劇本若都 Tier 3，總實作 ~25 session；若混合 Tier 2 / Tier 3，可壓到 ~15 session |
| 2026-05-12 | **S05 確立「§4 (MM4) 是 §6 五大分解的視覺基石」** | $A = CR / LU / QR$ / $S = Q\Lambda Q^{\mathrm{T}}$ / $A = U\Sigma V^{\mathrm{T}}$ 都可用 (MM4) 展開成「秩 1 之和」；§6 5 章寫作時必引 §4 (MM4) 作對應，**VizScript-02 是 SVD 的視覺前置**。本決策影響 S07–S09 寫作路徑 — 每個分解章節都複用 ch04 VizScript-02 結構 + 換成對應的 $\mathbf{u}_p / \mathbf{v}_p$ 物件 |

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

### S05 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/ch04-mat-mat.md | 新增 | **§4 章節 md：849 行**，含 1 圖描述（MatrixTimesMatrix 含 4 子圖 MM1/MM2/MM3/MM4，2×2 排版，每子圖獨立段）+ 4 VizMark + 4 VizScript（VizScript-01 ⭐⭐⭐ Tier 2 4 視角切換 / VizScript-02 ⭐⭐⭐ Tier 3 MM4 秩 1 累加 + Mona Lisa SVD demo + 重排序對比 + 誤差曲線 / VizScript-03 ⭐⭐ Tier 1 維度檢核 / VizScript-04 ⭐ Tier 1 MM1 walkthrough）；4 視角總表 + 與 §2 §3 對偶傳承表 + 維度檢核 + 非交換律段 |
| docs/book/_merged.md | 修改 | S05 標記 `[x]` 完成，VizMark 計數 `2 / 1 / 1` |
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.6 補 §4 耗時資料點（1h / 849 行）+ 新觀察「N-way 單圖章節需拆 N 個子圖獨立段」+ 「⭐⭐⭐ 劇本可選 Tier 2 / Tier 3」+ 版本 0.6 |
| docs/dev/CURRENT_SESSION.log | 修改 | S05 啟動 + 即時記錄 + 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S05 一行 |

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
| **Marimo + matplotlib + marimo.ui**（S02–S05 VizScript 首選） | 反應式 notebook、純 Python、可匯出 HTML | 較新生態系較小 |
| Streamlit + Plotly | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

**S04 觀察：** 4-Subspaces VizScript-02 需要 3D 互動（拖曳箭頭 + 平面塌縮動畫 + 飛行軌跡），matplotlib 3D 互動性偏弱；S12+ 評估時 **Plotly 3D + Dash** 或 **Three.js + Pyodide** 可能更合適這類 ⭐⭐⭐ Tier 3 劇本。

**S05 觀察：** ch04 VizScript-02 需 64×64 SVD 熱圖 + 4 種預設影像 + 累加動畫 — **Plotly Dash 強烈優先**（heatmap 渲染效能、影像對比布局、誤差曲線併同畫面都比 matplotlib 自然）。S12+ 評估技術棧時建議「同一份程式碼支援 Marimo（教學用）+ Dash（高品質 demo 用）」雙重後端，共用 _common/ 視覺化原語。

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

**矩陣乘法形狀：** $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$AB = C \in \mathbb{R}^{m \times n}$。**內維 $k$（A 的列數 = B 的行數）必須對齊**才可乘。

### 全書視覺一致性錨點（S03 確立，S04+ 沿用）

- **配色 hex：** 綠（列 / 直立）`#2ca02c`、粉紅 / 紅（行 / 橫躺）`#d62728`、藍點（個別數字 / $\mathbf{x}$ 分量）`#1f77b4`、灰填充 `#eeeeee` / 框 `#333333`、子空間半透明 alpha 0.3
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **3D 視窗尺寸（S04 新增）：** 預設 600×480 px、視角 elev=25° azim=-60°
- **動畫時間：** 視角切換 600–800ms、平行性高亮淡入 200ms、子空間維度變化 600ms、飛行軌跡 700ms、秩 1 累加 400ms / 項（S05 新增）、緩動 ease-in-out
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$（3D 限 $\{2, 3\}$、SVD demo 64×64 像素）
- **N-way 切換動畫（S05 新增）：** 多視角 tab 切換時 800ms 動畫含「色塊重排 + 重染色 + 公式同步」三層。

### 章節撰寫速度資料點（更新版）

- **S02 §1（含 A 派切換重寫 0.5h）：** 1.5h / 418 行 / 2 VizMark
- **S03 §2（ch01 範本可複用）：** 1h / 497 行 / 2 VizMark
- **S04 §3（4 VizMark 分級策略）：** 1.5h / 935 行 / 4 VizMark — **多圖多 VizMark 章節是「~2 倍篇幅 / 1.5 倍耗時」**
- **S05 §4（1 圖含 4 子圖 + 4 VizMark）：** 1h / 849 行 / 4 VizMark — **N-way 單圖章節比多圖章節省 0.5h（少寫 2 段獨立大圖描述）**
- **預估後續：** §5 patterns 1h（5 個 small pattern）/ §6.1 1.5h / §6.2–§6.3 各 1.5h / §6.4–§6.5 各 2h（SVD 最複雜）

### §4 (MM4) 與 §6 五大分解的鋪陳對應（S05 新增）

| §6 分解 | (MM4) 形式 | VizScript 結構複用 |
|---|---|---|
| $A = CR$ | $A = \sum_p \mathbf{c}_p \mathbf{r}^*_p$（$r$ 項） | ch04 VizScript-02 + 換成 $C$ 直立列 / $R$ 橫躺行 |
| $A = LU$ | $A = \sum_p \mathbf{l}_p \mathbf{u}^*_p$（$n$ 項） | ch04 VizScript-02 + 強調「下三角 × 上三角」 |
| $A = QR$ | $A = \sum_p \mathbf{q}_p \mathbf{r}^*_p$（$n$ 項） | ch04 VizScript-02 + 強調「$\mathbf{q}_p$ 正交」 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$ | ch04 VizScript-02 + 對稱矩陣特例 |
| $A = U\Sigma V^{\mathrm{T}}$ | $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ | ch04 VizScript-02 完整繼承（Eckart–Young + 截斷） |

**結論：** ch04 VizScript-02（MM4 秩 1 累加 + Mona Lisa SVD demo）是後續 5 章 VizScript 的「母模板」 — S07–S09 寫作時只需換物件名稱與額外特例（如正交、對稱、按 σ 排序），不需重新設計動畫結構。**S12+ 實作 ch04 VizScript-02 後，§6 5 大分解 VizScript 可加速實作 60%。**

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
4. docs/book/SCHEMA.md + docs/book/VIZ_SCHEMA.md — 雙 Schema 規範（A 派術語）
5. docs/book/ch01–ch04 — 4 套範本：單視角 / 對比結構 / 多圖多 VizMark / N-way 單圖
6. docs/dev/sop/SOP_DRAFT.md §2.6 補「N-way 單圖章節」+ §2.8 全書視覺錨點 + §2.9 多 VizMark 分級策略
然後繼續「待辦」中的第一項任務（S06 §5 Practical Patterns，5 個 Pattern + 3 張圖：Pattern12 / Pattern11-22 / Pattern3）。
```
