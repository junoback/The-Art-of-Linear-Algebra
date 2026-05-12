# 線性代數的藝術 — 互動式視覺化教材 / The Art of Linear Algebra — Interactive Visualization

> **本檔說明：** 全書合併單檔（BOOK.md），由 16 個分離的 md 檔合併生成
> 基於 Kenji Hiranabe《The Art of Linear Algebra》圖解筆記（2020–2024），參考 Gilbert Strang《Linear Algebra for Everyone》(2020) — 重新詮釋為互動式 Python 視覺化教材
>
> - **作者：** Kenji Hiranabe（原書圖解）+ Back Kuo & Claude（互動式視覺化整合）
> - **依據書籍：** Strang, *Linear Algebra for Everyone* (2020) — 全書視覺對應 §1–§7
> - **產出時間：** S11 整合階段（2026-05-13，含風格統一檢查校正）
> - **總計：** 16 個原 md 檔 / 8520 行 / **36 個 VizScript**
> - **狀態：** §1–§6 全書內容章節 100% 完成 — S12+ 進入 Python 視覺化實作階段
>
> **如何閱讀：** 本檔為「整本書下載 / 離線閱讀」用合併版；GitHub UI 上瀏覽建議用分離的 md 檔（連結保留原 `ch01-viewing-matrix.md#vizscript-01` 等跨檔錨點）。本檔內的跨檔連結會跳到原 md 檔的相對位置。

---

## 全書目錄（Table of Contents）

| 章節 | 主題 | 內容焦點 |
|---|---|---|
| **Foreword（序言）** | Strang 推薦序 + 三大主題導讀 + 1920–2026 緣起 + 路線 A/B/C | 158 行，0 VizMark |
| **§1 Viewing a Matrix - 4 Ways** | 矩陣的四種視角（直立列 / 橫躺行 / cell / 整塊）| 418 行，2 VizScript |
| **§2 Vector × Vector - 2 Ways** | 點積 (Dot) + 外積 (Outer) | 497 行,2 VizScript |
| **§3 Matrix × Vector - 2 Ways + 4-Subspaces** | (Mv1) / (Mv2) + (vM1) / (vM2) + Strang 兩塊大餅圖 | 935 行，4 VizScript |
| **§4 Matrix × Matrix - 4 Ways** | (MM1) – (MM4) 含 ⭐⭐⭐ Tier 3 Mona Lisa SVD demo | 849 行，4 VizScript |
| **§5 Practical Patterns** | P1/P2/P1'/P2'/P3/P4 共 6 個 Pattern + 4 圖 | 830 行，4 VizScript |
| **§6 The Five Factorizations of a Matrix** | 五大分解總覽 + §6.1–§6.5 細節 | （見子章節）|
| ─ §6 Overview | 五大分解一覽 + Tier 1 + pointer dashboard | 331 行，1 VizScript |
| ─ §6.1 A = CR | 列秩 = 行秩 + 對偶兩圖 + `using P1/P2` | 545 行，3 VizScript |
| ─ §6.2 A = LU | 三角分解 + 高斯消去 + `using MM4` | 654 行，3 VizScript |
| ─ §6.3 A = QR | Gram–Schmidt + 3D 投影 + `using P1` | 541 行，3 VizScript |
| ─ §6.4 S = QΛQᵀ | 譜分解 + 橢球主軸 + `using P4` | 695 行，3 VizScript |
| ─ §6.5 A = UΣVᵀ | SVD + ⭐⭐⭐ Tier 3 旗艦 + 4 應用 + `using P4` | **934 行（全書最長）**，4 VizScript |
| **Conclusion & References** | 結論 + 全書 36 個 VizScript 總覽 + Tier 統計（S11 校正版）+ S12+ 排程 | 199 行，0 VizMark |
| **Appendix A: Map of Eigenvalues** | 12 類矩陣 × 特徵值幾何位置完整表 | 272 行，1 VizScript |
| **Appendix B: Matrix World** | **11 層同心橢圓繼承樹 + ⭐⭐⭐ Tier 2 旗艦 — S12+ 教材首頁** | 328 行，1 VizScript |
| **Appendix C: The Four Subspaces** | Strang 兩塊大餅圖 + SVD 構造 4 基底 + 解 Ax=b 完整結構 | 334 行，1 VizScript |

---

## 全書統計（S11 校正版）

### VizScript 計數（合計 36）

| 類別 | 數量 | 列表 |
|---|---|---|
| ⭐⭐⭐ Tier 3 旗艦 | **2** | ch04 V-02（MM4 + Mona Lisa）/ ch06f V-01（SVD Master + 4 應用）|
| ⭐⭐⭐ Tier 3 候選 | **1** | ch03 V-02（4 Subspaces — S12+ 視時間升級）|
| ⭐⭐⭐ Tier 2 旗艦（附錄）| **1** | appendix-matrix-world V-01（**S12+ 教材首頁**）|
| ⭐⭐ Tier 2 主章 | **14** | ch01 V-01/02, ch02 V-01/02, ch03 V-01/03, ch04 V-01, ch05 V-01/02, ch06b/c/d/e V-01, ch06f V-02 |
| ⭐⭐ Tier 1 + pointer | **3** | ch06a V-01（§6 dashboard）+ map-eigenvalues V-01 + four-subspaces V-01 |
| ⭐ Tier 1（精簡 / 輕量）| **15** | 各章次要 / walkthrough VizScript |
| **總計** | **36** | 主章 33 + 附錄 3 |

### `using XX` PNG 標記譜系（S07–S10 重核確認）

| PNG | 標記 | 對應 Pattern | 視覺化 pointer 設計 |
|---|---|---|---|
| CR1 / CR2 | `using P1` / `using P2` | P1（列線性組合）/ P2（行線性組合）| ch06b V-01 雙 pointer 指 ch05 V-01 + ch04 V-02 |
| LU1 / LU2 | 無 / `using MM4` | MM4（秩 1 累加）| ch06c V-01 單 pointer 指 ch04 V-02 |
| QR | `using P1` | P1（列線性組合，R 上三角特化）| ch06d V-01 單 pointer 指 ch05 V-01 |
| EVD | `using P4` | P4（三明治，左右轉置）| ch06e V-01 單 pointer 指 ch05 V-03 |
| SVD | `using P4` | P4（三明治，雙側獨立）| ch06f V-01 **雙 pointer** 指 ch04 V-02 + ch05 V-03（全書唯一）|
| 附錄 3 張 | 無 | 地圖層級非 Pattern 套用層級 | 採整合 pointer 策略 |

### 章節篇幅比例（§6 五大分解，CR 為基準 1.0）

| 章節 | 行數 | 比例 | 應用面廣度 |
|---|---|---|---|
| §6.1 CR | 545 | 1.00 | 列秩 = 行秩證明 |
| §6.2 LU | 654 | 1.20 | 解 Ax=b 完整流程 |
| §6.3 QR | 541 | 0.99 | 最小二乘法 |
| §6.4 EVD | 695 | 1.28 | 對稱譜分解 + 二次型 |
| §6.5 SVD | **934** | **1.71** | **4 大應用集大成（壓縮 / PCA / 降噪 / 推薦）** |

### 全書視覺錨點（S11 規範化，詳見 [SCHEMA.md §3.5](SCHEMA.md#35-全書視覺錨點s11-規範化)）

| 錨點 | 規範值 |
|---|---|
| 6 主色 | 綠 `#2ca02c` / 粉紅 `#d62728` / 藍 `#1f77b4` / 紫 `#9467bd` / 橙 `#ff7f0e` / 金 `#FFD700` |
| 動畫時間 | 50ms / 200ms / 500ms / 800ms / 1500ms / 3000ms（無空格寫法）|
| **3D 視角預設** | **elevation=25° / azimuth=-60°**（全書 109 次 3D 提及統一錨點）|


---

## 序言（Foreword）— Gilbert Strang 推薦序與本書緣起

> **原書頁碼：** 英文版 p.1（書首）/ 簡中版 p.1
> **對應 .tex 段落：** `from-tex/en.md` 第 1–14 行 / `from-tex/zh.md` 第 1–11 行
> **本章圖數：** 0
> **本章 VizMark 數：** 0（散文章節，純文字導讀）
> **狀態：** [x] 已完成

---

### 章節摘要

《The Art of Linear Algebra》是日本敏捷顧問 Kenji Hiranabe（平鍋健兒）為 Gilbert Strang 的《Linear Algebra for Everyone》撰寫的圖解筆記。書首 Hiranabe 引用 Strang 親筆推薦序，Strang 在序中明確指出：「**圖解（pictures）是展示代數的絕佳方式**」，並強調除了「**行 · 列 點積**」之外，「**線性組合**」與「**秩 1 矩陣**」才是「**完成代數與藝術**」的關鍵。這短短一句話奠定了全書的兩大主軸 — 後續 §1–§6 的所有圖解，本質上都是「線性組合 + 秩 1 矩陣」這兩個概念的視覺呈現。本互動式版本（S02–S11 開發）把書中 50 張靜態圖轉成可調參即時看結果的 Python 視覺化，並補上 23 個 VizScript 細緻劇本，把 Strang/Hiranabe 的「直覺優先教學風格」推進到「可手動互動體驗」的下一階段。

---

### Gilbert Strang 推薦序（原文與繁中翻譯）

#### 英文原文

> I am happy to see Kenji Hiranabe's pictures of matrix operations in linear algebra! The pictures are an excellent way to show the algebra. We can think of matrix multiplications by row $\cdot$ column dot products, but that is not all — it is "linear combinations" and "rank 1 matrices" that complete the algebra and the art. I am very grateful to see the books in Japanese translation and the ideas in Kenji's pictures.
>
> — Gilbert Strang
> Professor of Mathematics at MIT

#### 繁體中文翻譯

> 我很高興能看到 Kenji Hiranabe 線性代數中矩陣運算的圖解！這些圖解是展示代數的絕佳方式。我們當然可以透過「行 (row) $\cdot$ 列 (column) 點積」來理解矩陣乘法，但那絕非全部 — 真正完成這門代數與藝術的，是「**線性組合 (linear combinations)**」和「**秩 1 矩陣 (rank 1 matrices)**」。我很感激能看到本書日文翻譯版，以及 Kenji 圖解中的所有想法。
>
> — Gilbert Strang
> 麻省理工學院（MIT）數學教授

---

### 序言三大主題（導讀）

Strang 序言雖短（不到 100 字），卻明確指出貫穿全書的**三大主題**。對應到本互動式版本的章節：

#### 主題 1：圖解優於符號

> **原文關鍵句：** "The pictures are an excellent way to show the algebra."

線性代數的傳統教材以**符號公式**為主、圖解為輔。本書反其道而行 — **圖解是主**、公式是輔。每張圖都是一個獨立的思考工具，公式只是對圖的形式化。

**對應章節：** 全書 §1–§6 共 50 張圖，每張都對應 1–4 個 VizMark + VizScript，把「圖解優於符號」的精神推進到「**可互動的圖解**」。

#### 主題 2：超越「行 · 列點積」的視野

> **原文關鍵句：** "We can think of matrix multiplications by row $\cdot$ column dot products, but that is not all."

傳統線代教學的入門點是「矩陣乘法 = 行 · 列點積」（即本書的 (Mv1)、(MM1) 視角）。Strang 強調這「不是全部」 — 必須同時看到**列空間視角**（(Mv2)、(MM2)）、**秩 1 視角**（(MM4)），才算真正理解矩陣乘法。

**對應章節：**
- §1 [Viewing a Matrix - 4 Ways](ch01-viewing-matrix.md)：1 個矩陣的 4 種觀看視角
- §2 [Vector × Vector - 2 Ways](ch02-vec-vec.md)：點積 (v1) vs 外積 (v2)
- §3 [Matrix × Vector - 2 Ways](ch03-mat-vec.md)：(Mv1) 點積版 vs (Mv2) 線性組合版
- §4 [Matrix × Matrix - 4 Ways](ch04-mat-mat.md)：(MM1)–(MM4) 四種乘法視角

#### 主題 3：線性組合 + 秩 1 矩陣 = 完整代數的藝術

> **原文關鍵句：** "it is 'linear combinations' and 'rank 1 matrices' that complete the algebra and the art."

這是 Strang 序言的**核心宣言**。**所有矩陣分解**（§6 的五大分解）的數學本質都是把矩陣寫成「**秩 1 矩陣之和**」 — 也就是 (MM4) 視角的應用：
$$
A = \sum_{p=1}^{r} \mathbf{x}_p \mathbf{y}_p^*
$$
五大分解（CR / LU / QR / EVD / SVD）的差異只在於「$\mathbf{x}_p$ 和 $\mathbf{y}_p^*$ 各自滿足什麼結構」 — 但**形式統一**。SVD 是這個視角的「集大成終章」，因為 SVD 的 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 按 $\sigma_p$ 降冪排序，所以「**前幾項貢獻最大、後幾項可丟棄**」（Eckart–Young 最佳低秩近似定理）。

**對應章節：**
- §4 VizScript-02（[ch04 (MM4) 秩 1 累加 + Mona Lisa SVD demo](ch04-mat-mat.md#vizscript-02)）⭐⭐⭐ Tier 3：母模板
- §6 [五大分解總覽](ch06a-five.md) + §6.1–§6.5 [CR](ch06b-CR.md) / [LU](ch06c-LU.md) / [QR](ch06d-QR.md) / [EVD](ch06e-QLQ.md) / [SVD](ch06f-USV.md)
- §6.5 VizScript-01（[SVD 完整互動 + 4 應用切換](ch06f-USV.md#vizscript-01)）⭐⭐⭐ Tier 3：集大成

---

### 本書緣起（簡要歷史背景）

| 年份 | 事件 |
|---|---|
| 2020 | Gilbert Strang 出版《Linear Algebra for Everyone》（Wellesley Cambridge Press），強調以「圖解直覺」教線性代數，目標是「**讓所有人都能理解**」 |
| 2020 | Kenji Hiranabe 繪製《Matrix World》slidedeck — 用同心橢圓表示矩陣類別包含關係（見 [Matrix World 附錄](appendix-matrix-world.md)）|
| 2021 | Hiranabe 繪製《Map of Eigenvalues》slidedeck — 用複平面散點圖表示 12 種矩陣的特徵值分佈（見 [Map of Eigenvalues 附錄](appendix-map-eigenvalues.md)）|
| 2021 | Hiranabe 整合 50 張圖解 + 6 個 Pattern + 5 大分解，撰寫《The Art of Linear Algebra》論文 |
| 2022 | 簡體中文版翻譯出版（譯者 KFChLiu，[twitter @KFChLiu](https://twitter.com/KFChLiu)）|
| 2023 | Hiranabe v1.5 修訂版（含 Matrix World v1.5 同心橢圓地圖更新）|
| 2026 | **本互動式版本啟動**（S00–S11 規劃 + S12+ Python 實作，目標 ~25–28 session 完成）|

---

### 本互動式版本的範圍與目標（讀者導讀）

#### 範圍

- **覆蓋章節：** §1–§6（內容章節）+ 序言（本檔）+ 結論 + 3 個附錄（共 13 個 md 檔，總計 ~8000 行）
- **語言：** 繁體中文為主（術語第一次出現括號附英文）
- **平行素材：** 同步整合英文版（[from-tex/en.md](from-tex/en.md)）與簡中版（[from-tex/zh.md](from-tex/zh.md)）的差異
- **跳過：** 日文版（內容與英文版一致，只是翻譯）

#### 目標（三層）

1. **第一層（已完成 S02–S10）：** 把原書 50 張圖各寫一份四欄位描述（視覺結構 / 數學內容 / 直覺解讀 / VizMark）+ 23 個 VizScript 細緻劇本（每個 800 字 + 13 段 A-M 格式）
2. **第二層（S11，即將）：** 整合 + 校對 + 統一風格 + 生成 `BOOK.md` 合併版 + `VIZ-CATALOG.md` 視覺化候選池目錄
3. **第三層（S12+，預估 25–28 session）：** Python 視覺化技術棧決策（傾向 **Marimo + plotly 3D + matplotlib + scikit-learn**）+ 從 23 個 VizScript 挑題目開做 PoC，最終產出「**可互動的 The Art of Linear Algebra**」

#### 視覺化分級（Tier 系統）

每個 VizScript 標 1–3 顆星，顯示視覺化的複雜度與優先順序：

- ⭐⭐⭐ **Tier 3**（4 個）：核心骨架旗艦，預估 S12+ 各 3 session 實作 — 含 [ch04 (MM4) Mona Lisa SVD demo](ch04-mat-mat.md#vizscript-02)、[ch06f SVD 完整互動 + 4 應用](ch06f-USV.md#vizscript-01) 兩支主旗艦
- ⭐⭐⭐ **Tier 2**（多支）：主章核心互動，預估 S12+ 各 2 session
- ⭐⭐ **Tier 1**（多支）：輕量互動 / 數值範例 walkthrough，預估 S12+ 各 1.5 session
- ⭐ **Tier 1 輕量**（多支）：純動畫或單一概念示範，預估 S12+ 各 1 session

---

### 如何閱讀本書

#### 路線 A：純讀者（不寫程式）

1. 先讀 [§1 Viewing a Matrix](ch01-viewing-matrix.md) 建立術語直覺
2. 順序讀 §2 → §3 → §4 → §5 → §6 主章
3. 每章「**直覺解讀**」段是核心；「**VizScript**」段可略過
4. 讀 [Conclusion](back-conclusion.md) + [Map of Eigenvalues](appendix-map-eigenvalues.md) + [Matrix World](appendix-matrix-world.md) 收尾

#### 路線 B：互動體驗者（S12+ 完成後）

1. 從 [Matrix World 互動式索引地圖](appendix-matrix-world.md) 進入（旗艦 dashboard）
2. 點任何元素跳到對應章節 + VizScript
3. 每個 VizScript 都有「拉桿 + 即時視覺反饋」可調參體驗
4. 重點推薦旗艦：[ch06f SVD 完整互動 + Mona Lisa demo](ch06f-USV.md#vizscript-01)

#### 路線 C：開發者 / 視覺化工程師

1. 直接讀 [VIZ_SCHEMA.md](VIZ_SCHEMA.md) 了解 VizScript 13 段 A-M 格式
2. 從 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 開始（母模板，全書最詳盡）
3. 跳到 [ch06f VizScript-01](ch06f-USV.md#vizscript-01)（集大成終章）
4. S11 產出的 `VIZ-CATALOG.md` 將集中所有 23 個 VizScript 索引

---

### 章末延伸

- **後續章節連結：** [→ §1 Viewing a Matrix](ch01-viewing-matrix.md)
- **延伸閱讀：**
  - Gilbert Strang (2020), *Linear Algebra for Everyone*, Wellesley Cambridge Press. <http://math.mit.edu/everyone>
  - Gilbert Strang (2016), *Introduction to Linear Algebra*, 5th ed., Wellesley Cambridge Press. <http://math.mit.edu/linearalgebra>
  - 詳細參考文獻見 [Conclusion + References](back-conclusion.md)

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 1–14 / `The-Art-of-Linear-Algebra.pdf` p.1
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 1–11
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **序言作者：** Gilbert Strang（MIT 數學系教授）
- **原 repo：** <https://github.com/junoback/The-Art-of-Linear-Algebra>
- **授權：** Apache 2.0

---

## 第 1 章. 矩陣的四種視角（Viewing a Matrix — 4 Ways）

> **原書頁碼：** p.2
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 15–47 行
> **本章圖數：** 1
> **本章 VizMark 數：** 2（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 0）
> **狀態：** [x] 已完成 / [ ] 校對中

---

### 章節摘要

一個 $m \times n$ 的矩陣 (matrix) 可以同時被當成**四種等價的物件**來看：

1. **整體一塊 (1 matrix)** — 一個運算子或一塊資料。
2. **$mn$ 個數字 (mn numbers)** — 二維表格中的個別元素 $a_{ij}$。
3. **$n$ 個列向量 (n column vectors)** — 把矩陣切成 $n$ 個直立的列 (column)，每列是 $\mathbb{R}^m$ 中的向量。
4. **$m$ 個行向量 (m row vectors)** — 把矩陣切成 $m$ 個橫躺的行 (row)，每行是 $\mathbb{R}^n$ 中的向量。

這四種視角描述的是**同一個數學物件**，但每一種「切法」對應到不同的線代直覺：整體視角對應線性變換的「黑盒子」、數字視角對應元素層級的運算（如點積 (dot product)）、列向量視角對應列空間 (column space) 與線性組合 (linear combination)、行向量視角對應行空間 (row space) 與「行方向」的看法。

本章是全書的「視角字典」：後面所有矩陣運算（vector × vector、matrix × vector、matrix × matrix、五種矩陣分解）都會反覆切換這四種視角來解釋同一個算式。能流暢切換視角，是讀懂這本書的入場票。

> ⚠ **中英術語慣例（全書通用）：** 本書採華文主流慣用 — **column = 列（直立）、row = 行（橫躺）**。若你過往讀台灣本土數學教科書習慣「column = 行、row = 列」（方向相反），此處請花一兩分鐘重新校準。本專案 `from-tex/zh.md` 為簡中譯本，用詞方向與本繁中版**一致**。

---

### 數學要點

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

### 圖片區

#### Figure 1.1: 矩陣的四種視角（Viewing a Matrix in 4 Ways）

**圖檔：** `docs/book/figs-png/ViewingMatrix-4Ways.png`（原始 EPS：`figs/ViewingMatrix-4Ways.eps`）
**原書頁碼：** p.2
**所屬章節：** §1

##### 視覺結構 (Visual Structure)

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

##### 數學內容 (Mathematical Content)

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

##### 直覺解讀 (Intuition)

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

##### 視覺化機會（VizMark 引用）

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

### 視覺化劇本（VizScripts）

> 本章兩個 VizMark 對應兩個 VizScript。格式遵 `VIZ_SCHEMA.md` §2（A–M 共 13 段）。
> 兩個劇本實作時可合成單一視覺化頁面（共用控制列、共用畫布），不必拆兩支獨立程式。

#### VizScript-01: 矩陣的四種觀看視角（4 Ways Toggle）

##### A. 一句話定位
讓使用者切換 4 種視角，看同一矩陣呈現出 4 種等價但風格迥異的「身分」。

##### B. 學習目標（Learning Outcome）
- 使用者能說出矩陣的 4 種觀看方式名稱（whole / numbers / columns / rows）
- 使用者能在切換時指出哪個元素 $a_{ij}$ 對映到哪個列向量 $\mathbf{a}_j$、哪個行向量 $\mathbf{a}_i^*$
- 使用者能說明「為什麼這 4 種視角描述的是同一個矩陣」
- 使用者能在腦中預測：若改 $a_{12}$，4 個視角中哪些區塊會變色 / 變數字
- 使用者能正確指認本書慣例「column = 列（直立）、row = 行（橫躺）」

##### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$
- **預設值：** $A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$（m=3, n=2，與原書圖 1.1 一致）
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$（由 VizMark-02 / VizScript-02 控制）
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1
- **退化情形：** rank-deficient（如某列為他列倍數）時，columns 視角中相依的列畫虛線外框並 tooltip 警示

##### D. 視覺布局（Visual Layout）
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

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 | radio (4) | whole / numbers / columns / rows | whole | 即時（400ms 過渡動畫） |
| m | slider | [2, 6] step 1 | 3 | 即時 |
| n | slider | [2, 6] step 1 | 2 | 即時 |
| $a_{ij}$ | numeric input grid $m \times n$ | [-9, 9] step 1 | 預設矩陣 | onBlur |
| 重設 | button | — | — | click → 還原預設 A |

##### F. 輸出畫面細節（Outputs）
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

##### G. 互動行為（Interactions）
- **hover cell：** 該 cell 加粗外框 + tooltip 顯示 `A[i+1][j+1] = value`（1-indexed 對齊原書）
- **click cell：** 該 cell 持續高亮 + 在公式區用相同色標記該 cell 所屬的列 $\mathbf{a}_j$ 與行 $\mathbf{a}_i^*$
- **click 列向量區（columns 視角時）：** 整列持續高亮 + 右側顯示該列作為 $\mathbb{R}^m$ 向量的座標列表
- **click 行向量區（rows 視角時）：** 整行持續高亮 + 右側顯示該行作為 $\mathbb{R}^n$ 向量的座標列表
- **快捷鍵：** 數字鍵 `1`/`2`/`3`/`4` 切換 whole/numbers/columns/rows；箭頭鍵移動 cell focus；`Esc` 取消選取
- **拖曳：** 不支援（避免與 numeric input 衝突）

##### H. 動畫腳本（視角切換）
- **t=0：** 當前視角穩態。
- **t=0–150ms：** 當前視角的特徵元素淡出（如 columns 視角的綠色色塊 opacity 0.4 → 0）。
- **t=150–400ms：** 新視角的特徵元素淡入 + 從中心向外展開（scale 0.85 → 1.0、opacity 0 → 目標 alpha）。
- **t=400ms 後：** 新視角穩態，cell 文字保持不變。
- **總長度：** 400ms
- **緩動函數：** ease-in-out（CSS `cubic-bezier(0.4, 0, 0.2, 1)` 等價）
- **可暫停 / 倒轉：** 否（< 500ms 短動畫無此需求）。

##### I. 邊界與錯誤處理
- **m=n=2 最小矩陣：** cell 尺寸增至 80×80 避免畫面空蕩。
- **m=6, n=6 最大：** cell 縮至 40×40、字級降為 12pt、動畫禁用避免頓挫。
- **使用者輸入非整數：** 紅框警示 0.5 秒後還原前一值，並在底部 status bar 顯示「請輸入 -9 到 9 的整數」。
- **rank-deficient（如 $\mathbf{a}_1 = 2 \mathbf{a}_2$）：** columns 視角中相依的列畫虛線外框 + tooltip「此列與其他列線性相依」；公式區 rank 數值用紅字顯示。
- **全零矩陣：** rank=0，所有視角正常顯示但加底部提示「零矩陣 — 所有列 / 行向量皆為零」。

##### J. 教學支援（Teaching Aids）
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

##### K. 技術實作建議（Tech Stack Hints）
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

##### L. 驗收標準（Acceptance Criteria）
- [ ] 4 個視角可切換，視覺呈現符合 §D / §F 規範
- [ ] $m, n$ slider 在 [2, 6] 範圍內拉動，cell 永不重疊、永不出框
- [ ] 任意 $a_{ij}$ 編輯後 < 100ms 重算並重畫完成
- [ ] 視角切換動畫總長 ≤ 400ms，60fps 無 frame drop
- [ ] rank-deficient 時 columns 視角虛線標示正確、rank 數值正確
- [ ] Walkthrough 5 步驟首次開啟自動觸發，可關閉並記住偏好
- [ ] 鍵盤 `1`/`2`/`3`/`4` 切換視角生效

##### M. 互動深度 Tier + 估時
- **Tier 1（基礎，0.5–1 session）：** 4 視角靜態切換 + $m, n$ slider，無動畫、無 cell 編輯。
- **Tier 2（增強，1–2 session）：** + cell 編輯 + tooltip + 視角切換動畫 + walkthrough。
- **Tier 3（完整，2–3 session）：** + 拖曳列向量端點改值（2D 幾何 drag）+ 多矩陣對比（split view）+ 匯出 PNG。
- **本劇本目標 Tier：** Tier 2
- **估時：** 1.5 session（含 snapshot 測試與 walkthrough）

---

#### VizScript-02: 矩陣維度的同步重組（Dimensions Synchronizer）

##### A. 一句話定位
拉動 $m, n$ slider 看「同一個 $A$ 在 4 個視角下，cell 數與向量數如何同步改變」。

##### B. 學習目標（Learning Outcome）
- 使用者能說明：列向量數 = $n$、行向量數 = $m$（不是反過來）
- 使用者能說明：列向量住在 $\mathbb{R}^m$、行向量住在 $\mathbb{R}^n$
- 使用者能在腦中預測：把 $n$ 從 2 拉到 5，columns 視角會多 3 條綠直條
- 使用者能在腦中預測：把 $m$ 從 3 拉到 5，每個列向量會「變長」（從 3 維變 5 維）

##### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$（與 VizScript-01 共用同一個 $A$）
- **預設值：** 與 VizScript-01 同（$m=3, n=2$，預設值 1-6）
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$，共 25 種組合
- **數值範圍：** 維度改變時，新增 cell 預設值用「順序遞增」填充（既有 cell 保留原值）。例如 $3 \times 2 \to 3 \times 3$，新增第 3 列填 `7, 8, 9`。
- **退化情形：** $m = n$（方陣）時，UI 不做特殊處理但底部 status bar 提示「方陣」。

##### D. 視覺布局（Visual Layout）
- **共用 VizScript-01 的整體布局**，新增以下元素：
  - 主畫面左上角：當前維度 badge `m × n` 大字（24pt sans bold，顏色 `#666`），slider 拖動時即時更新。
  - 主畫面右上角：對比框 — 始終並列顯示「上排抽象示意（4 個小圖示）」尺寸固定，不隨 $m, n$ 縮放，作為「速查圖鑑」。
  - 底部 slider 區：$m$ slider 與 $n$ slider 各佔 50% 寬，標籤「行數 m / rows」「列數 n / columns」。
- **動畫過渡時的補位策略：** 維度增加時，新 cell 從外往內滑入（位移動畫 200ms）；維度減少時，被切除的 cell 淡出 + 折疊（200ms）。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 | 預設 | 觸發 |
|---|---|---|---|---|
| m | slider | [2, 6] step 1 | 3 | 即時（200ms 動畫） |
| n | slider | [2, 6] step 1 | 2 | 即時（200ms 動畫） |
| 「同步換預設值」checkbox | toggle | on / off | off | 即時 |

- **「同步換預設值」on：** 維度變時整個 $A$ 用 1..mn 重填（如 $m=4, n=3$ 自動填 1-12）。
- **「同步換預設值」off（預設）：** 維度增加時新 cell 補 0；維度減少時被切的值保留在記憶體（再拉大時還原）。

##### F. 輸出畫面細節（Outputs）
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

##### G. 互動行為（Interactions）
- **slider 即時拖動：** 不只是 onChange 觸發，連 onInput 也觸發，達到「拉到一半就看到中間態」的即時感（但動畫節流到 60fps）。
- **slider 連按方向鍵：** 每按一次 step 1，伴隨 200ms 動畫；連按時動畫排隊但不疊加。
- **hover slider 數值：** tooltip 顯示「m=4 → 4 個行向量，每個住在 $\mathbb{R}^n$」之類即時提示。

##### H. 動畫腳本（維度變化）
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

##### I. 邊界與錯誤處理
- **m=2, n=2 最小：** slider 仍可下降到此，再低則 slider 鎖在 2，cursor 變 not-allowed。
- **m=6, n=6 最大：** cell 縮至 40×40、字級 12pt，動畫期間禁用 hover effect 避免閃爍。
- **同步換預設值勾選時 $a_{ij}$ 編輯：** 編輯時自動取消勾選並 status bar 提示「已切換到手動模式」。
- **rank 重算失敗（極罕見）：** 顯示 `rank = ?` 並 console.warn，不阻斷 UI。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - m slider：「m = 行數 = rows，影響列向量長度（每列是 $\mathbb{R}^m$）」
  - n slider：「n = 列數 = columns，影響行向量長度（每行是 $\mathbb{R}^n$）」
- **Walkthrough（與 VizScript-01 共用，補加 2 步）：**
  6. 「現在拉 m slider，注意列向量怎麼變長（綠直條變高）」
  7. 「拉 n slider，注意行向量怎麼變長（粉橫條變寬）」
- **常見誤解警示框：** 「初學者常混淆：『列向量有 n 個』而不是 m 個 — 因為每個直立的列是『一條 down to m 元素』，列向量數量等於『有幾條這樣的直列』，也就是 n。」
- **互動小測驗（選用）：** 「猜猜：當 $m=4, n=3$ 時，rows 視角有幾條橫條？」（答：4）

##### K. 技術實作建議（Tech Stack Hints）
- **與 VizScript-01 共享同一支 Python 主檔，** 不要拆兩支。
- **狀態管理：** 用 marimo 的 reactive cell 或 Streamlit 的 `st.session_state` 持存「使用者輸入過的歷史 $a_{ij}$」（供拉小再拉大時還原）。
- **動畫實作：**
  - matplotlib：用 `FuncAnimation` + blit 提升效能。
  - 替代：plotly `frame` 動畫（如選 Streamlit + Plotly 路線）。
- **效能：** 每次維度變化呼叫 `ax.clear()` 後重建 patches，不要在 patches list 上 incremental add/remove（容易脫鉤）。

##### L. 驗收標準（Acceptance Criteria）
- [ ] $m, n$ 改變時 4 個視角同步重畫，無 ghost cell 殘留
- [ ] 「同步換預設值」勾選 / 取消行為正確
- [ ] 維度增加時新 cell 預設值符合規格（補 0 或 1..mn）
- [ ] 維度減少再增加時，原值能還原（off 模式下）
- [ ] 動畫期間 hover 不觸發 tooltip（避免閃爍）
- [ ] 維度 badge `m × n` 與 `rank` 即時更新延遲 < 50ms

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1：** 維度改變即時重畫無動畫
- **Tier 3 擴充：** + 滑動到極端值時的「教學旁白」配音 / 字幕
- **估時：** 0.5 session（與 VizScript-01 同檔開發，主要工作是 slider 連動 + 動畫節流）

---

### 章末延伸

- **下一章：** [→ ch02-vec-vec.md](ch02-vec-vec.md) — Vector × Vector 的 2 種視角（v1 點積 / v2 外積）
- **延伸閱讀：** Gilbert Strang《Linear Algebra for Everyone》§1.1（線性組合與點積）、§1.3（秩 1 矩陣）、§1.4（行方式與列方式 row way & column way）
- **本章在「五大分解」中的位置：** 全書的「字典頁」 — 後面 §6 五大分解的圖示都會用本章建立的 4 視角 + 配色約定。

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 15–47 / `The-Art-of-Linear-Algebra.pdf` p.2
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` 對應段落（用詞方向與本繁中版一致，皆採華文主流 A 派）
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0

---

## 第 2 章. 向量乘以向量 — 兩種視角（Vector × Vector — 2 Ways）

> **原書頁碼：** p.2
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 49–67 行
> **本章圖數：** 1
> **本章 VizMark 數：** 2（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 0）
> **狀態：** [x] 已完成 / [ ] 校對中

---

### 章節摘要

兩個向量相乘，依方向不同會產出兩種**完全不同尺寸**的結果。**(v1) 點積 (dot product)** 是「行向量 × 列向量 = 一個數字」，把兩個向量的對應分量乘起來再加總，結果是純量。**(v2) 外積 (outer product)** 是「列向量 × 行向量 = 一個矩陣」，產出的不是數字而是一整個**秩 1 矩陣 (rank 1 matrix)**，這個矩陣的每一列都是 $\mathbf{a}$ 的倍數，每一行都是 $\mathbf{b}^{\mathrm{T}}$ 的倍數。

(v1) 是讀者早就熟悉的初等運算；(v2) 才是本書的關鍵 — 它是 §6 五大矩陣分解（CR / LU / QR / $Q\Lambda Q^{\mathrm{T}}$ / $U\Sigma V^{\mathrm{T}}$）的共同骨架，因為任何矩陣都可以寫成若干個秩 1 矩陣（外積）之和。本章只看 1 張圖，但這張圖建立的「**外積 = 秩 1 矩陣**」直覺，會在後續每一章都用到。

> ⚠ **術語提醒（沿用 §1 全書慣例）：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。本章兩個視角的「方向」是核心 — **(v1)** 是「橫躺 × 直立」（夾住中間像三明治）、**(v2)** 是「直立 × 橫躺」（外撐開像漢堡）。記住這個對比，後面所有矩陣乘法視角都能秒判斷產物是純量還是矩陣。

---

### 數學要點

兩個向量 $\mathbf{a} \in \mathbb{R}^m$、$\mathbf{b} \in \mathbb{R}^m$（或 $\mathbf{b} \in \mathbb{R}^n$，視運算而定），有兩種「相乘」方式：

#### (v1) 點積 / 內積（Dot Product / Inner Product）

$$
\mathbf{a} \cdot \mathbf{b}
\;=\;
\mathbf{a}^{\mathrm{T}} \mathbf{b}
\;=\;
\begin{bmatrix} a_1 & a_2 & \cdots & a_m \end{bmatrix}
\begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix}
\;=\;
\sum_{k=1}^{m} a_k b_k
\;\in\; \mathbb{R}
$$

- **維度約束：** $\mathbf{a}$ 與 $\mathbf{b}$ 必須在同一個 $\mathbb{R}^m$。
- **形狀運算：** $(1 \times m)(m \times 1) = (1 \times 1)$，結果是純量。
- **原書 (v1) 範例：**

$$
\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
= x_1 + 2x_2 + 3x_3
$$

#### (v2) 外積（Outer Product）→ 秩 1 矩陣

$$
\mathbf{a} \mathbf{b}^{\mathrm{T}}
\;=\;
\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_m \end{bmatrix}
\begin{bmatrix} b_1 & b_2 & \cdots & b_n \end{bmatrix}
\;=\;
\begin{bmatrix}
a_1 b_1 & a_1 b_2 & \cdots & a_1 b_n \\
a_2 b_1 & a_2 b_2 & \cdots & a_2 b_n \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_m b_1 & a_m b_2 & \cdots & a_m b_n
\end{bmatrix}
\;\in\; \mathbb{R}^{m \times n}
$$

- **維度約束：** $\mathbf{a}$ 與 $\mathbf{b}$ 可以住在**不同維度**的空間（$\mathbf{a} \in \mathbb{R}^m$、$\mathbf{b} \in \mathbb{R}^n$）。
- **形狀運算：** $(m \times 1)(1 \times n) = (m \times n)$，結果是矩陣。
- **秩：** 只要 $\mathbf{a} \ne \mathbf{0}$ 且 $\mathbf{b} \ne \mathbf{0}$，$\operatorname{rank}(\mathbf{a}\mathbf{b}^{\mathrm{T}}) = 1$。
- **結構觀察：** 矩陣的第 $j$ 直立列等於 $b_j \mathbf{a}$（$\mathbf{a}$ 的純量倍數）；第 $i$ 橫躺行等於 $a_i \mathbf{b}^{\mathrm{T}}$（$\mathbf{b}^{\mathrm{T}}$ 的純量倍數）。**所有列彼此平行、所有行彼此平行** — 這就是秩 1 的視覺意涵。
- **原書 (v2) 範例：**

$$
\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
\begin{bmatrix} x & y \end{bmatrix}
=
\begin{bmatrix}
x & y \\
2x & 2y \\
3x & 3y
\end{bmatrix}
$$

#### 對偶關係（v1 ↔ v2）

把同樣的兩個直立向量 $\mathbf{a}, \mathbf{b} \in \mathbb{R}^m$，**夾住中間（v1）** vs **撐到外面（v2）**，就決定產物是純量還是矩陣：

$$
\underbrace{\mathbf{a}^{\mathrm{T}} \mathbf{b}}_{\text{純量}\; \in \mathbb{R}}
\quad\text{vs}\quad
\underbrace{\mathbf{a}\, \mathbf{b}^{\mathrm{T}}}_{\text{矩陣}\; \in \mathbb{R}^{m \times m}}
$$

這個「夾 / 撐」對比是本章視覺化最值得做動畫的點（見 VizMark-02）。

#### 對應原書章節（Strang《Linear Algebra for Everyone》）

- Sec. 1.1 (p.2) Linear combination and dot products — 對應 (v1)
- Sec. 1.3 (p.25) Matrix of Rank One — 對應 (v2)
- Sec. 1.4 (p.29) Row way and column way — (v1) 與 (v2) 的對偶引子

---

### 圖片區

#### Figure 2.1: 向量乘以向量的兩種視角（Vector × Vector — (v1), (v2)）

**圖檔：** `docs/book/figs-png/VectorTimesVector.png`（原始 EPS：`figs/VectorTimesVector.eps`）
**原書頁碼：** p.2
**所屬章節：** §2

##### 視覺結構 (Visual Structure)

此圖採「左右並列兩區」結構，左半 (v1) 點積、右半 (v2) 外積，各區由「**抽象色塊示意（上）+ 具體數字範例（下）**」兩層組成。

- **左半：(v1) 點積**
  - 左上角小灰圈內標 `v1`，標示此區編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **粉紅色橫條** —— 行向量（row vector，橫躺）。
    2. **綠色直條** —— 列向量（column vector，直立）。
    3. **粉紅與綠重疊成的小方塊** —— 表示對應分量相乘逐項堆疊。
    4. **單一藍色實心圓點** —— 一個純量（數字）。
    5. 右側標註文字：`Dot product (number)`。
  - 抽象示意下方文字：**"Dot product (a·b) is expressed as $\mathbf{a}^{\mathrm{T}}\mathbf{b}$ in matrix language and yields a number."**
  - 具體範例（最下方）：
    $$\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = x_1 + 2x_2 + 3x_3$$
- **右半：(v2) 外積 → 秩 1 矩陣**
  - 左上角小灰圈內標 `v2`，標示此區編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **綠色直條** —— 列向量（column vector，直立）。
    2. **粉紅色橫條** —— 行向量（row vector，橫躺）。
    3. **完整方塊**：上緣一條粉紅橫條（標記第一橫躺行的來源）、左緣一條綠直條（標記第一直立列的來源）、其餘以淺灰填滿（表示矩陣其他元素都由兩者乘積決定）。
    4. **6 個藍色實心圓點**排成 $3 \times 2$ 網格 —— 表示產出的秩 1 矩陣有 6 個元素，但只有 1 個自由度。
    5. 右側標註文字：`Rank 1 Matrix`。
  - 抽象示意下方文字：**"$\mathbf{a}\mathbf{b}^{\mathrm{T}}$ is a matrix ($\mathbf{a}\mathbf{b}^{\mathrm{T}} = A$). If neither $a, b$ are 0, the result $A$ is a rank 1 matrix."**
  - 具體範例（最下方）：
    $$\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\begin{bmatrix} x & y \end{bmatrix} = \begin{bmatrix} x & y \\ 2x & 2y \\ 3x & 3y \end{bmatrix}$$
- **配色語意（沿用 §1）：** 綠 = 列向量 / 直立、粉紅 = 行向量 / 橫躺、藍點 = 個別數字、灰 = 結構填充。
- **左右兩區的形狀對比：** (v1) 結果端只有一個藍點（純量），(v2) 結果端是 $3 \times 2$ 共 6 個藍點的矩形（矩陣）。這個「端點圖形的大小差」是讀者要一眼讀懂的核心訊息。

讀者的視覺動線：先看左半 (v1) 確認「點積 = 一個數」這個熟悉概念 → 跳到右半 (v2) 注意端點從「一個點」變成「一塊矩陣」 → 對比兩個抽象示意的開頭：(v1) 是「粉紅 × 綠」、(v2) 是「綠 × 粉紅」順序顛倒 → 連結到下方具體範例驗證。

##### 數學內容 (Mathematical Content)

圖中演示的兩個運算：

**(v1) 點積：**

$$
\mathbf{a}^{\mathrm{T}} \mathbf{b}
= \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
= x_1 + 2x_2 + 3x_3 \in \mathbb{R}
$$

其中：

$$
\mathbf{a} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix},\;
\mathbf{b} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \in \mathbb{R}^3
$$

**(v2) 外積：**

$$
\mathbf{a}\, \mathbf{b}^{\mathrm{T}}
= \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \begin{bmatrix} x & y \end{bmatrix}
= \begin{bmatrix} x & y \\ 2x & 2y \\ 3x & 3y \end{bmatrix} \in \mathbb{R}^{3 \times 2}
$$

其中：

$$
\mathbf{a} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \in \mathbb{R}^3,\;
\mathbf{b} = \begin{bmatrix} x \\ y \end{bmatrix} \in \mathbb{R}^2
\;\Rightarrow\;
\mathbf{b}^{\mathrm{T}} = \begin{bmatrix} x & y \end{bmatrix}
$$

**秩驗證：** $\det\begin{bmatrix} x & y \\ 2x & 2y \end{bmatrix} = 2xy - 2xy = 0$；任兩個直立列 $(x, 2x, 3x)^{\mathrm{T}}$ 與 $(y, 2y, 3y)^{\mathrm{T}}$ 皆為 $\mathbf{a} = (1,2,3)^{\mathrm{T}}$ 的純量倍數 $x \cdot \mathbf{a}$、$y \cdot \mathbf{a}$，所以**列空間 (column space) 只有 1 維**，$\operatorname{rank} = 1$。

**維度檢核（最常出錯處）：**
- (v1) 內外都是 $\mathbb{R}^3$，能夠相乘是因為 $(1 \times 3)(3 \times 1) = (1 \times 1)$ 的中間維度 3 對得起來。
- (v2) $\mathbf{a} \in \mathbb{R}^3$、$\mathbf{b} \in \mathbb{R}^2$，**兩個向量本來不在同一空間也沒關係** — 外積要的是「外面」的維度 $m=3$ 與 $n=2$ 各自當行 / 列數，「中間」的維度恆為 1。

##### 直覺解讀 (Intuition)

**1. 「方向」決定結果是純量還是矩陣。** 同樣兩個直立列向量 $\mathbf{a}, \mathbf{b} \in \mathbb{R}^m$，把哪一個轉置（變橫躺）會徹底改變結果尺寸：
- 第一個轉置成橫躺（$\mathbf{a}^{\mathrm{T}} \mathbf{b}$）→ 「橫躺夾住直立」→ 結果壓縮成 1 個數字。
- 第二個轉置成橫躺（$\mathbf{a} \mathbf{b}^{\mathrm{T}}$）→ 「直立撐開橫躺」→ 結果擴張成 $m \times m$ 矩陣。

可以記成「**夾 (clamp) → 純量**、**撐 (extend) → 矩陣**」。

**2. 秩 1 矩陣的「平行性」結構。** $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 的每一直立列都是 $\mathbf{a}$ 的純量倍數（係數來自 $\mathbf{b}$）、每一橫躺行都是 $\mathbf{b}^{\mathrm{T}}$ 的純量倍數（係數來自 $\mathbf{a}$）。這意味著：
- **列空間 (column space) 是一條過原點的直線**：$\operatorname{span}\{\mathbf{a}\} \subset \mathbb{R}^m$。
- **行空間 (row space) 也是一條過原點的直線**：$\operatorname{span}\{\mathbf{b}\} \subset \mathbb{R}^n$。
- 這就是「rank 1」的幾何畫面 — 不是兩條獨立方向，而是「一條方向（$\mathbf{a}$）被縮放後在不同位置複製」的結構。

**3. 為何 (v2) 是後續章節的鑰匙。** 全書 §6 的五大矩陣分解，看似分別在做不同的事，但本質都是把矩陣寫成**若干個秩 1 矩陣的和**：

$$
A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}} + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}} + \cdots + \sigma_r \mathbf{u}_r \mathbf{v}_r^{\mathrm{T}}
\quad\text{(SVD 的最終形式)}
$$

QR、LU、$Q\Lambda Q^{\mathrm{T}}$ 也都能寫成類似的「秩 1 矩陣加總」形式。若 (v2) 沒讀通，後續章節會覺得每個分解都是「魔術公式」；讀通後，會看出它們都是同一個外積框架的變奏。

**4. 點積與內積的詞彙混用。** 在 $\mathbb{R}^m$ 上、實數係數時，"dot product" 與 "inner product" 指同一件事（$\sum a_k b_k$）。在更廣義的內積空間裡兩者才有區別（內積會加共軛或加權），但本書全程在 $\mathbb{R}^m$ 上，可視為同義詞。

**常見誤解警示：**
- **$\mathbf{a}^{\mathrm{T}}\mathbf{b}$ 與 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 不可互換** — 前者是 $1 \times 1$ 純量，後者是 $m \times n$ 矩陣，差異不只是寫法。
- **「外積」一詞在不同教材有不同意思** — 本書（與 Strang）指的是 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$（產生矩陣）；某些物理 / 幾何脈絡用「外積」指 cross product $\mathbf{a} \times \mathbf{b}$（產生向量，限 $\mathbb{R}^3$）。本書內 outer product 一律指**矩陣產出**。
- **秩 1 矩陣不一定每個元素都非零** — 若 $\mathbf{a}$ 或 $\mathbf{b}$ 有某個分量為 0，對應的整列 / 整行就是 0，但只要兩向量都非零向量，整個矩陣的秩仍是 1（不會是 0）。

**為什麼這張圖該做成互動視覺化？** 因為「夾 vs 撐」、「拉某個分量導致整列 / 整行同步縮放」這類概念是動態的 — 讀者拉動 $\mathbf{a}, \mathbf{b}$ 的分量值，看著秩 1 矩陣的所有列同步等比例變化，會直接「看到」rank 1 的視覺意涵；這是靜態圖永遠做不到的事（見 VizMark-01）。另外 (v1) ↔ (v2) 的視角切換動畫，能把「同樣兩個向量、轉置誰決定產物尺寸」這個對偶結構在 1 秒內演完（見 VizMark-02）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [拉桿調參] ⭐⭐⭐
> **位置：** Figure 2.1 / §2 / (v2) 外積區
> **核心概念：** 外積 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 產生秩 1 矩陣，**每列彼此平行、每行彼此平行**
> **互動梗概：** 拉 $\mathbf{a}, \mathbf{b}$ 各分量 slider，矩陣 6 格即時重算 + 高亮顯示「此列是 $\mathbf{a}$ 的幾倍」「此行是 $\mathbf{b}^{\mathrm{T}}$ 的幾倍」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [切換視角] ⭐⭐
> **位置：** Figure 2.1 / §2 / (v1) ↔ (v2) 對偶
> **核心概念：** 同樣兩個直立向量，轉置誰決定產物是純量 (v1) 還是秩 1 矩陣 (v2)
> **互動梗概：** toggle 切換 (v1) / (v2)，畫面演動畫「橫躺向量在左 vs 在右」的位移與結果端點的大小變化
> **詳見劇本：** VizScript-02（章末）

---

### 視覺化劇本（VizScripts）

> 本章兩個 VizMark 對應兩個 VizScript。格式遵 `VIZ_SCHEMA.md` §2（A–M 共 13 段）。
> 兩個劇本實作時可合成單一視覺化頁面（共用控制列、共用畫布），不必拆兩支獨立程式。

#### VizScript-01: 外積與秩 1 矩陣（Outer Product → Rank 1 Visualizer）

##### A. 一句話定位
讓使用者拉動兩個向量的分量，即時看「列向量 × 行向量 = 秩 1 矩陣」的所有元素同步等比例變化。

##### B. 學習目標（Learning Outcome）
- 使用者能說出「外積產出 $m \times n$ 矩陣，秩永遠是 1」（除非有零向量）。
- 使用者能在腦中預測：若把 $\mathbf{a}$ 的第 2 分量乘以 2，矩陣的哪些 cell 會變、變成多少。
- 使用者能指認「每直立列都是 $\mathbf{a}$ 的純量倍數」、「每橫躺行都是 $\mathbf{b}^{\mathrm{T}}$ 的純量倍數」這兩種平行結構。
- 使用者能透過視覺驗證「列空間是 $\operatorname{span}\{\mathbf{a}\}$ 一維直線」這個敘述。
- 使用者能理解「為何 $\mathbf{a}$ 或 $\mathbf{b}$ 任一為零時 rank 變 0、否則恆為 1」。

##### C. 待視覺化的數學物件
- **物件清單：** 列向量 $\mathbf{a} \in \mathbb{R}^m$、行向量 $\mathbf{b}^{\mathrm{T}} \in \mathbb{R}^{1 \times n}$（內部以列向量 $\mathbf{b} \in \mathbb{R}^n$ 儲存）、外積矩陣 $A = \mathbf{a}\mathbf{b}^{\mathrm{T}} \in \mathbb{R}^{m \times n}$。
- **預設值：** $\mathbf{a} = (1, 2, 3)^{\mathrm{T}}$、$\mathbf{b} = (x, y)^{\mathrm{T}} = (1, 1)^{\mathrm{T}}$（與原書一致；$x = y = 1$ 起始讓 cell 初值就是 $\mathbf{a}$ 的整數倍，易觀察）。
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$。
- **數值範圍：** $a_i, b_j \in [-9, 9]$ 步進 1（與 §1 一致）。
- **退化情形：**
  - **任一向量全零** → 矩陣全零、$\operatorname{rank} = 0$；右側資訊框紅字警示「rank = 0（至少一向量為零）」。
  - **某分量為 0** → 對應整列 / 整行為 0，但 rank 仍 = 1；該整列 / 整行以淺灰底標示。
  - **$\mathbf{a} = \mathbf{b}$ 且 $m = n$** → $A = \mathbf{a}\mathbf{a}^{\mathrm{T}}$ 是對稱秩 1 矩陣；額外顯示 "symmetric rank 1" 標籤。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 左 30% 向量輸入區（兩個向量 slider + 數值顯示）、中 45% 主畫面外積矩陣、右 25% 資訊區（公式 + rank + 平行性檢視）。
- **主畫面尺寸：** 600×480 px，白底；cell 60×60 px 視 $m, n$ 自動縮放。
- **向量輸入區布局：**
  - 上半：**列向量 $\mathbf{a}$**（綠色直條，$m$ 個 slider 縱向排列，每個 slider 旁顯示當前值）。
  - 下半：**行向量 $\mathbf{b}^{\mathrm{T}}$**（粉紅色橫條，$n$ 個 slider 橫向排列，每個 slider 上方顯示當前值）。
  - 視覺位置呼應外積式：$\mathbf{a}$ 在左（外積結果矩陣的左側）、$\mathbf{b}^{\mathrm{T}}$ 在上（結果矩陣的上方）。
- **主畫面內容：** $m \times n$ 矩陣 cell 網格，每 cell 顯示計算結果 $a_i \cdot b_j$；左側 cell 邊緣對齊 $\mathbf{a}$ slider、上側 cell 邊緣對齊 $\mathbf{b}^{\mathrm{T}}$ slider。
- **資訊區內容：** 公式 $A = \mathbf{a}\mathbf{b}^{\mathrm{T}}$ 即時用當前值渲染（MathJax）、`rank(A) = 1`（紅色字當為 0、綠色字當為 1）、「平行性檢視」radio（off / 顯示列平行 / 顯示行平行）。
- **配色（hex）：**
  - $\mathbf{a}$ 區域與「列平行」高亮：`#2ca02c`（綠，alpha 0.4 底）
  - $\mathbf{b}^{\mathrm{T}}$ 區域與「行平行」高亮：`#d62728`（粉紅，alpha 0.4 底；實際偏紅但呼應 §1）
  - 矩陣 cell 文字：`#000000` 16pt monospace
  - 零分量導致的整列 / 整行：淡灰底 `#eeeeee`
  - rank = 0 警示：紅字 `#cc0000`、rank = 1 正常：綠字 `#1a8a1a`
- **字型 / 字級：** 公式區 16pt MathJax；矩陣 cell 16pt monospace；slider 標籤 12pt sans。
- **邊距：** 上下左右各 20px、cell 間距 4px、輸入區與主畫面間距 24px。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| $m$ | slider | [2, 6] step 1 | 3 | 即時 |
| $n$ | slider | [2, 6] step 1 | 2 | 即時 |
| $a_i$ ($i=1\ldots m$) | slider 縱排 | [-9, 9] step 1 | $(1,2,3,\ldots)$ | 即時 |
| $b_j$ ($j=1\ldots n$) | slider 橫排 | [-9, 9] step 1 | $(1, 1, \ldots)$ | 即時 |
| 平行性檢視 | radio (3) | off / 列平行 / 行平行 | off | 即時 |
| 重設 | button | — | — | click → 還原預設 |

##### F. 輸出畫面細節（Outputs）
- **每 cell 即時顯示：** $a_i \cdot b_j$ 的乘積（整數運算，無浮點誤差）。
- **「列平行」模式：** 每一直立列被綠色色塊覆蓋，並在列底顯示 `= $b_j$ × $\mathbf{a}$`；hover 某列時其他列半透明 0.3 凸顯。
- **「行平行」模式：** 每一橫躺行被粉紅色色塊覆蓋，並在行右顯示 `= $a_i$ × $\mathbf{b}^{\mathrm{T}}$`；hover 某行時其他行半透明 0.3。
- **公式區即時更新：**
  $$A = \begin{bmatrix} a_1 \\ \vdots \\ a_m \end{bmatrix} \begin{bmatrix} b_1 & \cdots & b_n \end{bmatrix} = \begin{bmatrix} a_1 b_1 & \cdots & a_1 b_n \\ \vdots & \ddots & \vdots \\ a_m b_1 & \cdots & a_m b_n \end{bmatrix}$$
  以實際數字渲染。
- **rank 顯示：** `rank(A) = ` + 由 `numpy.linalg.matrix_rank(A, tol=1e-9)` 計算的值（恆 0 或 1）。

##### G. 互動行為（Interactions）
- **拉動 $a_i$ slider：** 該 cell 列（第 $i$ 橫躺行）整列即時重算；若處於「行平行」模式，該行整體縮放動畫 200ms。
- **拉動 $b_j$ slider：** 第 $j$ 直立列整列即時重算；若處於「列平行」模式，該列整體縮放動畫 200ms。
- **hover cell $(i, j)$：** 該 cell 加粗外框；tooltip 顯示 `A[${i}][${j}] = ${a_i}} × ${b_j} = ${a_i * b_j}`。
- **click cell $(i, j)$：** 該 cell 持續高亮 + 同時把 $a_i$ slider 與 $b_j$ slider 兩條控制端標出紅圈，視覺連結「這格的值來自這兩個 slider」。
- **快捷鍵：** `R` 切到「列平行」、`C` 切到「行平行」、`O` 關閉、`0` 把所有 slider 歸零（演示 rank = 0）。

##### H. 動畫腳本（平行性高亮淡入）
- **t=0–200ms:** radio 切到「列平行」時，全矩陣各直立列從無背景到綠色底 alpha 0 → 0.4 漸入，「= $b_j$ × $\mathbf{a}$」標籤從下方滑入。
- **t=200ms 後:** 穩態，等待 hover 或下次切換。
- **總長度：** 200ms。
- **緩動：** ease-out（CSS cubic-bezier(0, 0, 0.2, 1)）。
- **暫停 / 倒轉：** 否。

##### I. 邊界與錯誤處理
- **$\mathbf{a} = \mathbf{0}$ 或 $\mathbf{b} = \mathbf{0}$：** 全矩陣 cell 變灰、文字置中顯示 `0`；右側 rank 紅字「rank = 0」；公式區下方紅字提示「至少一向量為零，外積退化」。
- **某 $a_i = 0$：** 第 $i$ 橫躺行整行淡灰底，cell 仍顯示 `0`；rank 仍 = 1，提示「第 $i$ 行為零，但 rank 維持 1」。
- **$m = n = 6$ 最大：** cell 縮為 48×48 px、字級 14pt、slider 較密；動畫禁用避免頓。
- **$m = n = 2$ 最小：** cell 增為 80×80 px，slider 標籤字級放大 14pt。
- **使用者拖動 slider 過快：** debounce 30ms 避免重畫風暴。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - $a_i$ slider：「列向量 $\mathbf{a}$ 的第 $i$ 個分量（直立綠色那條）」
  - $b_j$ slider：「行向量 $\mathbf{b}^{\mathrm{T}}$ 的第 $j$ 個分量（橫躺粉紅那條）」
  - 平行性 radio：「打開後可看到外積結果矩陣的所有直立列彼此平行（或所有橫躺行彼此平行），這就是 rank 1 的視覺意涵」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「左邊是直立列向量 $\mathbf{a}$，上面是橫躺行向量 $\mathbf{b}^{\mathrm{T}}$」
  - Step 2：「中間每個 cell 是對應的 $a_i \times b_j$」
  - Step 3：「按右下『列平行』，看到每一直立列其實是 $\mathbf{a}$ 的不同倍數」
  - Step 4：「拉 $\mathbf{a}$ 任一分量，看到對應整橫躺行同步縮放 — 這就是 rank 1」
  - Step 5：「拉到所有 $a_i = 0$，rank 變 0，外積退化」
- **常見誤解警示：** 「rank 1 不代表只有 1 個非零元素 — 是 1 個自由度（一條方向被複製）」
- **延伸閱讀：** 原書 p.2 §2、本專案 `ch02-vec-vec.md`、Strang LAFE Sec. 1.3 (p.25) Matrix of Rank One。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo（反應式 notebook）+ matplotlib（2D 矩陣繪製）+ marimo.ui（控制元件）
- **替代方案：** Streamlit + Plotly heatmap（如需網頁分享，平行性高亮用 `go.Heatmap` + `shapes` 疊圖）
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫 cell + 色塊
  - `matplotlib.text.Text` 放數字 + 公式（公式用 `r"$...$"`）
  - `marimo.ui.slider`、`marimo.ui.radio`、`marimo.ui.button`
  - `numpy.outer(a, b)` 計算外積、`numpy.linalg.matrix_rank` 計算秩
- **檔案結構：**
  ```
  viz/
    ch02_outer_product.py        # 主入口（含 VizScript-01 與 02 共用畫面）
    _common/
      palette.py                 # 沿用 §1 配色（綠 #2ca02c / 粉紅 #d62728 / 灰）
      vector_canvas.py           # 直立列與橫躺行的繪圖工具（給 §3+ 重用）
  ```
- **效能：** 拉 slider 時用 `ax.clear()` 重畫 cell + 文字即可；勿在每次更新時 `plt.figure()`。建議在 `marimo.cache` 包住 `numpy.outer` 計算（雖然很快，但維持模式一致）。
- **測試：** snapshot test：預設值矩陣輸出 + rank = 0 退化情況 + symmetric ($\mathbf{a} = \mathbf{b}$) 情況各 1 張 PNG，CI 比對。

##### L. 驗收標準（Acceptance Criteria）
- [ ] $\mathbf{a}, \mathbf{b}$ 各分量 slider 拉動後，矩陣 cell 重算 < 100ms 完成。
- [ ] 「列平行」模式高亮正確：所有直立列皆同色綠底，且 hover 某列時其他列半透明。
- [ ] 「行平行」模式高亮正確：所有橫躺行皆同色粉底，且 hover 某行時其他行半透明。
- [ ] 任一向量設為全零時，rank 顯示「0」紅字 + 退化提示文字出現。
- [ ] $m, n$ 在 [2, 6] 範圍內可拉動，cell 永不重疊、永不出框。
- [ ] Walkthrough 5 步驟首次開啟自動觸發，可關閉並有「再看一次」按鈕。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純顯示 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 矩陣 + 兩組 slider，無平行性高亮、無動畫。
- **Tier 3 擴充：** + 拖曳 $\mathbf{a}$ 在 2D / 3D 空間的箭頭端點改值（geometric drag）+ 旁邊同步畫「列空間 = $\operatorname{span}\{\mathbf{a}\}$ 一條直線」3D 視角。
- **估時：** 1.5 session（含測試與 walkthrough）

---

#### VizScript-02: 點積 vs 外積對偶切換（Dot ↔ Outer Duality）

##### A. 一句話定位
讓使用者 toggle 切換 (v1) / (v2)，看同樣兩個直立向量 $\mathbf{a}, \mathbf{b}$ 因為**轉置誰**而產出截然不同尺寸的結果。

##### B. 學習目標（Learning Outcome）
- 使用者能說出 (v1) $\mathbf{a}^{\mathrm{T}}\mathbf{b}$ 的形狀運算是 $(1 \times m)(m \times 1) = (1 \times 1)$ 純量。
- 使用者能說出 (v2) $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 的形狀運算是 $(m \times 1)(1 \times n) = (m \times n)$ 矩陣。
- 使用者能解釋「為什麼 (v1) 要求兩向量同維度、(v2) 不需要」。
- 使用者能在切換時看出哪個向量被轉置（橫躺起來）、結果端點如何從一個點擴張成一塊矩陣。

##### C. 待視覺化的數學物件
- **物件清單：** 列向量 $\mathbf{a} \in \mathbb{R}^m$、列向量 $\mathbf{b} \in \mathbb{R}^n$（在 (v1) 模式時要求 $m = n$）；產物 $s = \mathbf{a}^{\mathrm{T}}\mathbf{b} \in \mathbb{R}$（v1）或 $A = \mathbf{a}\mathbf{b}^{\mathrm{T}} \in \mathbb{R}^{m \times n}$（v2）。
- **預設值：** $\mathbf{a} = (1, 2, 3)^{\mathrm{T}}$、$\mathbf{b} = (1, 1, 1)^{\mathrm{T}}$（預設 $m = n = 3$ 讓兩種視角都可運作）。
- **維度範圍：** $m, n \in [2, 6]$；在 (v1) 模式時 UI 強制鎖 $n = m$（切到 (v1) 時 $n$ slider 跟著 $m$ 同步並顯示鎖頭符號）。
- **數值範圍：** 同 VizScript-01。
- **退化情形：**
  - **(v1) $\mathbf{a} \perp \mathbf{b}$（點積 = 0）：** 結果顯示 `0`，配文字「兩向量正交」。
  - **(v2) $\mathbf{a} = \mathbf{0}$ 或 $\mathbf{b} = \mathbf{0}$：** 與 VizScript-01 相同的零矩陣退化處理。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 75% 主動畫畫面、下 25% 控制列（含 (v1)/(v2) toggle + 共用的 $\mathbf{a}, \mathbf{b}$ slider）。
- **主畫面尺寸：** 800×480 px，白底；中央是運算式佈局，由左至右四段：**[向量 1] — [向量 2] — [`=`] — [結果]**。
- **(v1) 模式排列：** [粉紅橫條 $\mathbf{a}^{\mathrm{T}}$] [綠直條 $\mathbf{b}$] `=` [單一藍點，藍點旁公式 `s = ...`]。
- **(v2) 模式排列：** [綠直條 $\mathbf{a}$] [粉紅橫條 $\mathbf{b}^{\mathrm{T}}$] `=` [$m \times n$ 藍點網格矩陣]。
- **公式區（畫面右上角，疊在主畫面內）：** 即時 LaTeX 公式 + 結果端的形狀標籤 `(1×1)` 或 `(m×n)`。
- **配色：** 同 VizScript-01 + §1（綠 / 粉紅 / 藍點 / 灰底）。
- **字型 / 字級：** 結果區公式 18pt MathJax、向量內部分量數字 14pt monospace。
- **邊距：** 上下 20px、左右 30px。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 | toggle | v1 / v2 | v1 | 即時（含 500ms 動畫過渡） |
| $m$ | slider | [2, 6] step 1 | 3 | 即時 |
| $n$ | slider | [2, 6] step 1 | 3 | 即時（v1 模式時與 $m$ 鎖定同步） |
| $a_i$ | slider $m$ 個 | [-9, 9] step 1 | $(1,2,3)$ | 即時 |
| $b_j$ | slider $n$ 個 | [-9, 9] step 1 | $(1,1,1)$ | 即時 |

##### F. 輸出畫面細節（Outputs）
- **(v1) 結果端：** 單一藍點（直徑 32px），點旁文字 `s = a₁b₁ + a₂b₂ + ... + aₘbₘ = ${value}`；當 $s = 0$ 額外標籤「⊥」。
- **(v2) 結果端：** $m \times n$ 藍點網格 + 每 cell 對應數字 `a_i × b_j`；左緣綠色細條（標 $\mathbf{a}$ 來源）、上緣粉色細條（標 $\mathbf{b}^{\mathrm{T}}$ 來源），與圖 2.1 右側抽象示意一致。
- **形狀標籤：** (v1) 時顯示 `(1×$m$)·($m$×1) = (1×1) 純量`；(v2) 時顯示 `($m$×1)·(1×$n$) = ($m$×$n$) 矩陣`。
- **rank 顯示：** (v2) 模式時右下角顯示 rank（0 或 1）；(v1) 模式時改顯示「Dot product = $s$」。

##### G. 互動行為（Interactions）
- **toggle v1 ↔ v2：** 觸發轉置動畫（見 §H）；公式區同步切換。
- **拉動 $a_i$ / $b_j$ slider：** 結果端即時重算；(v1) 模式時藍點上的文字更新；(v2) 模式時對應 cell 更新。
- **hover 向量某分量：**
  - (v1) 模式：對應位置的 $\mathbf{a}^{\mathrm{T}}$ 與 $\mathbf{b}$ 同時高亮，並在點積展開式中對應項加粗。
  - (v2) 模式：對應整行 / 整列亮起。
- **快捷鍵：** `1` 切到 v1、`2` 切到 v2、`Space` toggle。

##### H. 動畫腳本（v1 ↔ v2 轉置切換）
- **從 v1 → v2:**
  - **t=0:** v1 穩態（粉紅橫條 + 綠直條 + 藍點）。
  - **t=0–200ms:** 結果藍點 fade out（opacity 1 → 0）。
  - **t=200–500ms:** 左邊粉紅橫條「立起來」變綠直條（旋轉 90° 並換色，500ms 內完成）；同時右邊綠直條「躺下來」變粉紅橫條。實作上：把 $\mathbf{a}$ 的橫躺 row vector 圖示縮短 + 顏色由粉紅變綠 + 高度增加；$\mathbf{b}$ 反之。
  - **t=500–700ms:** 中央出現空白矩陣框（淡入），cell 逐個從中心向外展開（stagger 30ms / cell）填上數字。
  - **t=700ms 後:** v2 穩態。
- **從 v2 → v1:** 反向重播（cell 收回 → 矩陣框消失 → 兩個向量旋轉換色 → 藍點淡入）。
- **總長度：** 700ms。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **暫停 / 倒轉：** 是（提供「再播一次」按鈕；toggle 過程中按 Esc 立即停在當前 frame）。

##### I. 邊界與錯誤處理
- **v1 模式但 $m \ne n$：** UI 不允許（slider 鎖定）；若使用者用快捷鍵硬切，跳出 toast「v1 需要兩向量同維度，已自動把 $n$ 設為 $m$」。
- **動畫進行中再切換：** debounce 100ms 或等動畫完成才接受下一次 toggle，避免狀態錯亂。
- **$m = n = 6$ 大尺寸 + v2：** 矩陣 cell 縮為 48×48 px；動畫禁用 stagger 改用整體 fade。
- **點積結果絕對值 > 999：** 結果文字字級自動由 18pt 降為 14pt 避免溢框。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - toggle (v1)：「行向量 × 列向量 = 一個數字（純量）」
  - toggle (v2)：「列向量 × 行向量 = 一個秩 1 矩陣」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 (v1) 視角，左邊粉紅橫條是 $\mathbf{a}^{\mathrm{T}}$、右邊綠直條是 $\mathbf{b}$」
  - Step 2：「結果只有一個藍點 — 一個數字」
  - Step 3：「按右下 toggle 切換到 (v2)」
  - Step 4：「兩個向量轉了 90 度 — 左邊變綠直條 $\mathbf{a}$、右邊變粉紅橫條 $\mathbf{b}^{\mathrm{T}}$」
  - Step 5：「結果從 1 個藍點擴張成一塊矩陣 — 但只有 1 個自由度（rank 1）」
- **常見誤解警示：**
  - 「(v1) 與 (v2) 不是計算順序的選擇，是把哪個向量轉置的選擇」
  - 「點積得到的數字 = 外積矩陣的跡 (trace)？」 — **錯**，這只在 $m = n$ 且 $\mathbf{a} = \mathbf{b}$ 時近似成立（$\operatorname{tr}(\mathbf{a}\mathbf{a}^{\mathrm{T}}) = \|\mathbf{a}\|^2 = \mathbf{a}^{\mathrm{T}}\mathbf{a}$）；一般 $\mathbf{a} \ne \mathbf{b}$ 時兩者不等。
- **延伸閱讀：** 原書 p.2、`ch02-vec-vec.md` 數學要點段。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + `matplotlib.animation.FuncAnimation`（控制 v1↔v2 動畫）+ marimo.ui。
- **替代方案：** D3.js + SVG（如需高品質網頁動畫；旋轉換色用 CSS transform + filter）。
- **關鍵 API：**
  - `matplotlib.transforms.Affine2D().rotate_deg_around()` 做向量旋轉動畫
  - `matplotlib.animation.FuncAnimation(fig, update, frames=42, interval=16)`（700ms / 42 frames）
  - `matplotlib.patches.FancyArrowPatch` 做向量箭頭（也可用 Rectangle）
- **檔案結構：** 與 VizScript-01 同檔（`viz/ch02_outer_product.py`），共用 `_common/palette.py` 與 `vector_canvas.py`。
- **效能：** 動畫期間預先計算所有 frame 的座標 / 顏色，存 list，避免每 frame 重算。動畫結束後切回 reactive 模式。
- **測試：** 動畫關鍵 frame（t=0 / 200 / 500 / 700ms）各 1 張 snapshot PNG。

##### L. 驗收標準（Acceptance Criteria）
- [ ] v1 ↔ v2 toggle 動畫總長 ≤ 700ms，60fps 無 frame drop。
- [ ] v1 模式下 $m \ne n$ 不可能發生（UI 鎖定）。
- [ ] 點積結果 $\mathbf{a}^{\mathrm{T}}\mathbf{b} = 0$ 時自動標示「⊥」。
- [ ] 切換動畫中再按 toggle 不導致狀態錯亂（debounce 或佇列）。
- [ ] Walkthrough 5 步驟首次開啟自動觸發。
- [ ] 公式區 LaTeX 渲染 < 50ms 完成（MathJax cache）。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純靜態並列兩張圖（v1 + v2），無動畫無切換。
- **Tier 3 擴充：** + 把 $\mathbf{a}, \mathbf{b}$ 同時也在 2D 平面上畫成箭頭，動畫顯示「夾角」（點積幾何意涵 $\mathbf{a}^{\mathrm{T}}\mathbf{b} = \|\mathbf{a}\|\|\mathbf{b}\|\cos\theta$）。
- **估時：** 1.5 session（含動畫調校與 walkthrough）

---

### 章末延伸

- **後續章節連結：** [→ ch03-mat-vec.md](ch03-mat-vec.md) — §3 矩陣乘以向量（Matrix × Vector）也有兩種視角（dot product way / linear combination way），是本章 (v1) 與 (v2) 的自然推廣。

- **延伸閱讀 / 相關概念：**
  - Strang《Linear Algebra for Everyone》Sec. 1.1（線性組合與點積）、Sec. 1.3（秩 1 矩陣）、Sec. 1.4（行 / 列方法）— 原書直接對應段落。
  - 後續 §6 五大分解皆以「秩 1 矩陣之和」為共同骨架；本章 (v2) 是必備前置知識。
  - **跨領域類比：** 神經網路裡的權重外積更新（Hebbian rule、低秩近似 LoRA）本質就是「外積 → 秩 1 矩陣」的應用 — 不在本書範圍但值得知道。

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 49–67 / `The-Art-of-Linear-Algebra.pdf` p.2
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 47–66
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0

---

## 第 3 章. 矩陣乘以向量 — 兩種視角 + 四個基本子空間（Matrix × Vector — 2 Ways + The Four Subspaces）

> **原書頁碼：** p.3
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 69–112 行
> **本章圖數：** 3（Figure 3.1 / 3.2 / 3.3）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成 / [ ] 校對中

---

### 章節摘要

矩陣乘以向量 $A\mathbf{x}$ 有兩種視角：**(Mv1) 點積方式** — 把 $A$ 的每一橫躺行當成一個向量，與 $\mathbf{x}$ 做點積，得到一條由「行數個點積」堆出來的列向量；**(Mv2) 線性組合方式** — 把 $A$ 的每一直立列當成一個向量，用 $\mathbf{x}$ 的分量當係數做線性組合，得到的依然是同一條列向量。**初學會先學 (Mv1)，但 (Mv2) 才是後續所有章節（特別是子空間與分解）的鑰匙。**

對偶側：**行向量** $\mathbf{y}$ 從左邊乘以 $A$ 也有完全平行的兩種視角 — **(vM1)** 點積方式（$\mathbf{y}$ 對 $A$ 每一直立列做點積）、**(vM2)** 線性組合方式（$A$ 每一橫躺行用 $\mathbf{y}$ 分量做線性組合）。

把這兩組視角合起來，會自然冒出**四個基本子空間 (Four Fundamental Subspaces)**：
- 在 $\mathbb{R}^n$ 中：**行空間 (row space)** $\mathbf{C}(A^{\mathrm{T}})$（所有可能的 $\mathbf{y}A$）與 **零空間 (nullspace)** $\mathbf{N}(A)$（所有滿足 $A\mathbf{x} = \mathbf{0}$ 的 $\mathbf{x}$），兩者**正交互補**；
- 在 $\mathbb{R}^m$ 中：**列空間 (column space)** $\mathbf{C}(A)$（所有可能的 $A\mathbf{x}$）與 **左零空間 (left nullspace)** $\mathbf{N}(A^{\mathrm{T}})$（所有滿足 $\mathbf{y}A = 0$ 的 $\mathbf{y}$），兩者**正交互補**。

> ⚠ **本章是全書最濃縮的一章。** §1 鋪設視角、§2 是「外積 = 秩 1」基本骨架，本章一次端上**「兩個運算 × 兩個視角 × 兩個方向」=「八種乘法畫面」+ 四個子空間的幾何圖**。讀通後，§6 的所有分解都會變成自然推論。

> ⚠ **術語提醒（沿用 §1 / §2 全書慣例 — A 派）：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。$\mathbf{C}(A) = $ 列空間（columns of $A$ 張成）、$\mathbf{C}(A^{\mathrm{T}}) = $ 行空間（rows of $A$ 張成）、$\mathbf{N}(A) = $ 零空間、$\mathbf{N}(A^{\mathrm{T}}) = $ 左零空間。

---

### 數學要點

設 $A \in \mathbb{R}^{m \times n}$（$m$ 行 $n$ 列）、$\mathbf{x} \in \mathbb{R}^n$、$\mathbf{y} \in \mathbb{R}^{1 \times m}$（行向量）。

#### (Mv1) 點積方式（Dot Product Way）

把 $A$ 拆成 $m$ 個橫躺行 $\mathbf{a}^*_1, \mathbf{a}^*_2, \ldots, \mathbf{a}^*_m \in \mathbb{R}^{1 \times n}$（每個是行向量），則：

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix}
\mathbf{x}
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 \cdot \mathbf{x} \\ \mathbf{a}^*_2 \cdot \mathbf{x} \\ \vdots \\ \mathbf{a}^*_m \cdot \mathbf{x} \end{bmatrix}
\;\in\; \mathbb{R}^m
$$

- **形狀運算：** $(m \times n)(n \times 1) = (m \times 1)$。
- **逐分量計算：** 第 $i$ 個輸出分量 $= \sum_{k=1}^{n} a_{ik} x_k$。
- **原書 (Mv1) 範例：**

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
\;=\;
\begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}
$$

#### (Mv2) 線性組合方式（Linear Combination Way）

把 $A$ 拆成 $n$ 個直立列 $\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n \in \mathbb{R}^m$（每個是列向量），則：

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}
\;=\;
x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots + x_n \mathbf{a}_n
\;\in\; \mathbb{R}^m
$$

- **形狀運算：** 同 (Mv1)，$(m \times n)(n \times 1) = (m \times 1)$。
- **直覺：** $\mathbf{x}$ 的每一個分量都是一個「混合比例」，告訴你要把 $A$ 的某一直立列**放大幾倍**，再把所有放大後的列**疊加**起來。
- **原書 (Mv2) 範例：**

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
\;=\;
x_1 \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + x_2 \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}
$$

#### 對偶關係（Mv1 ↔ Mv2）

兩種視角**計算結果完全一致**，差別在「讀法」：
- (Mv1) 是「**逐個橫躺行單獨吃進整個 $\mathbf{x}$**」 — 每一橫躺行各自做完一個 dot product，把 $m$ 個結果堆出來。
- (Mv2) 是「**逐個直立列同時被 $\mathbf{x}$ 的某分量縮放**」 — $\mathbf{x}$ 一次決定所有列的縮放比例，再把它們向量相加。

兩者也對應「**外向看**」與「**內向看**」：(Mv1) 把 $A$ 攤平成橫躺行；(Mv2) 把 $A$ 拼立成直立列。

#### (vM1) 行向量點積方式（Row Dot Product Way）

把 $A$ 拆成 $n$ 個直立列 $\mathbf{a}_1, \ldots, \mathbf{a}_n$，行向量 $\mathbf{y} \in \mathbb{R}^{1 \times m}$ 從左乘以 $A$：

$$
\mathbf{y} A
\;=\;
\mathbf{y}
\begin{bmatrix} \mathbf{a}_1 & \cdots & \mathbf{a}_n \end{bmatrix}
\;=\;
\begin{bmatrix} \mathbf{y} \cdot \mathbf{a}_1 & \mathbf{y} \cdot \mathbf{a}_2 & \cdots & \mathbf{y} \cdot \mathbf{a}_n \end{bmatrix}
\;\in\; \mathbb{R}^{1 \times n}
$$

- **形狀運算：** $(1 \times m)(m \times n) = (1 \times n)$，結果是一個行向量。
- **逐分量計算：** 第 $j$ 個輸出分量 $= \mathbf{y} \cdot \mathbf{a}_j = \sum_{i=1}^{m} y_i a_{ij}$。
- **原書 (vM1) 範例：**

$$
\mathbf{y} A
\;=\;
\begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix}
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\;=\;
\begin{bmatrix} y_1 + 3y_2 + 5y_3 & 2y_1 + 4y_2 + 6y_3 \end{bmatrix}
$$

#### (vM2) 行向量線性組合方式（Row Linear Combination Way）

把 $A$ 拆成 $m$ 個橫躺行 $\mathbf{a}^*_1, \ldots, \mathbf{a}^*_m$，則：

$$
\mathbf{y} A
\;=\;
\begin{bmatrix} y_1 & y_2 & \cdots & y_m \end{bmatrix}
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix}
\;=\;
y_1 \mathbf{a}^*_1 + y_2 \mathbf{a}^*_2 + \cdots + y_m \mathbf{a}^*_m
\;\in\; \mathbb{R}^{1 \times n}
$$

- **直覺：** $\mathbf{y}$ 的每一分量是「混合比例」，把 $A$ 的某一橫躺行放大幾倍，再把所有橫躺行疊加成一條新行向量。
- **原書 (vM2) 範例：**

$$
\mathbf{y} A
\;=\;
\begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix}
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\;=\;
y_1 \begin{bmatrix} 1 & 2 \end{bmatrix} + y_2 \begin{bmatrix} 3 & 4 \end{bmatrix} + y_3 \begin{bmatrix} 5 & 6 \end{bmatrix}
$$

#### Mv ↔ vM 對偶（左乘 vs 右乘的鏡像對稱）

| | 點積方式（1） | 線性組合方式（2） | 結果型 |
|---|---|---|---|
| **右乘** $A\mathbf{x}$ | (Mv1) 每**橫躺行** · $\mathbf{x}$ | (Mv2) $\mathbf{x}$ 對 $A$ 的**直立列**做線性組合 | 列向量 $\in \mathbb{R}^m$ |
| **左乘** $\mathbf{y}A$ | (vM1) $\mathbf{y}$ · 每**直立列** | (vM2) $\mathbf{y}$ 對 $A$ 的**橫躺行**做線性組合 | 行向量 $\in \mathbb{R}^{1 \times n}$ |

**記憶口訣：**「**點積看對立方向、線性組合看同方向**」— Mv1 行（橫躺） · 列（直立）方向互垂直；Mv2 列向量被列向量縮放（同直立）。vM 也一樣：vM1 行 · 列 垂直、vM2 行向量被行向量縮放（同橫躺）。

#### 四個基本子空間（The Four Fundamental Subspaces）

把上面兩個運算所有可能的輸出蒐集起來，就會在 $\mathbb{R}^n$ 與 $\mathbb{R}^m$ 中各得到兩個子空間，共**四個**：

| 子空間 | 定義 | 所在空間 | 維度 | 物理意義 |
|---|---|---|---|---|
| **列空間** $\mathbf{C}(A)$ | $\{A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n\}$ = $A$ 所有直立列的線性組合 | $\mathbb{R}^m$ | $r$（秩） | "What $A$ can output as $A\mathbf{x}$" — 所有 (Mv2) 結果的集合 |
| **零空間** $\mathbf{N}(A)$ | $\{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0}\}$ | $\mathbb{R}^n$ | $n - r$ | "What $A$ sends to zero" — 滿足 (Mv1) 全為 0 的 $\mathbf{x}$ |
| **行空間** $\mathbf{C}(A^{\mathrm{T}})$ | $\{\mathbf{y}A : \mathbf{y} \in \mathbb{R}^{1 \times m}\}$ = $A$ 所有橫躺行的線性組合 | $\mathbb{R}^n$ | $r$（與列空間同維） | 所有 (vM2) 結果的集合 |
| **左零空間** $\mathbf{N}(A^{\mathrm{T}})$ | $\{\mathbf{y} \in \mathbb{R}^{1 \times m} : \mathbf{y}A = 0\}$ | $\mathbb{R}^m$ | $m - r$ | 滿足 (vM1) 全為 0 的 $\mathbf{y}$ |

**兩對正交分解（perpendicular decomposition）：**

$$
\mathbb{R}^n \;=\; \mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A),
\qquad
\mathbf{C}(A^{\mathrm{T}}) \perp \mathbf{N}(A)
$$

$$
\mathbb{R}^m \;=\; \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}}),
\qquad
\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}})
$$

**正交性的直接證明（一行）：** 設 $\mathbf{v} \in \mathbf{N}(A)$，則 $A\mathbf{v} = \mathbf{0}$，亦即 $A$ 的每一橫躺行 $\cdot \mathbf{v} = 0$。所以 $\mathbf{v}$ 與每一橫躺行都垂直 → $\mathbf{v} \perp \mathbf{C}(A^{\mathrm{T}})$。

**為何說「自然冒出」？** (Mv1) 與 (vM1) 都是「以橫躺 / 直立向量做點積」 — 點積等於零正是「垂直」的定義；而 (Mv2) 與 (vM2) 都是「以列 / 行做線性組合」 — 線性組合的張成正是「子空間」的定義。**四個子空間就是「兩個運算 × 兩個視角」自然交叉的產物**。

#### 對應原書章節（Strang《Linear Algebra for Everyone》）

- Sec. 1.1 (p.3) Linear combinations — 對應 (Mv2)
- Sec. 1.3 (p.21) Matrices and Column Spaces — 對應 $\mathbf{C}(A)$
- Sec. 3.5 (p.124) Dimensions of the Four Subspaces — 對應四子空間維度定理
- 補充：Sec 6.1 $A = CR$ 給出秩 $r$ 的具體分解（將在 §6.1 詳細處理）

---

### 圖片區

本章共 3 張圖：Figure 3.1（Mv1, Mv2）、Figure 3.2（vM1, vM2）、Figure 3.3（Four Subspaces）。

---

#### Figure 3.1: 矩陣乘以向量的兩種視角（Matrix × Vector — (Mv1), (Mv2)）

**圖檔：** `docs/book/figs-png/MatrixTimesVector.png`（原始 EPS：`figs/MatrixTimesVector.eps`）
**原書頁碼：** p.3
**所屬章節：** §3

##### 視覺結構 (Visual Structure)

此圖採「左右並列兩區」結構，**左半 (Mv1) 點積方式**、**右半 (Mv2) 線性組合方式**，每區「**抽象色塊示意（上）+ 文字描述（中）+ 具體數字範例（下）**」三層。

- **左半：(Mv1) 點積方式**
  - 左上角小灰圈內標 `Mv1`，標示視角編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **粉紅色橫條 × 3 條** 堆疊在大方框內 —— 表示 $A$ 的 3 個橫躺行（rows）。
    2. **綠色直條** —— 表示列向量 $\mathbf{x}$（直立）。
    3. **粉紅色橫條 × 3 條**，每條中段被綠色色塊覆蓋 —— 表示產出的列向量 $A\mathbf{x}$，每個分量是「該橫躺行 · $\mathbf{x}$」的 dot product 結果（粉紅 + 綠交疊代表 dot 過程）。
  - 中段文字：**"The row vectors of $A$ are multiplied by a vector $\mathbf{x}$ and become the three dot-product elements of $A\mathbf{x}$."**
  - 具體範例（最下方）：
    $$A\mathbf{x} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}$$
- **右半：(Mv2) 線性組合方式**
  - 左上角小灰圈內標 `Mv2`，標示視角編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **綠色直條 × 2 條** 並列在大方框內 —— 表示 $A$ 的 2 個直立列（columns）。
    2. **2 個藍色實心圓點**直立排列在小方框內 —— 表示 $\mathbf{x}$ 的兩個分量（$x_1, x_2$）。
    3. 在 `=` 右側出現 **2 個項相加**的結構：「藍點 × 綠直條 + 藍點 × 綠直條」 —— 表示 $\mathbf{x}$ 的每個分量分別縮放 $A$ 的每一直立列，再相加。
  - 中段文字：**"The product $A\mathbf{x}$ is a linear combination of the column vectors of $A$."**
  - 具體範例（最下方）：
    $$A\mathbf{x} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = x_1 \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + x_2 \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}$$
- **配色語意（沿用 §1 §2）：** 綠 = 列向量 / 直立、粉紅 = 行向量 / 橫躺、藍點 = 標量 / $\mathbf{x}$ 分量、灰 = 結構填充。
- **左右兩區的「視角互補」對比：**
  - (Mv1) 主角是**橫躺粉紅** — $A$ 被攤平成 3 個橫躺行，每行各自吃進整個 $\mathbf{x}$。
  - (Mv2) 主角是**直立綠** — $A$ 被拼立成 2 個直立列，$\mathbf{x}$ 從上方一次分配權重給所有列。
  - 兩種視角的「動詞」不同：(Mv1) 是「**逐行 dot**」、(Mv2) 是「**整體 weight**」。

讀者的視覺動線：先看左半 (Mv1) 確認熟悉的「逐行點積運算」 → 跳到右半 (Mv2) 看到「同樣的結果可從『列向量加權和』算出」 → 對比下方兩個具體範例（同一個 $A$ 和 $\mathbf{x}$，左邊是分量展開、右邊是列向量乘係數展開）→ 領悟「(Mv2) 把 $A\mathbf{x}$ 重新詮釋成 column space 中的一個向量」這個關鍵翻轉。

##### 數學內容 (Mathematical Content)

兩種視角共享同一個結果 $A\mathbf{x} \in \mathbb{R}^m$，但展開方式不同。

**設定：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \in \mathbb{R}^{3 \times 2}$，$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \in \mathbb{R}^2$。

**(Mv1) 點積展開：**

$$
A\mathbf{x} \;=\; \begin{bmatrix} \mathbf{a}^*_1 \cdot \mathbf{x} \\ \mathbf{a}^*_2 \cdot \mathbf{x} \\ \mathbf{a}^*_3 \cdot \mathbf{x} \end{bmatrix} \;=\; \begin{bmatrix} (1, 2) \cdot (x_1, x_2) \\ (3, 4) \cdot (x_1, x_2) \\ (5, 6) \cdot (x_1, x_2) \end{bmatrix} \;=\; \begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}
$$

**(Mv2) 線性組合展開：**

$$
A\mathbf{x} \;=\; x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 \;=\; x_1 \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + x_2 \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} \;=\; \begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}
$$

**驗證恆等：** 兩種展開的每一分量逐項相同（$x_1 + 2x_2 = 1 \cdot x_1 + 2 \cdot x_2$，依此類推）。

**形狀運算（兩種視角共通）：** $(3 \times 2)(2 \times 1) = (3 \times 1)$。中間維度 2 必須相等才能做乘法。

**列空間的具體呈現：** 任何 $A\mathbf{x}$ 都可寫成 $x_1 (1,3,5)^{\mathrm{T}} + x_2 (2,4,6)^{\mathrm{T}}$，即 $\mathbf{C}(A) = \operatorname{span}\{(1,3,5)^{\mathrm{T}}, (2,4,6)^{\mathrm{T}}\} \subset \mathbb{R}^3$。由於這兩個列向量線性獨立（不成比例），$\dim \mathbf{C}(A) = r = 2$，是 $\mathbb{R}^3$ 中的一個平面。

##### 直覺解讀 (Intuition)

**1. 同一個運算的兩種「閱讀方向」。** 矩陣乘向量 $A\mathbf{x}$ 不是兩個算式 — 是同一個算式被「**橫切**」（Mv1：一行一行做點積）或「**縱切**」（Mv2：一列一列做縮放再相加）的兩個視角。剛入門時 (Mv1) 直觀（套用點積公式），但 (Mv2) 才是矩陣論的核心 — 因為它把 $A\mathbf{x}$ 解讀成「$A$ 列空間裡的某個向量」，直接連接到子空間 / 秩 / 解的存在性。

**2. 為什麼 (Mv2) 是後續一切的鑰匙？**

- **「$A\mathbf{x} = \mathbf{b}$ 有解 ⟺ $\mathbf{b} \in \mathbf{C}(A)$」** — 這個基本定理直接從 (Mv2) 視角看到：因為 $A\mathbf{x}$ 就是 $A$ 直立列的線性組合，所以 $\mathbf{b}$ 必須是這些列的某個組合才有解。從 (Mv1) 視角看則需要繞一圈點積與聯立方程。
- **「秩 = 線性無關直立列的最大個數」** — 從 (Mv2) 視角看，秩就是「$\mathbf{C}(A)$ 的維度」，是 $A$「能輸出多少不同方向」的衡量。
- **「特徵向量 / 奇異向量都是『被 $A$ 直立列線性組合』後恰好指向特定方向的 $\mathbf{x}$」** — §6 的所有矩陣分解都建立在 (Mv2) 視角上。

**3. 兩個視角對應兩種解方程策略。** 解 $A\mathbf{x} = \mathbf{b}$：
- **從 (Mv1) 出發** → 高斯消去法（Gaussian elimination）— 對橫躺行做加減消元。
- **從 (Mv2) 出發** → 投影 / 最小二乘 / SVD — 找 $\mathbf{C}(A)$ 中最接近 $\mathbf{b}$ 的點。
高中學的解聯立屬 (Mv1) 思路；機器學習與信號處理大量使用 (Mv2) 思路。

**4. 矩陣的本質是「函數」，$\mathbf{x}$ 是「指令」。** 從 (Mv2) 看，$A$ 把「$\mathbf{x}$ 的每個分量」翻譯成「對應直立列要放大幾倍」。$\mathbf{x}$ 是一份「混合配方」、$A$ 的直立列是「材料庫」、$A\mathbf{x}$ 是「成品」。

**常見誤解警示：**
- **「(Mv1) 和 (Mv2) 是不同算法」** — 否，**完全相同的計算結果**，只是「視角 / 解讀順序」不同。差別在心智模型而非數值。
- **「線性組合 (Mv2) 的係數從哪來？」** — $\mathbf{x}$ 的分量本身就是係數，不需另外求。$\mathbf{x}$ 的角色從「被矩陣作用的向量」翻轉成「指揮列向量怎麼組合的係數」。
- **「直立列必須線性獨立」** — 否，$A$ 的直立列可以線性相依（此時 $r < n$），但 $A\mathbf{x}$ 永遠落在 $\mathbf{C}(A)$ 內。

**為什麼這張圖該做成互動視覺化？** 「拉 $\mathbf{x}$ 的分量看 (Mv2) 兩個列同步縮放再疊加」是動態概念 — 靜態圖無法傳達「縮放動畫」與「向量加法尾接頭視覺」。並且 (Mv1) → (Mv2) 的「視角切換」本身就是本書最重要的認知翻轉（見 VizMark-01）。另外輸入 $\mathbf{x}$ 看 $A\mathbf{x}$ 在 3D 平面上掃過 $\mathbf{C}(A)$ 也是建立子空間直覺的關鍵（見 VizMark-04）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [切換視角] ⭐⭐⭐
> **位置：** Figure 3.1 / §3 / (Mv1) ↔ (Mv2) 對偶
> **核心概念：** $A\mathbf{x}$ 同時是「橫躺行的點積堆疊」與「直立列的線性組合」 — 兩種視角同結果
> **互動梗概：** toggle (Mv1) / (Mv2)，畫面動畫切換「行橫躺被綠覆蓋 → 列直立被藍點縮放並疊加」，下方公式同步重排
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-04** [拉桿調參 + 空間幾何] ⭐
> **位置：** Figure 3.1 / §3 / (Mv2) 結果端
> **核心概念：** $A\mathbf{x}$ 永遠落在 $\mathbf{C}(A)$ 中（$\mathbb{R}^m$ 內的子空間）
> **互動梗概：** 一邊拉 $\mathbf{x}$ 各分量、一邊在 3D 視窗即時顯示 $A\mathbf{x}$ 端點 + 已掃過的軌跡（漸層淡化），顯示「軌跡完全落在某個平面內」
> **詳見劇本：** VizScript-04（章末，輕量版）

---

#### Figure 3.2: 向量乘以矩陣的兩種視角（Vector × Matrix — (vM1), (vM2)）

**圖檔：** `docs/book/figs-png/VectorTimesMatrix.png`（原始 EPS：`figs/VectorTimesMatrix.eps`）
**原書頁碼：** p.3
**所屬章節：** §3

##### 視覺結構 (Visual Structure)

此圖採「**上下並列兩區**」結構（與 Figure 3.1 的左右並列形成轉置對應），**上半 (vM1) 行向量點積**、**下半 (vM2) 行向量線性組合**。

- **上半：(vM1) 行向量點積方式**
  - 左上角小灰圈內標 `vM1`，標示視角編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **粉紅色橫條** —— 行向量 $\mathbf{y}$（橫躺）。
    2. **綠色直條 × 2 條** 並列在大方框內 —— 表示 $A$ 的 2 個直立列。
    3. **粉紅色橫條** 中含 2 個被綠覆蓋的小區段 —— 表示產出的行向量 $\mathbf{y}A$，2 個分量各是「$\mathbf{y}$ · 該直立列」的 dot product。
  - 右側文字：**"A row vector $\mathbf{y}$ is multiplied by the two column vectors of $A$ and become the two dot-product elements of $\mathbf{y}A$."**
  - 具體範例（下方）：
    $$\mathbf{y}A = \begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} = \begin{bmatrix} (y_1 + 3y_2 + 5y_3) & (2y_1 + 4y_2 + 6y_3) \end{bmatrix}$$
- **下半：(vM2) 行向量線性組合方式**
  - 左上角小灰圈內標 `vM2`。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **3 個藍色實心圓點** 橫排在小方框內 —— 表示 $\mathbf{y}$ 的三個分量（$y_1, y_2, y_3$）。
    2. **粉紅色橫條 × 3 條** 堆疊在大方框內 —— 表示 $A$ 的 3 個橫躺行。
    3. 在 `=` 右側出現 **3 個項相加**的結構：「藍點 × 粉紅橫條 + 藍點 × 粉紅橫條 + 藍點 × 粉紅橫條」 —— 表示 $\mathbf{y}$ 的每個分量分別縮放 $A$ 的每一橫躺行，再相加。
  - 右側文字：**"The product $\mathbf{y}A$ is a linear combination of the row vectors of $A$."**
  - 具體範例（下方）：
    $$\mathbf{y}A = \begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} = y_1 \begin{bmatrix} 1 & 2 \end{bmatrix} + y_2 \begin{bmatrix} 3 & 4 \end{bmatrix} + y_3 \begin{bmatrix} 5 & 6 \end{bmatrix}$$
- **配色語意（沿用）：** 綠 / 粉紅 / 藍點 / 灰，**配色與 Figure 3.1 完全一致**（讀者跨圖認知不需重學）。
- **與 Figure 3.1 的對偶結構：**
  - 上下兩區的「主角形狀」與 Figure 3.1 完全鏡像：(vM1) 主角是**直立綠**（$A$ 攤成 2 個直立列）、(vM2) 主角是**橫躺粉紅**（$A$ 攤成 3 個橫躺行）。
  - 兩張圖合看會發現：**右乘 (Mv*)** 把焦點放在「結果落在 $\mathbb{R}^m$」、**左乘 (vM*)** 把焦點放在「結果落在 $\mathbb{R}^{1 \times n}$」。

讀者的視覺動線：因為已經看過 Figure 3.1，這張圖可以快讀 — 重點不是學新內容，而是**確認對偶結構** + **建立「左乘 ↔ 右乘 = 行 / 列鏡像」直覺**。

##### 數學內容 (Mathematical Content)

**設定：** $\mathbf{y} = \begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix} \in \mathbb{R}^{1 \times 3}$，$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（與 Figure 3.1 同矩陣）。

**(vM1) 點積展開：**

$$
\mathbf{y}A \;=\; \begin{bmatrix} \mathbf{y} \cdot \mathbf{a}_1 & \mathbf{y} \cdot \mathbf{a}_2 \end{bmatrix} \;=\; \begin{bmatrix} y_1 + 3y_2 + 5y_3 & 2y_1 + 4y_2 + 6y_3 \end{bmatrix}
$$

**(vM2) 線性組合展開：**

$$
\mathbf{y}A \;=\; y_1 \mathbf{a}^*_1 + y_2 \mathbf{a}^*_2 + y_3 \mathbf{a}^*_3 \;=\; y_1 \begin{bmatrix} 1 & 2 \end{bmatrix} + y_2 \begin{bmatrix} 3 & 4 \end{bmatrix} + y_3 \begin{bmatrix} 5 & 6 \end{bmatrix}
$$

**形狀運算：** $(1 \times 3)(3 \times 2) = (1 \times 2)$。

**行空間具體呈現：** 任何 $\mathbf{y}A$ 都可寫成 3 個橫躺行 $(1,2), (3,4), (5,6)$ 的線性組合，即 $\mathbf{C}(A^{\mathrm{T}}) = \operatorname{span}\{(1,2), (3,4), (5,6)\} \subset \mathbb{R}^2$（注意這 3 個橫躺行所在空間是 $\mathbb{R}^2$）。但 3 個 2 維向量必線性相依（最多 2 個獨立），可驗證 $(3,4) = 2(1,2) + (1,0) \cdot \cdots$（不太對；正確的關係見下）。實際上 $\dim \mathbf{C}(A^{\mathrm{T}}) = r = 2$（與列空間同維） — $\mathbf{C}(A^{\mathrm{T}}) = \mathbb{R}^2$ 整個平面。

##### 直覺解讀 (Intuition)

**1. 結構完全平行於 Figure 3.1。** 把 Figure 3.1 整張圖「**轉置一下**」（行 ↔ 列、左右並列 → 上下並列），就得到 Figure 3.2。所有概念（點積方式 / 線性組合方式 / 結果空間 / 等等）一對一對應。**讀通 Figure 3.1 後，Figure 3.2 約 30 秒就能 internalize。**

**2. 為何要區分左乘 / 右乘？** 在抽象代數裡，矩陣乘法不滿足交換律（$A\mathbf{x} \ne \mathbf{x}A$ 一般而言形狀都不同），所以「從哪邊乘」決定了：
- **產物形狀：** $A\mathbf{x}$ 是列向量、$\mathbf{y}A$ 是行向量。
- **所連接的子空間：** $A\mathbf{x}$ 連到 $\mathbf{C}(A)$（列空間）、$\mathbf{y}A$ 連到 $\mathbf{C}(A^{\mathrm{T}})$（行空間）。

**3. 工程實作為何需要兩個視角？** Python / NumPy 預設用列向量，PyTorch 卻習慣把 batch 維度放最前，**矩陣等價於從左乘**。傳統線性代數教科書多用右乘（$A\mathbf{x} = \mathbf{b}$），深度學習論文常用左乘（$\mathbf{y} = \mathbf{x}W$）。本章兩種視角都要熟練，才能無痛切換不同教材 / 框架。

**4. 對偶證明的便利。** 「列空間維度 = 行空間維度」（即「row rank = column rank」）這個經典定理，從 (Mv2) + (vM2) 對偶就有自然證明：(Mv2) 告訴你 $\dim \mathbf{C}(A) = r$ 個獨立直立列 ⟺ (vM2) 告訴你經過某種行操作後也是 $r$ 個獨立橫躺行（細節見 Strang §3.4）。

**常見誤解警示：**
- **「左乘和右乘的『點積方式』看似都是 dot，但 dot 的對象不同」** — (Mv1) 是 $A$ 的橫躺行 · $\mathbf{x}$，(vM1) 是 $\mathbf{y}$ · $A$ 的直立列。對象從「行 vs 列」換到「行 vs 列」（看似一樣但角色互換）。
- **「行向量 $\mathbf{y}$ 與列向量 $\mathbf{y}^{\mathrm{T}}$ 可以互換」** — 數值資料同，但乘法位置不同：$\mathbf{y}A$ 需要橫躺、$A\mathbf{y}^{\mathrm{T}}$ 需要直立。**記得在程式裡管好 shape（`y.reshape(1,-1)` vs `y.reshape(-1,1)`）。**

**為什麼這張圖該做成互動視覺化？** 因為它與 Figure 3.1 的對偶結構是「**值得用一個動畫一次演完**」的點 — 看著 (Mv*) 和 (vM*) 同步切換，建立「左 / 右乘 = 行 / 列鏡像」直覺。但獨立 Figure 3.2 視覺化的價值次於 Figure 3.1，所以本書設計上把它合進 VizMark-01（與 Mv 共用畫面）或單獨做個輕量 VizMark（見 VizMark-03）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-03** [切換視角] ⭐⭐
> **位置：** Figure 3.2 / §3 / (vM1) ↔ (vM2) 對偶（與 Mv 鏡像）
> **核心概念：** 左乘 $\mathbf{y}A$ 的兩種視角結構完全對偶於右乘 $A\mathbf{x}$，行 / 列角色互換
> **互動梗概：** 與 VizMark-01 共畫面但 toggle 切到「左乘模式」 — 整個畫面從「向量在右上」翻轉到「向量在左下」，所有色塊（行 / 列）旋轉 90°
> **詳見劇本：** VizScript-03（章末）

---

#### Figure 3.3: 四個基本子空間（The Four Subspaces）

**圖檔：** `docs/book/figs-png/4-Subspaces.png`（原始 EPS：`figs/4-Subspaces.eps`）
**原書頁碼：** p.3（圖以 8cm 寬呈現）
**所屬章節：** §3 結尾

##### 視覺結構 (Visual Structure)

此圖採「**左右兩塊大空間 + 中央上方箭頭**」結構，是本章（也是全書）視覺上最具標誌性的一張圖，俗稱「**Strang 兩塊大餅圖**」。

- **整體佈局：**
  - **中央上方：** 箭頭從左指向右，箭頭上方文字 $A \in \mathbb{R}^{m \times n}$，箭頭兩端分別標 $\mathbb{R}^n$（左）、$\mathbb{R}^m$（右）。
  - **左方塊：** 在 $\mathbb{R}^n$ 中的兩個子空間。
  - **右方塊：** 在 $\mathbb{R}^m$ 中的兩個子空間。
- **左方塊（$\mathbb{R}^n$）：**
  - **上半大區（傾斜長方形）：行空間 $\mathbf{C}(A^{\mathrm{T}})$**
    - 標籤：**$\mathbf{C}(A^{\mathrm{T}})$**、$\dim = r$
    - 內含文字 "row space"、"all $\mathbf{y}A$"
    - 區內畫**3 條粉紅色橫條**（對應 $A$ 的 3 個橫躺行作為行空間的生成元）。
  - **下半小區（傾斜小方形）：零空間 $\mathbf{N}(A)$**
    - 標籤：**$\mathbf{N}(A)$**、$\dim = n - r$
    - 內含文字 "nullspace"、"$A\mathbf{x} = \mathbf{0}$"
    - 區內無色塊填充（強調這是「會被 $A$ 抹平」的方向）。
  - **兩區交接處：** 直角符號 + 文字 "perpendicular"（**正交**）。
- **右方塊（$\mathbb{R}^m$）：**
  - **上半大區（傾斜長方形）：列空間 $\mathbf{C}(A)$**
    - 標籤：**$\mathbf{C}(A)$**、$\dim = r$
    - 內含文字 "column space"、"all $A\mathbf{x}$"
    - 區內畫**2 條綠色直條**（對應 $A$ 的 2 個直立列作為列空間的生成元）。
  - **下半小區（傾斜小方形）：左零空間 $\mathbf{N}(A^{\mathrm{T}})$**
    - 標籤：**$\mathbf{N}(A^{\mathrm{T}})$**、$\dim = m - r$
    - 內含文字 "left nullspace"、"$\mathbf{y}A = 0$"
    - 區內無色塊填充。
  - **兩區交接處：** 直角符號 + 文字 "perpendicular"。
- **底部正交分解公式：**
  - 左下：**$\mathbb{R}^n = \mathbf{N}(A) + \mathbf{C}(A^{\mathrm{T}})$**、**$\mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}})$**
  - 右下：**$\mathbb{R}^m = \mathbf{C}(A) + \mathbf{N}(A^{\mathrm{T}})$**、**$\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}})$**
- **配色語意：**
  - **粉紅色橫條（$\mathbf{C}(A^{\mathrm{T}})$ 內）** = 橫躺行的家。
  - **綠色直條（$\mathbf{C}(A)$ 內）** = 直立列的家。
  - **兩個零空間區無色** = 「被擠到角落、會被抹平」的方向。
  - **方塊傾斜畫法** = 提示這些子空間不必對齊座標軸，是一般子空間。

讀者的視覺動線：先看中央上方的「$\mathbb{R}^n \xrightarrow{A} \mathbb{R}^m$」確認 $A$ 是函數 → 看左方塊知道「在 $\mathbb{R}^n$ 中，$\mathbf{x}$ 可分解成行空間部分 + 零空間部分」→ 看右方塊知道「在 $\mathbb{R}^m$ 中，輸出 $A\mathbf{x}$ 必落在列空間，左零空間是右側『額外』的維度」→ 對比兩塊的「大區 = 列空間 / 行空間」配色（綠 / 粉紅）強化「直立 vs 橫躺」記憶 → 底部公式收尾。

##### 數學內容 (Mathematical Content)

**四個子空間的精確定義與維度：**

| 子空間 | 符號 | 在哪個 $\mathbb{R}$ 裡 | 維度 | 生成元 |
|---|---|---|---|---|
| 列空間 (column space) | $\mathbf{C}(A)$ | $\mathbb{R}^m$ | $r$ | $A$ 的直立列（取最大線性獨立子集） |
| 零空間 (nullspace) | $\mathbf{N}(A)$ | $\mathbb{R}^n$ | $n - r$ | $A\mathbf{x} = \mathbf{0}$ 的所有解 |
| 行空間 (row space) | $\mathbf{C}(A^{\mathrm{T}})$ | $\mathbb{R}^n$ | $r$ | $A$ 的橫躺行（取最大線性獨立子集） |
| 左零空間 (left nullspace) | $\mathbf{N}(A^{\mathrm{T}})$ | $\mathbb{R}^m$ | $m - r$ | $\mathbf{y}A = \mathbf{0}$ 的所有解 |

**正交互補（基本定理 / Fundamental Theorem of Linear Algebra Part 2）：**

$$
\mathbf{C}(A^{\mathrm{T}}) \;=\; \mathbf{N}(A)^\perp, \qquad \mathbf{C}(A) \;=\; \mathbf{N}(A^{\mathrm{T}})^\perp
$$

且兩個方向皆有**直和分解 (orthogonal direct sum decomposition)**：

$$
\mathbb{R}^n \;=\; \mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A), \qquad \mathbb{R}^m \;=\; \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}})
$$

**正交性的兩行證明：**
- 設 $\mathbf{v} \in \mathbf{N}(A)$ 則 $A\mathbf{v} = \mathbf{0}$。把這個式子展開（用 Mv1 視角）：$A$ 每一橫躺行 $\mathbf{a}^*_i$ 與 $\mathbf{v}$ 的點積為 0，所以 $\mathbf{v} \perp$ 任一橫躺行。因為行空間由橫躺行張成，$\mathbf{v} \perp \mathbf{C}(A^{\mathrm{T}})$。 ✓
- 對偶：$\mathbf{y} \in \mathbf{N}(A^{\mathrm{T}})$ → $\mathbf{y}A = 0$ → $\mathbf{y}$ 與 $A$ 每一直立列點積為 0 → $\mathbf{y} \perp \mathbf{C}(A)$。 ✓

**維度關係（Rank-Nullity Theorem）：**

$$
\dim \mathbf{C}(A) + \dim \mathbf{N}(A) \;=\; n \quad (\text{由秩 } r + (n-r) = n)
$$

$$
\dim \mathbf{C}(A^{\mathrm{T}}) + \dim \mathbf{N}(A^{\mathrm{T}}) \;=\; m \quad (\text{由秩 } r + (m-r) = m)
$$

**關鍵奇蹟（row rank = column rank）：** $\dim \mathbf{C}(A) = \dim \mathbf{C}(A^{\mathrm{T}}) = r$ — 雖然這兩個子空間住在不同維度的空間（$\mathbb{R}^m$ 與 $\mathbb{R}^n$），但**維度恰好相同**。這個事實是線性代數最深刻的對稱之一，是 SVD 的存在性背後的核心（§6.5）。

##### 直覺解讀 (Intuition)

**1. $A$ 是 $\mathbb{R}^n \to \mathbb{R}^m$ 的映射，但它只「看見」一個 $r$ 維的方向。** $\mathbf{x}$ 的「行空間部分」$\mathbf{x}_r \in \mathbf{C}(A^{\mathrm{T}})$ 是 $A$ 真正「處理」的部分（會被映射到 $\mathbf{C}(A)$ 中的某個向量）；$\mathbf{x}$ 的「零空間部分」$\mathbf{x}_n \in \mathbf{N}(A)$ 則被 $A$ **完全抹平**（映射到 $\mathbf{0}$）。

$$
\mathbf{x} \;=\; \underbrace{\mathbf{x}_r}_{\in \mathbf{C}(A^{\mathrm{T}})} + \underbrace{\mathbf{x}_n}_{\in \mathbf{N}(A)}, \qquad A\mathbf{x} \;=\; A\mathbf{x}_r + \underbrace{A\mathbf{x}_n}_{= \mathbf{0}} \;=\; A\mathbf{x}_r
$$

**2. 為什麼右邊 $\mathbf{C}(A)$ 是大區，$\mathbf{N}(A^{\mathrm{T}})$ 是小區？** 因為 $A$ 的「**輸出能力**」就是 $\mathbf{C}(A)$ — 這個子空間維度為 $r$。$\mathbf{N}(A^{\mathrm{T}})$ 是右邊「**$A$ 摸不到的方向**」 — 若 $\mathbf{b} \in \mathbf{N}(A^{\mathrm{T}})$，則任何 $A\mathbf{x}$ 都不等於 $\mathbf{b}$（除非 $\mathbf{b} = \mathbf{0}$），因為它與每一直立列都垂直。$\mathbf{N}(A^{\mathrm{T}})$ 是「**$A\mathbf{x} = \mathbf{b}$ 無解的方向**」。

**3. $A\mathbf{x} = \mathbf{b}$ 的解的結構，全在這張圖裡。**
- **存在性：** $\mathbf{b} \in \mathbf{C}(A)$ ⟺ 有解。等價於 $\mathbf{b}$ 在右方塊上半大區內。
- **唯一性：** 解唯一 ⟺ $\mathbf{N}(A) = \{\mathbf{0}\}$ ⟺ 左方塊下半小區只有原點 ⟺ $r = n$（直立列線性獨立）。
- **若有解但不唯一：** 通解為「一個特解 $\mathbf{x}_p$」+「零空間 $\mathbf{N}(A)$ 中任意向量 $\mathbf{x}_n$」 — 即解集是 $\mathbb{R}^n$ 中與 $\mathbf{N}(A)$ 平行的一個 affine 子空間。

**4. 投影 / 最小二乘 / SVD 都是這張圖的延伸。**
- **投影：** 若 $\mathbf{b} \notin \mathbf{C}(A)$（無解），找 $\mathbf{C}(A)$ 中最接近 $\mathbf{b}$ 的點 $\hat{\mathbf{b}}$ — 等價於把 $\mathbf{b}$ 沿 $\mathbf{N}(A^{\mathrm{T}})$ 方向投到 $\mathbf{C}(A)$。
- **最小二乘解：** $\hat{\mathbf{x}} = (A^{\mathrm{T}}A)^{-1} A^{\mathrm{T}} \mathbf{b}$，本質是把 $\mathbf{b}$ 投影到 $\mathbf{C}(A)$ 後再「逆映射」到 $\mathbf{C}(A^{\mathrm{T}})$。
- **SVD：** $A = U\Sigma V^{\mathrm{T}}$ 直接把這張圖的「兩對正交分解」對齊 — $V$ 的前 $r$ 列構成 $\mathbf{C}(A^{\mathrm{T}})$ 的標準正交基底、$U$ 的前 $r$ 列構成 $\mathbf{C}(A)$ 的標準正交基底（§6.5 詳述）。

**5. 為何稱「**Strang 的兩塊大餅**」？** Gilbert Strang 在 *Linear Algebra and Its Applications* 與 *Linear Algebra for Everyone* 中反覆畫這張圖（不同版本略有差異），把它稱為「**Linear Algebra in a Picture**」 — 因為大多數線性代數核心定理（rank-nullity / fundamental theorem / least squares / SVD）都可以從這張圖直接讀出。在本書 Hiranabe 的版本配色更鮮明，視覺辨識度更高。

**常見誤解警示：**
- **「四個子空間都在 $\mathbb{R}^n$ 或都在 $\mathbb{R}^m$」** — 否，$\mathbb{R}^n$ 中只有 $\mathbf{C}(A^{\mathrm{T}})$ 與 $\mathbf{N}(A)$，$\mathbb{R}^m$ 中只有 $\mathbf{C}(A)$ 與 $\mathbf{N}(A^{\mathrm{T}})$。「列空間」住在「列向量所在的空間」（$\mathbb{R}^m$）才合理。
- **「$\mathbf{C}(A^{\mathrm{T}}) = \mathbf{C}(A)$」** — 否，兩者一個在 $\mathbb{R}^n$ 一個在 $\mathbb{R}^m$，**只有維度相同（都是 $r$）**，子空間本身不同。
- **「零空間是『$A$ 沒有意義的方向』」** — 不嚴謹，正確說法是「$A$ 把它抹平到 $\mathbf{0}$ 的方向」。在最小二乘 / 投影應用中，零空間對應「**不影響輸出的自由度**」（如冗餘參數）。

**為什麼這張圖該做成互動視覺化？** 因為「**拉動 $A$ 的某個元素看四個子空間維度即時變化（並隨秩降低看 $\mathbf{N}(A)$ 從點長成線、列空間從平面塌成線）**」是動態的，遠比靜態圖直觀。另外把 $\mathbf{x}$ 在 $\mathbb{R}^n$ 中拉動、看 $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ 即時分解、再看 $A\mathbf{x}$ 在右方塊跑到哪 — 這個「**雙向跨空間流動動畫**」是線性代數教學最有價值的視覺化之一（見 VizMark-02，本書 ⭐⭐⭐ 第一名）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-02** [3D 空間幾何 + 拉桿調參] ⭐⭐⭐
> **位置：** Figure 3.3 / §3 / 四個基本子空間
> **核心概念：** $\mathbb{R}^n = \mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A)$、$\mathbb{R}^m = \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}})$，兩對正交分解；$\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ 後 $A\mathbf{x} = A\mathbf{x}_r$
> **互動梗概：** 左右兩個 3D 視窗（$\mathbb{R}^3$ as $\mathbb{R}^n$ / $\mathbb{R}^3$ as $\mathbb{R}^m$），中央拉動 $A$ 的元素 slider。左視窗顯示 $\mathbf{C}(A^{\mathrm{T}})$（平面或直線）+ $\mathbf{N}(A)$（補的直線或點）+ 用戶可拖曳的 $\mathbf{x}$ 箭頭即時分解成 $\mathbf{x}_r + \mathbf{x}_n$；右視窗顯示 $\mathbf{C}(A)$ + $\mathbf{N}(A^{\mathrm{T}})$ + $A\mathbf{x}$ 軌跡。秩變化時兩邊子空間維度動畫平滑過渡。
> **詳見劇本：** VizScript-02（章末，⭐⭐⭐ 最詳細版本）

---

### 視覺化劇本（VizScripts）

> 本章 4 個 VizMark 對應 4 個 VizScript。格式遵 `VIZ_SCHEMA.md` §2（A–M 共 13 段）。
> ⭐⭐⭐ 兩支（VizScript-01 / 02）寫到完整 13 段詳細劇本；⭐⭐ 一支（VizScript-03）寫到中等詳度；⭐ 一支（VizScript-04）寫到輕量輪廓即可。
> 4 支劇本可合成單一視覺化頁面（共用控制列與畫布切換 tab），不必拆 4 支獨立程式。

#### VizScript-01: Mv1 ↔ Mv2 視角切換（Dot Way vs Linear Combination Way）

##### A. 一句話定位
讓使用者 toggle 切換 (Mv1) / (Mv2)，看同一個 $A\mathbf{x}$ 同時被「逐橫躺行做點積堆疊」與「直立列加權線性組合」兩種視角呈現。

##### B. 學習目標（Learning Outcome）
- 使用者能說出 (Mv1) $A\mathbf{x}$ 的第 $i$ 個分量是 $A$ 第 $i$ 橫躺行 · $\mathbf{x}$。
- 使用者能說出 (Mv2) $A\mathbf{x} = x_1 \mathbf{a}_1 + \cdots + x_n \mathbf{a}_n$ 是直立列的線性組合。
- 使用者能驗證兩種視角計算的結果完全一致（逐分量比對動畫）。
- 使用者能解釋「(Mv2) 視角告訴我們 $A\mathbf{x}$ 必落在 $\mathbf{C}(A)$」。
- 使用者能在拉 $\mathbf{x}$ 分量時即時觀察「(Mv1) 點積值如何變」與「(Mv2) 列縮放動畫」。

##### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$、列向量 $\mathbf{x} \in \mathbb{R}^n$、結果 $\mathbf{b} = A\mathbf{x} \in \mathbb{R}^m$。
- **預設值：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（與原書 Figure 3 一致）、$\mathbf{x} = (1, 1)^{\mathrm{T}}$、$m = 3$、$n = 2$。
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$。
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1、$x_j \in [-9, 9]$ 步進 1（沿用 §1 §2）。
- **退化情形：**
  - **$\mathbf{x} = \mathbf{0}$：** 結果全 0，兩種視角都示範「點積全 0」與「線性組合係數全 0」。
  - **某 $x_j = 0$：** (Mv2) 對應的直立列「縮放係數 0」灰掉。
  - **$A$ 某直立列為零：** 該列不參與 (Mv2) 加總；視角切換時該列灰底。
  - **$A$ 秩 < $n$：** 在資訊區提示 "rank deficient: 列空間維度 = ?"。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 70% 主畫面、下 30% 控制列 + 公式區。
- **主畫面尺寸：** 900×480 px，白底；分割成「左 35%（$A$ 與 $\mathbf{x}$）+ 中 10%（`=`）+ 右 35%（結果 $\mathbf{b}$）+ 右側 20%（資訊框）」。
- **(Mv1) 模式排列：**
  - 左 35%：$A$ 顯示為 $m$ 條粉紅色橫條堆疊（每條 240×40 px、間隔 8px），右側緊鄰綠色直條 $\mathbf{x}$（80×$m\cdot 48$ px）。
  - 中 10%：大號 `=` 等號。
  - 右 35%：結果列向量 $\mathbf{b}$，畫成 $m$ 條粉紅色橫條，每條中段（綠色覆蓋部分）顯示計算數值。
- **(Mv2) 模式排列：**
  - 左 35%：$A$ 顯示為 $n$ 條綠色直條並列（每條 48×240 px、間隔 8px），上方緊鄰 $n$ 個藍色實心圓點橫排 $\mathbf{x}$。
  - 中 10%：大號 `=` 等號。
  - 右 35%：拆成「藍點 × 綠直條 + 藍點 × 綠直條 + ...」共 $n$ 項，每兩項間用大 `+` 號連接；最右側出現「= 結果列向量」的綠直條 + 數值。
- **資訊框（右側 20%）：**
  - 上半：當前模式 badge（"Mv1: Dot Product Way" / "Mv2: Linear Combination Way"），底色綠 / 藍切換。
  - 中半：當前算式逐分量展開（用 MathJax 即時渲染）。
  - 下半：「列空間提示」`A·x always lies in C(A) ⊂ R^m`（綠字，僅 (Mv2) 模式顯示）。
- **配色：** 沿用全書錨點 — 綠 `#2ca02c`（列 / 直立）、粉紅 `#d62728`（行 / 橫躺）、藍點 `#1f77b4`（$\mathbf{x}$ 分量）、灰 `#eeeeee`（背景填充）、文字 `#000`。
- **字型 / 字級：** 公式區 16pt MathJax、cell 內數字 14pt monospace、模式 badge 18pt sans bold、提示 12pt sans。
- **邊距：** 上下 20px、左右 24px、cell 間距 4px。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 | toggle | Mv1 / Mv2 | Mv1 | 即時（含 600ms 動畫過渡） |
| $m$ | slider | [2, 6] step 1 | 3 | 即時 |
| $n$ | slider | [2, 6] step 1 | 2 | 即時 |
| $a_{ij}$ ($i\!=\!1..m$, $j\!=\!1..n$) | slider grid ($m \times n$) | [-9, 9] step 1 | 原書值 | 即時 |
| $x_j$ ($j\!=\!1..n$) | slider 橫排 | [-9, 9] step 1 | $(1, 1, \ldots)$ | 即時 |
| 公式逐項高亮 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click → 還原預設 |

##### F. 輸出畫面細節（Outputs）
- **(Mv1) 模式輸出：**
  - 結果區每一橫躺行中段顯示「$\sum_{k=1}^{n} a_{ik} x_k$」具體數字（如「$1 \cdot 1 + 2 \cdot 1 = 3$」），公式區同步逐項展開。
  - hover 結果某行 → 對應 $A$ 該橫躺行 + $\mathbf{x}$ 整條 highlight 加粗外框，視覺連結「這個分量來自哪個 dot product」。
- **(Mv2) 模式輸出：**
  - 中段 `=` 右側依序顯示 `$x_1$ × [$\mathbf{a}_1$] + $x_2$ × [$\mathbf{a}_2$] + ...`，每項中綠直條長度按 $|x_j|$ 等比例縮放、$x_j < 0$ 時直條翻轉並底色變淺；最後一項後面接「`=`」與結果綠直條。
  - hover 某項 $x_j \mathbf{a}_j$ → 該項加粗、其他項半透明 0.3；右側結果區也同步以該項顏色「箭頭尾接頭」動畫畫一段。
- **公式區：** 即時 LaTeX，$A\mathbf{x} = \cdots$（依模式顯示 Mv1 或 Mv2 展開）。

##### G. 互動行為（Interactions）
- **toggle Mv1 ↔ Mv2：** 觸發轉視角動畫（見 §H）；公式區同步切換。
- **拉動 $a_{ij}$ slider：** 立即重算結果。(Mv1) 模式下對應第 $i$ 橫躺行內第 $j$ 個元素亮一下；(Mv2) 模式下對應第 $j$ 直立列內第 $i$ 元素亮一下。
- **拉動 $x_j$ slider：**
  - (Mv1) 模式：所有橫躺行的點積結果同時重算，結果分量用淡黃色閃 200ms。
  - (Mv2) 模式：第 $j$ 直立列的「縮放動畫」即時放大 / 縮小（高度按 $|x_j| / 9 \cdot 240$ px 縮放），最終結果直條同步重畫。
- **hover cell / hover 結果分量：** 見 §F。
- **快捷鍵：** `1` → Mv1、`2` → Mv2、`Space` → toggle、`R` → reset、`H` → 公式逐項高亮 toggle。

##### H. 動畫腳本（Mv1 ↔ Mv2 視角切換）
- **從 Mv1 → Mv2：**
  - **t=0：** Mv1 穩態（$A$ 顯為粉紅橫條堆、$\mathbf{x}$ 為綠直條）。
  - **t=0–200ms：** 結果區所有粉紅橫條 fade out（opacity 1 → 0）。
  - **t=200–500ms：** 左區的 $A$ 從「橫躺行堆疊」翻轉成「直立列並列」 — 動畫實作上是把每一橫躺行的色塊**旋轉 90° + 換色（粉紅 → 綠）**，同時 $\mathbf{x}$ 從右側「直立綠」**旋轉 90° + 換色（綠 → 藍點橫排）**移到 $A$ 上方。
  - **t=500–800ms：** 右區依次淡入 $n$ 個 `$x_j$ × 綠直條` 項（每項 stagger 60ms 從中心放大到正常大小），各項之間 `+` 號淡入。
  - **t=800ms 後：** Mv2 穩態。
- **從 Mv2 → Mv1：** 反向重播。
- **總長度：** 800ms。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **暫停 / 倒轉：** 是（動畫進行中按 toggle 立即 reverse；按 Esc 凍結在當前 frame）。

##### I. 邊界與錯誤處理
- **$m = n = 6$ 大尺寸：** 直條 / 橫條尺寸自動縮為 36×120 px；slider grid 改為可摺疊 panel 避免擠版。
- **動畫進行中再切換：** debounce 100ms 或佇列；防止狀態錯亂。
- **$\mathbf{x} = \mathbf{0}$：** 結果區所有元素顯示 `0`，背景轉淡灰；(Mv2) 模式下所有藍點變灰、所有直條變淺。
- **$A$ 某直立列全 0：** (Mv2) 該列灰掉並顯示「dead column → 不貢獻列空間」；(Mv1) 該列下的所有 $a_{ij}$ slider 標 `0` 灰底。
- **拖動 slider 過快：** debounce 30ms 避免重畫風暴；動畫 throttle 至 60fps。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - Mv1 toggle：「每一橫躺行各自做 dot product，堆成結果」
  - Mv2 toggle：「$\mathbf{x}$ 的每個分量縮放對應直立列，疊加成結果 — 這就是『$A\mathbf{x}$ 在 $\mathbf{C}(A)$ 內』的證明」
  - 公式逐項高亮 checkbox：「滑鼠移到某項，自動 highlight 對應的色塊與分量」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 Mv1：每條粉紅橫躺行是 $A$ 的一行，與綠色直立 $\mathbf{x}$ 做 dot product」
  - Step 2：「右邊結果的每個粉紅橫條中段顯示 dot product 數值 — 共 $m$ 個分量」
  - Step 3：「按右下 toggle 切到 Mv2」
  - Step 4：「現在 $A$ 攤成 $n$ 個直立列，$\mathbf{x}$ 的每個分量決定『該列要放大幾倍』」
  - Step 5：「右邊把 $n$ 個放大後的列『箭頭尾接頭』加起來 — 永遠落在 $A$ 的列空間 $\mathbf{C}(A)$」
  - Step 6：「拉 $x_1$ slider 看看第 1 個直立列同步縮放，感受『線性組合』的動態」
- **常見誤解警示：**
  - 「Mv1 和 Mv2 不是不同的『算法』，是同一個運算的兩種讀法」
  - 「Mv2 的『線性組合係數』就是 $\mathbf{x}$ 本身，不需另外算」
- **延伸閱讀：** 原書 p.3、`ch03-mat-vec.md` 數學要點、Strang LAFE Sec. 1.1 + 1.3。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo（反應式 notebook）+ matplotlib + `matplotlib.animation.FuncAnimation`（控制視角切換動畫）+ marimo.ui。
- **替代方案：** Streamlit + Plotly + custom JS（如需高品質瀏覽器分享，旋轉換色用 CSS transform + filter）。
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫粉紅橫條 / 綠直條
  - `matplotlib.transforms.Affine2D().rotate_deg_around()` 做橫 ↔ 直旋轉
  - `marimo.ui.slider`、`marimo.ui.switch`（toggle）、`marimo.ui.array`（slider grid）
  - `numpy.dot(A, x)` 計算結果
- **檔案結構：**
  ```
  viz/
    ch03_matrix_vector.py        # 主入口（含 VizScript-01 / 02 / 03 / 04 共用畫面 tab 切換）
    _common/
      palette.py                 # 沿用 §1 §2 配色
      vector_canvas.py           # §2 已建，§3 直接 import
      subspace_3d.py             # 新增：3D 子空間繪製（給 VizScript-02 用）
  ```
- **效能：** 動畫期間預先計算所有 frame 的色塊座標 / 顏色，存 list；動畫結束後切回 reactive。Slider 拖動以 30ms debounce。
- **測試：** 動畫關鍵 frame（t=0 / 200 / 500 / 800）各 1 張 snapshot；預設值 Mv1 / Mv2 各 1 張靜態 snapshot；退化（$\mathbf{x} = \mathbf{0}$）1 張。

##### L. 驗收標準（Acceptance Criteria）
- [ ] Mv1 ↔ Mv2 toggle 動畫總長 ≤ 800ms，60fps 無 frame drop。
- [ ] 拉 $x_j$ slider 在 (Mv2) 模式下，第 $j$ 直立列縮放動畫 200ms 平滑完成。
- [ ] hover 結果分量 → 對應 $A$ 行 / 列正確高亮（Mv1 高亮整橫躺行、Mv2 高亮整直立列）。
- [ ] 公式區 LaTeX 渲染 < 50ms 完成。
- [ ] $\mathbf{x} = \mathbf{0}$ 或 $A$ 某直立列為 0 時顯示對應退化提示。
- [ ] Walkthrough 6 步驟首次開啟自動觸發，可關閉並有「再看一次」按鈕。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純並列兩種視角靜態圖，無動畫。
- **Tier 3 擴充：** + 加 3D 視窗即時畫 $A\mathbf{x}$ 在 $\mathbf{C}(A)$ 平面上的位置（與 VizScript-04 部分合併）。
- **估時：** 1.5 session（含測試與 walkthrough）

---

#### VizScript-02: 四個基本子空間互動式（Four Subspaces Interactive — Strang's Big Picture）

##### A. 一句話定位
左右兩個 3D 視窗分別展示 $\mathbb{R}^n$ 與 $\mathbb{R}^m$ 中的「行空間 ⊕ 零空間」與「列空間 ⊕ 左零空間」，使用者拖曳 $\mathbf{x}$ 看 $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ 即時分解、$A\mathbf{x}$ 在右視窗即時定位，並可拉 $A$ 元素看子空間維度隨秩變化。

##### B. 學習目標（Learning Outcome）
- 使用者能指認 $\mathbb{R}^n$ 中「行空間 $\mathbf{C}(A^{\mathrm{T}})$」與「零空間 $\mathbf{N}(A)$」兩個正交互補子空間。
- 使用者能指認 $\mathbb{R}^m$ 中「列空間 $\mathbf{C}(A)$」與「左零空間 $\mathbf{N}(A^{\mathrm{T}})$」兩個正交互補子空間。
- 使用者能驗證 $\dim \mathbf{C}(A) = \dim \mathbf{C}(A^{\mathrm{T}}) = r$（即使所在空間不同）。
- 使用者能在拖曳 $\mathbf{x}$ 時看出 $\mathbf{x}_r \in \mathbf{C}(A^{\mathrm{T}})$、$\mathbf{x}_n \in \mathbf{N}(A)$，並 $A\mathbf{x} = A\mathbf{x}_r$（零空間部分被抹平）。
- 使用者能在拉 $A$ 元素降秩時看出列空間從平面塌成直線、零空間從點 / 線長成線 / 面（維度補償）。
- 使用者能說出「為什麼右方塊上半（$\mathbf{C}(A)$）這麼重要 — 因為它是『$A\mathbf{x} = \mathbf{b}$ 有解 ⟺ $\mathbf{b}$ 在這裡』的關鍵」。

##### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$（限 $m, n \in \{2, 3\}$ 以便 3D 視覺化），$\mathbf{x} \in \mathbb{R}^n$，$\mathbf{x}_r \in \mathbf{C}(A^{\mathrm{T}})$，$\mathbf{x}_n \in \mathbf{N}(A)$，$A\mathbf{x} \in \mathbf{C}(A)$，4 個子空間（每個是 $\mathbb{R}^n$ / $\mathbb{R}^m$ 中的直線 / 平面 / 點）。
- **預設值：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（$m=3, n=2$，秩 = 2），$\mathbf{x} = (1, 1)^{\mathrm{T}}$。預設秩 = 2 讓零空間是 $\{\mathbf{0}\}$、$\mathbf{C}(A^{\mathrm{T}}) = \mathbb{R}^2$（整個左視窗平面）、$\mathbf{C}(A)$ 是 $\mathbb{R}^3$ 中的某個平面。
- **維度範圍：** $m \in \{2, 3\}$、$n \in \{2, 3\}$。
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1。
- **退化情形：**
  - **$A = 0$：** 全部子空間退化（$\mathbf{C}(A) = \{0\}$、$\mathbf{N}(A) = \mathbb{R}^n$ 整個），動畫平滑塌縮。
  - **$r = 1$：** $\mathbf{C}(A)$ 是直線、$\mathbf{N}(A)$ 維度增為 $n-1$。
  - **$\mathbf{x} \in \mathbf{N}(A)$：** $A\mathbf{x} = \mathbf{0}$，右視窗 $A\mathbf{x}$ 標籤標 "annihilated"。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 75%（左 45% 左視窗 + 中 10% 連接動畫 + 右 45% 右視窗）+ 下 25% 控制列。
- **左視窗（$\mathbb{R}^n$，3D matplotlib axes）：** 600×480 px，背景白；座標軸標 $e_1, e_2, e_3$（若 $n=3$）；行空間 $\mathbf{C}(A^{\mathrm{T}})$ 以**粉紅色半透明平面 / 直線**繪製、零空間 $\mathbf{N}(A)$ 以**灰色虛線直線 / 點**繪製；用戶拖曳的 $\mathbf{x}$ 為**藍色箭頭**從原點出發、分解後的 $\mathbf{x}_r$（粉紅實心箭頭）與 $\mathbf{x}_n$（灰色虛線箭頭）平行四邊形連接。
- **右視窗（$\mathbb{R}^m$，3D matplotlib axes）：** 600×480 px，同樣設定；列空間 $\mathbf{C}(A)$ 以**綠色半透明平面 / 直線**繪製、左零空間 $\mathbf{N}(A^{\mathrm{T}})$ 以**灰色虛線**繪製；結果 $A\mathbf{x}$ 為**藍色箭頭**從原點出發、其端點與 $\mathbf{x}_r$ 經 $A$ 映射的位置一致。
- **中央連接（10%）：** 上方文字 $A$ 與箭頭 $\to$；中段顯示「$\mathbf{x} \mapsto A\mathbf{x}$」與「$\mathbf{x}_n \mapsto \mathbf{0}$」兩條動畫光線（拖曳時 $\mathbf{x}$ 沿光線從左飛到右）。
- **控制列（下 25%）：**
  - 左：$A$ 元素 slider grid（$m \times n$ 個）+ $m, n$ slider。
  - 中：模式 radio（"All Subspaces" / "Only $\mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A)$" / "Only $\mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}})$"）。
  - 右：「$\mathbf{x}$ 自動掃描」button（讓 $\mathbf{x}$ 自動轉一圈 360° 看 $A\mathbf{x}$ 在 $\mathbf{C}(A)$ 上的軌跡）+ 「reset」。
- **配色：** $\mathbf{C}(A^{\mathrm{T}})$ 粉紅 `#d62728` alpha 0.3、$\mathbf{C}(A)$ 綠 `#2ca02c` alpha 0.3、$\mathbf{N}(A)$ 與 $\mathbf{N}(A^{\mathrm{T}})$ 灰 `#888888` 虛線、$\mathbf{x}$ 藍 `#1f77b4`、$A\mathbf{x}$ 藍 `#1f77b4`、$\mathbf{x}_r$ 粉紅實心、$\mathbf{x}_n$ 灰虛線、座標軸黑。
- **字型 / 字級：** 子空間標籤 14pt bold sans、座標軸 10pt、控制列 12pt。
- **邊距：** 視窗間距 12px、整體 padding 20px。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| $m$ | radio | 2 / 3 | 3 | 即時 |
| $n$ | radio | 2 / 3 | 2 | 即時 |
| $a_{ij}$ | slider grid | [-9, 9] step 1 | 原書值 | 即時 |
| $\mathbf{x}$（拖曳） | 3D drag | $\mathbb{R}^n$ 中任意 | $(1, 1, 0)$ | 即時 |
| 模式 | radio | All / Left only / Right only | All | 即時 |
| 顯示分解 | checkbox | $\mathbf{x}_r + \mathbf{x}_n$ 平行四邊形 | on | 即時 |
| 自動掃 $\mathbf{x}$ | button | — | — | click → 4 秒 360° 旋轉 |
| 顯示秩 | toggle | on / off | on | 即時 |
| reset | button | — | — | — |

##### F. 輸出畫面細節（Outputs）
- **左視窗：**
  - 行空間平面 / 直線（粉紅）半透明填充。
  - 零空間 / 點 / 直線（灰虛線）。
  - 拖曳的 $\mathbf{x}$ 藍色實心箭頭。
  - $\mathbf{x}_r$ 粉紅實心、$\mathbf{x}_n$ 灰虛線（兩者尾接 $\mathbf{x}$ 端點，組成平行四邊形）。
  - 上方文字 `R^n: dim C(A^T) = r = ?, dim N(A) = n-r = ?`。
- **右視窗：**
  - 列空間平面 / 直線（綠）。
  - 左零空間（灰虛線）。
  - $A\mathbf{x}$ 藍色實心箭頭（端點落在綠色面 / 線內）。
  - 上方文字 `R^m: dim C(A) = r = ?, dim N(A^T) = m-r = ?`。
- **資訊區（中央底部）：** 即時 LaTeX
  - $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$（顯示具體數值）
  - $A\mathbf{x} = A\mathbf{x}_r$（驗證零空間被抹平）
  - $\operatorname{rank}(A) = r$
- **驗證提示：** 動畫顯示「$\mathbf{x}_r \perp \mathbf{x}_n$」「$A\mathbf{x} \perp \mathbf{N}(A^{\mathrm{T}})$」兩個垂直記號。

##### G. 互動行為（Interactions）
- **拖曳 $\mathbf{x}$（左視窗）：**
  - 即時計算 $\mathbf{x}_r = \mathrm{proj}_{\mathbf{C}(A^{\mathrm{T}})}(\mathbf{x})$、$\mathbf{x}_n = \mathbf{x} - \mathbf{x}_r$。
  - 平行四邊形即時重畫。
  - 右視窗 $A\mathbf{x}$ 箭頭即時更新（從 $A\mathbf{x}_r$ 計算 — 因為 $A\mathbf{x}_n = 0$，數值上等同 $A\mathbf{x}$ 但概念上強調「只有 $\mathbf{x}_r$ 部分貢獻」）。
  - 飛行動畫：拖曳暫停 500ms 後，自動播放一個「$\mathbf{x}$ 從左視窗『沿映射光線』飛到右視窗變成 $A\mathbf{x}$」的軌跡動畫（700ms）。
- **拉 $a_{ij}$ slider：** 即時重算秩、所有子空間（粉紅 / 綠平面 / 直線重畫，並用「平面 → 直線」平滑動畫 600ms 表現維度變化）；左 / 右視窗的子空間自動更新標籤。
- **點「自動掃 $\mathbf{x}$」：** $\mathbf{x}$ 在左視窗的 $\mathbf{C}(A^{\mathrm{T}})$ 平面上以單位圓沿著平面繞 360°（4 秒）；右視窗 $A\mathbf{x}$ 同步在 $\mathbf{C}(A)$ 內畫出對應軌跡（橢圓 / 直線）；軌跡淡化保留 2 秒讓使用者看到全貌。
- **模式切換：** 隱藏 / 顯示對應視窗的子空間平面，但保留箭頭。
- **快捷鍵：** `A` 切到「All」、`L` 左視窗 only、`R` 右視窗 only、`Space` 自動掃 $\mathbf{x}$、`0` reset。

##### H. 動畫腳本（秩變化的子空間維度過渡）
- **拉 $a_{ij}$ 導致秩從 $r$ 降到 $r-1$：**
  - **t=0：** $\mathbf{C}(A)$ 是平面（$r=2$ 在 $\mathbb{R}^3$ 中）。
  - **t=0–300ms：** 平面**朝其中一個方向縮窄**（沿 $\mathbf{C}(A)$ 中即將被抹去的方向），最終塌成直線（$r=1$）。實作上：取秩 $r-1$ 的最大線性獨立子集對應的方向作為「保留方向」，朝其他方向縮窄。
  - **t=300–600ms：** 同時左視窗 $\mathbf{N}(A)$ 從點長成直線、右視窗 $\mathbf{N}(A^{\mathrm{T}})$ 從點長成直線（維度補償）。動畫從原點向外擴展。
- **總長度：** 600ms。
- **緩動：** ease-in-out。
- **暫停 / 倒轉：** 是（slider 回拉立即反向動畫）。

##### I. 邊界與錯誤處理
- **$m = n = 3$ 且 $A$ 滿秩：** $\mathbf{C}(A)$ 是整個 $\mathbb{R}^3$（畫成淡綠 alpha 0.15 充滿視窗）、$\mathbf{N}(A^{\mathrm{T}}) = \{\mathbf{0}\}$ 只顯示原點記號。
- **$A = \mathbf{0}$：** 警示文字 "$A$ 為零矩陣 — 所有 $\mathbf{x}$ 都在 $\mathbf{N}(A)$" 出現 3 秒。
- **3D 視窗旋轉 / 縮放：** 拖曳視窗背景（不是箭頭）做相機旋轉；滾輪縮放。預設視角 elevation = 25°、azimuth = -60°。
- **$\mathbf{x}$ 拖出視窗範圍：** 限制 $\|\mathbf{x}\|_\infty \le 9$；超過時箭頭縮回邊界。
- **計算密集（拖動 + 自動掃同時）：** 取消上一個自動掃任務。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - $\mathbf{C}(A^{\mathrm{T}})$ 標籤：「行空間 — 所有 $A$ 橫躺行的線性組合所成的子空間」
  - $\mathbf{N}(A)$ 標籤：「零空間 — 所有滿足 $A\mathbf{x} = \mathbf{0}$ 的 $\mathbf{x}$」
  - $\mathbf{x}_r$ 箭頭：「$\mathbf{x}$ 在行空間中的分量 — 這部分被 $A$ 真正『映射』」
  - $\mathbf{x}_n$ 箭頭：「$\mathbf{x}$ 在零空間中的分量 — 這部分被 $A$ 抹平」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「左邊是 $\mathbb{R}^n$，所有可能的 $\mathbf{x}$ 都住在這裡」
  - Step 2：「粉紅色平面是『行空間 $\mathbf{C}(A^{\mathrm{T}})$』— $A$ 真正『處理』的方向」
  - Step 3：「灰色直線是『零空間 $\mathbf{N}(A)$』— $A$ 把它抹平」
  - Step 4：「拖曳藍色 $\mathbf{x}$ 看它分解成粉紅 $\mathbf{x}_r$ + 灰 $\mathbf{x}_n$」
  - Step 5：「右邊是 $\mathbb{R}^m$，結果 $A\mathbf{x}$ 永遠落在綠色『列空間 $\mathbf{C}(A)$』內」
  - Step 6：「拉 $A$ 的某個元素讓秩降低，看子空間維度動畫切換」
  - Step 7：「按『自動掃 $\mathbf{x}$』，看 $\mathbf{x}$ 繞行空間一圈，$A\mathbf{x}$ 同步在列空間裡跑」
- **常見誤解警示：**
  - 「行空間和列空間不是同一個子空間 — 它們住在不同維度的空間（$\mathbb{R}^n$ vs $\mathbb{R}^m$），但**維度恰好相等**」
  - 「秩 = 行 / 列獨立向量個數 = $\mathbf{C}(A^{\mathrm{T}})$ 維度 = $\mathbf{C}(A)$ 維度」
  - 「零空間和左零空間不對稱 — 一個在 $\mathbb{R}^n$、一個在 $\mathbb{R}^m$」
- **延伸閱讀：** Strang LAFE Sec. 3.5 (p.124) 四子空間維度定理；原書 p.3 Figure 5；本書 §6.5 SVD 把這張圖完整對齊。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib 3D（`mpl_toolkits.mplot3d`）+ marimo.ui + custom drag handler（用 `matplotlib` 的 `mpl_connect('button_press_event', ...)`）。
- **替代方案：** Plotly 3D scatter + surface（互動效能較好；拖曳用 Plotly 的 dash callbacks）。或 Three.js（最高品質但跳脫 Python 生態）。
- **關鍵 API：**
  - `numpy.linalg.matrix_rank(A)` 求秩
  - `numpy.linalg.svd(A)` 取 $U, \Sigma, V^{\mathrm{T}}$ → $V$ 前 $r$ 列為 $\mathbf{C}(A^{\mathrm{T}})$ 標準正交基底、$U$ 前 $r$ 列為 $\mathbf{C}(A)$ 基底、$V$ 後 $n-r$ 列為 $\mathbf{N}(A)$ 基底、$U$ 後 $m-r$ 列為 $\mathbf{N}(A^{\mathrm{T}})$ 基底（**用 SVD 求四子空間基底是最穩定的方法**）
  - `mpl_toolkits.mplot3d.art3d.Poly3DCollection` 畫半透明平面
  - `matplotlib.patches.FancyArrowPatch` 配 `mpl_toolkits.mplot3d.proj3d.proj_transform` 畫 3D 箭頭
  - `scipy.linalg.null_space(A)` 直接求 $\mathbf{N}(A)$ 基底（替代 SVD）
- **檔案結構：** 與 VizScript-01 共用 `viz/ch03_matrix_vector.py`；3D 繪圖工具放 `viz/_common/subspace_3d.py`。
- **效能：**
  - 預先用 SVD 算好基底並 cache；只在 $A$ 變動時重算。
  - 拖曳 $\mathbf{x}$ 時只重畫箭頭，不重畫平面（用 `set_data_3d` 不要 `clear`）。
  - 「自動掃 $\mathbf{x}$」用 `FuncAnimation` 預先計算 60 frames，避免每 frame 算 SVD。
- **測試：**
  - 秩 = 2 / 1 / 0 各畫 1 張 3D snapshot。
  - $\mathbf{x}$ 從預設位置拖到原點過程中 3 個關鍵 frame snapshot（含分解平行四邊形）。
  - 拉 $a_{11}$ 從 1 → 0（不降秩）與 1 → -3（可能降秩）各 1 張動畫關鍵 frame。

##### L. 驗收標準（Acceptance Criteria）
- [ ] 左右視窗 3D 顯示正確：行空間粉紅平面、列空間綠平面、零空間 / 左零空間灰虛線，正交關係視覺正確。
- [ ] 拖曳 $\mathbf{x}$ 時 $\mathbf{x}_r + \mathbf{x}_n$ 分解平行四邊形即時更新 < 50ms。
- [ ] 「飛行動畫」$\mathbf{x} \to A\mathbf{x}$ 軌跡 700ms 平滑無 frame drop。
- [ ] 拉 $a_{ij}$ 降秩時平面塌成直線 / 零空間擴維動畫 600ms 完成且維度數字正確同步。
- [ ] 「自動掃 $\mathbf{x}$」軌跡完全落在綠色列空間內（驗證 $A\mathbf{x} \in \mathbf{C}(A)$）。
- [ ] 維度顯示文字 `dim C(A) = r`、`dim N(A) = n-r` 等四項與實際運算一致。
- [ ] 退化情形（$A = 0$、$r = 0$）正確顯示警示文字並平滑塌縮。
- [ ] Walkthrough 7 步驟首次開啟自動觸發。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 3
- **Tier 1 對應：** 純靜態圖（原書 Figure 5 重現）+ rank 計算結果文字顯示。
- **Tier 2 對應：** Tier 1 + 拖曳 $\mathbf{x}$ 看分解（無 3D 旋轉、無秩動畫）。
- **Tier 3 擴充內容（本劇本目標）：** 完整 3D 雙視窗 + 拖曳 $\mathbf{x}$ + 飛行動畫 + 秩變化平面塌縮 + 自動掃 $\mathbf{x}$ 軌跡。
- **Tier 4 進階擴充：** + 投影 / 最小二乘可視化（拖 $\mathbf{b}$ 不在 $\mathbf{C}(A)$ 內時，顯示沿 $\mathbf{N}(A^{\mathrm{T}})$ 投影到 $\hat{\mathbf{b}}$）— 留給 §6.5 SVD 章節做。
- **估時：** 3 session（含 3D 互動 debug、SVD 基底計算測試、動畫調校）

---

#### VizScript-03: vM1 ↔ vM2 行向量視角切換（Left Multiplication Duality）

##### A. 一句話定位
與 VizScript-01 共畫面但以「左乘 $\mathbf{y}A$」角度呈現，讓使用者在 toggle 「右乘 / 左乘」時看整張畫面行 / 列鏡像翻轉，建立兩種方向的對偶直覺。

##### B. 學習目標
- 使用者能說出 (vM1) 是 $\mathbf{y}$ 與 $A$ 各直立列的點積。
- 使用者能說出 (vM2) 是 $A$ 各橫躺行被 $\mathbf{y}$ 分量縮放後線性組合。
- 使用者能解釋為何 $\mathbf{y}A$ 落在 $\mathbf{C}(A^{\mathrm{T}})$（行空間）。
- 使用者能在 toggle 「右乘 ↔ 左乘」時看出整張畫面行 / 列、上下 / 左右**鏡像翻轉**。

##### C. 待視覺化的數學物件
- 矩陣 $A$（同 VizScript-01）、行向量 $\mathbf{y} \in \mathbb{R}^{1 \times m}$、結果 $\mathbf{z} = \mathbf{y}A \in \mathbb{R}^{1 \times n}$。
- 預設值：$A$ 同 VizScript-01、$\mathbf{y} = (1, 1, 1)$。
- 退化情形：$\mathbf{y} = \mathbf{0}$ → 結果全 0；$\mathbf{y} \in \mathbf{N}(A^{\mathrm{T}})$ → 結果為 0 並標 "annihilated by A^T"。

##### D. 視覺布局
- 與 VizScript-01 共用同一畫面，多加一個頂部 toggle「右乘 $A\mathbf{x}$ / 左乘 $\mathbf{y}A$」。
- (vM1) 模式：$\mathbf{y}$ 橫躺粉紅條在左、$A$ 直立列在右；結果是橫躺粉紅條右端含 $n$ 個 dot product 結果。
- (vM2) 模式：$\mathbf{y}$ 藍點橫排在上、$A$ 橫躺行堆疊在下；結果是 $m$ 項「藍點 × 粉紅橫條」相加 + 結果粉紅橫條。
- 配色完全沿用 VizScript-01。

##### E. 輸入控制
- toggle「右乘 / 左乘」(新增) + (vM1) / (vM2) toggle + $A$ slider grid + $\mathbf{y}$ slider 橫排 + 重設。

##### F. 輸出畫面細節
- (vM1) 結果：橫躺粉紅條，內含 $n$ 個 dot product 數值。
- (vM2) 結果：$m$ 項相加結構，最右側結果橫躺粉紅條。
- 公式區即時顯示 $\mathbf{y}A = ?$。

##### G. 互動行為
- 拉 $\mathbf{y}$ 分量 → 即時重算；(vM2) 模式下對應橫躺行縮放動畫。
- toggle vM1 ↔ vM2 動畫類似 VizScript-01 但軸換 90°（畫面從「上下分」變「左右分」）。

##### H. 動畫腳本
- 與 VizScript-01 共用引擎；vM 模式整體畫面**鏡像翻轉**（上下對換、行 / 列換色），動畫時長 800ms，緩動 ease-in-out。

##### I. 邊界與錯誤處理
- 同 VizScript-01。$\mathbf{y} \in \mathbf{N}(A^{\mathrm{T}})$ 時資訊區紅字提示 "y ∈ left nullspace → yA = 0"。

##### J. 教學支援
- Tooltip：vM1「點積 $\mathbf{y}$ · 直立列」、vM2「行向量縮放加總」。
- Walkthrough 4 步驟：「現在是左乘 vM1 → 切到 vM2 → 拉 $y_1$ 看第 1 橫躺行縮放 → 注意結果落在 $\mathbf{C}(A^{\mathrm{T}})$（與 VizScript-02 左視窗呼應）」。

##### K. 技術實作建議
- 共用 `viz/ch03_matrix_vector.py`；vM 模式只是把 `numpy.dot(A, x)` 換成 `numpy.dot(y, A)` 並把繪圖佈局做 transpose。
- API 同 VizScript-01。

##### L. 驗收標準
- toggle 右乘 ↔ 左乘畫面 800ms 完成翻轉、無布局錯亂。
- 拉 $\mathbf{y}$ slider 結果即時更新 < 50ms。
- $\mathbf{y} = \mathbf{0}$ 顯示退化提示。

##### M. 互動深度 Tier + 估時
- 目標 Tier 2。Tier 1 = 靜態並列 vM1 / vM2。Tier 3 = 與 VizScript-02 左視窗連動，$\mathbf{y}A$ 端點在 $\mathbf{C}(A^{\mathrm{T}})$ 視覺定位。估時 0.5 session（共用 VizScript-01 引擎，只加 transpose 邏輯）。

---

#### VizScript-04: 列空間軌跡掃描（Column Space Trace — Lite）

##### A. 一句話定位
拉 $\mathbf{x}$ 各分量看 $A\mathbf{x}$ 在 3D 空間中的端點即時移動 + 留下漸層淡化軌跡，視覺驗證「軌跡完全落在 $\mathbf{C}(A)$ 平面內」。

##### B. 學習目標
- 使用者能視覺驗證 $A\mathbf{x} \in \mathbf{C}(A)$。
- 使用者能直觀理解 $\mathbf{C}(A)$ 的「2 維 = 平面」「1 維 = 直線」對應 $A$ 不同秩。

##### C. 待視覺化的數學物件
- 同 VizScript-02 右視窗，但簡化版（無左視窗、無分解、無秩變化動畫）。

##### D. 視覺布局
- 單 3D 視窗 600×480 px，顯示 $\mathbb{R}^m$ 中的 $\mathbf{C}(A)$ 半透明綠平面 + $A\mathbf{x}$ 藍色箭頭 + 漸層淡化的歷史軌跡（最近 100 frames）。
- 下方控制列：$\mathbf{x}$ 各分量 slider。

##### E. 輸入控制
- $\mathbf{x}$ slider ($n$ 個)、清除軌跡 button、reset。

##### F. 輸出畫面細節
- $A\mathbf{x}$ 當前位置箭頭（不透明）+ 過往位置（透明度按時間衰減）。
- 軌跡的所有點落在綠平面內（視覺驗證）。

##### G. 互動行為
- 拉 $\mathbf{x}$ → 端點移動 + 留新軌跡點；軌跡 deque(maxlen=100)。
- 清除軌跡 button → 重置軌跡。

##### H. 動畫腳本
- 端點移動有 100ms 平滑插值（避免跳動）。

##### I-M. 簡化版
- 邊界 / 教學 / 實作 / 驗收：類似 VizScript-02 但範圍限縮。
- **目標 Tier：** Tier 1。
- **估時：** 0.5 session（建立在 VizScript-02 子集上）。

---

### 章末延伸

- **後續章節連結：** [→ ch04-mat-mat.md](ch04-mat-mat.md) — §4 矩陣乘以矩陣 (Matrix × Matrix) 有 **4 種視角** (MM1, MM2, MM3, MM4)，正是把本章 (Mv1)(Mv2)(vM1)(vM2) 推廣到矩陣 × 矩陣。本章對偶 + 線性組合直覺是 §4 的直接前置。

- **跨章節結構連結：**
  - **§5 Practical Patterns** 大量使用 (Mv2) 與 (vM2) 線性組合視角（投影 / 排列矩陣 / 旋轉矩陣等）。
  - **§6 五大分解** 每一個都基於「四子空間」結構：CR 把 $A$ 寫成 $\mathbf{C}(A^{\mathrm{T}})$ 與 $\mathbf{C}(A)$ 的對偶連接、QR 是行空間的標準正交化、SVD 把四子空間一次對齊到兩組標準正交基底。

- **延伸閱讀 / 相關概念：**
  - Strang《Linear Algebra for Everyone》Sec. 1.1（線性組合）、Sec. 1.3（矩陣與列空間）、Sec. 3.5（四子空間維度）— 原書直接對應段落。
  - Strang 在 *Linear Algebra and Its Applications* 5th ed. 也有相似 4-Subspaces 圖（俗稱 Strang's Big Picture），版本配色略不同但結構相同。
  - **跨領域類比：**
    - 機器學習：線性回歸 $A\mathbf{x} = \mathbf{b}$ 中，當 $\mathbf{b} \notin \mathbf{C}(A)$（資料不在模型可表達空間）時，最小二乘 $\hat{\mathbf{x}}$ 把 $\mathbf{b}$ 投影到 $\mathbf{C}(A)$，殘差 $\mathbf{b} - A\hat{\mathbf{x}} \in \mathbf{N}(A^{\mathrm{T}})$（與列空間正交）。
    - 信號處理：頻譜濾波本質是把訊號分解到不同子空間（傅立葉基底張成的子空間）。
    - 資料壓縮：主成分分析 (PCA) 把資料投影到 $\mathbf{C}(A)$ 維度最低的方向組合（與 SVD 直接相關）。

- **本章學完後讀者應該能回答：**
  - 一個 $3 \times 2$ 矩陣的列空間 / 行空間 / 零空間 / 左零空間各住在哪個 $\mathbb{R}^?$？維度可能是多少？
  - 為什麼 $A\mathbf{x} = \mathbf{b}$ 「有解」這件事可以直接從子空間角度判斷？
  - (Mv2) 視角與 (Mv1) 視角的計算結果為何相同？兩者各自適合什麼樣的數學推導？

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 69–112 / `The-Art-of-Linear-Algebra.pdf` p.3
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 68–107
- **圖檔：**
  - `figs/MatrixTimesVector.eps` → `docs/book/figs-png/MatrixTimesVector.png`
  - `figs/VectorTimesMatrix.eps` → `docs/book/figs-png/VectorTimesMatrix.png`
  - `figs/4-Subspaces.eps` → `docs/book/figs-png/4-Subspaces.png`
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0

---

## 第 4 章. 矩陣乘以矩陣 — 四種視角（Matrix × Matrix — 4 Ways）

> **原書頁碼：** p.4
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 114–125 行
> **本章圖數：** 1（Figure 4.1，含 MM1 / MM2 / MM3 / MM4 四子圖 2×2 排版）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成 / [ ] 校對中

---

### 章節摘要

矩陣乘以矩陣 $AB = C$ 是「矩陣乘以向量」的自然延伸。同一個結果 $C$ 可以從**四個視角**讀出：**(MM1) 點積方式** — $C$ 的每個元素 $c_{ij}$ 各自是「$A$ 第 $i$ 橫躺行 · $B$ 第 $j$ 直立列」的 dot product；**(MM2) 列線性組合方式** — $C$ 的每一直立列 $\mathbf{c}_j$ 是「$A$ 的直立列以 $B$ 第 $j$ 列為係數的線性組合」；**(MM3) 行線性組合方式** — $C$ 的每一橫躺行 $\mathbf{c}^*_i$ 是「$B$ 的橫躺行以 $A$ 第 $i$ 行為係數的線性組合」；**(MM4) 外積之和方式** — $AB$ 直接拆成 $k$ 個秩 1 矩陣相加（$\mathbf{a}_p$ 列 × $\mathbf{b}^*_p$ 行）。

四種視角對應 §2（向量 × 向量）與 §3（矩陣 × 向量）的不同延伸：**(MM1) ↔ (Mv1) ↔ (v1) 點積家族**；**(MM2) ↔ (Mv2) 列線組家族（從右切看 B）**；**(MM3) ↔ (vM2) 行線組家族（從左切看 A）**；**(MM4) ↔ (v2) 外積家族 — 這條線是 §6 SVD 與 CR 分解的真正鑰匙**。

> ⚠ **本章是 §6 五大分解的「視覺前置」。** §6 所有矩陣分解 ($A = CR$、$A = LU$、$A = QR$、$S = Q\Lambda Q^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$) 都會把右側拆成「兩個 / 三個矩陣相乘」並用 (MM4) 或 (MM2)（取決於分解類型）來重新詮釋成秩 1 累加或列空間重塑。**MM4 視角不熟，後面 SVD 永遠卡住。**

> ⚠ **術語提醒（沿用 §1–§3 全書慣例 — A 派）：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。$A$ 的「第 $j$ 直立列」記作 $\mathbf{a}_j \in \mathbb{R}^m$、「第 $i$ 橫躺行」記作 $\mathbf{a}^*_i \in \mathbb{R}^{1 \times k}$。$B$ 同理。$AB = C$ 的形狀運算 $(m \times k)(k \times n) = (m \times n)$，**中間維度 $k$ 必須對齊**。

---

### 數學要點

設 $A \in \mathbb{R}^{m \times k}$（$m$ 行 $k$ 列）、$B \in \mathbb{R}^{k \times n}$（$k$ 行 $n$ 列）、$C = AB \in \mathbb{R}^{m \times n}$。

矩陣切片符號（沿用 §3）：
- $\mathbf{a}_p \in \mathbb{R}^m$ = $A$ 的第 $p$ 直立列 ($p = 1, \ldots, k$)。
- $\mathbf{a}^*_i \in \mathbb{R}^{1 \times k}$ = $A$ 的第 $i$ 橫躺行 ($i = 1, \ldots, m$)。
- $\mathbf{b}_j \in \mathbb{R}^k$ = $B$ 的第 $j$ 直立列 ($j = 1, \ldots, n$)。
- $\mathbf{b}^*_p \in \mathbb{R}^{1 \times n}$ = $B$ 的第 $p$ 橫躺行 ($p = 1, \ldots, k$)。
- $\mathbf{c}_j$、$\mathbf{c}^*_i$ 同理。

#### (MM1) 點積方式（Element-wise Dot Product Way）

把 $A$ 拆成 $m$ 個橫躺行、$B$ 拆成 $n$ 個直立列，則 $C$ 的每個元素是「行 · 列」點積：

$$
c_{ij}
\;=\;
\mathbf{a}^*_i \cdot \mathbf{b}_j
\;=\;
\sum_{p=1}^{k} a_{ip} \, b_{pj}
\qquad (i = 1, \ldots, m;\ j = 1, \ldots, n)
$$

寫成矩陣方塊形式：

$$
\underbrace{
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix}
}_{A}
\;
\underbrace{
\begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_n \end{bmatrix}
}_{B}
\;=\;
\begin{bmatrix}
\mathbf{a}^*_1 \cdot \mathbf{b}_1 & \mathbf{a}^*_1 \cdot \mathbf{b}_2 & \cdots & \mathbf{a}^*_1 \cdot \mathbf{b}_n \\
\mathbf{a}^*_2 \cdot \mathbf{b}_1 & \mathbf{a}^*_2 \cdot \mathbf{b}_2 & \cdots & \mathbf{a}^*_2 \cdot \mathbf{b}_n \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{a}^*_m \cdot \mathbf{b}_1 & \mathbf{a}^*_m \cdot \mathbf{b}_2 & \cdots & \mathbf{a}^*_m \cdot \mathbf{b}_n
\end{bmatrix}
$$

- **總點積次數：** $m \cdot n$ 個（每個元素 1 次點積，每次點積 $k$ 次乘法 + $(k{-}1)$ 次加法）。
- **直覺：** 「每元素一個點積」 — 這是教科書最熟悉的視角，與 (Mv1) 的「每分量一個點積」一脈相承。
- **原書 (MM1) 範例（$m=3, k=2, n=2$）：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix}
\;=\;
\begin{bmatrix}
(x_1 + 2 x_2) & (y_1 + 2 y_2) \\
(3 x_1 + 4 x_2) & (3 y_1 + 4 y_2) \\
(5 x_1 + 6 x_2) & (5 y_1 + 6 y_2)
\end{bmatrix}
$$

#### (MM2) 列線性組合方式（Column Linear Combination Way）

把 $B$ 拆成 $n$ 個直立列 $\mathbf{b}_1, \ldots, \mathbf{b}_n$，則 $C$ 的每一直立列各自是「$A$ 對 $\mathbf{b}_j$ 的線性組合」（即 (Mv2) 重複 $n$ 次）：

$$
AB \;=\; A \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_n \end{bmatrix} \;=\; \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \cdots & A\mathbf{b}_n \end{bmatrix}
$$

逐列展開：

$$
\mathbf{c}_j \;=\; A \mathbf{b}_j \;=\; b_{1j} \mathbf{a}_1 + b_{2j} \mathbf{a}_2 + \cdots + b_{kj} \mathbf{a}_k
\qquad (j = 1, \ldots, n)
$$

- **直覺：** $B$ 的每一直立列 $\mathbf{b}_j$ 是一份「配方」，告訴你**把 $A$ 的直立列用什麼比例混合**，得到 $C$ 的第 $j$ 直立列。$C$ 的所有直立列因此都落在 $\mathbf{C}(A)$（$A$ 的列空間）裡。
- **原書 (MM2) 範例：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix}
\;=\;
A
\begin{bmatrix} \mathbf{x} & \mathbf{y} \end{bmatrix}
\;=\;
\begin{bmatrix} A\mathbf{x} & A\mathbf{y} \end{bmatrix}
$$

其中 $A\mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 = x_1 (1,3,5)^{\mathrm{T}} + x_2 (2,4,6)^{\mathrm{T}}$。

- **關鍵推論（後續章節依賴）：** $\mathbf{C}(AB) \subseteq \mathbf{C}(A)$ — 乘上任何 $B$ 從右邊，列空間只會「等於或縮小」，永遠不會超出 $A$ 的列空間。

#### (MM3) 行線性組合方式（Row Linear Combination Way）

把 $A$ 拆成 $m$ 個橫躺行 $\mathbf{a}^*_1, \ldots, \mathbf{a}^*_m$，則 $C$ 的每一橫躺行各自是「$\mathbf{a}^*_i$ 對 $B$ 的線性組合」（即 (vM2) 重複 $m$ 次）：

$$
AB \;=\; \begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix} B \;=\; \begin{bmatrix} \mathbf{a}^*_1 B \\ \mathbf{a}^*_2 B \\ \vdots \\ \mathbf{a}^*_m B \end{bmatrix}
$$

逐行展開：

$$
\mathbf{c}^*_i \;=\; \mathbf{a}^*_i B \;=\; a_{i1} \mathbf{b}^*_1 + a_{i2} \mathbf{b}^*_2 + \cdots + a_{ik} \mathbf{b}^*_k
\qquad (i = 1, \ldots, m)
$$

- **直覺：** $A$ 的每一橫躺行 $\mathbf{a}^*_i$ 是一份「配方」，告訴你**把 $B$ 的橫躺行用什麼比例混合**，得到 $C$ 的第 $i$ 橫躺行。$C$ 的所有橫躺行因此都落在 $\mathbf{C}(B^{\mathrm{T}})$（$B$ 的行空間）裡。
- **原書 (MM3) 範例：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix}
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \mathbf{a}^*_3 \end{bmatrix} B
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 B \\ \mathbf{a}^*_2 B \\ \mathbf{a}^*_3 B \end{bmatrix}
$$

其中 $\mathbf{a}^*_1 B = \begin{bmatrix} 1 & 2 \end{bmatrix} B = 1 \cdot (x_1, y_1) + 2 \cdot (x_2, y_2) = (x_1 + 2x_2, \, y_1 + 2y_2)$。

- **關鍵推論：** $\mathbf{C}((AB)^{\mathrm{T}}) \subseteq \mathbf{C}(B^{\mathrm{T}})$ — 行空間只會「等於或縮小」。

#### (MM4) 外積之和方式（Sum of Outer Products / Rank-1 Decomposition Way）— **本章核心**

把 $A$ 拆成 $k$ 個直立列、$B$ 拆成 $k$ 個橫躺行（**注意：拆數 $k$ 是「內維度」，不是 $m$ 或 $n$**），則 $AB$ 等於 $k$ 個外積（秩 1 矩陣）的和：

$$
AB
\;=\;
\begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_k \end{bmatrix}
\begin{bmatrix} \mathbf{b}^*_1 \\ \mathbf{b}^*_2 \\ \vdots \\ \mathbf{b}^*_k \end{bmatrix}
\;=\;
\sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p
\;=\;
\mathbf{a}_1 \mathbf{b}^*_1 + \mathbf{a}_2 \mathbf{b}^*_2 + \cdots + \mathbf{a}_k \mathbf{b}^*_k
$$

每一項 $\mathbf{a}_p \mathbf{b}^*_p$ 都是一個**秩 1 矩陣**（$m \times n$），是 §2 (v2) 外積 → rank 1 結構的**直接重複 $k$ 次**。

- **形狀檢核：** $\mathbf{a}_p \in \mathbb{R}^{m \times 1}$、$\mathbf{b}^*_p \in \mathbb{R}^{1 \times n}$、$\mathbf{a}_p \mathbf{b}^*_p \in \mathbb{R}^{m \times n}$。$k$ 個 $m \times n$ 矩陣相加仍是 $m \times n$。
- **直覺：** 把 $AB$ 看成「**$k$ 個秩 1 圖層疊加**」。當 $k$ 很大時（如 SVD），疊加越多項越接近原矩陣；截斷前幾項即低秩近似。
- **原書 (MM4) 範例（$k = 2$）：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}
\;=\;
\begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \end{bmatrix}
\,+\,
\begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} \begin{bmatrix} b_{21} & b_{22} \end{bmatrix}
$$

展開為兩個秩 1 矩陣：

$$
=\;
\begin{bmatrix} b_{11} & b_{12} \\ 3 b_{11} & 3 b_{12} \\ 5 b_{11} & 5 b_{12} \end{bmatrix}
\,+\,
\begin{bmatrix} 2 b_{21} & 2 b_{22} \\ 4 b_{21} & 4 b_{22} \\ 6 b_{21} & 6 b_{22} \end{bmatrix}
\;=\;
\begin{bmatrix} b_{11} + 2 b_{21} & b_{12} + 2 b_{22} \\ 3 b_{11} + 4 b_{21} & 3 b_{12} + 4 b_{22} \\ 5 b_{11} + 6 b_{21} & 5 b_{12} + 6 b_{22} \end{bmatrix}
$$

- **與 §6 五大分解的銜接：**
  - **$A = CR$（行列消去）：** $A$ 寫成「獨立列 × 行操作」的乘積，秩 = 獨立列數 = MM4 的有效項數。
  - **$A = LU$（消去法）：** $LU$ 即 (MM4)（$L$ 的直立列 × $U$ 的橫躺行）的有限項相加。
  - **$A = QR$（正交化）：** 同上 (MM4) 結構，但 $Q$ 的直立列彼此正交。
  - **$S = Q \Lambda Q^{\mathrm{T}}$（譜分解）：** 對稱矩陣的特殊 (MM4)，$S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$。
  - **$A = U \Sigma V^{\mathrm{T}}$（SVD）：** 最一般的 (MM4)，$A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，按 $\sigma_p$ 大小排序，取前 $r$ 項即最佳低秩近似（Eckart–Young 定理）。

**(MM4) 不誇張地說，是這本書（也是線性代數應用版圖）的 \*核心\*。**

#### 四個視角總表

| 視角 | 拆法 | 主角 | 一句話 | 結果空間關係 |
|---|---|---|---|---|
| **(MM1)** | $A$ 攤橫躺行 + $B$ 攤直立列 | 每個元素 1 個點積 | 「行 · 列 = $c_{ij}$」 | — |
| **(MM2)** | $B$ 攤直立列 | $C$ 的每一直立列 = $A$ 列的線組 | 「$\mathbf{c}_j = A \mathbf{b}_j$」 | $\mathbf{C}(C) \subseteq \mathbf{C}(A)$ |
| **(MM3)** | $A$ 攤橫躺行 | $C$ 的每一橫躺行 = $B$ 行的線組 | 「$\mathbf{c}^*_i = \mathbf{a}^*_i B$」 | $\mathbf{C}(C^{\mathrm{T}}) \subseteq \mathbf{C}(B^{\mathrm{T}})$ |
| **(MM4)** | $A$ 攤直立列 + $B$ 攤橫躺行 | $AB$ = $k$ 個秩 1 矩陣相加 | 「$AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$」 | $\operatorname{rank}(AB) \le k$；§6 分解皆基於此 |

#### 與 §2 §3 的對偶傳承

| §2 / §3 視角 | §4 推廣 | 關係 |
|---|---|---|
| (v1) 點積 $\mathbf{v} \cdot \mathbf{w}$ | (MM1) 點積每元素 | 「dot product 升級到陣列規模」 |
| (v2) 外積 $\mathbf{v} \mathbf{w}^*$ → 秩 1 矩陣 | (MM4) 外積之和 | 「外積家族真正的家」 |
| (Mv1) $A\mathbf{x}$ 點積 | (MM1) | — |
| (Mv2) $A\mathbf{x}$ 列線組 | (MM2) | 「Mv2 重複 $n$ 次」 |
| (vM1) $\mathbf{y}A$ 點積 | (MM1) | — |
| (vM2) $\mathbf{y}A$ 行線組 | (MM3) | 「vM2 重複 $m$ 次」 |

**記憶口訣：** 「**MM1 像 dot 連環、MM2 是 Mv2 重播、MM3 是 vM2 重播、MM4 是 v2 升級。**」

#### 維度檢核（中間維度對齊）

$(m \times k)(k \times n) = (m \times n)$。**內維度 $k$（A 的列數 = B 的行數）必須相等**才能做乘法。常見錯誤：

- **shape mismatch：** $A$ 是 $3 \times 4$、$B$ 是 $5 \times 2$ → $k$ 不對齊，無法乘。
- **方陣不一定可乘自身：** $A$ 是 $3 \times 4$ → $A \cdot A$ 不合法（要算 $A^{\mathrm{T}} A$ 或 $A A^{\mathrm{T}}$）。
- **MM4 拆數恰是 $k$：** 因為這是內維度，不是 $m$ 也不是 $n$。SVD 把 $A$ ($m \times n$) 拆成 $\sum_{p=1}^{r} \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，這裡 $r \le \min(m, n)$ 是秩，比 $k$（如果 $A$ 不是分解形式）更精確。

#### 矩陣乘法不滿足交換律

一般而言 $AB \ne BA$，且兩者形狀可能不同：

- $A$ 是 $m \times k$、$B$ 是 $k \times n$ → $AB$ 是 $m \times n$、$BA$ 形狀需 $n = m$ 才合法且為 $k \times k$。
- **方陣可換的條件：** 兩個方陣同階 + 共享一組特徵向量（如同時對角化）。
- **(MM4) 視角的直覺：** $AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$ 是「左列 × 右行」、$BA = \sum_q \mathbf{b}_q \mathbf{a}^*_q$ 是「左列 × 右行」但拆的對象互換，幾何上完全不同。

---

### 圖片詳細描述（Figure Descriptions）

#### Figure 4.1: 矩陣乘以矩陣的四種視角（Matrix × Matrix — (MM1), (MM2), (MM3), (MM4)）

**圖檔：** `docs/book/figs-png/MatrixTimesMatrix.png`（原始 EPS：`figs/MatrixTimesMatrix.eps`）
**原書頁碼：** p.4（書封底也呈現此圖）
**所屬章節：** §4

##### 視覺結構 (Visual Structure)

此圖採「**2 × 2 並列四子圖**」結構，是本書最大資訊密度的單頁圖之一。每個子圖左上角有灰色小圈圈標 `MM1`、`MM2`、`MM3`、`MM4` 編號。範例矩陣設定為 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \in \mathbb{R}^{3 \times 2}$、$B = \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} \in \mathbb{R}^{2 \times 2}$（部份子圖 $B$ 寫作 $\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}$ — 兩種記法等價）。

- **左上 (MM1) 點積方式：**
  - 抽象示意：**$A$（3 條粉紅橫躺行）× $B$（2 條綠直立列）= $C$（3×2 棋盤格，每 cell 內畫一條粉紅橫條 + 一條綠直條交叉**「混色」**）**。
  - 右側文字：**"Every element becomes a dot product of row vector and column vector."**
  - 具體範例（下方）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} = \begin{bmatrix} (x_1 + 2 x_2) & (y_1 + 2 y_2) \\ (3x_1 + 4x_2) & (3 y_1 + 4 y_2) \\ (5x_1 + 6x_2) & (5 y_1 + 6 y_2) \end{bmatrix}$$
- **右上 (MM2) 列線性組合方式：**
  - 抽象示意：**$A$（灰色實心方塊）× $B$（2 條綠直立列在大方框）= $A B$（同樣 2 條綠直立列在大方框，但每條稍透明帶漸層）= 進一步寫成 `[Ax  Ay]` 兩條結果直立列**。
  - 右側文字：**"$A\mathbf{x}$ and $A\mathbf{y}$ are linear combinations of columns of $A$."**
  - 具體範例（下方）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} = A \begin{bmatrix} \mathbf{x} & \mathbf{y} \end{bmatrix} = \begin{bmatrix} A\mathbf{x} & A\mathbf{y} \end{bmatrix}$$
- **左下 (MM3) 行線性組合方式：**
  - 抽象示意：**$A$（3 條粉紅橫躺行）× $B$（灰色實心方塊）= $C$（3 條粉紅橫躺行 + 灰色背景，每條稍透明帶漸層）= 進一步寫成「$\mathbf{a}^*_1 X$ / $\mathbf{a}^*_2 X$ / $\mathbf{a}^*_3 X$」三條結果橫躺行**。
  - 右側文字：**"The produced rows are linear combinations of rows."**
  - 具體範例（下方，原書記 $B$ 為 $X$）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} = \begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \mathbf{a}^*_3 \end{bmatrix} X = \begin{bmatrix} \mathbf{a}^*_1 X \\ \mathbf{a}^*_2 X \\ \mathbf{a}^*_3 X \end{bmatrix}$$
- **右下 (MM4) 外積之和方式：**
  - 抽象示意：**$A$（2 條綠直立列）× $B$（2 條粉紅橫躺行）= 兩個「綠直立 × 粉紅橫躺」秩 1 矩陣（$m \times n$ 大小，內含上方一橫條粉紅 + 左側一直條綠的「+」字交叉染色）相加**。
  - 右側文字：**"Multiplication $AB$ is broken down to a sum of rank 1 matrices."**
  - 具體範例（下方）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 \end{bmatrix} \begin{bmatrix} \mathbf{b}^*_1 \\ \mathbf{b}^*_2 \end{bmatrix} = \mathbf{a}_1 \mathbf{b}^*_1 + \mathbf{a}_2 \mathbf{b}^*_2$$
    展開：
    $$= \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \end{bmatrix} + \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} \begin{bmatrix} b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} b_{11} & b_{12} \\ 3 b_{11} & 3 b_{12} \\ 5 b_{11} & 5 b_{12} \end{bmatrix} + \begin{bmatrix} 2 b_{21} & 2 b_{22} \\ 4 b_{21} & 4 b_{22} \\ 6 b_{21} & 6 b_{22} \end{bmatrix}$$
- **配色語意（全章一致，沿用 §1–§3）：**
  - **粉紅色橫條** = 橫躺行（row）。
  - **綠色直條** = 直立列（column）。
  - **灰色實心方塊** = 矩陣整體（不分行 / 列），表示「不關心內部切法、只看為一個 transformation」。
  - **漸層 / 半透明效果** = 「該軸方向被線性組合稀釋 / 投影」。
  - **棋盤交叉（MM1 結果）** = 「每元素同時受到 row + column 兩條方向影響」。
- **四子圖排版方向意義：**
  - **左欄 (MM1, MM3)：** 「逐行 / 逐元素」思維 — 結果用「橫躺行家族」描述。
  - **右欄 (MM2, MM4)：** 「逐列 / 整體疊加」思維 — 結果用「直立列家族」或「秩 1 矩陣相加」描述。
  - **上排 (MM1, MM2)：** 結果是「具體元素填上的最終矩陣」。
  - **下排 (MM3, MM4)：** 結果是「結構性分解（橫躺行家族或秩 1 之和）」 — 更接近 §6 分解視角。

讀者的視覺動線：左上 (MM1) 是熟悉起點 → 順時針到右上 (MM2) 把每元素點積擴展到「整列被線組」→ 跳到右下 (MM4) 把整個運算改寫成「兩個秩 1 之和」 → 最後左下 (MM3) 收尾，與 (MM2) 形成左右乘對稱。**讀完 (MM4) 後再回頭看 (MM1) 會發現「點積方式只是把 (MM4) 中所有秩 1 矩陣的 $(i, j)$ 元素加起來」 — 四視角是同一件事的四種讀法。**

##### 數學內容 (Mathematical Content)

**設定（沿用原書）：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \in \mathbb{R}^{3 \times 2}$、$B = \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} \in \mathbb{R}^{2 \times 2}$、$C = AB \in \mathbb{R}^{3 \times 2}$。

**四種視角驗證恆等（左上角元素 $c_{11}$）：**

- **(MM1)：** $c_{11} = \mathbf{a}^*_1 \cdot \mathbf{b}_1 = 1 \cdot x_1 + 2 \cdot x_2 = x_1 + 2 x_2$。
- **(MM2)：** $\mathbf{c}_1 = A \mathbf{b}_1 = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 = x_1 (1,3,5)^{\mathrm{T}} + x_2 (2,4,6)^{\mathrm{T}}$；$\mathbf{c}_1$ 的第 1 分量 = $x_1 + 2 x_2$。✓
- **(MM3)：** $\mathbf{c}^*_1 = \mathbf{a}^*_1 B = 1 \cdot (x_1, y_1) + 2 \cdot (x_2, y_2) = (x_1 + 2x_2, y_1 + 2y_2)$；$\mathbf{c}^*_1$ 的第 1 分量 = $x_1 + 2x_2$。✓
- **(MM4)：** $AB = \mathbf{a}_1 \mathbf{b}^*_1 + \mathbf{a}_2 \mathbf{b}^*_2$；左上角 = $1 \cdot x_1 + 2 \cdot x_2 = x_1 + 2 x_2$。✓

四種視角數值完全等價，差別在「**閱讀順序 / 心智模型 / 連結後續概念的方向**」。

**運算量檢核：** 四種視角總 FLOP 數相同（$2 \cdot m \cdot k \cdot n$ — 含 $mkn$ 個乘法 + $m(k-1)n$ 個加法），但**記憶體存取模式不同**：

| 視角 | 主要 loop 順序 | 記憶體優勢 |
|---|---|---|
| (MM1) | `for i for j for p: c[i,j] += a[i,p]*b[p,j]` | 直觀但 cache miss 高（B column-major 不利 row-major 存取） |
| (MM2) | `for j: c[:,j] = A @ b[:,j]` | 適合直立列為主的儲存（Fortran / MATLAB） |
| (MM3) | `for i: c[i,:] = a[i,:] @ B` | 適合橫躺行為主的儲存（C / NumPy 預設 row-major） |
| (MM4) | `for p: C += a[:,p:p+1] @ b[p:p+1,:]` | 適合 streaming / out-of-core（隨來隨累加，無需一次載入完整 A, B） |

**形狀運算（四視角共通）：** $(3 \times 2)(2 \times 2) = (3 \times 2)$。內維度 $k = 2$。

**(MM4) 秩 1 之和的視覺意義：**

$$\mathbf{a}_1 \mathbf{b}^*_1 = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \end{bmatrix} = \begin{bmatrix} b_{11} & b_{12} \\ 3b_{11} & 3b_{12} \\ 5b_{11} & 5b_{12} \end{bmatrix}$$

注意這個矩陣的每一直立列都是 $\mathbf{a}_1 = (1,3,5)^{\mathrm{T}}$ 的倍數，每一橫躺行都是 $\mathbf{b}^*_1 = (b_{11}, b_{12})$ 的倍數 — 這就是「**秩 1 矩陣**」的定義（所有直立列共線、所有橫躺行也共線）。

**$AB$ 的秩界限：** $\operatorname{rank}(AB) \le \min(\operatorname{rank} A, \operatorname{rank} B) \le \min(m, k, n)$。從 (MM4) 看：$AB$ 是 $k$ 個秩 1 矩陣相加，秩最多 $k$。若 $A$ 的列空間或 $B$ 的行空間維度更小，秩進一步受限。

##### 直覺解讀 (Intuition)

**1. 四個視角是同一座山的四個觀景台。** 不是「四種不同算法」 — 是同一個 $AB$ 的四種「拆解方式」。教科書通常先教 (MM1)（因為「點積」最具體），但 (MM2) (MM3) 是矩陣論大量結論的源頭，(MM4) 則是 §6 五大分解的鑰匙。**真正讀通的人腦中四個視角能隨意切換 — 看見一個 $AB$ 表達式，會自動同時看到 4 個結構。**

**2. 為什麼 (MM4) 是「最重要」的視角？** 因為：
- **§6 所有分解都是 (MM4) 的特例：** 把 $A$ 寫成兩 / 三個矩陣相乘，再用 (MM4) 把右側展開成「秩 1 之和」。SVD 的 $A = U \Sigma V^{\mathrm{T}}$ 展開即 $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，是「按重要性排序的 (MM4) 之和」。
- **低秩近似的數學依據：** 取 (MM4) 前 $k$ 項即「秩 $k$ 截斷」近似，Eckart–Young 定理保證 SVD 的截斷是 Frobenius 範數下最佳。**這在影像壓縮、推薦系統（矩陣分解）、PCA 都是核心**。
- **Streaming 運算的視角：** $AB$ 不需一次計算完。每次處理一對 $(\mathbf{a}_p, \mathbf{b}^*_p)$ 就累加一個秩 1 圖層 — 適合分散式 / 線上學習。

**3. (MM2) vs (MM3) 的對偶。** 兩者完美對稱：
- (MM2)：「把 $B$ 視為『右側操作』」 — $B$ 的每一直立列指揮如何混合 $A$ 的列。$C$ 的列空間繼承自 $A$ 的列空間。
- (MM3)：「把 $A$ 視為『左側操作』」 — $A$ 的每一橫躺行指揮如何混合 $B$ 的行。$C$ 的行空間繼承自 $B$ 的行空間。
**口訣：** 「**從右邊乘 = 從右側看 = 看 $B$ 怎麼切 = 列線組；從左邊乘 = 從左側看 = 看 $A$ 怎麼切 = 行線組。**」

**4. (MM1) 是「Bad Default」嗎？** 不是。(MM1) 在四方面仍然不可或缺：
- **教學起點：** 對中學程度讀者最容易理解。
- **單一元素查詢：** 只要算 $c_{ij}$ 一個值，(MM1) 是最直接的方式（不需展開整個 $A$ 或 $B$）。
- **稀疏矩陣最佳化：** 若 $A$ 的某 row 多 0 / $B$ 的某 column 多 0，(MM1) 視角下可早終止點積。
- **數學證明便利：** 推導 $c_{ij}$ 的代數性質時 (MM1) 視角最方便（如 trace、Frobenius inner product）。
但 (MM1) 缺乏「子空間 / 秩 / 分解」的視角延伸性 — 這是它的限制。

**5. 何時選哪個視角思考？**

| 你的目標 | 推薦視角 |
|---|---|
| 算單一元素 $c_{ij}$ | (MM1) |
| 理解 $AB$ 的列空間 / 解 $Ax = b$ | (MM2) |
| 理解 $AB$ 的行空間 / 列消去法 | (MM3) |
| 矩陣分解 / SVD / 低秩近似 / streaming | **(MM4)** |
| 證明 trace / 矩陣範數性質 | (MM1) |
| 推導 chain rule（神經網路反向傳播） | (MM2) 或 (MM3)（看 $A$ 還是 $B$ 是參數） |

**常見誤解警示：**
- **「(MM4) 的秩 1 矩陣可以隨便排序」** — 數值上可以（加法可換），但 SVD 的關鍵是「**按 $\sigma_p$ 大小排序後截斷才是最佳近似**」。隨便排序則截斷品質沒保證。
- **「(MM2) 和 (Mv2) 只是寫法不同」** — (Mv2) 是「一個 $\mathbf{x}$ 對 $A$ 列做線組」、(MM2) 是「$n$ 個 $\mathbf{b}_j$ 各自對 $A$ 列做線組」。(MM2) = (Mv2) 重複 $n$ 次，但這個「重複」本身就是 (MM2) 的核心。
- **「四種視角適合不同類型的矩陣」** — 否，四種視角對任何矩陣都成立。差別在你想看出什麼性質。
- **「(MM4) 對非方陣不適用」** — 完全適用。$A$ 是 $m \times k$、$B$ 是 $k \times n$，$AB$ 是 $\sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p$ — 每項是 $m \times n$ 矩陣，與 $A, B$ 是否方陣無關。

**為什麼這張圖該做成互動視覺化？** 因為四個視角的「**等價性**」是動態概念 — 看著同一個 $AB$ 的計算流程從 (MM1) 模式切換到 (MM4) 模式，會即時看到「點積堆 → 列線組 → 行線組 → 秩 1 圖層疊加」的轉換動畫，這是靜態圖完全傳達不了的（見 VizMark-01）。並且 (MM4) 秩 1 圖層的「動態疊加 + rank-$k$ 截斷」是 SVD 教學最缺的鋪陳（見 VizMark-02），把這個畫面做好，§6 SVD 的學習曲線可以下降一半。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [切換視角] ⭐⭐⭐
> **位置：** Figure 4.1 / §4 / (MM1) ↔ (MM2) ↔ (MM3) ↔ (MM4) 四視角切換
> **核心概念：** $AB$ 的四種「拆解 / 閱讀」視角等價（同結果、不同心智模型）
> **互動梗概：** 四個 tab 切換，每次切換觸發 800ms 動畫，把 $A, B, C$ 的色塊（行 / 列 / 灰塊）按目標視角重排，公式逐項同步重排
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [拉桿調參 + 動態累加] ⭐⭐⭐
> **位置：** Figure 4.1 / §4 / (MM4) 子圖 + §6 SVD 預備
> **核心概念：** $AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$ 的秩 1 圖層**逐項累加 / 截斷**動畫，建立「低秩近似」直覺（為 §6 SVD 鋪陳）
> **互動梗概：** 拉「累加項數」slider 從 0 → $k$，看每加一個秩 1 圖層 $C$ 如何越來越接近目標；切換到「彩色圖像」demo 看 SVD 截斷的視覺效果
> **詳見劇本：** VizScript-02（章末）

> 🎬 **VizMark-03** [維度檢核 + 對齊] ⭐⭐
> **位置：** Figure 4.1 / §4 / 整體
> **核心概念：** $(m \times k)(k \times n) = (m \times n)$ 的「內維度對齊」是矩陣乘法合法性的唯一條件
> **互動梗概：** 拉 $A$ 與 $B$ 的尺寸 slider，動態顯示「$k$ 對齊 / 不對齊」的視覺紅綠提示 + 形狀 prediction
> **詳見劇本：** VizScript-03（章末，精簡版）

> 🎬 **VizMark-04** [數值步進] ⭐
> **位置：** Figure 4.1 / §4 / (MM1) 子圖
> **核心概念：** 逐 cell walk through (MM1) 點積計算過程，連結到中學算盤式思維
> **互動梗概：** 按播放鍵，從 $c_{11}$ 開始依序高亮對應的 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$、播放點積結果填入 cell 的動畫
> **詳見劇本：** VizScript-04（章末，輕量版）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: 矩陣乘以矩陣的四種視角切換（4-Way Toggle Animation）

##### A. 一句話定位
單一畫面同時可切換 (MM1) / (MM2) / (MM3) / (MM4) 四種視角，每次切換以 800ms 動畫把 $A, B, C$ 的色塊（橫躺粉紅、直立綠、灰塊、秩 1 圖層）按目標視角重排並重新染色，下方公式逐項同步展開。

##### B. 學習目標（Learning Outcome）
- 使用者能切換四個視角並指出每個視角下 $A, B, C$ 的「主角形狀」（橫躺 / 直立 / 整塊 / 秩 1 圖層）。
- 使用者能寫出每個視角下 $c_{ij}$、$\mathbf{c}_j$、$\mathbf{c}^*_i$、$\mathbf{a}_p \mathbf{b}^*_p$ 的精確公式。
- 使用者能說出「(MM4) 把 $AB$ 解讀成『秩 1 之和』，為 §6 SVD 鋪陳」。
- 使用者能根據手上的任務（算單一元素 / 找列空間 / 找行空間 / 做分解）選用對應視角。
- 使用者能在「拉 $\mathbf{x}$ slider」時觀察到 (MM2) 模式下「$A$ 不動、$B$ 的某直立列權重變化、結果直立列同步變化」的列線組行為。

##### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$C = AB \in \mathbb{R}^{m \times n}$、4 個切片家族（$\mathbf{a}^*_i, \mathbf{a}_p, \mathbf{b}^*_p, \mathbf{b}_j$）、$k$ 個秩 1 矩陣 $\mathbf{a}_p \mathbf{b}^*_p$。
- **預設值：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（$m=3, k=2$）、$B = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$（$k=2, n=2$，使 $C$ 各分量均為「對應 $A$ row sum 倍率」便於觀察）。
- **維度範圍：** $m, n \in [2, 6]$，$k \in [2, 5]$（限 $k \le 5$ 以避免 MM4 秩 1 圖層過多視覺擁擠）。
- **數值範圍：** $a_{ij}, b_{ij} \in [-9, 9]$ 步進 1。
- **退化情形：**
  - $B = I$（$k = n$）：$AB = A$，四視角都顯示「結果完全等於 $A$」的特殊情況。
  - $B = 0$：$AB = 0$，所有色塊變灰、(MM4) 秩 1 圖層全 0。
  - $\operatorname{rank}(A) = 1$ 且 $\operatorname{rank}(B) = 1$：$AB$ 也是秩 1，(MM4) 只剩 1 個非 0 圖層。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 70% 視角區（依模式顯示對應子圖）+ 中 10% 公式區 + 下 20% 控制列。
- **視角區共用畫布：** 1200×480 px 白底；色塊主舞台位於畫布中央 1000×360 px。
- **(MM1) 模式：** 左 $A$（3 條粉紅橫條 stack，60px 高 × 240px 寬）+ 中 `=` + 右 $B$（2 條綠直條 stack，240px 高 × 60px 寬）+ 「箭頭 →」+ $C$（3×2 棋盤格 cell，每 cell 內畫一條粉紅橫條 + 一條綠直條交叉）。
- **(MM2) 模式：** 左 $A$（灰色實心方塊 240×240 px，內以淡粉紅 / 淡綠十字格線提示但不主導）+ `×` + $B$（2 條綠直立列）+ `=` + $C$（2 條綠直立列，每條漸層稀釋表示「線組混合」）。
- **(MM3) 模式：** 左 $A$（3 條粉紅橫躺行）+ `×` + $B$（灰色實心方塊）+ `=` + $C$（3 條粉紅橫躺行，漸層稀釋）。
- **(MM4) 模式：** 左 $A$（2 條綠直立列）+ `×` + $B$（2 條粉紅橫躺行）+ `=` + 2 個「秩 1 矩陣」並排（每個 $m \times n$ 方塊，上方一條粉紅橫 + 左側一條綠直「+」字交叉染色）+ 「$+$」+ ... + 「$=$」+ 最終 $C$。
- **配色（全章一致）：** 綠 `#2ca02c`、粉紅 `#d62728`、藍點 `#1f77b4`、灰填充 `#eeeeee` / 框 `#333333`、漸層 alpha 0.3。
- **公式區：** 等寬字 14pt，LaTeX 渲染（即時切換）。
- **控制列：** 模式 tab（4 個）+ $A$ slider grid + $B$ slider grid + $m, k, n$ slider + 重設 button。
- **字型 / 字級：** 視角標題 18pt sans bold、$A, B, C$ 標籤 14pt italic、cell 內數字 12pt mono、控制列 12pt。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 mode | tab × 4 | MM1 / MM2 / MM3 / MM4 | MM1 | 即時 + 動畫 |
| $m$ | slider | [2, 6] | 3 | 即時 |
| $k$ | slider | [2, 5] | 2 | 即時 |
| $n$ | slider | [2, 6] | 2 | 即時 |
| $a_{ij}$ ($i\!=\!1..m, p\!=\!1..k$) | slider grid | [-9, 9] step 1 | $1, 2, ..., mk$ | 即時 |
| $b_{pj}$ ($p\!=\!1..k, j\!=\!1..n$) | slider grid | [-9, 9] step 1 | 1 (all 1) | 即時 |
| 公式逐項高亮 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click → 還原預設 |

##### F. 輸出畫面細節（Outputs）
- **(MM1) 模式輸出：**
  - $C$ 棋盤格每 cell 中段顯示「$\sum_p a_{ip} b_{pj}$」具體數字（如「$1 \cdot 1 + 2 \cdot 1 = 3$」），公式區同步展開。
  - hover cell $c_{ij}$ → 對應 $\mathbf{a}^*_i$（粉紅整橫條）+ $\mathbf{b}_j$（綠整直條）highlight 加粗外框。
- **(MM2) 模式輸出：**
  - $C$ 的每一直立列中段顯示「$A \mathbf{b}_j$」與展開 `$b_{1j} \mathbf{a}_1 + b_{2j} \mathbf{a}_2 + \ldots$」。
  - hover 結果某直立列 → 對應 $B$ 的該直立列 + 所有 $A$ 直立列同時 highlight（縮放係數對應 $b_{pj}$）。
- **(MM3) 模式輸出：**
  - $C$ 的每一橫躺行中段顯示「$\mathbf{a}^*_i B$」與展開 `$a_{i1} \mathbf{b}^*_1 + a_{i2} \mathbf{b}^*_2 + \ldots$」。
  - hover 結果某橫躺行 → 對應 $A$ 的該橫躺行 + 所有 $B$ 橫躺行同時 highlight。
- **(MM4) 模式輸出：**
  - $k$ 個秩 1 矩陣並排，每個顯示「$\mathbf{a}_p \mathbf{b}^*_p$」與具體元素網格（每個 cell 數字 = $a_{ip} \cdot b_{pj}$）。
  - 最右側「$=$ $C$」顯示累加結果。
  - hover 第 $p$ 個秩 1 矩陣 → 對應 $\mathbf{a}_p$（綠直條）+ $\mathbf{b}^*_p$（粉紅橫條）highlight。
- **公式區：** 即時 LaTeX，$AB = \cdots$（依模式顯示對應展開）。
- **左下角狀態列：** `mode: MM2 | shape: (3×2)(2×2) = (3×2) | rank ≤ 2`。

##### G. 互動行為（Interactions）
- **切換 mode tab：** 觸發轉視角動畫（見 §H）；公式區同步切換 LaTeX。
- **拉動 $a_{ij}$ slider：** 立即重算結果。當前模式對應的色塊內元素數值即時變化；(MM1) 模式下對應第 $i$ 橫躺行內第 $p$ 個元素亮一下；(MM4) 模式下對應第 $p$ 個秩 1 矩陣的「綠直立列」亮一下。
- **拉動 $b_{pj}$ slider：** 對稱行為。
- **拉動 $m, k, n$ slider：** 調整矩陣尺寸 — 色塊重繪 + slider grid 重建。**注意 $k$ 必須在 $A$ 列數與 $B$ 行數同步**（拉 $k$ 同時改兩邊形狀，視覺強化「中間維度對齊」概念）。
- **hover cell / 直立列 / 橫躺行 / 秩 1 圖層：** 見 §F。
- **快捷鍵：** `1` → MM1、`2` → MM2、`3` → MM3、`4` → MM4、`Space` → 依序循環、`R` → reset、`H` → 公式逐項高亮 toggle。

##### H. 動畫腳本（視角切換）
- **從 MM1 → MM2：**
  - **t=0：** MM1 穩態（$A$ 粉紅橫條堆 + $B$ 綠直條 + $C$ 棋盤交叉格）。
  - **t=0–200ms：** $C$ 棋盤格內粉紅橫條 fade out（opacity 1 → 0）；$A$ 的粉紅橫條合併成灰色實心方塊（每條從外向中心收攏 + 染色變灰）。
  - **t=200–500ms：** $C$ 棋盤格散開成 $n$ 個獨立直立綠條（每條從棋盤中抽出 + 對齊到 $B$ 直立列下方）。
  - **t=500–800ms：** $C$ 直立列各自加上漸層稀釋效果（提示「線組混合」）。
- **從 MM2 → MM3：**
  - **t=0–300ms：** $A$ 灰塊散開成 $m$ 條粉紅橫躺行；$B$ 從直立列合併成灰塊。
  - **t=300–600ms：** $C$ 從直立列轉為橫躺行（每條直立列旋轉 90° + 換色 → 粉紅橫躺）。
  - **t=600–800ms：** $C$ 橫躺行各自加上漸層稀釋。
- **從 MM3 → MM4：**
  - **t=0–200ms：** $A$ 粉紅橫躺行翻轉成綠直立列（每條旋轉 90° + 換色）；$B$ 灰塊散開成 $k$ 條粉紅橫躺行。
  - **t=200–500ms：** $C$ 橫躺行 fade out；同時在原本 $C$ 區域畫出 $k$ 個秩 1 矩陣（每個從中心放大到正常大小，stagger 60ms）。
  - **t=500–800ms：** 「$+$」號淡入於秩 1 矩陣之間，「$=$」與最終 $C$ 在最右側淡入。
- **從 MM4 → MM1（循環）：** 對應反向動畫。
- **總長度：** 800ms。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **暫停 / 倒轉：** 是（動畫進行中切換立即 reverse）。

##### I. 邊界與錯誤處理
- **$k$ 不對齊（理論上 UI 不允許，但測試模式可手動觸發）：** 紅色閃爍提示「$A$ 列數 ≠ $B$ 行數」+ 計算被擋下。
- **$m, n, k$ 大尺寸（>5）：** cell 自動縮為 36×36 px；slider grid 改為可摺疊 panel。
- **動畫進行中再切換：** debounce 100ms 或佇列。
- **$A = 0$ 或 $B = 0$：** $C$ 全 0 + 灰色 + 提示「乘 0 矩陣」。
- **拖動 slider 過快：** debounce 30ms。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - MM1 tab：「每元素 = 一條橫躺行 · 一條直立列」
  - MM2 tab：「$C$ 的每一直立列 = $A$ 直立列的線性組合（係數來自 $B$ 對應直立列）」
  - MM3 tab：「$C$ 的每一橫躺行 = $B$ 橫躺行的線性組合（係數來自 $A$ 對應橫躺行）」
  - MM4 tab：「$AB$ = $k$ 個秩 1 矩陣相加 — §6 SVD 與低秩近似的鑰匙」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 MM1：$C$ 的每個元素是『$A$ 橫躺行 · $B$ 直立列』」
  - Step 2：「按 `2` 切到 MM2：$A$ 變灰塊、$B$ 仍是直立列、結果直立列是『$A\mathbf{b}_j$』」
  - Step 3：「按 `3` 切到 MM3：對稱於 MM2，這次 $B$ 變灰塊」
  - Step 4：「按 `4` 切到 MM4：$AB$ 變成 $k$ 個秩 1 矩陣之和 — 這是 SVD 的鑰匙！」
  - Step 5：「拉 $b_{pj}$ slider 看每個視角下變化的位置不同 — 但結果完全相同」
- **常見誤解警示：**
  - 「四個視角不是不同算法 — 是同一個 $AB$ 的四種讀法」
  - 「MM4 的 $k$ 是『內維度』，不是 $m$ 或 $n$」
- **延伸閱讀：** 原書 p.4、`ch04-mat-mat.md` 數學要點、Strang LAFE Sec. 1.4。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo（反應式 notebook）+ matplotlib + `matplotlib.animation.FuncAnimation`（控制視角切換動畫）+ marimo.ui。
- **替代方案：** Streamlit + Plotly + custom JS（如需高品質瀏覽器分享）。
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫粉紅橫條 / 綠直條 / 灰塊。
  - `matplotlib.transforms.Affine2D().rotate_deg_around()` 做橫 ↔ 直旋轉。
  - `matplotlib.collections.PatchCollection` 高效繪製大量秩 1 矩陣 cell。
  - `marimo.ui.tabs`（4 個視角切換）、`marimo.ui.slider`、`marimo.ui.array`（slider grid）。
  - `numpy.einsum('ip,pj->ij', A, B)` 計算結果。
- **檔案結構：**
  ```
  viz/
    ch04_matrix_matrix.py        # 主入口（含 VizScript-01 / 02 / 03 / 04 共用畫面 tab）
    _common/
      palette.py                 # 沿用 §1–§3 配色
      matrix_canvas.py           # §3 已建（橫條 / 直條 / 灰塊原語），§4 直接 import + 新增「秩 1 圖層」原語
      rank1_layer.py             # 新增：(MM4) 秩 1 矩陣繪製（綠直 + 粉紅橫「+」字交叉）
  ```
- **效能：** 動畫期間預先計算所有 frame 的色塊座標 / 顏色，存 list；動畫結束後切回 reactive。$k > 3$ 時 (MM4) 模式秩 1 圖層橫向排版改為兩排（避免畫布過寬）。
- **測試：** 動畫關鍵 frame（t=0 / 300 / 600 / 800）各 1 張 snapshot；4 個模式各 1 張靜態 snapshot；退化（$B = I$ / $B = 0$）各 1 張。

##### L. 驗收標準（Acceptance Criteria）
- [ ] 視角 tab 切換動畫總長 ≤ 800ms，60fps 無 frame drop。
- [ ] 拉 $a_{ij}$ / $b_{pj}$ slider 即時更新 $C$，並在當前模式對應位置高亮 200ms。
- [ ] hover $C$ 元素 / 直立列 / 橫躺行 / 秩 1 圖層 → 對應 $A, B$ 部分正確高亮。
- [ ] 公式區 LaTeX 渲染 < 50ms 完成。
- [ ] $k$ 改變時 $A$ 列數與 $B$ 行數同步更新（不允許不對齊）。
- [ ] $B = I$ 時 $C$ 與 $A$ 完全等價（視覺上可確認）。
- [ ] Walkthrough 5 步驟首次開啟自動觸發。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純並列四子圖靜態，無動畫切換。
- **Tier 3 擴充：** + 加 3D 視窗即時顯示 $A$ 列空間與 $B^{\mathrm{T}}$ 行空間的「列空間映射 = $C$ 列空間」幾何（與 §3 4-Subspaces 互動連接）。
- **估時：** 1.5 session（含測試與 walkthrough）

---

#### VizScript-02: MM4 外積之和的逐項累加與秩截斷（Rank-1 Layer Accumulation + Rank-$k$ Truncation）— SVD 鋪陳

##### A. 一句話定位
拉「累加項數 $r$」slider 從 0 走到 $k$，看 $C$ 從全 0 逐項加上 $\mathbf{a}_p \mathbf{b}^*_p$ 秩 1 圖層、最終疊加成完整 $AB$；切換到「彩色圖像」demo 模式時，使用實際 64×64 像素影像（內建 4 張：Mona Lisa / 條紋 / 漸層 / 隨機）做 SVD 截斷，視覺展示「**前幾個秩 1 圖層保留主要結構、後面的只加細節**」。

##### B. 學習目標（Learning Outcome）
- 使用者能直觀感受「$AB$ = $k$ 個秩 1 矩陣相加」的視覺意義。
- 使用者能說出「每個 $\mathbf{a}_p \mathbf{b}^*_p$ 是一個秩 1 矩陣，所有直立列共線、所有橫躺行共線」。
- 使用者能解釋「秩 $r$ 截斷」概念：取前 $r$ 個秩 1 圖層 = 用 $r$ 個秩 1 矩陣近似原矩陣。
- 使用者能在「彩色圖像 demo」中觀察到「前 5–10 個 SVD 秩 1 圖層保留人臉 / 主要結構，後面的只在加紋理細節」。
- 使用者能在「秩 1 圖層重排序」交互中觀察到「按 $\sigma_p$ 大小排序的截斷品質遠好於隨機排序」 — 鋪陳 §6.5 Eckart–Young 定理。
- 使用者能說出「(MM4) 是 SVD 的鑰匙、是 PCA / 推薦系統 / 影像壓縮的核心」。

##### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$k$ 個秩 1 矩陣 $\mathbf{a}_p \mathbf{b}^*_p$、累加中間結果 $C_r = \sum_{p=1}^{r} \mathbf{a}_p \mathbf{b}^*_p$、目標 $C = AB$、誤差 $\|C - C_r\|_F$。
- **預設值（兩種模式）：**
  - **模式 1（小矩陣 demo）：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$、$B = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$（$B = I_2$，使 $AB = A$，便於對比）；$k = 2$。
  - **模式 2（彩色圖像）：** $A, B$ 從 SVD 分解出（內建 64×64 灰階圖像 → $A = U \Sigma^{1/2}$、$B = \Sigma^{1/2} V^{\mathrm{T}}$），$k = 64$（full rank）。
- **維度範圍：**
  - 模式 1：$m \in [2, 6]$、$k \in [2, 5]$、$n \in [2, 6]$。
  - 模式 2：固定 $64 \times 64$，$k = 64$。
- **退化情形：**
  - $r = 0$：$C_r = 0$（全黑 / 全 0），誤差 $\|C\|_F$。
  - $r = k$：$C_r = C$（完美還原），誤差 0。
  - $\mathbf{a}_p = 0$ 或 $\mathbf{b}^*_p = 0$：該秩 1 圖層為 0，跳過不變化。
  - 兩個秩 1 圖層相同（共線）：累加時視為「方向重疊」用淡色提示。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 55% 主舞台 + 中 15% 秩 1 圖層 strip + 下 30% 控制列 + 圖表。
- **主舞台（左中右三區）：**
  - **左 30%：** $A$ + $B$ 原始矩陣顯示（$A$ 綠直立列 stack、$B$ 粉紅橫躺行 stack）。
  - **中 35%：** 「+」號 + $r$ 個秩 1 圖層相加結構 + 「$=$」+ 累加結果 $C_r$（cell 值即時更新，每個 cell 內字級隨數字長度自適應）。
  - **右 35%：** 目標 $C$ 與當前 $C_r$ 對比（兩個矩陣並列，差異用熱色 colormap 顯示 $|C - C_r|$）。模式 2 時改為「彩色圖像對比」：原圖 / 累加圖 / 誤差熱圖三張 64×64 像素影像。
- **秩 1 圖層 strip（中 15%）：** 橫向排列 $k$ 個秩 1 矩陣縮圖（每個 60×60 px），按「當前是否已被累加」分為亮色 / 灰色兩組；hover 縮圖顯示「$\mathbf{a}_p \mathbf{b}^*_p$」公式與其能量貢獻 $\|\mathbf{a}_p\| \cdot \|\mathbf{b}^*_p\|$（模式 2 顯示對應的 $\sigma_p$）。
- **下 30% 控制列：**
  - 上排：「累加項數 $r$」slider [0, $k$] + play / pause button + 「自動播放」speed slider。
  - 中排：模式切換 radio（小矩陣 / Mona Lisa / 條紋 / 漸層 / 隨機）+ 「重排序」radio（按 $\sigma_p$ 排序 / 按 $\|\mathbf{a}_p\|$ 排序 / 隨機排序 / 自訂順序）。
  - 下排：誤差曲線圖（橫軸 $r$、縱軸 $\|C - C_r\|_F$ / $\|C\|_F$，當前 $r$ 標紅點）。
- **配色：** $\mathbf{a}_p$ 綠 `#2ca02c`、$\mathbf{b}^*_p$ 粉紅 `#d62728`、秩 1 圖層 cell 用「藍 → 白 → 紅」連續 colormap（依數值正負）、累加結果 $C_r$ 用同 colormap。模式 2 用 gray colormap。
- **字型 / 字級：** 矩陣標題 18pt、cell 數字 12pt、圖層 strip 標籤 10pt、誤差曲線 12pt。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 累加項數 $r$ | slider | [0, $k$] | 0 | 即時 + 動畫 |
| play / pause | button | — | pause | click |
| 自動播放速度 | slider | 200ms – 2s / 項 | 700ms | 即時 |
| 模式 | radio | 小矩陣 / Mona Lisa / 條紋 / 漸層 / 隨機 | 小矩陣 | 切換重建 |
| 重排序 | radio | $\sigma_p$ 排序 / $\|\mathbf{a}_p\|$ 排序 / 隨機 / 自訂 | $\sigma_p$ | 即時重算 |
| $a_{ip}, b_{pj}$（小矩陣模式） | slider grid | [-9, 9] step 1 | 預設值 | 即時 |
| 顯示誤差熱圖 | checkbox | on / off | on | 即時 |
| 顯示能量貢獻 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click |

##### F. 輸出畫面細節（Outputs）
- **主舞台累加結果 $C_r$：**
  - 小矩陣模式：每 cell 顯示具體數字，數字字級隨整體尺寸自適應。
  - 圖像模式：64×64 灰階熱圖即時更新。
- **秩 1 圖層 strip：**
  - 已累加的圖層（$p \le r$）顯示飽和色 + 邊框深色；未累加（$p > r$）顯示淡灰色 + 邊框虛線。
  - 每個縮圖右下角標 `p`，下方標 $\sigma_p$（模式 2）或 $\|\mathbf{a}_p\| \|\mathbf{b}^*_p\|$（模式 1）。
- **目標 / 對比區：**
  - 上方：「目標 $C$」（不變）+ 「累加 $C_r$」（即時）。
  - 下方：「誤差 $|C - C_r|$」熱圖，紅色越深表示誤差越大。
  - 模式 2：三張 64×64 影像並列（原圖 / 重建圖 / 誤差圖）+ 「相對誤差 $\|C - C_r\|_F / \|C\|_F = 23.4\%$」即時數字。
- **誤差曲線圖：**
  - 橫軸 $r$，縱軸 $\|C - C_r\|_F / \|C\|_F$，曲線呈遞減（按 $\sigma_p$ 排序時下降最快）。
  - 當前 $r$ 用紅點 + 垂直虛線標記。
  - 不同重排序方式用不同顏色曲線（按 $\sigma_p$ 排序：粗藍實線；隨機排序：淡灰虛線；對比效果一目了然）。
- **公式區：** 即時 LaTeX `$C_r = \sum_{p=1}^{r} \mathbf{a}_p \mathbf{b}^*_p$`，並列出當前 $r$ 對應的具體展開項。

##### G. 互動行為（Interactions）
- **拉「$r$」slider 從 0 到 $k$：** 主舞台累加結果即時更新（每加 1 項，新秩 1 圖層從 strip 飛到主舞台中央 + 與當前累加結果做加法動畫 400ms）；strip 中對應圖層從灰變亮；誤差曲線紅點同步移動。
- **拉「$r$」slider 從 $k$ 到 0（倒退）：** 反向動畫，秩 1 圖層從累加結果中「飛回」strip + 變灰。
- **play 自動播放：** 依速度設定自動推進 $r$，從 0 走到 $k$ + 暫停 1 秒 + 從 $k$ 走回 0 循環。
- **切換模式：** 整個畫面重建（小矩陣 → 圖像模式時，所有 cell 變成像素網格）。
- **切換重排序：** 秩 1 圖層 strip 順序重排（300ms 動畫）+ 誤差曲線重繪（同色曲線淡化、新色曲線淡入）+ 提示「按 $\sigma_p$ 排序時前 5 項已覆蓋 87% 能量」之類的數字提示。
- **hover 秩 1 圖層 strip 某項：** 該項放大 1.2 倍 + 顯示詳細 tooltip（$\mathbf{a}_p$ / $\mathbf{b}^*_p$ 數值、能量、累積占比）；主舞台對應位置高亮。
- **快捷鍵：** `Space` play / pause、`→` $r$ += 1、`←` $r$ -= 1、`R` reset、`0` reset $r$ to 0、`Shift+End` $r$ to $k$、`M` 切換模式（依序循環）。

##### H. 動畫腳本（秩 1 圖層飛入累加）
- **新增第 $p$ 項（$r$ 從 $r$ 到 $r+1$）：**
  - **t=0：** strip 第 $p$ 項從灰色開始放大。
  - **t=0–150ms：** 該項放大 1.3 倍 + 從 strip 位置「彈出」朝主舞台中央飛入（位置插值 + 透明度 0.7 → 1）。
  - **t=150–350ms：** 該項抵達主舞台「+」號右側 + 縮回正常大小 + 顯示「$+ \mathbf{a}_p \mathbf{b}^*_p$」標籤。
  - **t=350–650ms：** 該項與當前累加結果合併 — 像素級疊加動畫（每個 cell 數值從舊值 lerp 到新值 + 顏色 colormap 同步插值，stagger 從左上到右下 5ms 一個 cell）。
  - **t=650–800ms：** 「+」號 / 「=」號 / 結果 $C_r$ 同步更新數字 + 誤差數字字級閃一下提示降低。
  - **strip 第 $p$ 項：** 從灰色轉為飽和色（150ms fade）。
- **總長度：** 800ms / 項。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **倒退（$r$ 從 $r$ 到 $r-1$）：** 反向重播，秩 1 圖層從主舞台「飛回」strip。
- **自動播放：** 連續執行新增動畫，stagger 200ms（速度依 slider）。

##### I. 邊界與錯誤處理
- **$r = 0$：** 主舞台累加結果全 0 + 灰底；誤差曲線紅點在最左、誤差最大（= 100%）。
- **$r = k$：** 累加結果與目標 $C$ 完全相同（cell 值逐項對比可驗證）；誤差為 0；秩 1 圖層 strip 全亮。
- **拉 slider 過快：** debounce 50ms，動畫跳過中間幀直接到目標 $r$ 對應狀態（避免播放堆疊）。
- **圖像模式切換中：** 顯示 loading spinner 500ms；SVD 計算在 worker 執行，主執行緒不卡。
- **$\mathbf{a}_p = 0$ 或 $\mathbf{b}^*_p = 0$：** strip 該項標「dead layer」灰色標籤；累加時無變化。
- **重排序為「自訂」：** 顯示 drag handle 讓使用者拖曳 strip 改順序。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - 秩 1 圖層縮圖：「第 $p$ 個秩 1 矩陣 $\mathbf{a}_p \mathbf{b}^*_p$，能量 $\|\mathbf{a}_p\|\|\mathbf{b}^*_p\| = 17.3$」
  - $r$ slider：「累加前 $r$ 個秩 1 圖層 — 拉到 $k$ 即完整 $AB$」
  - 重排序選項：「按 $\sigma_p$ 排序的截斷是 Frobenius 範數下最佳近似（Eckart–Young 定理，§6.5）」
  - 誤差曲線：「累積保留能量比例 — 注意按 $\sigma_p$ 排序時前 5 項已覆蓋大部分能量」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在 $r = 0$，$C_r = 0$（全 0 矩陣 / 全黑影像）」
  - Step 2：「按 → 鍵或拉 slider 到 $r = 1$，看第 1 個秩 1 圖層飛入累加」
  - Step 3：「注意第 1 個秩 1 矩陣的『所有直立列共線、所有橫躺行共線』 — 這就是『秩 1』的定義」
  - Step 4：「繼續加到 $r = k$，看 $C_r$ 完全還原 $AB$」
  - Step 5：「切到『Mona Lisa』模式，看前 5–10 個秩 1 圖層已能還原人臉輪廓 — 這就是 SVD 壓縮的精髓」
  - Step 6：「切『隨機排序』看誤差曲線變差 — 說明『按 $\sigma_p$ 排序』才能最佳壓縮（§6.5 SVD 會證明）」
- **常見誤解警示：**
  - 「秩 1 矩陣不是『1 個元素的矩陣』 — 是『所有列共線』的矩陣」
  - 「(MM4) 對任何矩陣都可拆，不限 SVD — SVD 是『最佳化的 (MM4) 拆法』」
  - 「截斷 $r < k$ 不是『近似誤差』 — 是『有意丟掉小能量項』，是壓縮策略」
- **延伸閱讀：** 原書 p.4、§6.5 ($A = U \Sigma V^{\mathrm{T}}$)、Strang LAFE Sec. 1.4 + Sec. 7.4 Eckart–Young、`ch04-mat-mat.md` 數學要點 (MM4) 段。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + matplotlib.animation + marimo.ui（小矩陣模式）；圖像模式建議 Plotly + Dash（heatmap 渲染更快、影像對比更專業）。
- **替代方案：** Streamlit（純 Python、部署簡單） + Plotly。
- **關鍵 API：**
  - `numpy.linalg.svd(image, full_matrices=False)` 計算 SVD（圖像模式）。
  - `numpy.einsum('p,ip,pj->ij', sigma[:r], U[:,:r], Vt[:r,:])` 計算秩 $r$ 重建。
  - `numpy.outer(a_p, b_p)` 計算秩 1 矩陣。
  - `matplotlib.image.imshow` / `plotly.express.imshow` 繪製熱圖。
  - `matplotlib.animation.FuncAnimation` 累加動畫（每 frame 更新 cell 數值）。
- **檔案結構：**
  ```
  viz/
    ch04_matrix_matrix.py
    _common/
      rank1_layer.py             # 共用秩 1 圖層繪製
      svd_demo.py                # 圖像 SVD 預先計算 + cache
    assets/
      mona_lisa_64.npy           # 64×64 灰階 numpy array
      stripes_64.npy
      gradient_64.npy
      random_64.npy
  ```
- **效能：** 圖像 SVD 預先計算並 cache 到 `assets/`；播放時只做切片運算（$O(64 \times 64 \times r)$）。
- **測試：** $r = 0, 1, k/2, k$ 各 1 張 snapshot；4 種圖像各 1 張（$r = 5, 10, 20, 64$）；誤差曲線 1 張。

##### L. 驗收標準（Acceptance Criteria）
- [ ] 拉 $r$ slider 從 0 走到 $k$，每加 1 項動畫 ≤ 800ms。
- [ ] 切換 4 種圖像模式無延遲（< 200ms 載入）。
- [ ] Mona Lisa 模式 $r = 10$ 時可清楚辨識人臉。
- [ ] 重排序「$\sigma_p$」與「隨機」對比下，前者誤差曲線明顯較陡。
- [ ] 累加動畫 60fps 無 frame drop（64×64 cell × 60fps × 64 frame = 245760 cell updates / sec OK）。
- [ ] hover 秩 1 圖層 strip 即時顯示能量數值。
- [ ] Walkthrough 6 步驟首次開啟自動觸發。
- [ ] $r$ 倒退時動畫反向，無視覺殘留。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 3
- **Tier 1 對應：** 純並列「目標 / 累加 / 誤差」三張靜態圖，無動畫。
- **Tier 2 對應：** 加 $r$ slider 控制累加項數 + 即時更新（無秩 1 圖層 strip）。
- **Tier 3 擴充（本版本）：** + 圖像 demo 4 張 + 重排序對比 + 誤差曲線 + 飛入動畫。
- **Tier 4 擴充（S12+ 可選）：** + 多影像並排對比（同一 $r$ 看不同影像的壓縮品質差異）+ 對應 SVD 「Mode 1 / Mode 2 / Mode 3」分解模式互動。
- **估時：** 2.5 session（含 4 張圖像準備、SVD 預計算、累加動畫、誤差曲線、Walkthrough 等；圖像模式是難點，Plotly Dash 整合需 0.5 session）

---

#### VizScript-03: 維度檢核與內維對齊（Shape Validator）

##### A. 一句話定位
拉 $A, B$ 的尺寸 slider 即時看「$k$ 對齊 / 不對齊」綠紅燈號 + $(m \times k)(k \times n) = (m \times n)$ 形狀預測，並用色塊「能不能拼起來」的視覺暗示讓使用者體會「中間維度必須匹配」。

##### B. 學習目標（Learning Outcome）
- 使用者能在拉 slider 時即時判定 $AB$ 是否合法。
- 使用者能說出「$A$ 列數 = $B$ 行數」是矩陣乘法的唯一形狀條件。
- 使用者能根據 $A, B$ 形狀推測 $AB$ 形狀（拼起來 = 外維度組合）。

##### C. 待視覺化的數學物件
- $A \in \mathbb{R}^{m \times k_A}$、$B \in \mathbb{R}^{k_B \times n}$、合法條件 $k_A = k_B$。
- **預設值：** $m=3, k_A=k_B=2, n=2$（合法）。
- **維度範圍：** 各維度 $\in [1, 8]$。

##### D. 視覺布局
- 上 60% 視覺區：$A$ 灰塊（寬 $m$ cm × 高 $k_A$ cm 比例）+ $B$ 灰塊（寬 $k_B$ × 高 $n$）+ 「拼接示意」中間區（綠 / 紅圈圈）+ $AB$ 預測形狀（虛框）。
- 下 40% 控制列：$m, k_A, k_B, n$ 各一個 slider [1–8]，外加「強制 $k_A = k_B$」toggle。

##### E. 輸入控制
$m, k_A, k_B, n$ slider × 4 + `k 同步` toggle。

##### F. 輸出畫面細節
- $A, B$ 灰塊根據 slider 即時調整 aspect ratio。
- 中間「對齊圈」：$k_A = k_B$ 時顯示綠勾，否則紅叉 + 提示「$k_A = $ X ≠ Y = $k_B$」。
- $AB$ 預測形狀：合法時顯示綠虛框 $(m \times n)$ + 灰填充、不合法時顯示「— illegal —」與紅虛框。
- 公式區：合法時 LaTeX `$(m \times k)(k \times n) = (m \times n)$`；不合法時整段刪除線 + 紅字提示。

##### G. 互動行為
- 拉 slider 即時重繪 + 對齊圈狀態更新。
- toggle `k 同步` 為 on 時，拉 $k_A$ 自動同步 $k_B$（避免不合法）。
- hover $A$ 或 $B$ 灰塊：顯示「行 / 列數」標籤。

##### H. 動畫腳本
- 不合法 → 合法：紅叉淡出 + 綠勾淡入 200ms + $AB$ 虛框從紅變綠 + 灰填充淡入 300ms。
- 合法 → 不合法：反向。

##### I. 邊界與錯誤處理
- 維度 1：cell 變極小（4 px），改用文字標 "1"。
- 維度 8：cell 縮為 18 px。

##### J. 教學支援
- Tooltip：對齊圈 — 「中間維度匹配是矩陣乘法唯一形狀條件 — 若有疑問就拼一下『$A$ 列數』 vs 『$B$ 行數』」。

##### K. 技術實作建議
- Marimo + matplotlib (`Rectangle` + `Text`)，無動畫密集，純 reactive。

##### L. 驗收標準
- [ ] slider 即時響應 < 50ms。
- [ ] $k_A \ne k_B$ 時紅叉與紅虛框正確顯示。
- [ ] toggle `k 同步` 行為正確。

##### M. 互動深度 Tier + 估時
- **Tier 1**；估時 0.5 session。

---

#### VizScript-04: MM1 點積 walkthrough（Per-Element Dot Product Tour）

##### A. 一句話定位
按播放鍵，從 $c_{11}$ 開始依序遍歷 $C$ 的每個元素，每個元素高亮對應 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$、播放點積計算過程（$a_{i1} \cdot b_{1j} + a_{i2} \cdot b_{2j} + \ldots$）、填入結果到對應 cell。

##### B. 學習目標
- 使用者能完整重現 (MM1) 點積計算流程。
- 使用者能將 (MM1) 公式與視覺色塊一一對應。

##### C. 待視覺化的數學物件
- $A, B, C$、每個元素 $c_{ij}$ 對應的 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$、點積中間值。
- **預設：** 原書範例（$m=3, k=2, n=2$）。

##### D. 視覺布局
- 與 VizScript-01 (MM1) 模式畫面共用。
- 增加一個底部 walkthrough panel（顯示當前算到的 $c_{ij}$ + 點積展開式）。

##### E. 輸入控制
- play / pause、speed slider、jump-to-cell (i, j)。

##### F. 輸出畫面細節
- 當前 $c_{ij}$ cell 內顯示展開式「$a_{i1} b_{1j} + a_{i2} b_{2j}$」+ 數字代入 + `=` + 最終值。
- 對應 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$ 加粗外框 + 亮色填充。
- 其他 cell 半透明 0.5。

##### G. 互動行為
- 自動播放：依序遍歷 $i = 1..m, j = 1..n$，每個 cell 暫停 1.5 秒。
- click 任意 cell 跳轉到該位置。

##### H. 動畫腳本
- 移到下個 cell：點積中間值「$a_{i1} \cdot b_{1j}$」浮現 → 「+ $a_{i2} \cdot b_{2j}$」浮現 → 「= $c_{ij}$」浮現 → 該 cell 填入結果。

##### I. 邊界與錯誤處理
- 大矩陣（$mn > 20$）：自動加速到 0.5 秒 / cell。

##### J. 教學支援
- Tooltip：點積中間值 — 「$a_{i1} b_{1j}$ 是 $\mathbf{a}^*_i$ 第 1 元素 × $\mathbf{b}_j$ 第 1 元素」。

##### K. 技術實作建議
- 與 VizScript-01 共用 ch04 主入口，新增 `walkthrough_mm1.py` 模組。

##### L. 驗收標準
- [ ] 自動播放遍歷所有 $c_{ij}$。
- [ ] click 任意 cell 跳轉正確。

##### M. 互動深度 Tier + 估時
- **Tier 1**；估時 0.5 session。

---

### 章末延伸與來源對照

#### 與原書其他章節的連結
- **§1 (Viewing a Matrix - 4 Ways)：** 提供「橫躺行 / 直立列 / 元素 / 秩 1 之和」四種看 $A$ 的方式 → 直接套用到本章 $C = AB$ 的四種讀法。(MM1) ↔ 「個別元素」、(MM2) ↔ 「直立列家族」、(MM3) ↔ 「橫躺行家族」、(MM4) ↔ 「秩 1 之和」。
- **§2 (Vector × Vector - 2 Ways)：** (v2) 外積 → 秩 1 矩陣 = (MM4) 中每一項 $\mathbf{a}_p \mathbf{b}^*_p$ 的單獨型態。「§2 v2 是 §4 MM4 的單項。」
- **§3 (Matrix × Vector - 2 Ways + 4-Subspaces)：** (Mv2) = (MM2) 取 $B$ 為單一直立列 $\mathbf{b} \in \mathbb{R}^k$；(vM2) = (MM3) 取 $A$ 為單一橫躺行 $\mathbf{a}^* \in \mathbb{R}^{1 \times k}$。本章把 §3 的「兩個視角」推廣到「兩個矩陣的乘積」，從而出現第 4 個全新視角 (MM4)。
- **§5 (Practical Patterns)：** Pattern 1 / 2 / 1′ / 2′ / 3 都是 (MM2) 或 (MM3) 或 (MM4) 的特殊配置 — Pattern 1 = (MM2) 加 (Mv2)、Pattern 2 = (MM3) 加 (vM2)。本章是 §5 的數學基石。
- **§6 (Five Factorizations)：** 全部都是 (MM4) 的展開：
  - $A = CR$：$A = C R$ 是 (MM2) + (MM4)（$C$ 是 $A$ 獨立直立列、$R$ 是行操作；展開 $CR$ 即 $\sum_p \mathbf{c}_p \mathbf{r}^*_p$）。
  - $A = LU$：$LU$ 同 (MM4) 結構（$L$ 直立列 × $U$ 橫躺行），秩 1 之和的有限項。
  - $A = QR$：同 $LU$ 結構，但 $Q$ 的直立列正交。
  - $S = Q \Lambda Q^{\mathrm{T}}$：$S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$，對稱矩陣的 (MM4) 譜分解。
  - $A = U \Sigma V^{\mathrm{T}}$：$A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，最一般的 (MM4)，按 $\sigma_p$ 大小排序即最佳低秩近似（Eckart–Young）。

#### 與工程實作的銜接
- **NumPy / PyTorch：** `A @ B` 預設以 (MM3) 模式實作（row-major 友善）；`numpy.einsum('ip,pj->ij', A, B)` 可指定其他模式。
- **BLAS：** Level 3 BLAS（GEMM）內部以 (MM4) 風格 + cache blocking 實現，把大矩陣拆成小區塊外積之和以利用 CPU cache。
- **GPU 矩陣乘法：** Tensor core 直接以 (MM1) + (MM4) 混合（4×4 點積 + 累加），與 NVIDIA Tensor Core 設計直接對應。
- **影像壓縮 / 推薦系統：** SVD 截斷即 (MM4) 取前 $r$ 項（如 Netflix Prize 用 $r \approx 50$ 個 latent factors 即可達到良好預測精度）。
- **神經網路反向傳播：** 鏈式法則 $\frac{\partial L}{\partial A} = \frac{\partial L}{\partial C} B^{\mathrm{T}}$ 是 (MM2) / (MM3) 應用 — 整個 PyTorch autograd 由 (MM1)–(MM4) 視角組合而成。

#### 來源對照
- **`docs/book/from-tex/en.md`** 第 114–125 行（英文版 § Matrix times Matrix - 4 Ways）。
- **`docs/book/from-tex/zh.md`** 第 109–120 行（簡中版 § 矩阵乘以矩阵 - 4 个视角）。
- **`docs/book/from-pdf/en.txt`** Figure 6 對應段落（line 215–262）— 含 4 子圖具體展開。
- **`docs/book/figs-png/MatrixTimesMatrix.png`** 主圖（2×2 並列四子圖）。
- **Strang《Linear Algebra for Everyone》Sec. 1.4** (p.35) "Four Ways to Multiply $AB = C$" — 與本章順序完全一致。
- **書封底圖** — 原書封底重印此圖，是全書最具識別性的視覺標誌。

---

### 章節結束自檢清單

- [x] 摘要段點明四視角名稱 + 各自核心 + (MM4) 是 SVD 鑰匙
- [x] 數學要點覆蓋四個視角 + 對偶總表 + 與 §2 §3 傳承表 + 維度檢核 + 非交換律
- [x] (MM4) 段強調與 §6 五大分解的銜接
- [x] Figure 4.1 完整四欄描述（含四子圖獨立段落）
- [x] 4 個 VizMark + VizScript：⭐⭐⭐ × 2 完整 13 段 / ⭐⭐ × 1 精簡 13 段 / ⭐ × 1 輪廓
- [x] 章末延伸銜接 §1–§3 來源 + §5 §6 後續
- [x] 來源對照行數精確
- [x] 沿用 A 派術語（列 = column 直立、行 = row 橫躺）
- [x] 沿用全書視覺一致性錨點（配色 hex、cell 尺寸、動畫時間）

---

## 第 5 章. 實用模式（Practical Patterns）

> **原書頁碼：** p.5–7
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 127–203 行
> **本章圖數：** 4（Figure 5.1 = P1/P2、Figure 5.2 = P1'/P2'、Figure 5.3 = P3、Figure 5.4 = P4）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成 / [ ] 校對中

---

### 章節摘要

§4 的四種視角（MM1/MM2/MM3/MM4）已涵蓋所有 $AB$ 的拆解方式。本章把這些視角**特殊化**到三類在工程中極常見的「**配置**」上：(P1) (P1') 用對角矩陣**從右**乘 → **column scaling**（列縮放）；(P2) (P2') 用對角矩陣**從左**乘 → **row scaling**（行縮放）；(P3) $XD\mathbf{c}$ 是「對角線上嵌一個向量」的三明治結構，等於「**特徵向量按特徵值加權後再以初始條件係數線組**」 — 解微分方程 $\frac{d\mathbf{u}}{dt} = A\mathbf{u}$ 與遞迴方程 $\mathbf{u}_{n+1} = A\mathbf{u}_n$ 的核心；(P4) $U \Sigma V^{\mathrm{T}}$ 是「兩個正交矩陣夾一個對角矩陣」的三明治結構，等於「秩 1 矩陣按奇異值加權後相加」 — **特徵值分解與 SVD 共用的視覺骨架**。

> ⚠ **本章是 §6 五大分解的「最後一塊鋪陳」。** P1/P2/P1'/P2' 解釋對角矩陣的視覺角色（§6.4 $S = Q\Lambda Q^{\mathrm{T}}$ 與 §6.5 $A = U\Sigma V^{\mathrm{T}}$ 的中間項）；P3 把「特徵值 / 特徵向量 / 初始條件」三件事接合成「微分方程通解」（§6.4 的工程動機）；P4 把整個 (MM4) 視角包裝成「三明治結構」 — §6.4–§6.5 兩大分解都直接套此模式。

> ⚠ **術語提醒：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。對角矩陣 $D$ 視作「**只在對角線存活**」的特殊形狀，視覺上以「藍色圓點 stack」表示對角元素 $d_1, d_2, \ldots$。

---

### 數學要點

設 $A \in \mathbb{R}^{m \times n}$（$m$ 行 $n$ 列）、$B \in \mathbb{R}^{m \times n}$（待左乘對象）、$D \in \mathbb{R}^{n \times n}$ 與 $D' \in \mathbb{R}^{m \times m}$ 為對角矩陣。$X \in \mathbb{R}^{n \times n}$ 為可逆方陣（特徵向量矩陣），$\mathbf{c} \in \mathbb{R}^n$ 為向量。$U \in \mathbb{R}^{m \times r}$、$\Sigma \in \mathbb{R}^{r \times r}$ 對角、$V^{\mathrm{T}} \in \mathbb{R}^{r \times n}$。

#### Pattern 對應 §4 視角總表

| Pattern | 公式 | 對應 §4 視角 | 直覺 | §6 用途 |
|---|---|---|---|---|
| **(P1)** | $A B = C$，$B$ 任意 | (MM2) + (Mv2) | 從右乘 → $C$ 列是 $A$ 列的線組 | (MM2) 一般化 |
| **(P2)** | $B A = C$，$B$ 任意 | (MM3) + (vM2) | 從左乘 → $C$ 行是 $A$ 行的線組 | (MM3) 一般化 |
| **(P1')** | $A D = [d_1 \mathbf{a}_1\ \cdots\ d_n \mathbf{a}_n]$ | (MM2) 之特例（$B = D$） | 從右乘對角矩陣 → **每一列各自被一個對角元素縮放** | $Q\Lambda$、$U\Sigma$ |
| **(P2')** | $D' B = [d'_1 \mathbf{b}^*_1; \cdots; d'_m \mathbf{b}^*_m]^{\mathrm{T}}$ | (MM3) 之特例（$A = D'$） | 從左乘對角矩陣 → **每一行各自被一個對角元素縮放** | $\Lambda Q^{\mathrm{T}}$、$\Sigma V^{\mathrm{T}}$ |
| **(P3)** | $X D \mathbf{c} = \sum_p c_p d_p \mathbf{x}_p$ | (P1') + (Mv2) 串接 | $\mathbf{c}$ 先被 $D$ 縮成 $D\mathbf{c}$，再以 $D\mathbf{c}$ 為係數線組 $X$ 的列 | $X e^{\Lambda t} \mathbf{c}$ 通解 |
| **(P4)** | $U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ | (P1') + (MM4) 串接 | $\Sigma$ 先把 $V^{\mathrm{T}}$ 各行縮成 $\sigma_p \mathbf{v}^{\mathrm{T}}_p$，再用 (MM4) 把 $U$ 列 ⊗ 縮放後的行做秩 1 累加 | **特徵值 / SVD 分解共骨架** |

#### (P1) Pattern 1 — 從右乘任意矩陣（列運算）

**公式：** $A B$，其中 $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$ 任意。

由 (MM2) + (Mv2) 知道：

$$
A B = A \begin{bmatrix} \mathbf{b}_1 & \cdots & \mathbf{b}_n \end{bmatrix} = \begin{bmatrix} A\mathbf{b}_1 & \cdots & A\mathbf{b}_n \end{bmatrix}, \qquad A\mathbf{b}_j = \sum_{p=1}^k b_{pj} \mathbf{a}_p
$$

- **直覺：** 從**右**乘 $B$ 是「**列運算**」 — $B$ 每一直立列 $\mathbf{b}_j$ 都是「混合 $A$ 列的配方」。三個 $\mathbf{b}_j$ 各自混出一條 $\mathbf{c}_j$。
- **關鍵推論：** $\mathbf{C}(AB) \subseteq \mathbf{C}(A)$。

#### (P2) Pattern 2 — 從左乘任意矩陣（行運算）

**公式：** $A B$，把 $A$ 視為「左側操作對 $B$」（即 $A$ 是對 $B$ 行做線組的係數矩陣）。對應 (MM3) + (vM2)：

$$
A B = \begin{bmatrix} \mathbf{a}^*_1 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix} B = \begin{bmatrix} \mathbf{a}^*_1 B \\ \vdots \\ \mathbf{a}^*_m B \end{bmatrix}, \qquad \mathbf{a}^*_i B = \sum_{p=1}^k a_{ip} \mathbf{b}^*_p
$$

- **直覺：** 從**左**乘 $A$ 是「**行運算**」 — $A$ 每一橫躺行 $\mathbf{a}^*_i$ 都是「混合 $B$ 行的配方」。三個 $\mathbf{a}^*_i$ 各自混出一條 $\mathbf{c}^*_i$。
- **關鍵推論：** $\mathbf{C}((AB)^{\mathrm{T}}) \subseteq \mathbf{C}(B^{\mathrm{T}})$（即「行空間」遺傳自 $B$）。
- **(P1) ↔ (P2) 對偶口訣：** 「**從右乘看 $B$ 直立列、從左乘看 $A$ 橫躺行**」。

#### (P1') Pattern 1' — 從右乘對角矩陣（純列縮放）

**公式：** 設 $A \in \mathbb{R}^{m \times n}$、$D = \operatorname{diag}(d_1, \ldots, d_n) \in \mathbb{R}^{n \times n}$，則：

$$
A D = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix} \begin{bmatrix} d_1 & & \\ & \ddots & \\ & & d_n \end{bmatrix} = \begin{bmatrix} d_1 \mathbf{a}_1 & d_2 \mathbf{a}_2 & \cdots & d_n \mathbf{a}_n \end{bmatrix}
$$

- **直覺：** 對角矩陣從右乘 → **第 $p$ 直立列被 $d_p$ 縮放**（不混合，純倍率）。視覺上 $A$ 的綠直立列「各自被自己對應的對角元素拉長 / 縮短」。
- **(P1) 的退化情形：** 把 $B$ 設為對角矩陣，(P1) 中「線組混合」退化成「純倍率」 — 每個 $\mathbf{c}_j$ 只用到 $A$ 的一條列（其他係數為 0）。
- **§6 用途：** $S = Q \Lambda Q^{\mathrm{T}}$ 中的 $Q\Lambda$ 步驟 = $Q$ 從右乘 $\Lambda$ → 每個特徵向量 $\mathbf{q}_p$ 被自己的特徵值 $\lambda_p$ 縮放；$A = U \Sigma V^{\mathrm{T}}$ 中的 $U\Sigma$ 步驟同理 → 每個左奇異向量 $\mathbf{u}_p$ 被自己的奇異值 $\sigma_p$ 縮放。

#### (P2') Pattern 2' — 從左乘對角矩陣（純行縮放）

**公式：** 設 $B \in \mathbb{R}^{m \times n}$、$D = \operatorname{diag}(d_1, \ldots, d_m) \in \mathbb{R}^{m \times m}$，則：

$$
D B = \begin{bmatrix} d_1 & & \\ & \ddots & \\ & & d_m \end{bmatrix} \begin{bmatrix} \mathbf{b}^*_1 \\ \vdots \\ \mathbf{b}^*_m \end{bmatrix} = \begin{bmatrix} d_1 \mathbf{b}^*_1 \\ \vdots \\ d_m \mathbf{b}^*_m \end{bmatrix}
$$

- **直覺：** 對角矩陣從左乘 → **第 $p$ 橫躺行被 $d_p$ 縮放**。視覺上 $B$ 的粉紅橫躺行「各自被自己對應的對角元素拉長 / 縮短」。
- **(P2) 的退化情形：** 把 $A$ 設為對角矩陣，(P2) 中「行線組」退化成「純倍率」。
- **§6 用途：** $\Lambda Q^{\mathrm{T}}$ 步驟（$\Lambda$ 從左乘 $Q^{\mathrm{T}}$ → 每個 $\mathbf{q}^{\mathrm{T}}_p$ 被 $\lambda_p$ 縮放）；$\Sigma V^{\mathrm{T}}$ 步驟（$\Sigma$ 從左乘 $V^{\mathrm{T}}$ → 每個 $\mathbf{v}^{\mathrm{T}}_p$ 被 $\sigma_p$ 縮放）。

#### (P1') ↔ (P2') 對偶總表

| 視角 | 公式 | 直覺 | 對應 §4 視角 |
|---|---|---|---|
| **(P1')** $AD$ | 對角矩陣**從右**乘 → **每一直立列**乘對角元素 | 「直立列縮放」（綠列拉長 / 縮短） | (MM2) 之退化 |
| **(P2')** $DB$ | 對角矩陣**從左**乘 → **每一橫躺行**乘對角元素 | 「橫躺行縮放」（粉紅行拉長 / 縮短） | (MM3) 之退化 |

**口訣：** 「**右乘對角 → 縮直立列、左乘對角 → 縮橫躺行**」 — 這是對角矩陣最基礎的視覺角色，整個 §6 都會反覆用到。

#### (P3) Pattern 3 — 三明治 $X D \mathbf{c}$（特徵基底加權線組）

**公式：** 設 $X = [\mathbf{x}_1\ \cdots\ \mathbf{x}_n] \in \mathbb{R}^{n \times n}$（可逆）、$D = \operatorname{diag}(d_1, \ldots, d_n)$、$\mathbf{c} \in \mathbb{R}^n$。則：

$$
X D \mathbf{c} = X \begin{bmatrix} d_1 c_1 \\ d_2 c_2 \\ \vdots \\ d_n c_n \end{bmatrix} = \sum_{p=1}^n c_p\, d_p\, \mathbf{x}_p
$$

**兩步拆解：** ① 先 $D \mathbf{c}$ → 把 $\mathbf{c}$ 的每個分量乘以對應的 $d_p$（這是 (Mv2) 的退化 — 對角矩陣作用在向量上 = 分量逐個縮放）；② 再 $X (D\mathbf{c})$ → 用 $D\mathbf{c}$ 為係數對 $X$ 的列做線組（這是 (Mv2) 標準形式）。

##### §6.4 微分方程 / 遞迴方程的工程動機

**設定：** $A \in \mathbb{R}^{n \times n}$、$\mathbf{u}(0) = \mathbf{u}_0$。考慮兩類動態系統：

$$
\frac{d \mathbf{u}(t)}{dt} = A \mathbf{u}(t) \quad \text{（連續時間）}; \qquad \mathbf{u}_{n+1} = A \mathbf{u}_n \quad \text{（離散時間）}
$$

設 $A$ 有特徵分解 $A = X \Lambda X^{-1}$（$\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$、$X$ 列為特徵向量 $\mathbf{x}_p$），且初始條件可被特徵基底展開：

$$
\mathbf{u}_0 = c_1 \mathbf{x}_1 + \cdots + c_n \mathbf{x}_n \quad \Longleftrightarrow \quad \mathbf{c} = X^{-1} \mathbf{u}_0
$$

則兩類問題的通解都是 (P3) 形式：

$$
\boxed{
\mathbf{u}(t) = e^{At} \mathbf{u}_0 = X e^{\Lambda t} X^{-1} \mathbf{u}_0 = X e^{\Lambda t} \mathbf{c} = \sum_{p=1}^n c_p\, e^{\lambda_p t}\, \mathbf{x}_p
}
$$

$$
\boxed{
\mathbf{u}_n = A^n \mathbf{u}_0 = X \Lambda^n X^{-1} \mathbf{u}_0 = X \Lambda^n \mathbf{c} = \sum_{p=1}^n c_p\, \lambda_p^n\, \mathbf{x}_p
}
$$

對應 (P3) 中的 $D$ 各為「$e^{\Lambda t}$」與「$\Lambda^n$」 — 兩者都是對角矩陣，元素分別是 $e^{\lambda_p t}$ 與 $\lambda_p^n$。

- **直覺三層：** ① 把初始條件 $\mathbf{u}_0$ 用特徵向量基底寫成 $\mathbf{c}$（座標變換）；② 每個特徵分量按自己的特徵值「演化」（連續時間：$e^{\lambda_p t}$ 指數成長 / 衰減；離散時間：$\lambda_p^n$ 幾何級數）；③ 把演化後的分量重新組裝回原座標系（線組 $X$ 列）。
- **特徵值分類：** $\operatorname{Re}(\lambda_p) > 0$ → 該分量爆炸成長；$\operatorname{Re}(\lambda_p) < 0$ → 該分量衰減；$\operatorname{Re}(\lambda_p) = 0, \operatorname{Im}(\lambda_p) \neq 0$ → 純振盪；$|\lambda_p| > 1$（離散）→ 不穩定；$|\lambda_p| < 1$ → 穩定收斂到 0。
- **§6 鋪陳：** (P3) 是「為什麼要做特徵分解」的工程理由 — 解動態系統的標準工具。§6.4 會把這個構造完整展開。

#### (P4) Pattern 4 — 三明治 $U \Sigma V^{\mathrm{T}}$（兩矩陣夾對角的秩 1 之和）

**公式：** 設 $U \in \mathbb{R}^{m \times r}$、$\Sigma = \operatorname{diag}(\sigma_1, \ldots, \sigma_r)$、$V^{\mathrm{T}} \in \mathbb{R}^{r \times n}$。則：

$$
U \Sigma V^{\mathrm{T}} = \underbrace{\begin{bmatrix} \mathbf{u}_1 & \cdots & \mathbf{u}_r \end{bmatrix}}_{U} \underbrace{\begin{bmatrix} \sigma_1 & & \\ & \ddots & \\ & & \sigma_r \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} \mathbf{v}^{\mathrm{T}}_1 \\ \vdots \\ \mathbf{v}^{\mathrm{T}}_r \end{bmatrix}}_{V^{\mathrm{T}}} = \sum_{p=1}^r \sigma_p\, \mathbf{u}_p\, \mathbf{v}^{\mathrm{T}}_p
$$

**兩步拆解：** ① 先 $\Sigma V^{\mathrm{T}}$ → (P2') 縮放每個 $\mathbf{v}^{\mathrm{T}}_p$ 為 $\sigma_p \mathbf{v}^{\mathrm{T}}_p$；② 再 $U(\Sigma V^{\mathrm{T}})$ → (MM4) 把 $U$ 列 ⊗ 縮放後的行做秩 1 累加。

或等價地：① 先 $U \Sigma$ → (P1') 縮放每個 $\mathbf{u}_p$ 為 $\sigma_p \mathbf{u}_p$；② 再 $(U\Sigma) V^{\mathrm{T}}$ → (MM4) 累加。

- **直覺：** **「兩個正交基底 + 一個對角矩陣 = 矩陣的最簡分解」** — $U$ 的列是「結果的基底」、$V^{\mathrm{T}}$ 的行是「來源的基底」、$\Sigma$ 的對角元素 $\sigma_p$ 是「兩基底之間的伸縮率」。
- **(P4) 同時是特徵值與 SVD 的骨架：**
  - **特徵值分解（對稱矩陣）：** $S = Q \Lambda Q^{\mathrm{T}} = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$（兩基底相同 = $Q$）。
  - **SVD（任意矩陣）：** $A = U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$（兩基底不同）。
- **§6 鋪陳：** (P4) 是 (P3) 的「矩陣化」 — (P3) 是 $X D \mathbf{c}$（一個向量），(P4) 是 $U \Sigma V^{\mathrm{T}}$（一個矩陣）。**P3 處理動態系統、P4 處理矩陣分解，都靠對角矩陣承載「按 index 加權」的本質。**

#### (P3) ↔ (P4) 對偶與升級

| 視角 | 公式 | 對角元素角色 | 結果類型 | §6 章節 |
|---|---|---|---|---|
| **(P3)** $X D \mathbf{c}$ | $\sum_p c_p d_p \mathbf{x}_p$ | $d_p = e^{\lambda_p t}$ 或 $\lambda_p^n$ — 動態演化因子 | 向量（$\mathbf{u}(t)$ 或 $\mathbf{u}_n$） | §6.4 特徵值分解 |
| **(P4)** $U \Sigma V^{\mathrm{T}}$ | $\sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ | $\sigma_p$ — 兩基底間的伸縮率 | 矩陣（$A$ 本身） | §6.4 ($Q\Lambda Q^{\mathrm{T}}$) / §6.5 ($U\Sigma V^{\mathrm{T}}$) |

**結論口訣：** 「**對角矩陣 = 按 index 加權**」 — (P1')(P2') 對 column / row 做加權、(P3) 對「特徵分量的動態演化」做加權、(P4) 對「秩 1 圖層的能量」做加權。從 (P1') 到 (P4) 是同一概念的層層升級。

---

### Figure 5.1: Pattern 1, 2 — (P1), (P2)

> **檔案：** `figs-png/Pattern12.png`
> **原書位置：** Figure 7（p.5 上半）

##### 視覺結構 (Visual Structure)

整圖**上下兩排**，上排展示 (P1)、下排展示 (P2)，左右各分三段（左 = 等號形式、中 = 解構成 3 條子等式、右 = 「using …」標籤連回 §4 視角）。

- **上排（P1）：** 左段顯示「3 條綠直立列 $A$ × 3×3 灰底點陣 $B$ = 3 條灰直立列 $C$」；中段把 $C$ 展開成 3 條獨立子等式：「$\mathbf{c}_1 = \bullet \cdot \mathbf{a}_1 + \bullet \cdot \mathbf{a}_2 + \bullet \cdot \mathbf{a}_3$」「$\mathbf{c}_2 = \cdots$」「$\mathbf{c}_3 = \cdots$」（每個 $\bullet$ 是來自 $B$ 直立列的對應分量，淡藍 / 橘 / 紫三色區分對應 $B$ 的 3 直立列）；右段「using MM2 + Mv2」標籤。
- **下排（P2）：** 左段顯示「3 條粉紅橫躺行（縱向 stack）$A$ × 3 條粉紅橫躺行 $B$ = 3 條灰橫躺行 $C$」（注意此處 $A$ 是「從左乘的對象」，視覺上仍標 $B$ 在右、$A$ 在左 — 但**作用方向相反**）；中段展開 3 條子等式：「$\mathbf{c}^*_1 = \bullet \cdot \mathbf{b}^*_1 + \bullet \cdot \mathbf{b}^*_2 + \bullet \cdot \mathbf{b}^*_3$」⋯ ；右段「using MM3 + vM2」標籤。
- **配色：** $A$ 的列綠 `#2ca02c`、$B$ 的行粉紅 `#d62728`、係數藍 / 橘 / 紫圓點對應 §4 中「係數來源」、$C$ 灰填充 `#eeeeee` + 深灰框 `#333333`。

##### 數學內容 (Mathematical Content)

(P1)：$AB = [A\mathbf{b}_1\ A\mathbf{b}_2\ A\mathbf{b}_3] = [b_{11}\mathbf{a}_1+b_{21}\mathbf{a}_2+b_{31}\mathbf{a}_3,\ \ldots]$。

(P2)：$AB = [\mathbf{a}^*_1 B;\ \mathbf{a}^*_2 B;\ \mathbf{a}^*_3 B]$，每行 = $a_{i1}\mathbf{b}^*_1 + a_{i2}\mathbf{b}^*_2 + a_{i3}\mathbf{b}^*_3$。

兩排對比：(P1) 的「係數來自 $B$ 的直立列」與 (P2) 的「係數來自 $A$ 的橫躺行」是嚴格對偶（轉置）。

##### 直覺解讀 (Intuition)

「**從右乘 = 切 $B$ 的直立列做 $A$ 列的線組（P1）；從左乘 = 切 $A$ 的橫躺行做 $B$ 行的線組（P2）**」。這張圖把 §4 (MM2) (MM3) 的核心訊息「**乘法方向決定切誰**」用「3 條子等式並列」的視覺方式強調出來。中央展開的子等式把整個 $C$ 拆成「逐列 / 逐行」獨立計算 — 這對寫程式的人是極自然的視角（NumPy 的 for-loop 視角）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [對角矩陣統一互動] ⭐⭐⭐
> **位置：** Figure 5.1 + Figure 5.2 / §5 / (P1) (P2) (P1') (P2') 統合
> **詳見劇本：** VizScript-01（章末）

---

### Figure 5.2: Pattern 1', 2' — (P1'), (P2')

> **檔案：** `figs-png/Pattern11-22.png`
> **原書位置：** Figure 8（p.5 下半）

##### 視覺結構 (Visual Structure)

整圖**左右兩塊**，左塊 (P1')、右塊 (P2')，每塊各分上下兩段（上 = 色塊等式、下 = 文字描述 + 公式）。

- **左塊（P1' — $AD$，從右乘對角）：** 上段顯示「3 條綠直立列 $A$ × 對角 $D$（用 3 個藍色實心圓點沿對角線排列、其餘位置留白）= 3 條綠直立列 $AD$（與 $A$ 同色但每條被『藍點疊在頂端』 — 視覺暗示『被縮放』）」；下段文字「Applying a diagonal matrix from the right scales each column.」+ 公式 `AD = [a₁ a₂ a₃] diag(d₁, d₂, d₃) = [d₁a₁ d₂a₂ d₃a₃]`。
- **右塊（P2' — $DB$，從左乘對角）：** 上段顯示「對角 $D$（藍點對角排列）× 3 條粉紅橫躺行 $B$（縱向 stack）= 3 條粉紅橫躺行 $DB$（每條疊一個藍點在最左 — 暗示『被縮放』）」；下段文字「Applying a diagonal matrix from the left scales each row.」+ 公式 `DB = diag(d₁, d₂, d₃) [b₁*; b₂*; b₃*] = [d₁b₁*; d₂b₂*; d₃b₃*]`。
- **配色：** $A$ 列綠 `#2ca02c`、$B$ 行粉紅 `#d62728`、對角元素藍 `#1f77b4` 圓點（直徑 12px）；對角矩陣的「非對角位置」**完全留白**（不畫 0 元素，視覺強調「對角矩陣 = 只有對角線存在」）。

##### 數學內容 (Mathematical Content)

(P1')：$A D = [d_1 \mathbf{a}_1\ d_2 \mathbf{a}_2\ d_3 \mathbf{a}_3]$ — 每一直立列被自己對應的對角元素縮放。

(P2')：$D B = [d_1 \mathbf{b}^*_1;\ d_2 \mathbf{b}^*_2;\ d_3 \mathbf{b}^*_3]$ — 每一橫躺行被自己對應的對角元素縮放。

對偶：$(AD)^{\mathrm{T}} = D^{\mathrm{T}} A^{\mathrm{T}} = D A^{\mathrm{T}}$（對角矩陣 $D = D^{\mathrm{T}}$），故 (P1') 與 (P2') 完全是「轉置對稱」的兩面。

##### 直覺解讀 (Intuition)

「**右乘對角 → 縮直立列；左乘對角 → 縮橫躺行**」 — 對角矩陣是矩陣世界中**最簡單的「按 index 加權」工具**，不混合任何資訊，純倍率。這個極簡視覺（綠列被「藍點戴上帽子」拉長 / 縮短）是 §6.4 / §6.5 整個分解骨架的視覺起點 — $Q\Lambda$ 之 $\Lambda$、$U\Sigma$ 之 $\Sigma$，都是這個「列縮放動畫」。讀者若能在 0.5 秒內看懂 (P1')、就有資格挑戰 (P4)；若能再 0.5 秒看懂 (P4)、SVD 的視覺骨架已掌握 80%。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [對角矩陣統一互動] ⭐⭐⭐
> **位置：** Figure 5.1 + Figure 5.2 / §5 / 4 個 Pattern 統合
> **核心概念：** 一鍵切換 (P1) (P2) (P1') (P2') 看「右 / 左乘」與「任意 / 對角」二維對比
> **互動梗概：** 4 個 tab 切換 + 對角元素 slider 拉動時看到「綠列各自被縮放」的動畫；切換成 (P1) 時 $B$ 從對角矩陣補滿成任意矩陣，視覺上出現「線組混合」效果
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-04** [數值步進] ⭐
> **位置：** Figure 5.2 / §5 / (P1') 數值 walkthrough
> **詳見劇本：** VizScript-04（章末，輕量版）

---

### Figure 5.3: Pattern 3 — (P3) — $X D \mathbf{c}$ 三明治

> **檔案：** `figs-png/Pattern3.png`
> **原書位置：** Figure 9（p.6）

##### 視覺結構 (Visual Structure)

整圖**橫向布局**，左中右三段。

- **左段：** 「3 條綠直立列 $X$（$\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3$）× 對角 $D$（藍點 stack）× 一條紫色實心直立列 $\mathbf{c}$（紫圓點 stack 縱向 3 個）」 — 三明治結構左半邊。
- **中段：** 「$=$」 + 三項相加 「$\bullet \cdot \mathbf{x}_1 + \bullet \cdot \mathbf{x}_2 + \bullet \cdot \mathbf{x}_3$」 — 每個 $\bullet$ 是「藍 + 紫」雙圓點（暗示『$d_p \cdot c_p$』兩因子相乘）疊在綠列前。
- **右段：** 文字描述「This pattern makes another combination of columns. You will encounter this in differential/recurrence equations.」+ 完整公式 `XDc = [x₁ x₂ x₃] diag(d₁, d₂, d₃) [c₁; c₂; c₃] = c₁d₁x₁ + c₂d₂x₂ + c₃d₃x₃`。
- **配色：** 特徵向量 $X$ 列綠（與 $A$ 列同色，提示「列空間概念繼承」）、對角 $D$ 元素藍、係數向量 $\mathbf{c}$ 紫 `#9467bd`（新色 — 為「特徵基底中的座標」獨立配色）、結果項中的雙圓點是「藍 + 紫」並排顯示 $d_p \cdot c_p$。

##### 數學內容 (Mathematical Content)

$X D \mathbf{c} = X \begin{bmatrix} d_1 c_1 \\ d_2 c_2 \\ d_3 c_3 \end{bmatrix} = c_1 d_1 \mathbf{x}_1 + c_2 d_2 \mathbf{x}_2 + c_3 d_3 \mathbf{x}_3$ — 三因子相乘 $\sum c_p d_p \mathbf{x}_p$。

兩步拆解：
1. **先 $D \mathbf{c}$**（(Mv2) 退化）：$\mathbf{c}$ 各分量被對應對角元素縮放，得到新向量 $D\mathbf{c} = (d_1 c_1, d_2 c_2, d_3 c_3)^{\mathrm{T}}$。
2. **再 $X (D\mathbf{c})$**（(Mv2) 標準）：用 $D\mathbf{c}$ 為係數對 $X$ 列做線組。

或等價地：先 $X D$（(P1') 縮放 $X$ 各列為 $d_p \mathbf{x}_p$）、再 $(XD) \mathbf{c}$（(Mv2) 線組）。

**§6.4 微分 / 遞迴方程通解的具體實例：**

- 連續：$\mathbf{u}(t) = X e^{\Lambda t} \mathbf{c} = \sum c_p e^{\lambda_p t} \mathbf{x}_p$，這裡 $D = e^{\Lambda t} = \operatorname{diag}(e^{\lambda_p t})$。
- 離散：$\mathbf{u}_n = X \Lambda^n \mathbf{c} = \sum c_p \lambda_p^n \mathbf{x}_p$，這裡 $D = \Lambda^n = \operatorname{diag}(\lambda_p^n)$。

##### 直覺解讀 (Intuition)

(P3) 的精髓是「**換基底 → 各分量獨立演化 → 換回原基底**」三段式：

1. **換基底：** $\mathbf{c} = X^{-1} \mathbf{u}_0$，把原座標 $\mathbf{u}_0$ 換成「特徵基底中的座標 $\mathbf{c}$」。
2. **各分量獨立演化：** 在特徵基底裡，$A$ 變成對角矩陣 $\Lambda$，每個分量 $c_p$ 各自按 $e^{\lambda_p t}$ 或 $\lambda_p^n$ 演化（互不干擾） — 這就是對角矩陣 $D$ 出現的原因。
3. **換回原基底：** $X (D\mathbf{c})$ 把演化後的特徵分量重新組裝回原座標。

**為何要做特徵分解？** 因為「**對角矩陣容易處理 — 無耦合**」。沒有特徵分解的話，連續系統需要解 $n$ 個耦合微分方程；做了特徵分解 $A = X \Lambda X^{-1}$，就變成 $n$ 個獨立的標量方程（每個只涉及一個 $\lambda_p$）。**(P3) 是「為什麼特徵值是工程師的最好朋友」的視覺答案。**

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-02** [P3 動態系統 demo] ⭐⭐⭐
> **位置：** Figure 5.3 / §5 / (P3) + §6.4 鋪陳
> **核心概念：** 拉時間 $t$ slider 看 $\mathbf{u}(t) = \sum c_p e^{\lambda_p t} \mathbf{x}_p$ 的軌跡，分量按特徵值各自演化
> **詳見劇本：** VizScript-02（章末）

---

### Figure 5.4: Pattern 4 — (P4) — $U \Sigma V^{\mathrm{T}}$ 三明治

> **檔案：** `figs-png/Pattern4.png`
> **原書位置：** Figure 10（p.7）

##### 視覺結構 (Visual Structure)

整圖**橫向布局**，左中右三段。

- **左段：** 「3 條綠直立列 $U$（$\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$）× 對角 $\Sigma$（藍點 stack）× 3 條粉紅橫躺行 $V^{\mathrm{T}}$（縱向 stack）」 — 完整三明治結構。
- **中段：** 「$=$」 + 三個秩 1 矩陣方塊相加 「$\sigma_1 \mathbf{u}_1 \mathbf{v}^{\mathrm{T}}_1 + \sigma_2 \mathbf{u}_2 \mathbf{v}^{\mathrm{T}}_2 + \sigma_3 \mathbf{u}_3 \mathbf{v}^{\mathrm{T}}_3$」 — 每個秩 1 矩陣方塊用「灰底 + 一條綠直立列疊在最左 + 一條粉紅橫躺行疊在最上 + 藍圓點在交叉處」的「**十字交叉**」視覺表示「綠 ⊗ 粉紅」外積結構。秩 1 矩陣**方塊間**有「+」號連接、最左有「$=$」連接到三明治。
- **右段：** 文字描述「A matrix is broken down to a sum of rank 1 matrices, as in singular value/eigenvalue decomposition.」+ 完整公式 `UΣVᵀ = [u₁ u₂ u₃] diag(σ₁, σ₂, σ₃) [v₁ᵀ; v₂ᵀ; v₃ᵀ] = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + σ₃u₃v₃ᵀ`。
- **配色：** $U$ 列綠、$V^{\mathrm{T}}$ 行粉紅、$\Sigma$ 對角藍點（點直徑與 P3 同 12px，提示「同類角色」）、秩 1 矩陣方塊內部灰填 + 邊框 `#333333` 凸顯外積結構。

##### 數學內容 (Mathematical Content)

$U \Sigma V^{\mathrm{T}} = \sum_{p=1}^r \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ — 三因子相乘等於 $r$ 個秩 1 矩陣按 $\sigma_p$ 加權後相加。

兩步拆解（兩種等價路徑）：
- **路徑 A：** 先 $\Sigma V^{\mathrm{T}}$（(P2') 縮放每行為 $\sigma_p \mathbf{v}^{\mathrm{T}}_p$），再 $U(\Sigma V^{\mathrm{T}})$（(MM4) 累加）。
- **路徑 B：** 先 $U \Sigma$（(P1') 縮放每列為 $\sigma_p \mathbf{u}_p$），再 $(U\Sigma) V^{\mathrm{T}}$（(MM4) 累加）。

**重要特例：**
- **特徵值分解（對稱矩陣）：** $S = Q \Lambda Q^{\mathrm{T}}$ — 同一個正交矩陣 $Q$ 同時擔任「左基底」與「右基底」（轉置版）。$Q\Lambda Q^{\mathrm{T}} = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$。
- **SVD（任意矩陣）：** $A = U \Sigma V^{\mathrm{T}}$ — 兩個不同的正交矩陣 $U, V$ 分別是「左 / 右」基底。
- **共通骨架：** 都是「**正交基底 + 對角矩陣 + 正交基底**」的三明治。**對角元素的大小決定該秩 1 圖層的「能量」**，取前 $k$ 大者是最佳低秩近似（Eckart–Young）。

##### 直覺解讀 (Intuition)

(P4) 是 (MM4) 的「**結構化版本**」 — (MM4) 對任何 $AB$ 都成立，但 (P4) 加了三個約束讓拆解「最有意義」：

1. **$U$ 與 $V$ 都正交**（$U^{\mathrm{T}} U = I$、$V^{\mathrm{T}} V = I$） → 秩 1 圖層之間「**幾何上正交**」，互不干擾。
2. **對角矩陣 $\Sigma$ 元素非負且降冪排列**（$\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$） → 「**前面的圖層比後面的重要**」 — 截斷時保留前 $k$ 個自動是最佳。
3. **唯一性：** 對任何 $A$，這樣的 $U, \Sigma, V$ 存在且基本唯一（差異僅在 $\sigma$ 重複時的旋轉自由度）。

**為何 (P4) 是「整本書的終點」？** 因為它把 §1（4 視角看矩陣）、§2（向量乘法）、§3（矩陣 × 向量）、§4 (MM4)（外積之和）、§5 (P1')(P2')（對角縮放）全部整合到一個結構裡。**讀完 (P4) 等於讀完整本書的視覺骨架**，§6 後面的 5 個分解都只是「填細節 + 加性質約束」。

> 💡 **與 ch04 VizScript-02 的關係：** ch04 已用 Mona Lisa 64×64 SVD 做完整動畫示範「秩 1 圖層累加 + 截斷誤差」，本章不重做 — 直接 pointer 到 ch04，僅在 VizScript-03 補一個「**P4 三明治結構互動**」（Tier 1 輕量版）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-03** [P4 三明治結構] ⭐⭐
> **位置：** Figure 5.4 / §5 / (P4) + §6.4 / §6.5 鋪陳
> **詳見劇本：** VizScript-03（章末，精簡 — 累加動畫指向 ch04 VizScript-02）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: 對角矩陣統一互動（P1 / P2 / P1' / P2' Toggle）

##### A. 一句話定位
單一畫面 4 個 tab 切換 (P1) (P2) (P1') (P2')，看「**右乘 / 左乘**」與「**任意矩陣 / 對角矩陣**」二維對比 — 對角矩陣 slider 拉動時，視覺即時呈現「綠直立列被自己的對角元素拉長 / 縮短」（P1'）或「粉紅橫躺行被自己的對角元素拉長 / 縮短」（P2'）的純倍率動畫；切換到 (P1) (P2) 時 $B$ / $A$ 從對角矩陣「補滿」成任意矩陣，視覺上出現「線組混合」漸入效果。

##### B. 學習目標（Learning Outcome）
- 使用者能在 4 個 tab 之間自由切換並指出每個視角下「縮放對象 / 縮放因子」的視覺位置。
- 使用者能說出「右乘對角 → 縮直立列、左乘對角 → 縮橫躺行」口訣。
- 使用者能在「對角元素 → 任意元素」漸入動畫中觀察到「(P1') 是 (P1) 的退化、(P2') 是 (P2) 的退化」。
- 使用者能拉 $d_p$ 滑桿到 0 看到對應直立列 / 橫躺行「整條消失」 — 直觀理解「對角元素為 0 = 該維度被刪除」（連到 §6.5 SVD 的低秩截斷）。
- 使用者能在切換 (P1) ↔ (P2) 時觀察到視覺上的「**轉置對稱**」 — 兩者完全是「左 ↔ 右、列 ↔ 行」鏡像。

##### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$（綠直立列 stack）、矩陣 $B \in \mathbb{R}^{m \times n}$（粉紅橫躺行 stack）、對角矩陣 $D \in \mathbb{R}^{n \times n}$（藍點 stack）、結果矩陣 $C$（依模式以「縮放後的綠 / 粉紅」表示）。
- **預設值：** $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$、$D = \operatorname{diag}(1, 2, 3)$、$B = D$（初始狀態 (P1') = (P1) 的退化）。
- **維度範圍：** $m, n \in [2, 5]$（保持 cell 視覺清晰）。
- **數值範圍：** $a_{ij}, b_{ij} \in [-9, 9]$ 步進 1；$d_p \in [-3, 3]$ 步進 0.5（對角元素範圍縮小，便於觀察直立列「拉長 / 縮短」效果）。
- **退化情形：**
  - $D = I$：(P1') (P2') 結果與輸入完全相同（無縮放）。
  - $d_p = 0$ 對某 $p$：對應第 $p$ 直立列 / 橫躺行整條變灰、消失。
  - $D$ 元素全相同 = $\alpha$：所有列 / 行被同一倍率縮放（純標量乘法 $\alpha A$）。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 65% 主舞台 + 中 10% 公式區 + 下 25% 控制列。
- **主舞台：** 1100×360 px 白底，左 30% 顯示「左乘運算元」、中 10% 顯示乘號、右 30% 顯示「右乘運算元」、再右 30% 顯示等號 + 結果。依模式不同，左 / 右運算元身分對調：
  - **(P1) mode：** 左 = $A$（綠直立列）、右 = $B$（任意，灰底 + 細格線）。
  - **(P2) mode：** 左 = $A$（任意，灰底 + 細格線）、右 = $B$（粉紅橫躺行）。
  - **(P1') mode：** 左 = $A$（綠直立列）、右 = $D$（藍點對角，無背景框）。
  - **(P2') mode：** 左 = $D$（藍點對角）、右 = $B$（粉紅橫躺行）。
- **對角矩陣表現：** 藍圓點直徑 14px，沿對角線排列，**非對角位置完全留白**（不畫 0 元素，視覺強調「只有對角線存在」）。
- **結果區色塊：** 縮放後的列 / 行用「原色 + 寬度依 $|d_p|$ 比例縮放」呈現（如 $d_2 = 2$ 時第 2 列寬度變 2 倍；$d_2 = 0.5$ 時變 0.5 倍）。負 $d_p$ 用「漸層斜線」紋理表示「方向反轉」。
- **配色：** 綠 `#2ca02c` / 粉紅 `#d62728` / 藍對角 `#1f77b4` / 灰填 `#eeeeee` / 漸層 alpha 0.3 / 負值斜線紋理。
- **公式區：** 即時 LaTeX 14pt mono。
- **字型 / 字級：** 視角標題 18pt sans bold、cell 數字 12pt mono、控制列 12pt。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 mode | tab × 4 | P1 / P2 / P1' / P2' | P1' | 即時 + 動畫 |
| $m$ | slider | [2, 5] | 3 | 即時 |
| $n$ | slider | [2, 5] | 3 | 即時 |
| $a_{ij}$（綠列模式時） | slider grid | [-9, 9] step 1 | 1..9 | 即時 |
| $b_{ij}$（粉紅行模式時） | slider grid | [-9, 9] step 1 | 0..0 | 即時 |
| $d_p$（對角模式時） | slider × $n$ | [-3, 3] step 0.5 | 1, 2, 3 | 即時 |
| 「補滿成任意矩陣」 | button | — | — | click → 從 $D$ 漸入到任意 $B$（觸發 800ms 動畫） |
| 公式逐項高亮 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click |

##### F. 輸出畫面細節（Outputs）
- **(P1') 模式：** 結果區 $n$ 條綠直立列各自寬度 = 原寬 × $|d_p|$；每條列上方標 `$d_p \mathbf{a}_p$`；對角矩陣藍點的圓點半徑與 $|d_p|$ 成正比（視覺加強）。
- **(P2') 模式：** 結果區 $m$ 條粉紅橫躺行各自高度 = 原高 × $|d_p|$；每條行左方標 `$d_p \mathbf{b}^*_p$`。
- **(P1) 模式：** 結果區 $n$ 條綠直立列，每條為「$A$ 列的線性組合」，顯示「$\mathbf{c}_j = b_{1j}\mathbf{a}_1 + b_{2j}\mathbf{a}_2 + \ldots$」公式 + 各 $\mathbf{a}_p$ 對應位置以淡色虛線連到結果列。
- **(P2) 模式：** 對偶行為。
- **公式區：** 依模式即時 LaTeX 顯示對應 (P1)–(P2') 之一。
- **左下角狀態列：** `mode: P1' | shape: (3×3)·diag(d) = (3×3) | scale: [1, 2, 3]`。

##### G. 互動行為（Interactions）
- **切換 mode tab：** 觸發 600ms 切換動畫（見 §H）；公式區同步切換 LaTeX。
- **拉動 $d_p$ slider：** 對應第 $p$ 直立列 / 橫躺行寬度（高度）即時更新，動畫 200ms ease-out。
- **拉動 $a_{ij}$ / $b_{ij}$ slider：** cell 內數字立即更新；對應位置高亮 200ms。
- **「補滿成任意矩陣」button：** 從當前對角矩陣 $D$ 漸入到隨機 $B$（800ms），逐 cell 從 0 漸入；動畫過程中視覺上「從 (P1') 漸變成 (P1)」，幫助理解兩者關係。
- **拉動 $m$ / $n$ slider：** 矩陣形狀重繪 + slider grid 重建。
- **快捷鍵：** `1`–`4` → 切到對應 mode、`Space` → mode 循環、`R` → reset、`F` → 觸發「補滿」按鈕。

##### H. 動畫腳本（mode 切換）
- **(P1') → (P1)：**「右側 $D$ 對角藍點 stack 漸入填滿成隨機 $B$ 灰色 cell（800ms 整體 fade-in）」+「結果區的綠列從『純倍率縮放』漸變為『線組混合』顯示淡色虛線連線」。
- **(P1) → (P2)：**「整個畫面左右鏡像翻轉」+「綠列 ↔ 粉紅行對調」+「公式同步翻轉」+「左 / 右運算元身分交換」。動畫 600ms。
- **(P2) → (P2')：**「左側 $A$ 灰色 cell 漸出收回成 $D$ 藍點 stack」+「結果區粉紅行從『線組混合』漸變為『純倍率縮放』」。
- **(P2') → (P1')：**「整個畫面左右鏡像翻轉」+「粉紅行 ↔ 綠列對調」+「對角矩陣從左移到右」。
- **總長度：** 600ms（mode 內切換）/ 800ms（含「補滿」漸入）。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。

##### I. 邊界與錯誤處理
- **$D$ 元素全為 0：** 結果矩陣全 0、灰底 + 提示「對角全 0 = 結果為 0 矩陣」。
- **某 $d_p = 0$：** 對應列 / 行漸隱（opacity 1 → 0.15）+ 邊框虛線 + tooltip「該維度被刪除（rank 降 1）」。
- **拖動 slider 過快：** debounce 30ms。
- **mode 切換中再切換：** 動畫 reverse 後接續到目標。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - P1' tab：「右乘對角 → 縮列：第 $p$ 直立列 × $d_p$」
  - P2' tab：「左乘對角 → 縮行：第 $p$ 橫躺行 × $d_p$」
  - P1 tab：「右乘任意 = 列線組（混合）」
  - P2 tab：「左乘任意 = 行線組（混合）」
  - $d_p$ slider：「拉到 0 看該列消失（rank 降 1）」
  - 「補滿」button：「看 (P1') 怎麼漸變成 (P1) — 對角 → 任意」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 (P1')：右乘對角矩陣 → 每一綠直立列被自己的藍點縮放」
  - Step 2：「拉 $d_2$ 滑桿從 1 到 3，看第 2 列變寬」
  - Step 3：「拉 $d_2$ 到 0，看第 2 列消失 — rank 降 1」
  - Step 4：「按 `2` 切到 (P2')：對角矩陣移到左邊、改為縮行」
  - Step 5：「按『補滿』看 (P1') → (P1) 的漸變」
- **常見誤解警示：**
  - 「對角矩陣不一定是方陣 — 可以是 $m \times n$ 對角（非對角位置 0），但本章假設方陣以避免混淆」
  - 「右乘對角 ≠ 左乘對角，矩陣乘法不可交換 — 視覺上很明顯：縮列 ≠ 縮行」
- **延伸閱讀：** 原書 p.5–6、§6.4 ($Q\Lambda Q^{\mathrm{T}}$)、§6.5 ($U\Sigma V^{\mathrm{T}}$)。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + matplotlib.animation + marimo.ui。
- **替代方案：** Streamlit + Plotly。
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫綠列 / 粉紅行 / 灰塊。
  - `matplotlib.patches.Circle` 畫藍對角圓點。
  - `matplotlib.transforms.Affine2D().scale()` 處理「列寬隨 $d_p$ 變化」。
  - `marimo.ui.tabs` (4 modes)、`marimo.ui.slider`、`marimo.ui.array`。
  - `numpy.diag` / `numpy.outer` 計算。
- **檔案結構：**
  ```
  viz/
    ch05_patterns.py             # 主入口（含 VizScript-01 / 02 / 03 / 04）
    _common/
      palette.py                 # 沿用 §1–§4 配色
      matrix_canvas.py           # 沿用：綠列 / 粉紅行 / 灰塊原語
      diagonal_widget.py         # 新增：對角矩陣藍點 stack（含 d_p slider 綁定）
  ```
- **效能：** mode 切換動畫預先計算所有 keyframe；slider 拖動 debounce 30ms。
- **測試：** 4 modes 各 1 張 snapshot；$d_p = 0$ 退化 1 張；「補滿」漸入中段 t=400ms 1 張。

##### L. 驗收標準（Acceptance Criteria）
- [ ] 4 mode tab 切換動畫 ≤ 600ms，60fps。
- [ ] 拉 $d_p$ slider 即時更新對應列 / 行寬度，動畫 ≤ 200ms。
- [ ] $d_p = 0$ 時對應列 / 行 opacity 0.15、邊框虛線、tooltip 顯示「rank 降 1」。
- [ ] 「補滿」button 觸發 800ms 漸入動畫 — 從對角到任意矩陣。
- [ ] 公式區 LaTeX 渲染 < 50ms。
- [ ] Walkthrough 5 步驟自動觸發。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 4 mode 純並列靜態圖、無動畫切換、$d_p$ slider 改用文字 input。
- **Tier 3 擴充：** + 加 3D 視窗顯示「綠列縮放」對列空間幾何的影響（$d_p$ 改變 → 列空間從 3D 平面退化成 2D 直線等）。
- **估時：** 1 session

---

#### VizScript-02: P3 動態系統互動（$X D \mathbf{c}$ 與微分 / 遞迴方程）

##### A. 一句話定位
拉時間 $t$ slider 看 $\mathbf{u}(t) = \sum_p c_p e^{\lambda_p t} \mathbf{x}_p$ 的軌跡演化（連續模式）或拉步數 $n$ slider 看 $\mathbf{u}_n = \sum_p c_p \lambda_p^n \mathbf{x}_p$ 的軌跡跳躍（離散模式）；左側 (P3) 三明治結構 $X D \mathbf{c}$ 的對角元素 $d_p = e^{\lambda_p t}$（或 $\lambda_p^n$）即時更新；右側 2D / 3D 軌跡圖即時顯示 $\mathbf{u}$ 在原座標空間的位置 + 各特徵分量分解的「彩色子向量」。

##### B. 學習目標（Learning Outcome）
- 使用者能在「拉 $t$ 滑桿」時直觀感受「**特徵分量按特徵值各自演化**」 — $\lambda > 0$ 分量爆炸、$\lambda < 0$ 分量衰減、$\lambda = 0$ 分量靜止。
- 使用者能說出「(P3) = 換特徵基底 + 各分量獨立演化 + 換回原基底」三步驟。
- 使用者能解釋「對角矩陣為什麼出現 — 因為特徵基底中無耦合」。
- 使用者能在「離散 vs 連續」切換中觀察到 $\lambda^n$ 與 $e^{\lambda t}$ 的差異（$\lambda > 1$ 離散爆炸 vs $\operatorname{Re}(\lambda) > 0$ 連續爆炸）。
- 使用者能在「複數特徵值」demo 中觀察到「振盪 + 衰減 / 成長」的螺旋軌跡（連到 §6.4 的振盪解）。

##### C. 待視覺化的數學物件
- **物件清單：** 特徵向量矩陣 $X = [\mathbf{x}_1, \ldots, \mathbf{x}_n]$（綠直立列 stack）、特徵值對角矩陣 $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$、初始條件係數 $\mathbf{c} = X^{-1} \mathbf{u}_0$（紫直立向量）、時間 $t$（或步數 $n$）、即時對角矩陣 $D(t) = e^{\Lambda t}$（或 $\Lambda^n$）、結果向量 $\mathbf{u}(t) = X D(t) \mathbf{c}$。
- **預設值（兩種模式）：**
  - **2D demo（穩定吸引子）：** $A = \begin{bmatrix} -0.5 & 0 \\ 0 & -0.2 \end{bmatrix}$（已對角，$\lambda_1 = -0.5, \lambda_2 = -0.2$，$\mathbf{x}_1 = (1, 0)^{\mathrm{T}}, \mathbf{x}_2 = (0, 1)^{\mathrm{T}}$），$\mathbf{u}_0 = (3, 2)^{\mathrm{T}}$ → 軌跡螺旋收斂到原點（$t \to \infty$）。
  - **2D demo（振盪）：** $A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$（$\lambda = \pm i$），純振盪、軌跡是圓。
  - **3D demo：** 自訂 $3 \times 3$ 矩陣，使用者拉 slider 設特徵值。
- **維度範圍：** $n \in \{2, 3\}$（高維無法視覺化軌跡）。
- **數值範圍：** $\lambda_p \in [-2, 2]$（避免數值溢位）；$t \in [0, 10]$ 步進 0.05；$n \in [0, 50]$ 步進 1（離散）。
- **退化情形：**
  - $\lambda_p = 0$：對應分量靜止不動。
  - $\mathbf{c}$ 在某個 $\mathbf{x}_p$ 方向分量為 0：該分量永遠不出現在軌跡中。
  - 重複特徵值：不可對角化的情況提示「使用 Jordan form」（不在本互動範圍）。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 60% 主舞台（左 40% (P3) 結構 + 右 60% 軌跡圖） + 中 15% 分量分解條 + 下 25% 控制列。
- **(P3) 結構區：** 顯示 $X D(t) \mathbf{c}$ 三明治，$D(t)$ 的藍對角圓點半徑隨 $|d_p(t)|$ 即時變化（$d_p$ 變大 → 藍點變大 + 加深，$d_p$ 變小 → 縮小 + 變淡）；右下角同時顯示「兩步拆解」迷你縮圖：① $D\mathbf{c}$ 中間結果向量、② $X(D\mathbf{c})$ 結果。
- **軌跡圖（2D）：** 600×480 px 笛卡兒座標系，原點居中、軸範圍依預設自適應；軌跡用「藍實線 + 不同 $t$ 點用淡 → 深漸變」顯示完整路徑；當前 $\mathbf{u}(t)$ 用紫色實心圓點標記；初始 $\mathbf{u}_0$ 用空心圓點標記；特徵向量 $\mathbf{x}_1, \mathbf{x}_2$ 從原點畫綠箭頭（長度依 $|c_p \mathbf{x}_p|$）。
- **軌跡圖（3D）：** 同上但用 plotly.graph_objects.Scatter3d 或 matplotlib 3D；旋轉 / 縮放互動。
- **分量分解條：** 中 15% 區域顯示 $n$ 條「彩色長條」，每條長度 = $|c_p e^{\lambda_p t}|$（連續）或 $|c_p \lambda_p^n|$（離散）、顏色依特徵值正負（藍 = 衰減 / 紅 = 成長 / 綠 = 振盪）。
- **配色：** 特徵向量 $\mathbf{x}_p$ 綠 `#2ca02c`、對角元素藍 `#1f77b4`、初始 $\mathbf{c}$ 紫 `#9467bd`、軌跡藍 `#1f77b4` 漸變、分量條依正負（衰減藍 / 成長紅 / 振盪綠）。
- **字型 / 字級：** 軌跡圖座標 12pt、分量條標籤 11pt、控制列 12pt。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 模式 | radio | 連續 / 離散 | 連續 | 切換重建 |
| $t$（連續） | slider | [0, 10] step 0.05 | 0 | 即時 |
| $n$（離散） | slider | [0, 50] step 1 | 0 | 即時 |
| play / pause | button | — | pause | click |
| 自動播放速度 | slider | 50ms – 1s / step | 200ms | 即時 |
| 預設 demo | radio | 穩定 / 振盪 / 不穩定 / 自訂 | 穩定 | 切換重建 |
| $\lambda_p$（自訂模式） | slider × $n$ | [-2, 2] step 0.1 | 預設值 | 即時 |
| $\mathbf{x}_p$（自訂模式） | slider grid | [-3, 3] step 0.1 | 預設值 | 即時 |
| $\mathbf{u}_0$（自訂） | slider × $n$ | [-5, 5] step 0.1 | (3, 2, 0...) | 即時 |
| 顯示分量分解 | checkbox | on / off | on | 即時 |
| 顯示軌跡尾跡 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click |

##### F. 輸出畫面細節（Outputs）
- **(P3) 結構區：**
  - $X$ 列：固定（不變）。
  - $D(t)$ 對角圓點：半徑 ∝ $|d_p(t)|$，顏色依正負（藍 / 紅）；hover 顯示 `$d_p(t) = e^{\lambda_p t} = 0.61$` 之類數字。
  - $\mathbf{c}$：固定（不變）。
  - 中間 $D\mathbf{c}$：紫色 stack，每個元素 = $d_p(t) c_p$，即時更新。
  - 結果 $\mathbf{u}(t)$：紫色實心向量，與軌跡圖紫點同步。
- **軌跡圖：**
  - 完整軌跡曲線（漸變色）。
  - 當前位置紫點（直徑 8px）。
  - 特徵向量綠箭頭（長度即時 = $|c_p e^{\lambda_p t}|$）。
  - 「+」分解：$\mathbf{u}(t) = c_1 e^{\lambda_1 t} \mathbf{x}_1 + c_2 e^{\lambda_2 t} \mathbf{x}_2$ 顯示為「兩條彩色子向量首尾相接」（從原點 → 第一個分量端點 → $\mathbf{u}(t)$）。
  - 角落顯示 `$t = 2.30 \mid \mathbf{u}(t) = (1.20, 1.32)^{\mathrm{T}}$`。
- **分量分解條：** $n$ 條長條 + 即時數字 `$c_1 e^{\lambda_1 t} = 1.20$`、`$c_2 e^{\lambda_2 t} = 0.85$`。
- **公式區：** `$\mathbf{u}(t) = X e^{\Lambda t} \mathbf{c} = \sum_p c_p e^{\lambda_p t} \mathbf{x}_p$` 即時 LaTeX。

##### G. 互動行為（Interactions）
- **拉 $t$ slider：** 軌跡圖紫點即時移動；(P3) 結構區藍點半徑同步更新；分量條長度同步更新。
- **play 自動播放：** $t$ 從 0 到 10 自動推進，到達後暫停 1 秒、重設 $t = 0$ 再循環。
- **切換模式：** 連續 → 離散時 $t$ slider 變 $n$ slider，軌跡從連續曲線變「離散點 stack」（每個點之間用淡灰虛線連接表示「跳躍順序」）。
- **切換 demo：** 軌跡圖、分量條、(P3) 結構區全部重繪；保留前一個 demo 的軌跡淡灰色作為對比 1 秒後消失。
- **拉 $\lambda_p$ slider（自訂模式）：** 軌跡完全重算 + 重繪；提示「特徵值改變導致軌跡質變」。
- **快捷鍵：** `Space` play / pause、`→` $t$ += 0.1、`←` $t$ -= 0.1、`R` reset、`D` 切換 demo（循環）、`M` 切換模式。

##### H. 動畫腳本（時間演化）
- **每 frame（$t$ 增加 $\Delta t$）：**
  - **t → t+Δt（200ms 預設速度）：**
    - **0–30ms：** 計算新 $\mathbf{u}(t+\Delta t)$ + $D(t+\Delta t)$ 的對角元素。
    - **30–150ms：** 軌跡圖紫點滑動到新位置（lerp）；尾跡延伸；分量子向量端點同步移動。
    - **30–150ms：** (P3) 結構區藍點半徑 lerp 到新值；分量條長度 lerp。
    - **150–200ms：** 數字字級閃一下提示變化（特別當 $|d_p|$ 改變超過 20% 時）。
- **緩動：** linear（時間軸最自然）。
- **倒退（拉 $t$ slider 往左）：** 軌跡曲線「縮回」到當前 $t$，紫點移到對應位置。

##### I. 邊界與錯誤處理
- **$\lambda > 0$ 大值（成長爆炸）：** 軌跡延伸超出畫布時自動縮放座標系（座標範圍動態擴大），右上角顯示「auto-zoom: range expanded to ±20」。
- **$\lambda$ 為複數：** 自動切換到「振盪」demo（單獨展示複數特徵值的螺旋）；提示「複數特徵值 → 振盪解」。
- **重複特徵值：** 計算特徵向量時若 $X$ 不可逆（$\det X = 0$），紅色警告「特徵向量不獨立 — Jordan form 需要」+ 暫停動畫。
- **拉 slider 過快：** debounce 50ms。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - $t$ slider：「時間 — 拉動看每個分量按 $e^{\lambda_p t}$ 演化」
  - $\lambda_p$ slider：「特徵值 — 控制第 $p$ 分量的成長 / 衰減速度」
  - 分量條：「$|c_p e^{\lambda_p t}|$ — 該分量目前的能量」
  - (P3) 結構：「對角矩陣 $D(t) = e^{\Lambda t}$ 隨時間變化 — 每個對角元素獨立演化」
- **Walkthrough（首次自動觸發）：**
  - Step 1：「現在 $t = 0$，$D = I$，$\mathbf{u}(0) = \mathbf{u}_0$（初始位置）」
  - Step 2：「拉 $t$ 滑桿到 1.0，看軌跡走出第一段，每個分量按 $e^{\lambda_p}$ 縮放」
  - Step 3：「注意分量條：$\lambda_1 = -0.5$ 的分量越來越短（衰減）」
  - Step 4：「按 play 看完整軌跡螺旋收斂到原點」
  - Step 5：「切到『振盪』demo 看複數特徵值的圓形軌跡」
  - Step 6：「切到『不穩定』demo 看 $\lambda > 0$ 的爆炸軌跡」
- **常見誤解警示：**
  - 「(P3) 中的 $D$ 不是矩陣 $A$ 的對角化 — 是 $e^{\Lambda t}$ 或 $\Lambda^n$，是 $\Lambda$ 的『時間版本』」
  - 「$X$ 是特徵向量矩陣，不是任意可逆矩陣 — 用其他基底拆 $\mathbf{u}_0$ 不會給出無耦合解」
  - 「$e^{\Lambda t}$ ≠ $e^{At}$ 的元素 — 是『先對角化再指數』」
- **延伸閱讀：** 原書 p.6、§6.4 ($Q\Lambda Q^{\mathrm{T}}$)、Strang LAFE Sec. 6.4 Systems of Differential Equations。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + matplotlib.animation（小 demo）；3D demo 建議 Plotly（軌跡互動旋轉 / 縮放品質好）。
- **替代方案：** Streamlit + Plotly。
- **關鍵 API：**
  - `numpy.linalg.eig(A)` 算特徵值與向量。
  - `scipy.linalg.expm(A * t)` 算 $e^{At}$（驗證用）。
  - `numpy.einsum('ij,j,j->i', X, np.exp(eigvals * t), c)` 計算 $\mathbf{u}(t)$。
  - `matplotlib.animation.FuncAnimation` 連續播放。
  - `plotly.graph_objects.Scatter3d` 3D 軌跡。
- **檔案結構：**
  ```
  viz/
    ch05_patterns.py
    _common/
      eig_solver.py              # 特徵值計算 + 退化偵測
      trajectory_plot.py         # 2D / 3D 軌跡共用繪製
      diagonal_widget.py         # 沿用 VizScript-01
  ```
- **效能：** 軌跡預計算 200 個時間點 + cache；slider 拖動只查表；自動播放用 FuncAnimation 60fps。
- **測試：** 4 demo（穩定 / 振盪 / 不穩定 / 自訂）各 1 張 snapshot；$t = 0, 1, 5, 10$ 各 1 張；$\lambda$ 為複數時 1 張。

##### L. 驗收標準（Acceptance Criteria）
- [ ] 拉 $t$ slider 即時更新軌跡紫點 + (P3) 藍點半徑，動畫 ≤ 150ms。
- [ ] 4 個預設 demo 切換流暢、保留前一個軌跡 1 秒。
- [ ] play 自動播放 60fps、可暫停 / 倒退。
- [ ] 自訂模式下拉 $\lambda_p$ slider 軌跡完全重繪 < 200ms。
- [ ] 複數特徵值正確顯示螺旋（不應拋例外）。
- [ ] Walkthrough 6 步驟自動觸發。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純靜態 4 個 demo 並列、無互動 slider。
- **Tier 3 擴充：** + 加「相空間流場」（vector field）疊在軌跡圖背景；+ 不同初始條件多軌跡同畫面對比；+ 連到實際工程例（彈簧質量系統 / 化學反應動力學 / 人口模型）。
- **估時：** 1.5 session（含 demo 配置與 walkthrough）

---

#### VizScript-03: P4 三明治結構（$U \Sigma V^{\mathrm{T}}$ 互動 — 精簡版）

##### A. 一句話定位
靜態 + 輕量互動展示 $U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ 的三明治結構分解；左側顯示三明治、右側顯示秩 1 之和；拉 $\sigma_p$ slider 看「該秩 1 圖層的能量隨 $\sigma_p$ 縮放」 + 切換到「特徵值版（$Q\Lambda Q^{\mathrm{T}}$）」看兩者結構差異 — **不重做累加 / 截斷 demo（指向 ch04 VizScript-02）**。

##### B. 學習目標（Learning Outcome）
- 使用者能說出「(P4) = 兩個正交基底 + 一個對角矩陣」三層結構。
- 使用者能在「$U\Sigma V^{\mathrm{T}}$ ↔ $Q\Lambda Q^{\mathrm{T}}$」切換時觀察「兩基底相同（特徵值）vs 兩基底不同（SVD）」的差異。
- 使用者能拉 $\sigma_p$ slider 看「對應秩 1 圖層的視覺亮度（能量）」隨之變化。
- 使用者能說出「(P4) 是 §6.4 / §6.5 兩大分解的共骨架」。
- 使用者能跟著 pointer 跳到 ch04 VizScript-02 看完整累加 / 截斷動畫。

##### C. 待視覺化的數學物件
- 矩陣 $U \in \mathbb{R}^{m \times r}$（綠列）、$\Sigma = \operatorname{diag}(\sigma_1, \ldots, \sigma_r)$（藍對角）、$V^{\mathrm{T}} \in \mathbb{R}^{r \times n}$（粉紅行）、$r$ 個秩 1 矩陣 $\sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$、最終 $A = U\Sigma V^{\mathrm{T}}$。
- **預設值：** $m = n = 3, r = 3$；$U, V$ 預設為 $3 \times 3$ 旋轉矩陣（互不相同）；$\Sigma = \operatorname{diag}(3, 2, 1)$。
- **特徵值模式預設：** $S = Q \Lambda Q^{\mathrm{T}}$ 中 $Q$ = 旋轉矩陣、$\Lambda = \operatorname{diag}(2, 1, -1)$。
- **退化情形：** $\sigma_p = 0$ 對應秩 1 圖層完全消失；$\sigma_p$ 全相等 → 各圖層能量相同（無「主成分」概念）。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 75% 主舞台 + 下 25% 控制列。
- **主舞台（左右兩塊）：**
  - **左 50%：** 三明治結構 $U \Sigma V^{\mathrm{T}}$（綠 + 藍 + 粉紅）+ 「$=$」+ 完整結果矩陣 $A$（cell heatmap，藍 → 白 → 紅 colormap）。
  - **右 50%：** $r$ 個秩 1 矩陣方塊並列 + 「+」號連接 + 「$=$」+ $A$ 副本。每個秩 1 方塊內畫「綠直立列 + 粉紅橫躺行 + 藍圓點交叉」（沿用 ch04 VizScript-02 的「+ 字交叉」原語）；方塊邊框粗細 ∝ $|\sigma_p|$（視覺強調能量大小）。
- **配色：** 沿用全章配色；秩 1 方塊內熱圖用「藍 → 白 → 紅」colormap。
- **公式區（下緣）：** `$U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$` 即時 LaTeX。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 模式 | radio | SVD ($U\Sigma V^{\mathrm{T}}$) / 特徵值 ($Q\Lambda Q^{\mathrm{T}}$) | SVD | 切換重建 |
| $r$ | slider | [1, 4] | 3 | 即時 |
| $\sigma_p$ / $\lambda_p$ | slider × $r$ | [-3, 3] step 0.5 | 3, 2, 1 / 2, 1, -1 | 即時 |
| 跳到 ch04 VizScript-02 | button | — | — | click → 開新 tab / 跳頁 |
| 重設 | button | — | — | click |

##### F. 輸出畫面細節（Outputs）
- **三明治區：** $\Sigma$ 藍點半徑 ∝ $|\sigma_p|$；hover 顯示 `$\sigma_2 = 2.0$`。
- **秩 1 方塊：** 邊框粗細 ∝ $|\sigma_p|$；hover 第 $p$ 方塊 → tooltip 顯示「$\sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，能量占比 = $\sigma_p^2 / \sum \sigma^2$ = 64.3%」+ 對應 $\mathbf{u}_p$（綠列）+ $\mathbf{v}^{\mathrm{T}}_p$（粉紅行）在三明治中高亮。
- **結果矩陣 $A$：** cell heatmap 即時更新；colormap 範圍依 $\max|A_{ij}|$ 自適應。

##### G. 互動行為（Interactions）
- **拉 $\sigma_p$ slider：** 對應秩 1 方塊邊框粗細即時更新 + 內熱圖顏色強度同步變化；最終 $A$ 重算。
- **拉 $r$ slider：** 秩 1 方塊數量增減（fade in / out 200ms）；三明治結構 $\Sigma$ 對角元素數變化。
- **切換 SVD ↔ 特徵值模式：** 整體重繪 — SVD 模式 $U \neq V$（兩種顏色基底）、特徵值模式 $U = V = Q$（同色，提示「兩基底相同」）。動畫 600ms。
- **「跳到 ch04 VizScript-02」button：** 開新 tab 或跳到對應劇本（看完整累加 / 截斷 / Mona Lisa demo）。

##### H. 動畫腳本
- **無複雜動畫**（Tier 1 設計）；slider 拉動時所有更新即時 < 100ms。
- **模式切換：** 600ms「兩基底融合 / 分離」動畫 — SVD → 特徵值時 $V$ 漸漸轉色融合到 $U$；反向則分離。

##### I. 邊界與錯誤處理
- **$\sigma_p = 0$：** 對應秩 1 方塊變灰底 + 邊框虛線 + 提示「能量 0 — 不貢獻」。
- **$r = 0$：** 結果矩陣全 0、提示「rank 0」。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - SVD mode：「$U, V$ 不同 — 適用任意矩陣」
  - 特徵值 mode：「$U = V = Q$ — 僅適用對稱矩陣」
  - $\sigma_p$ slider：「拉到 0 看該秩 1 圖層消失」
  - 「跳到 ch04」：「看完整累加 / 截斷 / Mona Lisa SVD 影像 demo」
- **Walkthrough（首次自動）：**
  - Step 1：「(P4) = 三明治結構：兩個正交基底 + 對角矩陣」
  - Step 2：「右側秩 1 方塊：每個是 $\sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$」
  - Step 3：「拉 $\sigma_2$ slider 看第 2 個方塊邊框變細 — 能量降低」
  - Step 4：「切到『特徵值』模式看 $U = V = Q$ — 對稱矩陣的特例」
  - Step 5：「想看完整累加 / Mona Lisa demo？按『跳到 ch04』」
- **常見誤解警示：**
  - 「(P4) 不限對稱矩陣 — 但特徵值版需要對稱性」
  - 「$\sigma_p$ 永遠非負；$\lambda_p$ 可以是負或複數」
- **延伸閱讀：** 原書 p.7、§6.4、§6.5、ch04 VizScript-02、Strang LAFE Sec. 7.4。

##### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib（與 VizScript-01 共用畫面框架）。
- **關鍵 API：**
  - `numpy.linalg.svd(A)` 取 $U, \Sigma, V^{\mathrm{T}}$。
  - `numpy.linalg.eigh(S)` 取對稱矩陣特徵值（保證實數）。
  - 沿用 ch04 `_common/rank1_layer.py`。
- **檔案結構：** 沿用 `ch05_patterns.py`，本劇本約 200 行（小型）。

##### L. 驗收標準（Acceptance Criteria）
- [ ] 拉 $\sigma_p$ slider 即時更新 < 100ms。
- [ ] 模式切換動畫 600ms 流暢。
- [ ] 「跳到 ch04 VizScript-02」按鈕功能正確（開新分頁或滾動到對應位置）。
- [ ] $\sigma_p = 0$ 退化處理正確。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 1
- **Tier 2 擴充：** + 「能量重排序」radio（按 $\sigma_p$ 升 / 降序排列秩 1 方塊）+ 「對稱性檢查」按鈕（驗證輸入是否對稱矩陣，不對稱時切回 SVD 模式）。
- **Tier 3 擴充：** 與 ch04 VizScript-02 合併為單一互動，含累加 / 截斷 / Mona Lisa demo（但這在 ch04 已實作，本章不重複）。
- **估時：** 0.5 session

---

#### VizScript-04: P1' 數值步進 walkthrough（輕量版）

##### A. 一句話定位
按播放鍵，從 $\mathbf{a}_1$ 到 $\mathbf{a}_n$ 依序高亮 $A$ 的每一直立列、同時對應的對角元素 $d_p$ 變紅（被選中），動畫顯示 $d_p \mathbf{a}_p$ 從原 $A$ 區域複製、被「藍點戴上帽子」、寬度按 $|d_p|$ 拉伸 / 縮短後落入結果區的對應位置 — 整個 $AD$ 計算過程的純數值 walkthrough。

##### B. 學習目標（Learning Outcome）
- 使用者能跟著動畫一步一步看完 $AD$ 的「**逐列縮放**」過程。
- 使用者能在中學 / 大一程度建立「對角矩陣 = 列縮放器」的具體心智模型。
- 使用者能說出每一步「現在處理第 $p$ 列、被縮放因子是 $d_p$、結果是 $d_p \mathbf{a}_p$」。

##### C. 待視覺化的數學物件
- $A \in \mathbb{R}^{m \times n}$（綠列 stack）、$D = \operatorname{diag}(d_1, \ldots, d_n)$（藍點 stack）、結果 $AD$（綠列被縮放後的 stack）。
- **預設值：** $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$、$D = \operatorname{diag}(2, 0.5, -1)$（含一個 < 1、一個負值，便於展示三種視覺效果）。
- **維度範圍：** $m = n = 3$（固定，輕量版不調尺寸）。
- **退化情形：** $d_p = 0$ 對應列消失（變灰、寬度為 0）。

##### D. 視覺布局（Visual Layout）
- **整體比例：** 上 80% 主舞台 + 下 20% 控制列。
- **主舞台：** 左 30% 顯示 $A$（綠列 stack）、中 15% 顯示 $D$（藍點 stack）+ 「$=$」、右 40% 顯示結果 $AD$（隨動畫逐列填入）+ 上方公式區「$AD = [d_1\mathbf{a}_1\ d_2\mathbf{a}_2\ d_3\mathbf{a}_3]$」逐項高亮。
- **配色：** 沿用；當前處理中的列 / 對角元素用「閃爍橘 `#ff7f0e`」高亮。

##### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| play / pause / reset | button × 3 | — | — | click |
| 速度 | slider | 500ms – 3s / step | 1500ms | 即時 |
| 跳到第 $p$ 步 | slider | [0, n] | 0 | 即時 |
| $d_p$（可選） | slider × n | [-3, 3] step 0.5 | (2, 0.5, -1) | 即時（中斷動畫） |

##### F. 輸出畫面細節（Outputs）
- **動畫每一步：**
  - $A$ 的第 $p$ 列邊框閃爍橘色 200ms。
  - $D$ 的第 $p$ 對角藍點變紅 200ms。
  - 「$d_p \mathbf{a}_p$」標籤在中央上方淡入。
  - 第 $p$ 列被「複製出來」，飛到結果區對應位置 + 寬度 lerp 到 $|d_p|$ 倍 + 若 $d_p < 0$ 加斜線紋理。
- **進度條：** 下方顯示當前處於第 $p$ 步 / 總 $n$ 步。

##### G. 互動行為（Interactions）
- **play：** 按 1500ms / 步速度自動推進，到達 $p = n$ 後暫停。
- **pause：** 暫停在當前步。
- **reset：** 結果區清空、回到 $p = 0$。
- **跳到第 $p$ 步 slider：** 立即跳轉，前 $p$ 步結果靜態顯示。
- **快捷鍵：** `Space` play / pause、`R` reset、`→` 下一步、`←` 上一步。

##### H. 動畫腳本
- **單步（$p \to p+1$）：**
  - **0–200ms：** 第 $p$ 列邊框閃爍橘 + $d_p$ 藍點變紅。
  - **200–600ms：** 列複製出 + 飛到結果區 + 寬度 lerp。
  - **600–1000ms：** 結果區該位置 cell 數字逐個淡入（從上到下）。
  - **1000–1500ms：** 全部 settle，準備下一步。
- **緩動：** ease-out。

##### I. 邊界與錯誤處理
- **$d_p = 0$：** 對應列「消失動畫」（寬度從原寬度 lerp 到 0）+ 結果區留白。
- **$d_p < 0$：** 結果列加斜線紋理 + tooltip「方向反轉」。

##### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - play 按鈕：「逐列看 $AD = [d_1\mathbf{a}_1, d_2\mathbf{a}_2, d_3\mathbf{a}_3]$ 是怎麼算出來的」
  - 速度 slider：「拉慢看清楚每一步的 lerp」
- **Walkthrough：** 與動畫合一，無額外 step。
- **延伸閱讀：** ch05 VizScript-01（看 4 個 Pattern 比較）。

##### K. 技術實作建議
- **首選方案：** Marimo + matplotlib.animation（簡單，無需多模式）。
- **檔案結構：** 整合到 `ch05_patterns.py`，約 100 行。

##### L. 驗收標準
- [ ] 動畫每步 1500ms 流暢。
- [ ] 跳轉 slider 同步前 $p$ 步結果。
- [ ] $d_p < 0$ 與 $d_p = 0$ 退化提示正確。

##### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 1
- **估時：** 0.3 session

---

### 章末延伸

#### 與前面章節的連結

- **§1 (Viewing Matrix - 4 Ways)：** 對角矩陣是「列為單位向量倍數 + 行為單位向量倍數」的特例 — (P1') (P2') 是 §1 第 2 / 第 3 視角的退化版。
- **§2 (Vector × Vector)：** (P3) 中 $D \mathbf{c}$ 是 (Mv2) 的退化（對角矩陣作用在向量 = 分量縮放）；$X(D\mathbf{c})$ 是 (Mv2) 標準式。(P4) 中的秩 1 矩陣 $\mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ 是 §2 (v2) 外積的直接套用。
- **§3 (Matrix × Vector)：** (P3) 整體就是 $X(D\mathbf{c})$ 即 (Mv2) 應用在「對角縮放後的向量」上。
- **§4 (Matrix × Matrix - 4 Ways)：**
  - (P1) = (MM2) + (Mv2) 的整合。
  - (P2) = (MM3) + (vM2) 的整合。
  - (P1') = (MM2) 的退化（$B = D$）。
  - (P2') = (MM3) 的退化（$A = D$）。
  - (P4) = (P1') + (MM4) 串接 — **整個 (MM4) 視角的「結構化版本」**。

#### 後續章節的應用

- **§6.1 ($A = CR$)：** 用 (P1) 視角理解「$C$ 從右乘 $R$ → $A$ 是 $C$ 列的線組」。
- **§6.2 ($A = LU$)：** $L$（單位下三角）從左乘 $U$（上三角）— 用 (P2) 理解「$L$ 行對 $U$ 行做線組」。
- **§6.3 ($A = QR$)：** 同 LU 視角，但 $Q$ 正交。
- **§6.4 ($S = Q \Lambda Q^{\mathrm{T}}$)：** **直接套 (P4) 模板** — $Q$ 從右乘 $\Lambda$ 套 (P1')、結果再從右乘 $Q^{\mathrm{T}}$ 套 (MM4)；最終 $S = \sum \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$。**(P3) 解釋為什麼要做這個分解** — 解動態系統。
- **§6.5 ($A = U \Sigma V^{\mathrm{T}}$)：** **直接套 (P4) 模板** — $U$ 從右乘 $\Sigma$ 套 (P1')、結果再從右乘 $V^{\mathrm{T}}$ 套 (MM4)；最終 $A = \sum \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$。Mona Lisa SVD demo 的視覺基礎在 ch04 VizScript-02。

#### 工程實作的對應

- **(P1') / (P2') 程式視角：** NumPy `A @ np.diag(d)` ≡ `A * d`（廣播自動處理列縮放）；`np.diag(d) @ B` ≡ `d[:, None] * B`（行縮放）。**對角矩陣不應該存成完整 $n \times n$ 矩陣** — 浪費 $n^2 - n$ 個 0。
- **(P3) 程式視角：** 解 $\mathbf{u}(t) = X e^{\Lambda t} X^{-1} \mathbf{u}_0$ 的高效寫法：先算 $\mathbf{c} = X^{-1} \mathbf{u}_0$（一次 `np.linalg.solve`），之後查 $\mathbf{u}(t) = X(\exp(\lambda t) \cdot \mathbf{c})$（每個 $t$ 一次 $O(n^2)$）。比直接 `expm(A * t) @ u0` 快很多（避免每個 $t$ 重算矩陣指數）。
- **(P4) 程式視角：** SVD 截斷只要切片 `A_k = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]`。低秩近似的記憶體成本是 $O(k(m+n))$，遠小於原矩陣 $O(mn)$。

---

### 來源對照

| 內容 | 來源檔案 / 段落 |
|---|---|
| Pattern 文字描述 | `from-tex/en.md` 第 127–203 行 / `from-tex/zh.md` 第 122–196 行 |
| Figure 5.1 (Pattern12.png) | `figs-png/Pattern12.png`（原書 Figure 7） |
| Figure 5.2 (Pattern11-22.png) | `figs-png/Pattern11-22.png`（原書 Figure 8） |
| Figure 5.3 (Pattern3.png) | `figs-png/Pattern3.png`（原書 Figure 9） |
| Figure 5.4 (Pattern4.png) | `figs-png/Pattern4.png`（原書 Figure 10） |
| (P3) 微分方程通解 | 原書 p.6 / Strang LAFE Sec. 6.4 |
| (P4) 三明治結構 | 原書 p.7 / Strang LAFE Sec. 7.1 / Sec. 7.4 |
| 4 視角對應 §4 | 本書 ch04-mat-mat.md §4 (MM1)–(MM4) |
| (MM4) 累加 / 截斷 demo | 本書 ch04-mat-mat.md VizScript-02（ch05 VizScript-03 指標到此） |
| 配色 / cell 尺寸 / 動畫時間 | 本書 SOP_DRAFT.md §2.8 全書視覺一致性錨點 |

---

## 6. 矩陣的五大分解（The Five Factorizations of a Matrix）— 總覽

> **原書頁碼：** p.7–p.8（總覽表），實際細節 p.8–p.13（§6.1–§6.5）
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` § The Five Factorizations of a Matrix（en.md line 205–254 為總覽段；§6.1–§6.5 自 256 起）
> **本章圖數：** 1（總覽圖 `5-Factorizations.png`）
> **本章 VizMark 數：** 1（⭐⭐⭐ × 1，Tier 1 + pointer）
> **狀態：** [x] 已完成（S07）

---

### 章節摘要

§1–§4 把矩陣的「乘法」拆成四個視角（MM1/MM2/MM3/MM4），§5 把幾個實用配置（對角矩陣縮放、$XD\mathbf{c}$、$U\Sigma V^{\mathrm{T}}$ 三明治）提煉為 Pattern。本章 §6 是全書的**結論章**：把所有矩陣（square、rectangular、symmetric、orthogonal、任意）對應到**五個經典分解**，並且每個分解都能用前面建立的視覺語彙（綠色直立列 / 粉紅橫躺行 / 藍點對角元素 / 三明治結構）一眼看出形狀。

五大分解：

1. **$A = CR$** — 任意矩陣 → 獨立列（column）× 行階梯形（row echelon form）。**列秩 = 行秩**最直觀的證明。
2. **$A = LU$** — 方陣（無 row exchange）→ 下三角 × 上三角。Gaussian 消去法的矩陣化。
3. **$A = QR$** — 任意列獨立矩陣 → 正交列 × 上三角。Gram–Schmidt 正交化。
4. **$S = Q\Lambda Q^{\mathrm{T}}$** — 對稱矩陣 → 特徵向量 × 對角特徵值 × 特徵向量轉置。**$S$ 而非 $A$，凸顯只適用對稱**。
5. **$A = U\Sigma V^{\mathrm{T}}$** — **任意矩陣**（含長方）→ 兩組正交基 × 對角奇異值。最一般的「分解之王」。

本章作為**第 6 章的開門總覽**，重點不在公式細節（細節留給 §6.1–§6.5），而在三件事：

- **形狀辨識**：5 個分解的視覺結構各自的「指紋」（哪個是兩塊綠色直立列？哪個有藍點對角？哪個是三明治？）；
- **適用條件**：什麼形狀的矩陣（rectangular vs square、general vs symmetric vs orthogonal）對應哪個分解；
- **與 §1–§5 的關係**：每個分解都能用 (MM4) 寫成「秩 1 之和」，並且每個分解都是 §5 某個 Pattern 的特例或組合。

掌握本章，後續 §6.1–§6.5 就只剩「驗證形狀 + 推導步驟」。

---

### 數學要點

#### 1. 五大分解總表

| 編號 | 分解 | 適用矩陣 | 三因子形狀 | 核心定理 / 用途 | 細節章節 |
|---|---|---|---|---|---|
| **F1** | $A = CR$ | 任意 $m \times n$ | $\underbrace{C}_{m \times r}\underbrace{R}_{r \times n}$（$r$ = rank） | **列秩 = 行秩** | §6.1（`ch06b-CR.md`） |
| **F2** | $A = LU$ | 方陣 $n \times n$（無 row exchange） | $\underbrace{L}_{n \times n}\underbrace{U}_{n \times n}$（下三角 × 上三角） | 解 $A\mathbf{x}=\mathbf{b}$ 的 Gaussian 消去 | §6.2（`ch06c-LU.md`） |
| **F3** | $A = QR$ | $m \times n$ 列獨立（$m \ge n$） | $\underbrace{Q}_{m \times n}\underbrace{R}_{n \times n}$（正交列 × 上三角） | Gram–Schmidt、最小二乘 | §6.3（`ch06d-QR.md`） |
| **F4** | $S = Q\Lambda Q^{\mathrm{T}}$ | **對稱**方陣 $n \times n$ | $\underbrace{Q}_{n \times n}\underbrace{\Lambda}_{n \times n}\underbrace{Q^{\mathrm{T}}}_{n \times n}$（三明治：正交 × 對角 × 正交轉置） | 譜定理、PCA、二次型 | §6.4（`ch06e-QLQ.md`） |
| **F5** | $A = U\Sigma V^{\mathrm{T}}$ | **任意** $m \times n$ | $\underbrace{U}_{m \times m}\underbrace{\Sigma}_{m \times n}\underbrace{V^{\mathrm{T}}}_{n \times n}$（三明治：正交 × 矩形對角 × 正交轉置） | 低秩近似、PCA、Eckart–Young | §6.5（`ch06f-USV.md`） |

**符號規約：**

- $r$ = $\operatorname{rank}(A)$，本章用「分解 reduces to $r$ outer products」這個視角串連 §4 (MM4)；
- $C$ 的列 = $A$ 的**獨立列**；$R$ = $A$ 的 reduced row echelon form（去掉零行）；
- $L$ = 下三角，對角為 1；$U$ = 上三角，對角為主元（pivot）；
- $Q$ = 正交（orthogonal），$Q^{\mathrm{T}}Q = I$（列正交，「窄而長」形狀時為左逆）；
- $\Lambda$ = 對角矩陣，藍點為特徵值 $\lambda_i$；$\Sigma$ = 矩形對角，藍點為奇異值 $\sigma_i \ge 0$ 且降冪；
- **F4 用 $S$ 不用 $A$**：原書刻意換符號強調「對稱才能 $Q^{\mathrm{T}}$ 對應 $Q^{-1}$」。

#### 2. 視覺辨識指紋（看圖 1 秒辨形狀）

對應 `5-Factorizations.png` 的視覺語彙（綠 = 直立列、粉紅 = 橫躺行、藍點 = 對角元素或正交基的「點群」標記）：

| 分解 | 視覺指紋（從左到右） |
|---|---|
| $A = CR$ | **2 塊綠色直立列**（$C$，獨立列）× **2 塊粉紅橫躺行**（$R$，行階梯） |
| $A = LU$ | **3 階遞減綠色直立列**（$L$，下三角縮短）× **3 階遞減粉紅橫躺行**（$U$，上三角縮短） |
| $A = QR$ | **3 條等高綠色直立列**（$Q$，正交）× **6 個藍點三角排列**（$R$，上三角對角強調） |
| $S = Q\Lambda Q^{\mathrm{T}}$ | **3 條綠色直立列**（$Q$）× **3 個藍點對角**（$\Lambda$）× **3 條綠色橫躺行**（$Q^{\mathrm{T}}$）— **第一個三明治** |
| $A = U\Sigma V^{\mathrm{T}}$ | **3 條綠色直立列**（$U$）× **2 個藍點對角**（$\Sigma$，**個數 = rank**）× **2 條粉紅橫躺行**（$V^{\mathrm{T}}$）— **第二個三明治** |

**形狀辨識口訣：**

- **看「直立列 × 橫躺行」雙層** → CR / LU / QR（「外積之和」之兩層結構）；
- **看「三明治」三層** → QΛQᵀ / UΣVᵀ（「正交 × 對角 × 正交」之三層結構，與 §5 (P3)(P4) 同骨架）；
- **看「藍點對角數量」** → CR/LU/QR 沒對角；QΛQᵀ 對角數 = $n$（含零特徵值也算）；UΣVᵀ 對角數 = $r$（**rank 就是非零奇異值個數**）。

#### 3. (MM4) 視角統一形式 — 五大分解都是「秩 1 之和」

§4 (MM4) 教過：兩矩陣相乘 = 兩矩陣的「列 × 行」外積之和。**五大分解全部可用 (MM4) 寫成同一個形式**，只是配料不同：

$$
\text{(共同骨架)} \qquad XY^{\mathrm{T}} \;=\; \sum_{p=1}^{r} \mathbf{x}_p \, \mathbf{y}^{\mathrm{T}}_p
$$

逐個對應到五大分解：

| 分解 | (MM4) 形式 | 項數 | 每項的意義 |
|---|---|---|---|
| $A = CR$ | $A = \displaystyle\sum_{p=1}^{r} \mathbf{c}_p \, \mathbf{r}^{*}_p$ | $r$ | 第 $p$ 個獨立列 × 對應的行階梯行 |
| $A = LU$ | $A = \displaystyle\sum_{p=1}^{n} \mathbf{l}_p \, \mathbf{u}^{*}_p$ | $n$ | 第 $p$ 個 $L$ 列 × 第 $p$ 個 $U$ 行（**剝皮 / peeling**） |
| $A = QR$ | $A = \displaystyle\sum_{p=1}^{n} \mathbf{q}_p \, \mathbf{r}^{*}_p$ | $n$ | 第 $p$ 個正交列 × 第 $p$ 個 $R$ 行 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | $S = \displaystyle\sum_{p=1}^{n} \lambda_p \, \mathbf{q}_p \, \mathbf{q}^{\mathrm{T}}_p$ | $n$ | $\lambda_p$ 加權的特徵向量自外積（**對稱秩 1**） |
| $A = U\Sigma V^{\mathrm{T}}$ | $A = \displaystyle\sum_{p=1}^{r} \sigma_p \, \mathbf{u}_p \, \mathbf{v}^{\mathrm{T}}_p$ | $r$ | $\sigma_p$ 加權的「左 × 右奇異向量」外積 |

**關鍵共通結構：** 每個分解都是「$r$ 或 $n$ 個秩 1 矩陣之和」。差別在：

- **單向 vs 雙向**：CR/LU/QR 是「列向量 × 行向量」，QΛQᵀ/UΣVᵀ 是「向量 × 對角加權 × 向量」（**三明治**）；
- **是否有對角加權**：QΛQᵀ/UΣVᵀ 把「分量大小」抽出成對角矩陣 $\Lambda$ 或 $\Sigma$；
- **基底是否正交**：QR/QΛQᵀ/UΣVᵀ 的「列 / 行向量」彼此正交（內積為 0），CR/LU 不一定。

**這個共通骨架是 §6.1–§6.5 撰寫的母模板**：每章只要回到 (MM4) 累加圖，把 $\mathbf{x}_p$、$\mathbf{y}_p$ 換成各自分解的角色，視覺化的核心動畫就完成。

#### 4. 五大分解的「升級鏈」結構

從 (P1)/(P2) 列縮放 → (P1')/(P2') 對角縮放 → (P3) $XD\mathbf{c}$ → (P4) $U\Sigma V^{\mathrm{T}}$ 是 §5 的升級鏈。§6 的五大分解也呈相似升級結構，可看作 §5 Pattern 的「應用版」：

| 階 | 結構複雜度 | 對應分解 | §5 Pattern 對應 |
|---|---|---|---|
| 1 | **兩因子（列 × 行）** | $A = CR$、$A = LU$、$A = QR$ | (P1)/(P2)（列縮放、行縮放） |
| 2 | **三因子（三明治）** | $S = Q\Lambda Q^{\mathrm{T}}$ | (P3)（$XD\mathbf{c}$ 升級，去掉 $\mathbf{c}$，得對稱矩陣分解） |
| 3 | **三因子非方陣（最一般）** | $A = U\Sigma V^{\mathrm{T}}$ | (P4)（$U\Sigma V^{\mathrm{T}}$ 三明治，§5 已預先鋪陳） |

**直覺：** §5 的 (P3)(P4) 不是「孤立的奇技淫巧」，而是 §6.4 / §6.5 的視覺前奏。§6.4 把 (P3) 中的 $\mathbf{c}$ 拿掉、把 $X$ 限制成正交，就得 $S = Q\Lambda Q^{\mathrm{T}}$；§6.5 直接把 (P4) 的圖搬過來、加上「奇異值降冪 + 列獨立」條件，就得 SVD。

#### 5. 適用矩陣對照（哪種矩陣對應哪些分解）

| 矩陣類別 | 適用分解 |
|---|---|
| 任意 $m \times n$（含長方、退化） | **$A = CR$**（一定有）、**$A = U\Sigma V^{\mathrm{T}}$**（一定有） |
| $m \times n$ 列獨立（$m \ge n$，$\operatorname{rank}(A) = n$） | + **$A = QR$** |
| 方陣 $n \times n$ 可逆 + 無 row exchange | + **$A = LU$** |
| 方陣 $n \times n$ 可對角化 | + $A = X\Lambda X^{-1}$（**非正交**，本書 §6 未強調，留給附錄） |
| **對稱**方陣 $n \times n$（即 $S = S^{\mathrm{T}}$） | + **$S = Q\Lambda Q^{\mathrm{T}}$**（**強保證實特徵值 + 正交特徵向量**） |
| 正定（positive definite）對稱方陣 | + Cholesky $S = L L^{\mathrm{T}}$（本書 §6 未列，是 $LU$ 的對稱特例） |

**兩個「萬能」分解：** $A = CR$ 和 $A = U\Sigma V^{\mathrm{T}}$ 對**任何**矩陣都成立（含 $r < \min(m, n)$ 的退化情況）。這也解釋為什麼 SVD 被稱為「**矩陣分解之王**」— 它對所有矩陣都能跑、永遠存在、永遠是 $\sigma_p \ge 0$ 降冪、永遠提供最佳低秩近似。

---

### 圖片詳細描述（Figure Description）

#### Figure 6.0: 五大分解總覽（The Five Factorizations of a Matrix）

**圖檔：** `docs/book/figs-png/5-Factorizations.png`（原始 EPS：`figs/5-Factorizations.eps`）
**原書頁碼：** p.7–p.8（表 1）
**所屬章節：** §6 開門總覽

##### 視覺結構 (Visual Structure)

整張圖是一個**直立排列的 5 列總表**，每列代表一個分解。每列由**左、中、右三欄**組成：

- **左欄（公式）：** 大字體 LaTeX 公式（$A=CR$、$A=LU$、$A=QR$、$S=Q\Lambda Q^{\mathrm{T}}$、$A=U\Sigma V^{\mathrm{T}}$）；
- **中欄（視覺示意）：** 用前面章節建立的視覺語彙（綠色直立列 = column、粉紅橫躺行 = row、藍色實心圓點 = 對角元素 / 正交基標記）排出每個分解的「形狀指紋」；
- **右欄（三行文字）：** 各分解的核心性質與用途說明（英文原文）。

5 列由上而下：

1. **$A=CR$**：2 塊綠色直立列 緊接著 2 塊粉紅橫躺行（無對角元素），形狀像「兩塊綠木板 + 兩塊粉紅木板」對接；
2. **$A=LU$**：3 塊**遞減高度**的綠色直立列（左最高、中次之、右最矮，呈下三角剪影）緊接著 3 塊**遞減長度**的粉紅橫躺行（上最長、中次之、下最短，呈上三角剪影）；
3. **$A=QR$**：3 塊**等高**的綠色直立列（凸顯正交而非三角）緊接著一個矩陣框框內擺 6 個藍點（呈倒三角排列，凸顯 $R$ 是上三角矩陣，藍點為主元位置）；
4. **$S=Q\Lambda Q^{\mathrm{T}}$**：3 塊綠色直立列 緊接著 3 個藍點對角（從左上到右下排列，中間矩陣的非對角位置完全留白）緊接著 3 塊**綠色橫躺行**（注意：第三塊與第一塊是同色綠，因為 $Q^{\mathrm{T}}$ 就是 $Q$ 的轉置，**第一個三明治結構**）；
5. **$A=U\Sigma V^{\mathrm{T}}$**：3 塊綠色直立列（$U$）緊接著 2 個藍點對角（$\Sigma$，**只有 2 個而不是 3 個** — 視覺強調「rank = 2 < 3」，即矩形對角矩陣只有 $r$ 個非零奇異值）緊接著 2 塊**粉紅**橫躺行（$V^{\mathrm{T}}$，注意：與 $U$ 不同色，因為 $U$ 和 $V$ 是兩組不同的正交基，**第二個三明治結構**）。

**閱讀順序：** 由上而下逐行讀，每行從左（公式）到中（圖）到右（文字）。先掃中欄看「形狀差異」，再回左欄對公式。

##### 數學內容 (Mathematical Content)

5 個分解的數學定義（公式如「§數學要點」總表）。中欄的視覺示意對應以下符號：

- **綠色直立列：** $C / L / Q / U$ 等矩陣的**列向量**（column vectors）；
- **粉紅橫躺行：** $R / U / V^{\mathrm{T}}$ 等矩陣的**行向量**（row vectors）；
- **藍色實心圓點：** $\Lambda$ 的特徵值 $\lambda_i$、$\Sigma$ 的奇異值 $\sigma_i$、$R$（in QR）的主元位置 — 整體傳達「對角矩陣的非零位置」；
- **遞減高度 / 長度的綠 / 粉紅塊：** 三角矩陣（下三角 / 上三角）的「列高度遞減」或「行長度遞減」視覺化；
- **等高 / 等寬正交列：** 正交矩陣 $Q$ 的列在「長度相同 + 互相垂直」上的視覺暗示。

**關鍵尺寸：** 雖然圖中只畫示意 3×3 大小，但比例傳達了：

- CR：$C$ 是「窄而瘦長」（$m \times r$，$r < n$），$R$ 是「矮而寬」（$r \times n$）；
- QR：$Q$ 是「列獨立」與 $A$ 同寬，$R$ 是方陣；
- QΛQᵀ：$Q$ 是方陣、$\Lambda$ 是方對角；
- UΣVᵀ：$U$、$V$ 都是方正交，但 $\Sigma$ 可以是矩形（$m \times n$），多餘部分為零。

##### 直覺解讀 (Intuition)

這張圖是全書的「**最後一頁的速查表**」— 把前面 §1–§5 建立的所有視覺語彙，**一次性套用到 5 個經典分解**，讓讀者一眼看出：

- 「**綠 × 粉紅** = 兩矩陣相乘的最自然色配對」（從 §1 視角開始延續到全書）；
- 「**藍點 = 對角元素 / 個別數字**」（從 §1 一直貫穿）；
- 「**三明治結構** = 三因子 + 中間是對角」（§5 (P3)(P4) 已預先教會，§6.4/§6.5 直接套用）；
- 「**遞減 / 等高 / 對齊** = 三角 vs 正交的視覺指紋」（§6.2 vs §6.3 vs §6.4 的關鍵區別）。

對教學的價值：**讀完前 5 章的讀者，看到本頁 5 行視覺示意，應該能脫口而出每行對應的分解名稱和用途**，無需查公式。本圖就是要訓練這個「形狀 → 分解」的反射弧。

**為什麼這張圖該做成互動視覺化？** 因為形狀辨識需要「同一個矩陣 $A$ 同時看 5 種分解結果」的對照能力。靜態圖只能五個並列死板地看；互動 demo 可以「拉桿選矩陣類型（任意 / 列獨立 / 方陣 / 對稱）→ 自動 highlight 哪些分解適用、哪些不適用 → 點某個分解就 toggle 出該分解的具體數值 + 視覺色塊重排」。這對「形狀 → 適用分解」的反射弧訓練比靜態圖快 10 倍以上（見 VizMark-01）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [五分解互動切換] ⭐⭐⭐ Tier 1 + pointer
> 「拉桿選矩陣類型 → 自動標記適用分解 → 點分解 toggle 具體數值 + 視覺色塊；(MM4) 累加 demo 全部 pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)」
> **詳見劇本：** VizScript-01（章末）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: 五大分解互動切換（5-Factorization Toggle Dashboard）

**Tier：** ⭐⭐⭐ Tier 1 + pointer（核心畫面控制器，秩 1 累加 demo 全部 delegate 到 ch04 VizScript-02）
**對應 VizMark：** VizMark-01（Figure 6.0）
**預估實作工作量：** S12+ 約 1.5 session（畫面框架 + 5 個分解的數值生成 + 適用性閘門邏輯；秩 1 累加動畫**不在本劇本**，重用 ch04 母模板）

> **設計策略（S07 首次正式使用「跨章 pointer」）：**
>
> 本劇本只負責**畫面切換 + 數值對照 + 形狀視覺化**，五個分解的「秩 1 累加動畫」全部不重複實作 — 透過按鈕「→ 看 (MM4) 秩 1 累加動畫」跳轉到 ch04 VizScript-02 並把該分解的 $(\mathbf{x}_p, \mathbf{y}_p)$ 序列當參數傳入。對偶結構（三明治）也透過按鈕「→ 看 P3/P4 三明治動畫」跳轉到 [ch05 VizScript-02](ch05-patterns.md#vizscript-02) / [ch05 VizScript-03](ch05-patterns.md#vizscript-03)。這個策略讓本章在「概念整合」上聚焦，不重複耗工時在已有動畫上。

##### A. 一句話定位

「給一個矩陣 $A$，**同時**看它對應 5 個分解的形狀，並透過點擊跳到每個分解的詳細動畫。」

##### B. 學習目標（Learning Outcome）

- **形狀辨識反射弧：** 看到矩陣類型，1 秒內知道哪些分解適用、哪些不適用；
- **視覺指紋記憶：** 把 5 個分解的視覺結構烙進腦中（兩因子 vs 三明治、有對角 vs 無對角、降冪 vs 等高）；
- **「分解之王」直覺：** 親手切「對稱→任意→退化」，看到只有 CR 和 SVD 永遠適用，建立「SVD 是萬能」的直覺。

##### C. 互動參數（UI Inputs）

- **矩陣類型選擇器（radio）：** 5 個選項 — 「任意 $m \times n$」/ 「列獨立 $m \ge n$」/「方陣可逆」/「對稱方陣」/「自訂（手動輸入）」；
- **尺寸滑桿：** $m \in [2, 6]$、$n \in [2, 6]$；對稱模式 $m = n$ 連動；
- **秩滑桿（rank）：** $r \in [1, \min(m,n)]$（控制「滿秩 vs 退化」，影響 CR 和 SVD 的有效項數）；
- **5 個分解開關（checkbox / tab）：** 點開即顯示該分解的數值 + 視覺示意，**未開啟保持灰階占位**；
- **「→ (MM4) 累加動畫」跳轉按鈕：** 每個分解開關旁有此按鈕，點擊跳 ch04 VizScript-02 並帶該分解的秩 1 序列；
- **「→ 三明治動畫」跳轉按鈕：** QΛQᵀ 和 UΣVᵀ 兩個分解有此按鈕，跳 ch05 VizScript-02/03。

##### D. 視覺布局（Layout）

**主畫面 5 行 × 3 欄總表結構（仿 Figure 6.0）：**

| 行 | 欄 1（公式） | 欄 2（形狀視覺化） | 欄 3（數值 + 跳轉按鈕） |
|---|---|---|---|
| 1 | $A = CR$ | 動態色塊（綠 $C$ + 粉紅 $R$，比例與當前 $r$ 同步） | $\dim C$、$\dim R$、 $r$；按鈕 1（→ MM4 累加） |
| 2 | $A = LU$ | 遞減綠 $L$ + 遞減粉紅 $U$（若不適用，灰階 + 圖示「✗ row exchange needed」） | $L$、$U$ 三角元素；按鈕 1 |
| 3 | $A = QR$ | 等高綠 $Q$ + 上三角藍點 $R$ | $Q^{\mathrm{T}}Q = I$ 驗證面板；按鈕 1 |
| 4 | $S = Q\Lambda Q^{\mathrm{T}}$ | 三明治 + $\lambda_p$ 對角藍點 | 特徵值列表；按鈕 1、按鈕 2（→ P3 三明治） |
| 5 | $A = U\Sigma V^{\mathrm{T}}$ | 三明治 + $\sigma_p$ 對角藍點（個數 = $r$） | 奇異值列表（降冪）；按鈕 1、按鈕 2（→ P4 三明治） |

**頂端控制條：** 矩陣類型 / 尺寸 / 秩；**底部結果條：** 適用性閘門總覽（5 個分解 ✓/✗ 圖示）。

##### E. 動畫流程（Animation Sequence）

1. **(0s) 初始：** 載入「3×3 對稱矩陣」預設，5 行皆綠色 ✓ 適用（對稱方陣是 5 個分解全適用的特例）；
2. **(用戶切「任意 $4 \times 3$」)：** LU 自動變灰打 ✗ （非方陣）、QΛQᵀ 變灰打 ✗（非對稱）；CR/QR/SVD 保留 ✓；色塊比例重排（800ms 動畫）；
3. **(用戶調秩 $r = 2$)：** CR 的綠 $C$ 從 3 列縮成 2 列、SVD 的藍點對角從 3 個縮成 2 個；其他不變；
4. **(用戶點 QR 行的「→ MM4」按鈕)：** 跳轉到 ch04 VizScript-02，自動載入 $(\mathbf{q}_p, \mathbf{r}^*_p)$ 3 對秩 1 序列；
5. **(用戶切「對稱方陣 $3 \times 3$」)：** 全部 5 行恢復 ✓；點 QΛQᵀ 行的「→ P3」按鈕，跳 ch05 VizScript-02 並載入該對稱矩陣的特徵分解作為 $XD\mathbf{c}$ 的特例（$\mathbf{c} = \mathbf{e}_p$ 單位向量逐個）。

##### F. 預設 demo 序列

1. **「對稱方陣 $3 \times 3$」**（全 5 ✓，教學起點，建立「對稱矩陣分解最多」直覺）；
2. **「任意 $4 \times 3$ 滿秩」**（CR/QR/SVD ✓，LU/QΛQᵀ ✗，教學「為什麼 SVD 是萬能」）；
3. **「任意 $4 \times 3$ rank 2 退化」**（只剩 CR 和 SVD ✓，凸顯萬能性）；
4. **「對稱半正定」**（5 ✓ 且 $\lambda_p \ge 0$，鋪陳 §6.5 SVD 是 QΛQᵀ 的推廣）。

##### G. 色彩與樣式（依全書視覺一致性錨點）

- 綠 `#2ca02c`（直立列）/ 粉紅 `#d62728`（橫躺行）/ 藍 `#1f77b4`（對角元素 / 主元）；
- 灰 `#cccccc`（不適用分解的占位）；
- ✓ 綠勾、✗ 紅叉圖示在右側適用性閘門條；
- 跳轉按鈕：白底深綠邊框 + 「→」字樣，hover 時填色 `#2ca02c`。

##### H. 公式同步區（Equation Sync Panel）

底部 LaTeX 公式區，依當前 hover 的分解動態切換：

```
A = CR    →    A = ∑_{p=1}^{r} c_p r^*_p
```

**hover 時可拆解高亮：** $\mathbf{c}_p$（綠閃 200ms）、$\mathbf{r}^*_p$（粉紅閃 200ms），與右側形狀視覺化同步。

##### I. 邊界條件與防呆

- **退化情況：** 用戶輸入 $r > \min(m, n)$ 自動 clip 並提示「rank 上限 = $\min(m, n)$」；
- **不適用分解的處理：** 灰階占位 + tooltip 「對稱不滿足 / 非方陣 / row exchange needed」說明原因，不是直接隱藏（教學上要看到「為什麼不能」）；
- **跳轉按鈕的狀態管理：** 點擊後保留當前矩陣資料；返回時自動恢復先前的選擇狀態。

##### J. 教學節奏建議

- **第 1 階段（0–1 分鐘）：** 用戶看預設「對稱方陣」，全 5 ✓，建立「最特殊的矩陣 = 最多分解」直覺；
- **第 2 階段（1–3 分鐘）：** 切「任意長方矩陣」，看到 LU/QΛQᵀ 變灰，引發「為什麼？」思考；
- **第 3 階段（3–5 分鐘）：** 切「退化 rank 2」，看到 QR 也變灰（若 $m < n$ 或退化），只剩 CR 和 SVD；建立「萬能分解」反射弧；
- **第 4 階段（5–10 分鐘）：** 點各個分解的「→」按鈕，跳轉到 ch04 / ch05 的母模板動畫看細節。

##### K. 變化版本（Variation）

- **「對比模式」：** 同時開啟兩個分解（如 QΛQᵀ + UΣVᵀ），左右對照三明治形狀差異（對稱用同色 / 非對稱用雙色）；
- **「時間切換模式」：** 自動每 3 秒切下一個矩陣類型，5 個分解的適用性閘門呈現動態勾叉變化，類似教學影片自動播放。

##### L. 為何不直接做秩 1 累加動畫（採 pointer 策略的理由）

- **不重複實作工時：** ch04 VizScript-02 已實作 (MM4) 累加動畫 + Mona Lisa SVD demo，本章 5 個分解共用此母模板，pointer 即可重用；
- **概念定位差異：** 本章 ch06a 是「**比較 5 個分解的差異**」，焦點是「形狀指紋」而非「累加細節」；累加細節在母模板看，效果更好；
- **S12+ 工時估算：** 若不採 pointer 策略，本劇本需重做 5 套秩 1 累加動畫（5 × 0.5 session = 2.5 session）；採 pointer 後只需 1 套畫面框架（1.5 session），節省 1 session 工時。

##### M. 驗收條件（Acceptance Criteria）

- 用戶切換 5 種矩陣類型，5 個分解的適用性閘門即時更新（< 100ms 響應）；
- 點任一「→」按鈕，能正確跳轉並帶當前矩陣資料；
- 5 個分解的數值面板與形狀視覺化同步（拉桿改秩，CR/SVD 的綠塊個數與藍點個數同步變化）；
- 「對稱半正定」demo 中，QΛQᵀ 與 UΣVᵀ 的數值應完全一致（$\lambda_p = \sigma_p$、$Q = U = V$），驗證 §6.4 / §6.5 的特例關係；
- 視覺輸出與 `5-Factorizations.png` 的 5 行佈局完全吻合（同樣的綠 / 粉紅 / 藍配色 + 三明治結構）。

---

### 章末延伸

- **後續章節連結：**
  - [→ ch06b-CR.md](ch06b-CR.md)（§6.1 $A=CR$ — 列秩 = 行秩，第一個分解，建立「分解就是因數分解」直覺）
  - [→ ch06c-LU.md](ch06c-LU.md)（§6.2 $A=LU$ — Gaussian 消去法的矩陣化）
  - [→ ch06d-QR.md](ch06d-QR.md)（§6.3 $A=QR$ — Gram–Schmidt 正交化）
  - [→ ch06e-QLQ.md](ch06e-QLQ.md)（§6.4 $S=Q\Lambda Q^{\mathrm{T}}$ — 對稱譜分解，連通 §5 (P3)）
  - [→ ch06f-USV.md](ch06f-USV.md)（§6.5 $A=U\Sigma V^{\mathrm{T}}$ — SVD，分解之王，連通 §5 (P4)）

- **前置章節傳承：**
  - [← ch04-mat-mat.md](ch04-mat-mat.md) §4 (MM4) 視角是本章 5 大分解的母模板（秩 1 之和的共同骨架）；
  - [← ch05-patterns.md](ch05-patterns.md) §5 (P1)/(P2) 是 CR/LU/QR 的視覺前奏，(P3)/(P4) 是 QΛQᵀ/UΣVᵀ 的視覺前奏。

- **延伸閱讀：**
  - Gilbert Strang《Linear Algebra for Everyone》第 6 章（5 個分解的詳細推導 + 應用 — PCA、最小二乘、低秩近似）；
  - Trefethen & Bau《Numerical Linear Algebra》Lecture 4–5（QR / SVD 數值穩定算法）；
  - 附錄 `Map_of_Eigenvalues_5.7.png`（5.7 版特徵值地圖，把 §6.4 / §6.5 的位置標出來）；
  - 附錄 `World_of_Matrices.png`（矩陣世界地圖，5 大分解就是這個地圖的「主要道路」）。

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` § The Five Factorizations of a Matrix（en.md line 205–254 為總覽段；§6.1–§6.5 自 256 起）/ `The-Art-of-Linear-Algebra.pdf` p.7–p.8 表 1
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` § 矩阵的五种分解（zh.md line 197–246 為總覽段）
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0

---

> **撰寫者註（S07）：** 本章是 §6 的開門總覽，刻意短（~400 行）+ 單一 VizMark + 採「Tier 1 + pointer」策略。後續 §6.1–§6.5 五章各自詳述一個分解，每章的「(MM4) 秩 1 累加」demo 都 pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)、「三明治」demo（QΛQᵀ / UΣVᵀ）都 pointer 到 [ch05 VizScript-02/03](ch05-patterns.md#vizscript-02)。本策略讓 §6 五章合計可節省 ~3 session 的視覺化重做工時（S06 SOP §2.6 補強驗證）。

---

## 6.1 矩陣分解 1：$A = CR$（Column–Row Factorization）

> **原書頁碼：** p.8–p.9
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.1 $A=CR$（en.md line 256–305 / zh.md line 248–293）
> **本章圖數：** 2（`CR1.png`、`CR2.png`，**原書圖中明標 using P1 / using P2**，與 §5 直接連結）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S07）

---

### 章節摘要

$A = CR$ 是 §6 五大分解的**第一個**，也是教學上**最直觀**的一個。它的核心定理是：**任何**矩陣的「列秩 = 行秩」（column rank = row rank）— 這個事實本身令人意外（列空間 $\mathbf{C}(A)$ 在 $\mathbb{R}^m$、行空間 $\mathbf{C}(A^{\mathrm{T}})$ 在 $\mathbb{R}^n$，兩個維度不同的空間怎麼會有相同的維度數？），而 $A = CR$ 是把這個定理「**裝進一個矩陣等式裡**」的最簡潔說法。

具體流程：

1. **掃** $A$ 的列（column）從左到右，把**獨立列**留下放進 $C$，**依賴列**捨去；
2. 剩下的 $C$ 是 $m \times r$ 矩陣（$r$ = $A$ 的秩 / rank）；
3. 為了重建 $A$，右乘一個 $r \times n$ 的 **row reduced echelon form** $R$；
4. $A = C R$ 同時揭示：$C$ 有 $r$ 個獨立**列** → 列秩 = $r$；$R$ 有 $r$ 個獨立**行** → 行秩 = $r$；因為等式相同，列秩 = 行秩。

本章另一個關鍵點是**與 §5 Pattern 的視覺直接連結**：原書 CR1 圖在右下角畫 `using P1`、CR2 圖在右下角畫 `using P2`。這代表 $A = CR$ 的「列拆解」就是 §5 (P1) Pattern 1（「從右乘任意矩陣 → 列線性組合」）的特例；「行拆解」就是 §5 (P2) Pattern 2 的特例。本章 VizScript 因此採取**雙 pointer 策略**：(MM4) 累加 demo pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)；(P1)/(P2) 列縮放動畫 pointer 到 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)；本章只寫**獨立列高亮 + RREF 過程 + rank 視覺化**等 CR 特有的內容。

數值範例（本章貫穿）：

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 5 \end{bmatrix}
\;=\;
\underbrace{\begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}}_{C}
\underbrace{\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}}_{R}
$$

讀者掃 $A$ 的列：列 1 $= (1, 2)^{\mathrm{T}}$、列 2 $= (2, 3)^{\mathrm{T}}$、列 3 $= (3, 5)^{\mathrm{T}} = $ 列 1 $+$ 列 2（依賴列）。捨去列 3，保留列 1、列 2 形成 $C$。$R$ 自動由「如何用 $C$ 的列拼回 $A$ 的列」推導：列 1 = $1 \cdot \mathbf{c}_1 + 0 \cdot \mathbf{c}_2$、列 2 = $0 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$、列 3 = $1 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$ → $R = \bigl[\begin{smallmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{smallmatrix}\bigr]$。

---

### 數學要點

#### 1. 定義與形狀

$$
A_{m \times n} = C_{m \times r} \, R_{r \times n}, \qquad r = \operatorname{rank}(A)
$$

- **$C$（Column matrix）：** $r$ 個**獨立列**，由 $A$ 從左到右掃描得到（不是任意 basis，是「按出現順序保留」的 basis）；
- **$R$（Row reduced echelon form）：** 把 $A$ 做 row reduction 直到變成 RREF 後，**去掉所有零行**得到的 $r \times n$ 矩陣；
- **$r$ 的視覺含義：** 在中間是「窄腰」，$C$ 矩陣寬 $r$、$R$ 矩陣高 $r$ — 視覺上 $A = CR$ 的「腰部」就是 rank。

#### 2. 與 (MM4) 視角的連結 — 秩 1 之和

把 $A = CR$ 套用 §4 (MM4) 「列 × 行外積之和」視角：

$$
A = CR = \sum_{p=1}^{r} \mathbf{c}_p \, \mathbf{r}^{*}_p
$$

- $\mathbf{c}_p$ = $C$ 的第 $p$ 列（綠色直立）；
- $\mathbf{r}^{*}_p$ = $R$ 的第 $p$ 行（粉紅橫躺）；
- $\mathbf{c}_p \mathbf{r}^{*}_p$ 是一個秩 1 矩陣，視覺上是「綠色直立列 × 粉紅橫躺行」的網格；
- $A$ 是 $r$ 個秩 1 矩陣的**精確和**（不是近似 — 因為 $\operatorname{rank}(A) = r$，所以 $r$ 項剛好就能精確還原）。

**範例展開（$r = 2$）：**

$$
A = \mathbf{c}_1 \mathbf{r}^{*}_1 + \mathbf{c}_2 \mathbf{r}^{*}_2
= \begin{bmatrix}1\\2\end{bmatrix}\begin{bmatrix}1 & 0 & 1\end{bmatrix}
+ \begin{bmatrix}2\\3\end{bmatrix}\begin{bmatrix}0 & 1 & 1\end{bmatrix}
$$

逐項計算驗證：

$$
\begin{bmatrix}1 & 0 & 1\\ 2 & 0 & 2\end{bmatrix}
+ \begin{bmatrix}0 & 2 & 2\\ 0 & 3 & 3\end{bmatrix}
= \begin{bmatrix}1 & 2 & 3\\ 2 & 3 & 5\end{bmatrix} = A \;\checkmark
$$

#### 3. 與 §5 (P1)/(P2) 的視覺連結 — using P1 / using P2 標記

原書 CR1 / CR2 兩張圖的**右下角**分別標 `using P1` 和 `using P2`，直接點明：

##### CR1 = (P1) 列觀點

$$
\underbrace{A = C R}_{\text{把 } A \text{ 的列用 } C \text{ 的列線組}} \quad\Leftrightarrow\quad \mathbf{a}_j = \sum_{p=1}^{r} R_{pj} \cdot \mathbf{c}_p
$$

**對照 §5 (P1)：** $A = \text{(diag) X (col)} \to$ 在 (P1) 中是「從右乘任意矩陣 → 結果矩陣的列 = 原矩陣列的線性組合」。在 CR 中，$A$ 的第 $j$ 列 $\mathbf{a}_j$ 由 $C$ 的兩個獨立列 $\mathbf{c}_1, \mathbf{c}_2$ 加權組成，權重就是 $R$ 的第 $j$ 行 $\mathbf{r}^{*}_j$ 的元素。**這是 (P1) 在「rank $r$ 的窄腰中」的特例**。

##### CR2 = (P2) 行觀點

$$
\underbrace{A = C R}_{\text{把 } A \text{ 的行用 } R \text{ 的行線組}} \quad\Leftrightarrow\quad \mathbf{a}^{*}_i = \sum_{p=1}^{r} C_{ip} \cdot \mathbf{r}^{*}_p
$$

**對照 §5 (P2)：** $A = \text{(row) X (diag)} \to$ 在 (P2) 中是「從左乘任意矩陣 → 結果矩陣的行 = 原矩陣行的線性組合」。在 CR 中，$A$ 的第 $i$ 行 $\mathbf{a}^{*}_i$ 由 $R$ 的兩個獨立行 $\mathbf{r}^{*}_1, \mathbf{r}^{*}_2$ 加權組成，權重就是 $C$ 的第 $i$ 行的元素。**這是 (P2) 在「rank $r$ 的窄腰中」的特例**。

**關鍵領悟（S07 PNG 重核重大發現）：** 原書 $A = CR$ 不是把 §5 Pattern 重新發明，而是**直接套用 §5 (P1)(P2) 來教證列秩 = 行秩**。這代表：

- **(P1) 視角看：** $A$ 的列空間 $\mathbf{C}(A) = \mathbf{C}(C)$（被 $C$ 的 $r$ 個列張成），維度 = $r$；
- **(P2) 視角看：** $A$ 的行空間 $\mathbf{C}(A^{\mathrm{T}}) = \mathbf{C}(R^{\mathrm{T}})$（被 $R$ 的 $r$ 個行張成），維度 = $r$；
- **兩者相等：** 同一個 $r$ 出現在兩邊 → **列秩 = 行秩**。

#### 4. 列秩 = 行秩 — 為什麼這個定理「不顯然」

兩個空間的維度本來就**很容易不同**：

- $\mathbf{C}(A) \subseteq \mathbb{R}^m$ — 列空間住在 $m$ 維；
- $\mathbf{C}(A^{\mathrm{T}}) \subseteq \mathbb{R}^n$ — 行空間住在 $n$ 維。

$m \ne n$ 的長方矩陣（rectangular）兩個空間**整個**住在不同維度的環境裡。然而它們的**維度數**（也就是 basis 大小）卻必相等。例：$3 \times 5$ 矩陣，列空間最多 3 維、行空間最多 5 維 — 直覺上「行空間能容納更多獨立」，但實際上若 $A$ 的列秩 = 2，行秩**一定也是** 2，**不會是 3 或更高**。$A = CR$ 把這個「相等」**強迫到**同一個 $r$ 上：$C$ 的列數 = $R$ 的行數 = $r$。

**證明速覽：** 假設列秩 = $r$，從 $A$ 取出 $r$ 個獨立列形成 $C$，剩下的列都是 $C$ 列的線性組合。把這些「組合係數」整理成 $R$，自然 $A = CR$。觀察 $R$ 的行：$R$ 是「精簡」過的 RREF（除去零行），$r$ 個行**必獨立**（RREF 的非零行永遠獨立）→ 行秩 ≤ $r$。對稱地，從 $A^{\mathrm{T}}$ 起跑也能得行秩 = $r'$ 且必有 $A^{\mathrm{T}} = R'^{\mathrm{T}} C'^{\mathrm{T}}$，列秩 ≤ $r'$。兩個不等式合起來：列秩 = 行秩 = $r$。

#### 5. 對 $A = CR$ 的 Procedure（從左到右掃描）

| 步驟 | 動作 | 矩陣狀態 |
|---|---|---|
| 1 | 取 $A$ 的列 1：非零，**保留**到 $C$ | $C \leftarrow [\mathbf{a}_1]$ |
| 2 | 取 $A$ 的列 2：檢查能否表為列 1 的線組（即是否為 $\alpha \mathbf{a}_1$ 形式）；若不能，**保留**到 $C$ | $C \leftarrow [\mathbf{a}_1, \mathbf{a}_2]$（若獨立） |
| 3 | 取 $A$ 的列 3：檢查能否表為列 1、列 2 的線組（$\beta_1 \mathbf{a}_1 + \beta_2 \mathbf{a}_2$）；若能，**捨去**（記下係數 $\beta_1, \beta_2$） | $C$ 不變；記 $\beta$ |
| ... | 重複至所有列掃完 | $C \in \mathbb{R}^{m \times r}$ |
| 末 | 把每列的「線組係數」整理成 $R$ 的對應行 | $R \in \mathbb{R}^{r \times n}$ |

**範例（$A = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr]$）：**

- 列 1 = $(1, 2)^{\mathrm{T}}$：保留 → $\mathbf{c}_1$；
- 列 2 = $(2, 3)^{\mathrm{T}}$：$2 \neq \alpha \cdot 1$ 且 $3 \neq \alpha \cdot 2$ 對任何 $\alpha$，獨立，保留 → $\mathbf{c}_2$；
- 列 3 = $(3, 5)^{\mathrm{T}}$：嘗試 $\beta_1 (1, 2)^{\mathrm{T}} + \beta_2 (2, 3)^{\mathrm{T}} = (3, 5)^{\mathrm{T}}$ → $\beta_1 + 2\beta_2 = 3$、$2\beta_1 + 3\beta_2 = 5$ → $\beta_1 = 1, \beta_2 = 1$ → **依賴**，捨去；
- 整理係數：列 1 對應 $(1, 0)^{\mathrm{T}}$、列 2 對應 $(0, 1)^{\mathrm{T}}$、列 3 對應 $(1, 1)^{\mathrm{T}}$ → $R$ = 把這三個豎著拼成 $r \times n$ 矩陣 = $\bigl[\begin{smallmatrix}1 & 0 & 1 \\ 0 & 1 & 1\end{smallmatrix}\bigr]$；
- 驗證：$CR = \bigl[\begin{smallmatrix}1 & 2 \\ 2 & 3\end{smallmatrix}\bigr]\bigl[\begin{smallmatrix}1 & 0 & 1 \\ 0 & 1 & 1\end{smallmatrix}\bigr] = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr] = A \checkmark$。

#### 6. $A = CR$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **CR ↔ LU** | LU 是 CR 的「方陣 + 三角」特例。但 LU 對 $L, U$ 加了三角結構，CR 對 $C, R$ 只加「獨立」與「RREF」結構 |
| **CR ↔ QR** | QR 是「把 $C$ 正交化」的版本 — Gram–Schmidt 把 $C$ 變成 $Q$（正交列），把對應係數變成 $R$（上三角）。**從 CR 到 QR = 套一層 GS** |
| **CR ↔ SVD** | SVD 是「最對稱、最平衡」的 CR — 把 $C$ 變正交 $U$、把 $R$ 變正交 $V^{\mathrm{T}}$、中間插一個對角 $\Sigma$ 容納「縮放因子」。**從 CR 到 SVD = 兩端都正交化** |
| **CR ↔ QΛQᵀ** | QΛQᵀ 限對稱 $S$，且 $C$ 和 $R$ 不獨立（$C = Q$、$R = \Lambda Q^{\mathrm{T}}$） |

**結論：** $A = CR$ 是「**最少要求**」的分解（只要矩陣是矩陣就有），其他四個都是 CR 加各種「結構性」要求的特化。**從教學順序看：先教 CR 建立「分解 = 找出秩 + 拆兩塊」直覺，再教 LU/QR/QΛQᵀ/SVD 加各種結構**，是原書的設計邏輯。

#### 7. 數學要點總結（一張表）

| 性質 | $A = CR$ 的對應 |
|---|---|
| 適用矩陣 | 任意 $m \times n$（含長方、退化） |
| $C$ 的列來源 | $A$ 從左到右掃描，獨立列保留 |
| $R$ 的本質 | 把每列表為「$C$ 列的線組」的係數矩陣（恰好是 RREF 去零行） |
| 「腰」的大小 | $r = \operatorname{rank}(A)$ |
| 列秩 = 行秩 證明 | $C$ 的 $r$ 獨立列 = 列秩；$R$ 的 $r$ 獨立行 = 行秩；同一個 $r$ |
| §4 (MM4) 對應 | $A = \sum_{p=1}^{r} \mathbf{c}_p \mathbf{r}^{*}_p$（秩 1 之和，$r$ 項） |
| §5 (P1) 對應 | CR1 圖明標：列觀點的 (P1)（$\mathbf{a}_j = \sum R_{pj} \mathbf{c}_p$） |
| §5 (P2) 對應 | CR2 圖明標：行觀點的 (P2)（$\mathbf{a}^{*}_i = \sum C_{ip} \mathbf{r}^{*}_p$） |
| 計算效率 | $O(mn^2)$（高斯消去），但教學上是「概念分解」，不是「算分解」 |

---

### 圖片詳細描述（Figure Descriptions）

#### Figure 6.1: $CR$ 中的列秩（Column Rank in $CR$）— 標 using P1

**圖檔：** `docs/book/figs-png/CR1.png`（原始 EPS：`figs/CR1.eps`）
**原書頁碼：** p.8 圖 11
**所屬章節：** §6.1 $A=CR$（列觀點）

##### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，共 5 段，從左到右：

1. **第 1 段：** 矩陣 $A$ 的方框（灰色填充），框內畫出 **3 條等寬直立的灰色矩形**代表 $A$ 的 3 列；上方有大字 `A`；
2. **第 2 段：** 等號 `=` 大字；
3. **第 3 段：** 矩陣 $C$（方框框住 **2 條綠色直立列**），上方有大字 `C`，每條綠列下方有編號 `1`、`2`；
4. **第 4 段：** 矩陣 $R$（方框框住 **3 列藍/橙/紫色實心圓點對**，每列 2 個點上下排列），上方有大字 `R`；藍/橙/紫**色標對應 $A$ 的 3 列來源**（藍 = 列 1、橙 = 列 2、紫 = 列 3）；
5. **第 5 段：** 等號 `=` 大字；
6. **第 6 段：** 拆解結果，3 個直立列方框並排：
   - 第 1 列：藍·綠1 + （0·綠2 隱去）→ 顯示「藍1 + 綠 1」標記（即 $\mathbf{a}_1 = 1 \cdot \mathbf{c}_1$）；
   - 第 2 列：（0·綠1 隱去）+ 橙·綠2 → 顯示「橙 + 綠 2」標記（即 $\mathbf{a}_2 = 1 \cdot \mathbf{c}_2$）；
   - 第 3 列：紫·綠1 + 紫·綠2 → 顯示「紫 1 + 紫 2」標記（即 $\mathbf{a}_3 = 1 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$）；
7. **右下角圖示：** 圓圈內標 `P1`，文字 `using` — **直接標明「本圖用 §5 Pattern 1 視角」**。

**閱讀順序：** 由左到右讀整個等式鏈 `A = C R = （三列拆解）`。重點掃右側的 3 個拆解列，**藍 / 橙 / 紫色標**讓讀者立刻看出「每列從 $C$ 的兩列各取多少權重」。

##### 數學內容 (Mathematical Content)

對應數學表示：

$$
A = C R = \begin{bmatrix} | & | & | \\ \mathbf{a}_1 & \mathbf{a}_2 & \mathbf{a}_3 \\ | & | & | \end{bmatrix}
= \begin{bmatrix} | & | \\ \mathbf{c}_1 & \mathbf{c}_2 \\ | & | \end{bmatrix} \begin{bmatrix} R_{11} & R_{12} & R_{13} \\ R_{21} & R_{22} & R_{23} \end{bmatrix}
$$

第 $j$ 列展開（**(P1) Pattern 1**）：

$$
\mathbf{a}_j = R_{1j} \cdot \mathbf{c}_1 + R_{2j} \cdot \mathbf{c}_2
$$

對應 $A = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr]$ 範例：

- $\mathbf{a}_1 = 1 \cdot \mathbf{c}_1 + 0 \cdot \mathbf{c}_2$（藍列 = 1·綠1，圖中只標藍 + 綠 1）；
- $\mathbf{a}_2 = 0 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$（橙列 = 1·綠2，圖中只標橙 + 綠 2）；
- $\mathbf{a}_3 = 1 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$（紫列 = 1·綠1 + 1·綠2，圖中標紫 1 + 紫 2）。

**顏色編碼的意義（藍 / 橙 / 紫）：** 用顏色代替數字權重，避免在小圖中塞滿小數字。藍 → $R$ 的第 1 行（對應 $A$ 的列 1）、橙 → $R$ 的第 2 行（對應 $A$ 的列 2）、紫 → $R$ 的第 3 行（對應 $A$ 的列 3 即依賴列）。

##### 直覺解讀 (Intuition)

CR1 是「**$A$ 的每一列都用 $C$ 的 2 個獨立列線組出來**」的視覺證明。讀者看右側 3 個拆解列，會立刻領悟：

- **獨立列（列 1、列 2）** 各只用了「自己對應的」$C$ 列一次（藍對綠 1、橙對綠 2），所以拆解圖只有單一綠塊；
- **依賴列（列 3）** 用了 $C$ 的兩列各一次（紫 + 綠 1、紫 + 綠 2），所以拆解圖有兩個綠塊；
- 「**列空間 $\mathbf{C}(A)$ 完全等於 $\mathbf{C}(C)$**」這個事實，從圖上「每列都是 $C$ 列的線組」直觀可見。

**「using P1」標籤的重要性（S07 PNG 重核發現）：** 原書作者**刻意**把這張圖標 `using P1`，等於明說「本圖就是 §5 Pattern 1 的應用」。視覺上看：

- §5 (P1) 圖是 `[列 1 ... 列 n] × diag(d_1, ..., d_n)` → 結果是「每列被 $d_p$ 縮放」；
- CR1 圖是 `[列 1, 列 2] × R` → 結果是「每列被 $R$ 的對應行線組」；
- (P1) 是 **「對角矩陣 R」** 的特例，CR1 是 **「任意 R」** 的一般版。

這個連結讓讀者把 §5 練的 (P1) 直覺**直接搬到** §6.1 — 無需重新建立心智模型，視覺化也可以**直接重用 ch05 VizScript-01 的對角矩陣互動**（只是把對角矩陣換成一般矩陣 $R$）。

**為什麼這張圖該做成互動視覺化？** 因為「獨立列 vs 依賴列」的判斷需要動態檢視 — 用戶調 $A$ 的元素，自動 highlight 哪些列被保留進 $C$、哪些被捨去；同時看到 $R$ 對應位置如何自動填出。靜態圖只能展示一個固定 $A$，互動 demo 可以讓用戶嘗試多種矩陣（含退化、含 rank 1 / 2 / 3）並即時看到 $C, R$ 的形狀變化。這是「列秩 = 行秩」定理感覺最深刻的時刻（見 VizMark-01）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [CR 拆解 + 獨立列高亮 + RREF 過程] ⭐⭐⭐
> 「拉桿調 $A$ 的元素 → 自動掃描獨立列 / 依賴列 → 動態組 $C$ / $R$ → 三色標記列來源（藍 / 橙 / 紫）」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [rank 與獨立列數對應] ⭐⭐
> 「用戶改 $A$ 的列讓 rank 變化（3 → 2 → 1 → 0），看 $C$ 的綠列數量同步變化 + $R$ 的形狀同步」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [2×3 範例 walkthrough] ⭐
> 「用書中範例 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$ 一步一步演示掃描過程，每步顯示『該列獨立還是依賴』」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

#### Figure 6.2: $CR$ 中的行秩（Row Rank in $CR$）— 標 using P2

**圖檔：** `docs/book/figs-png/CR2.png`（原始 EPS：`figs/CR2.eps`）
**原書頁碼：** p.8 圖 12
**所屬章節：** §6.1 $A=CR$（行觀點）

##### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**（與 CR1 同款式，但內容互換為行視角），共 5 段：

1. **第 1 段：** 矩陣 $A$ 的方框（灰色填充），框內畫出 **2 條等高橫躺的灰色矩形**代表 $A$ 的 2 行；上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $C$（方框框住 **2 列 × 2 個藍/紫色實心圓點**），上方有大字 `C`；**藍點對應 $A$ 的行 1、紫點對應 $A$ 的行 2**；
4. **第 4 段：** 矩陣 $R$（方框框住 **2 條粉紅橫躺行**），上方有大字 `R`，每條粉紅行右側有編號 `1`、`2`；
5. **第 5 段：** 等號 `=`；
6. **第 6 段：** 拆解結果，2 個橫躺行方框並排（上下排列）：
   - 上行：藍·粉紅1 + 藍·粉紅2 → 顯示「藍 1 + 藍 2」（即 $\mathbf{a}^{*}_1 = $ 藍·$\mathbf{r}^{*}_1$ + 藍·$\mathbf{r}^{*}_2$）；
   - 下行：紫·粉紅1 + 紫·粉紅2 → 顯示「紫 1 + 紫 2」（即 $\mathbf{a}^{*}_2 = $ 紫·$\mathbf{r}^{*}_1$ + 紫·$\mathbf{r}^{*}_2$）；
7. **右下角圖示：** 圓圈內標 `P2`，文字 `using` — **直接標明「本圖用 §5 Pattern 2 視角」**。

**閱讀順序：** 由左到右讀整個等式鏈 `A = C R = （兩行拆解）`。重點掃右側的 2 個拆解行，**藍 / 紫色標**讓讀者立刻看出「每行從 $R$ 的兩行各取多少權重」。

**與 CR1 的對偶關係（重要）：**

| | CR1 | CR2 |
|---|---|---|
| 視角 | 列 (column) | 行 (row) |
| $A$ 的呈現 | 3 條直立灰列 | 2 條橫躺灰行 |
| $C$ 的呈現 | 2 條綠**直立列** | 2 列 × 2 個**藍紫點**（每行對應 $A$ 的一行） |
| $R$ 的呈現 | 3 列 × 2 個**藍橙紫點** | 2 條粉紅**橫躺行** |
| 拆解 | 3 個直立列 = $C$ 列的線組 | 2 個橫躺行 = $R$ 行的線組 |
| 標籤 | `using P1` | `using P2` |
| 直觀傳達 | 「$A$ 的列空間 = $C$ 的列空間」 | 「$A$ 的行空間 = $R$ 的行空間」 |
| 維度結論 | 列秩 = $r$（= $C$ 列數） | 行秩 = $r$（= $R$ 行數） |

**這對「對偶圖」是教學設計的傑作 —** 同一個 $A = CR$ 等式，從兩個視角（列 / 行）各畫一張，**兩張並排**讓讀者一秒領悟「列秩 = 行秩 = $r$」。

##### 數學內容 (Mathematical Content)

對應數學表示（**(P2) Pattern 2** 行視角）：

$$
A = C R, \qquad \mathbf{a}^{*}_i = \sum_{p=1}^{r} C_{ip} \cdot \mathbf{r}^{*}_p
$$

對應 $A = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr]$ 範例：

- 行 1（$\mathbf{a}^{*}_1 = (1, 2, 3)$）= $1 \cdot \mathbf{r}^{*}_1 + 2 \cdot \mathbf{r}^{*}_2 = 1 \cdot (1,0,1) + 2 \cdot (0,1,1) = (1, 2, 3)$ ✓；
- 行 2（$\mathbf{a}^{*}_2 = (2, 3, 5)$）= $2 \cdot \mathbf{r}^{*}_1 + 3 \cdot \mathbf{r}^{*}_2 = 2 \cdot (1,0,1) + 3 \cdot (0,1,1) = (2, 3, 5)$ ✓；
- 圖中藍 / 紫色標代表 $C$ 的第 1 行（藍 = $(1, 2)$）和第 2 行（紫 = $(2, 3)$）。

##### 直覺解讀 (Intuition)

CR2 是「**$A$ 的每一行都用 $R$ 的 2 個獨立行線組出來**」的視覺證明。讀者看右側 2 個拆解行：

- $A$ 的行 1 用了 $R$ 的兩行（藍·$\mathbf{r}^{*}_1$ + 藍·$\mathbf{r}^{*}_2$），權重 = 藍 = $(1, 2)$；
- $A$ 的行 2 用了 $R$ 的兩行（紫·$\mathbf{r}^{*}_1$ + 紫·$\mathbf{r}^{*}_2$），權重 = 紫 = $(2, 3)$；
- 「**行空間 $\mathbf{C}(A^{\mathrm{T}})$ 完全等於 $\mathbf{C}(R^{\mathrm{T}})$**」這個事實，從圖上「每行都是 $R$ 行的線組」直觀可見。

**綜合 CR1 + CR2 的結論：**

- CR1：列空間維度 = $C$ 的列數 = $r$；
- CR2：行空間維度 = $R$ 的行數 = $r$；
- 同一個 $r$ → **列秩 = 行秩**。

**「using P2」標籤的重要性：** 與 CR1 同理，原書明標本圖是 §5 (P2) 的特例。視覺化可直接重用 ch05 VizScript-01 的對角矩陣互動，只是把 $C$ 的對角矩陣換成一般 $m \times r$ 矩陣。

**對 (P1)/(P2) 對偶的全書一致性：** §5 把 (P1)↔(P2) 寫成對偶總表，§6.1 把 CR1↔CR2 寫成對偶圖。**這個「對偶兩張圖」的視覺模式會在 §6.2 LU、§6.3 QR、§6.4 QΛQᵀ、§6.5 SVD 中重複出現**（每個分解都可以從列觀點和行觀點各畫一張）。S07 在寫 ch06b 時建議全書統一這個對偶圖模式，提升閱讀一致性。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [CR 拆解 + 行視角同步] ⭐⭐⭐
> 「同 CR1 的 VizMark-01，但加 toggle 切換『列視角 (CR1) / 行視角 (CR2) / 同時看兩者』三模式」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [rank 與獨立行數對應] ⭐⭐
> 「用戶改 $A$ 的行讓 rank 變化，看 $R$ 的粉紅行數量同步 + $C$ 的形狀同步」（VizScript-02 共用）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: CR 拆解 + 三色獨立列高亮 + RREF 動態過程（CR Toggle Animation）

**Tier：** ⭐⭐⭐ Tier 2（含對偶 CR1/CR2 切換 + RREF 計算動畫；秩 1 累加 demo pointer 到 ch04，(P1)/(P2) 列縮放動畫 pointer 到 ch05）
**對應 VizMark：** Figure 6.1 VizMark-01、Figure 6.2 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 1 session + 互動邏輯與 RREF 計算 1 session）

##### A. 一句話定位

「給一個 $A$，動態掃描獨立列、組出 $C$ 和 $R$，並切換列視角 (CR1) / 行視角 (CR2) / 同時看兩者，視覺驗證列秩 = 行秩。」

##### B. 學習目標（Learning Outcome）

- **獨立 / 依賴列辨識：** 看到一個矩陣，能一眼判斷哪些列獨立、哪些列是先前列的線組；
- **列秩 = 行秩 直覺：** 透過 CR1 和 CR2 兩張對偶圖**同時動態變化**，建立「$r$ 在兩邊都是 $r$」的視覺反射弧；
- **RREF 結構直覺：** 看到 $R$ 自動形成 RREF（識別矩陣 $I_r$ 嵌在「保留列」對應的欄、依賴列的係數填在其他欄）；
- **跨章連結：** 點 (P1)(P2) 按鈕跳 ch05 VizScript-01 看對角矩陣特例、點 (MM4) 按鈕跳 ch04 VizScript-02 看秩 1 累加。

##### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $m \times n$ 格子網格，$m \in [2, 5]$、$n \in [2, 6]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$（書中範例，$r = 2$）；
  - 範例 2：$\bigl[\begin{smallmatrix}1&2&3\\2&4&6\end{smallmatrix}\bigr]$（$r = 1$，所有列共線）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&0&0\\0&1&0\\0&0&1\end{smallmatrix}\bigr]$（單位矩陣，$r = 3$，所有列獨立）；
  - 範例 4：$\bigl[\begin{smallmatrix}1&2&3&4\\2&4&6&8\\3&6&9&12\end{smallmatrix}\bigr]$（$r = 1$，三維列空間退化到一維）；
  - 範例 5：$\bigl[\begin{smallmatrix}1&1&0\\0&1&1\\1&0&1\end{smallmatrix}\bigr]$（**陷阱題**：看起來像獨立，實際 $r = 2$，列 3 = 列 1 + 列 2 − 列 2 ... 留給用戶探索）；
- **視角切換 (radio)：** `列視角 (CR1)` / `行視角 (CR2)` / `同時看兩者（並排）`；
- **掃描速度滑桿：** 自動掃描動畫的速度（0.5×–4×）；
- **跳轉按鈕：**
  - 「→ (P1)(P2) 對角矩陣特例」按鈕（跳 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)，自動把當前 $R$ 換成對角矩陣 $D$）；
  - 「→ (MM4) 秩 1 累加」按鈕（跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)，自動載入 $(\mathbf{c}_p, \mathbf{r}^{*}_p)$ 序列）。

##### D. 視覺布局（Layout）

**主畫面三區（並排視角時）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $A$ 的格子輸入網格 + 預設範例選擇器 + 滑桿 |
| 中區（CR1 列視角） | $A$（灰列）= $C$（綠列）$R$（藍橙紫點陣）= 三列拆解（綠塊 + 三色標記）；底部 `using P1` 圖示 |
| 右區（CR2 行視角） | $A$（灰行）= $C$（藍紫點陣）$R$（粉紅行）= 兩行拆解（粉紅塊 + 兩色標記）；底部 `using P2` 圖示 |

**底部資訊條：**

- $r$ = 當前 rank（大字顯示）；
- $C$ 和 $R$ 的形狀（$m \times r$、$r \times n$）；
- 兩個跳轉按鈕。

##### E. 動畫流程（Animation Sequence）

**自動掃描模式（用戶按播放鈕）：**

1. **(0s) 初始：** $A$ 灰色顯示，$C$、$R$ 區域空白；
2. **(1s) 掃列 1：** $A$ 的列 1 變藍 → 「獨立」標記出現 → 列 1 飛入 $C$ 變綠 → $R$ 的第 1 行第 1 列填 1；
3. **(2s) 掃列 2：** $A$ 的列 2 變橙 → 嘗試用 $C$ 的當前列線組 → 不能 → 「獨立」標記出現 → 列 2 飛入 $C$ 變綠 → $R$ 的第 2 行第 2 列填 1；
4. **(3s) 掃列 3：** $A$ 的列 3 變紫 → 嘗試用 $C$ 的當前列線組 → **能**（$\beta_1 = 1, \beta_2 = 1$）→ 「依賴，捨去」標記出現 → 紫色係數填入 $R$ 的第 3 行；
5. **(4s) 結束：** $C$ 和 $R$ 完成，$A$ 整體高亮 + 顯示 `A = CR` 等式；
6. **(5s) 自動切到 CR2 視角：** 重新掃描，但這次以**行**為單位（藍 → 紫順序），展示行視角的線組；
7. **(6s) 並排顯示：** CR1 + CR2 同時顯示，兩邊都標 $r = 2$，**動態箭頭連線**強調「同一個 $r$」。

**手動互動模式：**

- 用戶改 $A$ 的某個元素，**整個畫面 600ms 重排動畫**：rank 重算 / $C$ 列數可能變化 / $R$ 重生 / 拆解列重組；
- 拉桿改 $a_{ij}$ 為連續值（即時更新），讓用戶看到「微擾不改變 rank」vs 「特定值跳變導致 rank 改變」的對比。

##### F. 預設 demo 序列（教學節奏）

1. **範例 1（書中範例 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$，$r = 2$）：** 預設啟動，自動掃描一次，建立基線理解；
2. **範例 4（退化 $r = 1$）：** 三列全部依賴，$C$ 只有 1 列、$R$ 只有 1 行，凸顯「退化矩陣的窄腰」；
3. **範例 3（單位矩陣 $I_3$，$r = 3$）：** 所有列獨立，$C = I$、$R = I$，凸顯「滿秩 = CR 退化為 $A = AI$」；
4. **範例 5（陷阱題）：** 用戶手動掃描，發現列 3 是依賴的（雖然第一眼看不出來），訓練「不要靠視覺判斷獨立性，要用線組驗證」的習慣。

##### G. 色彩與樣式

- 綠 `#2ca02c`（$C$ 的列、CR1 的拆解列、$Q^{\mathrm{T}}$ 同色）；
- 粉紅 `#d62728`（$R$ 的行、CR2 的拆解行）；
- 藍 `#1f77b4`（CR1 範例的列 1 標記、CR2 範例的行 1 標記）；
- 橙 `#ff7f0e`（CR1 範例的列 2 標記）；
- 紫 `#9467bd`（CR1 範例的列 3 標記、CR2 範例的行 2 標記，對應 §5 動態系統紫色）；
- 灰 `#cccccc`（$A$ 的占位 / 「依賴列被捨去」的剪頭線）。

**色彩設計原則：** 跟原書 CR1 / CR2 圖完全一致的「藍 / 橙 / 紫」色標，並與 §5 的對應色彩語義對接（紫色 = 「特殊」或「動態演化」的色）。

##### H. 公式同步區（Equation Sync Panel）

底部固定一個 LaTeX 公式區，依當前掃描狀態動態更新：

```
(初始)         A = ?
(掃完列1)      A = [c_1 ...] [1 ...] = ...
(掃完列2)      A = [c_1, c_2] [1 0; 0 1; ...] = ...
(掃完列3，列3依賴)  A = CR = [c_1, c_2] [1 0 1; 0 1 1]   ✓ rank = 2
```

**hover $C$ 的某列 → 高亮 $A$ 中對應的所有「使用該列的列」**（藍橙紫色重疊）；hover $R$ 的某行 → 高亮 $A$ 中對應的「以該行為基的行」。

##### I. 邊界條件與防呆

- **零矩陣：** $A = 0$ 時 $r = 0$、$C$ 和 $R$ 都是空矩陣，顯示「rank = 0，列空間 = 行空間 = {0}」；
- **單列矩陣：** $n = 1$ 時 $C = \mathbf{a}_1$、$R = [1]$（若 $\mathbf{a}_1 \neq 0$）；
- **rank 重算的數值穩定性：** 用「列向量是否與 $C$ 已有列的線組差 < $\epsilon$ = 1e-10」判定，不用嚴格 = 0；
- **退化視覺：** rank 變化時，被捨去的列顯示「→ 0」淡出動畫，不是直接消失（教學上要看到「被捨去」這個動作）。

##### J. 教學節奏建議

- **第 1 階段（0–2 分鐘）：** 預設範例 1 自動播放，建立「掃描 + 獨立 / 依賴 + 三色標記」的基線；
- **第 2 階段（2–5 分鐘）：** 切換 CR1 ↔ CR2 視角，看「列空間 / 行空間」的對偶；
- **第 3 階段（5–10 分鐘）：** 切到並排視角，**動態箭頭強調「同一個 $r$」**，建立列秩 = 行秩反射弧；
- **第 4 階段（10–15 分鐘）：** 嘗試不同預設範例，特別是退化（範例 4）和陷阱題（範例 5）；
- **第 5 階段（15+ 分鐘）：** 點跳轉按鈕，到 ch04/ch05 看 (MM4) 累加和 (P1)/(P2) 對角特例；回流時保持當前 $A$ 的設定。

##### K. 變化版本（Variation）

- **「教師模式」：** 加教師控制台，可逐步播放（一步一停）並用解說條解釋每步動作；
- **「測驗模式」：** 隨機生成矩陣，讓用戶手動標記獨立 / 依賴列，自動評分；
- **「歷史回放」：** 用戶調過的 $A$ 序列存在側邊欄，可回看歷次 $r$ 變化（建立「rank 是 robust 的」直覺）。

##### L. 跨章 pointer 細節

**Pointer 1：「→ (MM4) 秩 1 累加」（跳 ch04 VizScript-02）**

- 帶參數：$(\mathbf{c}_1, \mathbf{r}^{*}_1)$、$(\mathbf{c}_2, \mathbf{r}^{*}_2)$、...、$(\mathbf{c}_r, \mathbf{r}^{*}_r)$；
- ch04 VizScript-02 接收後自動載入 $r$ 個秩 1 層；
- 用戶在 ch04 看完累加動畫後，「返回 CR」按鈕跳回 ch06b 並保留當前 $A$。

**Pointer 2：「→ (P1)(P2) 對角矩陣特例」（跳 ch05 VizScript-01）**

- 帶參數：把 $R$ 強制改為對角矩陣 $D = \operatorname{diag}(R_{11}, R_{22}, ..., R_{rr})$；
- ch05 VizScript-01 演示 $CD$ 的列縮放（即 (P1) 特例）；
- 教學含義：「如果 $R$ 是對角，CR 就退化為 (P1) 列縮放；CR 是 (P1) 的一般化」。

##### M. 驗收條件（Acceptance Criteria）

- 用戶修改 $A$ 的任一元素，整個畫面 < 800ms 完成重排（含 rank 重算、$C$/$R$ 重組、三色重標）；
- CR1 ↔ CR2 視角切換動畫流暢（800ms ease-in-out，色塊重排不跳變）；
- 並排視角下，兩個 $r$ 標記**完全同步**變化（測試列秩 = 行秩的視覺一致性）；
- 範例 1 自動掃描完整跑完 ≤ 6 秒，每步驟（列 1 / 列 2 / 列 3）有明確的「獨立 / 依賴」標記出現；
- 兩個跳轉按鈕能正確帶參數跳到 ch04 / ch05 的對應 VizScript，且能正確返回；
- 退化矩陣（rank = 0、1）和滿秩矩陣的視覺呈現均正確（不出現「綠列 0 個」或「粉紅行 0 個」的崩潰）；
- 數值穩定性：用戶調 $a_{ij}$ 為「接近依賴」（如 $\epsilon$ 偏離整數），rank 不抖動。

---

#### VizScript-02: rank 與獨立列 / 行數的對應動畫（Rank–Independence Tracker）

**Tier：** ⭐⭐ Tier 1（精簡 13 段，重點演示「改 $A$ 看 $r$ 變化」，不涉及 CR1/CR2 兩視角切換）
**對應 VizMark：** Figure 6.1 VizMark-02、Figure 6.2 VizMark-02
**預估實作工作量：** S12+ 約 0.5 session（重用 VizScript-01 的 rank 計算邏輯，畫面簡化）

##### A–C 簡述

- **定位：** 「用戶改 $A$ 的某一列為其他列的線組，看 $r$ 從 3 跳到 2，$C$ 的綠列數從 3 個降到 2 個、$R$ 的粉紅行數同步從 3 個降到 2 個」；
- **學習目標：** rank 是 $A$ 的「內在維度」，獨立於畫面表現；視覺看到 $r$ 和 $C/R$ 形狀的一致變化；
- **互動參數：** 預設 $3 \times 3$ 矩陣 + 滑桿可拉某列為其他列的線組（$\alpha, \beta$ 雙滑桿）。

##### D–F 簡述

- **布局：** 左區 $A$ 輸入 + $r$ 大字顯示、右區 $C$ / $R$ 並排（綠列 + 粉紅行）；
- **動畫：** 用戶拉滑桿讓 $\mathbf{a}_3 \to \alpha \mathbf{a}_1 + \beta \mathbf{a}_2$，rank 從 3 → 2 的瞬間 $C$ 的第 3 列「淡出 + 飛向 $R$ 的第 3 行作為線組係數」；
- **demo 序列：** rank 3 → rank 2（第 3 列被吸收） → rank 1（第 2 列也被吸收）→ rank 0（全零）。

##### G–M 簡述

- **色彩 / 公式：** 同 VizScript-01；
- **驗收：** rank 跳變的動畫流暢、$C/R$ 形狀變化與 rank 同步、退化情況不崩潰；
- **教學節奏：** 5 分鐘內讓用戶建立「rank 是 $A$ 的本質、$C/R$ 形狀是 rank 的視覺化」直覺。

---

#### VizScript-03: 2×3 範例逐步 walkthrough（Step-by-step CR Demo）

**Tier：** ⭐ Tier 1（輕量版，僅針對書中範例 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$ 一步一步動畫）
**對應 VizMark：** Figure 6.1 VizMark-03
**預估實作工作量：** S12+ 約 0.3 session（硬編碼書中範例的步驟）

##### 簡述

- **定位：** 「用書中 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$ 一步一步示範 CR 掃描，每步顯示『該列獨立還是依賴』+ 數值計算」；
- **互動：** 「下一步」按鈕逐步前進、「自動播放」按鈕、「重置」按鈕；
- **每步畫面：**
  - 步 1：「掃列 1，獨立，加入 $C$ 作為 $\mathbf{c}_1 = (1, 2)^{\mathrm{T}}$」；
  - 步 2：「掃列 2，嘗試 $\alpha \mathbf{c}_1$ 不能匹配 $(2, 3)$，獨立，加入 $C$ 作為 $\mathbf{c}_2 = (2, 3)^{\mathrm{T}}$」；
  - 步 3：「掃列 3，嘗試 $\beta_1 \mathbf{c}_1 + \beta_2 \mathbf{c}_2 = (3, 5)$ → $\beta_1 = 1, \beta_2 = 1$，依賴，捨去」；
  - 步 4：「完成 $A = CR$」+ 顯示完整公式 + 驗證乘法結果；
- **特色：** 適合初次學 CR 的讀者，可印刷成靜態 PDF 教材；
- **跨章 pointer：** 結束時顯示按鈕「→ 看其他範例（VizScript-01）」、「→ (P1)(P2) 對角特例（ch05）」、「→ (MM4) 秩 1 累加（ch04）」。

---

### 章末延伸

- **後續章節連結：**
  - [→ ch06c-LU.md](ch06c-LU.md)（§6.2 $A=LU$ — Gaussian 消去法的 CR 三角化升級）
  - [→ ch06d-QR.md](ch06d-QR.md)（§6.3 $A=QR$ — CR 的正交化升級，$C$ 變正交 $Q$）

- **前置章節傳承：**
  - [← ch04-mat-mat.md](ch04-mat-mat.md) §4 (MM4)：$A = \sum \mathbf{c}_p \mathbf{r}^{*}_p$ 母模板；
  - [← ch05-patterns.md](ch05-patterns.md) §5 (P1)/(P2)：CR1 = (P1) 列觀點、CR2 = (P2) 行觀點 — **原書直接標 `using P1` / `using P2`**；
  - [← ch06a-five.md](ch06a-five.md) §6 總覽：CR 是 5 大分解的「最少要求」起點。

- **延伸閱讀：**
  - Gilbert Strang《Linear Algebra for Everyone》§1.4「Matrix Multiplication and $A = CR$」p.29 — 本章原始來源；
  - Strang《Linear Algebra for Everyone》§3.2「Independent Columns and the Column Space」— RREF 計算細節；
  - 附錄 `World_of_Matrices.png` — CR 在矩陣世界地圖中是「最一般」的起點。

- **對 RREF 計算的補充：** 本章只演示「依結果說明 $R$」，沒詳述「如何由 $A$ 計算 RREF」— Gaussian 消去法的細節留給 §6.2 LU 章。讀者若需要對應的數值算法，可看：
  - Trefethen & Bau《Numerical Linear Algebra》Lecture 20 (Gaussian elimination with partial pivoting)；
  - SciPy `scipy.linalg.lu` / NumPy `numpy.linalg.matrix_rank` 等工程實作。

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` §6.1 $A=CR$（en.md line 256–305）/ `The-Art-of-Linear-Algebra.pdf` p.8–p.9（含圖 11、12）
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` §6.1 $A=CR$（zh.md line 248–293）
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0

---

> **撰寫者註（S07）：** 本章是 §6 五大分解的「第一章詳細版」。**S07 重大發現：** 原書 CR1/CR2 圖明標 `using P1` / `using P2`，**直接連結到 §5 (P1)(P2) Pattern**。這意味著 §6.1–§6.5 都會把 §5 Pattern 標籤套到對應的分解視角圖上（後續章節需逐章核對 PNG 是否有 `using PX` 標記，可能影響 VizScript 跨章 pointer 設計）。本章 VizScript-01 因此採取**雙 pointer 策略**：(MM4) 累加 → ch04 VizScript-02；(P1)(P2) 對角特例 → ch05 VizScript-01。本策略首次驗證「同一 VizScript 雙向 pointer」可行性，後續 §6.2–§6.5 可複用。

---

## 6.2 矩陣分解 2：$A = LU$（Lower–Upper Triangular Factorization）

> **原書頁碼：** p.9–p.10
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.2 $A=LU$（en.md line 307–377 / zh.md line 295–365）
> **本章圖數：** 2（`LU1.png` 無標、`LU2.png` 明標 **using MM4**）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S08）

---

### 章節摘要

$A = LU$ 是 §6 五大分解的**第二個**，也是與「**手算求解 $A\mathbf{x} = \mathbf{b}$**」最直接相關的一個。它的物理出發點是**高斯消去法**（Gaussian elimination）：把方陣 $A$ 用一連串的「行運算」（row operations）化簡成上三角矩陣 $U$，而把這些行運算「記下來」（順序）形成的下三角矩陣 $L$（單位對角）正好滿足 $A = LU$。

具體流程：

1. 用初等行運算矩陣 $E$ 把 $A$ 變成上三角 $U$：$EA = U$；
2. 反推：$A = E^{-1} U$，令 $L = E^{-1}$（必為下三角且對角線為 1）；
3. 得 $A = LU$，**$L$ 下三角 + 單位對角、$U$ 上三角 + 主元（pivots）在對角**。

求解 $A\mathbf{x} = \mathbf{b}$ 因此可拆成**兩步三角方程**：

$$
A\mathbf{x} = \mathbf{b} \;\Longleftrightarrow\; LU\mathbf{x} = \mathbf{b} \;\Longleftrightarrow\;
\begin{cases} L\mathbf{c} = \mathbf{b} & \text{(前代 / forward substitution)} \\ U\mathbf{x} = \mathbf{c} & \text{(後代 / back substitution)} \end{cases}
$$

這把「一個 $n \times n$ 的全密集方程」轉成「兩個 $n \times n$ 的三角方程」，計算量從 $O(n^3)$ 的高斯消去（含主元搜尋）降為 $O(n^2)$ 的兩次三角回代 — 在多個右端項 $\mathbf{b}_1, \mathbf{b}_2, \ldots$ 共用同一個 $A$ 時，**$LU$ 只算一次、回代算多次**，是數值線性代數最重要的計算結構之一。

本章的「視覺出發點」與 §6.1 CR 不同：

- **§6.1 CR** 是「掃描列、留獨立」的直觀算法；
- **§6.2 LU** 是「**遞迴 rank 1 peeling**」— 從 $A$ 的左上角剝下一個秩 1 矩陣（$\mathbf{l}_1 \mathbf{u}^*_1$）、留下右下角的子矩陣 $A_2$、再對 $A_2$ 重複，剝下第二個秩 1 矩陣……直到剝光。最後 $n$ 個 $\mathbf{l}_p \mathbf{u}^*_p$ 拼起來就是 $LU$。

**與 §4 (MM4) 的連結是 LU 視覺化的核心：** 原書 `LU2.png` 右下角直接標 `using MM4`，明示「$LU$ 是 (MM4) 的特例 — 但 $\mathbf{l}_p$ 是下三角列、$\mathbf{u}^*_p$ 是上三角行」。本章 VizScript 因此採**單 pointer 策略**：(MM4) 累加 demo 直接 pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)；本章獨立寫的是 **peeling 過程動畫 + 高斯消去步驟對齊 + 三角結構視覺化** 等 LU 特有的內容。

數值範例（本章貫穿，原書 Sec.2.3 經典示範）：

$$
A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}
\;=\;
\underbrace{\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}}_{L}
\underbrace{\begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}}_{U}
$$

讀者用高斯消去驗證：

1. 第二行 $-$ 2 × 第一行：$(4, 3, 3) - 2(2, 1, 1) = (0, 1, 1)$（$L_{21} = 2$）；
2. 第三行 $-$ 4 × 第一行：$(8, 7, 9) - 4(2, 1, 1) = (0, 3, 5)$（$L_{31} = 4$）；
3. 第三行 $-$ 3 × 新的第二行：$(0, 3, 5) - 3(0, 1, 1) = (0, 0, 2)$（$L_{32} = 3$）；
4. 得 $U$，$L$ 即記下的「行乘數」加上單位對角線。

---

### 數學要點

#### 1. 定義與形狀

$$
A_{n \times n} = L_{n \times n} \, U_{n \times n}
$$

- **$L$（Lower triangular）：** 下三角矩陣，**對角線元素恆為 1**（單位下三角 / unit lower triangular），對角線下方填消去過程的「行乘數」$L_{ij} = \dfrac{a_{ij}^{(j)}}{a_{jj}^{(j)}}$（$i > j$）；
- **$U$（Upper triangular）：** 上三角矩陣，**對角線元素是主元**（pivots）$u_{ii}$，對角線上方填消去後的剩餘元素，對角線下方全為零；
- **形狀：** 兩者都是 $n \times n$ 方陣（$LU$ 標準形式要求 $A$ 是方陣）；
- **可分解條件：** 若高斯消去過程**不需要換行**（即所有主元都非零），則 $A$ 可分解為 $LU$。若需要換行，則 $PA = LU$，其中 $P$ 是置換矩陣（permutation）— 本章先處理 $A = LU$ 的乾淨情形。

#### 2. 與 (MM4) 視角的連結 — 秩 1 之和（核心 ⭐）

把 $A = LU$ 套用 §4 (MM4) 「列 × 行外積之和」視角：

$$
A = LU = \sum_{p=1}^{n} \mathbf{l}_p \, \mathbf{u}^{*}_p
$$

- $\mathbf{l}_p$ = $L$ 的第 $p$ 列（綠色直立，**從第 $p$ 列起非零**，前面 $p-1$ 個元素必為 0）；
- $\mathbf{u}^{*}_p$ = $U$ 的第 $p$ 行（粉紅橫躺，**從第 $p$ 行起非零**，前面 $p-1$ 個元素必為 0）；
- $\mathbf{l}_p \mathbf{u}^*_p$ 是「左上角為零、右下角為秩 1 子塊」的特殊秩 1 矩陣 — 視覺上像「**從左上角向右下角延伸的秩 1 楔形**」（wedge）。

**關鍵差異對比 §6.1 CR：**

| 性質 | $A = CR$（$r$ 項） | $A = LU$（$n$ 項） |
|---|---|---|
| 項數 | $r = \operatorname{rank}(A)$ | $n$（即使 rank 不足，項數仍是 $n$，只是某些 $\mathbf{l}_p \mathbf{u}^*_p$ 變成全零項） |
| $\mathbf{l}_p$ / $\mathbf{c}_p$ 結構 | $\mathbf{c}_p$ 可任意（從 $A$ 取獨立列） | $\mathbf{l}_p$ **強制下三角**：前 $p-1$ 個元素為 0 |
| $\mathbf{u}^*_p$ / $\mathbf{r}^*_p$ 結構 | $\mathbf{r}^*_p$ 可任意（RREF 行） | $\mathbf{u}^*_p$ **強制上三角**：前 $p-1$ 個元素為 0 |
| 視覺特徵 | 綠列 × 粉紅行的「完整網格」 | 綠列 × 粉紅行的「**右下角楔形**」（左上 $p-1$ 行/列為零） |
| 連結 §5 | (P1)/(P2)（using P1/P2 標記） | (MM4)（using MM4 標記） |

**範例展開（$n = 3$，原書 Sec.2.3 範例）：**

$$
A = \mathbf{l}_1 \mathbf{u}^*_1 + \mathbf{l}_2 \mathbf{u}^*_2 + \mathbf{l}_3 \mathbf{u}^*_3
$$

具體計算：

- $\mathbf{l}_1 \mathbf{u}^*_1 = \begin{bmatrix}1\\2\\4\end{bmatrix} \begin{bmatrix}2 & 1 & 1\end{bmatrix} = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 2 & 2 \\ 8 & 4 & 4 \end{bmatrix}$（**滿格秩 1，是 $A$ 的「外層楔形」**）；

- $\mathbf{l}_2 \mathbf{u}^*_2 = \begin{bmatrix}0\\1\\3\end{bmatrix} \begin{bmatrix}0 & 1 & 1\end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 3 & 3 \end{bmatrix}$（**第 1 行 / 列為零，右下 2×2 秩 1，是 $A_2$ 的「外層楔形」**）；

- $\mathbf{l}_3 \mathbf{u}^*_3 = \begin{bmatrix}0\\0\\1\end{bmatrix} \begin{bmatrix}0 & 0 & 2\end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 2 \end{bmatrix}$（**只剩右下角單一元素，是 $A_3$ 的「核」**）；

- 三項相加 $= \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix} = A \;\checkmark$。

**這就是 `LU2.png` 標 `using MM4` 的意義：** 三個秩 1 矩陣相加 = $A$，**每個秩 1 矩陣的「非零範圍」逐層向右下角縮小**（楔形 → 楔形 → 點），這是 (MM4) 在「三角結構」中的特化。

#### 3. 高斯消去（Gaussian Elimination）= 反向 peeling

把第 2 節的展開「**從 $A$ 倒推**」就是高斯消去：

$$
A_1 = A, \quad A_{p+1} = A_p - \mathbf{l}_p \mathbf{u}^*_p, \qquad p = 1, 2, \ldots, n
$$

具體過程（以本章範例為例）：

| 步驟 | 動作 | 矩陣狀態 |
|---|---|---|
| $p = 1$ | 取 $A_1 = A$ 第 1 行 $\mathbf{u}^*_1 = (2, 1, 1)$；取第 1 列 $\div$ 主元 $\mathbf{l}_1 = (1, 2, 4)^{\mathrm{T}}$（除以 $a_{11} = 2$） | $A_1 = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}$ |
| $A_2 = A_1 - \mathbf{l}_1 \mathbf{u}^*_1$ | 第 1 行 / 列「**清零**」，子矩陣 $A_2$ 出現於右下 | $A_2 = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 3 & 5 \end{bmatrix}$ |
| $p = 2$ | 取 $A_2$ 第 2 行 $\mathbf{u}^*_2 = (0, 1, 1)$；取第 2 列 $\div$ 主元 $\mathbf{l}_2 = (0, 1, 3)^{\mathrm{T}}$ | $A_2$（同上） |
| $A_3 = A_2 - \mathbf{l}_2 \mathbf{u}^*_2$ | 第 2 行 / 列也清零 | $A_3 = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 2 \end{bmatrix}$ |
| $p = 3$ | 取 $A_3$ 第 3 行 $\mathbf{u}^*_3 = (0, 0, 2)$；取第 3 列 $\div$ 主元 $\mathbf{l}_3 = (0, 0, 1)^{\mathrm{T}}$ | $A_3$（同上） |
| $A_4 = A_3 - \mathbf{l}_3 \mathbf{u}^*_3$ | 全零，結束 | $\mathbf{0}$ |

完整對應：

- $L = [\mathbf{l}_1 \;|\; \mathbf{l}_2 \;|\; \mathbf{l}_3] = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}$（每個 $\mathbf{l}_p$ 排成 $L$ 的第 $p$ 列）；
- $U = \begin{bmatrix} \mathbf{u}^*_1 \\ \mathbf{u}^*_2 \\ \mathbf{u}^*_3 \end{bmatrix} = \begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}$（每個 $\mathbf{u}^*_p$ 排成 $U$ 的第 $p$ 行）。

**遞迴 peeling 的視覺隱喻：** $A$ 像一個三層洋蔥，每次剝掉外層的「秩 1 楔形」（$\mathbf{l}_p \mathbf{u}^*_p$），露出內層更小的子矩陣 $A_{p+1}$。最後一層是右下角一個純量（主元 $u_{nn}$）。**這是 LU1 圖的核心訊息**。

#### 4. 求解 $A\mathbf{x} = \mathbf{b}$ 的兩步法（Forward + Back Substitution）

求解流程：

$$
A\mathbf{x} = \mathbf{b} \quad\Longleftrightarrow\quad LU\mathbf{x} = \mathbf{b} \quad\Longleftrightarrow\quad
\underbrace{L\mathbf{c} = \mathbf{b}}_{\text{前代}} \;\to\; \underbrace{U\mathbf{x} = \mathbf{c}}_{\text{後代}}
$$

**前代（forward substitution）：** $L\mathbf{c} = \mathbf{b}$ 中 $L$ 下三角且對角為 1：

$$
\begin{cases}
c_1 = b_1 \\
c_2 = b_2 - L_{21} c_1 \\
c_3 = b_3 - L_{31} c_1 - L_{32} c_2 \\
\vdots
\end{cases}
$$

**從第 1 行往下推**，每行只用「前面已算好的 $c$」減去乘積。

**後代（back substitution）：** $U\mathbf{x} = \mathbf{c}$ 中 $U$ 上三角且對角為主元：

$$
\begin{cases}
x_n = c_n / u_{nn} \\
x_{n-1} = (c_{n-1} - u_{n-1,n} x_n) / u_{n-1, n-1} \\
\vdots \\
x_1 = (c_1 - u_{12} x_2 - \cdots - u_{1n} x_n) / u_{11}
\end{cases}
$$

**從第 $n$ 行往上推**，每行只用「後面已算好的 $x$」減去乘積、除以主元。

**範例：** 設 $\mathbf{b} = (1, 5, 17)^{\mathrm{T}}$，用上面的 $L, U$ 求 $\mathbf{x}$。

1. **前代** $L\mathbf{c} = \mathbf{b}$：
   - $c_1 = 1$；
   - $c_2 = 5 - 2 \cdot 1 = 3$；
   - $c_3 = 17 - 4 \cdot 1 - 3 \cdot 3 = 4$；
   - $\mathbf{c} = (1, 3, 4)^{\mathrm{T}}$。

2. **後代** $U\mathbf{x} = \mathbf{c}$：
   - $x_3 = 4 / 2 = 2$；
   - $x_2 = (3 - 1 \cdot 2) / 1 = 1$；
   - $x_1 = (1 - 1 \cdot 1 - 1 \cdot 2) / 2 = -1$；
   - $\mathbf{x} = (-1, 1, 2)^{\mathrm{T}}$。

3. **驗證** $A\mathbf{x}$：$\begin{bmatrix}2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9\end{bmatrix} \begin{bmatrix}-1 \\ 1 \\ 2\end{bmatrix} = \begin{bmatrix}-2+1+2 \\ -4+3+6 \\ -8+7+18\end{bmatrix} = \begin{bmatrix}1 \\ 5 \\ 17\end{bmatrix} = \mathbf{b}$ ✓。

**多右端項的優勢：** 對 $k$ 個不同的 $\mathbf{b}_1, \ldots, \mathbf{b}_k$，分解 $LU$ 只算一次（$O(n^3)$），之後每個 $\mathbf{b}_i$ 只要 $O(n^2)$ 回代。**這是反矩陣 $A^{-1}$ 不需要也不該明算的數值理由** — 用 $LU$ 解一連串 $A\mathbf{x}_i = \mathbf{b}_i$ 永遠比算出 $A^{-1}$ 再相乘穩定且高效。

#### 5. 為什麼 $L$ 必為「單位下三角」、$U$ 必為「上三角」

從第 3 節的構造看：

- **$\mathbf{l}_p$ 的形狀**（$p = 1, \ldots, n$）：
  - 前 $p-1$ 個元素為 0（因為 $A_p$ 的前 $p-1$ 行 / 列已被前面的 peeling 清零）；
  - 第 $p$ 個元素 $= 1$（取自身行除以自己 = 1，即 $A_p$ 的 $(p, p)$ 主元除以自己）；
  - 第 $p+1, \ldots, n$ 個元素 $=$ $A_p$ 的第 $p$ 列下方元素除以主元；
  - 排成 $L$ 的第 $p$ 列 → **下三角 + 對角 = 1**。

- **$\mathbf{u}^*_p$ 的形狀**：
  - 前 $p-1$ 個元素為 0；
  - 第 $p$ 個元素 $=$ 主元 $u_{pp}$；
  - 第 $p+1, \ldots, n$ 個元素 $=$ $A_p$ 的第 $p$ 行右側元素；
  - 排成 $U$ 的第 $p$ 行 → **上三角**。

**視覺化記憶口訣：** 「$L$ 對角為 1 是因為主元搬到 $U$」— $A_p$ 的 $(p, p)$ 元素本身既是 $\mathbf{l}_p$ 的第 $p$ 個（除以自己 = 1），又是 $\mathbf{u}^*_p$ 的第 $p$ 個（保留原值 = 主元）。**這個「分配」是 $LU$ 唯一性的關鍵**（若不規定 $L$ 對角為 1，主元可以隨意分配給 $L$ 或 $U$）。

#### 6. $A = LU$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **LU ↔ CR** | LU 是「方陣 + 三角結構」的 CR，項數變 $n$ 而非 $r$，且 $\mathbf{l}_p, \mathbf{u}^*_p$ 多了「前綴零」的三角限制 |
| **LU ↔ QR** | QR 把「下三角 $L$」換成「正交 $Q$」（保留 $R$ 上三角）— $A = QR$ 的 $Q$ 是「$A$ 的列做 Gram–Schmidt」後得到的正交基底。**從 LU 到 QR = 把 $L$ 正交化** |
| **LU ↔ SVD** | SVD 把「下三角 $L$ + 上三角 $U$」雙端都換成正交（$U, V^{\mathrm{T}}$），中間留對角 $\Sigma$。**從 LU 到 SVD = 兩端都正交化** |
| **LU ↔ QΛQᵀ** | QΛQᵀ 限對稱 $S$ 且 $L = Q$、$U = \Lambda Q^{\mathrm{T}}$；對對稱 $S$ 還有 $S = LDL^{\mathrm{T}}$（Cholesky 的廣義版），與 $LU$ 同源但加對稱性 |

**結論：** $A = LU$ 是「**最少結構**」的數值分解 — 只要求 $A$ 是「無需換行」的方陣，分解後的 $L, U$ 各保留三角結構。其他三個更高階分解（QR、QΛQᵀ、SVD）都可以看成「在 LU 的三角結構上**疊正交性**」。從教學順序看，**LU 是進入「分解的數值意義」最自然的起點**（解方程 + 多右端項），CR 是進入「分解的概念意義」最自然的起點（列秩 = 行秩）。

#### 7. 數學要點總結（一張表）

| 性質 | $A = LU$ 的對應 |
|---|---|
| 適用矩陣 | 方陣 $A_{n \times n}$，無需換行（即所有主元非零）；否則需 $PA = LU$ |
| $L$ 的結構 | 下三角 + 單位對角，下方填行乘數 $L_{ij}$ |
| $U$ 的結構 | 上三角 + 主元在對角，上方填消去剩餘元素 |
| 項數 | $n$（即使退化，項數仍 $n$，但某些 $\mathbf{l}_p \mathbf{u}^*_p$ 為全零） |
| 構造方法 | 高斯消去（前向）/ rank 1 peeling（等價反向）|
| §4 (MM4) 對應 | $A = \sum_{p=1}^{n} \mathbf{l}_p \mathbf{u}^*_p$（**`LU2.png` 標 `using MM4`**）|
| §5 Pattern 對應 | 無直接 (P1)(P2) 標記（不像 §6.1 CR）；但 (MM4) = (P1) 廣義版 |
| 求解 $A\mathbf{x} = \mathbf{b}$ | 兩步：$L\mathbf{c} = \mathbf{b}$（前代）+ $U\mathbf{x} = \mathbf{c}$（後代）|
| 計算量 | $LU$ 分解 $O(n^3)$、回代 $O(n^2)$；多右端項共用 $LU$ 大幅省時 |

---

### 圖片詳細描述（Figure Descriptions）

#### Figure 6.3: 從 $A$ 遞迴 rank 1 peeling 得到 $L, U$（LU1）

**圖檔：** `docs/book/figs-png/LU1.png`（原始 EPS：`figs/LU1.eps`）
**原書頁碼：** p.9 圖 13
**所屬章節：** §6.2 $A = LU$（peeling 解構視角）
**圖中標記：** 無 `using PX` 標籤（與 §6.1 CR1/CR2、§6.2 LU2 不同）

##### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，共 9 段：

1. **第 1 段：** 矩陣 $A$ 的方框（灰色填充正方形），上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 第 1 個秩 1 矩陣 — 方框內**整個外層**有色填充：**第 1 行（粉紅橫條）+ 第 1 列（綠直條）+ 內部灰底**（代表「外層楔形 = $\mathbf{l}_1 \mathbf{u}^*_1$ 的非零範圍佔據整個矩陣」）；
4. **第 4 段：** 加號 `+`；
5. **第 5 段：** 第 2 個秩 1 矩陣 — 方框內**第 2 行（粉紅橫條，較第 1 個小）+ 第 2 列（綠直條，較小）+ 右下灰底**（外層楔形向內縮一格）；
6. **第 6 段：** 加號 `+`；
7. **第 7 段：** 第 3 個秩 1 矩陣 — 方框內**只有右下角一小塊粉紅 + 一小塊綠**（外層楔形縮到最內，剩單一像素點）；
8. **第 8 段：** 等號 `=`；
9. **第 9–10 段：** 結果 $L$ 和 $U$：
   - $L$：方框內 **3 條等寬綠色直立列，從高到低**（$\mathbf{l}_1$ 最高滿格、$\mathbf{l}_2$ 中、$\mathbf{l}_3$ 最矮）— 視覺直觀展示「下三角 + 對角 1」；
   - $U$：方框內 **3 條等高粉紅橫躺行，從長到短**（$\mathbf{u}^*_1$ 最長、$\mathbf{u}^*_2$ 中、$\mathbf{u}^*_3$ 最短）— 視覺直觀展示「上三角 + 主元」。

**閱讀順序：** 由左到右讀「$A$ = 楔形 1 + 楔形 2 + 楔形 3 = $L$ × $U$」。**注意三個楔形的「非零範圍逐層向右下角縮小**」的視覺序列 — 這是 peeling 過程的核心訊息。

##### 數學內容 (Mathematical Content)

對應原書 §6.2 的核心公式：

$$
A = \underbrace{\mathbf{l}_1 \mathbf{u}^*_1}_{\text{楔形 1（滿格）}}
+ \begin{bmatrix} 0 & 0 & 0 \\ 0 & \multicolumn{2}{c}{} \\ 0 & \multicolumn{2}{c}{A_2} \end{bmatrix}
= \underbrace{\mathbf{l}_1 \mathbf{u}^*_1}_{\text{楔形 1}}
+ \underbrace{\mathbf{l}_2 \mathbf{u}^*_2}_{\text{楔形 2}}
+ \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & A_3 \end{bmatrix}
= L U
$$

對應本章範例 $A = \bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$：

- **楔形 1** $= \mathbf{l}_1 \mathbf{u}^*_1 = \begin{bmatrix}2 & 1 & 1\\ 4 & 2 & 2\\ 8 & 4 & 4\end{bmatrix}$（**整個 3×3 都有色**，因 $\mathbf{l}_1, \mathbf{u}^*_1$ 全非零）；
- **楔形 2** $= \mathbf{l}_2 \mathbf{u}^*_2 = \begin{bmatrix}0 & 0 & 0\\ 0 & 1 & 1\\ 0 & 3 & 3\end{bmatrix}$（**右下 2×2 有色**，第 1 行 / 列為零）；
- **楔形 3** $= \mathbf{l}_3 \mathbf{u}^*_3 = \begin{bmatrix}0 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 2\end{bmatrix}$（**只右下 1×1 有色**）。

**注意「綠色直條」與「粉紅橫條」的視覺對應：**

- $\mathbf{l}_p$ 直立排在「綠列」位置，所以圖中每個楔形的左側總有一條綠色直條；
- $\mathbf{u}^*_p$ 橫躺排在「粉紅行」位置，所以圖中每個楔形的頂端總有一條粉紅橫條；
- 兩者相交的「左上格」是楔形的「主元位置」（雖然圖中顯示為整個內框灰色，但實際是 $L_{pp} \cdot u_{pp}$ 的乘積，這個位置決定整個楔形的縮放）。

##### 直覺解讀 (Intuition)

LU1 是「**從 $A$ 倒推到 $L, U$**」的視覺證明 — 與 §6.1 CR 「掃描列、留獨立」的離散邏輯不同，**LU 是「連續剝皮」的視覺**：

- **三個楔形視覺上「**逐層向右下角縮小**」** — 楔形 1 最大（滿格）、楔形 2 中等（右下 2×2）、楔形 3 最小（右下 1×1）；
- **每個楔形的「綠列」和「粉紅行」共用一個主元** — 第 $p$ 個楔形的主元在 $(p, p)$ 位置；
- **三個楔形之和精確還原 $A$** — 因為「外層楔形 + 內層子矩陣」就是 $A$ 的一個重新拆解，且每次拆解都剝掉一個秩 1（rank 1）的部分；
- **最終結果 $L$ 的「綠列高度」與 $U$ 的「粉紅行長度」對應** — $\mathbf{l}_1$ 是最高的（滿格 $n$ 個元素，3 個），$\mathbf{l}_n$ 是最矮的（只有自己一個元素，1 個）；$\mathbf{u}^*_1$ 是最長的（$n$ 個元素），$\mathbf{u}^*_n$ 是最短的（1 個）。

**為什麼沒有 `using PX` 標籤？** 因為 LU1 強調的是 **「**從 $A$ 解構到子矩陣 $A_2, A_3$**」** 的遞迴過程，是「**消去演算法的視覺化**」，不是「線性組合視角」（P1/P2）也不是「外積累加視角」（MM4）。LU1 與 LU2 構成對偶：**LU1 = 解構（peeling）、LU2 = 重組（MM4 累加）**。

**這張圖該做成互動視覺化的理由：** 靜態圖只能展示三個固定的楔形，**互動 demo 可以讓用戶調 $A$ 看到每個楔形如何隨主元變化、消去過程如何遞迴前進、子矩陣 $A_2, A_3$ 如何「浮現」於右下角**。這是把「高斯消去」從「行運算口訣」變成「視覺數字流動」的最佳切入點。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [LU 雙視角切換 + 三色 rank 1 peeling 動畫] ⭐⭐⭐
> 「拉桿調 $A$ 的元素 → 動態剝下三個秩 1 楔形 → 同步顯示 $L, U$ 結構；toggle 切換 peeling 視角（LU1）/ MM4 合成視角（LU2）/ 並排兩者」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [高斯消去步驟對齊] ⭐⭐
> 「逐步消去動畫：每步顯示『目前主元位置 / 行乘數 $L_{ij}$ / 消去後的 $A_p$』，最後對齊到 $L, U$」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [3×3 範例 walkthrough] ⭐
> 「用書中範例 $\bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$ 一步一步動畫展示三次 peeling，每步顯示具體數字」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

#### Figure 6.4: 從 $L, U$ 用 (MM4) 重組 $A$（LU2）— 標 using MM4

**圖檔：** `docs/book/figs-png/LU2.png`（原始 EPS：`figs/LU2.eps`）
**原書頁碼：** p.9 圖 14
**所屬章節：** §6.2 $A = LU$（重組視角，**標 using MM4**）

##### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**（與 LU1 對偶但方向相反，從 $L, U$ 出發重組 $A$），共 11 段：

1. **第 1 段：** $L$（方框內 3 條綠色直立列，從高到低）；
2. **第 2 段：** $U$（方框內 3 條粉紅橫躺行，從長到短）；
3. **第 3 段：** 等號 `=`；
4. **第 4 段：** 第 1 個秩 1 矩陣 — 方框內**外層楔形**（第 1 行粉紅 + 第 1 列綠 + 內部灰）；
5. **第 5 段：** 加號 `+`；
6. **第 6 段：** 第 2 個秩 1 矩陣 — 方框內**第 2 層楔形**（第 2 行粉紅 + 第 2 列綠 + 右下 2×2 灰）；
7. **第 7 段：** 加號 `+`；
8. **第 8 段：** 第 3 個秩 1 矩陣 — 方框內**最內層**（只右下 1×1 粉紅 + 綠）；
9. **第 9 段：** （隱含）等號 `=` 連接到 $A$，但 LU2 圖直接終止於 3 個秩 1 矩陣的疊加（讀者心中想像疊加結果 = $A$）；
10. **第 10–11 段：** **右下角圖示**：圓圈內標 `MM 4`（兩行），左側文字 `using` — **直接標明「本圖用 §4 Pattern MM4 視角」**，即「矩陣乘法 = 列 × 行外積之和」。

**閱讀順序：** 由左到右讀整個等式鏈 $L \cdot U =$ 楔形 1 $+$ 楔形 2 $+$ 楔形 3。**「$\cdot$」隱在 $L$ 和 $U$ 並排之間**，因為 $LU$ 的乘法被 (MM4) 視角「拆解」為三個秩 1 矩陣的疊加。

##### 數學內容 (Mathematical Content)

對應數學表示（**(MM4) 視角的標準形式**）：

$$
LU = \sum_{p=1}^{n} \mathbf{l}_p \mathbf{u}^*_p
= \mathbf{l}_1 \mathbf{u}^*_1 + \mathbf{l}_2 \mathbf{u}^*_2 + \mathbf{l}_3 \mathbf{u}^*_3 = A
$$

對應本章範例：

- $\mathbf{l}_1 \mathbf{u}^*_1 = (1, 2, 4)^{\mathrm{T}} (2, 1, 1) = \begin{bmatrix}2&1&1\\4&2&2\\8&4&4\end{bmatrix}$；
- $\mathbf{l}_2 \mathbf{u}^*_2 = (0, 1, 3)^{\mathrm{T}} (0, 1, 1) = \begin{bmatrix}0&0&0\\0&1&1\\0&3&3\end{bmatrix}$；
- $\mathbf{l}_3 \mathbf{u}^*_3 = (0, 0, 1)^{\mathrm{T}} (0, 0, 2) = \begin{bmatrix}0&0&0\\0&0&0\\0&0&2\end{bmatrix}$；
- 三項相加 $= A$ ✓。

**與 §4 (MM4) 的關係（using MM4 標籤的重要性）：**

- §4 (MM4) 是「**$AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$**」的一般化版（$A$ 任意 $m \times k$，$B$ 任意 $k \times n$，$\mathbf{a}_p$ = $A$ 第 $p$ 列、$\mathbf{b}^*_p$ = $B$ 第 $p$ 行）；
- LU2 把這個 (MM4) **套用到 $L, U$**：$\mathbf{a}_p \to \mathbf{l}_p$、$\mathbf{b}^*_p \to \mathbf{u}^*_p$；
- 特化點：$\mathbf{l}_p$ 是「下三角列」（前 $p-1$ 個 0）、$\mathbf{u}^*_p$ 是「上三角行」（前 $p-1$ 個 0）— **這是 (MM4) 的「三角特例」**。

「`using MM4` 標籤」的意涵：原書作者**刻意**標明「LU 重組」就是 (MM4) 的應用。這代表視覺化可以**直接重用 ch04 VizScript-02 的秩 1 累加動畫**，只是把「自由的 $\mathbf{a}_p, \mathbf{b}^*_p$」換成「三角的 $\mathbf{l}_p, \mathbf{u}^*_p$」。這個跨章連結是 S07 PNG 重核發現的「**`using XX` 標記是跨章 pointer 官方鐵證**」的延續。

##### 與 LU1 的對偶關係（重要）

| | LU1 | LU2 |
|---|---|---|
| 視角 | 解構（從 $A$ 倒推 $L, U$）| 重組（從 $L, U$ 推 $A$）|
| 流程 | $A$ → 楔形 1 + $A_2$ → 楔形 1 + 楔形 2 + $A_3$ → ... → $LU$ | $L \cdot U$ → 楔形 1 + 楔形 2 + 楔形 3 → $A$ |
| 強調 | 「**剝皮**」（peeling）的遞迴過程 | 「**累加**」（accumulation）的展開過程 |
| 連結 §4/§5 | 無直接標籤（peeling 是 LU 特有演算法）| **`using MM4`**（直接點明 §4 (MM4)）|
| 教學意義 | 解釋「為什麼」可以分解（高斯消去）| 解釋「怎麼」用分解（重組）|
| 視覺化建議 | 動畫遞迴剝皮，子矩陣 $A_2, A_3$ 浮現 | 動畫秩 1 累加，pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) |

**這對「對偶圖」延續 §6.1 CR1/CR2 的全書一致模式：** 每個分解（CR、LU、QR、QΛQᵀ、SVD）都從「**正向**」（解構）和「**反向**」（重組）兩個方向各畫一張圖。S08 LU 進一步驗證了這個模式 — 預期 §6.4 QΛQᵀ 和 §6.5 SVD 也會有類似的對偶兩張圖。

##### 直覺解讀 (Intuition)

LU2 是「**$LU$ 怎麼重新組成 $A$**」的視覺證明 — 把 $L, U$ 的乘法「展開為三個秩 1 楔形的加法」。讀者看到：

- **第 1 個楔形** 來自 $L$ 的第 1 列 × $U$ 的第 1 行 — 整個矩陣都有貢獻（因 $\mathbf{l}_1, \mathbf{u}^*_1$ 全非零）；
- **第 2 個楔形** 來自 $L$ 的第 2 列 × $U$ 的第 2 行 — 因 $L_{12} = 0, U_{21} = 0$，第 1 行 / 列為零，貢獻集中於右下 2×2；
- **第 3 個楔形** 來自 $L$ 的第 3 列 × $U$ 的第 3 行 — 因前兩元素都為 0，只剩右下 1×1 的「主元 $u_{33}$ 自己」。

**「逐層內縮」的視覺意義：** $L, U$ 的三角結構**強制**了每個秩 1 矩陣的「非零範圍向右下角縮小」。這是「**結構驅動的稀疏化**」— 與 §5 (P3)(P4) 的「對角矩陣 sandwich」類似（三角矩陣是 sandwich 的「**單側版**」）。

**為什麼 `using MM4` 標籤這麼關鍵？** 它把「LU 看似神秘的數值算法」**還原**到「§4 教過的最直接矩陣乘法視角」— **沒有新概念**，只是 (MM4) 套到三角結構上。讀者學過 §4 (MM4) 後，LU2 立刻可以「秒懂」，無需重新建立心智模型。**這是原書「五大分解都用 (MM4) 統一視角」的設計核心**。

##### 視覺化機會（VizMark 引用）

LU2 主要由 VizMark-01 涵蓋（與 LU1 共用對偶切換）。

> 🎬 **VizMark-01** [LU 雙視角切換]（同 LU1，含 MM4 重組模式）
> **詳見劇本：** VizScript-01（章末）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: LU 雙視角切換 + 三色 rank 1 peeling 動畫（LU Toggle Animation）

**Tier：** ⭐⭐⭐ Tier 2（含 peeling/MM4 雙模式切換 + 三色秩 1 累加動畫；MM4 模式單 pointer 指 ch04 VizScript-02）
**對應 VizMark：** Figure 6.3 VizMark-01、Figure 6.4 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 1 session + 互動邏輯與高斯消去計算 1 session）

##### A. 一句話定位

「給一個方陣 $A$，動態展示 $LU$ 分解的兩個視角 — peeling（從 $A$ 剝下三個秩 1 楔形）/ MM4（從 $L, U$ 累加成 $A$）— 並切換兩者，視覺驗證 $A = LU = \sum_p \mathbf{l}_p \mathbf{u}^*_p$。」

##### B. 學習目標（Learning Outcome）

- **peeling 遞迴直覺：** 看到一個方陣，能想像它「逐層剝下秩 1 楔形」的過程，把高斯消去從口訣化為視覺；
- **MM4 累加直覺：** 看到 $L, U$，能立刻看出「列 × 行外積之和」結構，**LU 是 (MM4) 的三角特例**；
- **雙視角切換：** 透過 peeling 模式和 MM4 模式的對偶呈現，建立「**解構 = 重組的反向操作**」的反射弧；
- **跨章連結：** 點 (MM4) 按鈕跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 看一般化的秩 1 累加（不限三角）。

##### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $n \times n$ 格子網格，$n \in [2, 5]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$（書中範例，無需換行，主元 $2, 1, 2$）；
  - 範例 2：$\bigl[\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr]$（最小 2×2 範例）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&1&1\\1&2&3\\1&3&6\end{smallmatrix}\bigr]$（Pascal 矩陣，全主元 = 1）；
  - 範例 4：$\bigl[\begin{smallmatrix}2&4&2\\1&3&5\\3&5&7\end{smallmatrix}\bigr]$（中等大小，主元混合正負）；
  - 範例 5：$\bigl[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr]$（**陷阱題**：主元 = 0，需要換行，顯示「LU 失敗 → 改用 PA = LU」提示）；
- **視角切換 (radio)：** `peeling 視角 (LU1)` / `MM4 重組視角 (LU2)` / `同時看兩者（並排）`；
- **掃描速度滑桿：** 自動 peeling / 累加動畫的速度（0.5×–4×）；
- **跳轉按鈕：**
  - 「→ (MM4) 一般秩 1 累加」按鈕（跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)，自動載入 $(\mathbf{l}_p, \mathbf{u}^*_p)$ 序列當作 $(\mathbf{a}_p, \mathbf{b}^*_p)$）；
  - 「→ 解方程 demo」按鈕（跳本章 VizScript-02 的「前代 + 後代」流程）。

##### D. 視覺布局（Layout）

**主畫面三區（並排視角時）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $A$ 的格子輸入網格 + 預設範例選擇器 + 滑桿 |
| 中區（peeling 視角 LU1） | $A$（灰格）$= \mathbf{l}_1 \mathbf{u}^*_1 + \cdots + \mathbf{l}_n \mathbf{u}^*_n$，逐項剝下動畫 + 子矩陣 $A_2, A_3$ 在右下角浮現 + 最終 $L, U$ 在右側 |
| 右區（MM4 重組視角 LU2） | $L \cdot U =$ 三個秩 1 楔形相加，逐項累加動畫；底部 `using MM4` 圖示（圓圈標）+ 跳轉按鈕指 ch04 VizScript-02 |

**底部資訊條：**

- $n$ = 當前矩陣大小；
- $L$ 和 $U$ 的形狀（$n \times n$ × $n \times n$）；
- 每個主元 $u_{pp}$ 顯示（大字）+ 是否為零（紅警示）；
- 「**換行警示**」：若某主元為 0，顯示「需要 PA = LU，本動畫先跳過」（範例 5 陷阱題使用）。

##### E. 動畫腳本（Storyboard）

**Step 1（0–600ms）：** $A$ 的格子網格從左區滑入中區，每格元素淡入。

**Step 2（600–1200ms）：** **第 1 個 peeling**：
- 第 1 列高亮綠 → 主元 $a_{11}$ 高亮金 → 第 1 列除以主元變成 $\mathbf{l}_1$（綠色直條浮出，移到右側 $L$ 的第 1 列位置）；
- 第 1 行高亮粉紅 → 變成 $\mathbf{u}^*_1$（粉紅橫條浮出，移到右側 $U$ 的第 1 行位置）；
- 楔形 1 ($\mathbf{l}_1 \mathbf{u}^*_1$) 出現在中區「楔形堆疊」位置（外層楔形）；
- $A$ 減去楔形 1，第 1 行 / 列清零（變灰），右下角 $(n-1) \times (n-1)$ 子矩陣 $A_2$ 浮現（藍色高亮邊框）。

**Step 3（1200–1800ms）：** **第 2 個 peeling**：對 $A_2$ 重複上述，得 $\mathbf{l}_2, \mathbf{u}^*_2$，楔形 2 加入堆疊（內縮楔形）。

**Step 4（1800–2400ms）：** **第 3 個 peeling**：對 $A_3$ 重複，得 $\mathbf{l}_n, \mathbf{u}^*_n$，楔形 $n$ 加入堆疊（最內楔形）。

**Step 5（2400–3000ms）：** 完成。$A$ 全變灰（已被剝光）、$L, U$ 在右側完整顯示、中區堆疊三個楔形排列「外→中→內」。

**Step 6（可選，按 MM4 視角切換）：** 切到右區的 MM4 重組視角：
- $L, U$ 從中區複製到右區左上；
- 每個 $\mathbf{l}_p \mathbf{u}^*_p$ 楔形從左下「飛入」累加區（外積動畫）；
- 累加區的灰色 $A$ 逐步「充實」（每加一項變亮一些）；
- 最終 $A$ 完全顯示，與中區的 $A$ 並排（驗證一致）；
- 底部 `using MM4` 標籤淡入 + 「→ ch04 VizScript-02」按鈕高亮。

**Step 7（按「解方程」按鈕）：** 跳到 VizScript-02 流程。

##### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $L$ 的列 $\mathbf{l}_p$ / 楔形左側綠條 / 主元周邊的綠輔助線；
- **粉紅 `#d62728`：** $U$ 的行 $\mathbf{u}^*_p$ / 楔形頂端粉紅條 / 主元周邊的粉紅輔助線；
- **金 `#FFD700`（新增）：** 主元 $u_{pp}$ 高亮（即將被剝離的位置）；
- **藍 `#1f77b4`：** $A_p$ 子矩陣的邊框 / 解方程模式下 $\mathbf{b}$ 向量的元素；
- **灰 `#cccccc`：** 已被剝離的元素（變淡）；
- **紫 `#9467bd`：** 換行警示（當主元 = 0 時）。

##### G. 計算邏輯（Numerical Backend）

```python
def lu_factorization_peeling(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[np.ndarray]]:
    """Return L, U, and the list of intermediate A_p matrices and rank-1 wedges."""
    n = A.shape[0]
    A_p = A.astype(float).copy()
    L = np.eye(n)
    U = np.zeros((n, n))
    wedges = []
    A_history = [A_p.copy()]
    for p in range(n):
        pivot = A_p[p, p]
        if abs(pivot) < 1e-12:
            raise ValueError(f"Pivot zero at row {p}, need PA = LU")
        u_p = A_p[p, :].copy()       # u^*_p
        l_p = A_p[:, p] / pivot       # l_p, with l_p[p] = 1
        wedge = np.outer(l_p, u_p)    # rank-1 wedge
        wedges.append(wedge)
        L[:, p] = l_p
        U[p, :] = u_p
        A_p = A_p - wedge
        A_history.append(A_p.copy())
    return L, U, wedges, A_history
```

**驗證：** $\sum_p \text{wedges}[p] = A$（與 LU2 視角）；$L \cdot U = A$（與 LU1 結果）。

##### H. 跨章 pointer 邏輯

- **「→ (MM4) 秩 1 累加」按鈕（MM4 重組模式可見）：**
  - 點擊 → 跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)；
  - 自動把當前 $(\mathbf{l}_p, \mathbf{u}^*_p)$ 序列載入為 ch04 的 $(\mathbf{a}_p, \mathbf{b}^*_p)$ 序列；
  - ch04 動畫自動進入「3 項累加」模式並對齊本章的 peeling 順序。

- **「→ 解方程 demo」按鈕（peeling 模式可見）：**
  - 點擊 → 進入本章 VizScript-02 的「前代 + 後代」流程；
  - 自動帶入當前 $L, U$ + 預設 $\mathbf{b} = (1, 5, 17)^{\mathrm{T}}$。

##### I. UI 元件清單（Component Inventory）

| 元件 | 類型 | 預期實作 |
|---|---|---|
| 矩陣格子網格 | grid input | $n \times n$ 個 `<input type="number">`，autocomplete 整數 |
| 預設範例下拉 | select | 5 個範例 |
| 視角 radio | radio group | 3 選項（peeling / MM4 / 並排）|
| 動畫速度滑桿 | range | 0.5–4.0，step 0.25 |
| 跳轉按鈕 | button | 2 個（→ ch04、→ 解方程）|
| 主元高亮指示 | label | 顯示當前主元值 + 換行警示 |
| 楔形堆疊 | layered SVG | 3 層 SVG 楔形依序疊加 |
| $L, U$ 結構顯示 | 2 個小矩陣框 | 綠列 / 粉紅行排列 |

##### J. 教學文案（Voiceover / Caption Script）

- **開場：** 「$A = LU$ 把方陣拆成下三角 $L$ 乘上三角 $U$。但**這是怎麼來的**？答案是『**逐層剝下秩 1 楔形**』。」
- **第 1 次 peeling：** 「取 $A$ 的第 1 列除以主元 $a_{11}$，得 $\mathbf{l}_1$；取第 1 行直接成 $\mathbf{u}^*_1$。兩者外積 $\mathbf{l}_1 \mathbf{u}^*_1$ 是『**外層楔形**』。從 $A$ 減去這個楔形，剩下的就是小一號的子矩陣 $A_2$。」
- **遞迴：** 「對 $A_2$ 重複同樣動作，得 $\mathbf{l}_2, \mathbf{u}^*_2$ 和『**內縮楔形**』。再對 $A_3$ 重複……直到剝光。」
- **MM4 切換：** 「現在從另一個方向看：把 $L$ 的每列 × $U$ 的對應行相加，剛好還原 $A$。**這就是 §4 (MM4) 教過的『列 × 行外積之和』** — 圖右下角 `using MM4` 標籤就是在點明這件事。」
- **總結：** 「LU 分解的兩個視角 — peeling（解構）和 MM4（重組）— 是同一件事的兩個方向。**這是高斯消去的視覺化本質**。」

##### K. 退化案例 + 邊界處理（Edge Cases）

- **主元為零：** 顯示紅色警示「需要換行 (PA = LU)，本動畫只示範可直接分解的情形」，提供「換到範例 1」按鈕；
- **數值不穩定：** 當主元 $|u_{pp}| < 10^{-6}$ 顯示橙色警示「主元接近零，數值不穩，建議換行」；
- **退化矩陣（rank < n）：** $LU$ 仍可能存在（某些 $\mathbf{l}_p \mathbf{u}^*_p$ 為全零項），動畫顯示對應的楔形「淡出/消失」效果；
- **$n = 2$ 最小情形：** 只有兩次 peeling，動畫節奏加快（每步 500ms）；
- **大型矩陣（$n > 5$）：** 不開放（避免畫面塞）；S12+ 可考慮 $n = 6, 7$ 但需 scrolling。

##### L. 學習評量提示（Assessment Hooks）

互動結束時提供「**理解檢核**」：

1. **概念題：** 「如果 $A$ 的第 1 列除了 $a_{11}$ 全為 0，第 1 個楔形 $\mathbf{l}_1 \mathbf{u}^*_1$ 會長什麼樣？」（答：只有第 1 行有色，因 $\mathbf{l}_1 = (1, 0, 0)^{\mathrm{T}}$，外積只取出 $\mathbf{u}^*_1$ 的第 1 行）；
2. **計算題：** 「給 $L = \bigl[\begin{smallmatrix}1&0\\3&1\end{smallmatrix}\bigr], U = \bigl[\begin{smallmatrix}2&5\\0&7\end{smallmatrix}\bigr]$，畫出兩個秩 1 楔形並驗證相加 = $LU$。」
3. **遞迴題：** 「為什麼 peeling 的子矩陣 $A_{p+1}$ 的左上角 $p \times p$ 必為零？」（答：被前 $p$ 個楔形「完全覆蓋」並減去）；
4. **跨章連結題：** 「點 → ch04 VizScript-02 按鈕，把當前 $\mathbf{l}_p, \mathbf{u}^*_p$ 序列看成自由列向量 / 行向量，動畫應該還原 $A$。**這個一致性說明什麼？**」（答：(MM4) 是 LU 的母模板，LU 只是 (MM4) 的三角特化）。

##### M. 實作里程碑（Milestones for S12+）

1. **M1（第 1 session）：** 畫面框架（左/中/右三區 + 預設範例選擇 + radio）；
2. **M2：** Peeling 動畫（單視角 LU1）— 三步剝皮 + 子矩陣浮現；
3. **M3：** MM4 重組動畫（單視角 LU2）— 三步秩 1 累加；
4. **M4（第 2 session）：** 雙視角並排 + 同步控制 + 速度滑桿；
5. **M5：** 跨章 pointer 整合（→ ch04 VizScript-02 + → 解方程 demo）；
6. **M6：** 邊界處理（主元為零警示 + 退化情形）；
7. **M7：** 教學文案 + 評量檢核 + 5 個預設範例驗證；
8. **M8：** Demo 部署 + 嵌入 ch06c-LU.md。

---

#### VizScript-02: 高斯消去步驟 + 解 $A\mathbf{x} = \mathbf{b}$（精簡）

**Tier：** ⭐⭐ Tier 1 精簡（不含對偶切換，只展示前代 + 後代流程）
**對應 VizMark：** Figure 6.3 VizMark-02
**預估實作工作量：** S12+ 約 1 session

##### A. 一句話定位

「給定 $L, U, \mathbf{b}$，動畫展示『前代解 $L\mathbf{c} = \mathbf{b}$ → 後代解 $U\mathbf{x} = \mathbf{c}$』，並驗證 $A\mathbf{x} = \mathbf{b}$。」

##### B–D. 互動 + 布局

- **輸入：** $L, U$ 從 VizScript-01 帶入（或手動輸入 / 預設範例）+ $\mathbf{b}$ 列向量輸入（$n$ 個元素 $\in [-20, 20]$）；
- **布局：** 上半部「前代區」（$L \cdot \mathbf{c} = \mathbf{b}$ 三角方程組）+ 下半部「後代區」（$U \cdot \mathbf{x} = \mathbf{c}$ 三角方程組）。

##### E. 動畫腳本

**Step 1（前代）：** 從第 1 行往下，依序計算 $c_1, c_2, \ldots, c_n$：
- $c_1 = b_1$（直接讀）；
- $c_2 = b_2 - L_{21} c_1$（高亮 $L_{21}$ 和 $c_1$ 的乘積，從 $b_2$ 減去）；
- $c_3 = b_3 - L_{31} c_1 - L_{32} c_2$（更長的減法鏈）；
- ...
- 每步顯示具體數字計算過程 + 結果 $c_p$ 填入右側 $\mathbf{c}$ 向量。

**Step 2（後代）：** 從第 $n$ 行往上，依序計算 $x_n, x_{n-1}, \ldots, x_1$：
- $x_n = c_n / u_{nn}$（高亮主元 $u_{nn}$）；
- $x_{n-1} = (c_{n-1} - u_{n-1, n} x_n) / u_{n-1, n-1}$；
- ...
- 每步顯示具體計算 + 結果填入右側 $\mathbf{x}$ 向量。

**Step 3（驗證）：** 計算 $A\mathbf{x}$ 並與 $\mathbf{b}$ 並排顯示「✓ 相等」。

##### F–G. 配色 + 計算邏輯

配色同 VizScript-01。

```python
def forward_substitution(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = L.shape[0]
    c = np.zeros(n)
    for i in range(n):
        c[i] = b[i] - L[i, :i] @ c[:i]
    return c

def back_substitution(U: np.ndarray, c: np.ndarray) -> np.ndarray:
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - U[i, i+1:] @ x[i+1:]) / U[i, i]
    return x
```

##### H–M. 其餘段落

精簡版只保留核心動畫 + 1 個範例（$\mathbf{b} = (1, 5, 17)^{\mathrm{T}}$），其餘段落直接複用 VizScript-01 的設定（避免重複）。預估文字 ~500 字，動畫 1.5 分鐘。

---

#### VizScript-03: 3×3 範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1 輕量（單一範例逐步動畫，無互動參數）
**對應 VizMark：** Figure 6.3 VizMark-03
**預估實作工作量：** S12+ 約 0.5 session

##### A. 一句話定位

「對範例 $A = \bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$ 逐步動畫展示 peeling 三步驟，每步顯示具體數字。」

##### B–E. 簡述

- **輸入：** 無（固定範例）；
- **動畫腳本：** 3 段（剝下楔形 1 → 楔形 2 → 楔形 3），每段約 4 秒，總長 12 秒；
- **目標：** 入門用，學生第一次看 LU peeling 時用此 demo 建立直覺，看完後再點 VizScript-01 自由探索。

##### F–M. 其餘段落

配色同 VizScript-01；無互動，純線性動畫；無評量。預估文字 ~300 字。

---

### 小結

- **§6.2 A=LU** 是 §6 五大分解的第二個，數值上最重要（解 $A\mathbf{x} = \mathbf{b}$ 的標準方法）；
- **與 (MM4) 的連結直接顯式：** LU2 圖標 `using MM4`，是 S07 PNG 重核發現的「跨章 pointer 官方鐵證」第二例；
- **三個 VizScript：** ⭐⭐⭐ 雙視角（peeling/MM4）切換 + ⭐⭐ 前代/後代解方程 + ⭐ 範例 walkthrough；
- **下一章 §6.3 A=QR：** 把 LU 的「下三角 $L$」換成「正交 $Q$」，引入 Gram–Schmidt 正交化過程。

---

## 6.3 矩陣分解 3：$A = QR$（Orthogonal × Upper Triangular Factorization）

> **原書頁碼：** p.10–p.11
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.3 $A=QR$（en.md line 379–429 / zh.md line 367–415）
> **本章圖數：** 1（`QR.png`，原書圖中明標 **using P1**）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S08）

---

### 章節摘要

$A = QR$ 是 §6 五大分解的**第三個**，是把 LU 的「下三角 $L$」**升級為正交 $Q$** 的版本。它的核心過程是**格拉姆–施密特正交化**（Gram–Schmidt orthogonalization）：把 $A$ 的**列**（columns）一個一個處理，每一列都「**減去前面已產生的正交列方向**」再單位化，得到正交基底 $\mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n$。

具體流程：

1. **$\mathbf{q}_1$：** 直接把 $\mathbf{a}_1$ 單位化：$\mathbf{q}_1 = \mathbf{a}_1 / \|\mathbf{a}_1\|$；
2. **$\mathbf{q}_2$：** 把 $\mathbf{a}_2$ **減去** $\mathbf{q}_1$ 方向的投影，再單位化：$\mathbf{q}_2 = (\mathbf{a}_2 - (\mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2) \mathbf{q}_1) / \|\cdots\|$；
3. **$\mathbf{q}_3$：** 把 $\mathbf{a}_3$ **減去** $\mathbf{q}_1, \mathbf{q}_2$ 兩個方向的投影，再單位化；
4. ⋯ 重複至所有列處理完。

**反推 $R$：** 上面流程**留下的乘數**（投影係數 $r_{ij} = \mathbf{q}_i^{\mathrm{T}} \mathbf{a}_j$）和「單位化的縮放因子」（$r_{ii} = \|\cdots\|$）整理成**上三角矩陣** $R$，自然滿足 $A = QR$。

**核心不變量：** $Q$ 的列空間 = $A$ 的列空間（$\mathbf{C}(Q) = \mathbf{C}(A)$）— Gram–Schmidt **不改變 $A$ 撐起的空間**，只**重新挑一組正交的基底**來描述同一個空間。這是 QR 與 LU 的關鍵差異：

| 性質 | $A = LU$ | $A = QR$ |
|---|---|---|
| $Q$ 或 $L$ 的特性 | 下三角 | **正交**（$Q^{\mathrm{T}} Q = I$）|
| 另一側 $U$ 或 $R$ | 上三角 + 主元 | 上三角 + Gram–Schmidt 縮放因子 |
| 與 $A$ 的關係 | $L$ 記錄消去步驟 | $Q$ 是 $A$ 的正交化結果 |
| 空間不變量 | 無直接結構 | $\mathbf{C}(A) = \mathbf{C}(Q)$ |
| 主要用途 | 解 $A\mathbf{x} = \mathbf{b}$ | 最小平方法（least squares）/ 求正交基底 |
| `using` 標記 | LU2 標 (MM4)，LU1 無標 | QR 標 **(P1)** |

**`using P1` 標記的意義（S08 PNG 重核發現）：** 原書 `QR.png` 右下角圓圈標 `P1`，明示「QR 圖的視覺視角是 §5 Pattern 1」— **「從右乘上三角矩陣 $R$，等於把 $Q$ 的列做線性組合」**。這跟 §6.1 CR1 的 `using P1` 是同一個 Pattern，**但 QR 多了「Q 列正交」的特殊性質**。

**本章 VizScript 策略：** ⭐⭐⭐ VizScript-01 採**單 pointer 策略** — (P1) 列線性組合動畫 pointer 到 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)；本章獨立寫的是 **Gram–Schmidt 正交化過程動畫 + 3D 投影視覺 + $\mathbf{C}(A) = \mathbf{C}(Q)$ 不變量演示** 等 QR 特有的內容。

數值範例（本章貫穿）：

$$
A = \begin{bmatrix} 1 & 2 \\ 1 & 0 \end{bmatrix}
\;=\;
\underbrace{\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}}_{Q}
\underbrace{\sqrt{2}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}}_{R}
$$

驗證：

1. $\mathbf{a}_1 = (1, 1)^{\mathrm{T}}$，$\|\mathbf{a}_1\| = \sqrt{2}$，$\mathbf{q}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；$r_{11} = \sqrt{2}$；
2. $r_{12} = \mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2 = (2 + 0)/\sqrt{2} = \sqrt{2}$；
3. $\mathbf{w}_2 = \mathbf{a}_2 - r_{12} \mathbf{q}_1 = (2, 0)^{\mathrm{T}} - \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} = (2, 0)^{\mathrm{T}} - (1, 1)^{\mathrm{T}} = (1, -1)^{\mathrm{T}}$；
4. $\|\mathbf{w}_2\| = \sqrt{2}$，$r_{22} = \sqrt{2}$，$\mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
5. 驗證 $Q^{\mathrm{T}} Q = I_2$（兩列正交、單位）+ $QR = A$ ✓。

---

### 數學要點

#### 1. 定義與形狀

$$
A_{m \times n} = Q_{m \times n} \, R_{n \times n}, \qquad Q^{\mathrm{T}} Q = I_n
$$

- **$Q$（Orthogonal columns）：** $m \times n$ 矩陣，**列兩兩正交且單位長**（orthonormal columns）：$\mathbf{q}_i^{\mathrm{T}} \mathbf{q}_j = \delta_{ij}$（$i = j$ 時為 1，否則為 0）。若 $m = n$（方陣），$Q$ 是「正交矩陣」（orthogonal matrix），$Q^{-1} = Q^{\mathrm{T}}$；
- **$R$（Upper triangular）：** $n \times n$ 上三角矩陣，**對角線元素是 Gram–Schmidt 的「縮放因子」** $r_{ii} = \|\mathbf{w}_i\|$（向量單位化前的長度），對角線上方填 $r_{ij} = \mathbf{q}_i^{\mathrm{T}} \mathbf{a}_j$（投影係數）；
- **形狀（thin QR）：** $A$ 是 $m \times n$（通常 $m \geq n$），$Q$ 也是 $m \times n$（與 $A$ 同形）、$R$ 是 $n \times n$；
- **可分解條件：** $A$ 的列必須線性獨立（rank $= n$），否則 Gram–Schmidt 過程中會出現 $\mathbf{w}_p = \mathbf{0}$。

#### 2. Gram–Schmidt 正交化過程（核心 ⭐）

**遞迴公式（正向，從 $\mathbf{a}_p$ 求 $\mathbf{q}_p$）：**

$$
\mathbf{w}_p = \mathbf{a}_p - \sum_{k=1}^{p-1} (\mathbf{q}_k^{\mathrm{T}} \mathbf{a}_p) \mathbf{q}_k, \qquad
\mathbf{q}_p = \frac{\mathbf{w}_p}{\|\mathbf{w}_p\|}
$$

**逐步分解：**

1. **減投影：** $\mathbf{w}_p$ 是 $\mathbf{a}_p$ **減去**它在前 $p-1$ 個 $\mathbf{q}_k$ 方向的投影 — 結果 $\mathbf{w}_p$ 與所有 $\mathbf{q}_1, \ldots, \mathbf{q}_{p-1}$ **正交**；
2. **單位化：** $\mathbf{q}_p = \mathbf{w}_p / \|\mathbf{w}_p\|$ 把 $\mathbf{w}_p$ 縮成單位長度；
3. **記錄縮放：** $r_{pp} = \|\mathbf{w}_p\|$（縮放因子，存入 $R$ 對角線）；
4. **記錄投影係數：** $r_{kp} = \mathbf{q}_k^{\mathrm{T}} \mathbf{a}_p$（$k < p$，存入 $R$ 對角線上方）。

**範例（本章 2×2 範例展開）：**

第 1 列 $\mathbf{a}_1 = (1, 1)^{\mathrm{T}}$：
- $\mathbf{w}_1 = \mathbf{a}_1 = (1, 1)^{\mathrm{T}}$（無投影要減）；
- $r_{11} = \|\mathbf{w}_1\| = \sqrt{2}$；
- $\mathbf{q}_1 = \mathbf{w}_1 / \sqrt{2} = (1, 1)^{\mathrm{T}} / \sqrt{2}$。

第 2 列 $\mathbf{a}_2 = (2, 0)^{\mathrm{T}}$：
- $r_{12} = \mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2 = (1 \cdot 2 + 1 \cdot 0)/\sqrt{2} = 2/\sqrt{2} = \sqrt{2}$；
- $\mathbf{w}_2 = \mathbf{a}_2 - r_{12} \mathbf{q}_1 = (2, 0)^{\mathrm{T}} - \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} = (2, 0)^{\mathrm{T}} - (1, 1)^{\mathrm{T}} = (1, -1)^{\mathrm{T}}$；
- $r_{22} = \|\mathbf{w}_2\| = \sqrt{1 + 1} = \sqrt{2}$；
- $\mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$。

**驗證正交性：**

- $\mathbf{q}_1^{\mathrm{T}} \mathbf{q}_2 = (1 \cdot 1 + 1 \cdot (-1))/2 = 0$ ✓；
- $\|\mathbf{q}_1\| = 1, \|\mathbf{q}_2\| = 1$ ✓。

#### 3. 與 (P1) 視角的連結 — 反向公式：$\mathbf{a}_p = \sum r_{kp} \mathbf{q}_k$（核心 ⭐）

把第 2 節的「正向」流程**反過來**寫，得到 **(P1) 視角的核心公式**：

$$
\mathbf{a}_p = r_{pp} \mathbf{q}_p + \sum_{k=1}^{p-1} r_{kp} \mathbf{q}_k = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k
$$

**展開（本章 2×2 範例）：**

- $\mathbf{a}_1 = r_{11} \mathbf{q}_1 = \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} = (1, 1)^{\mathrm{T}}$ ✓；
- $\mathbf{a}_2 = r_{12} \mathbf{q}_1 + r_{22} \mathbf{q}_2 = \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} + \sqrt{2} \cdot (1, -1)^{\mathrm{T}}/\sqrt{2} = (1, 1)^{\mathrm{T}} + (1, -1)^{\mathrm{T}} = (2, 0)^{\mathrm{T}}$ ✓。

**整理成矩陣等式：**

$$
A = \begin{bmatrix} | & | & & | \\ \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \\ | & | & & | \end{bmatrix}
= \begin{bmatrix} | & | & & | \\ \mathbf{q}_1 & \mathbf{q}_2 & \cdots & \mathbf{q}_n \\ | & | & & | \end{bmatrix}
\begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1n} \\ & r_{22} & \cdots & r_{2n} \\ & & \ddots & \vdots \\ & & & r_{nn} \end{bmatrix} = QR
$$

**對照 §5 (P1)：** 「**右乘任意矩陣 = 左矩陣的列做線性組合**」。

- §5 (P1) 一般形式：$AB$ 的第 $j$ 列 = $A$ 的列的線性組合（係數 = $B$ 的第 $j$ 行）；
- QR 特化：$A$ 的第 $p$ 列 = $Q$ 的列的線性組合（係數 = $R$ 的第 $p$ 行，**只有上面 $p$ 個非零**因為 $R$ 上三角）。

**「using P1」標籤的意涵：** 原書 `QR.png` 標 `using P1`，直接點明「QR 圖就是 (P1) 在『$R$ 上三角』情形下的應用」。**這比 CR 的 (P1) 標記更精細** — CR 的 $R$ 是「RREF 不一定上三角」，QR 的 $R$ **強制上三角**，使得「$\mathbf{a}_p$ 只用 $\mathbf{q}_1, \ldots, \mathbf{q}_p$（前 $p$ 個）來組成」這個視覺特徵更強烈。

#### 4. 不變量：$\mathbf{C}(A) = \mathbf{C}(Q)$（列空間相等）

**核心定理：** Gram–Schmidt 過程**不改變 $A$ 的列空間**，只重新選一組正交基底：

$$
\mathbf{C}(A) = \operatorname{span}\{\mathbf{a}_1, \ldots, \mathbf{a}_n\}
= \operatorname{span}\{\mathbf{q}_1, \ldots, \mathbf{q}_n\} = \mathbf{C}(Q)
$$

**證明（雙向包含）：**

- **$\mathbf{C}(Q) \subseteq \mathbf{C}(A)$：** 從 Gram–Schmidt 流程看，$\mathbf{q}_p$ 是 $\mathbf{a}_1, \ldots, \mathbf{a}_p$ 的線性組合（減投影 + 縮放），所以每個 $\mathbf{q}_p$ 都在 $\mathbf{C}(A)$ 中；
- **$\mathbf{C}(A) \subseteq \mathbf{C}(Q)$：** 從反向公式 $\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k$ 看，每個 $\mathbf{a}_p$ 都在 $\mathbf{C}(Q)$ 中。

**結論：** 兩集合**互相包含 → 相等**。**這個不變量是 QR 在「最小平方法」中發揮作用的關鍵** — 因為「最小平方法 = 投影到 $\mathbf{C}(A)$」，而 $\mathbf{C}(A) = \mathbf{C}(Q)$，所以可以用「投影到正交基底 $Q$ 的列」來替代複雜的「投影到一般列 $A$」。

#### 5. QR 在「最小平方法（Least Squares）」中的應用

**問題：** 解 $A\mathbf{x} = \mathbf{b}$，但 $A$ 是「**長方** $m \times n, m > n$」（方程個數 > 未知數個數，通常無解），求**最佳近似** $\hat{\mathbf{x}}$ 使 $\|A\mathbf{x} - \mathbf{b}\|^2$ 最小。

**經典解法（正規方程）：** $A^{\mathrm{T}} A \hat{\mathbf{x}} = A^{\mathrm{T}} \mathbf{b}$，**但** $A^{\mathrm{T}} A$ 可能病態（ill-conditioned）。

**QR 解法：** 用 $A = QR$ 代入：

$$
A^{\mathrm{T}} A \hat{\mathbf{x}} = A^{\mathrm{T}} \mathbf{b}
\;\Longleftrightarrow\; R^{\mathrm{T}} Q^{\mathrm{T}} Q R \hat{\mathbf{x}} = R^{\mathrm{T}} Q^{\mathrm{T}} \mathbf{b}
\;\Longleftrightarrow\; R^{\mathrm{T}} R \hat{\mathbf{x}} = R^{\mathrm{T}} Q^{\mathrm{T}} \mathbf{b}
\;\Longleftrightarrow\; R \hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}
$$

（利用 $Q^{\mathrm{T}} Q = I$，並消去 $R^{\mathrm{T}}$ 後得「$R$ 上三角方程」。）

**結果：** 解 $R \hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$ — **單一三角方程**（後代法 $O(n^2)$），且**數值穩定**（避開了 $A^{\mathrm{T}} A$ 的病態）。

**這是 QR 在工程實務（迴歸分析、訊號處理、機器學習）中最常見的應用情境。**

#### 6. $A = QR$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **QR ↔ CR** | QR 是「**正交化過的 CR**」— 把 $C$ 變正交 $Q$（Gram–Schmidt），把 $R$ 從 RREF 換成上三角 |
| **QR ↔ LU** | QR 把 LU 的「下三角 $L$」**升級為正交 $Q$**（保留上三角 $R$）。**從 LU 到 QR = 把 $L$ 正交化** |
| **QR ↔ QΛQᵀ** | QΛQᵀ 限對稱 $S$，$Q$ 是「特徵向量正交基底」；QR 是「列正交基底」（一般矩陣可用）|
| **QR ↔ SVD** | SVD 是「**雙側正交化**」— 把 QR 的左側 $Q$ 保留為 $U$，把右側 $R$ 也正交化得 $V^{\mathrm{T}}$，中間插一個對角 $\Sigma$。**從 QR 到 SVD = 把 $R$ 也正交化** |

**結論：** $A = QR$ 是「**單側正交化**」分解 — 左側 $Q$ 強制正交，右側 $R$ 保留上三角。沿著「正交化逐步加強」的階梯看：

$$
\underbrace{CR}_{\text{0 側正交}} \;\to\; \underbrace{LU}_{\text{0 側正交 + 三角結構}} \;\to\; \underbrace{QR}_{\text{1 側正交 + 三角結構}} \;\to\; \underbrace{U\Sigma V^{\mathrm{T}}}_{\text{2 側正交 + 對角結構}}
$$

**這是原書「五大分解升級鏈」的核心軸 — QR 在中間扮演「**從三角到正交**」的橋梁角色**。

#### 7. 數學要點總結（一張表）

| 性質 | $A = QR$ 的對應 |
|---|---|
| 適用矩陣 | $A_{m \times n}$，列線性獨立（rank $= n$）；通常 $m \geq n$ |
| $Q$ 的結構 | $m \times n$，列兩兩正交 + 單位長（$Q^{\mathrm{T}} Q = I_n$）|
| $R$ 的結構 | $n \times n$ 上三角，對角線 = Gram–Schmidt 縮放因子，上方 = 投影係數 |
| 項數 | $n$（與 $A$ 的列數同）|
| 構造方法 | Gram–Schmidt（正向）或 Householder/Givens（更穩定的數值版本）|
| §4 (MM4) 對應 | $A = \sum_p r_{pp} \mathbf{q}_p \mathbf{e}^{\mathrm{T}}_p + (\text{投影修正項})$ 不直接是 (MM4) 形式 |
| §5 Pattern 對應 | **`QR.png` 標 `using P1`**：(P1) 列線性組合的「$R$ 上三角」特化 |
| 列空間不變量 | $\mathbf{C}(A) = \mathbf{C}(Q)$（Gram–Schmidt 不改變列空間，只換正交基底）|
| 求最小平方法 | $R \hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$（單一三角方程，數值穩定）|
| 計算量 | Gram–Schmidt $O(mn^2)$；Householder 略快且更穩定 |

---

### 圖片詳細描述（Figure Descriptions）

#### Figure 6.5: $A = QR$ — 標 using P1

**圖檔：** `docs/book/figs-png/QR.png`（原始 EPS：`figs/QR.eps`）
**原書頁碼：** p.10 圖 15
**所屬章節：** §6.3 $A = QR$（**唯一一張**，無對偶圖）
**圖中標記：** **`using P1`**（圓圈標，右下角）

##### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，共 9 段（與 §6.1 CR 不同，QR 只有一張圖整合所有資訊）：

1. **第 1 段：** 矩陣 $A$ 的方框（內含 **3 條等寬灰色直立列**）— 上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $Q$（方框內 **3 條等寬綠色直立列，每列頂部標 `1`/`2`/`3`**）— 上方有大字 `Q`；綠色色塊代表「**正交且單位長**」的視覺信號；
4. **第 4 段：** 矩陣 $R$（方框內 **6 個藍色圓點以「上三角」形狀排列**：上排 3 點、中排 2 點、下排 1 點）— 上方有大字 `R`；**藍點明示「$R$ 是上三角，左下三角區域全為零」**；
5. **第 5 段：** 等號 `=`；
6. **第 6–8 段：** 拆解結果，3 個直立列方框並排，**從左到右逐漸變寬（容納更多綠列疊加）**：
   - 第 6 段（$\mathbf{a}_1$ 拆解）：**1 條綠色直立列** + 上方藍點 `1`（代表 $r_{11}$）+ 內側標 `1` → $\mathbf{a}_1 = r_{11} \mathbf{q}_1$；
   - 第 7 段（$\mathbf{a}_2$ 拆解）：**2 條綠色直立列**（綠1 + 綠2）+ 上方兩個藍點 `1`、`2`（代表 $r_{12}$、$r_{22}$）+ 加號 `+` → $\mathbf{a}_2 = r_{12} \mathbf{q}_1 + r_{22} \mathbf{q}_2$；
   - 第 8 段（$\mathbf{a}_3$ 拆解）：**3 條綠色直立列**（綠1 + 綠2 + 綠3）+ 上方三個藍點 `1`、`2`、`3`（代表 $r_{13}$、$r_{23}$、$r_{33}$）+ 兩個加號 → $\mathbf{a}_3 = r_{13} \mathbf{q}_1 + r_{23} \mathbf{q}_2 + r_{33} \mathbf{q}_3$；
9. **右下角圖示：** 圓圈內標 `P1`，文字 `using` — **直接標明「本圖用 §5 Pattern 1 視角」**。

**「逐漸變寬」的視覺意義：** 每一列 $\mathbf{a}_p$ 用「前 $p$ 個」$\mathbf{q}_k$ 來組成，**$p$ 增加 → 用到的 $\mathbf{q}$ 越多 → 列拆解越寬**。這直接對應「$R$ 是上三角，第 $p$ 行的非零元素只到第 $p$ 個位置」的數學結構。

**閱讀順序：** 由左到右讀整個等式鏈 `A = Q R = (三個列拆解，逐漸變寬)`。重點掃右側的 3 個拆解列，注意「**綠列數量遞增 + 藍點位置呈上三角分布**」。

##### 數學內容 (Mathematical Content)

對應數學表示（**(P1) Pattern 1** 列視角，$R$ 上三角特化版）：

$$
A = QR = \begin{bmatrix} | & | & | \\ \mathbf{q}_1 & \mathbf{q}_2 & \mathbf{q}_3 \\ | & | & | \end{bmatrix}
\begin{bmatrix} r_{11} & r_{12} & r_{13} \\ & r_{22} & r_{23} \\ & & r_{33} \end{bmatrix}
$$

第 $p$ 列展開（**(P1) Pattern 1 的上三角特化**）：

$$
\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k
$$

具體：

- $\mathbf{a}_1 = r_{11} \mathbf{q}_1$（只用 $\mathbf{q}_1$，1 項）；
- $\mathbf{a}_2 = r_{12} \mathbf{q}_1 + r_{22} \mathbf{q}_2$（用 $\mathbf{q}_1, \mathbf{q}_2$，2 項）；
- $\mathbf{a}_3 = r_{13} \mathbf{q}_1 + r_{23} \mathbf{q}_2 + r_{33} \mathbf{q}_3$（用 $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$，3 項）。

**正交性副產品：** 因為 $\mathbf{q}_k$ 正交，**從 $A$ 提取係數 $r_{kp}$ 變得非常簡單**：

$$
r_{kp} = \mathbf{q}_k^{\mathrm{T}} \mathbf{a}_p
$$

（投影到 $\mathbf{q}_k$ 方向就是內積。）這與 CR / LU 不同 — CR 的 $R$ 要解 RREF、LU 的 $L$ 要消去 — 但 QR 的 $R$ **直接內積即可**，這是「正交基底」帶來的計算簡化。

##### 直覺解讀 (Intuition)

QR 圖傳達三層核心訊息：

1. **正交基底的「綠色直立列」隱喻：** $Q$ 的 3 條綠色直立列**等寬且等高**，視覺上強調「**長度都是 1 + 兩兩垂直**」。這跟 LU 的 $L$（綠列從高到低，視覺上「降階」）形成對比 — QR 的 $Q$ 是「**整齊的正交基底**」，LU 的 $L$ 是「**有序的三角結構**」；

2. **上三角 $R$ 的「藍點階梯」：** $R$ 的 6 個藍點呈上三角分布（上排 3 點、中排 2 點、下排 1 點），**視覺上明示「對角線 + 上三角區域才有值，左下三角全為零」**。這個視覺信號讓讀者立刻看出 $R$ 的稀疏結構；

3. **「列拆解逐漸變寬」的本質：** 第 $p$ 個拆解列用 $p$ 個綠列疊加，**直觀對應「Gram–Schmidt 過程中第 $p$ 步用到前 $p$ 個 $\mathbf{q}_k$」**。這個視覺序列是 QR 「**逐步擴充正交基底**」過程的最精煉表達。

**「using P1」標籤的重要性（S08 PNG 重核確認）：** 原書作者刻意把這張圖標 `using P1`，與 §6.1 CR1 同款 — 等於明說「**QR 圖跟 CR1 圖是同一種視角（(P1) 列線性組合），只是 $R$ 換成上三角**」。視覺化可以**直接重用 ch05 VizScript-01 的對角矩陣互動**（把對角換成上三角），或重用 ch06b VizScript-01 的 CR 互動（把 $R$ 限定為上三角）。

**為什麼這張圖該做成互動視覺化？** 因為 QR 的核心過程「**Gram–Schmidt 正交化**」是「**動態的逐步過程**」 — 用戶調 $A$ 看每一列如何「**減投影 → 單位化**」變成 $\mathbf{q}_p$，在 3D 空間中可以**清楚看到向量「重新指向正交方向」**的幾何意義。靜態圖只能展示最終結果，**互動 demo 可以展示中間每一步**，這是 QR 教學的關鍵突破點（見 VizMark-01）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [Gram–Schmidt 正交化動畫 + P1 列拆解] ⭐⭐⭐
> 「拉桿調 $A$ 的元素 → 逐步動畫 Gram–Schmidt 三步驟（減投影 → 單位化 → 記錄到 $R$）→ 3D 視窗看 $\mathbf{q}_p$ 如何指向正交方向 → 同步顯示 $Q, R$ 結構」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [3D 投影視覺] ⭐⭐
> 「3D 視窗中展示 $\mathbf{a}_p$ 投影到子空間 $\operatorname{span}\{\mathbf{q}_1, \ldots, \mathbf{q}_{p-1}\}$ + 減投影得 $\mathbf{w}_p$ + 單位化得 $\mathbf{q}_p$」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [QR 數值範例] ⭐
> 「用 2×2 範例 $A = \bigl[\begin{smallmatrix}1&2\\1&0\end{smallmatrix}\bigr]$ 一步一步動畫展示計算過程，每步顯示具體數字 + $r_{ij}$ 填入 $R$」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: Gram–Schmidt 正交化 + P1 列拆解動畫（QR Gram–Schmidt Animation）

**Tier：** ⭐⭐⭐ Tier 2（含 Gram–Schmidt 逐步動畫 + 3D 投影視覺 + P1 列拆解；單 pointer 指 ch05 VizScript-01）
**對應 VizMark：** Figure 6.5 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 + Gram–Schmidt 1 session + 3D 投影 1 session）

##### A. 一句話定位

「給一個 $A$（$m \times n$，$n \leq m$），動態展示 Gram–Schmidt 正交化過程 — 每一列減投影 / 單位化 / 記錄到 $R$ — 並用 3D 視窗看 $\mathbf{q}_p$ 如何指向正交方向，視覺驗證 $A = QR$ 且 $\mathbf{C}(A) = \mathbf{C}(Q)$。」

##### B. 學習目標（Learning Outcome）

- **Gram–Schmidt 流程直覺：** 看到一個矩陣，能在腦中跑「減投影 → 單位化」三步驟，**手算 Gram–Schmidt**；
- **正交性的幾何意義：** 透過 3D 視窗看到 $\mathbf{q}_p$ 與前 $\mathbf{q}_k$ 都**垂直**，建立「正交 = 各自獨立 = 投影為零」的直覺；
- **列空間不變量：** 動態切換「$A$ 的列」和「$Q$ 的列」，看到它們**撐起的子空間相同**（同一個 3D 平面 / 直線）；
- **(P1) 上三角特化：** 從反向公式看 $\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k$，理解「$R$ 上三角 → $\mathbf{a}_p$ 只用前 $p$ 個 $\mathbf{q}$」；
- **跨章連結：** 點 (P1) 按鈕跳 ch05 VizScript-01 看對角矩陣特例（理解 QR 是 (P1) 的「上三角版」）。

##### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $m \times n$ 格子網格，$m \in [2, 4]$、$n \in [2, m]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}1&2\\1&0\end{smallmatrix}\bigr]$（書中 2×2 範例，正方形）；
  - 範例 2：$\bigl[\begin{smallmatrix}1&1&0\\0&1&1\\1&0&1\end{smallmatrix}\bigr]$（3×3 含正交化的中等難度）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&0&0\\0&1&0\\0&0&1\end{smallmatrix}\bigr]$（單位矩陣，$Q = I, R = I$ 不變特例）；
  - 範例 4：$\bigl[\begin{smallmatrix}1&2&3\\0&4&5\\0&0&6\end{smallmatrix}\bigr]$（**已是上三角**，$Q = I, R = A$ 特例）；
  - 範例 5：$\bigl[\begin{smallmatrix}1&2&3\\1&2&3\\1&2&3\end{smallmatrix}\bigr]$（**退化** rank = 1，第 2、3 列正交化會得 $\mathbf{w}_p = \mathbf{0}$，顯示失敗警示）；
- **動畫模式切換 (radio)：** `分步動畫（手動下一步）` / `自動播放` / `對比 $A$ vs $Q$ 兩個基底`；
- **3D 視窗開關 (checkbox)：** 開啟後右側額外顯示 3D 視窗（僅當 $m \leq 3$ 可用）；
- **跳轉按鈕：**
  - 「→ (P1) 對角矩陣特例」按鈕（跳 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)，自動把 $R$ 換成對角矩陣）；
  - 「→ 最小平方法 demo」按鈕（跳到附加流程，用 $R\hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$ 解最小平方）。

##### D. 視覺布局（Layout）

**主畫面三區（標準模式）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $A$ 的格子輸入網格 + 預設範例選擇器 + radio + 滑桿 |
| 中區（Gram–Schmidt 動畫） | $A, Q, R$ 三矩陣並排 + 當前正在處理的列高亮（金色框）+ 投影 / 減 / 單位化 / 記錄 4 步驟說明文字 |
| 右區（3D 視窗，可選） | 3D 座標系中顯示 $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ (灰色 + 灰平面) 和 $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$ (綠色 + 綠平面) 並排，標出投影向量（虛線）|

**底部資訊條：**

- 當前正在處理的 $p$（大字顯示）；
- 當前的 $\mathbf{w}_p, r_{kp}, \mathbf{q}_p$ 數值（小字顯示）；
- 「**$\mathbf{C}(A) = \mathbf{C}(Q)$ 驗證**」（綠色 ✓ 顯示，hover 顯示計算過程）。

##### E. 動畫腳本（Storyboard）

**Step 1（0–500ms）：** $A$ 的格子網格從左區滑入中區，列 1 高亮金色框。

**Step 2（500–1500ms，第 $p = 1$ 步）：**
- 高亮 $\mathbf{a}_1$（綠色淡背景）；
- 公式區顯示 `r_{11} = ||a_1|| = ...`；
- 計算 $r_{11}$（顯示具體數字），$\mathbf{q}_1 = \mathbf{a}_1 / r_{11}$；
- $\mathbf{q}_1$ 移動到 $Q$ 的第 1 列位置（綠色立柱）；
- $r_{11}$ 填入 $R$ 的 $(1, 1)$ 位置（藍點）；
- 3D 視窗：$\mathbf{a}_1$（灰箭頭）淡入 → 縮放到單位長度成 $\mathbf{q}_1$（綠箭頭）。

**Step 3（1500–3000ms，第 $p = 2$ 步）：**
- 高亮 $\mathbf{a}_2$（黃色淡背景）；
- 公式區顯示 `r_{12} = q_1^T a_2 = ...` → 計算投影係數；
- 計算 $\mathbf{w}_2 = \mathbf{a}_2 - r_{12} \mathbf{q}_1$（顯示具體向量減法）；
- 3D 視窗：$\mathbf{a}_2$（灰箭頭）淡入 → 從 $\mathbf{a}_2$ 拉一條虛線到 $\mathbf{q}_1$ 的投影點（紅色投影箭頭）→ 投影向量「飛走」（從 $\mathbf{a}_2$ 移動到原點）→ 留下 $\mathbf{w}_2$（黃色箭頭，與 $\mathbf{q}_1$ 垂直）；
- 公式區顯示 `r_{22} = ||w_2|| = ...`；
- $\mathbf{q}_2 = \mathbf{w}_2 / r_{22}$，$\mathbf{q}_2$ 移動到 $Q$ 的第 2 列；
- $r_{12}, r_{22}$ 填入 $R$ 的 $(1, 2), (2, 2)$ 位置。

**Step 4（3000–5000ms，第 $p = 3$ 步，若 $n \geq 3$）：**
- 類似 Step 3，但減 2 個投影（$r_{13} \mathbf{q}_1 + r_{23} \mathbf{q}_2$）；
- 3D 視窗：$\mathbf{a}_3$ → 從 $\mathbf{q}_1, \mathbf{q}_2$ 撐起的平面投影 → 減去 → $\mathbf{w}_3$ 與平面垂直 → 單位化得 $\mathbf{q}_3$。

**Step 5（完成，5000–6000ms）：** $Q, R$ 全部填完，顯示 `A = QR` 等式驗證 ✓；
- 3D 視窗：$\{\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3\}$ 三個綠箭頭兩兩垂直 + $A$ 的 $\{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3\}$ 三個灰箭頭撐起同一個 3D 子空間（$\mathbf{C}(A) = \mathbf{C}(Q)$ 視覺證明）。

**Step 6（按「對比」radio）：** 顯示「兩個基底並排」：
- 左半 3D：$A$ 的三個列（灰）撐起的 3D 空間 + 任意紅色測試向量 $\mathbf{v}$ 顯示「用 $A$ 列線組」需要的係數（從正規方程算）；
- 右半 3D：$Q$ 的三個列（綠）撐起同樣的 3D 空間 + 同一個紅色測試向量 $\mathbf{v}$ 顯示「用 $Q$ 列線組」需要的係數（**只是內積，超簡單**）；
- **對比直覺：「同樣的空間，不同的座標系；$Q$ 的座標系正交，計算容易」**。

##### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $\mathbf{q}_p$ / $Q$ 的列 / 3D 視窗中的正交向量；
- **灰 `#cccccc`：** $\mathbf{a}_p$ / $A$ 的列 / 3D 視窗中的原始向量；
- **黃 `#FFD700`：** 當前正在處理的列 / $\mathbf{w}_p$（減投影後的中間結果）；
- **紅 `#d62728`：** 投影向量 $r_{kp} \mathbf{q}_k$（要從 $\mathbf{a}_p$ 減去的部分）；
- **藍 `#1f77b4`：** $R$ 的元素（藍點）/ 3D 視窗座標軸；
- **紫 `#9467bd`：** 失敗 / 退化警示（範例 5 rank 不足）。

##### G. 計算邏輯（Numerical Backend）

```python
def gram_schmidt(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[dict]]:
    """Return Q, R, and step-by-step history for animation."""
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    history = []
    for p in range(n):
        a_p = A[:, p].copy()
        w_p = a_p.copy()
        proj_components = []
        for k in range(p):
            r_kp = Q[:, k] @ a_p
            R[k, p] = r_kp
            proj = r_kp * Q[:, k]
            w_p = w_p - proj
            proj_components.append({"k": k, "r_kp": r_kp, "proj_vector": proj})
        r_pp = np.linalg.norm(w_p)
        if r_pp < 1e-12:
            raise ValueError(f"Column {p} is linearly dependent")
        R[p, p] = r_pp
        Q[:, p] = w_p / r_pp
        history.append({
            "p": p,
            "a_p": a_p, "w_p": w_p, "q_p": Q[:, p].copy(),
            "r_pp": r_pp, "projections": proj_components
        })
    return Q, R, history
```

**驗證：** $Q^{\mathrm{T}} Q = I$ ✓、$QR = A$ ✓、$\mathbf{C}(Q) = \mathbf{C}(A)$（透過 SVD 比對奇異值非零數）。

##### H. 跨章 pointer 邏輯

- **「→ (P1) 對角矩陣特例」按鈕：**
  - 點擊 → 跳 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)；
  - 自動把當前 $Q$ 載入為 ch05 的「左矩陣」，把 $R$ 的對角元素 $r_{ii}$ 載入為對角矩陣 $D$ 的對角元素（**忽略 $R$ 的上三角部分**）；
  - ch05 動畫展示「$Q D$ 是 $Q$ 列被 $r_{ii}$ 縮放的純粹 (P1) 特例」；
  - 對比理解：「QR 是 (P1) 的『上三角加強版』 — 多了『列之間的相互線性組合』」。

- **「→ 最小平方法 demo」按鈕：**
  - 進入附加流程：輸入 $\mathbf{b}$ 列向量 → 動畫展示 $\mathbf{c} = Q^{\mathrm{T}} \mathbf{b}$ → 後代解 $R \hat{\mathbf{x}} = \mathbf{c}$；
  - 顯示「殘差 $\mathbf{r} = \mathbf{b} - A\hat{\mathbf{x}}$」垂直於 $\mathbf{C}(A)$（**正交投影的幾何意義**）。

##### I. UI 元件清單（Component Inventory）

| 元件 | 類型 | 預期實作 |
|---|---|---|
| 矩陣格子網格 | grid input | $m \times n$ 個 `<input type="number">` |
| 預設範例下拉 | select | 5 個範例 |
| 動畫模式 radio | radio group | 3 選項 |
| 3D 視窗開關 | checkbox | 預設關閉（避免初次認知負荷）|
| 動畫速度滑桿 | range | 0.5–4.0 |
| 「下一步」按鈕 | button | 分步動畫模式專用 |
| 跳轉按鈕 | button | 2 個（→ ch05、→ 最小平方）|
| 3D 視窗 | matplotlib 3D / plotly 3D | 600×480 px |
| 公式 LaTeX 區 | MathJax / KaTeX | 即時更新計算公式 |

##### J. 教學文案（Voiceover / Caption Script）

- **開場：** 「$A = QR$ 把矩陣的列『重新指向正交方向』。**怎麼做**？答案是『**Gram–Schmidt 正交化**』 — 一個一個處理列，每列都減去前面已產生方向的投影，再單位化。」
- **第 1 步：** 「第 1 列 $\mathbf{a}_1$ 直接單位化得 $\mathbf{q}_1$ — 沒有前面的列要減投影。長度 $\|\mathbf{a}_1\|$ 記到 $R$ 的對角線。」
- **第 2 步：** 「第 2 列 $\mathbf{a}_2$ 先**投影到 $\mathbf{q}_1$ 方向**，這個投影量 $r_{12} = \mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2$ 記到 $R$ 的 $(1, 2)$ 位置。$\mathbf{a}_2$ 減去這個投影 → 剩下的 $\mathbf{w}_2$ 與 $\mathbf{q}_1$ 垂直 → 單位化得 $\mathbf{q}_2$。」
- **第 3 步（若 $n \geq 3$）：** 「第 3 列同理，但要減**兩個方向**的投影（$\mathbf{q}_1$ 和 $\mathbf{q}_2$）。結果 $\mathbf{q}_3$ 與前兩個 $\mathbf{q}$ 都垂直。」
- **完成：** 「現在 $Q$ 的三列兩兩正交，$R$ 是上三角，且 $A = QR$。**注意 3D 視窗 — $Q$ 和 $A$ 撐起的是同一個 3D 空間**，只是用不同的基底描述。」
- **(P1) 連結：** 「圖右下角的 `using P1` 標籤點明：$\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k$ 就是 §5 (P1)『列線性組合』的特例，**只是 $R$ 限定為上三角**。」

##### K. 退化案例 + 邊界處理（Edge Cases）

- **列線性依賴：** 若 $\mathbf{a}_p$ 是前 $\mathbf{a}_1, \ldots, \mathbf{a}_{p-1}$ 的線性組合，$\mathbf{w}_p = \mathbf{0}$，Gram–Schmidt 失敗。顯示橙色警示「rank < n，需用 Modified Gram–Schmidt 或 Householder」+ 範例 5 觸發；
- **接近依賴（病態）：** 若 $\|\mathbf{w}_p\| < 10^{-6}$，數值不穩，顯示紅色警示；
- **正方形 $A$：** $m = n$，$Q$ 是正交矩陣（$Q^{-1} = Q^{\mathrm{T}}$），不變動畫流程；
- **$A$ 已是正交：** $A^{\mathrm{T}} A = I$，則 $Q = A, R = I$，動畫顯示「跳過所有減投影步驟」；
- **$A$ 已是上三角：** $Q = I, R = A$，動畫顯示「跳過所有單位化步驟」。

##### L. 學習評量提示（Assessment Hooks）

互動結束時提供「**理解檢核**」：

1. **概念題：** 「為什麼第 $p$ 步要減**前 $p-1$ 個** $\mathbf{q}_k$ 方向的投影，不能跳過某幾個？」（答：跳過會導致 $\mathbf{w}_p$ 不與所有前 $\mathbf{q}$ 都垂直，破壞正交性）；
2. **計算題：** 「給 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$，動手算 $\mathbf{q}_1, \mathbf{q}_2, R$。」（答：$\mathbf{q}_1 = (3/5, 4/5)^{\mathrm{T}}$，$r_{11} = 5$，$r_{12} = 4$，$\mathbf{w}_2 = (-12/5, 9/5)^{\mathrm{T}}$，$r_{22} = 3$，$\mathbf{q}_2 = (-4/5, 3/5)^{\mathrm{T}}$）；
3. **空間題：** 「驗證 $\mathbf{C}(A) = \mathbf{C}(Q)$：取一個任意 $\mathbf{v} \in \mathbf{C}(A)$，找出用 $A$ 列的線組係數和用 $Q$ 列的線組係數。」（答：兩組係數透過 $R$ 線性關聯）；
4. **跨章連結題：** 「點 → (P1) 對角特例按鈕，看 ch05 動畫。**如果 QR 的 $R$ 強制為對角矩陣，QR 退化成什麼？**」（答：$A$ 本來就是「正交列乘上對角縮放」即 $A = QD$，這只是 QR 在「列已正交」時的退化版）。

##### M. 實作里程碑（Milestones for S12+）

1. **M1（第 1 session）：** 畫面框架（左/中/右三區 + 5 個預設範例 + radio）；
2. **M2：** Gram–Schmidt 分步動畫（中區）— 三步驟逐步演示；
3. **M3：** $Q, R$ 同步填充動畫；
4. **M4（第 2 session）：** 3D 視窗（投影 + 減 + 單位化的幾何動畫）；
5. **M5：** 「對比 $A$ vs $Q$ 兩個基底」模式；
6. **M6：** 跨章 pointer 整合（→ ch05、→ 最小平方法）；
7. **M7：** 邊界處理（退化情形 + 接近依賴警示）；
8. **M8：** 教學文案 + 評量檢核 + 5 個範例驗證。

---

#### VizScript-02: 3D 投影視覺（精簡）

**Tier：** ⭐⭐ Tier 1 精簡（單純 3D 投影動畫，無互動參數調整）
**對應 VizMark：** Figure 6.5 VizMark-02
**預估實作工作量：** S12+ 約 1 session

##### A. 一句話定位

「3D 視窗中展示 Gram–Schmidt 的核心動作 — 把 $\mathbf{a}_p$ 投影到子空間 $\operatorname{span}\{\mathbf{q}_1, \ldots, \mathbf{q}_{p-1}\}$，減去投影得垂直向量 $\mathbf{w}_p$，再單位化。」

##### B–E. 互動 + 布局

- **輸入：** 固定 3 個預設 3D 範例（無自由調整）；
- **布局：** 整個畫面 3D 視窗占大半（800 × 600），底部顯示對應公式；
- **動畫腳本：** 3 個範例各 8 秒，總長 24 秒：
  - 範例 A：3 個正交但未單位化的向量 → 純單位化（無投影需要）；
  - 範例 B：3 個一般向量 → 經典 Gram–Schmidt 三步驟；
  - 範例 C：第 3 個向量幾乎在前兩個張成的平面內 → 投影後 $\mathbf{w}_3$ 接近零，展示病態情形。

##### F–G. 配色 + 計算邏輯

配色同 VizScript-01；計算邏輯複用 `gram_schmidt` 函式。

##### H–M. 其餘段落

精簡版主要是純動畫展示，無教學文案以外的互動。預估文字 ~500 字。

---

#### VizScript-03: 2×2 QR 數值範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1 輕量（單一範例逐步數字動畫）
**對應 VizMark：** Figure 6.5 VizMark-03
**預估實作工作量：** S12+ 約 0.5 session

##### A. 一句話定位

「對範例 $A = \bigl[\begin{smallmatrix}1&2\\1&0\end{smallmatrix}\bigr]$ 逐步動畫展示 Gram–Schmidt 兩步驟，每步顯示具體數字（含 $\sqrt{2}$ 表示）。」

##### B–E. 簡述

- **輸入：** 無（固定範例）；
- **動畫腳本：** 2 段（求 $\mathbf{q}_1, r_{11}$ → 求 $\mathbf{q}_2, r_{12}, r_{22}$），每段約 5 秒，總長 10 秒；
- **目標：** 入門用，學生第一次看 QR 時用此 demo 建立直覺，看完後再點 VizScript-01 自由探索。

##### F–M. 其餘段落

配色同 VizScript-01；無互動，純線性動畫；無評量。預估文字 ~250 字。

---

### 小結

- **§6.3 A=QR** 是 §6 五大分解的第三個，是「**單側正交化**」分解（左側 $Q$ 正交、右側 $R$ 上三角）；
- **與 (P1) 的連結直接顯式：** QR 圖標 `using P1`，是 S08 PNG 重核發現的「跨章 pointer 官方鐵證」第三例；
- **與 LU 的階梯關係：** QR = LU 把「下三角 $L$」**升級為正交 $Q$**；下一步 SVD = QR 把「上三角 $R$」也正交化；
- **三個 VizScript：** ⭐⭐⭐ Gram–Schmidt 動畫 + 3D 投影 + (P1) 列拆解 + ⭐⭐ 3D 純投影 + ⭐ 2×2 數字 walkthrough；
- **核心應用：** 最小平方法 $R\hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$，避開正規方程 $A^{\mathrm{T}} A$ 的病態；
- **下兩章 §6.4 $S = Q\Lambda Q^{\mathrm{T}}$ + §6.5 $A = U\Sigma V^{\mathrm{T}}$（S09 處理）：** 把「單側正交」升級為「**雙側正交 + 中間對角**」，迎來 SVD 這個「分解之王」。

---

## 6.4 矩陣分解 4：$S = Q \Lambda Q^{\mathrm{T}}$（Spectral Decomposition / Eigenvalue Decomposition）

> **原書頁碼：** p.11–p.12
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.4 $S = Q\Lambda Q^{\mathrm{T}}$（en.md line 430–505 / zh.md line 418–492）
> **本章圖數：** 1（`EVD.png`，原書圖中明標 **using P4**）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S09）

---

### 章節摘要

$S = Q \Lambda Q^{\mathrm{T}}$ 是 §6 五大分解的**第四個**，也是**整本書第一個「對矩陣本身有結構限制」的分解** — **僅限對稱矩陣** $S = S^{\mathrm{T}}$。它有兩個常用名字：

- **EVD（Eigenvalue Decomposition，特徵值分解）：** 強調「找特徵值 $\lambda_p$ 與特徵向量 $\mathbf{q}_p$」這條對角化路徑；
- **譜分解（Spectral Decomposition）：** 強調最終把 $S$ 寫成「投影矩陣的線性組合」$S = \sum_p \lambda_p P_p$，每個 $\lambda_p$ 配一個秩 1 投影到 $\mathbf{q}_p$ 方向 — 這是「**譜定理**（Spectral Theorem）」的內容。

兩個名字描述的是**同一個分解**，差別在於「強調特徵值/向量這個組件」還是「強調最終的『**對稱結構** = 投影矩陣加權和**』」。本章把兩個視角都鋪開。

**對稱矩陣的兩個鐵律（譜定理保證）：**

1. **所有特徵值 $\lambda_p$ 都是實數**（不會出現複數）；
2. **不同特徵值對應的特徵向量 $\mathbf{q}_p$ 互相正交**（不需手動正交化），可選為單位長 → $Q$ 是**正交矩陣**（$Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I$）。

**這兩個性質是對稱矩陣獨有的「禮物」** — 一般方陣的 $A = X \Lambda X^{-1}$（特徵分解）需要算 $X^{-1}$（昂貴且可能病態），但對稱矩陣 $S = Q \Lambda Q^{\mathrm{T}}$ 直接用 $Q^{\mathrm{T}}$ 就行（轉置 = 反矩陣）。**這是對稱矩陣在工程實務中無所不在的根本原因**：協方差矩陣、Gram 矩陣 $A^{\mathrm{T}} A$、Hessian 矩陣、二次型、PCA、量子力學的可觀測量算符 — 都對稱、都用 EVD 解。

**`using P4` 標記的意義（S09 PNG 重核發現）：** 原書 `EVD.png` 右下角圓圈標 `P4`（**S09 重大發現**），明示「EVD 圖的視覺視角是 §5 Pattern 4」— **「兩個正交矩陣夾一個對角矩陣」三明治結構**。這跟 §6.5 SVD 標的也是 `using P4`（S09 同步發現），等於原書作者把「對稱情境的 EVD」與「一般情境的 SVD」**用同一個視覺語言（P4 三明治）統一表達**。本章 VizScript 採**單 pointer 策略**（PNG 標什麼就指什麼）pointer 到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（P4 三明治）。

**本章 VizScript 策略：** ⭐⭐⭐ VizScript-01 採**單 pointer 策略** — (P4) 三明治結構 pointer 到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)；本章獨立寫的是 **譜分解的「投影矩陣加權和」動畫 + 3D 視窗看橢球主軸對齊（譜定理的幾何直覺）+ $P_p$ 三性質（完備 / 正交 / 冪等）視覺驗證** 等 EVD 特有的內容。

**對比 LU/QR：**

| 性質 | $A = LU$ | $A = QR$ | $S = Q\Lambda Q^{\mathrm{T}}$ |
|---|---|---|---|
| 矩陣限制 | 可 LU 分解 | 列線性獨立 | **必須對稱** $S = S^{\mathrm{T}}$ |
| 左側結構 | 下三角 $L$ | 正交 $Q$ | **正交** $Q$ |
| 中間/右側 | 上三角 $U$ | 上三角 $R$ | **對角** $\Lambda$ + 正交 $Q^{\mathrm{T}}$ |
| 「雙側」性質 | 無 | 單側正交 | **雙側正交（且兩側互為轉置）** |
| `using` 標記 | LU2 標 (MM4) | QR 標 (P1) | **EVD 標 (P4)** |
| 對應 §5 Pattern | (MM4) 秩 1 累加 | (P1) 列線組 | **(P4) 三明治** |
| 求解 $A^{-1}$ | 兩步反代 | $R^{-1} Q^{\mathrm{T}}$ | $Q \Lambda^{-1} Q^{\mathrm{T}}$ |

**核心升級點：** 從 QR 升級到 EVD = **把右側 $R$ 的「上三角」也升級為「對角」+ 把右側換成左側 $Q$ 的轉置 $Q^{\mathrm{T}}$**。這是「**雙側正交且對稱的對角化**」 — 對稱矩陣才有這個特權。

數值範例（本章貫穿，2×2 對稱矩陣）：

$$
S = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}
\;=\;
\underbrace{\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}}_{Q}
\underbrace{\begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}}_{\Lambda}
\underbrace{\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}}_{Q^{\mathrm{T}}}
$$

驗證：

1. 特徵值：$\det(S - \lambda I) = (3-\lambda)^2 - 1 = 0 \Rightarrow \lambda = 4$ 或 $\lambda = 2$；
2. $\lambda_1 = 4$：$(S - 4I) \mathbf{q}_1 = \mathbf{0} \Rightarrow \mathbf{q}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；
3. $\lambda_2 = 2$：$(S - 2I) \mathbf{q}_2 = \mathbf{0} \Rightarrow \mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
4. 驗證 $\mathbf{q}_1^{\mathrm{T}} \mathbf{q}_2 = (1 \cdot 1 + 1 \cdot (-1))/2 = 0$ ✓（自動正交，譜定理鐵律）；
5. $Q \Lambda Q^{\mathrm{T}} = \frac{1}{2} \begin{bmatrix}1&1\\1&-1\end{bmatrix} \begin{bmatrix}4&0\\0&2\end{bmatrix} \begin{bmatrix}1&1\\1&-1\end{bmatrix} = \frac{1}{2} \begin{bmatrix}4&2\\4&-2\end{bmatrix} \begin{bmatrix}1&1\\1&-1\end{bmatrix} = \frac{1}{2} \begin{bmatrix}6&2\\2&6\end{bmatrix} = \begin{bmatrix}3&1\\1&3\end{bmatrix} = S$ ✓。

**譜分解形式（本章核心 ⭐）：**

$$
S = \lambda_1 \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}} + \lambda_2 \mathbf{q}_2 \mathbf{q}_2^{\mathrm{T}}
= 4 \cdot \dfrac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} + 2 \cdot \dfrac{1}{2} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}
= \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix} + \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}
= \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix} = S \checkmark
$$

---

### 數學要點

#### 1. 定義與形狀

$$
S_{n \times n} = Q_{n \times n} \, \Lambda_{n \times n} \, Q^{\mathrm{T}}_{n \times n}, \qquad S = S^{\mathrm{T}}, \quad Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I_n
$$

- **$S$（Symmetric）：** $n \times n$ **對稱矩陣**，$s_{ij} = s_{ji}$。**這是本章唯一的限制條件** — 若 $S$ 不對稱，本分解形式失效，需用更一般的 $A = X \Lambda X^{-1}$（特徵分解，$X$ 一般不正交，$X^{-1}$ 不等於 $X^{\mathrm{T}}$）；
- **$Q$（Orthogonal）：** $n \times n$ **正交矩陣**，列為單位長且兩兩正交的特徵向量 $\mathbf{q}_1, \ldots, \mathbf{q}_n$。**$Q^{-1} = Q^{\mathrm{T}}$**（這是「正交矩陣」的定義性質，使 EVD 計算容易）；
- **$\Lambda$（Diagonal）：** $n \times n$ **對角矩陣**，對角元素為實特徵值 $\lambda_1, \lambda_2, \ldots, \lambda_n$（**通常按大小排序**：$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$，可正可負可零）；
- **形狀：** 全為 $n \times n$ **方陣**（與 LU、QR 可長方不同）；
- **可分解條件：** **任意對稱矩陣**（包含對稱半正定 / 對稱不定）都可分解，無例外（譜定理保證）。**這比 LU（需主元不為零）和 QR（需列線性獨立）寬鬆** — 對稱性自帶「全勤證書」。

#### 2. 譜定理（核心 ⭐）

**譜定理（Spectral Theorem）：** 任意實對稱矩陣 $S$ 可表示為

$$
S = Q \Lambda Q^{\mathrm{T}} = \sum_{p=1}^{n} \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}} = \sum_{p=1}^{n} \lambda_p P_p
$$

其中 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 是「**投影到 $\mathbf{q}_p$ 方向的秩 1 投影矩陣**」。

**展開（本章 2×2 範例）：**

$$
S = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}
= \underbrace{4 \cdot \dfrac{1}{2}\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}}_{\lambda_1 P_1}
+ \underbrace{2 \cdot \dfrac{1}{2}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}}_{\lambda_2 P_2}
$$

**譜定理三條保證（對任意實對稱 $S$）：**

1. **實特徵值：** 所有 $\lambda_p \in \mathbb{R}$（不會出現 $a + bi$ 複數）；
2. **正交特徵向量：** 不同特徵值對應的 $\mathbf{q}_p, \mathbf{q}_q$ 自動正交（$\mathbf{q}_p^{\mathrm{T}} \mathbf{q}_q = 0$，$p \neq q$）；
3. **完備正交基底：** 即使有重根特徵值（multiplicity $> 1$），也能在該特徵子空間內選一組正交基底（不會像一般矩陣那樣「特徵向量不夠」造成 Jordan 標準形）。

**證明草稿（保證 1 + 2）：**

- **保證 1（實特徵值）：** 設 $S \mathbf{q} = \lambda \mathbf{q}$（$\mathbf{q} \neq \mathbf{0}$）。取共軛轉置 $\mathbf{q}^* S^* = \bar{\lambda} \mathbf{q}^*$，因 $S$ 實對稱所以 $S^* = S$，得 $\mathbf{q}^* S = \bar{\lambda} \mathbf{q}^*$。右乘 $\mathbf{q}$：$\mathbf{q}^* S \mathbf{q} = \bar{\lambda} \mathbf{q}^* \mathbf{q}$。但 $\mathbf{q}^* S \mathbf{q} = \mathbf{q}^* (\lambda \mathbf{q}) = \lambda \mathbf{q}^* \mathbf{q}$。兩邊比較：$\lambda = \bar{\lambda}$ → $\lambda$ 實數 ✓；
- **保證 2（正交特徵向量）：** 設 $S \mathbf{q}_p = \lambda_p \mathbf{q}_p$，$S \mathbf{q}_q = \lambda_q \mathbf{q}_q$，$\lambda_p \neq \lambda_q$。則 $\mathbf{q}_q^{\mathrm{T}} S \mathbf{q}_p = \lambda_p \mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p$。又 $\mathbf{q}_q^{\mathrm{T}} S \mathbf{q}_p = \mathbf{q}_q^{\mathrm{T}} S^{\mathrm{T}} \mathbf{q}_p = (S \mathbf{q}_q)^{\mathrm{T}} \mathbf{q}_p = \lambda_q \mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p$。兩邊比較：$(\lambda_p - \lambda_q) \mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p = 0$。因 $\lambda_p \neq \lambda_q$，所以 $\mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p = 0$ ✓。

**這兩個證明只用了 $S = S^{\mathrm{T}}$ 一個性質** — 對稱性是「實 + 正交」的唯一來源。

#### 3. 投影矩陣 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 的三性質（核心 ⭐）

譜分解的另一個視角：把 $S$ 看成 $n$ 個秩 1 投影矩陣的線性組合，每個 $P_p$ 配一個權重 $\lambda_p$。

每個 $P_p$ 是「**投影到 $\mathbf{q}_p$ 撐起的 1 維子空間**」的投影算子，有三條結構性質：

##### 3.1 完備性（Completeness）

$$
\sum_{p=1}^{n} P_p = P_1 + P_2 + \cdots + P_n = Q Q^{\mathrm{T}} = I_n
$$

**意義：** $n$ 個 1 維投影**覆蓋整個 $\mathbb{R}^n$ 空間**，沒有缺漏。對任意向量 $\mathbf{v}$：

$$
\mathbf{v} = I \mathbf{v} = \sum_{p=1}^{n} P_p \mathbf{v} = \sum_{p=1}^{n} (\mathbf{q}_p^{\mathrm{T}} \mathbf{v}) \mathbf{q}_p
$$

— 這就是「用正交基底展開向量」的標準公式。**完備性 = 正交基底的「無漏」性質。**

##### 3.2 正交性（Mutual Orthogonality）

$$
P_p P_q = O \quad (p \neq q)
$$

**驗證（本章範例）：**

$$
P_1 P_2 = \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} \cdot \dfrac{1}{2}\begin{bmatrix}1&-1\\-1&1\end{bmatrix}
= \dfrac{1}{4}\begin{bmatrix}0&0\\0&0\end{bmatrix} = O \checkmark
$$

**意義：** 投影到 $\mathbf{q}_p$ 後再投影到 $\mathbf{q}_q$（$p \neq q$）= 0。**因為 $\mathbf{q}_q$ 與 $\mathbf{q}_p$ 正交，$\mathbf{q}_p$ 方向上的分量在 $\mathbf{q}_q$ 上沒有任何投影**。

**幾何直覺：** 想像 $\mathbb{R}^3$ 中 $x, y, z$ 三軸（互相垂直），投影到 $x$ 軸再投影到 $y$ 軸 = 0（兩個投影方向不重疊）。$P_p P_q = O$ 是「**互補方向**」的代數寫法。

##### 3.3 冪等性（Idempotence）

$$
P_p^2 = P_p, \quad P_p^{\mathrm{T}} = P_p
$$

**驗證（本章範例）：**

$$
P_1^2 = \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} \cdot \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix}
= \dfrac{1}{4}\begin{bmatrix}2&2\\2&2\end{bmatrix} = \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} = P_1 \checkmark
$$

**意義：** 投影到 $\mathbf{q}_p$ 後**再投影一次仍是同一個結果** — 因為向量已經在 $\mathbf{q}_p$ 方向上了，再投影一次不會再縮小或改變方向。

**幾何直覺：** 想像把一個 3D 物體投影到 $xy$ 平面上得到陰影；對這個陰影**再投影一次到同一個 $xy$ 平面**還是同樣的陰影（陰影本身已在 $xy$ 平面上）。

**對稱性 $P_p^{\mathrm{T}} = P_p$：** 由 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 直接看出 — 轉置後仍是 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$。**這是「正交投影」的識別標誌**：對稱 + 冪等 = 正交投影矩陣。

##### 三性質統一視圖

| 性質 | 公式 | 幾何意義 |
|---|---|---|
| 完備性 | $\sum P_p = I$ | $n$ 個 1 維投影覆蓋整個 $\mathbb{R}^n$ |
| 正交性 | $P_p P_q = O$（$p \neq q$）| 不同方向的投影互不干擾 |
| 冪等性 | $P_p^2 = P_p$，$P_p^{\mathrm{T}} = P_p$ | 重複投影不變、轉置即自身 |

**這三條性質讓「譜分解 = 投影分解」 — 把 $S$ 看成「在每個正交方向上做不同強度的縮放」**。

#### 4. 與 (P4) 視角的連結 — 三明治結構（核心 ⭐）

**(P4) Pattern（§5）：** 「兩個矩陣夾一個對角矩陣 = 秩 1 之和（用對角元素加權）」

$$
\underbrace{U}_{\text{左側}} \underbrace{D}_{\text{對角}} \underbrace{V^{\mathrm{T}}}_{\text{右側}} = \sum_p d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**EVD 是 (P4) 的「特殊情境」** — **左側 $U = Q$，右側 $V^{\mathrm{T}} = Q^{\mathrm{T}}$（兩側相同！），對角 $D = \Lambda$：**

$$
S = \underbrace{Q}_{\text{左 = 正交}} \underbrace{\Lambda}_{\text{對角 = 特徵值}} \underbrace{Q^{\mathrm{T}}}_{\text{右 = 左的轉置}}
= \sum_p \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}
$$

**「兩側相同」是對稱矩陣的視覺指紋** — 在 (P4) 三明治結構中，左側和右側「**鏡像對稱**」，這直接對應 $S = S^{\mathrm{T}}$。

**對照表：**

| 元素 | (P4) 一般形式 | EVD 特化 |
|---|---|---|
| 左側 | $U$（任意） | $Q$（正交，特徵向量） |
| 對角 | $D$（任意對角） | $\Lambda$（特徵值） |
| 右側 | $V^{\mathrm{T}}$（任意） | $Q^{\mathrm{T}}$（**左側的轉置**） |
| 秩 1 形式 | $\sum d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ | $\sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ |
| 秩 1 結構 | 一般「外積」（$\mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$） | **「自外積」$\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}} = P_p$ 投影矩陣** |
| 對稱性 | 一般 $UDV^{\mathrm{T}}$ 不對稱 | $S = (Q\Lambda Q^{\mathrm{T}})^{\mathrm{T}} = Q \Lambda^{\mathrm{T}} Q^{\mathrm{T}} = Q \Lambda Q^{\mathrm{T}} = S$ ✓ |

**「using P4」標籤的意涵：** 原書 `EVD.png` 標 `using P4`，直接點明「EVD 圖就是 (P4) 在『左 = 右轉置 + 對角是特徵值』情形下的特化」。**這是非常精細的標記** — 同樣標 `P4` 的 `SVD.png`（§6.5）情形是「左右兩個正交矩陣**不同** + 對角是奇異值」，EVD 是「左右兩個正交矩陣**相同（互為轉置）** + 對角是特徵值」。**EVD = SVD 的「對稱矩陣對偶版」**。

**連結 (MM4)：** 把譜分解寫成 (MM4) 形式：

$$
S = \sum_{p=1}^{n} \underbrace{\lambda_p \mathbf{q}_p}_{\text{係數 × 列}} \cdot \underbrace{\mathbf{q}_p^{\mathrm{T}}}_{\text{行}} = \sum_{p=1}^{n} \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}
$$

這正好是 (MM4) 「外積之和」的形式，**只是兩個外積向量是同一個 $\mathbf{q}_p$**（而非一般 (MM4) 的 $\mathbf{c}_p$ 和 $\mathbf{r}_p$）。雖然 PNG 沒標 `using MM4`（只標 `using P4`），但 EVD 仍然**繼承 (MM4) 的所有性質**（秩 1 累加、低秩近似、漸進收斂等），可重用 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 的累加動畫概念。

#### 5. 對稱矩陣的特殊性 — 為什麼 EVD 不需 $X^{-1}$

**一般方陣的特徵分解：**

$$
A = X \Lambda X^{-1}
$$

其中 $X$ 是「特徵向量列矩陣」**不一定正交**，所以需要算 $X^{-1}$。算 $X^{-1}$ 有兩個問題：

1. **計算昂貴：** 反矩陣 $O(n^3)$，與 LU 分解相當；
2. **數值不穩：** 若 $X$ 接近奇異（特徵向量幾乎共線），$X^{-1}$ 元素會爆炸大 → 數值誤差放大。

**對稱矩陣的譜分解：**

$$
S = Q \Lambda Q^{\mathrm{T}}
$$

因 $Q$ 正交，$Q^{-1} = Q^{\mathrm{T}}$（**轉置 = 反矩陣**）。**轉置只需 $O(1)$（指標重排）**，且**完美數值穩定**（$\|Q\| = 1$，無放大）。

**這是對稱矩陣比一般矩陣「便宜 N 倍」的關鍵原因。** 在工程實務中：

- **協方差矩陣** $C = \frac{1}{n} X^{\mathrm{T}} X$ — 對稱 → PCA 用 EVD（不用普通特徵分解）；
- **Hessian 矩陣** $H_{ij} = \partial^2 f / \partial x_i \partial x_j$ — 對稱（混合偏導交換）→ 牛頓法 / 二次型優化用 EVD；
- **Gram 矩陣** $G = A^{\mathrm{T}} A$ — 對稱 → 核方法 / SVD 預備步驟用 EVD；
- **量子力學的可觀測量** — 算符自伴（埃爾米特）→ 譜分解 = 物理可測量。

#### 6. $S = Q\Lambda Q^{\mathrm{T}}$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **EVD ↔ CR** | EVD 限對稱、$Q$ 正交、$\Lambda$ 對角；CR 一般矩陣、$C$ 是獨立列、$R$ 是 RREF。**EVD 把對稱矩陣的「秩」直接寫成「非零特徵值的個數」**，而 CR 是「獨立列的個數」 — 兩者數值相等（$\operatorname{rank}(S) = $ 非零特徵值個數，對稱情境下這是定理）|
| **EVD ↔ LU** | LU 解 $S\mathbf{x} = \mathbf{b}$ 用兩步反代；EVD 解 $S\mathbf{x} = \mathbf{b}$ 用 $\mathbf{x} = Q \Lambda^{-1} Q^{\mathrm{T}} \mathbf{b}$（**$\Lambda^{-1}$ 只是對角元素取倒數**）。**EVD 在「重複解多個 $\mathbf{b}$」時更快**（共用 $Q, \Lambda^{-1}$） |
| **EVD ↔ QR** | QR 是「列正交化」（一般矩陣可用，$\mathbf{C}(A) = \mathbf{C}(Q)$）；EVD 是「對稱矩陣的雙側正交化」。**從 QR 到 EVD = 把 $R$ 也正交化（變對角 $\Lambda$）+ 強制左右對稱**。實務上**對稱矩陣的 EVD 計算常用 QR 演算法迭代**（QR 演算法 $\neq$ QR 分解，但每步用 QR 分解）|
| **EVD ↔ SVD** | **SVD 是 EVD 的「一般化」** — EVD 限對稱、雙側 $Q$ 相同；SVD 任意矩陣、雙側 $U \neq V$。對任意 $A$：$A^{\mathrm{T}} A$ 對稱半正定 → EVD 給出 $\Sigma^2$ 和 $V$；$A A^{\mathrm{T}}$ 對稱半正定 → EVD 給出 $\Sigma^2$ 和 $U$。**SVD = 兩個 EVD 的整合**（詳見 §6.5） |

**結論：** $S = Q\Lambda Q^{\mathrm{T}}$ 是「**對稱矩陣的雙側正交對角化**」。沿著「正交化逐步加強 + 對稱性限制」的階梯看：

$$
\underbrace{CR}_{\text{0 側正交}} \;\to\; \underbrace{LU}_{\text{0 側正交 + 三角結構}} \;\to\; \underbrace{QR}_{\text{1 側正交 + 三角結構}} \;\to\; \underbrace{Q\Lambda Q^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角結構}\\\text{（限對稱）}}} \;\to\; \underbrace{U\Sigma V^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角結構}\\\text{（一般矩陣）}}}
$$

**EVD 在 §6 五大分解中的角色：** 「**對稱情境的對角化**」 — 比 QR 多一層「右側也正交化」，比 SVD 多一層「對稱限制（使左右兩側相同）」。

#### 7. 數學要點總結（一張表）

| 性質 | $S = Q\Lambda Q^{\mathrm{T}}$ 的對應 |
|---|---|
| 適用矩陣 | 任意實對稱方陣 $S = S^{\mathrm{T}} \in \mathbb{R}^{n \times n}$（無須正定） |
| $Q$ 的結構 | $n \times n$ 正交矩陣，列為單位特徵向量 $\mathbf{q}_p$，$Q^{\mathrm{T}} = Q^{-1}$ |
| $\Lambda$ 的結構 | $n \times n$ 對角矩陣，對角元素為實特徵值 $\lambda_p$（通常按大小降冪排序）|
| 項數 | $n$（與矩陣維度同） |
| 構造方法 | 算 $\det(S - \lambda I) = 0$ 求 $\lambda_p$ → 解 $(S - \lambda_p I)\mathbf{q}_p = \mathbf{0}$；數值上用 QR 迭代演算法 |
| §4 (MM4) 對應 | $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$（外積向量左右相同 $\mathbf{q}_p$）|
| §5 Pattern 對應 | **`EVD.png` 標 `using P4`**：(P4) 三明治的「左 = 右轉置 + 對角是特徵值」特化 |
| 投影矩陣 $P_p$ 性質 | 完備（$\sum P_p = I$）+ 正交（$P_p P_q = O$）+ 冪等（$P_p^2 = P_p$）+ 對稱（$P_p^{\mathrm{T}} = P_p$）|
| 求 $S^{-1}$ | $S^{-1} = Q \Lambda^{-1} Q^{\mathrm{T}}$（$\Lambda^{-1}$ 只是對角倒數，前提 $\lambda_p \neq 0$）|
| 求 $S^k$（任意實 $k$） | $S^k = Q \Lambda^k Q^{\mathrm{T}}$（$\Lambda^k$ 只是對角元素 $k$ 次方）|
| 二次型 | $\mathbf{x}^{\mathrm{T}} S \mathbf{x} = \sum_p \lambda_p (\mathbf{q}_p^{\mathrm{T}} \mathbf{x})^2$（譜分解的二次型展開）|
| 計算量 | $O(n^3)$（QR 迭代演算法）|

---

### 圖片詳細描述（Figure Descriptions）

#### Figure 6.6: $S = Q\Lambda Q^{\mathrm{T}}$ — 標 using P4

**圖檔：** `docs/book/figs-png/EVD.png`（原始 EPS：`figs/EVD.eps`）
**原書頁碼：** p.11 圖 16
**所屬章節：** §6.4 $S = Q\Lambda Q^{\mathrm{T}}$（**唯一一張**，無對偶圖）
**圖中標記：** **`using P4`**（圓圈標，右下角）

##### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，3×3 對稱矩陣示意，共 8 段：

1. **第 1 段：** 矩陣 $S$ 的方框（內含**淺灰色塊**，無條紋）— 上方有大字 `S`；**淺灰色 = 「對稱結構」的視覺信號**（與 LU/QR 的 $A$ 用條紋色不同，這裡用單色塊強調對稱）；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $Q$（方框內 **3 條等寬綠色直立列，每列底部標 `1`/`2`/`3`**）— 上方有大字 `Q`；綠色 = 「正交且單位長」視覺信號（與 QR 的 $Q$ 同款）；
4. **第 4 段：** 矩陣 $\Lambda$（方框內 **3 個藍色圓點沿對角線排列**，非對角位置完全留白）— 上方有大字 $\Lambda$；**藍點明示「$\Lambda$ 是對角矩陣」**；
5. **第 5 段：** 矩陣 $Q^{\mathrm{T}}$（方框內 **3 條等寬綠色橫躺行，每行左側標 `1`/`2`/`3`**）— 上方有大字 $Q^{\mathrm{T}}$；**$Q$ 直立 + $Q^{\mathrm{T}}$ 橫躺 = 視覺上立刻看出「轉置關係 = 列變行」**；
6. **第 6 段：** 等號 `=`；
7. **第 7–9 段：** 拆解結果，**3 個方框並排，每個都標 $\lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$**：
   - 第 7 段：$\lambda_1 \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}}$ — 方框內含 **1 條綠色直立列（標 `1`）+ 上方淡綠橫躺行（標 `1`）**，藍點標 $\lambda_1$；
   - 第 8 段：加號 `+`；$\lambda_2 \mathbf{q}_2 \mathbf{q}_2^{\mathrm{T}}$ — **同樣結構，標 `2`**；
   - 第 9 段：加號 `+`；$\lambda_3 \mathbf{q}_3 \mathbf{q}_3^{\mathrm{T}}$ — **同樣結構，標 `3`**；
8. **右下角圖示：** 圓圈內標 `P4`，文字 `using` — **直接標明「本圖用 §5 Pattern 4 視角」**。

**「直立列 + 橫躺行」對偶布局的視覺意義：** 每個 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 拆解圖中，**$\mathbf{q}_p$（綠色直立列）疊在 $\mathbf{q}_p^{\mathrm{T}}$（淡綠橫躺行）之上**，明確展示「自外積 = 列向量乘以自己的轉置」。**這是譜定理「投影矩陣」概念的視覺化** — 每個 $P_p$ 的形狀都是「列 × 行」的 $n \times n$ 矩陣，而非單一的列或行。

**閱讀順序：** 由左到右讀整個等式鏈 `S = Q Λ Q^T = (三個 λ_p P_p 累加)`。重點掃右側的 3 個拆解項，注意「**綠列 + 綠行對偶布局 + 藍點 λ_p 加權**」。

##### 數學內容 (Mathematical Content)

對應數學表示（**(P4) Pattern 4** 三明治視角，左 = 右轉置特化版）：

$$
S = Q \Lambda Q^{\mathrm{T}}
= \begin{bmatrix} | & | & | \\ \mathbf{q}_1 & \mathbf{q}_2 & \mathbf{q}_3 \\ | & | & | \end{bmatrix}
\begin{bmatrix} \lambda_1 & & \\ & \lambda_2 & \\ & & \lambda_3 \end{bmatrix}
\begin{bmatrix} - & \mathbf{q}_1^{\mathrm{T}} & - \\ - & \mathbf{q}_2^{\mathrm{T}} & - \\ - & \mathbf{q}_3^{\mathrm{T}} & - \end{bmatrix}
= \sum_{p=1}^{3} \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}
$$

**關鍵數值關係（對任意對稱 $S$）：**

- $S = S^{\mathrm{T}}$（對稱性）；
- $Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I_n$（正交性）；
- $\sum P_p = I_n$（完備性）；
- $P_p P_q = O$（$p \neq q$，正交性）；
- $P_p^2 = P_p^{\mathrm{T}} = P_p$（冪等對稱性）。

**從 $S$ 提取 $(\lambda_p, \mathbf{q}_p)$：** 用「特徵值分解 + Gram-Schmidt 正交化重複根」算法，數值上用 QR 演算法迭代 — **不像 (MM4) 的外積那樣可直接讀出**，需要解 $\det(S - \lambda I) = 0$。

##### 直覺解讀 (Intuition)

EVD 圖傳達四層核心訊息：

1. **「對稱性 = 視覺鏡像」直覺：** $Q$（綠列直立）和 $Q^{\mathrm{T}}$（綠行橫躺）在 $\Lambda$ 兩側**鏡像對稱**，視覺上立刻看出「左右兩側是同一組向量，只是擺向不同」。**這就是對稱矩陣 $S = S^{\mathrm{T}}$ 的視覺指紋** — 一般矩陣的 (P4) 三明治左右是不同矩陣（$U, V^{\mathrm{T}}$，見 §6.5 SVD），EVD 是「自鏡像」特例；

2. **「對角 $\Lambda$ = 純縮放」直覺：** 中間的 3 個藍點沿對角排列，視覺上明示「**只有對角線有值，非對角全為零**」。$\Lambda$ 的作用是「在每個正交方向上做不同強度的縮放（縮放因子 = 特徵值 $\lambda_p$）」；

3. **「投影矩陣 $P_p$ = 自外積」直覺：** 右側 3 個拆解項的 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ **使用同一個向量做兩次外積**（綠列 × 綠行，左右標號相同 `1`、`2`、`3`），視覺上強調「自外積得到秩 1 投影矩陣」。**這跟 (MM4) 的一般外積 $\mathbf{c}_p \mathbf{r}_p^{\mathrm{T}}$ 不同**（左右標號可以不同），EVD 強制「左右標號相同」；

4. **「譜分解 = 加權的投影累加」直覺：** $S = \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$ — 每個方向 $\mathbf{q}_p$ 都有一個「強度 $\lambda_p$」，加總就是整個對稱矩陣的全部資訊。**這是譜定理的核心視覺敘述** — 對稱矩陣 = 「正交方向 × 對應強度」的加權集合。

**「using P4」標籤的重要性（S09 PNG 重核確認）：** 原書作者刻意把這張圖標 `using P4`，與 §6.5 SVD 同款 — 等於明說「**EVD 圖跟 SVD 圖是同一種視角（(P4) 三明治），只是 EVD 強制左右兩側互為轉置**」。視覺化可以**直接重用 [ch05 VizScript-03](ch05-patterns.md#vizscript-03) 的 P4 三明治互動**（把 $V^{\mathrm{T}}$ 鎖成 $U^{\mathrm{T}}$，把 $\Sigma$ 換成 $\Lambda$ 含負值），這就是為什麼本章 VizScript-01 採**單 pointer 策略**指 ch05 VizScript-03。

**為什麼這張圖該做成互動視覺化？** 因為 EVD 的核心過程「**對稱矩陣 → 正交基底 + 對角縮放**」是「**從矩陣形狀讀出向量幾何**」的關鍵步驟 — 用戶調 $S$ 看每個 $\lambda_p, \mathbf{q}_p$ 如何變、3D 視窗看「**$S$ 作用 = 在每個 $\mathbf{q}_p$ 方向上拉伸 $\lambda_p$ 倍**」（橢球主軸對齊的幾何直覺）、譜定理 $\sum \lambda_p P_p$ 加權累加的「投影分解」過程。靜態圖只能展示最終結果，**互動 demo 可以展示「拉一個對稱矩陣的元素 → 看特徵值如何變 + 橢球如何旋轉」**，這是 EVD 教學的關鍵突破點（見 VizMark-01）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [譜分解互動 + 橢球主軸對齊 3D] ⭐⭐⭐
> 「拉桿調 $S$ 的元素（強制對稱）→ 即時計算 $\lambda_p, \mathbf{q}_p$ → 動畫展示譜分解 $S = \sum \lambda_p P_p$ 三項累加 → 3D 視窗看單位球被 $S$ 變成橢球（主軸 = $\mathbf{q}_p$ 方向，半徑 = $|\lambda_p|$）→ 視覺驗證 $P_p$ 三性質」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [$P_p$ 三性質視覺驗證] ⭐⭐
> 「3 個 $P_p$ 矩陣並排顯示 + 互動驗證完備（$\sum P_p = I$）/ 正交（$P_p P_q = O$）/ 冪等（$P_p^2 = P_p$）三條性質」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [2×2 EVD 數值範例] ⭐
> 「用 2×2 範例 $S = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$ 一步一步動畫展示計算過程（特徵值 → 特徵向量 → 譜分解），每步顯示具體數字 + 公式」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: 譜分解互動 + 橢球主軸對齊（EVD Spectral Decomposition Animation）

**Tier：** ⭐⭐⭐ Tier 2（含譜分解逐項動畫 + 3D 橢球主軸視覺 + $P_p$ 三性質驗證；單 pointer 指 ch05 VizScript-03）
**對應 VizMark：** Figure 6.6 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 + 譜分解動畫 1 session + 3D 橢球視覺 1 session）

##### A. 一句話定位

「給一個對稱矩陣 $S$（$n \in \{2, 3\}$），動態展示譜分解 $S = \sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ — 三個秩 1 投影矩陣加權累加 — 並用 3D 視窗看 $S$ 把單位球變成橢球（主軸 = $\mathbf{q}_p$ 方向，半徑 = $|\lambda_p|$），視覺驗證譜定理。」

##### B. 學習目標（Learning Outcome）

- **譜定理直覺：** 看到對稱矩陣，能在腦中想像「**正交方向 + 對應特徵值縮放**」的幾何圖景；
- **特徵向量 = 不變方向：** 透過 3D 視窗看到 $S \mathbf{q}_p = \lambda_p \mathbf{q}_p$（向量方向不變、只縮放）；
- **橢球主軸對齊：** 看到單位球被 $S$ 變成橢球，主軸方向就是 $\mathbf{q}_p$、半徑就是 $|\lambda_p|$；
- **$P_p$ 三性質：** 看完備性（三項加總 = $I$）/ 正交性（$P_p P_q = O$）/ 冪等性（重複投影不變）；
- **跨章連結：** 點 (P4) 按鈕跳 ch05 VizScript-03 看一般三明治結構（理解 EVD 是 P4 的「自鏡像」特例）。

##### C. 互動參數（UI Inputs）

- **矩陣輸入 $S$：** $n \times n$ 格子網格，$n \in \{2, 3\}$，每格 $s_{ij} \in [-9, 9]$ 步進 1；
  - **強制對稱：** 改 $s_{ij}$ 自動同步改 $s_{ji}$（UI 上連動）；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$（書中 2×2 範例，$\lambda = 4, 2$ 兩正特徵值）；
  - 範例 2：$\bigl[\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr]$（$\lambda = 3, 1$ 兩正特徵值）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\bigr]$（$\lambda = 3, -1$ **一正一負**，橢球變雙曲線）；
  - 範例 4：$\bigl[\begin{smallmatrix}3&0&0\\0&2&0\\0&0&1\end{smallmatrix}\bigr]$（**已是對角**，$Q = I$ 特例）；
  - 範例 5：$\bigl[\begin{smallmatrix}2&1&0\\1&2&0\\0&0&3\end{smallmatrix}\bigr]$（3×3 含一個獨立軸）；
  - 範例 6：$\bigl[\begin{smallmatrix}1&1&1\\1&1&1\\1&1&1\end{smallmatrix}\bigr]$（**退化** rank = 1，$\lambda = 3, 0, 0$，譜分解只有 1 項）；
- **動畫模式切換 (radio)：** `分項動畫（手動下一項）` / `自動播放譜分解` / `對比 $S$ vs 橢球變形`；
- **3D 視窗開關 (checkbox)：** 開啟後右側顯示 3D 視窗（僅當 $n \in \{2, 3\}$ 可用）；
- **顯示模式 (checkbox 三選擇)：** `顯示譜分解` / `顯示橢球` / `顯示 $P_p$ 三性質`；
- **跳轉按鈕：**
  - 「→ (P4) 三明治結構」按鈕（跳 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)，自動把 $V^{\mathrm{T}}$ 鎖成 $U^{\mathrm{T}}$，把 $\Sigma$ 換成 $\Lambda$）；
  - 「→ (MM4) 秩 1 累加」按鈕（跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 看一般 (MM4) 累加形式）。

##### D. 視覺布局（Layout）

**主畫面三區（標準模式）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $S$ 的格子輸入網格（含對稱連動）+ 預設範例選擇器 + radio + 顯示模式 checkbox |
| 中區（譜分解動畫） | $S, Q, \Lambda, Q^{\mathrm{T}}$ 四矩陣並排（鏡像布局） + 拆解後 3 項 $\lambda_p P_p$ 並排（含 + 號）+ 當前正在處理的項高亮（金色框）|
| 右區（3D 視窗，可選） | 3D 座標系中顯示單位球（灰色半透明）→ 變成橢球（金色半透明）+ 3 條 $\mathbf{q}_p$ 主軸（綠箭頭）+ 半徑標 $|\lambda_p|$ |

**底部資訊條：**

- 當前的 $\lambda_p, \mathbf{q}_p$ 數值（小字）；
- 「**譜定理驗證：$\sum \lambda_p P_p = S$**」（綠色 ✓ 顯示，hover 顯示計算過程）；
- 「**$P_p$ 三性質**」（三個小綠 ✓：完備 / 正交 / 冪等）；
- **跳轉按鈕區**（兩個橫向按鈕：→ (P4) 三明治 / → (MM4) 秩 1）。

##### E. 動畫腳本（Storyboard）

**Step 1（0–500ms）：** $S$ 的格子網格從左區滑入中區，特徵值計算啟動（後台），公式區顯示 `det(S - λI) = 0` 求 $\lambda_p$。

**Step 2（500–1500ms）：** $\lambda_p, \mathbf{q}_p$ 計算完成，$Q, \Lambda, Q^{\mathrm{T}}$ 三矩陣依序滑入中區（鏡像布局：$Q$ 在 $\Lambda$ 左側，$Q^{\mathrm{T}}$ 在右側，明顯**鏡像對稱**）；
- 3D 視窗：單位球淡入（灰色，半徑 1）→ $S$ 作用後變成橢球（金色，主軸長度 = $|\lambda_p|$，主軸方向 = $\mathbf{q}_p$ 綠箭頭）；
- 公式區同步顯示 `S = Q Λ Q^T`。

**Step 3（1500–3000ms，第 $p = 1$ 項，$\lambda_1$ 最大）：**
- 高亮第 1 項 $\lambda_1 \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}}$（金色框）；
- $\mathbf{q}_1$ 從 $Q$ 第 1 列位置「飛出」一份（綠色直立列副本）→ $\mathbf{q}_1^{\mathrm{T}}$ 從 $Q^{\mathrm{T}}$ 第 1 行位置「飛出」一份（淡綠橫躺行副本）→ 兩者疊在第 1 拆解項位置上組成 $P_1 = \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}}$ 矩陣；
- $\lambda_1$ 藍點從 $\Lambda$ 對角位置「飛出」一份 → 顯示為 $\lambda_1 P_1$ 的係數；
- 累計部分和 $S^{(1)} = \lambda_1 P_1$ 顯示為 3D 視窗中的「**只沿 $\mathbf{q}_1$ 方向的縮放**」（橢球瞬間變一條粗線，沿 $\mathbf{q}_1$ 方向長度 $|\lambda_1|$）。

**Step 4（3000–4500ms，第 $p = 2$ 項，$\lambda_2$）：**
- 類似 Step 3，但用 $\lambda_2, \mathbf{q}_2$；
- 累計部分和 $S^{(2)} = \lambda_1 P_1 + \lambda_2 P_2$ 顯示為 3D 視窗中的「**$\mathbf{q}_1, \mathbf{q}_2$ 兩個方向的縮放疊加**」（線變橢圓）；
- 顯示誤差 $\|S - S^{(2)}\|_F$（若 $n = 2$ 此時誤差 = 0）。

**Step 5（4500–6000ms，第 $p = 3$ 項，$\lambda_3$，若 $n = 3$）：**
- 類似 Step 3，但用 $\lambda_3, \mathbf{q}_3$；
- 累計部分和 $S^{(3)} = \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$（**完整**）；
- 3D 視窗：橢圓變完整橢球，主軸對齊 $\{\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3\}$；
- 顯示誤差 $\|S - S^{(3)}\|_F = 0$ ✓（譜定理驗證）。

**Step 6（按 `顯示 $P_p$ 三性質` checkbox）：**
- 三個 $P_p$ 矩陣淡入並排顯示；
- **完備性：** 三個 $P_p$ 同時亮起綠光 → 「飛」到一起加總 → 變成 $I_n$（藍色對角點）；
- **正交性：** $P_1 P_2$ 計算動畫 → 結果矩陣全為 0（藍灰）；同樣演示 $P_2 P_3, P_3 P_1$；
- **冪等性：** $P_1$ 自乘 → 結果仍是 $P_1$（高亮自我複製動畫）。

**Step 7（按 `對比` radio）：** 顯示「3D 旋轉動畫」：
- 旋轉 360° 看橢球從不同角度的形狀；
- 標出「**$\mathbf{q}_p$ 方向 = 橢球主軸方向 = $S$ 的不變方向**」；
- 互動拉桿改 $\lambda_p$ 看橢球如何即時拉伸 / 壓扁 / 翻轉（負特徵值 → 鏡像反射）。

##### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $\mathbf{q}_p$ / $Q$ 的列 / 3D 視窗中的橢球主軸；
- **淺綠（半透明）：** $\mathbf{q}_p^{\mathrm{T}}$ / $Q^{\mathrm{T}}$ 的行（強調轉置 = 同向量擺向不同）；
- **灰 `#cccccc`：** 原始單位球（3D 視窗）/ 對稱輸入 $S$ 的方框 fill；
- **金 `#FFD700`：** 變形後的橢球 / 當前正在處理的項（高亮框）；
- **藍 `#1f77b4`：** $\Lambda$ 的對角元素（藍點）/ 完備性結果 $I$（藍對角點）；
- **紫 `#9467bd`：** 退化警示（範例 6 rank 不足）/ 負特徵值的鏡像反射；
- **紅 `#d62728`：** （此章較少用）誤差條 / $\|S - S^{(k)}\|_F > 0$ 警示。

##### G. 計算邏輯（Numerical Backend）

```python
def spectral_decomposition(S: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[dict]]:
    """Symmetric S → (Q, Lambda, history_for_animation).
    Assumes S is symmetric. Returns eigenvalues sorted descending."""
    assert np.allclose(S, S.T), "S must be symmetric"
    eigvals, eigvecs = np.linalg.eigh(S)  # eigh for symmetric
    # Sort by |eigenvalue| descending (so largest visual contribution first)
    order = np.argsort(-np.abs(eigvals))
    Lambda = np.diag(eigvals[order])
    Q = eigvecs[:, order]
    history = []
    S_partial = np.zeros_like(S, dtype=float)
    for p in range(S.shape[0]):
        q_p = Q[:, p:p+1]
        P_p = q_p @ q_p.T
        lam_p = eigvals[order[p]]
        S_partial = S_partial + lam_p * P_p
        history.append({
            'p': p + 1,
            'lambda_p': lam_p,
            'q_p': q_p.flatten().tolist(),
            'P_p': P_p.tolist(),
            'S_partial': S_partial.tolist(),
            'error_fro': float(np.linalg.norm(S - S_partial, 'fro')),
        })
    return Q, Lambda, history


def verify_P_properties(Q: np.ndarray) -> dict:
    """Verify P_p three properties: completeness, mutual orthogonality, idempotence."""
    n = Q.shape[1]
    P_list = [Q[:, p:p+1] @ Q[:, p:p+1].T for p in range(n)]
    completeness = np.allclose(sum(P_list), np.eye(n))
    orthogonality = all(
        np.allclose(P_list[p] @ P_list[q], 0)
        for p in range(n) for q in range(n) if p != q
    )
    idempotence = all(
        np.allclose(P_list[p] @ P_list[p], P_list[p])
        for p in range(n)
    )
    return {
        'completeness': completeness,
        'orthogonality': orthogonality,
        'idempotence': idempotence,
    }


def ellipsoid_axes(S: np.ndarray) -> tuple[list[float], list[list[float]]]:
    """For 3D visualization: return semi-axis lengths and directions."""
    eigvals, eigvecs = np.linalg.eigh(S)
    semi_axes = [abs(lam) for lam in eigvals]
    directions = [eigvecs[:, p].tolist() for p in range(len(eigvals))]
    return semi_axes, directions
```

**3D 橢球渲染（matplotlib 3D 或 plotly 3D）：**

```python
# 參數化單位球：(cos(u)sin(v), sin(u)sin(v), cos(v))
u, v = np.meshgrid(np.linspace(0, 2*np.pi, 50), np.linspace(0, np.pi, 25))
unit_sphere = np.array([np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v)])
# 應用 S 變形：每個球面點 (x,y,z) → S @ (x,y,z)
ellipsoid = np.einsum('ij,jkl->ikl', S, unit_sphere)
# plotly Surface 渲染
```

**正確性驗證：**

- $Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I$（正交性）；
- $S Q = Q \Lambda$（特徵向量定義）；
- $\sum \lambda_p P_p = S$（譜定理）；
- `verify_P_properties` 三項都為 `True`。

##### H. 邊界情況處理

| 情況 | 偵測 | 處理 |
|---|---|---|
| $S$ 不對稱 | `np.allclose(S, S.T) == False` | UI 強制對稱連動，或彈警示「請輸入對稱矩陣」|
| 重根特徵值 | `len(set(eigvals)) < n`（容差比較）| 在重根子空間內 `np.linalg.eigh` 自動正交化，無需特殊處理 |
| 退化（$\lambda_p = 0$）| `abs(lam_p) < tol` | 譜分解仍正確，只是該項 $\lambda_p P_p = 0$；3D 橢球變扁平 |
| 負特徵值 | `lam_p < 0` | 3D 橢球該軸方向反射（紫色提示），$|\lambda_p|$ 為主軸長 |
| 全零 $S = O$ | `np.allclose(S, 0)` | 所有 $\lambda_p = 0$，分解平凡，3D 橢球縮成原點 |

##### I. 完成標準（Acceptance Criteria）

- [ ] 拉任意對稱矩陣 $S$ 的元素 → $\lambda_p, \mathbf{q}_p$ 即時更新（< 100ms）；
- [ ] 譜分解動畫流暢，每項拆解清晰可見（含 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 自外積過程）；
- [ ] 3D 橢球與單位球變形對應正確，主軸方向 = $\mathbf{q}_p$、半徑 = $|\lambda_p|$；
- [ ] $P_p$ 三性質視覺驗證正確（完備 / 正交 / 冪等都 ✓）；
- [ ] 跳轉到 ch05 VizScript-03 / ch04 VizScript-02 後參數正確帶入；
- [ ] 退化 / 負特徵值 / 重根特徵值的邊界情況都正確處理。

##### J. 反例與常見誤解

- **誤解 1：** 「只有對稱矩陣才有特徵分解。」**正解：** 任意方陣都有特徵分解 $A = X \Lambda X^{-1}$（除了部分需 Jordan 標準形的退化情形），但**只有對稱矩陣保證 $X$ 正交、$\Lambda$ 實對角、$X^{-1} = X^{\mathrm{T}}$**。EVD 的「美麗」來自對稱性的禮物；
- **誤解 2：** 「特徵值必為正。」**正解：** 對稱矩陣的特徵值是實數，但**可正可負可零**（範例 3 是一正一負）。**只有「對稱正定」才保證 $\lambda_p > 0$**（這是 PCA 用協方差矩陣的根本原因）；
- **誤解 3：** 「$Q$ 的列順序可任意。」**正解：** $Q$ 的列順序必須與 $\Lambda$ 的對角元素順序對應（$\mathbf{q}_p$ 是 $\lambda_p$ 對應的特徵向量），通常按 $\lambda_p$ 大小降冪排列（PCA 標準做法）；
- **誤解 4：** 「(P4) 三明治可以隨便用 EVD 看待。」**正解：** EVD 是 (P4) 的「自鏡像 + 對稱」特化，**不能反過來**把任意 (P4) 三明治稱為 EVD。一般 (P4) 是 SVD（§6.5），EVD 是其特殊情形。

##### K. 與其他 VizScript 的關係

- **本章 VizScript-02 / 03：** Tier 1 精簡版分別獨立處理 $P_p$ 三性質驗證和 2×2 數值範例 walkthrough；
- **ch04 VizScript-02 (MM4 秩 1 累加 + Mona Lisa SVD demo)：** 提供「秩 1 累加」的母模板。EVD 的「$\sum \lambda_p P_p$」是「對稱情境的 (MM4)」，動畫可重用；
- **ch05 VizScript-03 (P4 三明治)：** **本 VizScript 的單 pointer 目標**。EVD 是 (P4) 的「左 = 右轉置」特化，視覺布局共用「三明治」基本結構；
- **ch05 VizScript-02 (P3 動態系統)：** P3 是 $X D X^{-1}$（一般特徵分解）；EVD 的對稱版直接用 $Q D Q^{\mathrm{T}}$ 取代，動態系統 demo 可重用框架（如「對稱版動態系統」demo）；
- **ch06f VizScript-01 (SVD)：** SVD 是 EVD 的「一般化」（雙側不同正交矩陣）。**本 VizScript 的 3D 橢球視覺與 SVD 的「奇異值橢球」直接對應** — EVD 橢球是「對稱情境的 SVD 橢球」；
- **後續：** S12+ 實作時，本 VizScript 與 ch06f VizScript-01（SVD）共享 3D 橢球渲染棧，可顯著節省工時。

##### L. 配套素材清單

- **必備：** Python 3.11+、NumPy（`linalg.eigh`）、matplotlib 3D 或 plotly 3D（橢球渲染）、reactive UI 框架（marimo/streamlit）；
- **可選：** scipy.linalg（提供 `eigh_tridiagonal` 等更快的對稱矩陣特徵值算法）；
- **教學素材：** 「對稱矩陣典型例子」清單（協方差、Hessian、Gram 矩陣、二次型）每個各一張說明卡；
- **未來擴展：** 「協方差矩陣的 PCA 應用」demo（用真實資料如 Iris 資料集）、「Hessian 二次優化」demo。

##### M. 預期使用者反饋

- **「終於懂了為什麼對稱矩陣這麼特別」：** 透過 3D 橢球主軸對齊 + $Q^{\mathrm{T}} = Q^{-1}$ 的視覺對比，使用者建立「對稱性 = 雙側正交 + 計算便宜」的核心直覺；
- **「譜定理原來這麼具體」：** 譜分解的「$\sum \lambda_p P_p$ 加權累加」動畫讓抽象譜定理變成可看見的「投影 + 縮放」過程；
- **「PCA 的數學基礎終於清楚了」：** 透過協方差矩陣 EVD demo（M 段擴展），使用者理解「PCA = 對協方差矩陣做 EVD，挑前幾個最大特徵值對應的 $\mathbf{q}_p$ 作為主成分」；
- **「(P4) 三明治原來有這麼多變種」：** 透過跨章跳轉看 ch05 VizScript-03 一般 (P4) → 回 EVD 自鏡像 (P4) → 再到 ch06f SVD 雙側不同 (P4)，建立「(P4) 是 §6 後三章的共同骨架」整合視角。

---

#### VizScript-02: $P_p$ 三性質視覺驗證（精簡）

**Tier：** ⭐⭐ Tier 1（精簡 13 段）
**對應 VizMark：** Figure 6.6 VizMark-02
**預估實作工作量：** S12+ 約 0.5 session

##### A. 一句話定位

「給一個對稱矩陣 $S$，視覺化驗證投影矩陣 $P_p$ 的三條性質：完備（$\sum P_p = I$）/ 正交（$P_p P_q = O$）/ 冪等（$P_p^2 = P_p$）。」

##### B. 學習目標

- 把譜定理的抽象性質「**投影矩陣群**」變成具體的矩陣加法 / 乘法演示；
- 建立「正交基底 + 投影 = 完整覆蓋空間」的直覺。

##### C. 互動參數（精簡）

- **預設範例選擇器：** 5 個對稱矩陣（與 VizScript-01 共用）；
- **顯示模式 (radio)：** `完備性` / `正交性` / `冪等性`。

##### D-E. 視覺布局 + 動畫腳本（合併精簡）

**布局：** 上方 $S$ 矩陣 + 中間 3 個 $P_p$ 並排（每個展示 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 自外積結構）+ 底部驗證結果區。

**動畫：**
- 切換 `完備性`：3 個 $P_p$ 同時亮綠光 → 「飛」到一起加總 → 變成 $I_n$（藍色對角點，動畫 800ms）；
- 切換 `正交性`：選兩個 $P_p, P_q$（$p \neq q$）→ 計算 $P_p P_q$ 動畫 → 結果矩陣全為 0（藍灰填充 + 顯示 `= O`）；
- 切換 `冪等性`：選一個 $P_p$ → $P_p \cdot P_p$ 計算動畫 → 結果仍為 $P_p$（高亮自我複製動畫）。

##### F-M. 配色 / 計算 / 完成標準（共用 VizScript-01 規範，略）

**單一新功能：** 把 VizScript-01 的「Step 6 $P_p$ 三性質驗證」獨立成單章節，方便快速演示譜定理代數性質而不用看完整動畫。

---

#### VizScript-03: 2×2 EVD 數值範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1（輕量輪廓）
**對應 VizMark：** Figure 6.6 VizMark-03
**預估實作工作量：** S12+ 約 0.3 session

##### A. 一句話定位

「用 2×2 範例 $S = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$ 一步一步動畫展示 EVD 計算過程：求特徵值 → 求特徵向量 → 譜分解，每步顯示具體數字。」

##### B-M. 簡述

**步驟動畫：**

1. 顯示 $S = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$；
2. 計算 $\det(S - \lambda I) = (3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = 0$；
3. 求解 $\lambda = (6 \pm \sqrt{36-32})/2 = (6 \pm 2)/2$ → $\lambda_1 = 4, \lambda_2 = 2$；
4. 解 $(S - 4I)\mathbf{q}_1 = \mathbf{0}$ → $\mathbf{q}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；
5. 解 $(S - 2I)\mathbf{q}_2 = \mathbf{0}$ → $\mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
6. 驗證正交：$\mathbf{q}_1^{\mathrm{T}} \mathbf{q}_2 = 0$ ✓；
7. 組裝 $Q = \frac{1}{\sqrt{2}}\bigl[\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr]$，$\Lambda = \bigl[\begin{smallmatrix}4&0\\0&2\end{smallmatrix}\bigr]$；
8. 譜分解 $S = 4 P_1 + 2 P_2$ 計算每個 $P_p$；
9. 累加驗證 $4 \cdot \frac{1}{2}\bigl[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr] + 2 \cdot \frac{1}{2}\bigl[\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr] = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr] = S$ ✓。

**用途：** 入門教學，讓使用者第一次接觸 EVD 時看到完整計算過程的具體數字。**不含 3D 視窗、不含拖拉互動**，純步進動畫。

---

### 章末延伸

#### 與 §1–§5 的來源對應

- **§1（Viewing a Matrix）：** EVD 的「對稱性」可視為「**4 視角中行 = 列轉置**」的特例 — 對稱矩陣的列空間 = 行空間 = $\mathbf{C}(Q)$；
- **§2（Vector × Vector）：** EVD 的 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 是「自外積」（v2 視角的特例：兩個外積向量相同）；
- **§3（Matrix × Vector）：** EVD 的「$S \mathbf{q}_p = \lambda_p \mathbf{q}_p$」是「**矩陣 × 向量 = 純縮放（不轉向）**」的特殊情境，這定義了「特徵向量 = 不變方向」；
- **§4（MM4）：** 譜分解 $S = \sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 是 (MM4) 「外積之和」的特化（兩個外積向量相同 + 對稱矩陣保證項數 = 維度）；
- **§5（P4）：** **`EVD.png` 直接標 `using P4`**，EVD 是 (P4) 三明治的「自鏡像 + 對角是特徵值」特化。

#### 與 §6 其他分解的對應

- **§6.1 CR：** 對對稱 $S$ 應用 CR 得到 $C, R$，但 $C, R$ 一般不對稱；EVD 直接利用對稱性免去 CR 的「找獨立列」步驟；
- **§6.2 LU：** 對稱 $S$ 的 LU 是 $S = L D L^{\mathrm{T}}$（對稱版 LU），$L$ 下三角、$D$ 對角；EVD 比 LU **多一層正交化**（$L$ 變正交 $Q$）；
- **§6.3 QR：** QR 是「列正交化」（一般矩陣）；EVD 是「對稱矩陣的雙側正交化」。**從 QR 到 EVD = 強制 $A$ 對稱 + 把 $R$ 也正交化變對角**；
- **§6.5 SVD：** **SVD 是 EVD 的一般化** — 任意矩陣 $A$ 的 $A^{\mathrm{T}} A$ 對稱半正定 → 用 EVD 得到右奇異向量 $V$ 和奇異值平方 $\Sigma^2$；同樣 $AA^{\mathrm{T}}$ EVD 得 $U$。**SVD = 兩個 EVD 的整合**（詳見 §6.5）。

#### 工程應用前瞻（S12+ 實作目標）

- **PCA（主成分分析）：** 對協方差矩陣 $C = \frac{1}{N} X^{\mathrm{T}} X$ 做 EVD，挑前 $k$ 個最大特徵值對應的 $\mathbf{q}_p$ 作為主成分。本 VizScript-01 加 PCA demo（用 Iris 資料集，2D/3D 視覺降維過程）；
- **譜聚類（Spectral Clustering）：** 對相似度矩陣（對稱）做 EVD，用前幾個 $\mathbf{q}_p$ 作為新特徵空間的座標，再做 K-means。本章 VizScript-01 可擴展為「圖譜分析」demo；
- **二次型優化：** Hessian 矩陣 $H$ EVD → 看 $\lambda_p$ 符號判斷「凸 / 凹 / 鞍點」，看 $\mathbf{q}_p$ 方向決定下降方向。本 VizScript-01 可擴展為「優化問題的二次型可視化」demo；
- **量子力學：** 可觀測量算符 $\hat{O}$ EVD → 特徵值 = 觀測結果、特徵向量 = 對應的量子態。本章 VizScript-01 可擴展為「量子算符的譜分解」demo；
- **振動模態分析：** 結構矩陣 $K$（剛度矩陣，對稱半正定）EVD → 特徵值 = 振動頻率平方、特徵向量 = 振動模態。本章 VizScript-01 可擴展為「彈簧—質量系統的模態分解」demo。

#### 來源對照

| 元素 | 來源 |
|---|---|
| 數學公式 | `from-tex/en.md` line 430–505、`from-tex/zh.md` line 418–492 |
| 圖片 | `figs-png/EVD.png`（原始 EPS：`figs/EVD.eps`，原書 p.11）|
| Strang 連結 | LA for Everyone Sec. 6.3（對稱正定矩陣） |
| Pattern 連結 | §5 (P4) 三明治，本書 PNG 直接標 `using P4` |
| (MM4) 連結 | §4 (MM4) 外積之和，EVD 是「自外積」特化 |
| 跨章 pointer | [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（單 pointer，PNG 標 P4）/ [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)（次要 pointer，看 (MM4) 累加）|

---

## 6.5 矩陣分解 5：$A = U \Sigma V^{\mathrm{T}}$（Singular Value Decomposition / SVD）

> **原書頁碼：** p.12–p.13
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.5 $A = U\Sigma V^{\mathrm{T}}$（en.md line 507–569 / zh.md line 494–558）
> **本章圖數：** 1（`SVD.png`，原書圖中明標 **using P4**）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 1 Tier 3 / ⭐⭐⭐ × 1 Tier 2 / ⭐⭐ × 1 / ⭐ × 1）— **全書 VizMark 密度最高的章節**
> **狀態：** [x] 已完成（S09，全書最長章節 + 唯一 Tier 3 主 VizScript）

---

### 章節摘要

$A = U \Sigma V^{\mathrm{T}}$ 是 §6 五大分解的**最後一個**，也是**最重要的一個**。它是書中 Hiranabe 多次強調「**MM4 的旗艦應用**」（見 ch04 VizScript-02 母模板），也是 Strang「**Linear Algebra for Everyone**」全書的**封頂定理**（Sec. 7.1 Singular Values and Singular Vectors）。SVD 的三大特殊地位：

1. **唯一適用「任意 $m \times n$ 矩陣」的分解** — 不需方陣、不需對稱、不需正定、不需可逆、不需列獨立。**SVD 對所有矩陣都存在且唯一**（給定奇異值降冪排序後）；
2. **「最佳低秩近似定理（Eckart–Young）」的實作工具** — 取前 $k$ 個秩 1 項 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 累加，就是「在 Frobenius / 譜範數意義下最接近 $A$ 的秩 $k$ 矩陣」；
3. **「四子空間」的完美對齊工具** — $\mathbf{u}, \mathbf{v}$ 同時給出列空間 / 行空間 / 零空間 / 左零空間的正交基底（Strang 的經典「兩塊大餅」圖直接由 SVD 構造）。

**SVD 在工程實務中的「四大旗艦應用」：**

| 應用 | 用途 | SVD 角色 |
|---|---|---|
| **影像 / 資料壓縮** | 用秩 $k$ 近似節省儲存 | 取前 $k$ 個 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$，誤差由 $\sigma_{k+1}$ 控制 |
| **PCA（主成分分析）** | 降維 + 找主要變化方向 | 對置中資料 $X$ 做 SVD，$V$ 的列 = 主成分方向，$\sigma_p^2/N$ = 主成分變異 |
| **降噪 / 去模糊** | 移除小奇異值（雜訊）| 截斷 $\sigma_p < \tau$ 後重組 = 低通濾波 |
| **推薦系統 / 矩陣補全** | 用低秩結構填補缺失 | 用戶 × 產品評分矩陣的 SVD 找潛在因子（Latent Factor Model）|

**`using P4` 標記的意義（S09 PNG 重核發現）：** 原書 `SVD.png` 右下角圓圈標 `P4`（**S09 重大發現，與 EVD 同款**），明示「SVD 圖的視覺視角是 §5 Pattern 4 三明治」— 這跟 §6.4 EVD 標的也是 `using P4` 完全一致。**SVD 是 (P4) 的最一般情境** — 左側 $U$ 與右側 $V^{\mathrm{T}}$ **不同的兩個正交矩陣**（不像 EVD 強制相同），中間 $\Sigma$ 對角是非負的奇異值（不像 EVD 的特徵值可正可負）。

**本章 VizScript 策略（雙 pointer 設計，本章特例）：** 雖然 SVD PNG 標 `using P4`（按 S08 規律應單 pointer 指 ch05 P4），但 SVD 與 ch04 VizScript-02 (MM4 + Mona Lisa SVD demo) **本質同根** — 「秩 1 累加 + 低秩近似」這個視覺概念在 ch04 已實作 Mona Lisa demo，SVD 章直接是 Mona Lisa demo 的「**理論完整版**」。因此本章 VizScript-01 採**雙 pointer**：
- **主 pointer：** [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)（看 (MM4) 秩 1 累加 + Mona Lisa SVD demo 的母模板）
- **副 pointer：** [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（看 (P4) 三明治結構）

**雙 pointer 復活的判準（S09 修正 SOP §2.6 規律）：** 不只看 PNG 標記（`using XX`），也看「**內容鐵證**」 — 當該章核心 demo 與另一章已實作的旗艦 demo 同根時，可破例升級雙 pointer。**SVD 是這個判準的首例 + 全書最強烈的例子**（Mona Lisa SVD demo 就是為了 SVD 而提前在 ch04 鋪陳的）。

**對比 EVD（§6.4）— SVD 與 EVD 的關係：**

| 性質 | $S = Q\Lambda Q^{\mathrm{T}}$（EVD）| $A = U\Sigma V^{\mathrm{T}}$（SVD）|
|---|---|---|
| 矩陣限制 | 必須對稱 $S = S^{\mathrm{T}}$ | **任意 $m \times n$**（無限制）|
| 形狀 | $n \times n$ 方陣 | $m \times n$ **可長方** |
| 左側 | 正交 $Q$（$n \times n$）| 正交 $U$（$m \times m$ 或 $m \times r$）|
| 中間 | 對角 $\Lambda$（特徵值 $\lambda_p \in \mathbb{R}$）| 對角 $\Sigma$（奇異值 $\sigma_p \geq 0$）|
| 右側 | 正交 $Q^{\mathrm{T}}$（**= 左側轉置**）| 正交 $V^{\mathrm{T}}$（**與 $U$ 不同**）|
| 對角元素符號 | $\lambda_p$ 可正可負可零 | $\sigma_p$ **強制非負** |
| 與 (MM4) 連結 | $\sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$（自外積）| $\sum \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$（**一般外積**）|
| `using` 標記 | EVD 標 (P4) | SVD 標 (P4) |
| 求 $A^{-1}$ | $Q \Lambda^{-1} Q^{\mathrm{T}}$ | $V \Sigma^{-1} U^{\mathrm{T}}$（**或** Moore–Penrose 偽反 $V \Sigma^+ U^{\mathrm{T}}$）|
| 唯一性 | $\lambda_p$ 唯一（重根除外） | $\sigma_p$ 唯一（重根除外）|

**核心升級點：** 從 EVD 升級到 SVD = **解除「對稱」限制 + 把右側 $Q^{\mathrm{T}}$ 解放成獨立的 $V^{\mathrm{T}}$ + 把 $\Lambda$（可負）改成 $\Sigma$（非負）**。這是「**雙側獨立正交化的對角分解**」 — 任何矩陣都可以這樣分解。

**EVD 與 SVD 的橋梁公式（核心定理）：** 對任意 $A$：

$$
\boxed{
A^{\mathrm{T}} A = V \Sigma^{\mathrm{T}} \Sigma V^{\mathrm{T}} = V \Sigma^2 V^{\mathrm{T}}, \qquad
A A^{\mathrm{T}} = U \Sigma \Sigma^{\mathrm{T}} U^{\mathrm{T}} = U \Sigma^2 U^{\mathrm{T}}
}
$$

— 即 **$A^{\mathrm{T}} A$ 的 EVD 給出 $V$ 和 $\Sigma^2$；$AA^{\mathrm{T}}$ 的 EVD 給出 $U$ 和同樣的 $\Sigma^2$**。這就是「**SVD = 兩個對稱矩陣的 EVD 整合**」的精準描述。

數值範例（本章主貫穿，2×2 對稱版讓 SVD 退化成 EVD，方便對照 §6.4）：

$$
A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} = U \Sigma V^{\mathrm{T}}
\;=\;
\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
\begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}
\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

**驗證（對稱 $A$ 時 SVD = EVD）：** $U = V = Q$（同一個正交矩陣），$\Sigma = |\Lambda|$（取絕對值；本例 $\lambda = 3, 1$ 都正所以 $\Sigma = \Lambda$）。**這展示「對稱情境是 SVD 的特例」。**

第二範例（不對稱 2×2，展示 $U \neq V$）：

$$
A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}
$$

$$
A^{\mathrm{T}} A = \begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix}
$$

特徵值 $\lambda = 45, 5$，所以 $\sigma_1 = \sqrt{45} = 3\sqrt{5} \approx 6.708$，$\sigma_2 = \sqrt{5} \approx 2.236$。$V$ 由 $A^{\mathrm{T}} A$ 的特徵向量組成、$U$ 由 $A A^{\mathrm{T}}$ 的特徵向量組成（或用 $\mathbf{u}_p = A \mathbf{v}_p / \sigma_p$）。**$U \neq V$**（因為 $A$ 不對稱）。

第三範例（長方 3×2，展示「reduced SVD」的形狀）：

$$
A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}_{3 \times 2}
$$

$$
A^{\mathrm{T}} A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}_{2 \times 2}, \quad \lambda = 3, 1, \quad \sigma_1 = \sqrt{3}, \sigma_2 = 1
$$

Reduced SVD：$U \in \mathbb{R}^{3 \times 2}$、$\Sigma \in \mathbb{R}^{2 \times 2}$、$V^{\mathrm{T}} \in \mathbb{R}^{2 \times 2}$。**只有 $r = \operatorname{rank}(A) = 2$ 項非零秩 1 之和**：

$$
A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}} + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}}
$$

— 這是 SVD.png 直接展示的形式。

---

### 數學要點

#### 1. 定義與形狀（Full SVD vs Reduced SVD）

**Full SVD（完整版）：**

$$
A_{m \times n} = U_{m \times m} \, \Sigma_{m \times n} \, V^{\mathrm{T}}_{n \times n}
$$

- $U$：$m \times m$ 正交方陣，列為「左奇異向量」 $\mathbf{u}_1, \ldots, \mathbf{u}_m$；
- $\Sigma$：$m \times n$ 「**長方對角**」矩陣，對角元素為奇異值 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{\min(m,n)} \geq 0$，**非對角元素全為零**；
- $V$：$n \times n$ 正交方陣，列為「右奇異向量」 $\mathbf{v}_1, \ldots, \mathbf{v}_n$；
- $V^{\mathrm{T}}$：行為 $\mathbf{v}_p^{\mathrm{T}}$。

**Reduced SVD（簡化版，原書圖示用此）：**

$$
A_{m \times n} = U_{m \times r} \, \Sigma_{r \times r} \, V^{\mathrm{T}}_{r \times n}, \qquad r = \operatorname{rank}(A)
$$

- 只取「**非零奇異值對應的部分**」 — 對應的 $\mathbf{u}_p, \mathbf{v}_p$；
- 等價於 $A = \sum_{p=1}^{r} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$；
- **書中 SVD.png 是 reduced SVD**（看圖中 $U$ 是 3 列、$\Sigma$ 是 2 個藍點 = 2 個非零 $\sigma$、$V^{\mathrm{T}}$ 是 2 行）。

**選哪個？** 工程實務通常用 **reduced SVD**（節省記憶體、對應「秩 $r$ 才是有效資訊」的直覺）；理論證明常用 **full SVD**（保留 $U, V$ 的「正交方陣」性質方便代數推導）。

**可分解條件：** **任意實 $m \times n$ 矩陣**都有 SVD（無例外，包含全零矩陣 $A = O$ 也有 $\sigma_p \equiv 0$ 的平凡分解）。**這是 SVD 比所有其他分解都「親民」的根本特性**。

#### 2. SVD 的構造算法（核心 ⭐）— 兩個對稱矩陣 EVD 的整合

SVD 的存在性可以用「兩個對稱矩陣的 EVD」來證明，這也是數值計算 SVD 的基礎方法之一。

**Step 1：** 構造 $A^{\mathrm{T}} A$（$n \times n$，**對稱半正定**）。

- **對稱性：** $(A^{\mathrm{T}} A)^{\mathrm{T}} = A^{\mathrm{T}} A$ ✓（顯然）；
- **半正定：** 對任意 $\mathbf{x}$，$\mathbf{x}^{\mathrm{T}} (A^{\mathrm{T}} A) \mathbf{x} = \|A \mathbf{x}\|^2 \geq 0$ ✓。

**Step 2：** 對 $A^{\mathrm{T}} A$ 做 EVD（§6.4）：

$$
A^{\mathrm{T}} A = V \Lambda V^{\mathrm{T}}
$$

— $V$ 正交、$\Lambda$ 對角（特徵值 $\lambda_p \geq 0$ 因半正定）。**令 $\sigma_p = \sqrt{\lambda_p}$（取非負平方根，按降冪排序）。**

**Step 3：** 對非零 $\sigma_p > 0$，定義左奇異向量：

$$
\mathbf{u}_p = \dfrac{A \mathbf{v}_p}{\sigma_p}
$$

**驗證 $\mathbf{u}_p$ 正交且單位長：**

$$
\mathbf{u}_p^{\mathrm{T}} \mathbf{u}_q = \dfrac{1}{\sigma_p \sigma_q} (A \mathbf{v}_p)^{\mathrm{T}} (A \mathbf{v}_q) = \dfrac{1}{\sigma_p \sigma_q} \mathbf{v}_p^{\mathrm{T}} A^{\mathrm{T}} A \mathbf{v}_q = \dfrac{\lambda_q}{\sigma_p \sigma_q} \mathbf{v}_p^{\mathrm{T}} \mathbf{v}_q = \dfrac{\sigma_q^2}{\sigma_p \sigma_q} \delta_{pq} = \delta_{pq}
$$

— 左奇異向量自動正交且單位長 ✓。

**Step 4：** 對零奇異值 $\sigma_p = 0$，對應 $\mathbf{v}_p \in \mathbf{N}(A)$（$A$ 的零空間），$\mathbf{u}_p$ 不由公式定義，**任選一組張成 $\mathbf{N}(A^{\mathrm{T}})$（$A$ 的左零空間）的正交單位基底**填入 $U$ 的剩餘行。

**Step 5：** 組裝 $U, \Sigma, V$。

**對稱對偶（也可從 $AA^{\mathrm{T}}$ 出發）：**

$$
AA^{\mathrm{T}} = U \Sigma \Sigma^{\mathrm{T}} U^{\mathrm{T}} = U \Sigma^2 U^{\mathrm{T}}
$$

— **$AA^{\mathrm{T}}$ 的 EVD 直接給出 $U$ 和同樣的 $\sigma_p^2$**。所以 $V$ 從 $A^{\mathrm{T}} A$ 來、$U$ 從 $AA^{\mathrm{T}}$ 來。

**這個構造的視覺含義：** SVD = 「**先在 $\mathbb{R}^n$ 找一組正交方向 $\mathbf{v}_p$（讓 $A$ 把它們映射到正交方向）**」 + 「**對應的 $\mathbf{u}_p$ 自動是正交的**」+ 「**縮放因子是 $\sigma_p$**」。**SVD 找到了「$A$ 把正交映射到正交」的特殊方向組** — 一般矩陣不會把任意正交基底保持為正交，但 SVD 找到了那組「最特別的」正交基底（$\mathbf{v}_p$）使映射後仍正交（$\mathbf{u}_p$）。

#### 3. 與 (P4) 視角的連結 — 三明治結構（核心 ⭐）

**(P4) Pattern（§5）：** 「兩個矩陣夾一個對角矩陣 = 秩 1 之和（用對角元素加權）」

$$
\underbrace{U}_{\text{左側}} \underbrace{D}_{\text{對角}} \underbrace{V^{\mathrm{T}}}_{\text{右側}} = \sum_p d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**SVD 是 (P4) 的「最一般情境」** — 左側 $U$ 與右側 $V^{\mathrm{T}}$ **是兩個獨立的正交矩陣**（不像 EVD 強制 $U = V$），對角 $\Sigma$ 是非負的奇異值：

$$
A = \underbrace{U}_{\text{左 = 左奇異向量正交基底}} \underbrace{\Sigma}_{\text{對角 = 奇異值（非負降冪）}} \underbrace{V^{\mathrm{T}}}_{\text{右 = 右奇異向量正交基底（與 U 不同）}}
= \sum_p \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**對照表（SVD vs EVD vs 一般 (P4)）：**

| 元素 | (P4) 一般形式 | EVD 特化 | **SVD 完整版** |
|---|---|---|---|
| 左側 | $U$（任意） | $Q$（正交，特徵向量） | $U$（**正交，左奇異向量**） |
| 對角 | $D$（任意對角） | $\Lambda$（特徵值，可負） | $\Sigma$（**奇異值，非負降冪**） |
| 右側 | $V^{\mathrm{T}}$（任意） | $Q^{\mathrm{T}}$（左側轉置） | $V^{\mathrm{T}}$（**與 $U$ 不同的正交矩陣**） |
| 矩陣性質 | 任意 | 對稱 + 任意 | **任意（無限制）** |
| 秩 1 形式 | $\sum d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ | $\sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$（自外積） | $\sum \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$（**一般外積**） |
| 對稱性 | 無 | $S = S^{\mathrm{T}}$ | **無**（任意 $A$） |

**「using P4」標籤的意涵（與 EVD 對比）：** 原書 `SVD.png` 標 `using P4`，與 `EVD.png` 同款 — 但意義不同：
- **EVD 標 P4**：是 (P4) 的「**自鏡像 + 對角是特徵值**」特化（兩側相同）；
- **SVD 標 P4**：是 (P4) 的「**雙側獨立 + 對角是奇異值（非負）**」一般情境。

**`SVD = 完整 P4`，`EVD = 對稱 P4 特例`。** 這就是為什麼 §6.5 排在 §6.4 後面 — 一般情境放後面，特殊情境（更強限制）放前面，方便讀者「從特殊推一般」。

**連結 (MM4) — 本章雙 pointer 的「內容鐵證」：**

$$
A = \sum_{p=1}^{r} \underbrace{\sigma_p \mathbf{u}_p}_{\text{係數 × 列}} \cdot \underbrace{\mathbf{v}_p^{\mathrm{T}}}_{\text{行}} = \sum_{p=1}^{r} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

這正好是 (MM4) 「外積之和」的形式，**且是「最有意義的 (MM4)」** — 因為 $\sigma_p$ 按大小降冪排，所以「**前幾項貢獻最大、後幾項貢獻最小**」，這就是「**最佳低秩近似**」的根本（見第 5 節 Eckart–Young）。**ch04 VizScript-02 的 Mona Lisa SVD demo 就是預先實作了 SVD 章的核心視覺化** — SVD 章直接 pointer 到 ch04 即可，無須重複實作。

#### 4. 四子空間的 SVD 對齊（核心 ⭐）— Strang 兩塊大餅圖的 SVD 構造

回顧 §3 4-Subspaces：對任意 $A$ 有四個基本子空間：

- **行空間** $\mathbf{C}(A^{\mathrm{T}}) \subset \mathbb{R}^n$（維度 = $r$）；
- **零空間** $\mathbf{N}(A) \subset \mathbb{R}^n$（維度 = $n - r$）；
- **列空間** $\mathbf{C}(A) \subset \mathbb{R}^m$（維度 = $r$）；
- **左零空間** $\mathbf{N}(A^{\mathrm{T}}) \subset \mathbb{R}^m$（維度 = $m - r$）。

**SVD 直接給出四子空間的正交基底：**

| 子空間 | 維度 | SVD 正交基底 |
|---|---|---|
| 行空間 $\mathbf{C}(A^{\mathrm{T}})$ | $r$ | $\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$（**$V$ 的前 $r$ 列**）|
| 零空間 $\mathbf{N}(A)$ | $n - r$ | $\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$（**$V$ 的後 $n - r$ 列**）|
| 列空間 $\mathbf{C}(A)$ | $r$ | $\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$（**$U$ 的前 $r$ 列**）|
| 左零空間 $\mathbf{N}(A^{\mathrm{T}})$ | $m - r$ | $\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$（**$U$ 的後 $m - r$ 列**）|

**SVD 的「對齊性質」：** 對 $1 \leq p \leq r$，$A \mathbf{v}_p = \sigma_p \mathbf{u}_p$ — 這意味著 **$A$ 把 $\mathbf{v}_p$（行空間中的方向）映射到 $\sigma_p \mathbf{u}_p$（列空間中的對應方向）**。對 $p > r$，$A \mathbf{v}_p = \mathbf{0}$（$\mathbf{v}_p$ 在零空間中）。

**這是 Strang 兩塊大餅圖的精準數學表達** — SVD 的 $\mathbf{u}, \mathbf{v}$ 同時把「行空間 / 零空間」和「列空間 / 左零空間」分別正交分解，並用對角 $\sigma_p$ 連結兩側。**SVD 是「線性代數最完整的視覺定理」**，在 ch03 4-Subspaces 已有 ⭐⭐⭐ Tier 3 VizScript-02 母模板。

**對 SVD 來說有特殊意義的維度等式（rank-nullity 的 SVD 版）：**

$$
\underbrace{r}_{\text{非零 }\sigma_p \text{ 個數}} + \underbrace{(n - r)}_{\text{零 }\sigma_p \text{ 在 }V\text{ 側的個數}} = n, \qquad
r + (m - r) = m
$$

— **「奇異值的『非零個數』就是矩陣的秩 $r$」**。這是 SVD 給出 $\operatorname{rank}(A)$ 最直接、數值上最穩定的方法（比 RREF / 高斯消去都好）。

#### 5. 最佳低秩近似定理（Eckart–Young Theorem）— SVD 的旗艦應用（核心 ⭐）

**定理（Eckart–Young 1936）：** 對任意 $A_{m \times n}$，定義「**秩 $k$ SVD 截斷**」為

$$
A_k = \sum_{p=1}^{k} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}, \qquad k \leq r
$$

則 **$A_k$ 是「在 Frobenius 範數 / 譜範數意義下最接近 $A$ 的秩 $k$ 矩陣」**：

$$
\min_{\substack{B_{m \times n} \\ \operatorname{rank}(B) \leq k}} \|A - B\|_F = \|A - A_k\|_F = \sqrt{\sigma_{k+1}^2 + \sigma_{k+2}^2 + \cdots + \sigma_r^2}
$$

$$
\min_{\substack{B_{m \times n} \\ \operatorname{rank}(B) \leq k}} \|A - B\|_2 = \|A - A_k\|_2 = \sigma_{k+1}
$$

**直覺：** 「**捨棄最小的奇異值，誤差就最小**」 — 因為奇異值按降冪排，最後幾個 $\sigma_p$ 對矩陣的「能量貢獻」最少，移除它們造成的誤差最小。

**這是「**SVD 在所有應用中發揮作用的根本理由**」：**

- **影像壓縮：** 一張 $1000 \times 1000$ 影像（100 萬像素）用秩 $k = 50$ 近似，僅需儲存 $50 \cdot (1000 + 1000) = 100{,}000$ 個數（壓縮 10 倍），且視覺品質常常可接受（$\sigma_{51}$ 很小）；
- **PCA 降維：** 取前 $k$ 個 $\mathbf{v}_p$ 作為主成分，保留「方差最大」的 $k$ 個方向；
- **降噪：** 截斷小奇異值（雜訊集中在小 $\sigma_p$）即可去噪；
- **推薦系統：** 用低秩 $A_k$ 補全用戶 × 產品評分矩陣（Matrix Factorization）。

**Eckart–Young 證明大綱：** 用 $\|A - B\|_F^2 = \operatorname{tr}((A-B)^{\mathrm{T}}(A-B))$ + 推導 $B$ 的最佳形式必為 $A$ 的 SVD 截斷 + 用奇異值的「極值性質」 $\sigma_k = \min_{\dim S = m - k + 1} \max_{\mathbf{x} \in S, \|\mathbf{x}\|=1} \|A\mathbf{x}\|$。詳細證明見 Strang 7.2 或 Trefethen & Bau Lecture 5。

**這個定理對 ch04 VizScript-02 (Mona Lisa SVD demo) 是「靈魂」** — Mona Lisa 從 $k = 1, 2, 5, 10, 20, 50$ 依序顯示，每個 $k$ 都是「**最佳秩 $k$ 近似**」（不是隨意的低秩矩陣）。**SVD 章 VizScript-01 直接 pointer 到 ch04 看 Mona Lisa demo**，無須重複實作。

#### 6. SVD 的四大旗艦應用詳解（本章獨有，全書最豐富的應用章）

##### 6.1 影像 / 資料壓縮

**核心想法：** 影像（灰階）= $m \times n$ 矩陣，每個元素是像素亮度。對影像做 SVD，取前 $k$ 個秩 1 項組合 = 「**用 $k$ 個「特徵圖案」線性組合表達整張圖**」。

**儲存比較：**

- 原始：$m \times n$ 個數（如 $1000 \times 1000 = 10^6$）；
- 秩 $k$ 近似：$k(m + n) + k$ 個數（$U$ 的前 $k$ 列 + $V$ 的前 $k$ 列 + $k$ 個 $\sigma_p$）；
- **壓縮比 $\approx mn / (k(m+n))$**，當 $k \ll \min(m,n)$ 時壓縮極顯著。

**典型範例：** Mona Lisa $400 \times 250$ 像素 = 10 萬。秩 $k = 20$ 重建：$20 \cdot 650 + 20 = 13{,}020$，壓縮約 7.7 倍，視覺品質可接受（**詳見 ch04 VizScript-02 Mona Lisa demo**）。

##### 6.2 PCA（主成分分析）

**核心想法：** 給一筆資料 $X_{N \times d}$（$N$ 筆樣本、$d$ 個特徵），先「**置中**」（每行減平均）得 $\tilde{X}$，對 $\tilde{X}$ 做 SVD：

$$
\tilde{X} = U \Sigma V^{\mathrm{T}}
$$

**$V$ 的列（前 $k$ 個 $\mathbf{v}_p$）= 主成分方向。** 每個主成分對應的「方差貢獻」為 $\sigma_p^2 / N$。

**降維：** $\tilde{X}_{N \times d} \to \tilde{X} V_k = U_k \Sigma_k$（$N \times k$ 矩陣，每筆樣本變 $k$ 維）。

**為什麼用 SVD 不用直接對 $\tilde{X}^{\mathrm{T}} \tilde{X}$ 做 EVD？** 因為當 $N$ 很大時，$\tilde{X}^{\mathrm{T}} \tilde{X}$ 計算昂貴且數值不穩；SVD 直接對 $\tilde{X}$ 做（不算 $\tilde{X}^{\mathrm{T}} \tilde{X}$），數值穩定且效率更高。**現代 PCA 演算法都用 SVD。**

**經典應用：** 人臉識別（Eigenfaces）、基因表達分析、金融資料降維、特徵工程。

##### 6.3 降噪 / 去模糊

**核心想法：** 假設「**訊號集中在大奇異值對應的方向、雜訊集中在小奇異值對應的方向**」，截斷小奇異值即可降噪。

**算法：**

1. 對含雜訊的訊號 $A_{\text{noisy}}$ 做 SVD；
2. 設定閾值 $\tau$（如 $\tau = 0.01 \cdot \sigma_1$ 或用 Stein 不偏估計）；
3. 截斷：$A_{\text{denoised}} = \sum_{p: \sigma_p > \tau} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$；
4. （或軟閾值）替換每個 $\sigma_p \to \max(\sigma_p - \tau, 0)$。

**應用：** 影像降噪、地震訊號分離、語音降噪、生醫訊號（EEG/ECG）去人造干擾。

##### 6.4 推薦系統 / 矩陣補全

**核心想法：** 用戶 × 產品評分矩陣 $A_{N \times M}$（$N$ 個用戶、$M$ 個產品）通常**極度稀疏**（大部分用戶沒看過大部分產品 → 缺失值）。假設「**用戶喜好可由少數潛在因子（latent factors）描述**」 → 完整矩陣是低秩的。

**算法（Latent Factor Model）：**

1. 對已知評分位置做正則化最佳化 $\min \|P_{\Omega}(A - U \Sigma V^{\mathrm{T}})\|_F^2 + \lambda(\|U\|_F^2 + \|V\|_F^2)$；
2. 解得低秩近似 $A \approx U_k \Sigma_k V_k^{\mathrm{T}}$；
3. **預測缺失評分：** $A_{ij} \approx (U_k \Sigma_k V_k^{\mathrm{T}})_{ij}$（用 $i$ 用戶的 $k$ 維潛在因子 + $j$ 產品的 $k$ 維潛在因子內積）。

**經典案例：** Netflix Prize（2006–2009，獎金 100 萬美元）的核心解法之一就是 SVD 變體。

#### 7. $A = U\Sigma V^{\mathrm{T}}$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **SVD ↔ CR** | CR 給出列空間基底 $C$，但 $C$ 不一定正交；SVD 直接給出**正交**列空間基底 $U_{[:, :r]}$。**SVD 是 CR 的「正交化升級版」**且唯一適用任意矩陣 |
| **SVD ↔ LU** | LU 解 $A\mathbf{x} = \mathbf{b}$ 用兩步反代（限方陣 + 主元）；SVD 解 $A\mathbf{x} = \mathbf{b}$ 用 $\mathbf{x} = V \Sigma^{+} U^{\mathrm{T}} \mathbf{b}$（**Moore–Penrose 偽反**，**任意矩陣**都可解，給出最小二乘解） |
| **SVD ↔ QR** | QR 是「列正交化」（限列獨立）；SVD 是「**雙側正交化**」（任意矩陣）。**從 QR 到 SVD = 把 $R$ 也正交化變對角 $\Sigma$**。實務上**奇異值計算的標準算法是「先 QR 化簡，再 EVD」** — QR 是 SVD 計算的中間步驟 |
| **SVD ↔ EVD** | **SVD 是 EVD 的「一般化」** — EVD 限對稱、$U = V$；SVD 任意矩陣、$U \neq V$。對任意 $A$：$A^{\mathrm{T}} A$ EVD 給 $V, \Sigma^2$；$AA^{\mathrm{T}}$ EVD 給 $U, \Sigma^2$。**SVD = 兩個對稱半正定矩陣 EVD 的整合** |

**結論：** $A = U\Sigma V^{\mathrm{T}}$ 是「**任意矩陣的雙側獨立正交對角化**」 — 是五大分解中最一般、最完整、最重要的一個。沿著「正交化逐步加強 + 限制逐步解除」的階梯看：

$$
\underbrace{CR}_{\text{0 側正交}} \;\to\; \underbrace{LU}_{\text{0 側正交 + 三角}} \;\to\; \underbrace{QR}_{\text{1 側正交 + 三角}} \;\to\; \underbrace{Q\Lambda Q^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角}\\\text{（限對稱，鏡像）}}} \;\to\; \underbrace{U\Sigma V^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角}\\\text{（任意矩陣，獨立）}}}
$$

**SVD 是這個階梯的「終點」 — 結構最強（雙側正交 + 對角）+ 適用最廣（任意矩陣）+ 最佳低秩近似（Eckart–Young）+ 四子空間對齊（Strang 兩塊大餅）+ 工程應用最多（壓縮 / PCA / 降噪 / 推薦）。**

#### 8. 數學要點總結（一張表）

| 性質 | $A = U\Sigma V^{\mathrm{T}}$ 的對應 |
|---|---|
| 適用矩陣 | **任意實 $m \times n$ 矩陣**（無限制，包含全零、長方、不可逆） |
| $U$ 的結構 | $m \times m$（full）或 $m \times r$（reduced）正交矩陣，列為左奇異向量 $\mathbf{u}_p$，$U^{\mathrm{T}} U = I$ |
| $\Sigma$ 的結構 | $m \times n$（full）或 $r \times r$（reduced）「**長方對角**」矩陣，對角為非負奇異值 $\sigma_1 \geq \cdots \geq \sigma_r > 0$（之後皆 0） |
| $V$ 的結構 | $n \times n$（full）或 $r \times n$（reduced）正交矩陣，列為右奇異向量 $\mathbf{v}_p$，$V^{\mathrm{T}} V = I$ |
| 項數 | $r = \operatorname{rank}(A) \leq \min(m, n)$（reduced）或 $\min(m, n)$（full，含零項）|
| 構造方法 | 對 $A^{\mathrm{T}} A$（或 $AA^{\mathrm{T}}$）做 EVD → 取 $\sqrt{\lambda_p}$ 為 $\sigma_p$ → 用 $\mathbf{u}_p = A\mathbf{v}_p / \sigma_p$ 互推；數值上用「Golub–Reinsch」或「one-sided Jacobi」算法 |
| §4 (MM4) 對應 | $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$（**完整 (MM4) 形式 + 奇異值降冪排序**）|
| §5 Pattern 對應 | **`SVD.png` 標 `using P4`**：(P4) 三明治的「雙側獨立正交 + 對角非負」一般情境 |
| 求 $A^{-1}$（方陣可逆） | $A^{-1} = V \Sigma^{-1} U^{\mathrm{T}}$（對角倒數，前提 $\sigma_p > 0$）|
| 求 Moore–Penrose 偽反 | $A^{+} = V \Sigma^{+} U^{\mathrm{T}}$（**任意矩陣**，$\Sigma^{+}$ 對非零 $\sigma_p$ 取倒數，零保持）|
| 最佳秩 $k$ 近似 | $A_k = \sum_{p \leq k} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$，誤差 $\|A - A_k\|_F = \sqrt{\sum_{p > k} \sigma_p^2}$ |
| 四子空間 | $\mathbf{C}(A^{\mathrm{T}}) = \operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$，$\mathbf{N}(A) = \operatorname{span}\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$，$\mathbf{C}(A) = \operatorname{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$，$\mathbf{N}(A^{\mathrm{T}}) = \operatorname{span}\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$ |
| 計算量 | $O(\min(mn^2, m^2 n))$（標準算法）；隨機化 SVD $O(mn k)$（取前 $k$ 個）|

---

### 圖片詳細描述（Figure Descriptions）

#### Figure 6.7: $A = U\Sigma V^{\mathrm{T}}$ — 標 using P4

**圖檔：** `docs/book/figs-png/SVD.png`（原始 EPS：`figs/SVD.eps`）
**原書頁碼：** p.12 圖 17
**所屬章節：** §6.5 $A = U\Sigma V^{\mathrm{T}}$（**唯一一張**，無對偶圖；reduced SVD 形式）
**圖中標記：** **`using P4`**（圓圈標，右下角）

##### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，3×2 長方矩陣示意（reduced SVD），共 8 段：

1. **第 1 段：** 矩陣 $A$ 的方框（內含**淺灰色塊**，**長方形 3 列 × 2 行**）— 上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $U$（方框內 **3 條等寬綠色直立列，每列底部標 `1`/`2`/`3`**，呈 3×2 長方形）— 上方有大字 `U`；綠色 = 「正交且單位長」視覺信號；**注意是 3×2（reduced）不是 3×3（full）**；
4. **第 4 段：** 矩陣 $\Sigma$（方框內 **2 個藍色圓點沿對角線排列**，2×2 方形，非對角位置完全留白）— 上方有大字 $\Sigma$；**藍點明示「$\Sigma$ 是對角」+ 只有 2 個非零（對應 $r = 2$）**；
5. **第 5 段：** 矩陣 $V^{\mathrm{T}}$（方框內 **2 條等寬粉紅色橫躺行，每行左側標 `1`/`2`**，2×2 方形）— 上方有大字 $V^{\mathrm{T}}$；**粉紅色 = 行視角 + 「與 $U$ 不同」的視覺信號**（與 $U$ 綠色形成對比）；
6. **第 6 段：** 等號 `=`；
7. **第 7–8 段：** 拆解結果，**2 個方框並排，每個都標 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$**：
   - 第 7 段：$\sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}}$ — 方框內含 **1 條綠色直立列（標 `1`）+ 上方淡粉紅橫躺行（標 `1`）**，藍點標 $\sigma_1$；
   - 第 8 段：加號 `+`；$\sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}}$ — **同樣結構，標 `2`**；
8. **右下角圖示：** 圓圈內標 `P4`，文字 `using` — **直接標明「本圖用 §5 Pattern 4 視角」**。

**「綠列 + 粉紅行」對比布局的視覺意義：** 與 EVD 圖（兩側都用綠色）形成鮮明對比 — SVD 的兩側用**不同顏色**，視覺上明確展示「**$U$ 和 $V$ 是兩個不同的正交矩陣**」。**這是 SVD 與 EVD 的視覺指紋差異**：EVD 兩側是「自鏡像」（同色），SVD 兩側是「獨立配對」（異色）。

**閱讀順序：** 由左到右讀整個等式鏈 `A = U Σ V^T = (兩個 σ_p u_p v_p^T 累加)`。重點掃右側的 2 個拆解項，注意「**綠列 + 粉紅行對偶布局 + 藍點 σ_p 加權**」。**reduced SVD 的「項數 = 秩」直觀展示** — 圖中只有 2 項，因為 $r = 2$。

##### 數學內容 (Mathematical Content)

對應數學表示（**(P4) Pattern 4** 三明治視角，雙側獨立正交特化版）：

$$
A = U \Sigma V^{\mathrm{T}}
= \begin{bmatrix} | & | & | \\ \mathbf{u}_1 & \mathbf{u}_2 & \mathbf{u}_3 \\ | & | & | \end{bmatrix}
\begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \\ 0 & 0 \end{bmatrix}
\begin{bmatrix} - & \mathbf{v}_1^{\mathrm{T}} & - \\ - & \mathbf{v}_2^{\mathrm{T}} & - \end{bmatrix}
$$

或（reduced 形式，省略 $\mathbf{u}_3$ 對應的 0 列）：

$$
A = \begin{bmatrix} | & | \\ \mathbf{u}_1 & \mathbf{u}_2 \\ | & | \end{bmatrix}
\begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{bmatrix}
\begin{bmatrix} - & \mathbf{v}_1^{\mathrm{T}} & - \\ - & \mathbf{v}_2^{\mathrm{T}} & - \end{bmatrix}
= \sum_{p=1}^{2} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**關鍵數值關係（對任意 $A$）：**

- $A^{\mathrm{T}} A \mathbf{v}_p = \sigma_p^2 \mathbf{v}_p$（$\mathbf{v}_p$ 是 $A^{\mathrm{T}} A$ 的特徵向量）；
- $A A^{\mathrm{T}} \mathbf{u}_p = \sigma_p^2 \mathbf{u}_p$（$\mathbf{u}_p$ 是 $A A^{\mathrm{T}}$ 的特徵向量）；
- $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$（**SVD 的對齊性質**）；
- $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$（非負降冪排序）；
- $\operatorname{rank}(A) = r = $ 非零 $\sigma_p$ 的個數。

**從 $A$ 提取 $(\sigma_p, \mathbf{u}_p, \mathbf{v}_p)$：** 對 $A^{\mathrm{T}} A$ 做 EVD（§6.4 算法）→ 取平方根 → 用 $\mathbf{u}_p = A\mathbf{v}_p / \sigma_p$ 互推。

##### 直覺解讀 (Intuition)

SVD 圖傳達五層核心訊息：

1. **「雙側獨立 = SVD 的核心」直覺：** $U$（綠列）和 $V^{\mathrm{T}}$（粉紅行）用**不同顏色**展示，視覺上立刻看出「**兩側是兩個獨立的正交矩陣**」。**這是 SVD 與 EVD 的最大差異** — EVD 兩側是同一個 $Q$，SVD 兩側是獨立的 $U, V$；

2. **「對角 $\Sigma$ = 純縮放 + 非負」直覺：** 中間的 2 個藍點沿對角排列，**只有 2 個（不是 3 個）** — 視覺上明示「**reduced SVD 只取非零奇異值**」+ 「奇異值都 $\geq 0$（不像特徵值可負）」+ 「降冪排序（從大到小）」；

3. **「秩 1 拆解 = (MM4) 的最有意義版」直覺：** 右側 2 個拆解項使用**綠列 × 粉紅行**（不同色），視覺上強調「**一般外積 $\mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$**」（與 EVD 自外積 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 對比）。**且兩項按 $\sigma_p$ 降冪排，第 1 項貢獻最大（最佳秩 1 近似）**；

4. **「項數 = 秩」直覺：** 圖中只有 2 項拆解（不是 3 項），直接展示「**SVD 的非零項數 = 矩陣的秩**」。**這是 SVD 給 $\operatorname{rank}(A)$ 最直觀的方法**；

5. **「reduced SVD 適配長方陣」直覺：** $A$ 是 3×2 長方陣，reduced SVD 把 $U$ 也設為 3×2、$V$ 設為 2×2，整個分解在「**有效維度 = 秩 $r$**」下進行，不浪費儲存空間。

**「using P4」標籤的重要性（S09 PNG 重核確認）：** 原書作者刻意把這張圖標 `using P4`，與 §6.4 EVD 同款 — 等於明說「**SVD 圖跟 EVD 圖是同一種視角（(P4) 三明治），只是 SVD 雙側獨立、EVD 雙側同一**」。視覺化可以**直接重用 [ch05 VizScript-03](ch05-patterns.md#vizscript-03) 的 P4 三明治互動**（單 pointer 副線），但因「秩 1 累加 + 低秩近似」與 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) Mona Lisa SVD demo 完全同根，**主 pointer 採雙 pointer 設計指 ch04**。

**為什麼這張圖該做成互動視覺化？** 因為 SVD 是「**全書理論的封頂 + 工程應用最多**」：
- 「秩 1 累加」過程展示「**為何前幾項最重要**」（Eckart–Young 直覺）；
- 「**4 應用切換**」（壓縮 / PCA / 降噪 / 推薦）讓使用者理解 SVD 的實際用途；
- 「**4 子空間視覺**」（與 ch03 4-Subspaces 整合）展示 Strang 兩塊大餅圖的 SVD 構造；
- 「**2D 變形動畫**」（單位圓 → 橢圓）展示 SVD 的幾何直覺：$A = (\text{旋轉}) (\text{縮放}) (\text{旋轉})$。

靜態圖只能展示最終結果，**互動 demo 可以展示「**使用者調 $A$ → 即時更新 4 種應用 + 4 子空間 + 2D/3D 幾何**」**，這是 SVD 教學的關鍵突破點，也是**全書最值得實作 Tier 3 的 VizScript**（見 VizMark-01）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [SVD 完整互動 + 4 應用切換] ⭐⭐⭐ Tier 3
> 「全書旗艦 VizScript：拉桿調 $A$ → 即時 SVD → 4 應用切換（壓縮 / PCA / 降噪 / 推薦）+ 2D/3D 幾何（單位圓 → 橢圓）+ 4 子空間視覺整合 ch03 兩塊大餅圖 + Mona Lisa 低秩近似 demo（雙 pointer 指 ch04 Mona Lisa）」
> **詳見劇本：** VizScript-01（章末，Tier 3 全書最強）

> 🎬 **VizMark-02** [奇異值降冪 + Eckart–Young 視覺] ⭐⭐⭐ Tier 2
> 「Bar chart 顯示 $\sigma_1 \geq \sigma_2 \geq \cdots$ + 累計能量曲線 $\sum_{p \leq k} \sigma_p^2 / \sum \sigma_p^2$ + 滑桿選 $k$ 看截斷誤差 → 視覺化 Eckart–Young 定理」
> **詳見劇本：** VizScript-02（章末）

> 🎬 **VizMark-03** [4 子空間 SVD 構造] ⭐⭐
> 「整合 ch03 4-Subspaces 兩塊大餅圖 + SVD 直接給 $\mathbf{u}_p, \mathbf{v}_p$ 作為基底 + 動畫展示 $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$ 對齊性質」
> **詳見劇本：** VizScript-03（章末，精簡版）

> 🎬 **VizMark-04** [2×2 SVD walkthrough] ⭐
> 「用 2×2 範例 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$ 一步一步動畫展示 SVD 計算過程，每步顯示具體數字」
> **詳見劇本：** VizScript-04（章末，輕量版）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: SVD 完整互動 + 4 應用切換（SVD Master Interactive — Tier 3）

**Tier：** ⭐⭐⭐ **Tier 3（全書最強規格，與 ch04 VizScript-02 同級）**
**對應 VizMark：** Figure 6.7 VizMark-01
**預估實作工作量：** S12+ 約 **3 session**（畫面框架 1 session + 4 應用切換 1 session + 4 子空間 + 2D/3D 幾何 1 session）

##### A. 一句話定位

「給一個 $A$（$m \times n$，$m, n \in [2, 6]$），即時計算 SVD → 動態展示秩 1 累加 → 4 個應用切換（壓縮 / PCA / 降噪 / 推薦）+ 2D/3D 幾何（單位圓 → 橢圓）+ 4 子空間視覺，**整合全書所有核心概念**。」

##### B. 學習目標（Learning Outcome）

- **SVD 直覺：** 看到任何矩陣，能在腦中想像「**雙側正交基底 + 對角縮放**」的幾何圖景；
- **奇異值降冪意義：** 看到 $\sigma_p$ 大小與秩 1 項貢獻的對應，建立「**取前 $k$ 項 = 最佳低秩近似**」直覺；
- **4 應用具體化：** 透過 4 個獨立 demo 看到 SVD 在「**壓縮 / PCA / 降噪 / 推薦**」中的具體用法；
- **4 子空間整合：** 透過與 ch03 4-Subspaces 的整合視覺，理解「**SVD 是 Strang 兩塊大餅圖的構造工具**」；
- **2D 幾何直覺：** 單位圓被 $A$ 變成橢圓，主軸方向 = $\mathbf{u}_p$、半徑 = $\sigma_p$；
- **跨章連結（雙 pointer）：** 點 (P4) 跳 ch05 看一般三明治 / 點 (MM4) 跳 ch04 看 Mona Lisa demo。

##### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $m \times n$ 格子網格，$m, n \in [2, 6]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr]$（**對稱 2×2，SVD = EVD 退化情境，方便對照 §6.4**）；
  - 範例 2：$\bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$（**Strang 經典 2×2，$\sigma = 3\sqrt{5}, \sqrt{5}$**）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&1\\1&0\\0&1\end{smallmatrix}\bigr]$（**3×2 長方，reduced SVD，書中圖示同形**）；
  - 範例 4：$\bigl[\begin{smallmatrix}1&2&3\\2&4&6\end{smallmatrix}\bigr]$（**rank = 1 退化，只有 1 個非零 $\sigma$**）；
  - 範例 5：$I_3$（單位矩陣，所有 $\sigma_p = 1$，$U = V = I$）；
  - 範例 6：Mona Lisa $400 \times 250$（**真實影像，跳轉到 ch04 Mona Lisa demo**）；
  - 範例 7：Iris 資料集（150×4，**PCA 應用**）；
- **應用模式切換 (主 radio，本 VizScript 核心)：**
  - `基礎 SVD`（純秩 1 累加 + 4 子空間視覺）；
  - `應用 1：壓縮`（連到 Mona Lisa demo）；
  - `應用 2：PCA`（用範例 7 Iris 資料）；
  - `應用 3：降噪`（生成含雜訊訊號 → SVD 截斷）；
  - `應用 4：推薦系統`（生成稀疏評分矩陣 → 矩陣補全）；
- **顯示模式切換 (checkbox 多選)：**
  - `顯示 4 子空間`（整合 ch03 兩塊大餅圖）；
  - `顯示 2D/3D 幾何`（單位圓 → 橢圓動畫）；
  - `顯示秩 $k$ 截斷`（滑桿 $k \in [1, r]$）；
  - `顯示奇異值 bar chart`（含累計能量）；
- **跳轉按鈕（雙 pointer 設計，本 VizScript 全書唯一）：**
  - 「→ (MM4) 秩 1 累加 / Mona Lisa」按鈕（**主 pointer**，跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)）；
  - 「→ (P4) 三明治結構」按鈕（**副 pointer**，跳 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)）；
  - 「→ 4 子空間（ch03）」按鈕（跳 [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02)）；
  - 「→ 對稱情境 EVD」按鈕（跳 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)）。

##### D. 視覺布局（Layout）

**主畫面**（Tier 3 規格，分區更密）：

| 區 | 內容 |
|---|---|
| 左上區（輸入 + 範例） | $A$ 的格子輸入網格 + 範例選擇器 + 應用模式 radio |
| 中上區（SVD 矩陣分解） | $A, U, \Sigma, V^{\mathrm{T}}$ 四矩陣並排 + 秩 1 拆解項列下方 |
| 右上區（2D/3D 幾何） | 單位圓 → 橢圓變形動畫 + 主軸方向 $\mathbf{u}_p$（綠箭頭）+ 半徑 $\sigma_p$ |
| 左下區（奇異值 bar chart） | 縱軸 $\sigma_p$、橫軸 $p$ + 累計能量曲線 |
| 中下區（應用 demo 切換） | 依當前應用 mode 顯示：Mona Lisa（壓縮）/ Iris 散點圖（PCA）/ 訊號波形（降噪）/ 評分矩陣（推薦） |
| 右下區（4 子空間視覺，可選） | ch03 兩塊大餅圖 + SVD 給的 $\mathbf{u}_p, \mathbf{v}_p$ 標基底 |

**底部資訊條：**

- 當前的 $\sigma_p, \mathbf{u}_p, \mathbf{v}_p$ 數值（小字滾動）；
- 「**SVD 驗證：$U\Sigma V^{\mathrm{T}} = A$**」綠色 ✓；
- 「**Eckart–Young 驗證：$\|A - A_k\|_F = \sqrt{\sum_{p > k} \sigma_p^2}$**」綠色 ✓（hover 顯示具體數字）；
- **跳轉按鈕區**（4 個橫向按鈕：→ MM4 / → P4 / → 4-Subspaces / → EVD）。

##### E. 動畫腳本（Storyboard）

**Step 1（0–500ms，啟動）：** $A$ 從左上區滑入中上區，後台計算 $A^{\mathrm{T}} A$ 和 $AA^{\mathrm{T}}$ 的 EVD（顯示「Computing SVD…」進度條）。

**Step 2（500–2000ms，SVD 構造）：** $V$ 從 $A^{\mathrm{T}} A$ EVD 滑入右側、$\Sigma^2$ 滑入中間、$U$ 從 $AA^{\mathrm{T}}$ EVD 滑入左側；
- $\Sigma$ 顯示為對角藍點（按降冪排序，最大 $\sigma_1$ 在左上）；
- 公式區依序顯示 $A^{\mathrm{T}} A = V\Sigma^2 V^{\mathrm{T}}$、$AA^{\mathrm{T}} = U\Sigma^2 U^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$；
- 2D/3D 幾何區：單位圓淡入（灰色）→ 同步顯示 $A$ 變形成橢圓（金色，主軸 = $\mathbf{u}_p$ 方向、半徑 = $\sigma_p$）。

**Step 3（2000–4000ms，秩 1 累加動畫，類 ch04 VizScript-02 母模板）：**
- 第 1 項 $\sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}}$ 高亮 → 從 $U, \Sigma, V^{\mathrm{T}}$ 取出對應行列「飛」到下方拆解項位置；
- 累計部分和 $A^{(1)}$ 顯示在右側，**同步更新 2D/3D 幾何**（橢圓 → 一條線，沿 $\mathbf{u}_1$ 方向長 $\sigma_1$）；
- 顯示誤差條 $\|A - A^{(1)}\|_F$；
- 重複 Step 3 對 $p = 2, 3, \ldots, r$；
- 最終 $A^{(r)} = A$，誤差條變 0 ✓。

**Step 4（4000–5000ms，奇異值 bar chart 強調）：**
- bar chart 從左下區滑入，每個 $\sigma_p$ 對應一根藍色長條；
- 同步顯示「累計能量曲線」$\sum_{p \leq k} \sigma_p^2 / \sum \sigma_p^2$（紅色折線）；
- 滑桿 $k$ 出現在 chart 下方，使用者可拉動看截斷效果。

**Step 5（按 `應用 1：壓縮`）：**
- 中下區切換為 Mona Lisa 影像（從 ch04 VizScript-02 重用，雙 pointer 體現）；
- 滑桿選 $k$，影像即時更新為秩 $k$ 重建版本；
- 顯示壓縮比 $mn / (k(m+n))$ 與誤差 $\|A - A_k\|_F / \|A\|_F$；
- **「→ Mona Lisa 詳細 demo」按鈕**（跳 ch04 VizScript-02）。

**Step 6（按 `應用 2：PCA`）：**
- 中下區切換為 Iris 資料散點圖（4D → 2D 降維）；
- 顯示 $V$ 的前 2 列作為主成分方向；
- 滑桿選保留主成分數 $k$，散點圖即時投影到前 $k$ 個主成分空間；
- 顯示「方差貢獻」$\sigma_p^2 / N$；
- 三類 Iris（setosa / versicolor / virginica）用三色標示，**清楚展示 PCA 後類別仍可分離**。

**Step 7（按 `應用 3：降噪`）：**
- 中下區切換為含雜訊訊號（如雜訊正弦波 + 隨機矩陣表示 spectrogram）；
- 滑桿選閾值 $\tau$，截斷小於 $\tau$ 的奇異值；
- 同步顯示「原始 vs 降噪」並排對比；
- 顯示信噪比改善（SNR 改進）。

**Step 8（按 `應用 4：推薦系統`）：**
- 中下區切換為稀疏評分矩陣（用戶 × 電影，灰色 = 缺失、彩色 = 已知評分）；
- 滑桿選潛在因子數 $k$，運行矩陣補全演算法；
- 顯示「補全後預測」與「測試集 RMSE」；
- 列出「為使用者推薦的前 5 部電影」。

**Step 9（按 `顯示 4 子空間`）：**
- 右下區從 ch03 整合兩塊大餅圖（已實作的 ch03 VizScript-02 重用）；
- 把 $V$ 的前 $r$ 列標為「行空間正交基底」、$V$ 的後 $n-r$ 列標為「零空間正交基底」；
- 把 $U$ 的前 $r$ 列標為「列空間正交基底」、$U$ 的後 $m-r$ 列標為「左零空間正交基底」；
- 動畫 $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$（**對齊性質**）：左圓上 $\mathbf{v}_p$ 經 $A$ 映射到右圓上 $\sigma_p \mathbf{u}_p$。

**Step 10（互動結束）：** 「**→ Mona Lisa 詳細 demo**」「**→ 對稱情境 EVD**」「**→ P4 一般三明治**」「**→ 4 子空間**」四個按鈕高亮，鼓勵跨章探索。

##### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $\mathbf{u}_p$ / $U$ 的列 / 列空間 / 2D 橢圓主軸；
- **粉紅 / 紅 `#d62728`：** $\mathbf{v}_p^{\mathrm{T}}$ / $V^{\mathrm{T}}$ 的行 / 行空間（與 $U$ 綠色形成對比，**SVD 雙側獨立的視覺指紋**）；
- **灰 `#cccccc`：** 原始單位圓 / 對稱輸入 $A$ 的方框 fill / 補全前缺失值；
- **金 `#FFD700`：** 變形後的橢圓 / 當前正在處理的項；
- **藍 `#1f77b4`：** $\Sigma$ 的對角元素（藍點，bar chart 的長條）/ 已知評分（推薦系統）；
- **紫 `#9467bd`：** 退化警示（rank 不足）/ 4 子空間中的「零空間方向」；
- **橙 `#ff7f0e`：** 秩 $k$ 截斷曲線 / Iris 資料 versicolor 類；
- **多類別調色盤（PCA 三色）：** 設色（setosa）藍 / 變色（versicolor）橙 / 維色（virginica）綠。

##### G. 計算邏輯（Numerical Backend）

```python
def svd_with_history(A: np.ndarray) -> dict:
    """Full SVD + step-by-step history for animation."""
    U, sigma, Vt = np.linalg.svd(A, full_matrices=False)  # reduced SVD
    r = sum(sigma > 1e-10)  # numerical rank
    history = []
    A_partial = np.zeros_like(A, dtype=float)
    for p in range(len(sigma)):
        u_p = U[:, p:p+1]
        v_p = Vt[p:p+1, :]
        rank1 = sigma[p] * u_p @ v_p
        A_partial = A_partial + rank1
        history.append({
            'p': p + 1,
            'sigma_p': float(sigma[p]),
            'u_p': u_p.flatten().tolist(),
            'v_p': v_p.flatten().tolist(),
            'rank1': rank1.tolist(),
            'A_partial': A_partial.tolist(),
            'error_fro': float(np.linalg.norm(A - A_partial, 'fro')),
            'energy_cumulative': float(np.sum(sigma[:p+1]**2) / np.sum(sigma**2)),
        })
    return {'U': U, 'sigma': sigma, 'Vt': Vt, 'rank': r, 'history': history}


def four_subspaces(A: np.ndarray, tol: float = 1e-10) -> dict:
    """Return SVD-based orthonormal bases for the four fundamental subspaces."""
    U, sigma, Vt = np.linalg.svd(A, full_matrices=True)
    r = sum(sigma > tol)
    return {
        'row_space': Vt[:r].T,        # C(A^T): first r columns of V
        'null_space': Vt[r:].T,       # N(A): last n-r columns of V
        'col_space': U[:, :r],        # C(A): first r columns of U
        'left_null_space': U[:, r:],  # N(A^T): last m-r columns of U
        'rank': r,
    }


def pca(X: np.ndarray, k: int) -> dict:
    """Standard PCA via SVD (assumes X is N x d, rows = samples)."""
    X_centered = X - X.mean(axis=0)
    U, sigma, Vt = np.linalg.svd(X_centered, full_matrices=False)
    components = Vt[:k].T  # d x k, columns = principal directions
    explained_variance = sigma[:k]**2 / X.shape[0]
    projection = X_centered @ components  # N x k
    return {
        'components': components,
        'explained_variance': explained_variance,
        'projection': projection,
        'sigma': sigma,
    }


def low_rank_approx(A: np.ndarray, k: int) -> tuple[np.ndarray, float]:
    """Eckart-Young best rank-k approximation."""
    U, sigma, Vt = np.linalg.svd(A, full_matrices=False)
    A_k = U[:, :k] @ np.diag(sigma[:k]) @ Vt[:k]
    error_fro = float(np.linalg.norm(A - A_k, 'fro'))
    return A_k, error_fro


def denoise_svd(A_noisy: np.ndarray, threshold: float) -> np.ndarray:
    """Hard-threshold denoising via SVD truncation."""
    U, sigma, Vt = np.linalg.svd(A_noisy, full_matrices=False)
    sigma_thresh = np.where(sigma > threshold, sigma, 0)
    return U @ np.diag(sigma_thresh) @ Vt


def matrix_completion_simple(A_observed: np.ndarray, mask: np.ndarray, k: int, n_iter: int = 100) -> np.ndarray:
    """Simple matrix completion via iterated SVD truncation."""
    A = A_observed.copy()
    for _ in range(n_iter):
        A_k, _ = low_rank_approx(A, k)
        A = mask * A_observed + (1 - mask) * A_k
    return A


def ellipse_2d(A: np.ndarray, n_pts: int = 100) -> tuple[np.ndarray, np.ndarray]:
    """For 2D visualization: parametrize unit circle then apply A."""
    theta = np.linspace(0, 2 * np.pi, n_pts)
    unit_circle = np.array([np.cos(theta), np.sin(theta)])
    ellipse = A @ unit_circle
    return unit_circle, ellipse
```

**正確性驗證：**

- $U^{\mathrm{T}} U = V^{\mathrm{T}} V = I$（正交性）；
- $A V = U \Sigma$（對齊性質）；
- $\sum_p \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}} = A$（秩 1 累加完整）；
- `np.linalg.matrix_rank(A) == sum(sigma > tol)`（秩一致）。

##### H. 邊界情況處理

| 情況 | 偵測 | 處理 |
|---|---|---|
| $A$ 全零 | `np.allclose(A, 0)` | 所有 $\sigma_p = 0$，分解平凡，UI 顯示「全零矩陣，rank 0」|
| 退化（$\operatorname{rank} < \min(m, n)$）| 數值 $\sigma_p < tol$ 個數 > 0 | reduced SVD 自動只取非零項，4 子空間區顯示零空間維度 > 0 |
| 重複奇異值 | `len(set(sigma_rounded)) < r` | $\mathbf{u}_p, \mathbf{v}_p$ 在重複特徵子空間內任選正交基底（NumPy 自動處理）|
| $m \neq n$（長方）| 形狀檢查 | 自動切換 reduced SVD（避免 full SVD 浪費），UI 顯示「reduced SVD」標籤 |
| $\Sigma$ 含負對角 | 不可能（SVD 保證 $\sigma_p \geq 0$）| 若數值上出現極小負數，自動歸零並警示 |
| Mona Lisa demo 載入失敗 | 檢查影像檔案 | 顯示「請先下載 Mona Lisa 範例」+ 提供 fallback 隨機 32×32 矩陣 |

##### I. 完成標準（Acceptance Criteria）

- [ ] 拉任意矩陣 $A$ 的元素 → SVD 即時更新（< 200ms 含 4 應用同步）；
- [ ] 秩 1 累加動畫流暢，每項拆解清晰可見；
- [ ] 2D 橢圓變形與 SVD 對齊，主軸方向 = $\mathbf{u}_p$、半徑 = $\sigma_p$；
- [ ] 4 應用切換無延遲，每個 demo 獨立運作；
- [ ] 4 子空間視覺整合 ch03 兩塊大餅圖正確，$A\mathbf{v}_p = \sigma_p \mathbf{u}_p$ 動畫對齊；
- [ ] Eckart–Young 誤差曲線正確，與理論值 $\sqrt{\sum_{p>k} \sigma_p^2}$ 一致；
- [ ] 4 個跨章跳轉按鈕（雙 pointer 主 + 副 + 4-Subspaces + EVD）參數正確帶入；
- [ ] 退化 / 長方 / 重複 / 全零 / Mona Lisa 載入失敗等邊界情況都正確處理。

##### J. 反例與常見誤解

- **誤解 1：** 「SVD 只適用方陣 / 可逆矩陣。」**正解：** SVD 適用**任意** $m \times n$ 矩陣，這是它與 EVD 最大的差異。長方陣、退化矩陣、全零矩陣都有 SVD；
- **誤解 2：** 「奇異值就是特徵值。」**正解：** 奇異值是 $A^{\mathrm{T}} A$ 特徵值的**平方根**（且強制非負）。對對稱正定矩陣：$\sigma_p = \lambda_p$；對對稱含負矩陣：$\sigma_p = |\lambda_p|$；對一般矩陣：兩者無直接關係；
- **誤解 3：** 「$U$ 和 $V$ 可以隨意選。」**正解：** $U$ 由 $AA^{\mathrm{T}}$ 特徵向量決定、$V$ 由 $A^{\mathrm{T}} A$ 特徵向量決定，兩者透過 $A\mathbf{v}_p = \sigma_p \mathbf{u}_p$ 連結。**只有重複奇異值情境下才有選擇自由**；
- **誤解 4：** 「PCA 必須先做共變異矩陣再做 EVD。」**正解：** 現代 PCA 都直接對置中資料 $\tilde{X}$ 做 SVD，不算 $\tilde{X}^{\mathrm{T}} \tilde{X}$（避免數值不穩 + 節省計算）；
- **誤解 5：** 「Eckart–Young 只說 Frobenius 範數。」**正解：** Eckart–Young 對 **Frobenius、譜（2-norm）、核（trace norm，所有 unitarily invariant norm**）都成立，是個非常強的最佳性定理。

##### K. 與其他 VizScript 的關係

- **本章 VizScript-02 / 03 / 04：** Tier 2 / Tier 1 精簡版分別處理奇異值降冪 / 4 子空間構造 / 2×2 數值 walkthrough；
- **ch04 VizScript-02 (MM4 + Mona Lisa SVD demo)：** **本 VizScript 的主 pointer + 「應用 1：壓縮」直接重用** — Mona Lisa demo 的低秩近似互動完全相容，本章 VizScript-01 在 Step 5 直接 embed 或跳轉；
- **ch05 VizScript-03 (P4 三明治)：** **本 VizScript 的副 pointer** — SVD 是 (P4) 的最一般情境，視覺布局共用「三明治」基本結構，但 SVD 強調「雙側獨立」，視覺顏色用綠 + 粉紅對比展示；
- **ch03 VizScript-02 (4-Subspaces 兩塊大餅圖)：** **本 VizScript 「顯示 4 子空間」mode 的整合對象** — SVD 直接給出 4 子空間的正交基底，與 ch03 VizScript-02 完美對接，視為「**SVD 是 4-Subspaces 的構造工具**」；
- **ch06e VizScript-01 (EVD)：** **本 VizScript 的「對稱情境跳轉」對象** — 範例 1 的 $A = \bigl[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr]$ 是對稱的，SVD 退化為 EVD，跳轉到 ch06e VizScript-01 看對稱情境的譜分解；
- **後續：** S12+ 實作時，本 VizScript 是「**全書集大成的旗艦 demo**」 — 整合 ch03 + ch04 + ch05 + ch06e 五個前置 VizScript，完整實作後就有「**Linear Algebra 全書互動式視覺化教材**」的核心骨架。

##### L. 配套素材清單

- **必備：** Python 3.11+、NumPy（`linalg.svd`）、SciPy（PCA、矩陣補全）、matplotlib + plotly（2D/3D 幾何）、reactive UI 框架（marimo/streamlit）、Pillow（影像處理）；
- **可選：** scikit-learn（PCA 對照、Iris 資料集載入）、surprise（推薦系統矩陣補全標準庫）；
- **資料集：** Mona Lisa $400 \times 250$ 灰階影像（`mona_lisa.png`，從 ch04 重用）、Iris 資料集（150×4，scikit-learn 內建）、MovieLens 1M 評分資料（推薦系統，可選）；
- **教學素材：** 「SVD 4 大應用」一頁總覽圖卡 + 「Eckart–Young 定理」一頁公式卡 + 「PCA vs SVD 等價性」對照表；
- **未來擴展：** 「**隨機化 SVD**」（Halko–Martinsson–Tropp）demo、「**動態 SVD**」（即時更新）demo、「**張量分解**」（HOSVD）延伸介紹。

##### M. 預期使用者反饋

- **「終於懂了 SVD 為何是線代之王」：** 透過 4 應用同時展示，使用者建立「**SVD 是工程實務無所不在的工具**」直覺；
- **「Eckart–Young 原來這麼直觀」：** 透過秩 $k$ 截斷滑桿與誤差曲線，使用者體會「**捨棄最小 $\sigma_p$ = 最佳近似**」；
- **「PCA 不再神秘」：** 透過 Iris 散點圖降維 demo，使用者看到「**主成分 = 方差最大方向 = $V$ 的前 $k$ 列**」；
- **「4 子空間原來是 SVD 構造的」：** 透過與 ch03 兩塊大餅圖的整合，使用者理解「**SVD 是線代最完整的視覺定理**」；
- **「想做的都能做」：** 影像壓縮 / 降維 / 降噪 / 推薦四個應用各有獨立 demo，使用者離開時帶走「**SVD 工程實務工具箱**」；
- **「全書貫通」：** 透過雙 pointer + 4 子空間 + EVD 跨章跳轉，使用者建立「**§1–§6 全書 = 為了 SVD 鋪陳**」的整合視角，實現作者 Hiranabe 的「Art of Linear Algebra」原始意圖。

---

#### VizScript-02: 奇異值降冪 + Eckart–Young 視覺（Tier 2）

**Tier：** ⭐⭐⭐ Tier 2（精簡版的旗艦演示，與 VizScript-01 並列）
**對應 VizMark：** Figure 6.7 VizMark-02
**預估實作工作量：** S12+ 約 1 session

##### A. 一句話定位

「給一個 $A$，顯示 bar chart 的 $\sigma_1 \geq \sigma_2 \geq \cdots$ + 累計能量曲線 + 滑桿選 $k$ 看截斷誤差，視覺化 Eckart–Young 定理。」

##### B. 學習目標

- 看 $\sigma_p$ 的「能量分布」（前幾項佔比）；
- 看「秩 $k$ 截斷」的最佳性（誤差 = $\sqrt{\sum_{p>k} \sigma_p^2}$）；
- 建立「**奇異值衰減快 → 適合低秩近似**」直覺。

##### C-M（精簡）

**布局：** 上方 $A$ 矩陣 + 中間 bar chart（$\sigma_p$ 藍長條 + 累計能量紅折線）+ 下方滑桿 $k$ + 右下重建 $A_k$ 預覽 + 誤差條。

**動畫：**
- 拉滑桿 $k$ → bar chart 上前 $k$ 個 bar 高亮綠色、後面變灰 → 重建 $A_k$ 即時更新 → 誤差條長度即時調整；
- 對 $A$ 改元素 → bar chart 即時重新計算 → 累計能量曲線重畫；
- Eckart–Young 公式 $\|A - A_k\|_F = \sqrt{\sum_{p > k} \sigma_p^2}$ 公式區同步顯示具體數字。

**用途：** 快速看「**該取多少 $k$ 才足夠**」 — 工程實務最常問的問題。預設範例可放 Mona Lisa（看奇異值衰減快不快、決定壓縮比）。

---

#### VizScript-03: 4 子空間 SVD 構造（精簡）

**Tier：** ⭐⭐ Tier 1（精簡版，重用 ch03 VizScript-02 母模板）
**對應 VizMark：** Figure 6.7 VizMark-03
**預估實作工作量：** S12+ 約 0.5 session（重用 ch03 框架，只需加 SVD 連接層）

##### A. 一句話定位

「用 SVD 直接構造 4 子空間的正交基底，與 ch03 兩塊大餅圖整合：$\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$ 標行空間、$\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$ 標零空間、$\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$ 標列空間、$\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$ 標左零空間。」

##### B. 學習目標

- 看 SVD 與 4 子空間的「直接構造」關係；
- 看 $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$ 的「**對齊映射**」動畫（左圓 → 右圓）；
- 整合 ch03 已實作的 4-Subspaces 視覺。

##### C-M（精簡，重用 ch03 框架）

**布局：** ch03 兩塊大餅圖（左 $\mathbb{R}^n$ + 右 $\mathbb{R}^m$）+ SVD 標記層（$\mathbf{u}_p, \mathbf{v}_p$ 顯示為各子空間正交基底向量）。

**動畫：**
- 對 $A$ 改元素 → 即時重新計算 SVD → 4 子空間基底向量即時更新（含維度變化）；
- 滑鼠 hover 任一個 $\mathbf{v}_p$（左圓）→ 對應 $\mathbf{u}_p$（右圓）高亮 + 標 $\sigma_p$；
- 點 $\mathbf{v}_p$ → 動畫展示 $A \mathbf{v}_p$（左 → 右映射）= $\sigma_p \mathbf{u}_p$（綠箭頭縮放動畫）。

---

#### VizScript-04: 2×2 SVD 數值範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1（輕量輪廓）
**對應 VizMark：** Figure 6.7 VizMark-04
**預估實作工作量：** S12+ 約 0.3 session

##### A. 一句話定位

「用 2×2 範例 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$（Strang 經典）一步一步動畫展示 SVD 計算過程。」

##### B-M（簡述）

**步驟動畫：**

1. 顯示 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$；
2. 計算 $A^{\mathrm{T}} A = \bigl[\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr]$；
3. 求特徵值：$\det(A^{\mathrm{T}} A - \lambda I) = (25-\lambda)^2 - 400 = 0 \Rightarrow \lambda = 45, 5$；
4. $\sigma_1 = \sqrt{45} = 3\sqrt{5} \approx 6.708$，$\sigma_2 = \sqrt{5} \approx 2.236$；
5. 求 $\mathbf{v}_1$：$(A^{\mathrm{T}} A - 45 I) \mathbf{v}_1 = \mathbf{0} \Rightarrow \mathbf{v}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；
6. 求 $\mathbf{v}_2$：$\mathbf{v}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
7. 求 $\mathbf{u}_1 = A\mathbf{v}_1 / \sigma_1 = \frac{1}{3\sqrt{5}} \cdot \frac{1}{\sqrt{2}} \cdot \bigl[\begin{smallmatrix}3\\9\end{smallmatrix}\bigr] = \frac{1}{\sqrt{10}}(1, 3)^{\mathrm{T}}$；
8. 求 $\mathbf{u}_2 = A\mathbf{v}_2 / \sigma_2 = \frac{1}{\sqrt{5}} \cdot \frac{1}{\sqrt{2}} \cdot \bigl[\begin{smallmatrix}3\\-1\end{smallmatrix}\bigr] = \frac{1}{\sqrt{10}}(3, -1)^{\mathrm{T}}$；
9. 組裝 $U, \Sigma, V$ 並驗證 $U\Sigma V^{\mathrm{T}} = A$ ✓；
10. 譜分解 $A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}} + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}}$ 計算每項 + 累加驗證。

**用途：** 入門教學，讓使用者第一次接觸 SVD 時看到完整計算過程的具體數字。**不含 4 應用、不含 4 子空間、不含 2D 幾何**，純步進動畫。

---

### 章末延伸

#### 與 §1–§5 的來源對應

- **§1（Viewing a Matrix）：** SVD 統一了 4 視角 — $A = U\Sigma V^{\mathrm{T}}$ 同時給出列空間（$U$ 的前 $r$ 列）、行空間（$V$ 的前 $r$ 列）、列線性組合的座標系（$V^{\mathrm{T}}$）、行線性組合的座標系（$U$）；
- **§2（Vector × Vector）：** SVD 的 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 是「v2 視角的最有意義版」（外積 + 奇異值加權 + 降冪排序）；
- **§3（Matrix × Vector）：** SVD 的「$A \mathbf{v}_p = \sigma_p \mathbf{u}_p$」是「**矩陣 × 向量**」的「**最特別的一組正交基底**」 — 把正交映射到正交（一般矩陣不會）；
- **§4（MM4）：** SVD 是 (MM4) 的「**最有意義版本**」 — 外積之和按貢獻度排序、可截斷得最佳低秩近似（Eckart–Young）；**ch04 VizScript-02 的 Mona Lisa SVD demo 就是 SVD 章的核心預告片**；
- **§5（P4）：** **`SVD.png` 直接標 `using P4`**，SVD 是 (P4) 三明治的「**雙側獨立 + 對角非負**」最一般情境；
- **§3 4-Subspaces：** SVD 直接給出 4 子空間的正交基底（$\mathbf{v}_p$ 標行空間 / 零空間，$\mathbf{u}_p$ 標列空間 / 左零空間），**整合 ch03 VizScript-02 兩塊大餅圖完整 demo**。

#### 與 §6 其他分解的對應

- **§6.1 CR：** CR 給出「列空間基底」，SVD 給出「**正交**列空間基底」 — SVD 是 CR 的正交化升級；
- **§6.2 LU：** LU 解 $A\mathbf{x} = \mathbf{b}$（限方陣），SVD 解 $A\mathbf{x} = \mathbf{b}$（**任意矩陣 + Moore–Penrose 偽反**）；
- **§6.3 QR：** QR 是「列正交化」，SVD 是「**雙側正交化**」；數值上 SVD 算法常以 QR 為中間步驟；
- **§6.4 EVD：** EVD 限對稱、$U = V$；SVD 任意矩陣、$U \neq V$。**$A^{\mathrm{T}} A$ EVD 給 $V, \Sigma^2$；$AA^{\mathrm{T}}$ EVD 給 $U, \Sigma^2$。SVD = 兩個對稱半正定矩陣 EVD 的整合**。

#### §6 五大分解的視覺指紋總結（本章為終章）

| 分解 | PNG `using` 標記 | 視覺指紋 | 適用矩陣 |
|---|---|---|---|
| $A = CR$ | CR1 標 P1 / CR2 標 P2 | 對偶兩張圖（列視角 + 行視角） | 任意 |
| $A = LU$ | LU1 無標 / LU2 標 MM4 | peeling 逐層楔形 + (MM4) 累加 | 可 LU 分解 |
| $A = QR$ | QR 標 P1 | 綠色直立列（正交基底）+ 藍點上三角 | 列獨立 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | EVD 標 P4 | **左 = 右轉置（鏡像對稱）** + 對角藍點 | **限對稱** |
| $A = U\Sigma V^{\mathrm{T}}$ | SVD 標 P4 | **左綠 + 右粉紅（雙側獨立）** + 對角藍點 + 項數 = 秩 | **任意（無限制）** |

**結論：** §6 五大分解的視覺指紋透過「**`using XX` 標記 + 顏色對比 + 結構元素**」三層編碼，每張 PNG 都是「**自含的視覺定理**」。原書作者 Hiranabe 用 `using XX` 標記建立跨章索引網路（見 ch06a-five.md 升級鏈圖），**S07–S09 三 session 的 PNG 重核工作確立了這個索引網路的完整地圖**。

#### 工程應用前瞻（S12+ 實作目標，本章最豐富）

##### 影像 / 訊號處理

- **Mona Lisa SVD 壓縮 demo**（ch04 VizScript-02 + 本章 VizScript-01 整合）；
- **JPEG 壓縮的 SVD 對照**（DCT vs SVD 比較，看 SVD 為何理論最佳但實務用 DCT）；
- **影像降噪 demo**（雜訊正弦波 + SVD 截斷，可加 wavelet 對照）；
- **去模糊 demo**（Tikhonov 正則化 + SVD 截斷，醫學影像應用）。

##### 資料科學

- **Iris PCA demo**（4D → 2D 降維 + 三類別分離視覺化）；
- **MNIST 手寫數字 PCA**（784D → 2D 視覺化 10 類別分布）；
- **Eigenfaces demo**（人臉資料庫 SVD → 特徵臉視覺化）；
- **基因表達分析 PCA**（生醫應用，可選）。

##### 推薦系統

- **MovieLens 推薦 demo**（用戶 × 電影評分矩陣補全）；
- **Netflix Prize 簡化版**（介紹 SVD++、ALS 等變體）；
- **協同過濾 vs 矩陣補全**對照演示。

##### 數值線性代數

- **Moore–Penrose 偽反 demo**（最小二乘解 + SVD 構造）；
- **條件數視覺化** $\kappa(A) = \sigma_1 / \sigma_r$（看奇異值差距如何影響數值穩定性）；
- **隨機化 SVD demo**（Halko–Martinsson–Tropp 算法，大矩陣加速）。

##### 機器學習

- **線性回歸 SVD 求解**（替代正規方程的數值穩定方法）；
- **嶺回歸 SVD 視覺化**（正則化參數對奇異值的縮減效果）；
- **核 PCA**（kernel PCA 介紹 + SVD 在核空間的對應）。

#### 本章在全書架構中的定位（總結）

- **理論定位：** §6 五大分解的**最後一個 + 最完整的一個** — 同時滿足「適用最廣（任意矩陣）+ 結構最強（雙側正交對角）+ 應用最多（4 大旗艦應用）+ 直接連接 4 子空間（Strang 兩塊大餅圖）+ 最佳低秩近似（Eckart–Young）」五個指標；
- **VizScript 規格：** **全書唯一的 Tier 3 主 VizScript** — VizScript-01 預估 3 session（與 ch04 VizScript-02 同級），整合 4 應用 + 4 子空間 + 2D 幾何 + Mona Lisa demo；
- **跨章 pointer 設計：** **全書唯一的雙 pointer 主 + 副設計** — 主 pointer 指 ch04 VizScript-02 (MM4 + Mona Lisa)，副 pointer 指 ch05 VizScript-03 (P4)；
- **教學定位：** **§1–§6 全書的「集大成 + 工程化」終章** — 使用者完成本章後應建立「線性代數 = 為了 SVD 鋪陳，SVD = 工程實務的瑞士刀」的整合視角；
- **S12+ 實作優先順序：** **VizScript-01 是全書最值得實作的 demo，預估 3 session 但回報極高** — 完成後即可宣稱「**互動式 Linear Algebra 教材的核心骨架完成 80%**」。

#### 來源對照

| 元素 | 來源 |
|---|---|
| 數學公式 | `from-tex/en.md` line 507–569、`from-tex/zh.md` line 494–558 |
| 圖片 | `figs-png/SVD.png`（原始 EPS：`figs/SVD.eps`，原書 p.12）|
| Strang 連結 | LA for Everyone Sec. 7.1（奇異值與奇異向量）、Sec. 7.2（Eckart–Young 定理）|
| Pattern 連結 | §5 (P4) 三明治，本書 PNG 直接標 `using P4` |
| (MM4) 連結 | §4 (MM4) 外積之和，SVD 是「按 $\sigma_p$ 降冪排序的最有意義版」 |
| 4 子空間連結 | §3 4-Subspaces，SVD 直接給出 4 子空間正交基底 |
| 跨章 pointer（**雙 pointer**，全書唯一） | **主 pointer：** [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) (MM4 + Mona Lisa) / **副 pointer：** [ch05 VizScript-03](ch05-patterns.md#vizscript-03) (P4 三明治) / **整合 pointer：** [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) (4-Subspaces) / **對偶 pointer：** [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01) (EVD) |
| Eckart–Young 定理 | Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika* 1: 211–218 |
| Mona Lisa demo 影像 | `ch04 VizScript-02 配套素材` 重用 |
| Iris 資料集 | scikit-learn 內建（`sklearn.datasets.load_iris()`）|

---

## 結論與致謝（Conclusion & Acknowledgements）+ 全書 36 個 VizScript 總覽 + 參考文獻

> **原書頁碼：** 英文版 p.32–p.34（書尾）/ 簡中版 p.32–p.34
> **對應 .tex 段落：** `from-tex/en.md` 第 571–625 行 / `from-tex/zh.md` 第 559–602 行
> **本章圖數：** 0（純文字章節 + 內嵌 3 張附錄參考圖連結）
> **本章 VizMark 數：** 0（散文章節）
> **狀態：** [x] 已完成

---

### 章節摘要

本章是《The Art of Linear Algebra》原書結尾，由 Kenji Hiranabe 親筆撰寫，包含三段內容：（1）對全書「**系統性視覺化矩陣 / 向量乘法及五大分解應用**」的回顧；（2）給協助美化排版的 Ashley Fernandes 與 Gilbert Strang 教授的致謝；（3）參考文獻清單（含 Strang 兩本書 + Hiranabe 兩個獨立 slidedeck + Strang/Hiranabe 合作的 4 子空間圖）。本互動式版本在原 Conclusion 基礎上**新增「全書 33 個 VizScript 總覽」段** — 把 S02–S09 撰寫的所有視覺化劇本集中索引，作為 S11 `BOOK.md` 整合與 S12+ Python 實作的橋樑。**全書 §1–§6 主章節（8 章 + 9 個主 md = 6824 行）+ 序言 + 結論 + 3 附錄（共 13 個 md 檔 + ~7800–8000 行 + 33 個 VizScript）已 100% 完成 md 化階段。**

---

### Kenji Hiranabe 結論與致謝（原文與繁中翻譯）

#### 英文原文

> I presented systematic visualizations of matrix/vector multiplication and their application to the Five Matrix Factorizations. I hope you enjoyed them and will use them in your understanding of Linear Algebra.
>
> Ashley Fernandes helped me with beautifying this paper in typesetting and made it much more consistent and professional.
>
> To conclude this paper, I'd like to thank Prof. Gilbert Strang for publishing "Linear Algebra for Everyone". It guides us through a new vision to these beautiful landscapes in Linear Algebra. Everyone can reach a fundamental understanding of its underlying ideas in a practical manner that introduces us to contemporary and also traditional data science and machine learning. An important part of the matrix world.
>
> — Kenji Hiranabe

#### 繁體中文翻譯

> 我向大家展示了「**矩陣 / 向量乘法**」與「**五大矩陣分解**」應用的系統性視覺化。希望你能喜歡這些圖解，並用它們加深對線性代數的理解。
>
> 感謝 Ashley Fernandes 協助美化本論文的排版，讓全書更加一致與專業。
>
> 在結束本論文之前，我要特別感謝 Gilbert Strang 教授出版《Linear Algebra for Everyone》。它引導我們以全新的視角，去理解線性代數中那些美麗的景觀。透過這種實用的方式，每個人都能對線性代數的基本概念建立紮實的理解，並進一步通往**當代與傳統的資料科學和機器學習**。這是「**矩陣世界（Matrix World）**」中重要的一部分。
>
> — Kenji Hiranabe

---

### 全書 33 個 VizScript 總覽（S11 整合前的橋樑）

> 此段是本互動式版本**獨有**的整合內容（原書無此章）。把 S02–S09 撰寫的所有 VizScript 集中索引，方便：
>
> 1. **讀者：** 從興趣關鍵字（如「SVD 應用」「4 子空間」「動態系統」）直接跳到對應 VizScript
> 2. **S11 整合者：** 把所有 VizScript 移到 `VIZ-CATALOG.md` 集中管理
> 3. **S12+ 視覺化實作者：** 從 Tier 3 旗艦開始，按優先順序排程
>
> **Tier 系統說明：**
>
> - ⭐⭐⭐ **Tier 3**（2 個）：核心骨架旗艦，預估 S12+ 各 3 session 實作。完成後可宣稱「全書互動式教材核心骨架 80%」
> - ⭐⭐⭐ **Tier 2**（多支）：主章核心互動，預估 S12+ 各 2 session
> - ⭐⭐ **Tier 1**（多支）：輕量互動 / 數值範例 walkthrough，預估 S12+ 各 1.5 session
> - ⭐ **Tier 1 輕量**（多支）：純動畫或單一概念示範，預估 S12+ 各 1 session

#### 第一部分：§1–§5 觀念章節（共 16 個 VizScript）

| 章節 | 檔案 | VizScript 編號 | 標題 | Tier |
|---|---|---|---|---|
| §1 Viewing a Matrix | [ch01-viewing-matrix.md](ch01-viewing-matrix.md) | [VizScript-01](ch01-viewing-matrix.md#vizscript-01) | 矩陣的四種觀看視角（4 Ways Toggle） | ⭐⭐⭐ Tier 2 |
| §1 Viewing a Matrix | [ch01-viewing-matrix.md](ch01-viewing-matrix.md) | [VizScript-02](ch01-viewing-matrix.md#vizscript-02) | 矩陣維度的同步重組（Dimensions Synchronizer） | ⭐⭐ Tier 1 |
| §2 Vector × Vector | [ch02-vec-vec.md](ch02-vec-vec.md) | [VizScript-01](ch02-vec-vec.md#vizscript-01) | 外積與秩 1 矩陣（Outer Product → Rank 1） | ⭐⭐⭐ Tier 2 |
| §2 Vector × Vector | [ch02-vec-vec.md](ch02-vec-vec.md) | [VizScript-02](ch02-vec-vec.md#vizscript-02) | 點積 vs 外積對偶切換（Dot ↔ Outer Duality） | ⭐⭐ Tier 1 |
| §3 Matrix × Vector | [ch03-mat-vec.md](ch03-mat-vec.md) | [VizScript-01](ch03-mat-vec.md#vizscript-01) | Mv1 ↔ Mv2 視角切換（Dot Way vs LC Way） | ⭐⭐⭐ Tier 2 |
| §3 Matrix × Vector | [ch03-mat-vec.md](ch03-mat-vec.md) | [VizScript-02](ch03-mat-vec.md#vizscript-02) | **四個基本子空間互動式（Strang's Big Picture）** | ⭐⭐⭐ **Tier 3 候選** |
| §3 Matrix × Vector | [ch03-mat-vec.md](ch03-mat-vec.md) | [VizScript-03](ch03-mat-vec.md#vizscript-03) | vM1 ↔ vM2 行向量視角切換 | ⭐⭐ Tier 1 |
| §3 Matrix × Vector | [ch03-mat-vec.md](ch03-mat-vec.md) | [VizScript-04](ch03-mat-vec.md#vizscript-04) | 列空間軌跡掃描（精簡） | ⭐ Tier 1 |
| §4 Matrix × Matrix | [ch04-mat-mat.md](ch04-mat-mat.md) | [VizScript-01](ch04-mat-mat.md#vizscript-01) | 矩陣 × 矩陣四種視角切換（4-Way Toggle） | ⭐⭐⭐ Tier 2 |
| §4 Matrix × Matrix | [ch04-mat-mat.md](ch04-mat-mat.md) | [VizScript-02](ch04-mat-mat.md#vizscript-02) | **(MM4) 外積累加 + 秩截斷 + Mona Lisa SVD demo** | ⭐⭐⭐ **Tier 3 旗艦 #1** |
| §4 Matrix × Matrix | [ch04-mat-mat.md](ch04-mat-mat.md) | [VizScript-03](ch04-mat-mat.md#vizscript-03) | 維度檢核與內維對齊（Shape Validator） | ⭐⭐ Tier 1 |
| §4 Matrix × Matrix | [ch04-mat-mat.md](ch04-mat-mat.md) | [VizScript-04](ch04-mat-mat.md#vizscript-04) | MM1 點積 walkthrough（精簡） | ⭐ Tier 1 |
| §5 Patterns | [ch05-patterns.md](ch05-patterns.md) | [VizScript-01](ch05-patterns.md#vizscript-01) | 對角矩陣統一互動（P1/P2/P1'/P2' Toggle） | ⭐⭐⭐ Tier 2 |
| §5 Patterns | [ch05-patterns.md](ch05-patterns.md) | [VizScript-02](ch05-patterns.md#vizscript-02) | P3 動態系統軌跡（連通 §6.4 EVD） | ⭐⭐⭐ Tier 2 |
| §5 Patterns | [ch05-patterns.md](ch05-patterns.md) | [VizScript-03](ch05-patterns.md#vizscript-03) | P4 三明治結構（$U\Sigma V^{\mathrm{T}}$ 精簡） | ⭐⭐ Tier 1 + pointer |
| §5 Patterns | [ch05-patterns.md](ch05-patterns.md) | [VizScript-04](ch05-patterns.md#vizscript-04) | P1' 數值步進（輕量） | ⭐ Tier 1 |

#### 第二部分：§6 五大分解（共 17 個 VizScript）

| 章節 | 檔案 | VizScript 編號 | 標題 | Tier |
|---|---|---|---|---|
| §6 總覽 | [ch06a-five.md](ch06a-five.md) | [VizScript-01](ch06a-five.md#vizscript-01) | 五大分解互動切換（5-Factorization Dashboard） | ⭐⭐⭐ Tier 1 + pointer |
| §6.1 CR | [ch06b-CR.md](ch06b-CR.md) | [VizScript-01](ch06b-CR.md#vizscript-01) | CR 拆解 + 三色獨立列 + 對偶 CR1/CR2 切換 | ⭐⭐⭐ Tier 2（雙 pointer）|
| §6.1 CR | [ch06b-CR.md](ch06b-CR.md) | [VizScript-02](ch06b-CR.md#vizscript-02) | rank–獨立列 / 行對應動畫 | ⭐⭐ Tier 1 |
| §6.1 CR | [ch06b-CR.md](ch06b-CR.md) | [VizScript-03](ch06b-CR.md#vizscript-03) | 2×3 範例逐步 walkthrough | ⭐ Tier 1 |
| §6.2 LU | [ch06c-LU.md](ch06c-LU.md) | [VizScript-01](ch06c-LU.md#vizscript-01) | LU 雙視角 + peeling/MM4 切換 | ⭐⭐⭐ Tier 2（單 pointer 指 ch04）|
| §6.2 LU | [ch06c-LU.md](ch06c-LU.md) | [VizScript-02](ch06c-LU.md#vizscript-02) | 高斯消去 + 解 $A\mathbf{x}=\mathbf{b}$ | ⭐⭐ Tier 1 |
| §6.2 LU | [ch06c-LU.md](ch06c-LU.md) | [VizScript-03](ch06c-LU.md#vizscript-03) | 3×3 範例 walkthrough | ⭐ Tier 1 |
| §6.3 QR | [ch06d-QR.md](ch06d-QR.md) | [VizScript-01](ch06d-QR.md#vizscript-01) | Gram–Schmidt 正交化 + 3D 投影 | ⭐⭐⭐ Tier 2（單 pointer 指 ch05）|
| §6.3 QR | [ch06d-QR.md](ch06d-QR.md) | [VizScript-02](ch06d-QR.md#vizscript-02) | 3D 投影視覺（精簡） | ⭐⭐ Tier 1 |
| §6.3 QR | [ch06d-QR.md](ch06d-QR.md) | [VizScript-03](ch06d-QR.md#vizscript-03) | 2×2 QR 數值範例 walkthrough | ⭐ Tier 1 |
| §6.4 EVD | [ch06e-QLQ.md](ch06e-QLQ.md) | [VizScript-01](ch06e-QLQ.md#vizscript-01) | 譜分解互動 + 橢球主軸對齊 3D | ⭐⭐⭐ Tier 2（單 pointer 指 ch05 P4）|
| §6.4 EVD | [ch06e-QLQ.md](ch06e-QLQ.md) | [VizScript-02](ch06e-QLQ.md#vizscript-02) | $P_p$ 三性質視覺驗證（精簡） | ⭐⭐ Tier 1 |
| §6.4 EVD | [ch06e-QLQ.md](ch06e-QLQ.md) | [VizScript-03](ch06e-QLQ.md#vizscript-03) | 2×2 EVD 數值範例 walkthrough | ⭐ Tier 1 |
| §6.5 SVD | [ch06f-USV.md](ch06f-USV.md) | [VizScript-01](ch06f-USV.md#vizscript-01) | **SVD 完整互動 + 4 應用切換（壓縮/PCA/降噪/推薦）** | ⭐⭐⭐ **Tier 3 旗艦 #2**（雙 pointer）|
| §6.5 SVD | [ch06f-USV.md](ch06f-USV.md) | [VizScript-02](ch06f-USV.md#vizscript-02) | 奇異值降冪 + Eckart–Young 視覺 | ⭐⭐⭐ Tier 2 |
| §6.5 SVD | [ch06f-USV.md](ch06f-USV.md) | [VizScript-03](ch06f-USV.md#vizscript-03) | 4 子空間 SVD 構造（精簡，重用 ch03 V-02） | ⭐⭐ Tier 1 |
| §6.5 SVD | [ch06f-USV.md](ch06f-USV.md) | [VizScript-04](ch06f-USV.md#vizscript-04) | 2×2 SVD 數值範例 walkthrough（Strang 經典）| ⭐ Tier 1 |

#### Tier 分佈統計（全書，S11 校正版）

| Tier | 數量 | 列表 |
|---|---|---|
| ⭐⭐⭐ Tier 3 旗艦 | 2 | **[ch04 V-02](ch04-mat-mat.md#vizscript-02)（MM4 + Mona Lisa）+ [ch06f V-01](ch06f-USV.md#vizscript-01)（SVD Master）** |
| ⭐⭐⭐ Tier 3 候選 | 1 | [ch03 V-02](ch03-mat-vec.md#vizscript-02)（4 Subspaces — S12+ 視實作時間決定升級）|
| ⭐⭐⭐ Tier 2 旗艦（附錄）| 1 | **[appendix-matrix-world V-01](appendix-matrix-world.md#vizscript-01)（Matrix World — S12+ 全書互動式教材首頁）**|
| ⭐⭐ Tier 2 主章 | 14 | [ch01 V-01](ch01-viewing-matrix.md#vizscript-01) / [ch01 V-02](ch01-viewing-matrix.md#vizscript-02) / [ch02 V-01](ch02-vec-vec.md#vizscript-01) / [ch02 V-02](ch02-vec-vec.md#vizscript-02) / [ch03 V-01](ch03-mat-vec.md#vizscript-01) / [ch03 V-03](ch03-mat-vec.md#vizscript-03) / [ch04 V-01](ch04-mat-mat.md#vizscript-01) / [ch05 V-01](ch05-patterns.md#vizscript-01) / [ch05 V-02](ch05-patterns.md#vizscript-02) / [ch06b V-01](ch06b-CR.md#vizscript-01) / [ch06c V-01](ch06c-LU.md#vizscript-01) / [ch06d V-01](ch06d-QR.md#vizscript-01) / [ch06e V-01](ch06e-QLQ.md#vizscript-01) / [ch06f V-02](ch06f-USV.md#vizscript-02) |
| ⭐⭐ Tier 1 + pointer | 3 | [ch06a V-01](ch06a-five.md#vizscript-01)（五分解 dashboard）/ [appendix-map-eigenvalues V-01](appendix-map-eigenvalues.md#vizscript-01)（12 格特徵值地圖）/ [appendix-four-subspaces V-01](appendix-four-subspaces.md#vizscript-01)（4 子空間整合）|
| ⭐ Tier 1（精簡 / 輕量）| 15 | [ch03 V-04](ch03-mat-vec.md#vizscript-04) / [ch04 V-03](ch04-mat-mat.md#vizscript-03) / [ch04 V-04](ch04-mat-mat.md#vizscript-04) / [ch05 V-03](ch05-patterns.md#vizscript-03) / [ch05 V-04](ch05-patterns.md#vizscript-04) / [ch06b V-02](ch06b-CR.md#vizscript-02) / [ch06b V-03](ch06b-CR.md#vizscript-03) / [ch06c V-02](ch06c-LU.md#vizscript-02) / [ch06c V-03](ch06c-LU.md#vizscript-03) / [ch06d V-02](ch06d-QR.md#vizscript-02) / [ch06d V-03](ch06d-QR.md#vizscript-03) / [ch06e V-02](ch06e-QLQ.md#vizscript-02) / [ch06e V-03](ch06e-QLQ.md#vizscript-03) / [ch06f V-03](ch06f-USV.md#vizscript-03) / [ch06f V-04](ch06f-USV.md#vizscript-04) |
| **總計** | **36** | 主章 33（13 個 md 檔 ch01–ch06f 9 章 + 4 散文 / 附錄章）+ 附錄 3（旗艦 1 + pointer 2）|

#### S12+ Python 實作優先順序（S11 校正版）

| 批次 | 對象 | 預估 session 數 | 完成後成果 |
|---|---|---|---|
| **首批（核心骨架）** | ch04 V-02 + ch06f V-01（2 個 Tier 3 旗艦）| 6 session（各 3 session）| 「**全書互動式教材核心骨架 80%**」|
| **次批（教材首頁 + 4 子空間 + §6 主章）**| **appendix-matrix-world V-01（Tier 2 旗艦 — 教材首頁）** + ch03 V-02（升級 Tier 3 候選）+ ch06b/c/d/e V-01（4 個 §6 主章 Tier 2）+ ch01/02/05 V-01（3 個 §1/§2/§5 主章 Tier 2）| ~19 session | 全書主互動完成 + 教材首頁就緒 |
| **末批（剩餘 Tier 2 + Tier 1 + 附錄 pointer）**| ch01/02/03/04/05/06f V-02 + ch03 V-03（7 個剩餘 Tier 2）+ 3 個 Tier 1 + pointer（含 ch06a 五分解 dashboard + 2 個附錄 pointer 整合）+ 15 個 Tier 1 精簡 / 輕量 | ~6–8 session | 全書 36 個 VizScript 全部 100% 互動 |
| **Total S12+ 預估** | — | **~31–33 session**（不含技術棧 PoC 初期 ~3 session）| 完整互動式教材 |

---

### 參考文獻（References and Related Works）

#### 主要書籍（核心兩本，貫穿全書）

1. **Gilbert Strang** (2020), *Linear Algebra for Everyone*, Wellesley Cambridge Press.
   <http://math.mit.edu/everyone>
   — 本互動式版本的**最底層原書**，Hiranabe 的圖解筆記即基於此書

2. **Gilbert Strang** (2016), *Introduction to Linear Algebra*, Wellesley Cambridge Press, 5th ed.
   <http://math.mit.edu/linearalgebra>
   — Strang 早期經典，4 子空間 / SVD 的標準參考

#### Kenji Hiranabe 獨立 slidedeck（本互動式版本的兩個附錄來源）

3. **Kenji Hiranabe** (2021), *Map of Eigenvalues*, Slidedeck.
   <https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf>
   — 12 種矩陣 × 特徵值幾何位置的「分類地圖」，**對應本互動式版本 [§ Map of Eigenvalues 附錄](appendix-map-eigenvalues.md)**

4. **Kenji Hiranabe** (2020), *Matrix World*, Slidedeck.
   <https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf>
   博客：<https://anagileway.com/2020/09/29/matrix-world-in-linear-algebra-for-everyone/>
   — 用同心橢圓表示矩陣類別包含關係的「全書地圖」，**對應本互動式版本 [§ Matrix World 附錄](appendix-matrix-world.md)**（S12+ Matrix World 互動式索引地圖將作為「全書互動式教材的首頁」）

#### Strang/Hiranabe 合作圖

5. **Gilbert Strang, artwork by Kenji Hiranabe**, *The Four Subspaces and the solutions to $A\mathbf{x} = \mathbf{b}$*
   — Strang 的「兩塊大餅圖」標誌性視覺化，**對應本互動式版本 [§ The Four Subspaces 附錄](appendix-four-subspaces.md)**（同款圖在 §3 [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) 已建立 ⭐⭐⭐ Tier 3 候選互動）

---

### 致謝（本互動式版本）

- **原書作者：** Kenji Hiranabe（平鍋健兒，Change Vision Inc. / ESM Inc.，[twitter @hiranabe](https://twitter.com/hiranabe)，<https://anagileway.com>）
- **原書序言 & 線性代數教學典範：** Gilbert Strang 教授（MIT 數學系，<http://www-math.mit.edu/~gs/>）
- **簡中版翻譯：** KFChLiu（[twitter @KFChLiu](https://twitter.com/KFChLiu)，[微博 5717297833](https://weibo.com/u/5717297833)）
- **本互動式版本撰寫：** Back Kuo（郭志彬，Floadia Corporation Taiwan Branch）+ Claude（Anthropic）協作
- **撰寫工期：** 2026-05-11 至 2026-05-12（S00–S10，共 11 個 session，約 18h 純撰寫 + 多次 PNG 重核）
- **後續計畫（S11+）：** S11 整合 + 校對 + 統一 + 生成 `BOOK.md` 合併版 + `VIZ-CATALOG.md` 視覺化候選池；S12+ ~28–30 session 完成 Python 互動式實作（傾向 **Marimo + plotly 3D + matplotlib + scikit-learn** 技術棧）

---

### 全書里程碑回顧

| Session | 主題 | 完成 |
|---|---|---|
| S00 | 初始化 + clone repo + session 管理啟用 | 2026-05-11 |
| S01 + S01.5 | 機械轉換 + 雙 Schema 定版 + 路線圖 | 2026-05-12 |
| S02 | §1 Viewing a Matrix（[ch01](ch01-viewing-matrix.md)，418 行 + 2 VizMark）+ 術語切換至 A 派 | 2026-05-12 |
| S03 | §2 Vector × Vector（[ch02](ch02-vec-vec.md)，497 行 + 2 VizMark）+ 對偶結構章節模式 | 2026-05-12 |
| S04 | §3 Matrix × Vector + 4-Subspaces（[ch03](ch03-mat-vec.md)，935 行 + 4 VizMark）+ 多 VizMark 分級策略 | 2026-05-12 |
| S05 | §4 Matrix × Matrix（[ch04](ch04-mat-mat.md)，849 行 + 4 VizMark）+ **Tier 3 旗艦 #1** + N-way 章節模式 | 2026-05-12 |
| S06 | §5 Patterns（[ch05](ch05-patterns.md)，830 行 + 4 VizMark）+「Tier 1 + pointer」省篇幅策略 | 2026-05-12 |
| S07 | §6 五大分解總覽（[ch06a](ch06a-five.md)，331 行）+ §6.1 CR（[ch06b](ch06b-CR.md)，545 行）+ **兩章 session 模式首例 + PNG `using XX` 跨章標記發現** | 2026-05-12 |
| S08 | §6.2 LU（[ch06c](ch06c-LU.md)，654 行）+ §6.3 QR（[ch06d](ch06d-QR.md)，541 行）+ 主章 + 主章模式 + 3D 渲染棧導入 | 2026-05-12 |
| S09 | §6.4 EVD（[ch06e](ch06e-QLQ.md)，695 行）+ §6.5 SVD（[ch06f](ch06f-USV.md)，**934 行全書最長**）+ **§6 Tier 3 主 VizScript 首例 + 雙 pointer 復活判準** | 2026-05-12 |
| **S10** | **本檔（Foreword + Conclusion + 3 附錄）+ §1–§6 全書內容章節 100% 完成** | **2026-05-12** |
| S11 | 整合 + 校對 + `BOOK.md` + `VIZ-CATALOG.md` | 預定下次 |
| S12+ | Python 視覺化技術棧 + PoC 實作（~28–30 session）| 預定 |

---

### 章末延伸

- **回到首頁：** [→ § Foreword（序言）](front-foreword.md)
- **進入附錄：**
  - [Map of Eigenvalues（特徵值地圖）](appendix-map-eigenvalues.md)
  - [Matrix World（矩陣世界全書地圖）](appendix-matrix-world.md)
  - [The Four Subspaces（四個基本子空間）](appendix-four-subspaces.md)

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 571–625 / `The-Art-of-Linear-Algebra.pdf` p.32–p.34
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 559–602
- **新增內容（本互動式版本獨有）：** 全書 33 個 VizScript 總覽段（S10 撰寫，為 S11 `BOOK.md` 整合與 S12+ Python 實作的橋樑）
- **原 repo：** <https://github.com/junoback/The-Art-of-Linear-Algebra>
- **授權：** Apache 2.0

---

## 附錄 A：特徵值地圖（Map of Eigenvalues）

> **原書頁碼：** 英文版 References 第 3 條（p.34）/ 簡中版同
> **對應 .tex 段落：** `from-tex/en.md` 第 596–602 行（References 區）/ 完整 PDF：[`MapofEigenvalues.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf)
> **本章圖數：** 1（`MapofEigenvalues.png`）
> **本章 VizMark 數：** 1（⭐⭐ Tier 1 + pointer 指 [ch06e EVD VizScript-01](ch06e-QLQ.md#vizscript-01)）
> **PNG `using XX` 標記：** **無**（S10 PNG 重核確認 — HANDOFF 預估「可能標 P3」推翻；附錄是「地圖層級」非 Pattern 套用層級）
> **狀態：** [x] 已完成

---

### 章節摘要

《Map of Eigenvalues》是 Kenji Hiranabe 於 2021 年獨立發布的 slidedeck，**並非《Linear Algebra for Everyone》主書內容**，而是作為「**特徵值的視覺化分類地圖**」的補充作品。它把 12 種常見矩陣類別（從零矩陣 $O$ 到 Markov 矩陣）依「**特徵值在複平面上的幾何位置**」一字排開，讓讀者「**看一張圖就能辨認矩陣類型**」。每個類別給出：（1）類別名稱與符號；（2）小型範例矩陣（3×3）；（3）特徵值的代數條件（如 $\forall \lambda = 0$、$\forall \lambda \in \mathbb{R}$）；（4）特徵值在複平面上的散點圖（橙色圓點）。本附錄是 §6.4 EVD 的「**視覺地圖總覽**」 — 把該章的「對稱矩陣特殊性 $\forall \lambda \in \mathbb{R}$」放回 12 類矩陣的全景中。互動式版本透過「**單一 dashboard 同時呈現 12 類**」+ 拉桿改範例矩陣即時看特徵值移動，讓讀者建立「**矩陣類別 ↔ 特徵值分佈**」的雙向直覺。

---

### 數學要點

#### 1. 12 個矩陣類別與特徵值幾何位置（核心 ⭐）

> **數學物件：** 矩陣 $A \in \mathbb{R}^{n \times n}$（方陣）的**特徵值** $\lambda$ 滿足 $\det(A - \lambda I) = 0$。一般情況下 $\lambda \in \mathbb{C}$（含複數）。Hiranabe 把 12 種「結構化矩陣」依特徵值在**複平面**的分佈集中呈現。
>
> **記號：**
> - 橫軸 = $\mathrm{Re}(\lambda)$（實部）
> - 縱軸 = $\mathrm{Im}(\lambda)$（虛部）
> - 橙色實心圓點 = 每個特徵值的位置

| 矩陣類別 | 符號 / 定義 | 範例（$3 \times 3$）| 特徵值代數條件 | 幾何位置 |
|---|---|---|---|---|
| **零矩陣** | $O$（所有元素 0） | $\bigl[\begin{smallmatrix}0&0&0\\0&0&0\\0&0&0\end{smallmatrix}\bigr]$ | $\forall \lambda = 0$ | 原點 0 重根 |
| **單位矩陣** | $I$（對角全 1） | $\bigl[\begin{smallmatrix}1&0&0\\0&1&0\\0&0&1\end{smallmatrix}\bigr]$ | $\forall \lambda = 1$ | 實軸 1 重根 |
| **投影矩陣** | $P = P^2 = P^{\mathrm{T}}$ | $\bigl[\begin{smallmatrix}1&0&1\\0&1&0\\0&0&0\end{smallmatrix}\bigr]$（注：此例只是示意，真實投影需 $P = P^2$）| $\forall \lambda = 0 \text{ or } 1$ | 實軸 {0, 1} 兩點 |
| **冪零矩陣** | $N$，$\exists k: N^k = O$ | $\bigl[\begin{smallmatrix}0&1&1\\0&0&1\\0&0&0\end{smallmatrix}\bigr]$ | $\forall \lambda = 0$ | 原點重根（但 $N \neq O$）|
| **$zI$（標量倍單位）**| $zI$（對角 $z$）| $\bigl[\begin{smallmatrix}z&0&0\\0&z&0\\0&0&z\end{smallmatrix}\bigr]$ | $\forall \lambda = z$ | 複平面任意點 $z$ 處 |
| **可逆矩陣** | Invertible（$\det A \neq 0$）| 一般密度矩陣 | $\forall \lambda \neq 0$ | 整個複平面**除原點**（散佈）|
| **對稱矩陣** | $S = S^{\mathrm{T}}$ | $\bigl[\begin{smallmatrix}1&2&2\\2&0&1\\2&1&0\end{smallmatrix}\bigr]$ | $\forall \lambda \in \mathbb{R}$ | **實軸上**任意位置 |
| **對稱正定** | $S_+ = S^{\mathrm{T}}, \mathbf{x}^{\mathrm{T}} S \mathbf{x} > 0$ | $\bigl[\begin{smallmatrix}2&0&1\\0&1&0\\1&0&1\end{smallmatrix}\bigr]$ | $\forall \lambda > 0$ | **實軸正半軸** |
| **反對稱矩陣** | $A = -A^{\mathrm{T}}$ | $\bigl[\begin{smallmatrix}0&1&0\\-1&0&1\\0&-1&0\end{smallmatrix}\bigr]$ | $\forall \lambda \in i\mathbb{R}$（純虛數）| **虛軸上**（含原點）|
| **正交矩陣** | $Q$，$Q^{\mathrm{T}}Q = I$ | $\bigl[\begin{smallmatrix}0&1&0\\-1&0&0\\0&0&1\end{smallmatrix}\bigr]$ | $\forall \| \lambda \| = 1$ | **單位圓**上 |
| **Markov 矩陣** | 行和 = 1，$A_{ij} \geq 0$ | $\bigl[\begin{smallmatrix}0&0.2&0.9\\0.9&0&0\\0.1&0.8&0.1\end{smallmatrix}\bigr]$ | $\exists \lambda = 1$，其他 $\| \lambda \| \leq 1$ | **單位圓內**（含圓上 $\lambda=1$）|
| **奇異矩陣** | $\det A = 0$ | 任意 rank-deficient | $\exists \lambda = 0$ | 複平面散佈，**必含原點** |

#### 2. 對應 §6.4 EVD 的視覺意義

> Map of Eigenvalues 是 §6.4 EVD（$S = Q \Lambda Q^{\mathrm{T}}$）的「**前置全景**」。EVD 是「**對稱矩陣**」這一**單一類別**的詳細分解 — 而 Map 把這個類別放回 12 個類別的視覺地圖中，讓讀者「**先看到所有可能**，再聚焦對稱**」。

**三層遞進關係：**

1. **Map of Eigenvalues**（本附錄）：12 類全景，每類特徵值在複平面的「位置指紋」
2. **§6.4 EVD**（[ch06e](ch06e-QLQ.md)）：對稱類的詳細分解 $S = Q \Lambda Q^{\mathrm{T}}$，$\Lambda$ 對角元 = 實軸特徵值
3. **§6.5 SVD**（[ch06f](ch06f-USV.md)）：把 EVD 推廣到任意矩陣，奇異值 $\sigma \geq 0$（**實軸正半軸**，類比 Map 中「Positive Definite」位置）

#### 3. 與 §5 (P4) 三明治結構的連結

> EVD/SVD 的 (P4) 三明治結構 $S = Q \Lambda Q^{\mathrm{T}}$ 與 $A = U \Sigma V^{\mathrm{T}}$ 都以「**對角矩陣**」為核心。Map of Eigenvalues 中：
>
> - **對角矩陣**（$D$，藍點對角）的特徵值是「**對角元素本身**」 — 因為 $\det(D - \lambda I) = \prod(d_p - \lambda)$
> - 因此「**對角化**」的本質是「**用 $Q$ 把任意對稱矩陣轉到對角矩陣的座標**」 — Map 中對角矩陣是「**所有矩陣類別的最簡形式**」

#### 4. 三類特殊矩陣的幾何指紋（深入觀察）

| 矩陣類別 | 幾何指紋 | 為什麼？ |
|---|---|---|
| **對稱** ($S$) | 特徵值全在實軸 | $S^{\mathrm{T}}S = S^2$ 對稱保證 $\lambda$ 實數（譜定理）|
| **反對稱** ($A = -A^{\mathrm{T}}$) | 特徵值全在虛軸 | $A^{\mathrm{T}} = -A$ 導致 $\lambda + \bar\lambda = 0$ |
| **正交** ($Q^{\mathrm{T}}Q = I$) | 特徵值全在單位圓 | 範數保持 $\| Q\mathbf{x} \| = \| \mathbf{x} \|$ 導致 $\| \lambda \| = 1$ |

這三類矩陣構成了「**Normal matrices**」（$A^{\mathrm{T}}A = AA^{\mathrm{T}}$）的三個核心子集 — 詳見 [Matrix World 附錄](appendix-matrix-world.md) 的同心橢圓地圖（Symmetric ⊂ Normal ⊂ Square ⊂ Matrix）。

---

### 圖片詳細描述（Figure Description）

#### Figure A.1: 特徵值地圖（Map of Eigenvalues）— 無 `using` 標記

**圖檔：** `docs/book/figs-png/MapofEigenvalues.png`（原始 PDF：`MapofEigenvalues.pdf`）
**原書頁碼：** Slidedeck 獨立發布（References 第 3 條）
**所屬章節：** 附錄 A

##### 視覺結構 (Visual Structure)

整體**2 列 × 6 行**網格，每格是一個矩陣類別的迷你 dashboard：

- **每格的元素：**
  - 左上：類別名稱（粗體大字，如 $O$、$I$、$P$、$N$、$zI$、$S$、$S_+$、$Q$、Markov）
  - 右側：3×3 範例矩陣（方括號包），文字小但清晰
  - 中央：**複平面散點圖**，橫軸 = 實部、縱軸 = 虛部，原點標 0（或對應的座標 1）
  - **特徵值用橙色實心圓點呈現**，重疊處用「堆疊圓圈」表達重根
  - 下方：類別描述文字（如「$P = P^2 = P^{\mathrm{T}}$」、「$\forall \lambda = 0$ or $1$」）

- **第 1 列**（6 個）：$O$（Zero）→ $I$（Identity）→ $P$（Projection）→ $N$（Nilpotent）→ $zI$（z times Identity）→ Invertible（最右獨立大色塊，特徵值散佈整個複平面除原點）

- **第 2 列**（6 個）：$S$（Symmetric，實軸線排列）→ $S_+$（Positive definite，實軸正半部分）→ Anti-symmetric（純虛軸排列）→ $Q$（Orthogonal，單位圓上分佈）→ Markov（單位圓內含 1）→ Singular（最右大色塊，特徵值散佈含原點）

- **整體色調：** 背景純白、外框深藍細線、特徵值橙色實心圓、文字深藍中等粗體 — 風格極簡，目標是「**12 格並列一眼看完**」

- **視覺引導：** 讀者先從**整體網格**辨認結構（2 列 × 6 行），然後**每格獨立讀**（先看名稱 → 看複平面位置 → 看代數條件），最後**橫向對照**（例如：對稱 vs 反對稱 vs 正交三個對偶類別）

##### 數學內容 (Mathematical Content)

$$
A \in \mathbb{R}^{n \times n}, \quad \lambda \in \mathbb{C}, \quad \det(A - \lambda I) = 0
$$

**12 類矩陣的代數條件與幾何位置整理：**

$$
\begin{array}{lll}
\text{Zero }(O) & : & \forall \lambda = 0 \\
\text{Identity }(I) & : & \forall \lambda = 1 \\
\text{Projection }(P=P^2=P^{\mathrm{T}}) & : & \forall \lambda \in \{0, 1\} \\
\text{Nilpotent }(N^k = O) & : & \forall \lambda = 0 \quad (\text{但 } N \neq O)\\
zI & : & \forall \lambda = z \quad (z \in \mathbb{C}) \\
\text{Invertible }(\det A \neq 0) & : & \forall \lambda \neq 0 \\
\text{Symmetric }(S = S^{\mathrm{T}}) & : & \forall \lambda \in \mathbb{R} \\
\text{Positive Definite }(S_+) & : & \forall \lambda > 0 \\
\text{Anti-symmetric }(A = -A^{\mathrm{T}}) & : & \forall \lambda \in i\mathbb{R} \\
\text{Orthogonal }(Q^{\mathrm{T}}Q = I) & : & \forall |\lambda| = 1 \\
\text{Markov }(\mathbf{1}^{\mathrm{T}} A = \mathbf{1}^{\mathrm{T}}) & : & \exists \lambda = 1,\ \text{其他 } |\lambda| \leq 1 \\
\text{Singular }(\det A = 0) & : & \exists \lambda = 0
\end{array}
$$

##### 直覺解讀 (Intuition)

這張圖是「**特徵值的視覺百科**」 — 12 個常見矩陣類別並列，讓讀者建立「**矩陣類別 ↔ 特徵值位置**」的雙向直覺。**最重要的三條洞察：**

**洞察 1：對稱 = 實軸、反對稱 = 虛軸、正交 = 單位圓** — 這三類「**結構化矩陣**」對應**三條幾何曲線**（實軸 / 虛軸 / 單位圓），形成「**Normal matrices 的三大代表**」。§6.4 EVD 是「對稱 = 實軸」這一條的詳細展開。

**洞察 2：投影矩陣的特徵值只能是 0 或 1** — 因為 $P^2 = P$ 蘊含 $\lambda^2 = \lambda$，所以 $\lambda \in \{0, 1\}$。這個性質在 §5 (P3) 動態系統章與 §6.4 EVD 投影矩陣 $P_p$ 三性質都會用到（[ch05 VizScript-03](ch05-patterns.md#vizscript-03)）。

**洞察 3：Markov 矩陣必有 $\lambda = 1$，其他都在單位圓內** — 這是「**穩定態存在性定理**」的視覺呈現。Markov 鏈的長期行為由 $\lambda = 1$ 的特徵向量主導（如 Google PageRank、人口流動模型）。**Markov 矩陣是 §5 (P3) 動態系統的核心應用**。

**常見誤解：**

- **「冪零 $N$ 與零矩陣 $O$ 都有 $\forall \lambda = 0$，是否相同？」** 不同！$O$ 是「**對角化的 0 矩陣**」（$Q\Lambda Q^{\mathrm{T}}, \Lambda = O$），$N$ 是「**不可對角化的 0 特徵值**」（Jordan 塊內部有 1）。Map 用「$O$ 重疊圓點」vs「$N$ 偏移圓點」隱晦表達這個差異。
- **「Anti-symmetric 特徵值都是純虛數，那 0 算嗎？」** 算！0 = $i \cdot 0$ 屬於 $i\mathbb{R}$。**奇數階反對稱矩陣必有 $\lambda = 0$**（因 $\det A = \det(-A^{\mathrm{T}}) = (-1)^n \det A$）。

**對比另一種看法（Matrix World 同心橢圓地圖）：**

- **Map of Eigenvalues** 用「**並列網格**」看特徵值位置 — 適合「**分類辨識**」
- **Matrix World**（見 [appendix-matrix-world.md](appendix-matrix-world.md)）用「**同心橢圓**」看類別包含關係 — 適合「**理解誰是誰的特例**」

兩個附錄是「**同一矩陣分類問題的對偶視覺化**」 — 一個從「**特徵值幾何**」切入，一個從「**矩陣性質繼承關係**」切入。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [動態切換 + 拉桿] ⭐⭐ Tier 1 + pointer
> **位置：** Figure A.1 / 附錄 A 整圖
> **核心概念：** 12 矩陣類別 ↔ 特徵值幾何位置雙向辨認
> **互動梗概：** 12 格 dashboard 並列；點任一格放大顯示，可拉桿調整該類別範例矩陣的某些參數（如 $zI$ 拉動 $z$ 看橙點移動 / 對稱矩陣調整 $S$ 元素看特徵值在實軸滑動 / Markov 改機率看圓內分佈變化）；點任一格的「→ 看 EVD 詳解」跳轉到 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)（對稱類詳細展開），點「→ 看 P4 三明治」跳轉到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（投影矩陣 $P_p$ 三性質）
> **詳見劇本：** VizScript-01（章末）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: 特徵值地圖互動式 dashboard（Map of Eigenvalues Interactive）

**Tier：** ⭐⭐ Tier 1 + pointer（12 格 dashboard 控制器，每格特徵值動畫獨立但結構共用；對稱類詳細展開 pointer 到 ch06e）
**對應 VizMark：** Figure A.1 / VizMark-01

> 本劇本只負責**12 格網格切換 + 單格特徵值即時計算 + 跨類別參數對比**，對稱類的「$Q\Lambda Q^{\mathrm{T}}$ 詳細展開 + 橢球主軸對齊」全部不重複實作 — 透過按鈕「→ 看對稱類 EVD 詳解」跳轉到 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)。投影矩陣的「$P_p$ 三性質視覺驗證」也透過按鈕「→ 看 P4 三明治」跳轉到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)。

##### A. 一句話定位

把 12 個矩陣類別並列為互動式 dashboard，每格可獨立調整範例參數即時看特徵值在複平面上移動，讓讀者建立「**矩陣類別 ↔ 特徵值幾何位置**」的雙向直覺，並從 dashboard 點按鈕跳轉到 §6.4 EVD 的詳細展開。

##### B. 學習目標（Learning Outcome）

讀者完成此互動後能夠：

1. **辨認 12 類矩陣**：看到任意 3×3 矩陣，能依特徵值位置（實軸 / 虛軸 / 單位圓 / 原點 / 散佈）回推矩陣類別
2. **建立對偶直覺**：理解對稱（實軸）↔ 反對稱（虛軸）↔ 正交（單位圓）三類的對稱關係
3. **連結 §6.4 EVD**：理解 EVD 的本質是「對稱類」的詳細分解，整個 Map 是 EVD 的「全景前置」
4. **理解 Markov 應用**：認識 Markov 矩陣 $\lambda = 1$ 對應穩定態的視覺直覺

##### C. 整體布局（2 模式：grid view + zoom view）

- **Grid view（預設）：** 2 列 × 6 行 = 12 格，每格固定 240×180 px 含「類別名 + 縮小矩陣 + 迷你複平面」；hover 該格上方顯示「→ 點此放大互動」
- **Zoom view（點任一格觸發）：** 該格放大為 800×600 px 主視窗 + 左側 200 px 拉桿區（調整範例參數）+ 上方 60 px 按鈕區（含「← 回 Grid」、「→ 看 EVD 詳解」、「→ 看 P4 三明治」等 pointer 按鈕）

##### D. 可調參數（拉桿）

每類別拉桿不同，舉典型代表：

- **$zI$ 類：** 拉桿 $z = a + bi$（$a, b \in [-3, 3]$ 步進 0.1），即時看橙點在複平面移動
- **對稱類 $S$：** 拉桿 6 個獨立參數 $s_{11}, s_{22}, s_{33}, s_{12}, s_{13}, s_{23} \in [-9, 9]$ 步進 1，特徵值在實軸滑動
- **正交類 $Q$（2×2 簡化）：** 拉桿旋轉角 $\theta \in [0, 2\pi]$，特徵值在單位圓上對稱移動
- **Markov 類：** 拉桿 9 個機率參數 $p_{ij} \geq 0$ 且每行和 = 1（用 softmax 強制歸一），主特徵值固定在 $\lambda = 1$，其他特徵值在單位圓內移動

##### E. 顏色配方（沿用全書錨點）

- **特徵值橙點 `#ff7f0e`**：所有類別共用，實心圓直徑 12 px
- **複平面背景**：純白 + 灰格線 `#cccccc` 步進 0.5、原點與單位圓藍細線 `#1f77b4`
- **類別名標籤**：深藍 `#1f77b4` 粗體
- **跳轉按鈕**：白底深綠邊框 `#2ca02c`，hover 填色深綠

##### F. 動畫節奏

- **Grid view → Zoom view 切換：** 該格放大 600ms 緩動 ease-in-out，其他 11 格淡出 300ms
- **拉桿即時更新：** 每次值改變，特徵值橙點以 200ms 平滑移動到新位置（matplotlib `FuncAnimation` 或 plotly transition）
- **Markov 機率歸一動畫：** 拉桿後 softmax 後 400ms 顯示「機率箭頭」表達向歸一收斂

##### G. 公式同步顯示

- **Zoom view 右側顯示：**
  1. 當前矩陣 $A$（$3 \times 3$，數值即時更新）
  2. 特徵多項式 $\det(A - \lambda I)$（展開後的多項式）
  3. 特徵值 $\lambda_1, \lambda_2, \lambda_3$（複數形式，含 Re/Im 兩部分）
  4. 類別代數條件對照（如「目前 $S = S^{\mathrm{T}}$? ✓」即時驗證）

##### H. 驗收標準

1. **拉桿同步性：** 任一拉桿改變後，矩陣 / 多項式 / 特徵值 / 散點位置應 < 300ms 完成同步
2. **跨類別對比：** Grid view 12 格中至少 3 對「對偶類」（對稱 vs 反對稱 / 投影 vs 冪零 / Markov vs Singular）視覺差異一眼可辨
3. **跳轉準確：** 「→ 看 EVD 詳解」按鈕跳轉到 ch06e VizScript-01 並把當前對稱矩陣 $S$ 帶入作為 EVD 範例輸入
4. **常數類別處理：** $O$、$I$ 兩類無拉桿（特徵值固定），只顯示說明文字「特徵值為常數，無互動」

##### I. 邊界與健壯性

- **矩陣對稱性檢查：** 對稱類拉桿改變後自動 enforce $S_{ij} = S_{ji}$
- **正交性檢查：** 正交類用「先參數化（旋轉角 / Givens 角）→ 構造 $Q$」避免讀者拉到非正交狀態
- **Markov 行和檢查：** 每次拉桿後重新 softmax，但顯示「正規化前的原始機率」供使用者直覺輸入
- **退化特徵值警告：** 多重特徵值（如 $\lambda_1 = \lambda_2$）用紫色高亮，提示「重根 / 可能不可對角化」（連結 ch06e § 對稱矩陣特殊性）

##### J. 字幕 / 標題 / 圖例

- **Grid view 頂部：** 「特徵值地圖：12 個矩陣類別的視覺百科」
- **Zoom view 頂部：** 「[類別名]：拉桿即時看特徵值移動」
- **底部圖例：** 「橙點 = 特徵值在複平面位置」「藍圓 = 單位圓」「灰格 = 0.5 步進複平面」

##### K. 教學引導文案（嵌入互動視窗）

- **Grid view 初次進入：** 「12 格並列特徵值地圖。點任一格放大互動。試從『**對稱類**』開始，看實軸上 3 個橙點隨拉桿滑動。」
- **Zoom view 進入後：** 「現在看到的是 [類別名]。拉桿改變範例矩陣，注意特徵值如何在 [實軸 / 虛軸 / 單位圓 / ...] 上移動。再點頂端按鈕『→ 看 EVD 詳解』看對稱矩陣的完整分解。」

##### L. 平台技術建議（S12+ 實作）

- **建議平台：** Marimo（反應式 notebook）+ plotly（複平面散點動畫流暢度高）
- **核心套件：** `numpy.linalg.eig`（計算特徵值，含複數）、`plotly.graph_objects.Scatter`（橙點）、`marimo.ui.slider`（拉桿群）、`marimo.ui.button`（跳轉按鈕）
- **資料流：** 拉桿 → 矩陣 → `np.linalg.eig` → 特徵值 → plotly scatter update
- **效能：** 12 格 grid view 不需即時計算（預先計算範例固定值），只 Zoom view 觸發即時計算（每次拉桿 < 5ms）

##### M. 延伸與替代方案

- **延伸 1：** Tier 2 升級 — 增加「4×4 / 5×5 矩陣支援」（部分類別需更多參數）
- **延伸 2：** Tier 3 候選 — 整合 [Matrix World](appendix-matrix-world.md) 同心橢圓地圖，讓使用者點 Matrix World 任一圈層 → 自動跳到 Map of Eigenvalues 對應格
- **替代方案：** 純 HTML + D3 可實現相同 dashboard，但 D3 需手寫複數計算（不如 numpy 方便）

---

### 章末延伸

- **後續章節連結：** [→ § Matrix World 附錄](appendix-matrix-world.md)
- **回到主章節：** [→ §6.4 EVD（對稱類詳細展開）](ch06e-QLQ.md) / [→ §6.5 SVD（推廣到任意矩陣）](ch06f-USV.md)
- **延伸閱讀：**
  - Hiranabe 原 slidedeck：<https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf>
  - 博客介紹：<https://anagileway.com/2021/10/01/map-of-eigenvalues/>
  - Strang《Linear Algebra for Everyone》第 7 章「Eigenvalues and Eigenvectors」

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 596–602（References 第 3 條，附 PDF 連結）
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 578–584
- **原始 slidedeck：** [`MapofEigenvalues.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf)（v1.x，Kenji Hiranabe 2021 獨立發布）
- **作者：** Kenji Hiranabe（[twitter @hiranabe](https://twitter.com/hiranabe)，<https://anagileway.com>）
- **PNG 重核（S10）：** **無 `using XX` 標記**（HANDOFF 預估「可能標 P3」推翻；附錄是「地圖層級」非 Pattern 套用層級）
- **授權：** Apache 2.0

---

## 附錄 B：矩陣世界（Matrix World）— 全書地圖

> **原書頁碼：** 英文版 References 第 4 條（p.34）/ 簡中版同
> **對應 .tex 段落：** `from-tex/en.md` 第 604–610 行（References 區）/ 完整 PDF：[`MatrixWorld.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf)
> **本章圖數：** 1（`MatrixWorld.png`）
> **本章 VizMark 數：** 1（⭐⭐⭐ Tier 2 旗艦索引地圖 — S12+ 將作為「全書互動式教材的首頁」）
> **PNG `using XX` 標記：** **無**（S10 PNG 重核確認 — 圖內標記是 Strang《Linear Algebra for Everyone》的 section number（1.4 / 7.1 / 4.4 / 6.2 / 6.3 / 4.2 / 2.4 / 3.5 等），不是本書 Pattern 標記）
> **狀態：** [x] 已完成

---

### 章節摘要

《Matrix World》是 Kenji Hiranabe 於 2020 年發布、2023 年 v1.5 修訂的獨立 slidedeck，**並非《Linear Algebra for Everyone》主書內容**，而是「**所有矩陣類別的同心橢圓全景地圖**」。它把從最廣的「**矩陣 $m \times n$**」開始，一層一層往內縮，最終縮到「**單位矩陣 $I$ + 零矩陣 $O$**」這個最核心。每一層橢圓代表一類矩陣的**繼承關係**（內層 ⊂ 外層）：方陣 ⊂ 矩陣、可對角化 ⊂ 方陣、Normal ⊂ 可對角化、對稱 ⊂ Normal、正定 ⊂ 對稱 ... 直到 $I, O$。每層都標註「**對應的矩陣分解**」（如外圈標 $A = CR$ / $A = U\Sigma V^{\mathrm{T}}$、方陣層標 $A = QR$ / $A = LU$、對稱層標 $S = Q\Lambda Q^{\mathrm{T}}$、可對角化層標 $A = X\Lambda X^{-1}$）+「**對應 Strang 書的 section number**」（1.4 / 7.1 / 4.4 / 2.3 / 6.2 / 6.3 / 4.2 等）。本附錄是**全書 §1–§6 的「視覺索引」**，每個元素都 pointer 到對應章節 + VizScript。互動式版本 ⭐⭐⭐ Tier 2 旗艦規格：「點任一橢圓 / 標籤 / 分解符號 → 自動跳到對應章節 + VizScript」，是 S12+ 完成後**互動式教材的首頁**。

---

### 數學要點

#### 1. 同心橢圓的繼承層次（核心 ⭐）

> Matrix World 的核心邏輯是：**外層橢圓包含內層橢圓**，數學上表示「**外層的矩陣集合 ⊇ 內層**」。也就是「**內層的矩陣是外層的特例**」 — 性質越特殊、約束越多、橢圓越內。

**完整 11 層繼承樹（從外到內）：**

| 層級 | 矩陣類別 | 定義 / 約束 | 對應 Strang 書 section | 對應本互動式版本 |
|---|---|---|---|---|
| **L0（最外）** | **Matrix $m \times n$** | 任意實矩陣 | 1.4 | [ch01](ch01-viewing-matrix.md) |
| L1 | 含分解 $A = CR$ / $A = U\Sigma V^{\mathrm{T}}$ | 任意矩陣可分解 | 1.4 / 7.1 | [ch06b CR](ch06b-CR.md) / [ch06f SVD](ch06f-USV.md) |
| **L2** | **Square Matrix $n \times n$** | $m = n$ | — | [ch06](ch06a-five.md) |
| L2a | Invertible | $\det A \neq 0$，$\forall \lambda \neq 0$ | — | [ch06f §6.5](ch06f-USV.md) |
| L2b | Singular | $\det A = 0$，$\exists \lambda = 0$ | — | [Map of Eigenvalues](appendix-map-eigenvalues.md) |
| L3 | 含分解 $A = QR$ / $A = LU$ | 方陣分解 | 4.4 / 2.3 | [ch06d QR](ch06d-QR.md) / [ch06c LU](ch06c-LU.md) |
| **L4** | **Diagonalizable** | $\exists X, \Lambda: A = X\Lambda X^{-1}$，$X$ 可逆 | 6.2 | [ch06e EVD](ch06e-QLQ.md) §7 |
| L4a | 含分解 $A = X\Lambda X^{-1}$ | 一般可對角化 | 6.2 | [ch06e](ch06e-QLQ.md) |
| L4b | 不可對角化（Jordan form）| $A = X J X^{-1}$，$J$ 含 Jordan 塊 | A7 | [ch06e § Jordan 補述](ch06e-QLQ.md) |
| **L5** | **Normal** | $A^{\mathrm{T}}A = A A^{\mathrm{T}}$，**正交對角化** | A5 | [ch06e § 對稱推廣](ch06e-QLQ.md) |
| **L6** | **Symmetric** | $S = S^{\mathrm{T}}$，$\forall \lambda \in \mathbb{R}$ | 2.4 | [ch06e EVD](ch06e-QLQ.md) §1 |
| L6a | 含分解 $S = Q\Lambda Q^{\mathrm{T}}$ | 對稱譜分解 | 6.3 | [ch06e](ch06e-QLQ.md) |
| L7a | **Positive Semidefinite** | $\forall \lambda \geq 0$，$\forall A^{\mathrm{T}}A$ | 6.3 | [Map of Eigenvalues](appendix-map-eigenvalues.md) |
| **L7b** | **Positive Definite** | $\forall \lambda > 0$ | 6.3 | [Map of Eigenvalues](appendix-map-eigenvalues.md) |
| L8a | **Orthogonal** | $Q^{-1} = Q^{\mathrm{T}}$，$\forall \| \lambda \| = 1$ | 4.4 | [ch06d QR](ch06d-QR.md) |
| L8b | Permutation | $Q$ 為單位矩陣的列排列 | 2.4 | [ch05 (P1)(P2)](ch05-patterns.md) |
| **L9** | **Projection** | $P^2 = P = P^{\mathrm{T}}$，$\lambda \in \{0, 1\}$ | 4.2 | [ch05 (P4)](ch05-patterns.md) / [ch06d QR](ch06d-QR.md) |
| **L10** | **Diagonal** | 對角矩陣，$\Sigma = \text{diag}(\sigma^2, \sigma^2)$、$\Lambda = \text{diag}(\lambda, \lambda)$ | — | [ch05 (P1)(P2)](ch05-patterns.md) |
| **L11（最內）** | **$I, O$** | 單位矩陣 + 零矩陣 | — | [Map of Eigenvalues](appendix-map-eigenvalues.md) |

#### 2. 偽反矩陣的全矩陣統一公式（底部標註）

> 圖底部標：$A^{-1} = V\Sigma^{-1}U^{\mathrm{T}} \quad \leftrightarrow \quad A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ (3.5, 7.4)

這是 **Matrix World 的最重要單一發現** — Strang 把「逆矩陣（只對可逆方陣有效）」與「**Moore-Penrose 偽反矩陣 $A^{+}$**（對任意矩陣有效）」用 **SVD 統一**：

$$
A = U \Sigma V^{\mathrm{T}} \implies
\begin{cases}
A^{-1} = V \Sigma^{-1} U^{\mathrm{T}} & \text{若 } A \text{ 方且可逆} \\
A^{+} = V \Sigma^{+} U^{\mathrm{T}} & \text{對任意 } A \in \mathbb{R}^{m \times n}
\end{cases}
$$

其中 $\Sigma^{+}$ 是 $\Sigma$ 的偽反（$\sigma_p > 0$ 取倒數，$\sigma_p = 0$ 維持 0）。**$A^{+}$ 把「逆矩陣」這個只對可逆方陣有效的概念，推廣到所有 $m \times n$ 矩陣** — 這是 SVD 的核心應用之一（已在 [ch06f VizScript-01 4 應用切換](ch06f-USV.md#vizscript-01) 詳述）。

#### 3. Matrix World 的兩條軸線

> Matrix World 不只是同心橢圓 — 它把矩陣分類**沿兩條軸線**展開：

##### 軸線 A：縱深（外 → 內）= 性質越特殊

```
Matrix → Square → Diagonalizable → Normal → Symmetric → Positive Definite → Diagonal → I, O
```

每層加上一個約束（$m = n$、可對角化、$A^{\mathrm{T}}A = AA^{\mathrm{T}}$、$S = S^{\mathrm{T}}$、$\lambda > 0$、...），直到單位矩陣 $I$ 與零矩陣 $O$（最強約束）。

##### 軸線 B：橫向（左 ↔ 右）= 對稱 vs 一般

每層左半多放「**一般情形的分解**」（$A = X\Lambda X^{-1}$ 對角化、$A = LU$ 三角化、$A = QR$ Gram-Schmidt），右半放「**正交 / 對稱版本**」（$S = Q\Lambda Q^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$、Permutation 對角）。**這是 §6 五大分解的「視覺地圖化」** — 看一張圖即可知道每個分解屬於哪一類矩陣、誰是誰的特例。

#### 4. 連結 §6 五大分解總覽

| 五大分解 | 在 Matrix World 中的位置 | 適用矩陣 | 本互動式版本 |
|---|---|---|---|
| $A = CR$ | **最外層 L1** | 任意矩陣 | [ch06b](ch06b-CR.md) |
| $A = U\Sigma V^{\mathrm{T}}$ | **最外層 L1**（與 CR 同層）| 任意矩陣 | [ch06f](ch06f-USV.md) |
| $A = LU$ | L3（方陣層）| 方陣（多數可解 $A\mathbf{x}=\mathbf{b}$）| [ch06c](ch06c-LU.md) |
| $A = QR$ | L3（方陣層）+ L8（正交層補強）| 方陣（含瘦長 $m \geq n$）| [ch06d](ch06d-QR.md) |
| $S = Q\Lambda Q^{\mathrm{T}}$ | **L6（對稱層）** | 僅對稱矩陣 | [ch06e](ch06e-QLQ.md) |

**讀圖直覺：** 從外往內，分解越「特化」、適用範圍越窄、但結構越優美。**SVD 是「**唯一一個適用任意矩陣**」的分解** — 這就是為什麼 SVD 是「**集大成終章**」（[ch06f](ch06f-USV.md) 已詳述）。

---

### 圖片詳細描述（Figure Description）

#### Figure B.1: 矩陣世界（Matrix World）— v1.5（2023-03-02）

**圖檔：** `docs/book/figs-png/MatrixWorld.png`（原始 PDF：`MatrixWorld.pdf` v1.5）
**原書頁碼：** Slidedeck 獨立發布（References 第 4 條，v1.5 修訂版）
**所屬章節：** 附錄 B

##### 視覺結構 (Visual Structure)

整體**一張大圖**呈現「**同心橢圓宇宙**」：

- **整體布局：** 中央是橢圓巢狀結構（從最外的「Matrix ($m \times n$)」一直縮到最內的「$I, O$」），左右兩側散佈著「**範例矩陣**」（如 $\Lambda = \bigl[\begin{smallmatrix}1&2&3\\4&5&6\end{smallmatrix}\bigr]$、$\Lambda = \bigl[\begin{smallmatrix}2&1\\0&2\end{smallmatrix}\bigr]$、$\Lambda = \bigl[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr]$ 等）+「**分解符號 + section number**」（深灰底白字的標籤如「1.4 $A=CR$」「7.1 $A=U\Sigma V^{\mathrm{T}}$」）

- **同心橢圓層次（從外到內）：**
  1. **最外橢圓：** 標 "Matrix ($m \times n$)"，內含「$A = CR$」(1.4) 與「$A = U\Sigma V^{\mathrm{T}}$」(7.1)，標註「row rank = column rank」「SVD: orthonormal basis $U, V$」
  2. **第 2 層：** 「Square Matrix ($n \times n$)」，分為「Invertible（$\det(\Lambda) \neq 0$, all $\lambda \neq 0$）」與「Singular（at least one $\lambda = 0$, $\det(\Lambda) = 0$）」
  3. **第 3 層：** 「$A = QR$」(4.4，左 Gram-Schmidt) 與「$A = LU$」(2.3，右 Triangularize，「$U$ has at least one zero row」說明）
  4. **第 4 層：** "Diagonalizable" + 兩種分解：「$A = X\Lambda X^{-1}$」(6.2，左) 與「$A = XJX^{-1}$」(A7，右，$J$ = Jordan form)
  5. **第 5 層：** "Normal" (A5)，"$A^{\mathrm{T}}A = AA^{\mathrm{T}}$, diagonalizable by orthogonal matrix"
  6. **第 6 層（重要）：** "Symmetric" (2.4)，"$S = S^{\mathrm{T}}$, all $\lambda$ are real"，含「$S = Q\Lambda Q^{\mathrm{T}}$」(6.3) 與「Positive Semidefinite」(6.3) 兩標籤
  7. **第 7 層：** "Orthogonal" (4.4)，"$Q^{-1} = Q^{\mathrm{T}}$, all $|\lambda| = 1$"，內含 "Permutation" (2.4) 「permutation of $I$, all $\lambda$ are roots of 1」
  8. **第 8 層：** "Projection" (4.2)，"$P^2 = P = P^{\mathrm{T}}, \lambda = 1$ or $0$"
  9. **第 9 層：** "Diagonal"，$\Sigma = \bigl[\begin{smallmatrix}\sigma^2&\\&\sigma^2\end{smallmatrix}\bigr]$ 與 $\Lambda = \bigl[\begin{smallmatrix}\lambda&\\&\lambda\end{smallmatrix}\bigr]$
  10. **第 10 層：** "Positive Definite" (6.3)，"all $\lambda > 0$"
  11. **最內層：** "$I, O$"（單位矩陣 + 零矩陣）

- **底部標：** $A^{-1} = V\Sigma^{-1}U^{\mathrm{T}} \leftrightarrow A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ (3.5, 7.4) — 偽反矩陣統一公式

- **右上角圖例：** "Matrix Factorization"（深灰底，矩陣分解標籤）+ "Appearing section"（淺灰底，Strang 書 section number）

- **左下角署名：** "Drawn by Kenji Hiranabe / with the help of Prof. Gilbert Strang / (v1.5, Mar.2nd, 2023)" + 右下 CC-BY 授權標誌

- **整體色調：** 同心橢圓深藍細線 `#1f77b4`、分解標籤深灰底 `#666666` + 白字、section number 淺灰底 + 黑字、範例矩陣黑色純文字無背景；風格冷靜學術，無花俏色彩

- **視覺引導：** 讀者**先看最外橢圓**（理解「這是所有矩陣的全景」）→ **沿軸線縱深往內**（每層加一個約束）→ **對照分解符號**（每層適用的矩陣分解）→ **看 section number**（Strang 書中對應的詳細展開）

##### 數學內容 (Mathematical Content)

**同心橢圓的集合論表達：**

$$
\{I, O\} \subset \text{Diagonal} \subset \text{Positive Definite} \subset \text{Symmetric} \subset \text{Normal} \subset \text{Diagonalizable} \subset \text{Square} \subset \text{Matrix}
$$

**對偶分支（向左 / 向右）：**

$$
\begin{cases}
\text{左分支（一般）：} & A = X\Lambda X^{-1} \quad (\text{可對角化}) \\
\text{右分支（對稱）：} & S = Q\Lambda Q^{\mathrm{T}} \quad (\text{對稱對角化}) \\
\text{底層統一：} & A^{+} = V\Sigma^{+}U^{\mathrm{T}} \quad (\text{適用任意 } A) \\
\end{cases}
$$

**11 層繼承樹的層數約束遞增表：**

$$
\begin{array}{ll}
\text{Matrix:} & \text{無約束} \\
\text{Square:} & m = n \\
\text{Diagonalizable:} & \exists X: A = X \Lambda X^{-1} \\
\text{Normal:} & A^{\mathrm{T}} A = A A^{\mathrm{T}} \\
\text{Symmetric:} & S = S^{\mathrm{T}} \\
\text{Positive Semidefinite:} & \forall \lambda \geq 0 \\
\text{Positive Definite:} & \forall \lambda > 0 \\
\text{Orthogonal:} & Q^{\mathrm{T}}Q = I \\
\text{Projection:} & P^2 = P = P^{\mathrm{T}} \\
\text{Diagonal:} & A_{ij} = 0 \text{ for } i \neq j \\
\{I, O\}: & A = I \text{ or } A = O \\
\end{array}
$$

##### 直覺解讀 (Intuition)

Matrix World 是「**矩陣分類學的視覺百科**」 — 把所有重要矩陣類別、五大分解、對應 Strang 書章節**整合在一張圖**。**最重要的三條洞察：**

**洞察 1：「外層的矩陣分解適用更廣，內層的分解更精緻」** — 最外層的 $A = CR$ 和 $A = U\Sigma V^{\mathrm{T}}$ 適用**任意矩陣**，但分解結構相對「弱」（CR 的 $C$/$R$ 不對稱、SVD 的 $U/V$ 雖然正交但需排序）。最內層的對稱譜分解 $S = Q\Lambda Q^{\mathrm{T}}$ 只適用對稱矩陣，但結構**最優美**（$Q$ 兩側對稱、$\Lambda$ 對角全實）。**這個「廣 vs 精」的折衷是 §6 五大分解設計的核心邏輯**。

**洞察 2：「偽反矩陣 $A^{+}$ 統一了所有逆運算」** — 圖底部「$A^{-1} = V\Sigma^{-1}U^{\mathrm{T}} \leftrightarrow A^{+} = V\Sigma^{+}U^{\mathrm{T}}$」是整個 Matrix World 的「**底層統一定理**」。**任何矩陣**（含 singular、瘦長、矮胖）都可用 SVD 算偽反，這把「解 $A\mathbf{x}=\mathbf{b}$」從「方陣可逆」推廣到「**任意矩陣的最小範數解**」（[ch06f VizScript-01 推薦系統 / 矩陣補全 應用](ch06f-USV.md#vizscript-01) 的核心應用）。

**洞察 3：「Symmetric 是矩陣世界的『樞紐』類別」** — 從圖中可見：
- Symmetric → Positive Semidefinite → Positive Definite 是**連續正定性**的階梯
- Symmetric → $S = Q\Lambda Q^{\mathrm{T}}$ 是**正交對角化**的標誌
- Symmetric ⊂ Normal ⊂ Diagonalizable 是**對稱推廣**的階梯
- 任意矩陣 $A$ → $A^{\mathrm{T}}A$ 是「**從任意推導出對稱**」的標準操作（SVD 構造算法核心，見 [ch06f VizScript-03 4 子空間 SVD 構造](ch06f-USV.md#vizscript-03)）

**常見誤解：**

- **「Diagonal ⊂ Positive Definite ⊂ Symmetric — 是否所有對角矩陣都是正定？」** 不！只有「對角元全正」的對角矩陣才是正定。圖中 Diagonal 在 Positive Definite **內**只是表示「**對角矩陣是正定矩陣的一個重要子例**」（若對角元正則正定）。實際上「對角元含負數」的對角矩陣（如 $\bigl[\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr]$）是 Symmetric 但非 Positive Definite。
- **「Normal ⊂ Diagonalizable — 是否所有 normal 都可對角化？」** 是！這正是「Normal」的定義：**用正交矩陣 $Q$ 對角化**。Normal 是「**對稱矩陣的複數版本推廣**」（用 unitary 取代 orthogonal、Hermitian 取代 symmetric）。

**對比另一種看法（Map of Eigenvalues 並列網格）：**

- **Matrix World**（本附錄）用「**同心橢圓**」看類別**繼承**關係 — 適合「**理解誰是誰的特例**」
- **Map of Eigenvalues**（[appendix-map-eigenvalues.md](appendix-map-eigenvalues.md)）用「**並列網格**」看特徵值**位置**指紋 — 適合「**分類辨識**」

兩個附錄是「**同一矩陣分類問題的對偶視覺化**」 — Matrix World 從「**繼承結構**」切入，Map of Eigenvalues 從「**幾何指紋**」切入。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [互動式索引地圖 + 跳轉 dashboard] ⭐⭐⭐ Tier 2 旗艦（**S12+ 將作為「全書互動式教材的首頁」**）
> **位置：** Figure B.1 / 附錄 B 整圖
> **核心概念：** 同心橢圓全書地圖 + 點任一元素跳轉到對應章節 / VizScript
> **互動梗概：** 11 層同心橢圓互動式呈現，每層 hover 顯示說明 + click 觸發兩種行為之一：（A）展開該層的數學定義 + 範例矩陣 mini-dashboard；（B）「→ 跳轉到 chXX 詳細展開」直接導向對應章節。每個分解符號（$A = CR$、$A = LU$、$A = QR$、$A = X\Lambda X^{-1}$、$S = Q\Lambda Q^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$、$A^{+}$）都是可點擊按鈕，跳到對應 [ch06a–f](ch06a-five.md) 或 [Map of Eigenvalues](appendix-map-eigenvalues.md)。
> **詳見劇本：** VizScript-01（章末）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: 矩陣世界互動式索引地圖（Matrix World Interactive Index — Tier 2 旗艦）

**Tier：** ⭐⭐⭐ Tier 2 旗艦 — **S12+ 將作為「全書互動式教材的首頁」**（與 [ch06a VizScript-01](ch06a-five.md#vizscript-01) 五分解 dashboard 互補：前者是分類學索引、後者是分解視覺化索引）
**對應 VizMark：** Figure B.1 / VizMark-01

> 本劇本是「**全書導覽中樞**」 — 不重複實作任何具體分解動畫（那些都在各章 VizScript），只負責「**辨認矩陣類別 + 跳轉**」。每個橢圓 / 分解符號 / section number 都是 pointer，把整本互動式教材編織成「**從一張地圖點任何元素跳到對應章節 + VizScript**」的網狀結構。**這是 S12+ 完成後讀者進入教材的標準入口**。

##### A. 一句話定位

把 Hiranabe 的同心橢圓全書地圖實作為互動式 dashboard，11 層橢圓 + 13 個分解符號 + 8 個 Strang section number 全部可點擊跳轉到對應章節，作為全書互動式教材的「**首頁 + 導覽中樞**」。

##### B. 學習目標（Learning Outcome）

讀者完成此互動後能夠：

1. **建立全書地圖直覺**：看到「Matrix World 一張圖」即知道全書內容架構
2. **理解類別繼承**：理解 11 層橢圓的「**外層 ⊇ 內層 = 內層 ⊂ 外層**」邏輯
3. **連結五大分解的適用範圍**：知道哪個分解屬於哪層橢圓、為什麼 SVD 在最外層
4. **使用導覽**：從任一橢圓 / 分解 / section number 跳轉到本互動式版本對應 VizScript

##### C. 整體布局（單一旗艦視窗 + 三模式切換）

- **預設模式 = Map view：** 1200×900 px 主視窗呈現完整同心橢圓地圖（與原圖類似但向量化、可縮放）；右側 200 px 圖例區顯示「分解符號 = 灰底白字、section number = 淺灰底黑字、範例矩陣 = 純文字」+ Tier 標記顏色說明
- **Hover 模式：** 滑鼠 hover 任一橢圓 / 分解 / section number 時，該元素**高亮 + 上方浮現 tooltip** 顯示「**類別名 / 數學定義 / 對應章節 / 點此跳轉**」
- **Click 模式：** 點任一可互動元素觸發「**Mini-Dashboard panel 從右側滑出**」（panel 400 px 寬）顯示：類別詳細數學定義 + 3 個範例矩陣（含特徵值即時計算）+ 三個 pointer 按鈕「→ 看 [chXX] 詳解」「→ 看相關 VizScript」「→ 看 Map of Eigenvalues」

##### D. 可調參數（拉桿 + 過濾器）

- **層級可見度（11 個 checkbox）：** 可勾選/隱藏每層橢圓（如只看 L2 Square Matrix 以下）
- **分解符號可見度（13 個 checkbox）：** 可勾選/隱藏 13 個分解標籤
- **章節 highlight 過濾器：** 下拉選單「§1 / §2 / §3 / §4 / §5 / §6.1 / ... / §6.5」— 選一個章節即高亮 Matrix World 中所有對應元素（如選 §6.5 SVD 即高亮最外層橢圓 + $A = U\Sigma V^{\mathrm{T}}$ 標籤 + 底部 $A^{+}$ 公式 + Singular 區塊）
- **範例矩陣輸入區：** 拖入或貼上自訂 $3 \times 3$ 矩陣，**自動辨認該矩陣屬於哪些層**（高亮對應橢圓） — 例：輸入對稱矩陣，從外到內高亮 Matrix → Square → Diagonalizable → Normal → Symmetric

##### E. 顏色配方（沿用全書錨點 + 旗艦特色）

- **同心橢圓邊框：** 深藍 `#1f77b4` 細線（原圖風格）
- **Hover 高亮：** 該橢圓邊框 → 加粗 + 黃金 `#FFD700`（沿用 §6.x EVD 橢球變形色）
- **跳轉按鈕：** 白底深綠邊框 `#2ca02c`（全書一致）
- **分解符號標籤：** 深灰 `#666666` 底 + 白字（原圖風格）
- **範例矩陣（拖入）對應高亮：** 多層同時高亮時，按「**外 → 內**」漸變色（最外淺藍、最內紫紅）
- **章節過濾器高亮：** 該章節對應元素加粉紅 `#d62728` 點綴標記

##### F. 動畫節奏

- **Hover 進入：** 200ms 加粗邊框 + tooltip 淡入
- **Click 觸發 Panel：** 400ms 右側 panel 滑入（ease-out）+ Map view 縮小到 800 px 寬
- **章節過濾器切換：** 600ms 所有非該章節元素淡出至 30% 透明度，該章節元素閃爍 2 次後保持高亮
- **範例矩陣辨認動畫：** 800ms「**從外到內**」依序高亮對應層橢圓（呈現「往內收斂」直覺）
- **跳轉按鈕點擊：** 200ms fade-out Map view + 800ms 過渡到目標 VizScript

##### G. 公式同步顯示（Mini-Dashboard panel）

- 點任一元素後 panel 顯示：
  1. **類別名 + 集合論定義**（如「Symmetric: $\{S \in \mathbb{R}^{n \times n}: S = S^{\mathrm{T}}\}$」）
  2. **範例矩陣 3 個**（小、中、大，含特徵值即時計算與屬性檢驗）
  3. **相關分解的公式**（如 Symmetric panel 顯示 $S = Q\Lambda Q^{\mathrm{T}}$）
  4. **「Strang 書對應 section」連結**（如 [section 2.4 / 6.3](ch06e-QLQ.md)）
  5. **「相關 VizScript」按鈕列表**（如 Symmetric panel 列 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)、[Map of Eigenvalues VizScript-01](appendix-map-eigenvalues.md#vizscript-01)）

##### H. 驗收標準

1. **所有 11 層橢圓可獨立 hover/click**，無重疊干擾（z-index 從外到內遞增）
2. **13 個分解符號全部可點擊**並正確跳轉（CR / LU / QR / $X\Lambda X^{-1}$ / $S = Q\Lambda Q^{\mathrm{T}}$ / $U\Sigma V^{\mathrm{T}}$ / $A^{+}$ / $XJX^{-1}$ 等）
3. **範例矩陣輸入辨認準確：** 至少正確辨識 8 類常見矩陣（對稱 / 反對稱 / 正交 / 投影 / 對角 / Markov / 冪零 / 一般可對角化），辨認準確率 > 95%
4. **章節過濾器：** 切換 14 個章節（§1–§5 + ch06a–f + 3 附錄）任一，對應元素高亮無遺漏
5. **跳轉準確：** 任一 pointer 按鈕跳轉到對應 VizScript 並把上下文（如輸入矩陣）帶入

##### I. 邊界與健壯性

- **小尺寸矩陣輸入：** 1×1 純數字（純拉桿）視為 Diagonal 子集；2×2 / 3×3 完整辨認；4×4+ 顯示「**矩陣較大、辨認可能耗時 < 200ms**」 progress bar
- **數值容差：** 對稱性檢驗用 $\| S - S^{\mathrm{T}} \|_F < 10^{-6}$ 容差（避免浮點誤差）
- **退化情形：** 對全零矩陣 $O$ 直接跳到「$O$ 是最內層」說明
- **辨認失敗：** 若矩陣不屬於任一已知類別，提示「**此矩陣是『一般 Matrix』** — 從最外層開始」

##### J. 字幕 / 標題 / 圖例

- **頂部：** 「Matrix World — 全書互動式索引地圖（Hiranabe 2020 / v1.5 2023）」
- **左下：** 「點任一橢圓 / 分解符號 / section number 可跳轉」
- **右側圖例：** 圖例區固定 200 px，含「分解符號樣式 / section number 樣式 / hover 高亮樣式 / 跳轉按鈕樣式」
- **章末小字：** 「Drawn by Kenji Hiranabe, with the help of Prof. Gilbert Strang (CC-BY)」

##### K. 教學引導文案（嵌入互動視窗）

- **首次進入：** 「歡迎進入 Matrix World — 全書互動式索引地圖。**請從最外層橢圓 hover 起，沿著縱深往內探索**。每層代表一類矩陣，內層是外層的特例。點任一元素可跳到對應章節。」
- **章節過濾器觸發後：** 「您正在過濾 [§6.5 SVD] 相關元素 — 看 SVD 在 Matrix World 中的位置：**最外層橢圓（適用任意矩陣）+ 底部偽反公式**。點高亮元素跳到該 VizScript 詳細展開。」
- **範例矩陣輸入辨認後：** 「您輸入的矩陣屬於 [Symmetric] 類別 — 自外到內依序屬於：Matrix → Square → Diagonalizable → Normal → **Symmetric**。建議從 ch06e EVD 開始閱讀。」

##### L. 平台技術建議（S12+ 實作）

- **建議平台：** Marimo（反應式 notebook）+ plotly（同心橢圓可向量化縮放）+ matplotlib（高品質匯出 PNG / SVG 備用）
- **核心套件：** `plotly.graph_objects.Scatter`（橢圓 paths）、`marimo.ui.dropdown`/`checkbox`/`text_input`（過濾器 + 矩陣輸入）、`numpy.linalg.eig`（範例矩陣特徵值計算）、`scipy.linalg.norm`（對稱性容差檢驗）
- **資料結構：** 11 層橢圓 + 13 個分解符號 + 8 個 section number 共 32 個可點擊區域，全部編碼為 plotly traces 或 shapes
- **效能：** 預估 32 個 traces 渲染 < 100ms；hover/click 互動 < 50ms
- **匯出：** SVG 向量格式（保留印刷品質）+ 互動式 HTML（離線可用）

##### M. 延伸與替代方案

- **延伸 1（Tier 3 升級候選）：** 加入「**Matrix World 隨時間演化動畫**」 — 從最內 $\{I, O\}$ 出發，逐層展開到最外，視覺化「**矩陣分類學是如何構建的**」
- **延伸 2：** 整合 [Map of Eigenvalues](appendix-map-eigenvalues.md) — 點任一類別不只跳對應章節，也跳到 Map of Eigenvalues 同名格子看特徵值幾何位置
- **延伸 3：** 整合 [The Four Subspaces](appendix-four-subspaces.md) — 點 SVD 元素時自動展開 Strang 兩塊大餅圖（[ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) 的 SVD 整合版）
- **替代方案：** 純 HTML + D3 可實現相同 dashboard，D3 對 SVG 同心圓互動原生支援更好；但 numpy 計算特徵值 / 對稱性檢驗仍需 Python 後端

---

### 章末延伸

- **後續章節連結：** [→ § The Four Subspaces 附錄](appendix-four-subspaces.md)
- **前面章節連結：** [← § Map of Eigenvalues 附錄](appendix-map-eigenvalues.md)
- **回到主章節索引：** [→ §6 五大分解總覽](ch06a-five.md)
- **延伸閱讀：**
  - Hiranabe 原 slidedeck v1.5：<https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf>
  - 博客介紹：<https://anagileway.com/2020/09/29/matrix-world-in-linear-algebra-for-everyone/>
  - Strang《Linear Algebra for Everyone》第 1–7 章（Matrix World 中所有 section number 對應原書頁碼）

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 604–610（References 第 4 條，附 PDF 連結 + 圖嵌入）
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 586–592
- **原始 slidedeck：** [`MatrixWorld.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf)（v1.5，Hiranabe + Strang 合作 2023-03-02 修訂）
- **作者：** Kenji Hiranabe（with help of Prof. Gilbert Strang），CC-BY 授權
- **PNG 重核（S10）：** **無 `using XX` 標記**（圖內標記是 Strang 書 section number：1.4 / 7.1 / 4.4 / 6.2 / 6.3 / 4.2 / 2.4 / 2.3 / 3.5 / 7.4 + A5 / A7，不是本書 Pattern 標記）
- **授權：** Apache 2.0

---

## 附錄 C：四個基本子空間（The Four Subspaces and the Solutions to $A\mathbf{x} = \mathbf{b}$）

> **原書頁碼：** 英文版 References 第 5 條（p.34，無獨立 slidedeck，含於 4-Subspaces 圖）/ 簡中版同
> **對應 .tex 段落：** `from-tex/en.md` 第 612–617 行（References 區）/ 圖檔：`4-Subspaces.png`（與 §3 同款）
> **本章圖數：** 1（`4-Subspaces.png`，與 [ch03 § Figure 3.2](ch03-mat-vec.md) 同款）
> **本章 VizMark 數：** 1（⭐⭐ Tier 1 + pointer 指 [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) + [ch06f VizScript-03](ch06f-USV.md#vizscript-03)）
> **PNG `using XX` 標記：** **無**（S10 PNG 重核確認 — 4-Subspaces 圖是「基本概念圖」非 Pattern 套用層級）
> **狀態：** [x] 已完成

---

### 章節摘要

《The Four Subspaces and the Solutions to $A\mathbf{x} = \mathbf{b}$》是 Gilbert Strang 設計、Kenji Hiranabe 繪製的標誌性視覺化，**並非《Linear Algebra for Everyone》主書內容**，而是 Strang 在多本著作中反覆強調的「**線性代數最重要的一張圖**」。它把矩陣 $A \in \mathbb{R}^{m \times n}$ 對應的**四個基本子空間** — 行空間 $\mathbf{C}(A^{\mathrm{T}})$ + 零空間 $\mathbf{N}(A)$（在 $\mathbb{R}^n$ 上）和列空間 $\mathbf{C}(A)$ + 左零空間 $\mathbf{N}(A^{\mathrm{T}})$（在 $\mathbb{R}^m$ 上）— 用「**兩塊大餅圖**」呈現，並標註「**互相垂直**」「**維度和 = 全空間維度**」兩條關鍵關係。本附錄是 §3 [Matrix × Vector](ch03-mat-vec.md) + §6.5 [SVD](ch06f-USV.md) 的「**整合性收尾**」 — 與主章節相比，附錄**重「鳥瞰整合」而非「從零教學」**：（1）補 SVD 構造 4 子空間的**完整算法視角**（從 EVD 整合到 SVD 對齊）；（2）補解 $A\mathbf{x} = \mathbf{b}$ 的**完整解空間結構**（一般解 = 特解 + 零空間解）；（3）pointer 到 §3 / §6.5 已完成的旗艦 VizScript（[ch03 VizScript-02](ch03-mat-vec.md#vizscript-02)、[ch06f VizScript-03](ch06f-USV.md#vizscript-03)）。

---

### 數學要點

#### 1. 四個基本子空間的定義與維度

> 給定矩陣 $A \in \mathbb{R}^{m \times n}$ rank $r$，存在**四個基本子空間**：

| 子空間 | 符號 | 定義 | 維度 | 所屬全空間 |
|---|---|---|---|---|
| **列空間** | $\mathbf{C}(A)$ | $\{A\mathbf{x}: \mathbf{x} \in \mathbb{R}^n\}$（所有 $A\mathbf{x}$） | $r$ | $\mathbb{R}^m$ |
| **零空間** | $\mathbf{N}(A)$ | $\{\mathbf{x}: A\mathbf{x} = \mathbf{0}\}$ | $n - r$ | $\mathbb{R}^n$ |
| **行空間** | $\mathbf{C}(A^{\mathrm{T}})$ | $\{\mathbf{y} A: \mathbf{y} \in \mathbb{R}^m\}$（所有 $\mathbf{y}A$） | $r$ | $\mathbb{R}^n$ |
| **左零空間** | $\mathbf{N}(A^{\mathrm{T}})$ | $\{\mathbf{y}: \mathbf{y} A = \mathbf{0}\}$ | $m - r$ | $\mathbb{R}^m$ |

#### 2. 兩條核心關係（圖中明示）

##### 關係 A：正交補關係

$$
\mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}}) \quad \text{（在 } \mathbb{R}^n \text{ 上）}
$$
$$
\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}}) \quad \text{（在 } \mathbb{R}^m \text{ 上）}
$$

##### 關係 B：直和分解

$$
\mathbb{R}^n = \mathbf{N}(A) \oplus \mathbf{C}(A^{\mathrm{T}}) \quad \text{維度 } n = (n-r) + r
$$
$$
\mathbb{R}^m = \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}}) \quad \text{維度 } m = r + (m-r)
$$

#### 3. SVD 構造 4 子空間的標準正交基底（附錄重點 ⭐）

> §6.5 SVD 的 $A = U \Sigma V^{\mathrm{T}}$ 提供「**4 子空間的標準正交基底**」 — 這是 SVD 最深刻的應用之一。

**從 SVD 直接讀出 4 子空間基底：**

設 $A \in \mathbb{R}^{m \times n}$ rank $r$，SVD 分解為 $A = U \Sigma V^{\mathrm{T}}$，其中 $U = [\mathbf{u}_1, \ldots, \mathbf{u}_m]$、$V = [\mathbf{v}_1, \ldots, \mathbf{v}_n]$、$\Sigma$ 對角元 $\sigma_1 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots$。則：

$$
\begin{array}{ll}
\mathbf{C}(A) & = \mathrm{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_r\} \quad \text{（} U \text{ 前 } r \text{ 列）} \\
\mathbf{N}(A^{\mathrm{T}}) & = \mathrm{span}\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\} \quad \text{（} U \text{ 後 } m-r \text{ 列）} \\
\mathbf{C}(A^{\mathrm{T}}) & = \mathrm{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_r\} \quad \text{（} V \text{ 前 } r \text{ 列）} \\
\mathbf{N}(A) & = \mathrm{span}\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\} \quad \text{（} V \text{ 後 } n-r \text{ 列）} \\
\end{array}
$$

**SVD 的「**4 子空間最佳對齊性質**」：** $U$ 和 $V$ 是**標準正交矩陣**（$U^{\mathrm{T}}U = I_m$、$V^{\mathrm{T}}V = I_n$），所以「**列空間的基底彼此正交、零空間的基底彼此正交**」 — 這是其他分解（CR / LU / QR / EVD）無法提供的優勢。**SVD 同時最優地對齊 4 子空間，是「線性代數最完整的視覺定理」**。詳細展開見 [ch06f VizScript-03 4 子空間 SVD 構造](ch06f-USV.md#vizscript-03)。

#### 4. 解 $A\mathbf{x} = \mathbf{b}$ 的完整解空間結構（附錄重點 ⭐）

> 用 4 子空間結構可以**完整解析** $A\mathbf{x} = \mathbf{b}$ 的解（這是 Strang 圖題目「**Solutions to $A\mathbf{x} = \mathbf{b}$**」的由來）。

##### 情況 A：$\mathbf{b} \in \mathbf{C}(A)$（有解）

**特解：** $\mathbf{x}_p$ 滿足 $A\mathbf{x}_p = \mathbf{b}$
**通解：** $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n$，其中 $\mathbf{x}_n \in \mathbf{N}(A)$

$$
\boxed{\text{完整解} = \text{特解} + \text{零空間解}}
$$

**幾何視覺：** 通解是 $\mathbb{R}^n$ 中一個「**平移過的子空間**」（仿射子空間） — 通過 $\mathbf{x}_p$ 平行於 $\mathbf{N}(A)$ 的子空間。

**唯一解條件：** $\mathbf{N}(A) = \{\mathbf{0}\}$（即 $r = n$，全列獨立）

##### 情況 B：$\mathbf{b} \notin \mathbf{C}(A)$（無解）

**最小二乘解：** 找 $\mathbf{x}^*$ 使 $\| A\mathbf{x}^* - \mathbf{b} \|^2$ 最小
**公式：** $\mathbf{x}^* = A^{+} \mathbf{b}$（用偽反矩陣，見 [Matrix World 附錄](appendix-matrix-world.md) 底部公式）

**幾何視覺：** $\mathbf{x}^*$ 把 $\mathbf{b}$ **投影到** $\mathbf{C}(A)$（在 $\mathbb{R}^m$ 上正交投影）然後反推回 $\mathbb{R}^n$。

##### 通用解（含正則化）

$$
\mathbf{x}^* = A^{+} \mathbf{b} = V \Sigma^{+} U^{\mathrm{T}} \mathbf{b}
$$

這是 SVD 提供的「**最小二乘 + 最小範數**」最優解 — 比任何單純的「特解 + 零空間解」更穩健（避免病態方程的浮點誤差放大）。

#### 5. 與 §3、§6.5 主章節的整合對照（附錄定位）

| 概念 | §3 主章節 | §6.5 主章節 | 本附錄補充 |
|---|---|---|---|
| 4 子空間定義 | [ch03 §3 第 2 段](ch03-mat-vec.md) 從 $A\mathbf{x}$ 與 $\mathbf{y}A$ 引入 | [ch06f VizScript-03](ch06f-USV.md#vizscript-03) SVD 對齊 | **整合鳥瞰** — 4 子空間是 §3 入門 + §6.5 集大成 |
| 兩塊大餅圖視覺 | [ch03 Figure 3.2](ch03-mat-vec.md) + [VizScript-02](ch03-mat-vec.md#vizscript-02) ⭐⭐⭐ Tier 3 候選 | [ch06f VizScript-03](ch06f-USV.md#vizscript-03) SVD 構造版 | **pointer 整合** — 本附錄不重複實作 |
| SVD 基底對齊 | 未深入 | [ch06f VizScript-03 構造算法](ch06f-USV.md#vizscript-03) | **正交分解定理完整版** |
| 解 $A\mathbf{x}=\mathbf{b}$ | [ch03 §3 第 3 段](ch03-mat-vec.md) 零空間引入 | [ch06f VizScript-01 推薦系統 / 矩陣補全應用](ch06f-USV.md#vizscript-01) | **完整解空間結構** + 最小二乘 + 正則化 |
| 偽反矩陣 $A^{+}$ | 未涉及 | [ch06f §7 與其他分解關係](ch06f-USV.md)（總結表段，無對應 VizScript） | **整合定義 + 與 Matrix World 連結** |

**附錄定位：** 本附錄是「**§3 + §6.5 + Matrix World 三章的橋樑**」 — 不重複教學，只整合三章的觀點 + 補解 $A\mathbf{x}=\mathbf{b}$ 完整結構 + pointer 到旗艦 VizScript。

---

### 圖片詳細描述（Figure Description）

#### Figure C.1: 四個基本子空間（The Four Subspaces）— 無 `using` 標記，與 [ch03 Figure 3.2](ch03-mat-vec.md) 同款

**圖檔：** `docs/book/figs-png/4-Subspaces.png`（原始 EPS：`figs/4-Subspaces.eps`）
**原書頁碼：** §3 + References 第 5 條（同款圖）
**所屬章節：** 附錄 C（與 [ch03 §3](ch03-mat-vec.md) 共用此圖）

##### 視覺結構 (Visual Structure)

整體**左右對稱兩塊大餅**結構：

- **左塊（$\mathbb{R}^n$）：**
  - 上方大白色方塊（傾斜約 30°）標 "row space"、"all $\mathbf{y}A$"，方塊中央嵌粉紅色 3 個橫躺長條（**行向量**，標 $\mathbf{C}(A^{\mathrm{T}})$、$\dim = r$）
  - 下方小白色方塊標 "nullspace"、"$A\mathbf{x} = \mathbf{0}$"（標 $\mathbf{N}(A)$、$\dim = n-r$）
  - 兩塊垂直連接，標「perpendicular」並寫小直角符號
  - 左側標籤：$\mathbb{R}^n$、$\mathbf{C}(A^{\mathrm{T}})$、$\mathbf{N}(A)$
  - 底部標：$\mathbb{R}^n = \mathbf{N}(A) + \mathbf{C}(A^{\mathrm{T}})$、$\mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}})$

- **右塊（$\mathbb{R}^m$）：**
  - 上方大白色方塊（傾斜約 30° 鏡像）標 "column space"、"all $A\mathbf{x}$"，方塊中央嵌綠色 2 個直立長條（**列向量**，標 $\mathbf{C}(A)$、$\dim = r$）
  - 下方小白色方塊標 "left nullspace"、"$\mathbf{y}A = \mathbf{0}$"（標 $\mathbf{N}(A^{\mathrm{T}})$、$\dim = m-r$）
  - 標「perpendicular」+ 小直角符號
  - 右側標籤：$\mathbb{R}^m$、$\mathbf{C}(A)$、$\mathbf{N}(A^{\mathrm{T}})$
  - 底部標：$\mathbb{R}^m = \mathbf{C}(A) + \mathbf{N}(A^{\mathrm{T}})$、$\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}})$

- **上方箭頭：** $\mathbb{R}^n \xrightarrow{A \in \mathbb{R}^{m \times n}} \mathbb{R}^m$，表示「矩陣 $A$ 是從 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的映射」

- **整體色調：** 純白背景、深藍細線框 `#1f77b4`、行向量（左）粉紅 `#d62728`、列向量（右）綠色 `#2ca02c` — **這是全書配色錨點的「**起源**」**（[ch03 §3](ch03-mat-vec.md) 之後所有章節都沿用此配色）

- **視覺引導：** 讀者**先看上方箭頭**（理解 $A$ 是 $\mathbb{R}^n \to \mathbb{R}^m$ 映射）→ **看左塊**（$\mathbb{R}^n$ 拆成「行空間 + 零空間」兩個互相垂直子空間）→ **看右塊**（$\mathbb{R}^m$ 拆成「列空間 + 左零空間」兩個互相垂直子空間）→ **最後對照**「行空間和列空間維度都是 $r$」（圖的「秘密」 = **列秩 = 行秩定理**，[ch06b CR 章](ch06b-CR.md) 已詳述）

##### 數學內容 (Mathematical Content)

$$
A: \mathbb{R}^n \to \mathbb{R}^m, \quad A \in \mathbb{R}^{m \times n}, \quad \mathrm{rank}(A) = r \leq \min(m, n)
$$

**四個子空間的形式定義：**

$$
\begin{array}{ll}
\mathbf{C}(A) & = \mathrm{span}\{\mathbf{a}_1, \ldots, \mathbf{a}_n\} = \{A\mathbf{x}: \mathbf{x} \in \mathbb{R}^n\} \subset \mathbb{R}^m \\
\mathbf{N}(A) & = \{\mathbf{x} \in \mathbb{R}^n: A\mathbf{x} = \mathbf{0}\} \subset \mathbb{R}^n \\
\mathbf{C}(A^{\mathrm{T}}) & = \mathrm{span}\{\mathbf{a}^*_1, \ldots, \mathbf{a}^*_m\} = \{\mathbf{y} A: \mathbf{y} \in \mathbb{R}^m\} \subset \mathbb{R}^n \\
\mathbf{N}(A^{\mathrm{T}}) & = \{\mathbf{y} \in \mathbb{R}^m: \mathbf{y} A = \mathbf{0}\} \subset \mathbb{R}^m \\
\end{array}
$$

**正交分解定理（Strang's Fundamental Theorem of Linear Algebra）：**

$$
\begin{cases}
\mathbb{R}^n = \mathbf{N}(A) \oplus \mathbf{C}(A^{\mathrm{T}}), & \mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}}) \\
\mathbb{R}^m = \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}}), & \mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}}) \\
\dim \mathbf{C}(A) = \dim \mathbf{C}(A^{\mathrm{T}}) = r & \text{（列秩 = 行秩）} \\
\dim \mathbf{N}(A) = n - r, \quad \dim \mathbf{N}(A^{\mathrm{T}}) = m - r
\end{cases}
$$

##### 直覺解讀 (Intuition)

這張圖是「**Strang 對線性代數最重要的單一視覺貢獻**」 — 把矩陣 $A$ 的所有結構性質**壓縮到一張圖**。**最重要的三條洞察：**

**洞察 1：「兩塊大餅 = 兩個全空間 = 兩種對偶視角」** — 左塊看 $\mathbb{R}^n$（從「行向量」+「點積」角度，對應 [§3 (Mv1)](ch03-mat-vec.md)），右塊看 $\mathbb{R}^m$（從「列向量」+「線性組合」角度，對應 [§3 (Mv2)](ch03-mat-vec.md)）。**這是 §1–§3 教學主軸「**4 ways viewing a matrix**」的視覺收斂點**。

**洞察 2：「正交補定理 = 秩-零定理」** — 圖中「上塊（行/列空間）⊥ 下塊（零空間）」+ 兩塊維度相加 = 全空間維度，是 **rank-nullity theorem 的視覺呈現**：
$$
\dim \mathbf{C}(A^{\mathrm{T}}) + \dim \mathbf{N}(A) = r + (n-r) = n
$$
這個定理是線性代數最基本但最深刻的定理之一，圖把它變成「**一看就懂**」。

**洞察 3：「列秩 = 行秩 = $r$ 的圖示證明」** — 圖中左塊「行空間維度 = $r$」+ 右塊「列空間維度 = $r$」**兩個都標 $r$**。這就是 [ch06b CR 章](ch06b-CR.md) 詳述的列秩 = 行秩定理 — **CR 分解的 $C$ 是「列空間基底」、$R$ 是「行階梯形」，兩個視角的 $r$ 相同**。

**為什麼這張圖是 SVD 的「終極前奏」？**

§6.5 SVD 提供「**4 子空間的標準正交基底**」 — 用 $A = U \Sigma V^{\mathrm{T}}$ 同時把這四個子空間的基底**正交對齊**。**SVD 是 4-Subspaces 圖的「**填色版本**」 — 不只告訴你 4 個子空間存在，還給出每個子空間的「**最佳座標系**」**。詳見 [ch06f VizScript-03 SVD 4 子空間構造](ch06f-USV.md#vizscript-03)。

**常見誤解：**

- **「行空間和列空間是同一個東西嗎？」** 不！它們維度相同（都 $= r$），但**屬於不同的全空間**（$\mathbf{C}(A^{\mathrm{T}}) \subset \mathbb{R}^n$、$\mathbf{C}(A) \subset \mathbb{R}^m$）。當 $m \neq n$ 時兩個全空間維度不同，所以兩個子空間「**只是維度數字相同，是兩個獨立子空間**」。
- **「零空間和左零空間哪個比較重要？」** 對解 $A\mathbf{x}=\mathbf{b}$ 來說是**零空間**（決定解的多重性）；對解 $\mathbf{y}A=\mathbf{c}$ 來說是**左零空間**。對 SVD 而言**兩個同等重要**（都是 $U/V$ 的後段列）。

##### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [4 子空間整合互動 + 解 $A\mathbf{x}=\mathbf{b}$ 視覺化] ⭐⭐ Tier 1 + pointer
> **位置：** Figure C.1 / 附錄 C 整圖
> **核心概念：** 4 子空間正交分解 + SVD 構造基底 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構
> **互動梗概：** 採「**整合 pointer 策略**」 — 不重複實作 4 子空間動畫（已在 [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) 完成 ⭐⭐⭐ Tier 3 候選），不重複實作 SVD 構造（已在 [ch06f VizScript-03](ch06f-USV.md#vizscript-03) 完成）。本附錄 VizMark 只負責「**整合面板**」：左半重用 ch03 4 子空間結構視覺、右半新增「**解 $A\mathbf{x}=\mathbf{b}$ 完整結構互動**」（特解 + 零空間解 + 仿射子空間 + 最小二乘投影 + 偽反矩陣公式）+ 兩個跳轉按鈕。
> **詳見劇本：** VizScript-01（章末）

---

### 視覺化劇本（VizScripts）

#### VizScript-01: 4 子空間整合 + 解 $A\mathbf{x}=\mathbf{b}$ 視覺（Four Subspaces Integration — Tier 1 + pointer）

**Tier：** ⭐⭐ Tier 1 + pointer（核心整合面板，4 子空間結構動畫 pointer 到 [ch03 V-02](ch03-mat-vec.md#vizscript-02)，SVD 構造 pointer 到 [ch06f V-03](ch06f-USV.md#vizscript-03)）
**對應 VizMark：** Figure C.1 / VizMark-01

> 本劇本只負責**整合面板 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構新視覺**，4 子空間結構動畫（Strang 兩塊大餅）已在 ch03 V-02 ⭐⭐⭐ Tier 3 候選實作，SVD 構造（4 子空間基底正交對齊）已在 ch06f V-03 實作。本附錄不重複，透過按鈕「→ 看 4 子空間結構詳解」與「→ 看 SVD 4 基底構造」跳轉到對應章節。

##### A. 一句話定位

把 Strang 4-Subspaces 圖實作為「**整合面板**」 — 4 子空間結構與 SVD 基底構造由其他 VizScript 負責，本面板專注「**解 $A\mathbf{x}=\mathbf{b}$ 完整結構視覺**」（特解 + 零空間解 + 仿射子空間 + 最小二乘 + 偽反矩陣），讓讀者「**從 4 子空間直接看到所有 $A\mathbf{x}=\mathbf{b}$ 的可能解**」。

##### B. 學習目標（Learning Outcome）

讀者完成此互動後能夠：

1. **整合 §3 + §6.5 視角**：把入門期的 4 子空間概念與集大成期的 SVD 對齊整合
2. **理解 $A\mathbf{x}=\mathbf{b}$ 解空間**：知道完整解 = 特解 + 零空間平移、無解時用最小二乘
3. **連結偽反矩陣**：理解 $\mathbf{x}^* = A^{+}\mathbf{b}$ 是「**最小二乘 + 最小範數**」最優解
4. **連結 Matrix World**：理解本附錄與 [Matrix World](appendix-matrix-world.md) 底部偽反公式的對應

##### C. 整體布局（雙面板 + 跳轉按鈕）

- **左面板（400×600 px）：** 縮小版 4 子空間結構（重用 [ch03 V-02](ch03-mat-vec.md#vizscript-02) 視覺），無互動但顯示「→ 看 4 子空間結構詳解」按鈕
- **右面板（800×600 px，主互動）：** **「解 $A\mathbf{x}=\mathbf{b}$ 完整結構互動視覺」**：
  - 中央：3D 視角的 $\mathbb{R}^n$ 子空間表示（$n = 2$ 或 3）
  - 標出 $\mathbf{N}(A)$（紫色平面或線）
  - 標出 $\mathbf{x}_p$ 特解（金色點）
  - 標出 通解平面（$\mathbf{x}_p + \mathbf{N}(A)$，半透明黃色仿射子空間）
  - 標出 $\mathbf{x}^* = A^{+}\mathbf{b}$（綠色點，「最小範數最優解」位置）
  - 顯示 $A^{+}\mathbf{b}$ 是「**最近原點的通解**」直觀理解

- **上方控制條：** 拉桿選 $m, n \in \{2, 3\}$、輸入 $A$ 矩陣（自動算 rank $r$）、輸入 $\mathbf{b}$、選「有解 / 無解」情境

- **下方輸出區：** 顯示 $A^{+}$（用 SVD 算）、特解 $\mathbf{x}_p$、通解形式、最小二乘解 $\mathbf{x}^* = A^{+}\mathbf{b}$

##### D. 可調參數（拉桿）

- **矩陣 $A$ 維度：** $m, n \in \{2, 3\}$（保 3D 可視）
- **矩陣 $A$ 元素：** $a_{ij} \in [-3, 3]$ 步進 0.5
- **右側向量 $\mathbf{b}$：** $b_i \in [-3, 3]$ 步進 0.5
- **情境切換：** 「保證有解（$\mathbf{b}$ 在 $\mathbf{C}(A)$）/ 強制無解（$\mathbf{b}$ 在 $\mathbf{N}(A^{\mathrm{T}})$）/ 一般情形」

##### E. 顏色配方（沿用全書錨點）

- **零空間 $\mathbf{N}(A)$：** 紫色 `#9467bd` 半透明（沿 ch05 P3 / S09 4 子空間錨點）
- **特解 $\mathbf{x}_p$：** 金色 `#FFD700` 實心點（沿用 §6.x EVD 變形後橢球錨點）
- **通解平面（仿射子空間）：** 半透明黃色 alpha 0.3
- **最小範數最優解 $\mathbf{x}^*$：** 綠色 `#2ca02c` 實心點
- **列空間 $\mathbf{C}(A)$ 投影（右塊）：** 綠色半透明 alpha 0.3（與全書一致）
- **正交補 perpendicular 標記：** 灰直角符號

##### F. 動畫節奏

- **拉桿即時更新：** 矩陣 / 向量改變後，特解 / 通解平面 / 最優解以 300ms 平滑移動到新位置
- **情境切換動畫：** 800ms「保證有解 → 強制無解」過渡時，$\mathbf{b}$ 慢慢移出 $\mathbf{C}(A)$，最小二乘解 $\mathbf{x}^*$ 浮現（不再是 $\mathbf{x}_p$）
- **跨子空間切換：** 點「→ 看 4 子空間結構詳解」按鈕後，左面板放大、右面板淡出，整體切換到 [ch03 V-02](ch03-mat-vec.md#vizscript-02)

##### G. 公式同步顯示（右面板下方）

- 即時顯示：
  1. SVD 分解：$A = U \Sigma V^{\mathrm{T}}$（$U, \Sigma, V$ 矩陣即時更新）
  2. 偽反：$A^{+} = V \Sigma^{+} U^{\mathrm{T}}$
  3. 通解：$\mathbf{x} = \mathbf{x}_p + c_1 \mathbf{v}_{r+1} + \cdots + c_{n-r} \mathbf{v}_n$（$\mathbf{v}_j$ 是 SVD 的零空間基底）
  4. 最小範數最優解：$\mathbf{x}^* = A^{+}\mathbf{b}$（數值結果）
  5. 殘差：$\| A\mathbf{x}^* - \mathbf{b} \|_2$（若 > 0 表示無解情境）

##### H. 驗收標準

1. **3D 視覺正確：** 拉桿任意組合下，3D 視窗中的「**通解平面 = 平行 $\mathbf{N}(A)$ 通過 $\mathbf{x}_p$**」幾何關係始終成立
2. **最小範數性質：** $\mathbf{x}^* = A^{+}\mathbf{b}$ 確實是「**通解中最接近原點**」的點（可驗證 $\mathbf{x}^* \perp \mathbf{N}(A)$）
3. **無解情境準確：** 強制無解時，殘差 > 0 + $\mathbf{b}$ 在 $\mathbf{C}(A)$ 上的投影是 $A\mathbf{x}^*$
4. **跳轉正確：** 兩個跳轉按鈕分別準確跳到 [ch03 V-02](ch03-mat-vec.md#vizscript-02) 與 [ch06f V-03](ch06f-USV.md#vizscript-03)

##### I. 邊界與健壯性

- **rank 退化：** $A = O$ 時提示「零矩陣，所有 $\mathbf{x}$ 都是 $\mathbf{N}(A)$」+ 跳過 SVD 計算
- **數值容差：** 用 SVD 算 $A^{+}$ 時 $\sigma_p < 10^{-10}$ 視為 0（避免 1/0 爆炸）
- **超高維度：** $m, n > 3$ 時自動關閉 3D 視覺、改顯示「**4 子空間維度表 + 偽反公式**」

##### J. 字幕 / 標題 / 圖例

- **頂部：** 「**4 子空間 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構整合**（Strang's Big Picture Integration）」
- **底部圖例：** 「紫 = 零空間、金 = 特解、黃半透明 = 通解平面、綠 = 最小範數最優解、灰直角 = 正交」

##### K. 教學引導文案

- **首次進入：** 「**4 子空間是 §3 入門 + §6.5 集大成 + 整本書的『**結構主軸**』**。本附錄整合三種觀點。左面板看 4 子空間結構（→ 點按鈕看 ch03 V-02 詳解），右面板看 $A\mathbf{x}=\mathbf{b}$ 的完整解空間 — 拉桿改 $A, \mathbf{b}$，**注意通解 = 特解 + 零空間平移**。」
- **情境切換時：** 「現在 $\mathbf{b}$ 不在 $\mathbf{C}(A)$ 中 — 方程無精確解。但 SVD 提供 $\mathbf{x}^* = A^{+}\mathbf{b}$ 作為『**最小二乘最優解**』，最小化 $\| A\mathbf{x} - \mathbf{b} \|^2$。注意 $\mathbf{x}^*$ 同時也是『**通解中最接近原點**』的點（最小範數）。」

##### L. 平台技術建議（S12+ 實作）

- **建議平台：** Marimo + plotly 3D（仿射子空間可視）+ matplotlib（公式 LaTeX 渲染）
- **核心套件：** `numpy.linalg.svd`（SVD 計算偽反）、`numpy.linalg.pinv`（直接算 $A^{+}$ 對照驗證）、`plotly.graph_objects.Surface`（通解平面）、`marimo.ui.slider`（拉桿群）

##### M. 延伸與替代方案

- **延伸 1：** 加入 4 子空間的**正交投影矩陣**視覺（$P_C = A A^{+}$ 是「**到 $\mathbf{C}(A)$ 的正交投影**」、$P_{C^{\mathrm{T}}} = A^{+} A$ 是「**到 $\mathbf{C}(A^{\mathrm{T}})$ 的正交投影**」）
- **延伸 2：** 整合 [Map of Eigenvalues](appendix-map-eigenvalues.md) 中「投影矩陣 $P^2 = P = P^{\mathrm{T}}$」格 — 看正交投影矩陣的特徵值 $\lambda \in \{0, 1\}$
- **替代方案：** D3 + Three.js 可實現相同 3D 視覺，但需自寫線代計算（不如 numpy + scipy 方便）

---

### 章末延伸

- **後續章節連結：** 無（本附錄為全書最後）
- **回到全書索引：** [→ § Matrix World 全書地圖](appendix-matrix-world.md)（從這裡點任一元素跳到對應章節）
- **回到主章節：**
  - [→ §3 Matrix × Vector 入門（4 子空間首次出現）](ch03-mat-vec.md)
  - [→ §6.5 SVD 集大成（4 子空間正交對齊）](ch06f-USV.md)
- **延伸閱讀：**
  - Gilbert Strang, *Introduction to Linear Algebra*, 第 3.5 節「Dimensions of the Four Subspaces」
  - Strang YouTube 課程 18.06「Linear Algebra」第 14 講「The Four Fundamental Subspaces」
  - 線代核心定理：Fundamental Theorem of Linear Algebra（Strang）

---

### 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 612–617（References 第 5 條，無獨立 PDF，與 §3 圖共用）
- **原書簡中版：** 簡中 zh.md 無此 References 條目（簡中版只列 References 1–4，省略第 5 條）
- **圖檔：** `figs-png/4-Subspaces.png`（同款圖也用於 [ch03 §3](ch03-mat-vec.md) Figure 3.2）
- **作者：** Gilbert Strang（概念）+ Kenji Hiranabe（artwork）
- **PNG 重核（S10）：** **無 `using XX` 標記**（基本概念圖，非 Pattern 套用層級；4 子空間是 §3 主軸 + §6.5 SVD 對齊的基本結構）
- **授權：** Apache 2.0
