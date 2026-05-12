# 視覺化規範：VizMark + VizScript

> **目的：** 在章節 md 內標記「值得做互動視覺化」的點（VizMark），並對每點寫出**可直接餵給 LLM 產生完整 Python 程式碼**的劇本提示詞（VizScript）。
> **使用時機：** S02 起每個章節 session 撰寫圖片描述的同時，同步掃描標記與寫劇本。
> **產出總目錄：** S11 階段把全書 VizScript 抽出彙整成 `docs/book/VIZ-CATALOG.md`，作為 S12+ 開發視覺化的「待辦池」。

---

## 1. VizMark — 章節內視覺化標記

寫在章節 md 中，**插在對應段落或圖片描述附近**（不集中放在章末），讓讀者閱讀時即看到「這個點以後會有互動版」的提示。

### 1.1 格式

```markdown
> 🎬 **VizMark-NN** [類型] [優先級]
> **位置：** §X.Y / Figure-Z / 段落主題
> **核心概念：** 一句話（≤ 40 字）
> **互動梗概：** 一句話（≤ 50 字）描述「使用者拉什麼、看到什麼變」
> **詳見劇本：** VizScript-NN（章末）
```

### 1.2 欄位定義

| 欄位 | 說明 | 範例 |
|---|---|---|
| `NN` | 章內流水號，從 01 起 | `01` `02` |
| `[類型]` | 五選一（見 §1.3） | `[切換視角]` |
| `[優先級]` | `⭐⭐⭐` 核心 / `⭐⭐` 強化 / `⭐` 補充 | `⭐⭐⭐` |
| 位置 | 在書中哪裡 | `§1.2 Figure ViewingMatrix-4Ways` |
| 核心概念 | 此 VizMark 要讓使用者悟到什麼 | `同一矩陣的 4 種看法等價` |
| 互動梗概 | 簡短描述互動的「動詞」 | `按 4 個視角鈕，主圖即時換樣` |

### 1.3 五種 VizMark 類型

| 類型 | 適用情境 | 典型互動 |
|---|---|---|
| `[切換視角]` | 同物件多種詮釋（例：4 ways of viewing） | toggle / radio / tab |
| `[拉桿調參]` | 參數連續變化看效果（例：矩陣值變、維度變） | slider / numeric input |
| `[動畫敘事]` | 概念有時序步驟（例：高斯消去、QR 過程） | play/pause/step bar |
| `[空間幾何]` | 概念在 2D/3D 空間有形狀（例：子空間、特徵向量） | 3D 旋轉、軌跡追蹤 |
| `[即時演算]` | 使用者編輯輸入即時看計算結果（例：點乘、矩陣乘法） | 編輯框 → 即時重算 |

### 1.4 優先級判準

- **⭐⭐⭐ 核心**：移除此互動則該章節核心觀念無法傳達；S12+ 視覺化必做。
- **⭐⭐ 強化**：互動有顯著教學增益；建議做，可在第二波加入。
- **⭐ 補充**：錦上添花；資源足夠才做。

每章節 ⭐⭐⭐ 建議 1-2 個，⭐⭐ 2-3 個，⭐ 不限但別超過 5 個（避免淹沒重點）。

---

## 2. VizScript — 視覺化劇本提示詞（細緻版）

每個 VizMark 對應一個 VizScript，集中放在章節 md 末尾「## 視覺化劇本」段。

**寫作目標：** 此劇本內容**直接複製貼到 LLM**（如 Claude / GPT）說「依此規格寫 Python 程式」即可產出可執行的雛形，**不需再補充細節**。每篇約 600-900 字（不含程式碼骨架）。

### 2.1 格式（12 段，順序固定）

