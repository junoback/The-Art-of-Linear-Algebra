# 序言（Foreword）— Gilbert Strang 推薦序與本書緣起

> **原書頁碼：** 英文版 p.1（書首）/ 簡中版 p.1
> **對應 .tex 段落：** `from-tex/en.md` 第 1–14 行 / `from-tex/zh.md` 第 1–11 行
> **本章圖數：** 0
> **本章 VizMark 數：** 0（散文章節，純文字導讀）
> **狀態：** [x] 已完成

---

## 章節摘要

《The Art of Linear Algebra》是日本敏捷顧問 Kenji Hiranabe（平鍋健兒）為 Gilbert Strang 的《Linear Algebra for Everyone》撰寫的圖解筆記。書首 Hiranabe 引用 Strang 親筆推薦序，Strang 在序中明確指出：「**圖解（pictures）是展示代數的絕佳方式**」，並強調除了「**行 · 列 點積**」之外，「**線性組合**」與「**秩 1 矩陣**」才是「**完成代數與藝術**」的關鍵。這短短一句話奠定了全書的兩大主軸 — 後續 §1–§6 的所有圖解，本質上都是「線性組合 + 秩 1 矩陣」這兩個概念的視覺呈現。本互動式版本（S02–S11 開發）把書中 50 張靜態圖轉成可調參即時看結果的 Python 視覺化，並補上 23 個 VizScript 細緻劇本，把 Strang/Hiranabe 的「直覺優先教學風格」推進到「可手動互動體驗」的下一階段。

---

## Gilbert Strang 推薦序（原文與繁中翻譯）

### 英文原文

> I am happy to see Kenji Hiranabe's pictures of matrix operations in linear algebra! The pictures are an excellent way to show the algebra. We can think of matrix multiplications by row $\cdot$ column dot products, but that is not all — it is "linear combinations" and "rank 1 matrices" that complete the algebra and the art. I am very grateful to see the books in Japanese translation and the ideas in Kenji's pictures.
>
> — Gilbert Strang
> Professor of Mathematics at MIT

### 繁體中文翻譯

> 我很高興能看到 Kenji Hiranabe 線性代數中矩陣運算的圖解！這些圖解是展示代數的絕佳方式。我們當然可以透過「行 (row) $\cdot$ 列 (column) 點積」來理解矩陣乘法，但那絕非全部 — 真正完成這門代數與藝術的，是「**線性組合 (linear combinations)**」和「**秩 1 矩陣 (rank 1 matrices)**」。我很感激能看到本書日文翻譯版，以及 Kenji 圖解中的所有想法。
>
> — Gilbert Strang
> 麻省理工學院（MIT）數學教授

---

## 序言三大主題（導讀）

Strang 序言雖短（不到 100 字），卻明確指出貫穿全書的**三大主題**。對應到本互動式版本的章節：

### 主題 1：圖解優於符號

> **原文關鍵句：** "The pictures are an excellent way to show the algebra."

線性代數的傳統教材以**符號公式**為主、圖解為輔。本書反其道而行 — **圖解是主**、公式是輔。每張圖都是一個獨立的思考工具，公式只是對圖的形式化。

**對應章節：** 全書 §1–§6 共 50 張圖，每張都對應 1–4 個 VizMark + VizScript，把「圖解優於符號」的精神推進到「**可互動的圖解**」。

### 主題 2：超越「行 · 列點積」的視野

> **原文關鍵句：** "We can think of matrix multiplications by row $\cdot$ column dot products, but that is not all."

傳統線代教學的入門點是「矩陣乘法 = 行 · 列點積」（即本書的 (Mv1)、(MM1) 視角）。Strang 強調這「不是全部」 — 必須同時看到**列空間視角**（(Mv2)、(MM2)）、**秩 1 視角**（(MM4)），才算真正理解矩陣乘法。

**對應章節：**
- §1 [Viewing a Matrix - 4 Ways](ch01-viewing-matrix.md)：1 個矩陣的 4 種觀看視角
- §2 [Vector × Vector - 2 Ways](ch02-vec-vec.md)：點積 (v1) vs 外積 (v2)
- §3 [Matrix × Vector - 2 Ways](ch03-mat-vec.md)：(Mv1) 點積版 vs (Mv2) 線性組合版
- §4 [Matrix × Matrix - 4 Ways](ch04-mat-mat.md)：(MM1)–(MM4) 四種乘法視角

### 主題 3：線性組合 + 秩 1 矩陣 = 完整代數的藝術

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

## 本書緣起（簡要歷史背景）

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

