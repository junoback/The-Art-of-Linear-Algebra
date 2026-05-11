# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S01（完成）
- **日期:** 2026-05-12
- **狀態:** 機械轉換 + Schema 全部就緒，下次 S02 開始實際章節撰寫

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

### 待辦（多 session 路線圖）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S09）後，於 S10 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| S01（進行中） | 機械轉換 + Schema 設計 + EPS→PNG 一次性轉檔 | `docs/book/from-tex/{en,zh}.md`、`docs/book/from-pdf/{en,zh}.md`、`docs/book/SCHEMA.md`、`docs/book/figs-png/*.png`、`docs/book/_merged.md` 骨架 |
| S02 | PoC：§1 Viewing a Matrix - 4 Ways 整合 + 圖描述 | `docs/book/ch01-viewing-matrix.md`（含 4-5 張圖描述）+ 描述規範定版 |
| S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md` |
| S04 | §3 Matrix × Vector - 2 Ways | `ch03-mat-vec.md` |
| S05 | §4 Matrix × Matrix - 4 Ways + §5 Practical Patterns | `ch04-mat-mat.md`、`ch05-patterns.md` |
| S06 | §6 5 Factorizations 總覽 + CR + LU | `ch06a-five.md`、`ch06b-CR.md`、`ch06c-LU.md` |
| S07 | §6 QR + QΛQ' + UΣV' | `ch06d-QR.md`、`ch06e-QLQ.md`、`ch06f-USV.md` |
| S08 | Foreword + Conclusion + 附加圖（MapofEigenvalues + MatrixWorld） | `appendix-*.md` |
| S09 | 整合 + 校對 + 統一 + 目錄 | `docs/book/README.md`、`BOOK.md`（合併版） |
| S10+ | 互動式 Python 視覺化技術棧決策 + PoC | （延後，到時再規劃） |

---

## 關鍵決策記錄

| 日期 | 決策 | 原因 |
|------|------|------|
| 2026-05-11 | 啟用跨 session 管理系統 | 使用者明確表示這是長期跨多 session 專案 |
| 2026-05-11 | 不修改原 repo 的 LaTeX/PPT 檔案 | 原檔是書的成品，互動式版本應該是新增層而非取代 |
| 2026-05-12 | 全書 md 化路線：機械轉換 + 圖片詳細描述，分 10 session 完成 | 原書本質是圖解，純文字 md 無法傳達內容，需逐圖寫描述 |
| 2026-05-12 | 章節切分粒度：每 session 1 章 + 4-5 張圖描述 | 平衡品質與進度 |
| 2026-05-12 | 描述語言：繁體中文，術語括號保留英文（例：行空間 (column space)） | 使用者偏好繁中，但保留英文術語便於對照原書與通用文獻 |
| 2026-05-12 | 範圍：英文版 + 簡中版兩語並做，跳過日文版 | 使用者選擇方案 2（雙語），日文版主要差異是翻譯不影響視覺化 |
| 2026-05-12 | 圖片描述格式採四欄位 schema：視覺結構/數學內容/直覺解讀/互動化提示 | 後三欄位剛好對應未來 Python 視覺化的圖形、計算、說明、widget |

---

## 檔案變更追蹤

### S00 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/dev/HANDOFF.md | 新增 | Session 交接文件 |
| docs/dev/SESSION_INDEX.md | 新增 | Session 索引 |
| docs/dev/CURRENT_SESSION.log | 新增 | 即時記錄 |
| docs/dev/sop/SOP_DRAFT.md | 新增 | SOP 草稿 |

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
