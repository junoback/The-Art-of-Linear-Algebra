# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S01 + S01.5 補規劃（完成）
- **日期:** 2026-05-12
- **狀態:** 機械轉換 + 雙 Schema（章節 / 視覺化）+ 新版 10-session 路線圖全部就緒，下次 S02 開始 §1 章節撰寫（含 VizMark + VizScript）

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

### 進行中
- 無，S01 已收尾

### 待辦（多 session 路線圖 v2 — 方案 A 整合 VizMark+VizScript）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema（章節 / 視覺化）+ 路線圖補規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| S02 | §1 Viewing a Matrix - 4 Ways（驗證雙 Schema） | `ch01-viewing-matrix.md`（含描述 + 2–3 VizMark + 對應 VizScript） |
| S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md` |
| S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces） | `ch03-mat-vec.md` |
| S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md` |
| S06 | §5 Practical Patterns | `ch05-patterns.md` |
| S07 | §6 5 Factorizations 總覽 + §6.1 A=CR | `ch06a-five.md`、`ch06b-CR.md` |
| S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`、`ch06d-QR.md` |
| S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`、`ch06f-USV.md` |
| S10 | Foreword + Conclusion + 附錄 | `front-foreword.md`、`back-conclusion.md`、`appendix-map-eigenvalues.md`、`appendix-matrix-world.md` |
| S11 | 整合 + 校對 + 統一 + `BOOK.md` + `VIZ-CATALOG.md` | 合併版書 + 視覺化候選池目錄 |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 PoC | （延後到 S11 後再細規劃，預估 ~20 session）|

### 工件清單（S02+ 撰寫前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式 |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段細緻劇本格式（含 800 字範例）|
| `docs/book/_merged.md` | 章節進度追蹤 + 章節↔圖檔對映表 + VizMark 計數 |
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready）|

---

## 關鍵決策記錄

| 日期 | 決策 | 原因 |
|------|------|------|
| 2026-05-11 | 啟用跨 session 管理系統 | 使用者明確表示這是長期跨多 session 專案 |
| 2026-05-11 | 不修改原 repo 的 LaTeX/PPT 檔案 | 原檔是書的成品，互動式版本應該是新增層而非取代 |
| 2026-05-12 | 全書 md 化路線：機械轉換 + 圖片詳細描述 | 原書本質是圖解，純文字 md 無法傳達內容，需逐圖寫描述 |
| 2026-05-12 | 描述語言：繁體中文，術語括號保留英文（例：行空間 (column space)） | 使用者偏好繁中，但保留英文術語便於對照原書與通用文獻 |
| 2026-05-12 | 範圍：英文版 + 簡中版兩語並做，跳過日文版 | 使用者選擇方案 2（雙語），日文版主要差異是翻譯不影響視覺化 |
| 2026-05-12 | 圖片描述格式採四欄位 schema：視覺結構/數學內容/直覺解讀/視覺化機會（VizMark） | 後三欄位對應未來 Python 視覺化的圖形、計算、互動三層 |
| 2026-05-12 | **S01.5 補規劃**：方案 A — 章節 session 整合「描述 + VizMark + VizScript」三類工作 | 視覺化劇本品質強烈依賴對圖的深度理解，分離反而會浪費；+3 session 屬可接受比例 |
| 2026-05-12 | **VizScript 細緻度：細版 ~800 字 / 個（13 段固定格式）** | 目標是直接餵 LLM 生 Python 程式不需補充細節，避免 S12+ 實作時來回問細節 |
| 2026-05-12 | 新增 `VIZ_SCHEMA.md` + `VIZ-CATALOG.md`（S11 產出） | VizMark 散在各章便於閱讀；VIZ-CATALOG 集中彙整供 S12+ 挑題目實作 |
| 2026-05-12 | 章節切分微調：§5 獨立 1 session、§6 拆 3 session（總覽+CR / LU+QR / QΛQᵀ+UΣVᵀ）| 視覺化工作量讓每 session 章節密度降為 ~0.7 章 |
| 2026-05-12 | git origin 是上游 junoback repo，**收工 commit 留本地不 push** | 防誤推到別人 repo；建議 fork 或抽出獨立 repo 後再 push |

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

---

## 技術筆記

### Repo 原始內容概覽
- **LaTeX 主檔**：`The-Art-of-Linear-Algebra.tex`（英文）、`-j.tex`（日文）、`-zh-CN.tex`（簡中）
- **編好的 PDF**：三種語言版本均已存在（不需重新編譯也可閱讀）
- **圖檔來源**：`Illustrations.pptx`（PowerPoint），透過 makefile 流程印成 PS → EPS → 嵌入 LaTeX
- **編譯需求**（如需重編 PDF）：MacTeX（uplatex + dvipdfmx）、psutils（psselect）、ps2eps、PowerPoint（印 PS）

### 互動式版本可能的技術選項（待 S01 決策）
| 方案 | 優點 | 缺點 |
|------|------|------|
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Marimo | 反應式 notebook、純 Python、可匯出 HTML | 較新生態系較小 |
| Streamlit | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

### 不需立刻決定但需考量
- 是否做中文化版本（原書有日文/簡中翻譯）
- 是否包含習題 / 自我測驗
- 是否包含原書 Strang 演講影片連結

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
然後繼續「待辦」中的第一項任務。
```
