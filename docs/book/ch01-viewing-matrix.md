# 第 1 章. 矩陣的四種視角（Viewing a Matrix — 4 Ways）

> **原書頁碼：** p.2
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 15–47 行
> **本章圖數：** 1
> **本章 VizMark 數：** 2（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 0）
> **狀態：** [x] 已完成 / [ ] 校對中

---

## 章節摘要

一個 $m \times n$ 的矩陣 (matrix) 可以同時被當成**四種等價的物件**來看：

1. **整體一塊 (1 matrix)** — 一個運算子或一塊資料。
2. **$mn$ 個數字 (mn numbers)** — 二維表格中的個別元素 $a_{ij}$。
3. **$n$ 個列向量 (n column vectors)** — 把矩陣切成 $n$ 個直立的列 (column)，每列是 $\mathbb{R}^m$ 中的向量。
4. **$m$ 個行向量 (m row vectors)** — 把矩陣切成 $m$ 個橫躺的行 (row)，每行是 $\mathbb{R}^n$ 中的向量。

這四種視角描述的是**同一個數學物件**，但每一種「切法」對應到不同的線代直覺：整體視角對應線性變換的「黑盒子」、數字視角對應元素層級的運算（如點積 (dot product)）、列向量視角對應列空間 (column space) 與線性組合 (linear combination)、行向量視角對應行空間 (row space) 與「行方向」的看法。

本章是全書的「視角字典」：後面所有矩陣運算（vector × vector、matrix × vector、matrix × matrix、五種矩陣分解）都會反覆切換這四種視角來解釋同一個算式。能流暢切換視角，是讀懂這本書的入場票。

> ⚠ **中英術語慣例（全書通用）：** 本書採華文主流慣用 — **column = 列（直立）、row = 行（橫躺）**。若你過往讀台灣本土數學教科書習慣「column = 行、row = 列」（方向相反），此處請花一兩分鐘重新校準。本專案 `from-tex/zh.md` 為簡中譯本，用詞方向與本繁中版**一致**。

