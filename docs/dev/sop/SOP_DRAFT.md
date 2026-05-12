# SOP 草稿：AI 協同開發流程 — 互動式線性代數教材

> **目的：** 記錄 Claude Code 協同把《The Art of Linear Algebra》轉成互動式 Python 教材的完整流程，供日後其他「書 → 互動教材」專案複用。

---

## 第零章：概述

### 適用範圍
- 將既有教科書 / 圖解筆記轉為互動式視覺化教材
- 數學 / 物理 / 工程類書籍（本專案聚焦線性代數）

### 工具鏈
| 工具 | 用途 |
|------|------|
| Claude Code (CLI) | 程式碼修改、實作、重構 |
| claude.ai Chat | 概念討論、視覺化設計 |
| Python 視覺化庫 | （S01 後決定）matplotlib / Plotly / Manim / ipywidgets |

### 限制條件
- 不修改原 repo 的 LaTeX / PPT 檔案（保留原書成品）
- 互動式版本作為「新增層」存在，可選擇放在子目錄如 `interactive/`
- 跨 session 工作，每次需從 HANDOFF.md 恢復 context

---

## 第一章：專案初始化

### 1.1 Repo 取得 — S00 完成
- [x] Clone junoback/The-Art-of-Linear-Algebra
- [x] 確認原書內容範圍（5 大分解、特徵值地圖、Matrix World）

### 1.2 跨 Session 銜接機制 — S00 完成
- [x] 建立 docs/dev/ 結構

### 1.3 技術藍圖 — S01 待辦
- [ ] 與使用者確認技術棧
- [ ] 與使用者確認章節範圍與優先順序
- [ ] 與使用者確認部署形式

---

## 第二章：機械轉換工具鏈（S01 確立）

### 2.1 工具鏈選用與替代方案

| 任務 | 主用 | 替代 / 備援 | 備註 |
|---|---|---|---|
| `.tex` → `.md` | `pandoc -f latex -t markdown --wrap=preserve` | 無 | 公式以 `$$..$$` 保留 LaTeX |
| `.pdf` → 純文字 | `pdftotext -layout` (poppler) | `gs -sDEVICE=txtwrite` | poppler 品質高；gs 適合 poppler 沒裝時 |
| `.eps` → `.png` | `gs -sDEVICE=png16m -r150 -dEPSCrop` | `epstopdf` + `pdftocairo -png` | gs 不依賴 ImageMagick |
| `.eps` 預覽 | macOS Preview | `epstopdf` | EPS 不能直接內嵌 md |

**關鍵教訓：** macOS 預設不裝 ImageMagick / poppler；如要避免 brew 安裝拖時間，**ghostscript 一個工具就能涵蓋 EPS→PNG + PDF→TXT 兩個任務**，作為首發選擇最穩。後續 brew 裝完 poppler 再升級 PDF 文字品質。

### 2.2 章節對映流程
1. `grep -E "^\\\\(section|subsection)" <主檔>.tex` 抓章節
2. `grep "includegraphics" <主檔>.tex` 抓圖片清單
3. 對映表寫入 `docs/book/_merged.md` 的「章節↔圖檔對映」段
4. 章節 md 命名：`ch<NN>-<slug>.md`，子章節 `ch<NN><a-f>-<slug>.md`

### 2.3 圖片描述 Schema（四欄位）+ 雙 Schema 設計（S01.5 補規劃定版）

1. **視覺結構 (Visual Structure)** — 構圖、顏色、布局；目標：盲讀者可重建畫面
2. **數學內容 (Mathematical Content)** — 變數對映、LaTeX 公式、維度
3. **直覺解讀 (Intuition)** — 此圖傳達的核心觀念、常見誤解
4. **視覺化機會 (VizMark 引用)** — 若該圖有互動價值則插一個 VizMark 引用 block，並在章末「## 視覺化劇本」段寫對應 VizScript（13 段 A-M 細緻劇本，~800 字）