## 本互動式版本的範圍與目標（讀者導讀）

### 範圍

- **覆蓋章節：** §1–§6（內容章節）+ 序言（本檔）+ 結論 + 3 個附錄（共 13 個 md 檔，總計 ~8000 行）
- **語言：** 繁體中文為主（術語第一次出現括號附英文）
- **平行素材：** 同步整合英文版（[from-tex/en.md](from-tex/en.md)）與簡中版（[from-tex/zh.md](from-tex/zh.md)）的差異
- **跳過：** 日文版（內容與英文版一致，只是翻譯）

### 目標（三層）

1. **第一層（已完成 S02–S10）：** 把原書 50 張圖各寫一份四欄位描述（視覺結構 / 數學內容 / 直覺解讀 / VizMark）+ 23 個 VizScript 細緻劇本（每個 800 字 + 13 段 A-M 格式）
2. **第二層（S11，即將）：** 整合 + 校對 + 統一風格 + 生成 `BOOK.md` 合併版 + `VIZ-CATALOG.md` 視覺化候選池目錄
3. **第三層（S12+，預估 25–28 session）：** Python 視覺化技術棧決策（傾向 **Marimo + plotly 3D + matplotlib + scikit-learn**）+ 從 23 個 VizScript 挑題目開做 PoC，最終產出「**可互動的 The Art of Linear Algebra**」

### 視覺化分級（Tier 系統）

每個 VizScript 標 1–3 顆星，顯示視覺化的複雜度與優先順序：

- ⭐⭐⭐ **Tier 3**（4 個）：核心骨架旗艦，預估 S12+ 各 3 session 實作 — 含 [ch04 (MM4) Mona Lisa SVD demo](ch04-mat-mat.md#vizscript-02)、[ch06f SVD 完整互動 + 4 應用](ch06f-USV.md#vizscript-01) 兩支主旗艦
- ⭐⭐⭐ **Tier 2**（多支）：主章核心互動，預估 S12+ 各 2 session
- ⭐⭐ **Tier 1**（多支）：輕量互動 / 數值範例 walkthrough，預估 S12+ 各 1.5 session
- ⭐ **Tier 1 輕量**（多支）：純動畫或單一概念示範，預估 S12+ 各 1 session

---

## 如何閱讀本書

### 路線 A：純讀者（不寫程式）

1. 先讀 [§1 Viewing a Matrix](ch01-viewing-matrix.md) 建立術語直覺
2. 順序讀 §2 → §3 → §4 → §5 → §6 主章
3. 每章「**直覺解讀**」段是核心；「**VizScript**」段可略過
4. 讀 [Conclusion](back-conclusion.md) + [Map of Eigenvalues](appendix-map-eigenvalues.md) + [Matrix World](appendix-matrix-world.md) 收尾

### 路線 B：互動體驗者（S12+ 完成後）

1. 從 [Matrix World 互動式索引地圖](appendix-matrix-world.md) 進入（旗艦 dashboard）
2. 點任何元素跳到對應章節 + VizScript
3. 每個 VizScript 都有「拉桿 + 即時視覺反饋」可調參體驗
4. 重點推薦旗艦：[ch06f SVD 完整互動 + Mona Lisa demo](ch06f-USV.md#vizscript-01)

### 路線 C：開發者 / 視覺化工程師

1. 直接讀 [VIZ_SCHEMA.md](VIZ_SCHEMA.md) 了解 VizScript 13 段 A-M 格式
2. 從 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 開始（母模板，全書最詳盡）
3. 跳到 [ch06f VizScript-01](ch06f-USV.md#vizscript-01)（集大成終章）
4. S11 產出的 `VIZ-CATALOG.md` 將集中所有 23 個 VizScript 索引

---

## 章末延伸

- **後續章節連結：** [→ §1 Viewing a Matrix](ch01-viewing-matrix.md)
- **延伸閱讀：**
  - Gilbert Strang (2020), *Linear Algebra for Everyone*, Wellesley Cambridge Press. <http://math.mit.edu/everyone>
  - Gilbert Strang (2016), *Introduction to Linear Algebra*, 5th ed., Wellesley Cambridge Press. <http://math.mit.edu/linearalgebra>
  - 詳細參考文獻見 [Conclusion + References](back-conclusion.md)

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 1–14 / `The-Art-of-Linear-Algebra.pdf` p.1
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 1–11
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **序言作者：** Gilbert Strang（MIT 數學系教授）
- **原 repo：** <https://github.com/junoback/The-Art-of-Linear-Algebra>
- **授權：** Apache 2.0