> ### 💡 背後觀念：矩陣為什麼存在 + 為什麼要 4 種視角？
>
> 本章「矩陣 4 視角」背後有兩個更深的動機問題：
>
> - **[Q02：矩陣為什麼存在？「把表格看成單一物件」是什麼躍進？](appendix-D-why.md#q02)** — 矩陣不是憑空的記法，而是 **1858 年 Cayley 把方陣獨立為代數物件**的躍進。西元前 1 世紀《九章算術》方程章已用方陣記係數，但僅當作「運算的工作區」。從**記法**到**代數物件**的演進，讓我們能對矩陣本身做加法、乘法、求逆、分解 — 整本書 6 條核心應用全部建立在這個物件化之上。
> - **[Q03：為什麼同一個矩陣要看成 4 種視角？](appendix-D-why.md#q03)** — 4 視角不是並列裝飾，是「**問題決定視角**」的數學設計原則。類比同一個三角形，已知三邊用海倫公式、已知兩邊夾角用 $\frac{1}{2}ab\sin C$、已知外接圓半徑用 $\frac{abc}{4R}$ — **公式不同，三角形是同一個**。4 視角的等價性 = 線代「所有結果無論從哪個視角推都會殊途同歸」的優美性質。

---

## 數學要點

> 一個 $3 \times 2$ 矩陣 $A$ 的四種等價寫法（取自原書 p.2）：

$$
A= \begin{bmatrix}
    a_{11} & a_{12}\\
    a_{21} & a_{22}\\
    a_{31} & a_{32}
\end{bmatrix}
=
\begin{bmatrix}
    | & |\\
    \mathbf{a}_1 & \mathbf{a}_2\\
    | & |
\end{bmatrix}
=
\begin{bmatrix}
    -\;\mathbf{a}_1^*\;-\\
    -\;\mathbf{a}_2^*\;-\\
    -\;\mathbf{a}_3^*\;-
\end{bmatrix}
$$

**符號約定（全書通用）：**

- **列向量 (column vector)：** 粗體小寫無上標，如 $\mathbf{a}_1$、$\mathbf{a}_2$。$\mathbf{a}_j$ 表示 $A$ 的第 $j$ 列 (column)，屬於 $\mathbb{R}^m$。
- **行向量 (row vector)：** 粗體小寫加 $*$ 上標，如 $\mathbf{a}_1^*$、$\mathbf{a}_2^*$、$\mathbf{a}_3^*$。$\mathbf{a}_i^*$ 表示 $A$ 的第 $i$ 行 (row)，屬於 $\mathbb{R}^n$（橫向長度為 $n$）。
- **轉置 (transpose)：** 上標 $\mathrm{T}$，如 $\mathbf{a}^{\mathrm{T}}$、$A^{\mathrm{T}}$。

---

## 圖片區

### Figure 1.1: 矩陣的四種視角（Viewing a Matrix in 4 Ways）

**圖檔：** `docs/book/figs-png/ViewingMatrix-4Ways.png`（原始 EPS：`figs/ViewingMatrix-4Ways.eps`）
**原書頁碼：** p.2
**所屬章節：** §1

#### 視覺結構 (Visual Structure)

此圖採「上下兩排、左右並列 4 區」的結構：

- **上排（抽象示意）：** 從左到右四個圖示，以 `=` 號相連。
  1. **第 1 區：** 一塊純灰色實心矩形 — 代表「整個矩陣作為單一物件」。
  2. **第 2 區：** 灰色矩形外框，內含 $3 \times 2 = 6$ 個藍色實心小圓點（排成 3 行 2 列） — 代表「6 個個別數字」。
  3. **第 3 區：** 兩個並列的綠色直條色塊 — 代表「2 個列向量 (column vectors)」，每條包含 3 個數字。
  4. **第 4 區：** 三個堆疊的粉紅色橫條色塊 — 代表「3 個行向量 (row vectors)」，每條包含 2 個數字。
- **下排（具體例子）：** 同樣的四個視角，但以 $A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$ 為具體實例對照。
  1. **第 1 區：** 灰色實心方塊上印一個白色大寫字母 `A`。
  2. **第 2 區：** 矩陣完整列出 6 個數字 `1 4 / 2 5 / 3 6`，每個數字疊一個藍色小圓點。
  3. **第 3 區：** 同樣的 6 個數字，但**兩個直立的列 (columns)** 被半透明綠色背景高亮（左列 `1,2,3`、右列 `4,5,6`）。
  4. **第 4 區：** 同樣的 6 個數字，但**三個橫躺的行 (rows)** 被半透明粉紅色背景高亮（上行 `1,4`、中行 `2,5`、下行 `3,6`）。
- **配色語意：** 灰 = 整體、藍點 = 個別元素、綠直條 = 列向量、粉紅橫條 = 行向量。**藍 / 綠 / 粉紅** 三色在後續章節（§2–§6）會反覆出現代表同樣語意。
- **底部標籤：** 由左至右為 `1 matrix` / `6 numbers` / `2 column vectors with 3 numbers` / `3 row vectors with 2 numbers`，強化四個視角的口語名稱。

讀者的視覺動線：先由左至右看上排（抽象意義）→ 對下排具體例子，建立「抽象 ↔ 具體」連結 → 注意配色三組（灰 / 藍 / 綠 / 粉紅）對應四個視角的固定語意。

#### 數學內容 (Mathematical Content)

圖中所演示的矩陣：

$$
A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix} \in \mathbb{R}^{3 \times 2},\quad m=3,\; n=2
$$

四種視角的數學形式：

$$
\underbrace{A}_{\text{1 matrix}}
=
\underbrace{(a_{ij})_{3 \times 2}}_{6 \text{ numbers}}
=
\underbrace{\begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 \end{bmatrix}}_{2 \text{ column vectors in } \mathbb{R}^3}
=
\underbrace{\begin{bmatrix} \mathbf{a}_1^* \\ \mathbf{a}_2^* \\ \mathbf{a}_3^* \end{bmatrix}}_{3 \text{ row vectors in } \mathbb{R}^2}
$$

其中：

$$
\mathbf{a}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix},\;
\mathbf{a}_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix} \in \mathbb{R}^3
$$