**雙 Schema 分工：**
- `SCHEMA.md` 規範章節 md 整體結構（標頭、摘要、數學要點、圖描述、章末延伸）
- `VIZ_SCHEMA.md` 規範 VizMark 標記 + VizScript 劇本格式

**理由：** 後三欄位剛好對應未來 Python 視覺化的計算層 / 動畫層 / widget 層；VizScript 寫到 ~800 字後可**直接餵 LLM 一次產可跑的 Python 雛形**，S12+ 從 `VIZ-CATALOG.md` 挑題目不需返回 ch*.md 補細節。

### 2.4 雙語版本處理與術語慣例

- 主敘述用繁中（術語第一次出現括號標英文）
- 簡中 .tex 作為翻譯用詞參考（不直接照抄）
- **中文「行 / 列」採華文主流 A 派：column = 列（直立）、row = 行（橫躺）** — 與中國大陸、日本、多數 Python 中文文件一致。台灣本土數學教科書傳統採 B 派（column = 行 / row = 列）正好相反，讀者若來自此背景需特別校準。

**S02 教訓：** 跨章節術語慣例必須在 S01 階段就在 `SCHEMA.md` §3.1 鎖死。S02 寫到一半（ch01 已 418 行成稿）才發現要改方向，整檔重寫一次成本約 0.5h；若拖到 S05+ 全書反轉成本會幾何級數膨脹。

**規則：** 開新術語段、跨地區用詞分歧的詞（行/列、欄/列、矩陣分解等）下筆前，先 `grep` 全 `docs/book` 確認用詞一致性。

### 2.5 不修改原 repo + push 規則（S03 末更新）
- `docs/book/` 是新增層，原 `figs/` `*.tex` `*.pdf` 一律不動
- `origin` 指向 `junoback/The-Art-of-Linear-Algebra`，**即為使用者本人（Back Kuo）的 fork**，push 安全
- **S03 末確認：可直接 `git push origin main`，不需再問**（S02 + S03 commit 於 2026-05-12 push 完成）
- session 管理檔（`docs/dev/`）公開可見，撰寫時避免寫入敏感資訊（金鑰、私人連絡等）

### 2.6 章節 session 撰寫流程（S02 驗證 OK）

每個章節 session 的工作步驟：
1. 讀 `SCHEMA.md` + `VIZ_SCHEMA.md` 複習規範（每 session 開頭 5 分鐘）
2. 從 `from-tex/{en,zh}.md` 抓本章 LaTeX 結構與公式
3. 從 `from-pdf/en.txt` 補 pandoc 漏掉的（補漏率約 5%）
4. **直接用 Read tool 讀 PNG 圖檔**（Claude Code 多模態可看圖），逐張寫四欄位描述
5. 同步掃描視覺化機會 → 插 VizMark（命中 VIZ_SCHEMA §1.3 五種類型之一才插）
6. 章末寫 VizScript（每個 VizMark 對應一個 ~800 字劇本，13 段 A-M）
7. 寫章節摘要 + 數學要點（**最後寫**，因為描述完才能精煉摘要）
8. 更新 `_merged.md` 對應章節區塊（勾選 + 填 VizMark 計數）
9. 更新 `HANDOFF.md` + `CURRENT_SESSION.log` + `SESSION_INDEX.md`

**重要：** 第 4-6 步「圖描述 → VizMark → VizScript」是同一個閱讀-理解-記下的連續心智動作，**中間不要切到別的工作**，否則重新進入該章圖的細節會耗 10-15 分鐘 ramp-up。S01.5 補規劃時定的「方案 A 整合」原則就是基於此。

**S02 §1 實際耗時參考：** 約 1.5h（含 A 派切換的整檔重寫 0.5h、初版含 2 VizScript 約 1h）。預估後續 §2-§6 每章 1-2h（§3 含 4-Subspaces、§6 有 5 個分解可能各偏 2h）。