```markdown
### VizScript-NN: 標題

#### A. 一句話定位
（30 字內，讓人秒懂這個視覺化要做什麼）

#### B. 學習目標（Learning Outcome）
- （3-5 條，每條一句，描述「使用者操作完應該能說出 / 看出什麼」）

#### C. 待視覺化的數學物件
- **物件清單：** 例：矩陣 A、向量 b、子空間 W
- **預設值：** 例：A = [[1,2],[3,4]]、b = [5,6]
- **維度範圍：** 例：A 維度 m×n，m,n ∈ [2, 6]
- **數值範圍：** 例：元素 ∈ [-9, 9]，步進 1
- **退化情形需明確處理：** 例：奇異矩陣時行為、空矩陣時行為

#### D. 視覺布局（Visual Layout）
描述畫面分區與每區功能：
- **整體比例：** 例：左 60% 主畫面、右 25% 公式區、底 15% 控制列
- **主畫面內容：** 例：在 [-10,10] × [-10,10] 座標系畫向量箭頭
- **副畫面內容：** 例：對應 LaTeX 公式即時渲染
- **座標系：** 例：x 軸右、y 軸上、單位等比、格線淺灰
- **配色（具體 hex 或 colormap）：** 例：欄向量 `#1f77b4`（藍）、列向量 `#d62728`（紅）、結果 `#2ca02c`（綠）
- **字型 / 字級：** 例：標題 18pt 粗體、座標標籤 12pt
- **空白邊距：** 例：上下左右各 20px

#### E. 輸入控制（Inputs，逐個 widget 列）
每個控制 widget 包含 5 個屬性：
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| m | slider | [2, 6] step 1 | 3 | 即時 |
| n | slider | [2, 6] step 1 | 2 | 即時 |
| a_ij | numeric input × m×n | [-9, 9] step 1 | 預設矩陣 | onBlur |
| 視角 | radio | whole/numbers/cols/rows | whole | 即時（含動畫過渡）|

#### F. 輸出畫面細節（Outputs）
- **主畫面更新規則：** 例：m,n 改變時整個 canvas 重畫；a_ij 改變時僅該格 cell 與相關欄/列重畫
- **數字顯示精度：** 例：保留 2 位小數
- **動態元素：** 例：選中的欄向量加粗 2px、其他半透明 0.5
- **資訊框內容：** 例：右側顯示當前視角的 LaTeX 公式 + rank 即時更新

#### G. 互動行為（Interactions）
列出 hover / click / drag / keyboard 各自的反應：
- **hover 矩陣格子：** 該格高亮 + 顯示 (row, col) tooltip
- **click 欄向量：** 該欄高亮 + 公式區跳到「column view」
- **拖曳欄向量（若適用）：** 即時改 a_ij 並重算
- **快捷鍵：** 1/2/3/4 切換 4 個視角

#### H. 動畫腳本（若 VizMark 類型為「動畫敘事」或視角切換有過渡）
逐步骤描述 keyframe：
- **t=0–200ms:** 原視角元素淡出（opacity 1 → 0）
- **t=200–500ms:** 新視角元素淡入 + 變形（例：scattered numbers 聚合成 column vectors）
- **t=500ms 後:** 穩態，等待下次互動
- **總長度：** 500ms
- **緩動函數：** ease-in-out
- **可暫停 / 倒轉：** 是 / 否

#### I. 邊界與錯誤處理
明列極端情況的行為：
- **m=n=2 最小矩陣：** 正常顯示，提示「至少 2×2」
- **m=n=6 最大：** 字級自動縮小避免重疊
- **使用者輸入非數字：** 紅框警示 + 還原前一值
- **奇異 / 退化情況：** 例如 rank-deficient 時，subspaces 視角顯示「rank = X，少於 n」提示

#### J. 教學支援（Teaching Aids）
- **提示卡 / Tooltip 文字：** 列每個 widget 的 tooltip 內容
- **引導步驟（Walkthrough，選用）：** 例：「Step 1: 看整體 → Step 2: 點任一格 → Step 3: 切到 columns」
- **常見誤解警示：** 例：「點積與內積在這裡指同一件事」
- **延伸閱讀連結：** 例：原書 p.X 對應章節

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** 例：Marimo + matplotlib + ipywidgets
- **替代方案：** 例：Streamlit + Plotly（如需網頁部署）
- **關鍵 API：** 例：`matplotlib.animation.FuncAnimation`、`marimo.ui.slider`
- **檔案結構建議：** 例：`viz/ch01_viewing_matrix.py` 主檔 + `viz/_common.py` 共用工具
- **效能考量：** 例：m,n 改變要全重畫，避免每次都呼叫 plt.figure() 造成記憶體洩漏
- **測試：** 例：snapshot test 4 個視角各取 1 張 PNG 對比