$$
\mathbf{a}_1^* = \begin{bmatrix} 1 & 4 \end{bmatrix},\;
\mathbf{a}_2^* = \begin{bmatrix} 2 & 5 \end{bmatrix},\;
\mathbf{a}_3^* = \begin{bmatrix} 3 & 6 \end{bmatrix} \in \mathbb{R}^2
$$

**維度檢核：** 列向量數 $n=2$，每列住在 $\mathbb{R}^m = \mathbb{R}^3$；行向量數 $m=3$，每行住在 $\mathbb{R}^n = \mathbb{R}^2$。**列數 = $n$、行數 = $m$**，向量住的空間維度與「另一邊」的計數相同 — 這是讀者常犯混淆的點。

#### 直覺解讀 (Intuition)

這張圖看似簡單，但**它是全書的根本字典**。理解它的關鍵有三：

**1. 「等號」是視角等價，不是運算。** 上排四個圖示用 `=` 連接，這個 `=` 的意思是「以下四種看法描述同一個矩陣 $A$」，不是運算過程。從第 1 區走到第 4 區不需要做任何計算，只是換一副眼鏡。

**2. 配色是後續章節的伏筆。** 綠色 = 列、粉紅 = 行、藍 = 個別元素，這個配色約定貫穿全書。當你在 §3 看到 $A\mathbf{x}$ 用綠色高亮列向量、$\mathbf{y}A$ 用粉紅色高亮行向量時，就會立刻知道「啊這是列視角 / 行視角」。先在這張圖把配色刻進腦中，後面就省力。

**3. 四個視角對應四套運算直覺：**
- **整體視角** → 把矩陣當函式 $A: \mathbb{R}^n \to \mathbb{R}^m$，輸入向量輸出向量。
- **數字視角** → 元素級運算（如 $C_{ij} = \sum_k A_{ik}B_{kj}$ 點積式），最底層但最瑣碎。
- **列向量視角** → 線性組合：$A\mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots$，這把矩陣乘法看成「拿列向量按係數混合」。是 Strang 大力強調的視角。
- **行向量視角** → 點積式：$(A\mathbf{x})_i = \mathbf{a}_i^* \cdot \mathbf{x}$，等價但情境不同（如左乘 vs 右乘）。

**常見誤解警示：**
- 「6 個數字視角」≠「沒結構的散沙」 — 數字仍按 $(i,j)$ 索引組織，圖中藍點的排列保留了行列位置。
- 「行 / 列」中英術語易混 — 切記：**column 是直立的（中文：列）、row 是橫躺的（中文：行）**。若先前讀過台灣本土教材有相反習慣，請在此處重新校準。

**為什麼這張圖該做成互動視覺化？** 因為「視角切換」是動態的心智動作，靜態圖只能擺出 4 個成品結果，但無法呈現「同一個 $A$ 在你按下不同視角鈕時，**怎麼從一種樣子過渡到另一種樣子**」。這正是 VizMark-01 要解決的事 — 用動畫把抽象的「視角等價」演成可感知的「形變過渡」。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [切換視角] ⭐⭐⭐
> **位置：** Figure 1.1 / §1
> **核心概念：** 同一矩陣的 4 種等價觀看視角
> **互動梗概：** 按 4 個視角鈕，主圖即時切換並動畫過渡；矩陣維度可拉桿調整
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [拉桿調參] ⭐⭐
> **位置：** Figure 1.1 / §1
> **核心概念：** 維度 $m, n$ 改變時，4 視角的結構如何同步重組
> **互動梗概：** 拉 $m, n$ slider 改變矩陣形狀，4 個視角的圖示同步即時重畫
> **詳見劇本：** VizScript-02（章末）

