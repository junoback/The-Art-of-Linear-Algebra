# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S09（§6.4 EVD + §6.5 SVD 完成，**§6 主章序列收尾 + 全書最長章 + Tier 3 主 VizScript 首例**）
- **日期:** 2026-05-12
- **狀態:** `ch06e-QLQ.md`（695 行，3 VizMark：⭐⭐⭐ Tier 2 譜分解 + 橢球主軸 3D 單 pointer 指 ch05 P4 / ⭐⭐ Tier 1 P_p 三性質 / ⭐ Tier 1 2×2 EVD walkthrough）+ `ch06f-USV.md`（**934 行，全書最長章節**，4 VizMark：⭐⭐⭐ **Tier 3** SVD 完整互動 + 4 應用切換 + 4 子空間 + 2D 幾何 + Mona Lisa demo（**全書唯一雙 pointer 主 ch04 + 副 ch05**）/ ⭐⭐⭐ Tier 2 奇異值降冪 + Eckart-Young / ⭐⭐ Tier 1 4 子空間 SVD 構造 / ⭐ Tier 1 2×2 SVD walkthrough）完成；**S09 PNG 重核重大發現：EVD 與 SVD 都標 `using P4`**（HANDOFF 預估 SVD 雙標 P4+MM4 推翻），§6.x 7 張主圖 `using XX` 最終地圖：CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4；「**雙 pointer 復活判準**」明文化（PNG 標記重複 + 內容旗艦同根雙條件）；Tier 3 主 VizScript 首次出現在 §6（SVD VizScript-01 與 ch04 VizScript-02 並列「核心骨架雙旗艦」）；SOP §2.6 補 S09 6 觀察 + 版本 0.10；下次 S10 從 Foreword + Conclusion + 附錄（MapofEigenvalues / MatrixWorld / TheFourSubspaces）開始，**§1–§6 全書內容章節 100% 完成**

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
- [x] **S02** §1 Viewing a Matrix - 4 Ways：`ch01-viewing-matrix.md`（418 行）— 1 圖描述 + 2 VizMark + 2 VizScript
- [x] **S02** 全書術語慣例 B 派 → A 派切換 + `SCHEMA.md` §3.1 規範更新 + SOP_DRAFT.md §2.4 教訓記錄
- [x] **S03** §2 Vector × Vector - 2 Ways：`ch02-vec-vec.md`（497 行）— 1 圖描述 + 2 VizMark + 2 VizScript；驗證 ch01 範本可複用
- [x] **S03** SOP_DRAFT.md §2.8 對比 / 對偶結構章節寫作模式 + 全書視覺一致性錨點 + 版本 0.4
- [x] **S04** §3 Matrix × Vector - 2 Ways + 4-Subspaces：`ch03-mat-vec.md`（935 行）— 3 圖描述 + 4 VizMark + 4 VizScript
- [x] **S04** SOP_DRAFT.md §2.9 多 VizMark 分級策略 + 版本 0.5
- [x] **S05** §4 Matrix × Matrix - 4 Ways：`ch04-mat-mat.md`（849 行）— 1 圖含 4 子圖描述 + 4 VizMark + 4 VizScript（含 ⭐⭐⭐ Tier 3 VizScript-02 MM4 + Mona Lisa SVD demo，§6 SVD 鋪陳全書最強母模板）
- [x] **S05** SOP_DRAFT.md §2.6 補 N-way 單圖章節觀察 + Tier 2/3 選擇 + 版本 0.6
- [x] **S06** §5 Practical Patterns：`ch05-patterns.md`（830 行）— 4 張獨立圖描述 + 6 Pattern + 4 VizMark + 4 VizScript
- [x] **S06** SOP_DRAFT.md §2.6 補 S06 觀察（HANDOFF Pattern 重核 / Tier 1 + pointer / 對偶 Pattern 總表）+ 版本 0.7
- [x] **S07** §6 五大分解總覽：`ch06a-five.md`（331 行）+ §6.1 A=CR：`ch06b-CR.md`（545 行）— 兩章 session 模式首次驗證
- [x] **S07 PNG 重核重大發現：原書 CR1/CR2 圖明標 `using P1` / `using P2`** — §6.1–§6.5 跨章連結官方鐵證
- [x] **S07** SOP_DRAFT.md §2.6 補 S07 兩章 session + 雙 pointer + 對偶兩張圖 + 版本 0.8
- [x] **S08** §6.2 A=LU：`ch06c-LU.md`（654 行）+ §6.3 A=QR：`ch06d-QR.md`（541 行）— 主章 + 主章兩章 session 模式驗證
- [x] **S08 PNG 重核重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** — LU1 無標、LU2 標 `using MM4`、QR 標 `using P1`
- [x] **S08** SOP_DRAFT.md §2.6 補 S08 5 觀察（using MM4 / 單 pointer 規律 / 應用面廣度規律 / 3D in QR / 主章+主章模式）+ 版本 0.9
- [x] **S09** §6.4 S=QΛQᵀ：`ch06e-QLQ.md`（695 行）— 7 個數學要點段（定義 / 譜定理證明 / P_p 三性質詳解 / (P4) 連結 / 對稱矩陣特殊性 / 與其他分解關係 / 總結表）+ Figure 6.6 EVD 四欄描述（**標 using P4**）+ 3 VizMark：
  - **VizScript-01** ⭐⭐⭐ Tier 2「譜分解互動 + 橢球主軸對齊 3D」**單 pointer 指 [ch05 VizScript-03](docs/book/ch05-patterns.md#vizscript-03)**（PNG 標 P4 → 指 ch05 P4 三明治）
  - **VizScript-02** ⭐⭐ Tier 1「P_p 三性質視覺驗證」（精簡 13 段）
  - **VizScript-03** ⭐ Tier 1「2×2 EVD 數值範例 walkthrough」（輕量逐步動畫）
- [x] **S09** §6.5 A=UΣVᵀ：`ch06f-USV.md`（**934 行，全書最長章**）— 8 個數學要點段（定義 Full vs Reduced / 構造算法兩 EVD 整合 / (P4) 連結 / 4 子空間對齊 / Eckart-Young 定理 / 4 大旗艦應用詳解 / 與其他分解關係 / 總結表）+ Figure 6.7 SVD 四欄描述（**標 using P4**）+ **4 VizMark**：
  - **VizScript-01** ⭐⭐⭐ **Tier 3**「SVD 完整互動 + 4 應用切換（壓縮 / PCA / 降噪 / 推薦）+ 4 子空間視覺整合 ch03 兩塊大餅圖 + 2D 幾何單位圓→橢圓 + Mona Lisa demo」**全書唯一雙 pointer 主 [ch04 VizScript-02](docs/book/ch04-mat-mat.md#vizscript-02) + 副 [ch05 VizScript-03](docs/book/ch05-patterns.md#vizscript-03)**（**全書唯一 §6 Tier 3 主 VizScript**，與 ch04 VizScript-02 並列「核心骨架雙旗艦」）
  - **VizScript-02** ⭐⭐⭐ Tier 2「奇異值降冪 bar chart + 累計能量 + Eckart-Young 視覺」
  - **VizScript-03** ⭐⭐ Tier 1「4 子空間 SVD 構造（重用 ch03 VizScript-02 框架）」
  - **VizScript-04** ⭐ Tier 1「2×2 SVD 數值範例 walkthrough（Strang 經典 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$）」
- [x] **S09 PNG 重核重大發現：EVD 與 SVD 都標 `using P4`**（HANDOFF 預估 SVD 雙標 P4+MM4 推翻），§6.x 7 張主圖 `using XX` 最終地圖確立：CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4
- [x] **S09 「雙 pointer 復活判準」明文化：** PNG 標記重複（P4 在 EVD/SVD 都標）+ 內容旗艦同根（SVD 與 ch04 Mona Lisa demo 同根）**雙條件**成立才升級雙 pointer。EVD 嚴守單 pointer，SVD 升級雙 pointer
- [x] **S09 Tier 3 主 VizScript 首次出現在 §6** — SVD VizScript-01 是全書第二支 Tier 3（與 ch04 VizScript-02 並列），預估 S12+ 各 3 session
- [x] **S09** SOP_DRAFT.md §2.6 補 S09 耗時資料點（3h / 1629 行 / SVD 934 行為全書最長）+ 6 觀察（雙 pointer 判準 / §6.x PNG 標記最終地圖 / Tier 3 §6 首例 / 應用面廣度規律 / 主章序列篇幅比例 1.71 SVD 集大成 / §6 雙 pointer 設計地圖規律）+ 版本 0.10

### 進行中
- 無，S09 已收尾，**§1–§6 全書內容章節 100% 完成**

### 待辦（多 session 路線圖 v2 — 方案 A 整合 VizMark+VizScript）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema（章節 / 視覺化）+ 路線圖補規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| ✅ S02 | §1 Viewing a Matrix - 4 Ways | `ch01-viewing-matrix.md`（418 行） |
| ✅ S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md`（497 行） |
| ✅ S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces） | `ch03-mat-vec.md`（935 行） |
| ✅ S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md`（849 行） |
| ✅ S06 | §5 Practical Patterns | `ch05-patterns.md`（830 行） |
| ✅ S07 | §6 五大分解總覽 + §6.1 A=CR（兩章 session） | `ch06a-five.md`（331 行）+ `ch06b-CR.md`（545 行） |
| ✅ S08 | §6.2 A=LU + §6.3 A=QR（兩章 session 主章 + 主章模式） | `ch06c-LU.md`（654 行）+ `ch06d-QR.md`（541 行） |
| ✅ S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ（兩章 session 主章 + 主章模式收尾） | `ch06e-QLQ.md`（695 行）+ `ch06f-USV.md`（**934 行，全書最長**） |
| **→ S10** | Foreword + Conclusion + 附錄（MapofEigenvalues / MatrixWorld / TheFourSubspaces）+ References | `front-foreword.md`、`back-conclusion.md`、`appendix-map-eigenvalues.md`、`appendix-matrix-world.md`、`appendix-four-subspaces.md` |
| S11 | 整合 + 校對 + 統一 + `BOOK.md` + `VIZ-CATALOG.md` | 合併版書 + 視覺化候選池目錄 |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 PoC | （延後到 S11 後再細規劃，預估 ~20 session）|

### S10 起步建議

1. **S10 是「附錄 + 散文章」混合 session** — 預估 1.5–2h，共 ~600–800 行（5 個短檔 = Foreword 100 行 + Conclusion 80 行 + MapofEigenvalues 200 行 + MatrixWorld 200 行 + TheFourSubspaces 100 行）
2. **起步前必做：對附錄 PNG 重核 7 種 `using XX` 候選（依 S07–S09 教訓）：**
   - **MapofEigenvalues.png**：Strang 特徵值地圖，**預期可能標 `using P3`**（動態系統 = P3 三明治），對應 ch05 (P3) Pattern；可能也是無 using 標（地圖型描述）
   - **MatrixWorld.png**：全書地圖整合 5 大分解，**預期無 `using` 標**（是地圖層級而非 Pattern 套用）
   - **TheFourSubspaces.png**：Strang 兩塊大餅圖，**預期無 `using` 標**（基本概念在 §3 已用過，是基礎而非套用）
   - **8 種 `using XX` 候選：** P1 / P2 / P3 / P4 / MM1 / MM2 / MM3 / MM4 + 無標
3. **§10.1 Foreword (`front-foreword.md`)**（~100 行）：
   - 從 `from-tex/en.md` 開頭抓 Hiranabe 序言 + Strang 互動的歷史（pandoc 已轉換）
   - 用對應 Schema 但不需 VizMark / VizScript（散文性質）
   - 補繁中翻譯與導讀
4. **§10.2 Conclusion (`back-conclusion.md`)**（~80 行）：
   - 從 `from-tex/en.md` 結尾抓 Conclusion 段（line 571–586）+ References
   - **新增「**全書 6 章 + 23 VizScript 總覽**」段** — 鏈結 ch01–ch06f，作為 S11 整合前的橋樑
5. **§10.3 附錄：MapofEigenvalues (`appendix-map-eigenvalues.md`)**（~200 行）：
   - Hiranabe 的「特徵值地圖」是獨立 slide deck（非主書）— 描述 4 大特徵值類別（實數正 / 實數負 / 純虛 / 一般複數）對應的矩陣性質（對稱正定 / 對稱負定 / 反對稱 / 一般）
   - **與 §6.4 EVD 連結：** Map of Eigenvalues 為 EVD 的「視覺地圖總覽」，可重用 ch06e VizScript-01 的橢球視覺
   - 1–2 個 VizMark + VizScript（預期 ⭐⭐ Tier 1）
6. **§10.4 附錄：MatrixWorld (`appendix-matrix-world.md`)**（~200 行）：
   - 全書地圖：Hiranabe 把 5 大分解、4 大子空間、6 個 Pattern、4 個 (MM)、5 大特徵值類別「整合進一張大圖」
   - **與全書整合：** 為「全書視覺索引」，每個元素都 pointer 到對應章節
   - 1 個 VizMark：「Matrix World 互動式索引地圖」⭐⭐⭐ Tier 2（pointer dashboard，類似 ch06a 的「五分解互動 dashboard」放大版）
7. **§10.5 附錄：TheFourSubspaces (`appendix-four-subspaces.md`)**（~100 行）：
   - 把 ch03 4-Subspaces 的視覺再次封裝為獨立附錄（補 SVD 構造、補正交分解定理）
   - **與 §6.5 SVD 連結：** 直接用 SVD 構造 4 子空間，可重用 ch06f VizScript-03
   - 1 個 VizMark：「4 子空間 SVD 構造完整版」⭐⭐ Tier 1 + pointer 到 ch06f VizScript-03
8. **遵 SOP §2.6 附錄章節寫作模式：** 與主章節相比，附錄重「**整合性**」而非「**從零教學**」 — 各段都 pointer 到主章節，只補主章節漏掉的「**鳥瞰**」與「**整合**」內容。VizMark / VizScript 預期較少（總計 ~5–6 個，vs 主章節單章 3–4 個）
9. **「集大成」VizScript 候選：** 「**Matrix World 互動式索引地圖**」可作為 S10 的旗艦 VizScript（⭐⭐⭐ Tier 2 +），讓使用者「**從一張地圖點任何元素跳到對應章節 + VizScript**」，是 S11 BOOK.md 整合前的最佳「導覽工具」。**S12+ 可考慮把這個地圖作為「全書互動式教材的首頁」**

### 工件清單（S10+ 撰寫前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式（A 派術語） |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段 A-M 格式（含 800 字範例） |
| `docs/book/_merged.md` | 章節進度追蹤 + 章節↔圖檔對映表 + VizMark 計數 |
| `docs/book/ch01-viewing-matrix.md` | **S02 成稿，A 派術語的參考範本**（單視角章節） |
| `docs/book/ch02-vec-vec.md` | **S03 成稿，對比 / 對偶結構章節範本** |
| `docs/book/ch03-mat-vec.md` | **S04 成稿，多 VizMark + 多圖章節範本 + 4-Subspaces 標誌圖**（S10 附錄重用素材）|
| `docs/book/ch04-mat-mat.md` | **S05 成稿，N-way 單圖章節範本 + VizScript-02 母模板（S09 SVD 雙 pointer 主 pointer 目標）** |
| `docs/book/ch05-patterns.md` | **S06 成稿，多獨立小圖章節範本 + 「Tier 1 + pointer」策略首例（S09 EVD/SVD 副 pointer 目標）** |
| `docs/book/ch06a-five.md` | **S07 成稿，§6 開門總覽範本**（短章節 + Tier1+pointer dashboard，**S10 MatrixWorld 地圖規模放大版的母模板**） |
| `docs/book/ch06b-CR.md` | **S07 成稿，§6.x 分解主章節範本（雙 pointer + 對偶兩圖 + `using PX` 跨章標記）** |
| `docs/book/ch06c-LU.md` | **S08 成稿，分解主章節範本（無對偶圖差異，雙視角切換 + 單 pointer + `using MM4`）** |
| `docs/book/ch06d-QR.md` | **S08 成稿，分解主章節範本（單圖 + 3D 視覺，Gram-Schmidt + 單 pointer + `using P1`）** |
| `docs/book/ch06e-QLQ.md` | **S09 成稿，分解主章節範本（對稱情境，譜分解 + 橢球 3D + 單 pointer + `using P4`）** |
| `docs/book/ch06f-USV.md` | **S09 成稿，全書最長章 + 唯一 §6 Tier 3 主 VizScript（4 應用 + 4 子空間 + 雙 pointer + `using P4`）— S10 附錄會多次 pointer 到此** |
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready）|
| `docs/dev/sop/SOP_DRAFT.md` | §2.6 + §2.8 + §2.9 + S06–S09 補各種策略 — **S10+ 直接沿用** |

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
| 2026-05-12 | **S02 中途決策變更：術語慣例改採華文主流 A 派（column = 列直立 / row = 行橫躺）** | 與中國大陸、日本、多數 Python 中文文件、本書簡中譯本一致 |
| 2026-05-12 | SOP_DRAFT.md 新增「術語慣例必須在 S01 鎖死」教訓條 | S02 中途改 A 派付出整檔重寫 0.5h 成本 |
| 2026-05-12 | **S03 確立「全書視覺一致性錨點」（SOP §2.8）：配色 hex / cell 尺寸 / 動畫時間統一化** | S04+ 撰寫 VizScript 時直接套用 |
| 2026-05-12 | **S03 確立「對比 / 對偶結構章節寫作模式」** | §3、§4、§6 均適用同一格式，減少每章設計成本 |
| 2026-05-12 | **S04 確立「多 VizMark 章節分級寫作策略」（SOP §2.9）：⭐⭐⭐ 完整 / ⭐⭐ 精簡 / ⭐ 輪廓** | ch03 4 個 VizMark 若全寫 800 字會膨脹 |
| 2026-05-12 | **S04 確立「4-Subspaces 圖是全書視覺化最高 priority 之一（⭐⭐⭐ Tier 3）」** | Strang 兩塊大餅圖是線性代數核心定理（rank-nullity / 投影 / SVD）的視覺載體 |
| 2026-05-12 | **S05 確立「N-way 單圖章節寫作模式」+ ⭐⭐⭐ 劇本可選 Tier 2 / Tier 3** | ch04 VizScript-02 (MM4 + Mona Lisa SVD demo) 寫成 Tier 3 — 是 §6 SVD 的視覺前置 |
| 2026-05-12 | **S05 確立「§4 (MM4) 是 §6 五大分解的視覺基石」** | 5 大分解都可用 (MM4) 展開成「秩 1 之和」 |
| 2026-05-12 | **S06 教訓：HANDOFF 章節描述漏 P4** | 起步前必須對著原書 PNG 重核 Pattern/Figure 數量 |
| 2026-05-12 | **S06 確立「Tier 1 + pointer」省篇幅策略** | ch05 VizScript-03 (P4) 採此策略，§6 5 大分解每章都可重用 |
| 2026-05-12 | **S06 確立「對偶 Pattern 用對偶總表呈現」** | 節省 ~40% 篇幅且閱讀時更易對照 |
| 2026-05-12 | **S07 確立「兩章 session 模式」（總覽短 + 主章長）** | §6 五大分解總覽單獨一個 session 太浪費，與 §6.1 合 session 後省 0.5h |
| 2026-05-12 | **S07 重大發現：原書 PNG `using PX` 標記是跨章連結官方鐵證** | CR1.png 標 `using P1`、CR2.png 標 `using P2`，§5 Pattern 直接連到 §6.1 |
| 2026-05-12 | **S07 確立「雙 pointer VizScript 設計」** | ch06b VizScript-01 首例驗證可行 |
| 2026-05-12 | **S07 確立「對偶兩張圖（列視角 + 行視角）是 §6.1–§6.5 全書一致模式」** | CR1+CR2 對偶展示「列秩 = 行秩」 |
| 2026-05-12 | **S08 重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** | 跨章 pointer 不只連 ch05 (P1-P4)，也連 ch04 (MM1-MM4) |
| 2026-05-12 | **S08 確立「單 pointer 比雙 pointer 更常見」規律** | PNG 標什麼 `using XX`，VizScript 就指對應章；不強行加多 pointer |
| 2026-05-12 | **S08 確立「分解章篇幅由『應用面廣度』決定」** | LU 含解 Ax=b、QR 含最小平方法、CR 含列秩=行秩證明 |
| 2026-05-12 | **S08 確立「3D 投影視覺是 QR 章獨有需求」** | 3D 渲染棧成 §6 必備 |
| 2026-05-12 | **S08 確立「主章 + 主章兩章 session 模式」** | 兩個獨立分解主章放同一 session 可行 |
| 2026-05-12 | **S09 重大發現：EVD 與 SVD PNG 都標 `using P4`，HANDOFF 預估 SVD 雙標 P4+MM4 推翻** | §6.x 7 張主圖 `using XX` 最終地圖：CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4 |
| 2026-05-12 | **S09 確立「雙 pointer 復活判準」明文化** | 雙條件「PNG 標記重複（P4 在 EVD/SVD 都標）+ 內容旗艦同根（SVD 與 ch04 Mona Lisa demo 同根）」雙成立才升級雙 pointer。EVD 嚴守單 pointer，SVD 升級雙 pointer |
| 2026-05-12 | **S09 確立「Tier 3 主 VizScript 首次出現在 §6」** | SVD VizScript-01 是全書第二支 Tier 3 主 VizScript（與 ch04 VizScript-02 並列「核心骨架雙旗艦」），預估 S12+ 各 3 session，完成後可宣稱「全書互動式教材核心骨架 80%」 |
| 2026-05-12 | **S09 確立「§6 主章序列篇幅比例 1.0:1.20:0.99:1.28:1.71，SVD 為集大成終章」** | SVD 章 934 行為平均章節 1.6 倍 — 應用面最廣（4 大旗艦應用詳解）+ 跨章整合最深（與 ch03 4-Subspaces / ch04 MM4 / ch05 P4 全部整合）+ VizScript 規格最高（Tier 3）三方面證明「§1–§6 全書集大成終章」地位 |
| 2026-05-12 | **S09 確立「§6 章節雙 pointer 設計地圖規律」** | 對偶兩張圖（CR1+CR2 → 雙 pointer）+ 集大成章（SVD → 雙 pointer），單張圖且非集大成章採單 pointer（LU/QR/EVD）|

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
| docs/book/SCHEMA.md | 新增 | 章節 md 結構 + 圖片四欄描述格式 |
| docs/book/VIZ_SCHEMA.md | 新增（S01.5） | VizMark 標記 + VizScript 13 段細緻劇本格式 |
| docs/book/_merged.md | 新增 / 重寫（S01.5）| 章節進度追蹤 + 章節↔圖檔對映 + VizMark 計數欄 |
| docs/book/from-tex/{en,zh}.md | 新增 | pandoc 轉換 |
| docs/book/from-pdf/{en,zh}.txt | 新增 | pdftotext 純文字 |
| docs/book/figs-png/*.png | 新增 | 50 張 PNG |

### S02–S08 新增/修改的檔案
- S02：`ch01-viewing-matrix.md`（418 行）
- S03：`ch02-vec-vec.md`（497 行）
- S04：`ch03-mat-vec.md`（935 行）
- S05：`ch04-mat-mat.md`（849 行）
- S06：`ch05-patterns.md`（830 行）
- S07：`ch06a-five.md`（331 行）+ `ch06b-CR.md`（545 行）
- S08：`ch06c-LU.md`（654 行）+ `ch06d-QR.md`（541 行）
- 每 session 同時更新 _merged.md / SOP_DRAFT.md / CURRENT_SESSION.log / SESSION_INDEX.md

### S09 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/ch06e-QLQ.md | 新增 | **§6.4 S=QΛQᵀ：695 行**，7 個數學要點段（含譜定理證明 + P_p 三性質詳解 + 對稱性禮物）+ Figure 6.6 EVD（標 `using P4`）+ 3 VizMark：⭐⭐⭐ Tier 2 譜分解 + 橢球主軸 3D 單 pointer 指 ch05 / ⭐⭐ Tier 1 P_p 三性質 / ⭐ Tier 1 2×2 EVD walkthrough |
| docs/book/ch06f-USV.md | 新增 | **§6.5 A=UΣVᵀ：934 行（全書最長章節）**，8 個數學要點段（含 Full vs Reduced + 構造算法兩 EVD 整合 + 4 子空間對齊 + Eckart-Young 定理 + 4 大旗艦應用詳解）+ Figure 6.7 SVD（標 `using P4`）+ **4 VizMark**：⭐⭐⭐ **Tier 3** SVD 完整互動 + 4 應用切換（壓縮/PCA/降噪/推薦）+ 4 子空間 + 2D 幾何 + Mona Lisa demo（**全書唯一雙 pointer 主 ch04 + 副 ch05**）/ ⭐⭐⭐ Tier 2 奇異值降冪 + Eckart-Young / ⭐⭐ Tier 1 4 子空間 SVD 構造 / ⭐ Tier 1 2×2 SVD walkthrough |
| docs/book/_merged.md | 修改 | S09 標記 [x]，VizMark 計數「EVD 1/1/1 + SVD **1Tier3+1Tier2/1/1**」（合計 ⭐⭐⭐ × 3 / ⭐⭐ × 2 / ⭐ × 2，**全書 VizMark 密度最高的 session**）+ §6.4 §6.5 章節↔圖檔對映補 PNG `using P4` 標記說明 |
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.6 補 S09 耗時資料點（3h / 1629 行 / SVD 章 934 行為全書最長）+ 6 觀察 + 版本記錄追加 0.10 |
| docs/dev/CURRENT_SESSION.log | 修改 | S09 啟動 + 即時記錄（含 PNG 重核發現 + 雙 pointer 復活 + Tier 3 § 6 首例）+ 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S09 一行 |

---

## 技術筆記

### Repo 原始內容概覽
- **LaTeX 主檔**：`The-Art-of-Linear-Algebra.tex`（英文）、`-j.tex`（日文）、`-zh-CN.tex`（簡中）
- **編好的 PDF**：三種語言版本均已存在
- **圖檔來源**：`Illustrations.pptx`（PowerPoint），透過 makefile 流程印成 PS → EPS → 嵌入 LaTeX

### 互動式版本技術選項（S12+ 決策，目前傾向）
| 方案 | 優點 | 缺點 |
|------|------|------|
| **Marimo + matplotlib + marimo.ui**（S02–S09 VizScript 首選） | 反應式 notebook、純 Python、可匯出 HTML | 較新生態系較小 |
| Streamlit + Plotly | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

**S08–S09 觀察（3D 渲染棧成 §6 必備 + Mona Lisa 影像處理 + 多應用切換）：**
- §6.3 QR：3D 投影視覺（matplotlib 3D / plotly 3D）；
- §6.4 EVD：3D 橢球主軸對齊（plotly 3D 為主，因參數球面渲染流暢度高）；
- §6.5 SVD：**全書最複雜的視覺化棧** — 3D 橢球（plotly）+ Mona Lisa 影像處理（Pillow + numpy）+ Iris PCA 散點圖（matplotlib）+ 矩陣補全評分視覺（plotly heatmap）+ 4 子空間（重用 ch03）。**結論：S12+ 必確認技術棧支援所有需求**：**Marimo + plotly + matplotlib + scikit-learn + Pillow** 為最低限度組合。**最可能選擇：Marimo + plotly 3D + matplotlib + scikit-learn**（反應式 + 3D 流暢 + 純 Python + 多應用支援）。

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
| diagonal matrix | 對角矩陣 | 藍點對角排列、非對角位置留白 |
| row reduced echelon form (RREF) | 行階梯形（列簡化形）矩陣 | — |
| identity matrix | 單位矩陣 | — |
| spectral theorem | 譜定理（S09 新增）| — |
| singular value decomposition (SVD) | 奇異值分解（SVD）| — |
| eigenvalue decomposition (EVD) | 特徵值分解（EVD）/ 譜分解 | — |
| Eckart-Young theorem | Eckart-Young 定理 / 最佳低秩近似定理（S09 新增）| — |
| Moore-Penrose pseudoinverse | Moore-Penrose 偽反 / 偽反矩陣（S09 新增）| — |
| Frobenius norm | Frobenius 範數 / F 範數（S09 新增）| — |
| principal component analysis (PCA) | 主成分分析（S09 新增）| — |

**矩陣尺寸：** $A \in \mathbb{R}^{m \times n}$ 表示 **$m$ 行 $n$ 列**（$m$ rows, $n$ columns）。$m$ = 行數、$n$ = 列數。
**矩陣乘法形狀：** $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$AB = C \in \mathbb{R}^{m \times n}$。**內維 $k$ 必須對齊**。

### 全書視覺一致性錨點（S03 確立，S08+ 補 3D + 金色主元 + 黃色中間結果，S09 補 SVD 雙色對比）

- **配色 hex：** 綠（列 / 直立 / 正交向量 / **U / 列空間**）`#2ca02c`、粉紅 / 紅（行 / 橫躺 / 投影向量 / **V^T / 行空間 / SVD 雙側獨立指紋**）`#d62728`、藍點（個別數字 / 對角元素 / **σ_p 與 λ_p**）`#1f77b4`、灰填充 `#cccccc`（原始向量 / 已剝離元素 / **單位球 / 對稱輸入**）、子空間半透明 alpha 0.3、紫色（特徵基底 / 動態系統 / CR 第 3 列 / **退化警示 / 4 子空間零空間方向 / 負特徵值反射**）`#9467bd`、橙色（CR 第 2 列 / 接近依賴警示 / **秩 k 截斷曲線**）`#ff7f0e`、**金色 `#FFD700`**：主元 / 當前正在處理的列 / **變形後的橢球 / EVD 橢球**、**黃色**：中間結果 $\mathbf{w}_p$（減投影後未單位化）
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **3D 視窗尺寸：** 預設 600×480 px、視角 elev=25° azim=-60°（S08 QR 章 / S09 EVD 章 / S09 SVD 章必備）
- **動畫時間：** 視角切換 600–800ms、平行性高亮淡入 200ms、子空間維度變化 600ms、飛行軌跡 700ms、秩 1 累加 400ms / 項、緩動 ease-in-out、peeling 動畫 600ms / 楔形（S08）、Gram-Schmidt 減投影 500ms / 投影（S08）、**譜分解逐項累加 1500ms / 項（S09）**、**橢球變形 800ms（S09）**、**SVD 應用切換 500ms（S09）**
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$（3D 限 $\{2, 3\}$、SVD demo Mona Lisa 400×250 / Iris 150×4）；對角元素 $d_p \in [-3, 3]$ 步進 0.5、**特徵值 $\lambda_p \in [-9, 9]$（S09）**、**奇異值 $\sigma_p \geq 0$（S09，強制非負）**
- **N-way 切換動畫：** 多視角 tab 切換時 800ms 動畫含「色塊重排 + 重染色 + 公式同步」三層
- **對角矩陣表現：** 藍圓點直徑 12–14px 沿對角線排列、**非對角位置完全留白不畫 0**、$d_p$ 改變時藍點半徑 ∝ $|d_p|$
- **動態系統軌跡：** 軌跡藍漸變（淡 → 深 = 時間順序）、當前點紫實心 8px、特徵向量綠箭頭
- **CR 三色標記（S07）：** $A$ 的列 1 = 藍 / 列 2 = 橙 / 列 3 = 紫
- **LU 楔形視覺（S08）：** 楔形 $p$ 大小 ∝ 殘餘子矩陣 $A_p$ 範圍
- **QR 上三角藍點（S08）：** $R$ 用藍點 + 上三角形狀排列展示
- **EVD 鏡像對稱布局（S09 新增）：** $Q$（綠列直立）和 $Q^{\mathrm{T}}$（綠行橫躺）在 $\Lambda$ 兩側鏡像對稱 — 對稱矩陣的視覺指紋
- **SVD 雙色獨立布局（S09 新增）：** $U$（綠列直立）和 $V^{\mathrm{T}}$（**粉紅行橫躺**）使用不同顏色對比 — 雙側獨立的視覺指紋（與 EVD 同色形成對比）
- **譜分解投影矩陣 $P_p$（S09）：** $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 顯示為「綠列 + 淡綠橫躺行」自外積（左右標號相同）
- **SVD 秩 1 拆解（S09）：** $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 顯示為「綠列 + 淡粉紅橫躺行」一般外積（左右標號相同但顏色不同）
- **跨章跳轉按鈕（S07 / S08 / S09 補）：** 白底深綠邊框 + 「→」字樣，hover 填色 `#2ca02c`；按鈕分四類「→ (MM4) 累加 / Mona Lisa」（指 ch04 VizScript-02）/「→ (P1)(P2) 對角」（指 ch05 VizScript-01）/「→ (P4) 三明治」（指 ch05 VizScript-03，S09 新增為 EVD/SVD 主 pointer 之一）/「→ 4 子空間」（指 ch03 VizScript-02，S09 新增 SVD 整合用）；單 pointer / 雙 pointer 視「PNG `using XX` 標記 + 內容旗艦同根」雙判準決定（S09 確立）

### 章節撰寫速度資料點（S09 更新）

- **S02 §1（含 A 派切換重寫 0.5h）：** 1.5h / 418 行 / 2 VizMark
- **S03 §2（ch01 範本可複用）：** 1h / 497 行 / 2 VizMark
- **S04 §3（4 VizMark 分級策略）：** 1.5h / 935 行 / 4 VizMark
- **S05 §4（1 圖含 4 子圖 + 4 VizMark）：** 1h / 849 行 / 4 VizMark
- **S06 §5（4 圖各獨立 + 6 Pattern + 4 VizMark）：** 1h / 830 行 / 4 VizMark
- **S07 §6 總覽 + §6.1（兩章 session）：** 2h / 876 行（331 + 545）/ 4 VizMark — **兩章 session 模式首次驗證**
- **S08 §6.2 LU + §6.3 QR（兩章主章模式）：** 2.5h / 1195 行（654 + 541）/ 6 VizMark — **主章 + 主章模式驗證 + 3D 渲染棧導入**
- **S09 §6.4 EVD + §6.5 SVD（兩章主章模式收尾）：** **3h / 1629 行（695 + 934）/ 7 VizMark（含 1 Tier 3 + 1 Tier 2 + 5 Tier 1）— SVD 章 934 行為全書最長 + Tier 3 主 VizScript 首次出現在 §6 + 雙 pointer 復活**
- **S10 預估：** Foreword + Conclusion + 3 附錄 ~1.5–2h / 600–800 行 / 5–6 VizMark（附錄重「整合性」而非「從零教學」，每段都 pointer 到主章）

**§1–§6 累計（S09 收尾）：** 共 8 章節 + 9 個主 md 檔（ch01–ch06f）= **總計 6824 行**（不含散文章節 + 附錄）+ **23 VizScript**（4 個 Tier 3：ch04 VizScript-02 + ch06f VizScript-01 兩支主旗艦 + ch04 VizScript-01（Tier 2）+ ch06f VizScript-02（Tier 2）；多支 Tier 2 + Tier 1；S12+ 實作優先序明確）。**§1–§6 全書內容章節 100% 完成**，下階段轉入「附錄 + 校對 + 整合」。

### §4 (MM4) 與 §6 五大分解的鋪陳對應（S09 完整定版）

| §6 分解 | (MM4) 形式 | VizScript 結構複用 | PNG `using XX` 標記（S07–S09 確認） | Pointer 設計 |
|---|---|---|---|---|
| $A = CR$ | $A = \sum_p \mathbf{c}_p \mathbf{r}^*_p$（$r$ 項） | ch04 VizScript-02 + ch05 VizScript-01 | **CR1 標 P1、CR2 標 P2** | **雙 pointer**（對偶兩張圖）|
| $A = LU$ | $A = \sum_p \mathbf{l}_p \mathbf{u}^*_p$（$n$ 項） | ch04 VizScript-02 | **LU1 無標、LU2 標 MM4** | 單 pointer 指 ch04 |
| $A = QR$ | $A = \sum_p \mathbf{q}_p \mathbf{r}^*_p$（$n$ 項） | ch05 VizScript-01 | **QR 標 P1** | 單 pointer 指 ch05 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$（自外積）| ch05 VizScript-03 | **EVD 標 P4** | 單 pointer 指 ch05 |
| $A = U\Sigma V^{\mathrm{T}}$ | $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$（一般外積）| ch04 VizScript-02 + ch05 VizScript-03 | **SVD 標 P4** | **雙 pointer**（集大成 + 內容旗艦同根）|

**S09 結論（§6 主章序列收尾）：** ch04 VizScript-02（MM4 + Mona Lisa SVD demo）+ ch06f VizScript-01（SVD 完整互動）= **「全書互動式教材的核心骨架雙旗艦」**。**S12+ 實作優先順序明確化：**
1. **首批實作（核心骨架）：** ch04 VizScript-02 (3 session) + ch06f VizScript-01 (3 session) = **6 session 完成核心骨架 80%**；
2. **次批實作（§6 主章 + 4 子空間整合）：** ch06b/c/d/e VizScript-01 各 2 session = 8 session；ch03 VizScript-02 (4 子空間 3D) 3 session；ch05 VizScript-01/02 各 1.5 session = 共 14 session；
3. **末批實作（散文章節 + 輕量 VizMark + 附錄）：** 共 ~5–6 session；
4. **Total S12+ 預估：** **25–28 session 完成完整互動式教材**（不含技術棧 PoC 初期 ~3 session）。

**§6 章節雙 pointer 設計地圖規律（S09 確立）：**
- **雙 pointer 採用：** 對偶兩張圖（CR1+CR2）+ 集大成終章（SVD）；
- **單 pointer 採用：** 單張圖且非集大成章（LU / QR / EVD）；
- **判準：** PNG `using XX` 標記重複（同一 Pattern 在多章 PNG 出現）+ 內容旗艦同根（核心 demo 已在另一章實作）**雙條件**成立才升級雙 pointer。

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
4. docs/book/SCHEMA.md + docs/book/VIZ_SCHEMA.md — 雙 Schema 規範（A 派術語）
5. docs/book/ch01–ch05 + ch06a–ch06f — 11 套範本：單視角 / 對比結構 / 多圖多 VizMark / N-way 單圖 / 多獨立小圖 / Tier1+pointer 總覽 / §6.x 主章節對偶兩圖 / 分解主章節無對偶差異 / 分解主章節單圖 3D / 對稱譜分解 + 橢球 3D / SVD 全書最長 + Tier 3 + 雙 pointer + 4 應用
6. docs/dev/sop/SOP_DRAFT.md §2.6 補「§6.x PNG 標記最終地圖 + 雙 pointer 復活判準 + Tier 3 §6 首例 + §6 雙 pointer 設計地圖規律」 + §2.8 全書視覺錨點 + §2.9 多 VizMark 分級策略
然後繼續「待辦」中的第一項任務（S10 Foreword + Conclusion + 附錄（MapofEigenvalues / MatrixWorld / TheFourSubspaces），起步前對附錄 PNG 重核 8 種 using XX 標記候選；§1–§6 全書內容章節 100% 完成，下階段轉入「附錄 + 校對 + 整合」）。
```