**S03 §2 實際耗時參考：** 約 1h（無 schema 折騰、ch01 範本已成熟可直接套用），產出 497 行（比 ch01 略長，多了 (v1)/(v2) 對偶段 + 兩篇 VizScript）。驗證**「ch01 範本 + 對應 PNG 多模態讀圖」一條路打通後，後續章節撰寫速度穩定在 1h / 章**。

**S04 §3 實際耗時參考：** 約 1.5h（3 張圖 + 4 個 VizMark/VizScript），產出 935 行（接近 ch01 + ch02 之和）。**關鍵觀察：當章節包含**「兩個對偶運算（Mv ↔ vM）+ 一張總覽圖（4-Subspaces）+ 多視角」**時，總篇幅約是單視角章節的 2 倍**，但耗時只增加 50%（因為對偶結構與視覺錨點可從前章範本直接複製）。**4 個 VizScript 的詳度分級策略奏效**：⭐⭐⭐ 兩支寫完整 13 段 A-M（VizScript-01 Mv↔Mv 切換、VizScript-02 4-Subspaces 3D 互動）、⭐⭐ 一支中等詳度（VizScript-03 與 -01 共畫面只記 transpose 差異）、⭐ 一支輕量輪廓（VizScript-04 列空間軌跡），避免每個 VizMark 都堆 800 字導致章節超長失焦。

**S05 §4 實際耗時參考：** 約 1h（1 張圖含 4 子圖 + 4 個 VizMark/VizScript），產出 849 行，**比 ch03 短但 VizMark 分級結構完全相同**（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1）。**關鍵觀察：當章節是「N-way 視角型」且圖只有 1 張（內含 N 個子圖）時**，圖描述段落需要把每個子圖拆成獨立段落（本章 Figure 4.1 內 4 子圖各寫 ~15 行），總體耗時與篇幅比 ch03 略少（少了第 2、3 張獨立大圖的描述開銷）。**§2.9 分級策略再驗證：** VizScript-02（MM4 秩 1 累加 + SVD 圖像 demo）寫成 Tier 3 是合理選擇 — 這條劇本連通 §6.5 SVD 與工程實作（影像壓縮 / 推薦系統），值得最高詳度。**新觀察：** ⭐⭐⭐ 劇本可以選 Tier 2（VizScript-01）或 Tier 3（VizScript-02）；Tier 3 估時 2.5 session、Tier 2 估時 1.5 session，視 S12+ 時間預算決定要實作幾支 Tier 3。

### 2.8 「對比 / 對偶結構」章節的寫作模式（S03 觀察）

本書多個章節是「N 種視角對比型」（§1 4 ways / §2 2 ways / §3 2 ways / §4 4 ways / §6 5 種分解）。對這類章節，**「## 數學要點」段值得安排一個專門的「對比段 / 對偶段」**，把方向差異用一個對比框醒目寫出：

```latex
\underbrace{\mathbf{a}^{\mathrm{T}} \mathbf{b}}_{\text{純量}}
\quad\text{vs}\quad
\underbrace{\mathbf{a}\, \mathbf{b}^{\mathrm{T}}}_{\text{矩陣}}
```

並在直覺解讀段提煉一句「記憶口訣」（如本章「**夾 → 純量、撐 → 矩陣**」）。後續 §3（dot way vs combination way）、§4（4 種乘法）、§6（5 大分解）皆可複用此格式。

**附帶經驗：全書視覺一致性錨點（沿用 §1 / §2 範例值，減少後續決策成本）：**
- **配色 hex：** 綠（列 / 直立）`#2ca02c`、粉紅 / 紅（行 / 橫躺）`#d62728`、藍點（個別數字）`#1f77b4`、整體外框（whole）`#2ca02c` 加粗
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **動畫時間：** 視角切換 400–700ms、平行性高亮淡入 200ms、緩動 ease-in-out
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$

S04+ 撰寫 VizScript 時直接套用上述錨點，**不要重新發明配色 / 尺寸 / 時間**，除非該章有特殊需求（如 §6.5 SVD 需要 colormap 表達 $\sigma$ 大小，才允許偏離藍 / 綠 / 粉約定）。