---

## 視覺化劇本（VizScripts）

> 本章兩個 VizMark 對應兩個 VizScript。格式遵 `VIZ_SCHEMA.md` §2（A–M 共 13 段）。
> 兩個劇本實作時可合成單一視覺化頁面（共用控制列、共用畫布），不必拆兩支獨立程式。

### VizScript-01: 矩陣的四種觀看視角（4 Ways Toggle）

#### A. 一句話定位
讓使用者切換 4 種視角，看同一矩陣呈現出 4 種等價但風格迥異的「身分」。

#### B. 學習目標（Learning Outcome）
- 使用者能說出矩陣的 4 種觀看方式名稱（whole / numbers / columns / rows）
- 使用者能在切換時指出哪個元素 $a_{ij}$ 對映到哪個列向量 $\mathbf{a}_j$、哪個行向量 $\mathbf{a}_i^*$
- 使用者能說明「為什麼這 4 種視角描述的是同一個矩陣」
- 使用者能在腦中預測：若改 $a_{12}$，4 個視角中哪些區塊會變色 / 變數字
- 使用者能正確指認本書慣例「column = 列（直立）、row = 行（橫躺）」

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$
- **預設值：** $A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$（m=3, n=2，與原書圖 1.1 一致）
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$（由 VizMark-02 / VizScript-02 控制）
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1
- **退化情形：** rank-deficient（如某列為他列倍數）時，columns 視角中相依的列畫虛線外框並 tooltip 警示

#### D. 視覺布局（Visual Layout）
- **整體比例：** 左 60% 主畫面、右 25% 公式 / 資訊區、底 15% 視角切換條
- **主畫面尺寸：** 640×560 px，白底，cell 60×60 px 視 $m, n$ 自動縮放
- **副畫面（公式區）：** 上半 LaTeX 公式（MathJax 渲染）+ 下半當前視角的一句話說明（≤ 30 字）+ 即時 `rank(A)` 數值
- **底部視角切換條：** 4 個 radio button（whole / numbers / columns / rows），等寬排列
- **配色（hex）：**
  - 矩陣外框 `#333333`
  - cell 底 `#fafafa`、cell 文字 `#000000` 16pt monospace（Menlo / Consolas）
  - whole 視角整體外框 `#2ca02c`（綠）3px 粗
  - numbers 視角藍色圓點 `#1f77b4`，直徑 14px，置於 cell 右上角
  - columns 視角直立列高亮底 `#a8e6a3`（淡綠，alpha 0.4）
  - rows 視角橫躺行高亮底 `#f9c0c0`（淡粉，alpha 0.4）
- **字型：** 標題 18pt sans bold、座標標籤 12pt sans regular
- **邊距：** 上下左右各 20px，cell 間距 4px

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 | radio (4) | whole / numbers / columns / rows | whole | 即時（400ms 過渡動畫） |
| m | slider | [2, 6] step 1 | 3 | 即時 |
| n | slider | [2, 6] step 1 | 2 | 即時 |
| $a_{ij}$ | numeric input grid $m \times n$ | [-9, 9] step 1 | 預設矩陣 | onBlur |
| 重設 | button | — | — | click → 還原預設 A |