#### L. 驗收標準（Acceptance Criteria）
明列功能完成的判定條件（≤ 5 條）：
- [ ] 4 個視角可切換，每個視角主畫面內容符合 §D
- [ ] m,n 可在 [2,6] 拉動，cell 不重疊不出框
- [ ] 任一 a_ij 可編輯，編輯後即時重算
- [ ] 動畫過渡 ≤ 500ms 完成，無 frame drop
- [ ] 互動深度 Tier 標示與實際工時 ≤ 20% 誤差

#### M. 互動深度 Tier + 估時
- **Tier 1（基礎，0.5-1 session）：** 靜態 4 視角 + 維度 slider，無動畫
- **Tier 2（增強，1-2 session）：** + 編輯 cell + tooltip + 視角切換動畫
- **Tier 3（完整，2-3 session）：** + 拖曳欄向量改值 + 鍵盤快捷鍵 + 引導步驟
- **本劇本目標 Tier：** Tier 2
- **估時：** 1.5 session
```

> 註：上面格式段標 A-M 共 13 段，A 是定位（短），B-M 是 12 段細節，與本節標題「12 段」一致（C 拆兩段時不另列）。

### 2.2 寫作要點

1. **可剪貼性優先**：寫的時候想像「把這 800 字丟給 Claude，要它一次寫出可跑的 Python」，問自己「還有沒有它會卡的細節」。
2. **數字、範圍、單位都要明確**：別寫「合理範圍」「足夠大」這種抽象詞。
3. **顏色給 hex 或 colormap 名**：別只寫「藍色」「暖色」。**全書 6 主色 + 輔助色階直接引用 [SCHEMA.md §3.5.1](SCHEMA.md#351-配色規範hex--rgb)**（綠 `#2ca02c` / 粉紅 `#d62728` / 藍 `#1f77b4` / 紫 `#9467bd` / 橙 `#ff7f0e` / 金 `#FFD700` + 淡版 alpha 0.4 + 深版警示）。
4. **動畫給時間與緩動函數**：別只寫「平滑過渡」。**寫法統一無空格**：`200ms`、`800ms`，不是 `200 ms`（S11 風格規範）。常見錨點見 [SCHEMA.md §3.5.3](SCHEMA.md#353-動畫時間規範)。
5. **退化 / 邊界 case 必列**：rank-deficient、零矩陣、極端維度，至少各想一條。
6. **驗收標準寫成 checklist**：未來實作完可逐條打勾。

### 2.3 全書視覺錨點 cross-reference（S11 規範化）

VizScript 撰寫時不需重複定義以下「**全書共用視覺常數**」，直接引用 SCHEMA.md §3.5 即可：

| 視覺錨點 | 規範位置 | 摘要 |
|---|---|---|
| 配色 hex + RGB | [SCHEMA.md §3.5.1](SCHEMA.md#351-配色規範hex--rgb) | 6 主色 + 輔助色階（淡版 alpha 0.4 / 深版警示）+ 灰階補助 |
| cell 像素尺寸 | [SCHEMA.md §3.5.2](SCHEMA.md#352-cell-像素尺寸規範) | 60×60 / 48×48 / 20px 等常見組合 + 寫法統一 `AAxBB px` |
| 動畫時間 | [SCHEMA.md §3.5.3](SCHEMA.md#353-動畫時間規範) | 50ms / 200ms / 800ms 主要錨點 + 無空格寫法 |
| 3D 視角預設 | [SCHEMA.md §3.5.4](SCHEMA.md#354-3d-視角預設規範) | **elevation=25° / azimuth=-60°**（全書 3D 統一視角）|

---

## 3. VizScript 範例（4 Ways of Viewing a Matrix，供 S02 撰寫時對照）

> **註：以下是 S01.5 提前寫的範例，S02 實際撰寫時可能會細調，作為「細緻度標尺」用。**

### VizScript-EXAMPLE: 矩陣的四種觀看視角

#### A. 一句話定位
讓使用者切換 4 種視角，看同一矩陣呈現出 4 種等價但風格迥異的「身分」。

#### B. 學習目標
- 使用者能說出矩陣的 4 種觀看方式（whole / numbers / columns / rows）
- 使用者能在切換時指出哪個元素對映到哪個欄向量、列向量
- 使用者能解釋「為什麼這 4 種視角描述的是同一個數學物件」
- 使用者能在腦中預測：若改 $a_{12}$，4 個視角中哪些區塊會變

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$
- **預設值：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（m=3, n=2）
- **維度範圍：** m ∈ [2, 6]、n ∈ [2, 6]
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1
- **退化情形：** rank-deficient 時，欄向量視角中相依的欄用虛線標示

#### D. 視覺布局
- **整體比例：** 左 55% 主畫面、右 30% 公式 + 資訊區、底 15% 視角切換列
- **主畫面：** 600 × 600 px 白底，視 m,n 自動縮放單位 cell
- **副畫面（公式區）：** 上半部 LaTeX 公式（用 MathJax 渲染），下半部當前視角的文字說明（≤ 30 字）
- **配色：** 矩陣外框 `#333`、儲存格底 `#fafafa`、文字 `#000`、選中欄 `#1f77b4`（藍）、選中列 `#d62728`（紅）、整體框（whole 視角）`#2ca02c`（綠）
- **字型：** 數字 16pt monospace（Menlo / Consolas）、標題 18pt sans bold
- **單位 cell：** 60 × 60 px，cell 邊距 4 px

#### E. 輸入控制
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發 |
|---|---|---|---|---|
| m | slider | [2, 6] step 1 | 3 | 即時 |
| n | slider | [2, 6] step 1 | 2 | 即時 |
| a_ij | numeric input grid | [-9, 9] step 1 | 預設矩陣 | onBlur |
| 視角 | radio button 4 個 | whole / numbers / columns / rows | whole | 即時（含 400ms 過渡）|

#### F. 輸出畫面細節
- **whole 視角：** 矩陣整體外框加粗 3px、綠色，內部 cell 文字正常顯示
- **numbers 視角：** 所有 cell 邊框加粗、外框移除，強調個別元素
- **columns 視角：** 每欄以縱向半透明色塊覆蓋（藍色系），欄間隔加大 8px
- **rows 視角：** 每列以橫向半透明色塊覆蓋（紅色系），列間隔加大 8px
- **公式區內容：**
  - whole：$A = (a_{ij})_{m \times n}$
  - numbers：$A_{ij} = a_{ij}$，逐一列出
  - columns：$A = [\mathbf{a}_1 \;|\; \mathbf{a}_2 \;|\; \cdots \;|\; \mathbf{a}_n]$
  - rows：$A = \begin{bmatrix} \mathbf{a}_1^* \\ \vdots \\ \mathbf{a}_m^* \end{bmatrix}$
- **資訊框附加：** 顯示 rank(A) 即時計算結果

#### G. 互動行為
- **hover cell：** 該 cell 加粗外框 + tooltip 顯示 `A[i][j] = value`
- **click cell：** 該 cell 持續高亮 + 對應欄、列在公式區用同色標記
- **click 欄向量區（columns 視角時）：** 整欄持續高亮 + 右側顯示該欄做為 R^m 向量的座標
- **快捷鍵：** 數字鍵 1/2/3/4 切換 4 個視角；箭頭鍵移動 cell focus

#### H. 動畫腳本（視角切換）
- **t=0:** 當前視角穩態
- **t=0–150ms:** 當前視角的「特徵元素」（如 columns 視角的色塊）淡出（opacity 1 → 0）
- **t=150–400ms:** 新視角的特徵元素淡入 + 從中心向外展開（scale 0.8 → 1.0）
- **t=400ms 後:** 新視角穩態
- **總長度：** 400ms
- **緩動：** ease-in-out（CSS cubic-bezier(0.4, 0, 0.2, 1) 等價）
- **暫停 / 倒轉：** 否（短動畫不需）

#### I. 邊界與錯誤處理
- **m=2, n=2 最小：** cell 尺寸增至 80×80 避免空蕩
- **m=6, n=6 最大：** cell 縮至 40×40 + 字級 12pt，動畫禁用避免頓
- **使用者輸入非整數：** 紅框警示 0.5 秒後還原
- **rank 計算溢位 / 浮點誤差：** 用 `numpy.linalg.matrix_rank(A, tol=1e-9)` 並顯示警示
- **rank-deficient：** columns 視角中相依欄畫虛線外框 + tooltip「此欄與其他欄線性相依」

#### J. 教學支援
- **Tooltip：**
  - m slider: 「列數 (rows) — 矩陣有幾橫排」
  - n slider: 「行數 (columns) — 矩陣有幾直行」
  - 視角 radio: 各鈕滑過時顯示一句話定義
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1: 「先看 whole 視角，這是一個矩陣」
  - Step 2: 「按 numbers，看到的是同樣的 mn 個數字」
  - Step 3: 「按 columns，看到 n 個欄向量」
  - Step 4: 「按 rows，看到 m 個列向量」
  - Step 5: 「四種視角是等價的，描述同一個矩陣」
- **常見誤解警示：** 「中文『行 / 列』與英文 row / column 翻譯方向相反，本工具用 column = 行（直立）、row = 列（橫躺）」
- **延伸：** 原書 p.3 §1，本專案 `ch01-viewing-matrix.md`

#### K. 技術實作建議
- **首選：** Marimo (反應式 notebook) + matplotlib (2D 矩陣繪製) + marimo.ui (控制元件)
- **替代：** Streamlit + plotly.graph_objects（如需網頁分享）
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫 cell
  - `matplotlib.text.Text` 放數字
  - `marimo.ui.slider`, `marimo.ui.radio`, `marimo.ui.number`
  - `numpy.linalg.matrix_rank`
- **檔案結構：**
  ```
  viz/
    ch01_viewing_matrix.py       # 主入口
    _common/
      palette.py                 # 統一配色
      layout.py                  # cell 尺寸計算
  ```
- **效能：** m,n 改變時呼叫 `ax.clear()` 後重畫，不要 `plt.figure()` 否則記憶體洩漏
- **測試：** 4 個視角各做 1 張 snapshot PNG（`tests/snapshots/ch01_*.png`），CI 比對

#### L. 驗收標準
- [ ] 4 個視角可切換，視覺呈現符合 §D 配色與布局規範
- [ ] m, n slider 在 [2,6] 範圍內拉動，cell 永不重疊、永不出框
- [ ] 任意 a_ij 編輯後 < 100ms 重算完成
- [ ] 視角切換動畫總長 ≤ 400ms，60fps 無 frame drop
- [ ] rank-deficient 時 columns 視角虛線標示正確
- [ ] Walkthrough 5 步驟首次開啟自動觸發，可關閉

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 僅 4 視角切換 + m,n slider，無動畫無編輯
- **Tier 3 擴充：** + 拖曳欄向量端點改值（geometric drag）+ 多矩陣比對（split view）
- **估時：** 1.5 session（含測試與 walkthrough）

---

## 4. 與 SCHEMA.md 的關係

- `SCHEMA.md` 規範**章節 md 整體結構**（標頭、摘要、數學要點、圖片描述、章末延伸）
- `VIZ_SCHEMA.md`（本檔）規範**章節 md 內的視覺化部分**（VizMark 嵌段 + 章末 VizScript 集合）
- 在章節 md 中：
  - **VizMark** 散布在圖片描述後 / 段落間（看到「值得做互動」的點就標）
  - **「## 視覺化劇本」段** 集中放在「章末延伸」之前，包含本章所有 VizScript

## 5. VIZ-CATALOG.md（S11 階段產出）

S11 整合時，把全書 VizMark + VizScript 抽出彙整為 `docs/book/VIZ-CATALOG.md`：

- **總覽表：** 全書 VizMark 清單（編號、章節、類型、優先級、Tier、估時、狀態）
- **按優先級分組：** ⭐⭐⭐ → ⭐⭐ → ⭐ 三組
- **按類型分組：** 五種類型各列一段，供「想做動畫的優先挑哪些」這類查詢
- **依賴關係：** 若某 VizScript 用到前章節結果（例：UΣVᵀ 視覺化依賴 EVD），標明前置依賴

S12+ 開始實作 Python 視覺化時，從 VIZ-CATALOG 挑題目，每挑一個就有現成的 800 字劇本可直接餵 LLM 開做。

---

## 6. 版本

| 版本 | 日期 | 變更 |
|---|---|---|
| 0.1 | 2026-05-12 | 初版（S01.5 補規劃）|
| 0.2 | 2026-05-13 | S11 風格統一檢查 — §2.2 寫作要點 3/4 補 SCHEMA.md §3.5 cross-reference（配色 hex + 動畫時間無空格寫法）+ 新增 §2.3「全書視覺錨點 cross-reference」段（4 項對照表：配色 / cell 尺寸 / 動畫時間 / 3D 視角預設）|