### 2.9 多 VizMark 章節的分級寫作策略（S04 確立）

當一章節有 3+ 個 VizMark 時，**不要每個都寫完整 13 段 800 字**，否則章節篇幅膨脹失焦。改採**重要性分級**：

| Tier | 重要性 | 13 段詳度 | 字數 | 適用情境 |
|---|---|---|---|---|
| ⭐⭐⭐ | 全書關鍵概念 / 核心動畫 | 全 13 段 A-M 完整 | ~800-1000 | 例：4-Subspaces、SVD、Mv1↔Mv2 切換 |
| ⭐⭐ | 重要但與其他 VizMark 共享畫面 | 13 段精簡（C-F-G-K-L 為主） | ~300-500 | 例：vM1↔vM2（與 Mv 共畫面，只記 transpose） |
| ⭐ | 輕量延伸 / 子集 | 段落式輪廓（A/B/D/F/G + 簡化 I-M） | ~150-250 | 例：列空間軌跡（從更複雜 VizMark 抽出的子集） |

**判斷分級的問題：**
1. 是否獨立成支 Python 程式？是 → ⭐⭐⭐ 候選；否（與其他共畫面）→ ⭐⭐ 或 ⭐
2. 是否包含全書關鍵概念？是 → ⭐⭐⭐
3. 是否是另一個 VizMark 的「簡化版 / 子集」？是 → ⭐ 即可

**S04 實踐：** ch03 4 個 VizMark 分級為 ⭐⭐⭐(2) / ⭐⭐(1) / ⭐(1)，章節總長 935 行可控；若 4 個都寫 800 字會膨脹到 1300+ 行失焦。

### 2.7 收工流程（每 session 結束）

依 CLAUDE.md 規範三層防呆：
1. 更新 `docs/dev/CURRENT_SESSION.log`（追加結束記錄 + 下次起點）
2. 更新 `docs/dev/SESSION_INDEX.md`（追加一行 session 摘要）
3. 更新 `docs/dev/HANDOFF.md`（**整檔覆寫**：最後更新區、已完成、進行中、待辦、關鍵決策、檔案變更、技術筆記）
4. 檢查 `docs/dev/sop/SOP_DRAFT.md`（有新經驗就追加）
5. 簡短回報使用者：本次完成 / 下次建議

**關鍵：** HANDOFF.md 的「關鍵決策記錄」要追加新行而**不刪舊行**（保留決策史），檔案變更追蹤同理（按 session 分區累積）。

---

## 附錄

### A. 版本記錄
| 版本 | 日期 | 變更 |
|------|------|------|
| 0.1 | 2026-05-11 | 初版（S00 初始化）|
| 0.2 | 2026-05-12 | S01 + S01.5：§2 機械轉換 + §2.3 雙 Schema + §2.4 雙語 + §2.5 不改原 repo |
| 0.3 | 2026-05-12 | S02：§2.3 升級 VizMark 引用 / §2.4 改 A 派 + 教訓 / 新增 §2.6 章節 session 流程 + §2.7 收工流程 |
| 0.4 | 2026-05-12 | S03：§2.6 補 §2 耗時資料點（1h / 497 行）/ 新增 §2.8「對比 / 對偶結構」章節寫作模式 + 全書視覺一致性錨點 |
| 0.5 | 2026-05-12 | S04：§2.6 補 §3 耗時資料點（1.5h / 935 行 / 3 圖 4 VizMark）/ 新增 §2.9「多 VizMark 章節分級寫作策略」（⭐⭐⭐ 完整 / ⭐⭐ 精簡 / ⭐ 輪廓）|
| 0.6 | 2026-05-12 | S05：§2.6 補 §4 耗時資料點（1h / 849 行 / 1 圖含 4 子圖 / 4 VizMark） + 「N-way 單圖章節」觀察（圖描述段需拆 N 個子圖獨立段）+ ⭐⭐⭐ 劇本可選 Tier 2 / Tier 3（VizScript-02 MM4 累加選 Tier 3 連通 §6 SVD）|