#### F. 輸出畫面細節（Outputs）
- **whole 視角：** 矩陣整體外框加粗 3px 綠色，內部 cell 邊框淡灰，cell 文字正常顯示。
- **numbers 視角：** 每個 cell 右上角疊一個藍色實心圓點（呼應原書），cell 邊框加粗 1.5px。
- **columns 視角：** 每一直立的列以縱向半透明綠色色塊覆蓋（alpha 0.4），列間隔加大 8px，列底標籤 $\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n$。
- **rows 視角：** 每一橫躺的行以橫向半透明粉色色塊覆蓋（alpha 0.4），行間隔加大 8px，行右側標籤 $\mathbf{a}_1^*, \ldots, \mathbf{a}_m^*$。
- **公式區當前視角文字：**
  - whole：$A = (a_{ij})_{m \times n}$
  - numbers：逐一列出 $a_{ij}$ 的值
  - columns：$A = [\mathbf{a}_1 \;|\; \cdots \;|\; \mathbf{a}_n],\; \mathbf{a}_j \in \mathbb{R}^m$
  - rows：$A = \begin{bmatrix} \mathbf{a}_1^* \\ \vdots \\ \mathbf{a}_m^* \end{bmatrix},\; \mathbf{a}_i^* \in \mathbb{R}^n$
- **數字顯示精度：** 整數視角顯示原值；若改為浮點數模式（未來擴充）保留 2 位小數。
- **即時 rank：** 公式區下方一直顯示 `rank(A) = r`，由 `numpy.linalg.matrix_rank(A, tol=1e-9)` 計算。

#### G. 互動行為（Interactions）
- **hover cell：** 該 cell 加粗外框 + tooltip 顯示 `A[i+1][j+1] = value`（1-indexed 對齊原書）
- **click cell：** 該 cell 持續高亮 + 在公式區用相同色標記該 cell 所屬的列 $\mathbf{a}_j$ 與行 $\mathbf{a}_i^*$
- **click 列向量區（columns 視角時）：** 整列持續高亮 + 右側顯示該列作為 $\mathbb{R}^m$ 向量的座標列表
- **click 行向量區（rows 視角時）：** 整行持續高亮 + 右側顯示該行作為 $\mathbb{R}^n$ 向量的座標列表
- **快捷鍵：** 數字鍵 `1`/`2`/`3`/`4` 切換 whole/numbers/columns/rows；箭頭鍵移動 cell focus；`Esc` 取消選取
- **拖曳：** 不支援（避免與 numeric input 衝突）

#### H. 動畫腳本（視角切換）
- **t=0：** 當前視角穩態。
- **t=0–150ms：** 當前視角的特徵元素淡出（如 columns 視角的綠色色塊 opacity 0.4 → 0）。
- **t=150–400ms：** 新視角的特徵元素淡入 + 從中心向外展開（scale 0.85 → 1.0、opacity 0 → 目標 alpha）。
- **t=400ms 後：** 新視角穩態，cell 文字保持不變。
- **總長度：** 400ms
- **緩動函數：** ease-in-out（CSS `cubic-bezier(0.4, 0, 0.2, 1)` 等價）
- **可暫停 / 倒轉：** 否（< 500ms 短動畫無此需求）。

#### I. 邊界與錯誤處理
- **m=n=2 最小矩陣：** cell 尺寸增至 80×80 避免畫面空蕩。
- **m=6, n=6 最大：** cell 縮至 40×40、字級降為 12pt、動畫禁用避免頓挫。
- **使用者輸入非整數：** 紅框警示 0.5 秒後還原前一值，並在底部 status bar 顯示「請輸入 -9 到 9 的整數」。
- **rank-deficient（如 $\mathbf{a}_1 = 2 \mathbf{a}_2$）：** columns 視角中相依的列畫虛線外框 + tooltip「此列與其他列線性相依」；公式區 rank 數值用紅字顯示。
- **全零矩陣：** rank=0，所有視角正常顯示但加底部提示「零矩陣 — 所有列 / 行向量皆為零」。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - 視角 radio：滑過各鈕時顯示一句話定義（如「whole：把矩陣視為一個整體運算子」）
  - m slider：「行數 (rows) — 矩陣有幾橫躺的行，每行是 $\mathbb{R}^n$ 向量」
  - n slider：「列數 (columns) — 矩陣有幾直立的列，每列是 $\mathbb{R}^m$ 向量」
- **Walkthrough（首次開啟自動觸發，5 步驟）：**
  1. 「先看 whole 視角，這是一個 $3 \times 2$ 矩陣」
  2. 「按 numbers，看到的是同樣的 6 個數字，只是被攤開來標示」
  3. 「按 columns，看到 2 個列向量，每個都住在 $\mathbb{R}^3$」
  4. 「按 rows，看到 3 個行向量，每個都住在 $\mathbb{R}^2$」
  5. 「四種視角是等價的，描述同一個矩陣 $A$」
- **常見誤解警示卡：** 「本書採華文主流慣用：**column = 列（直立）、row = 行（橫躺）**。若你過去讀過台灣本土教材習慣相反方向，請花一兩分鐘調整。」
- **延伸閱讀：** 原書 p.2 §1、Strang《Linear Algebra for Everyone》§1.1
- **後續章節：** 看完 §1 後，§2 開始用同樣的配色標記 vector × vector

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo（反應式 notebook）+ matplotlib（2D 矩陣繪製）+ marimo.ui（控制元件）
- **替代方案：** Streamlit + Plotly（如需網頁部署）；ipywidgets + Jupyter（如要 .ipynb 分享）
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫 cell
  - `matplotlib.text.Text` 放數字與標籤
  - `matplotlib.patches.Circle` 畫 numbers 視角的藍點
  - `marimo.ui.radio`, `marimo.ui.slider`, `marimo.ui.number`
  - `numpy.linalg.matrix_rank`
- **檔案結構建議：**
  ```
  viz/
    ch01_viewing_matrix.py       # 主入口（含 VizScript-01 + 02）
    _common/
      palette.py                  # 統一配色 hex 常數
      layout.py                   # cell 尺寸自動計算
      i18n.py                     # 中英術語對照
  ```
- **效能考量：** $m, n$ 改變時呼叫 `ax.clear()` 後整重畫；切勿每次 `plt.figure()` 否則記憶體洩漏。
- **測試：** 4 個視角各做 1 張 snapshot PNG（`tests/snapshots/ch01_{whole,numbers,columns,rows}.png`），CI 比對。

#### L. 驗收標準（Acceptance Criteria）
- [ ] 4 個視角可切換，視覺呈現符合 §D / §F 規範
- [ ] $m, n$ slider 在 [2, 6] 範圍內拉動，cell 永不重疊、永不出框
- [ ] 任意 $a_{ij}$ 編輯後 < 100ms 重算並重畫完成
- [ ] 視角切換動畫總長 ≤ 400ms，60fps 無 frame drop
- [ ] rank-deficient 時 columns 視角虛線標示正確、rank 數值正確
- [ ] Walkthrough 5 步驟首次開啟自動觸發，可關閉並記住偏好
- [ ] 鍵盤 `1`/`2`/`3`/`4` 切換視角生效

#### M. 互動深度 Tier + 估時
- **Tier 1（基礎，0.5–1 session）：** 4 視角靜態切換 + $m, n$ slider，無動畫、無 cell 編輯。
- **Tier 2（增強，1–2 session）：** + cell 編輯 + tooltip + 視角切換動畫 + walkthrough。
- **Tier 3（完整，2–3 session）：** + 拖曳列向量端點改值（2D 幾何 drag）+ 多矩陣對比（split view）+ 匯出 PNG。
- **本劇本目標 Tier：** Tier 2
- **估時：** 1.5 session（含 snapshot 測試與 walkthrough）

---

### VizScript-02: 矩陣維度的同步重組（Dimensions Synchronizer）

#### A. 一句話定位
拉動 $m, n$ slider 看「同一個 $A$ 在 4 個視角下，cell 數與向量數如何同步改變」。

#### B. 學習目標（Learning Outcome）
- 使用者能說明：列向量數 = $n$、行向量數 = $m$（不是反過來）
- 使用者能說明：列向量住在 $\mathbb{R}^m$、行向量住在 $\mathbb{R}^n$
- 使用者能在腦中預測：把 $n$ 從 2 拉到 5，columns 視角會多 3 條綠直條
- 使用者能在腦中預測：把 $m$ 從 3 拉到 5，每個列向量會「變長」（從 3 維變 5 維）

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$（與 VizScript-01 共用同一個 $A$）
- **預設值：** 與 VizScript-01 同（$m=3, n=2$，預設值 1-6）
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$，共 25 種組合
- **數值範圍：** 維度改變時，新增 cell 預設值用「順序遞增」填充（既有 cell 保留原值）。例如 $3 \times 2 \to 3 \times 3$，新增第 3 列填 `7, 8, 9`。
- **退化情形：** $m = n$（方陣）時，UI 不做特殊處理但底部 status bar 提示「方陣」。

#### D. 視覺布局（Visual Layout）
- **共用 VizScript-01 的整體布局**，新增以下元素：
  - 主畫面左上角：當前維度 badge `m × n` 大字（24pt sans bold，顏色 `#666`），slider 拖動時即時更新。
  - 主畫面右上角：對比框 — 始終並列顯示「上排抽象示意（4 個小圖示）」尺寸固定，不隨 $m, n$ 縮放，作為「速查圖鑑」。
  - 底部 slider 區：$m$ slider 與 $n$ slider 各佔 50% 寬，標籤「行數 m / rows」「列數 n / columns」。
- **動畫過渡時的補位策略：** 維度增加時，新 cell 從外往內滑入（位移動畫 200ms）；維度減少時，被切除的 cell 淡出 + 折疊（200ms）。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 | 預設 | 觸發 |
|---|---|---|---|---|
| m | slider | [2, 6] step 1 | 3 | 即時（200ms 動畫） |
| n | slider | [2, 6] step 1 | 2 | 即時（200ms 動畫） |
| 「同步換預設值」checkbox | toggle | on / off | off | 即時 |

- **「同步換預設值」on：** 維度變時整個 $A$ 用 1..mn 重填（如 $m=4, n=3$ 自動填 1-12）。
- **「同步換預設值」off（預設）：** 維度增加時新 cell 補 0；維度減少時被切的值保留在記憶體（再拉大時還原）。

#### F. 輸出畫面細節（Outputs）
- **m 拉桿改變：**
  - whole 視角：矩陣縱向拉長 / 縮短，外框比例同步調整。
  - numbers 視角：藍點以 grid 排列同步增刪。
  - columns 視角：每條列向量「變長 / 變短」（綠色直條的高度變化）；列數不變。
  - rows 視角：橫條（行向量）「增加 / 減少」（新增一橫條粉色色塊，或最下方一橫條淡出消失）。
- **n 拉桿改變：**
  - whole 視角：矩陣橫向拉寬 / 縮窄。
  - numbers 視角：藍點橫向增刪。
  - columns 視角：直條（列向量）「增加 / 減少」（新增綠色直條從右側滑入，或最右側直條淡出）。
  - rows 視角：每條行向量「變長 / 變短」（粉色橫條的寬度變化）；行數不變。
- **公式區即時更新：** 維度標籤 `m × n` 與 rank 同步重算。

#### G. 互動行為（Interactions）
- **slider 即時拖動：** 不只是 onChange 觸發，連 onInput 也觸發，達到「拉到一半就看到中間態」的即時感（但動畫節流到 60fps）。
- **slider 連按方向鍵：** 每按一次 step 1，伴隨 200ms 動畫；連按時動畫排隊但不疊加。
- **hover slider 數值：** tooltip 顯示「m=4 → 4 個行向量，每個住在 $\mathbb{R}^n$」之類即時提示。

#### H. 動畫腳本（維度變化）
- **新增 cell：**
  - t=0：新 cell 透明且在最終位置外側 20px。
  - t=0–200ms：透明度 0 → 1，位置滑回最終位置。
  - 緩動：ease-out。
- **刪除 cell：**
  - t=0：cell 在原位置，透明度 1。
  - t=0–200ms：透明度 1 → 0，位置朝外側滑出 20px。
  - 緩動：ease-in。
- **既有 cell 重排：**
  - t=0–200ms：位置線性過渡到新格點。
  - 緩動：ease-in-out。
- **節流：** slider 連續拖動時，動畫只在 step 完成後重設；中間不堆疊 keyframe。

#### I. 邊界與錯誤處理
- **m=2, n=2 最小：** slider 仍可下降到此，再低則 slider 鎖在 2，cursor 變 not-allowed。
- **m=6, n=6 最大：** cell 縮至 40×40、字級 12pt，動畫期間禁用 hover effect 避免閃爍。
- **同步換預設值勾選時 $a_{ij}$ 編輯：** 編輯時自動取消勾選並 status bar 提示「已切換到手動模式」。
- **rank 重算失敗（極罕見）：** 顯示 `rank = ?` 並 console.warn，不阻斷 UI。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - m slider：「m = 行數 = rows，影響列向量長度（每列是 $\mathbb{R}^m$）」
  - n slider：「n = 列數 = columns，影響行向量長度（每行是 $\mathbb{R}^n$）」
- **Walkthrough（與 VizScript-01 共用，補加 2 步）：**
  6. 「現在拉 m slider，注意列向量怎麼變長（綠直條變高）」
  7. 「拉 n slider，注意行向量怎麼變長（粉橫條變寬）」
- **常見誤解警示框：** 「初學者常混淆：『列向量有 n 個』而不是 m 個 — 因為每個直立的列是『一條 down to m 元素』，列向量數量等於『有幾條這樣的直列』，也就是 n。」
- **互動小測驗（選用）：** 「猜猜：當 $m=4, n=3$ 時，rows 視角有幾條橫條？」（答：4）

#### K. 技術實作建議（Tech Stack Hints）
- **與 VizScript-01 共享同一支 Python 主檔，** 不要拆兩支。
- **狀態管理：** 用 marimo 的 reactive cell 或 Streamlit 的 `st.session_state` 持存「使用者輸入過的歷史 $a_{ij}$」（供拉小再拉大時還原）。
- **動畫實作：**
  - matplotlib：用 `FuncAnimation` + blit 提升效能。
  - 替代：plotly `frame` 動畫（如選 Streamlit + Plotly 路線）。
- **效能：** 每次維度變化呼叫 `ax.clear()` 後重建 patches，不要在 patches list 上 incremental add/remove（容易脫鉤）。

#### L. 驗收標準（Acceptance Criteria）
- [ ] $m, n$ 改變時 4 個視角同步重畫，無 ghost cell 殘留
- [ ] 「同步換預設值」勾選 / 取消行為正確
- [ ] 維度增加時新 cell 預設值符合規格（補 0 或 1..mn）
- [ ] 維度減少再增加時，原值能還原（off 模式下）
- [ ] 動畫期間 hover 不觸發 tooltip（避免閃爍）
- [ ] 維度 badge `m × n` 與 `rank` 即時更新延遲 < 50ms

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1：** 維度改變即時重畫無動畫
- **Tier 3 擴充：** + 滑動到極端值時的「教學旁白」配音 / 字幕
- **估時：** 0.5 session（與 VizScript-01 同檔開發，主要工作是 slider 連動 + 動畫節流）

---

## 章末延伸

- **下一章：** [→ ch02-vec-vec.md](ch02-vec-vec.md) — Vector × Vector 的 2 種視角（v1 點積 / v2 外積）
- **延伸閱讀：** Gilbert Strang《Linear Algebra for Everyone》§1.1（線性組合與點積）、§1.3（秩 1 矩陣）、§1.4（行方式與列方式 row way & column way）
- **本章在「五大分解」中的位置：** 全書的「字典頁」 — 後面 §6 五大分解的圖示都會用本章建立的 4 視角 + 配色約定。

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 15–47 / `The-Art-of-Linear-Algebra.pdf` p.2
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` 對應段落（用詞方向與本繁中版一致，皆採華文主流 A 派）
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0
