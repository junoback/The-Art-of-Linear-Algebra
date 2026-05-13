# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** **S17 完成（ch04 V-02 MM4 母模板架構階段 — 首批 Tier 3 旗艦開工骨架完成 / commit `cc957f1`）**
- **日期:** 2026-05-14
- **狀態:** **S17 完成：** 從 S16 Marimo 技術棧 PoC 三階段全通過跨入「首批 Tier 3 旗艦實作」階段。Back 選 HANDOFF S16 推薦路線 A 開始 [ch04-mat-mat.md VizScript-02](../book/ch04-mat-mat.md#vizscript-02) MM4+Mona Lisa SVD 母模板（完成後 §6 五分解 pointer 全解鎖）；S17 scope 鎖「最小可動骨架」（小矩陣 3×2·2×2 模式 + r slider 0..2 + 秩 1 圖層 strip + 主舞台 2×3 共 6 heatmap + WASM 部署），不含圖像 / 飛入動畫 / 4 重排序 / 誤差曲線 / Walkthrough（推 S18-S19）；產出 [viz/ch04_matrix_matrix.py](../../viz/ch04_matrix_matrix.py) 440 行 / 8 cell（A 6 entry sliders + B 4 entry sliders + r slider + 即時 LaTeX 計算 cell + 主舞台 6 heatmap subplot + 秩 1 圖層 strip + 三式對拍 healthcheck `A@B == sum of rank-1 layers == accumulate(A,B,k=2)` ✓）+ [viz/_common/rank1_layer.py](../../viz/_common/rank1_layer.py) 工具模組（rank1_outer / layers_of / accumulate / layer_energy，本機 reference / S18+ 非 WASM script 用；WASM export 不嵌入子模組所以 notebook 內聯 helper） + viz/_common/__init__.py；**2 round WASM debug：**(R1) Back 報「sliders + 結尾說明顯示，中間 3 cell（即時計算 / 主舞台 / strip）不見」→ 真因：**marimo 把 `_` 開頭 cell variable 視為 cell-private 不跨 cell export**，我寫 helper cell `return _accumulate, _layer_energy, _layers_of`，下游 cell 引用 NameError 整個 cell 沉默不渲染（不是 STDERR 是「未渲染」）→ 修法 helper 與計算合併同一 cell，命名無 `_` 前綴 / (R2) console 兩個 STDERR exception：① 主舞台 cell `TypeError: bad operand type for abs(): 'list'`（dummy `[[0]]` 傳進 `abs(M).max()`，list 沒 `.max()`）→ helper 內 `np.asarray(M, dtype=float)` + `np.abs()`；② strip cell `IndexError: tuple index out of range`（plotly `subplot_titles=[""] * k` 空字串被跳過不生成 annotation slot，後置 `annotations[p].text = ...` 越界）→ `make_subplots` 直接傳完整 title 不後置改 → R2 後 console clean ✓；**S17 3 個新 WASM 陷阱補進 SOP §2.15**（合計 6 大陷阱）：(4) marimo `_` 前綴 cell-private 不跨 cell / (5) plotly `subplot_titles` 空字串不生成 annotation slot / (6) plotly heatmap z 需 `np.asarray(M, dtype=float)` 保護。下次 S18 從 S17 骨架接「圖像模式 + Mona Lisa SVD」（VizScript-02 模式 2：64×64 灰階圖像 4 張預計算 SVD + cache + 三圖並列原圖/重建/誤差 + radio 切換 + 相對誤差數字）；S19 補完 Tier 3（飛入動畫 + 4 重排序對比 + 誤差曲線 + Walkthrough 6 步 + 快捷鍵）。**S16 完成：** 從 S15 全書 md 化結構就緒（22 Q&A 100% + 16 md callout 覆蓋）跨入「Python 視覺化實作階段」。Back 不立刻挑旗艦，先做「Marimo 技術棧 PoC」+ 載體討論（先例 6 個 Immersive Math ⭐⭐⭐⭐⭐ / Seeing Theory / Distill / 3B1B / Book of Shaders / D2L.ai；技術棧 6 個比較 → 維持 HANDOFF S11 已選 **Marimo + WASM** 路線）；三階段全通過：(1) uv 安裝（brew install uv 0.11.14）+ uv init viz --python 3.12 + uv add marimo plotly matplotlib numpy scikit-learn pillow → hello.py 4 cell reactive slider PoC（Stage 1 ✅）/ (2) ch01_mv1_poc.py 7 cell：6 slider × plotly 2D 4 箭頭 × (Mv2) 平行四邊形，同時展示 (Mv1) 點積 + (Mv2) 線性組合雙觀點，數值對拍 A@x == row_dot_x == x[0]·col1+x[1]·col2（Stage 2 ✅，3 round debug 才通）/ (3) marimo export html-wasm dist/ch01_mv1_poc 27 MB static dir GitHub Pages 可直接部署（Stage 3 ✅）；**3 個 WASM 教訓收進 SOP §2.15**（PEP 723 metadata 是 WASM dep 唯一聲明處 / plotly 必須 mo.ui.plotly(fig) 顯式包裝 / 首次載入 30-60s UX 警告）+ S17+ 旗艦開工 5 條 checklist；產出 viz/ 7 檔追蹤（dist/+.venv/+__pycache__/ gitignore）+ viz/README.md 含 Immersive Math 等先例 + Marimo vs Jupyter/Streamlit/Observable 對照表。下次 S17 從 VIZ-CATALOG 首批 Tier 3 旗艦（ch04 V-02 MM4+Mona Lisa 母模板 或 ch06f V-01 SVD Master）開始，技術棧驗證零阻抗起跑。**S15 完成：** 沿用 S12-S13 確立的 3-layer 框架 + 方案 D 雙層落點 + 批量寫作流程，產出 §6 共 6 條 Q&A：**Q14 為什麼要把矩陣「分解」？**（156 行 / Gauss 1809 → Eckart-Young 1936 200 年史 + 6 大工程動機 + 「為什麼正好五個」遞進對稱性 5 級表）+ **Q15 A=CR 列秩=行秩自然冒出**（119 行 / Sylvester 1851 rank + Frobenius 1879 + Strang 2020 首次代數封裝「最樸素分解」+ 3×3 rank 2 雙重讀法）+ **Q16 A=LU 高斯消去本質**（165 行 / 《九章算術》方程章 2000 年東方原型 + Newton 1707 → Gauss 1809 → Turing 1948 LU 命名 + 3×3 算驗 + 5 跨領域因果結構表）+ **Q17 A=QR Gram-Schmidt 動機**（138 行 / Gauss 1801 Ceres → Legendre/Gram/Schmidt/Householder 200 年最小平方→Hilbert 演化 + 3×2 完算 + 條件數不被平方化）+ **Q18 譜定理對稱特徵向量自動正交**（144 行 / Cauchy 1829 主軸定理 → 量子力學 1920s Hermitian + 雙證明 + 5 物理對稱↔數學物件對應）+ **Q19 SVD 為什麼任意矩陣存在**（174 行 / Beltrami 1873 首次發現 → Eckart-Young 1936 + 雙證明路徑 + 3×2 SVD 巧妙串接 Q17+Q18 同 $A$ + Strang「the most important theorem」名言）+ 6 主章 callout 客製化（[ch06a Q14+Q11+Q13](../book/ch06a-five.md) / [ch06b Q15+Q14](../book/ch06b-CR.md) / [ch06c Q16+Q14](../book/ch06c-LU.md) / [ch06d Q17](../book/ch06d-QR.md) / [ch06e Q18+Q11+Q13](../book/ch06e-QLQ.md) / [ch06f Q19+Q14+Q08+Q13](../book/ch06f-USV.md) 共 15 links）。總產出 [appendix-D-why.md](../book/appendix-D-why.md) **2740 行（+1083 行 / 65% 增量）/ 19 Q&A（19/22 = 86%）** + 6 主章 callout / 15 Q&A links（累計 **12 callout / 28 Q&A links — 全主章 100% 覆蓋** ✓）。**S15 全部完成 ✓：** Q20 特徵值地圖（225 行 / 200 年史 + 8 類代數機制 + Normal matrix 統一源頭）+ Q21 Matrix World 同心橢圓（246 行 / 250 年史 + 4 替代方案致命缺陷比較 + 結構主義立場）+ **Q22 解 Ax=b 為線代核心（311 行 = 全書最長 Q&A / 4000 年史 + 6 步從零推導 + 5 種解情境 + 全書 22 條會師結構 + Strang 「Linear Algebra = the study of Ax=b in all its depth」最強昇華）** + 3 附錄 callout（map Q20+Q18+Q11 / matrix-world Q21+Q14+Q19 / four-subspaces Q22+Q08+Q19 共 9 links）→ **全書 15 callout / 37 Q&A links / 16 個內容 md 100% 覆蓋達成 ✓**；整合收尾:(1) 跨檔 anchor 校驗 37 條跨檔引用 + 22 錨點 + **0 broken link** ✓ + (2) BOOK.md 重生 8650 → **12305 行（+42%）** + (3) SCHEMA.md 補 §3.6「背後觀念 callout 規範」 + (4) VIZ-CATALOG.md 新增「Appendix D 背後觀念層 22 Q&A 索引」獨立段 + (5) 全套收工（SESSION_INDEX/SOP/RETROSPECTIVE/HANDOFF/CURRENT_SESSION.log）。**S12-S15 4-session 路線完成：appendix-D-why.md 3522 行 / 22 Q&A = 100% ✓ + 全書 16 個內容 md 100% callout 覆蓋 ✓ + 平均效率 30 min/Q&A**。下次 S16+ 進入 **S12+ Python 視覺化實作階段**（從 [VIZ-CATALOG 首批 Tier 3 旗艦](../book/VIZ-CATALOG.md) ch04 V-02 或 ch06f V-01 開始 + 技術棧 PoC Marimo + plotly 3D + matplotlib + scikit-learn + Pillow）。

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
- [x] **S06** SOP_DRAFT.md §2.6 補 S06 觀察 + 版本 0.7
- [x] **S07** §6 五大分解總覽：`ch06a-five.md`（331 行）+ §6.1 A=CR：`ch06b-CR.md`（545 行）— 兩章 session 模式首次驗證
- [x] **S07 PNG 重核重大發現：原書 CR1/CR2 圖明標 `using P1` / `using P2`** — §6.1–§6.5 跨章連結官方鐵證
- [x] **S07** SOP_DRAFT.md §2.6 補 S07 + 版本 0.8
- [x] **S08** §6.2 A=LU：`ch06c-LU.md`（654 行）+ §6.3 A=QR：`ch06d-QR.md`（541 行）— 主章 + 主章兩章 session 模式驗證
- [x] **S08 PNG 重核重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** — LU1 無標、LU2 標 `using MM4`、QR 標 `using P1`
- [x] **S08** SOP_DRAFT.md §2.6 補 S08 5 觀察 + 版本 0.9
- [x] **S09** §6.4 S=QΛQᵀ：`ch06e-QLQ.md`（695 行）+ §6.5 A=UΣVᵀ：`ch06f-USV.md`（**934 行，全書最長章**）— §6 主章序列收尾 + 全書 §6 唯一 Tier 3 主 VizScript
- [x] **S09 PNG 重核重大發現：EVD 與 SVD 都標 `using P4`** — §6.x 7 張主圖 `using XX` 最終地圖：CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4
- [x] **S09 「雙 pointer 復活判準」明文化** — PNG 標記重複 + 內容旗艦同根雙條件
- [x] **S09 Tier 3 主 VizScript 首次出現在 §6** — SVD VizScript-01 與 ch04 VizScript-02 並列「核心骨架雙旗艦」
- [x] **S09** SOP_DRAFT.md §2.6 補 S09 6 觀察 + 版本 0.10
- [x] **S10 §1–§6 全書內容 100% 完成**：撰寫 Foreword + Conclusion + 3 附錄（5 個 md 檔 / 1290 行 / 3 VizMark / 3 VizScript）
  - **front-foreword.md**（158 行，0 VizMark）— Strang 推薦序英中對照 + 三大主題導讀（圖解優於符號 / 超越行列點積 / 線性組合+秩 1 矩陣完成代數的藝術）+ 1920-2026 緣起 + 路線 A/B/C
  - **back-conclusion.md**（198 行，0 VizMark）— Hiranabe 結論英中對照 + **全書 33 個 VizScript 總覽表（S11 整合橋樑）+ Tier 分佈統計 + S12+ 實作優先順序三批排程 + 全書 S00–S10 里程碑回顧 + 5 個參考文獻 + 致謝**
  - **appendix-map-eigenvalues.md**（272 行，⭐⭐ Tier 1 + pointer 指 ch06e EVD）— 12 類矩陣 × 特徵值幾何位置完整表 + 與 §6.4 EVD 三層遞進關係 + 與 (P4) 三明治連結 + 12 格 dashboard 互動劇本
  - **appendix-matrix-world.md**（**328 行，⭐⭐⭐ Tier 2 旗艦 — S12+ 全書互動式教材首頁**）— 11 層同心橢圓繼承樹（從 Matrix → Square → Diagonalizable → Normal → Symmetric → ... → {I, O}）+ 偽反矩陣全矩陣統一公式 + 兩條軸線設計（縱深 ⊥ 橫向）+ 13 段 A-M 完整 dashboard 劇本（含 3 模式切換 + 章節過濾器 + 範例矩陣辨認）
  - **appendix-four-subspaces.md**（334 行，⭐⭐ Tier 1 + pointer 指 ch03 V-02 + ch06f V-03）— Strang 正交分解定理 + SVD 構造 4 子空間標準正交基底 + **新增「解 $A\mathbf{x}=\mathbf{b}$ 完整解空間結構視覺」** 段：特解 + 零空間平移仿射子空間 + 最小範數最優解 $\mathbf{x}^* = A^{+}\mathbf{b}$（與 [appendix-matrix-world.md](../book/appendix-matrix-world.md) 底部偽反公式對應）
- [x] **S10 PNG 重核重大發現：3 張附錄 PNG 皆無 `using XX` 標記** — HANDOFF 預估「MapofEigenvalues 可能標 P3」推翻；附錄 PNG 是「**地圖層級 / 基本概念圖**」非「Pattern 套用層級」，標記譜系與主章 §6.x 不同
- [x] **S10 HANDOFF 累積錯誤校正：全書 VizScript 數從 23 校正為 36**（主章 33 + 附錄 3）— 前 session 多次累積寫 23 是漏算（ch03/ch04/ch05 各 4 VizScript = 12 個，多算少數 ~10）
- [x] **S10** SOP_DRAFT.md §2.6 補 S10 7 觀察 + 版本 0.11
- [x] **S11 任務 (3) 跨檔 anchor 校驗：** grep 全書 39 處 `#vizscript-NN` 連結邏輯全對 + 發現 9 處 broken `#N` 短 anchor 全部在 appendix-matrix-world.md (3) + appendix-four-subspaces.md (6)，方案 B 修復（重指 ch06f-USV.md#vizscript-01 或 #vizscript-03，符合附錄「pointer 哲學」）
- [x] **S11 任務 (5) 資料一致性校驗：** VizScript 36 ✓ / `using XX` 標記地圖（CR1=P1, CR2=P2, LU1=無, LU2=MM4, QR=P1, EVD=P4, SVD=P4, 附錄 3 張無）與 HANDOFF 完全一致 / Tier 統計表 6 處校正（總數 33→36、Matrix World V-01 補入 Tier 2 旗艦獨立分類、ch06a V-01 從 Tier 2 改 Tier 1+pointer、附錄 3 個列入、Tier 2 從~10 改 14 主章+1 旗艦、Tier 1 拆 Tier 1+pointer 3 個與 Tier 1 精簡 15 個）+ S12+ 三批排程連動修正（次批新增 Matrix World 旗艦 + 修「ch06b/c/d/e 5 個」→ 4 個）
- [x] **S11 任務 (1) BOOK.md 完整合併：** [BOOK.md](../book/BOOK.md) 8650 行單檔 / 16 個 md 依序串接（front-foreword → ch01–ch06f → back-conclusion → 3 附錄）/ fence-code-aware awk 降一級避開 Python code block 內 `#` 註解 / 含 root heading + 全書目錄 + Tier 統計 + `using XX` 標記地圖 + §6 篇幅比例 + S11 新增「全書視覺錨點」段（3D 視角預設 elevation=25° azimuth=-60° 等）
- [x] **S11 任務 (2) [VIZ-CATALOG.md](../book/VIZ-CATALOG.md) 抽取：** 241 行純 metadata 索引（不複製內容）/ 36 條目（首批 2 + 次批 9 + 末批 A 7 + B 3 + C 15）+ 全章節順序總覽 + 跨章 pointer ASCII 連動圖 + 進度追蹤段（⏳/🔨/✅/⚠️/🔄 五狀態）/ 每行 7 欄位 metadata（連結 + Tier + 批次 + 估時 + 互動類型 + 數學基底 + 跨章 pointer + 狀態）
- [x] **S11 任務 (4) 風格統一檢查：** SCHEMA.md 新增 §3.5「全書視覺錨點」（4 子節：配色 hex+RGB+輔助色階 / cell 寫法 / 動畫時間錨點 / 3D 視角預設）+ 版本 0.2；VIZ_SCHEMA.md §2.2 寫作要點補 cross-reference + 新增 §2.3 對照表 + 版本 0.2；sed 修空格不一致 13 處 X ms → Xms（macOS sed `\b` 不支援，改用無 boundary）+ 10 處 px 空格統一；BOOK.md 重新生成同步全部 S11 修正
- [x] **S11 額外處理 — Strang 8 本版權 PDF 防護：** Back 提供 Linear Algebra for Everyone / Intro to LA / LA and Learning from Data / Diff Eq + LA / CSE / Calculus Vol 1-3 至 docs/book/ 私人參考用；.gitignore 雙保險（`docs/book/*.pdf` pattern + 5 白名單反白）；memory feedback_private_pdfs.md 兩層級分開（PDF 檔本身絕對不 push / md 檔內可大段引用原文以提升完整性，Back 明確授權）+ back-conclusion.md root heading「33→36」修正
- [x] **S12 啟動「背後觀念層」開發階段** — Back 提出全書缺「為什麼這條規則長這樣」維度（現有 13 主章只「怎麼算」缺「為什麼這樣算」），確立 3-layer 框架（① 歷史 + ② 推導 + ③ 昇華）+ 方案 D 雙層落點（主章 callout + 附錄 D 詳盡 Q&A）+ 4-session 路線（S12-S15）+ 22 條 Q&A 全書清單
- [x] **S12 Q09 PoC**：[appendix-D-why.md](../book/appendix-D-why.md) 骨架建立（root + 簡介 + 3-layer 框架 + 22 條目錄表 + 術語提醒）+ Q09 完整 PoC（矩陣乘法為什麼「行乘列」？2500 字含九章算術方程章原文 + Sylvester 1850 / Cayley 1858 / Cayley 原論文引言 + 兩組線性變換代入展開逐步推導 + 觀察規律 3 欄表 + 一般化 boxed 定義 + 2×2 小例題雙路驗證 = $\begin{bmatrix}19&22\\43&50\end{bmatrix}$ + 5 條矩陣現象 ↔ 函數合成本質對照表 + Strang LAFE §1.4「點積規則不是核心、秩 1 分解才是」引言 + 12 條延伸閱讀）；Back review 確認風格 OK 直接批量寫
- [x] **S12 批量寫 Q01-Q08（Foreword + §1 + §2 + §3 共 8 條 / 865 行）**：
  - **Q01 為什麼線性代數要從圖解開始學？**（~56 行）— Strang 1976→2003→2020 五十年漸進反思 + Hiranabe 2021 譜系 + 「圖→直覺→符號→推導→**互動 = do**」5 階學習階梯 + Confucius "I do and I understand"
  - **Q02 矩陣為什麼存在？「把表格看成單一物件」是什麼躍進？**（~78 行）— 7 時代里程碑表（《九章算術》→ 關孝和 1683 → Leibniz 1693 → Cramer 1750 → Sylvester 1850 → Cayley 1858 → Frobenius 1878）+ 100 元方程「方程組視角 vs 矩陣物件視角」對比 + 6 條物件化代數紅利 + 「抽象階層提升」原則（標量 → 向量 → 矩陣 → 張量類比 OOP / 物理 / 生物）
  - **Q03 為什麼同一個矩陣要看成 4 種視角？**（~85 行）— V1-V4 4 視角分工總表 + **三角形面積公式類比**（基×高 / 海倫 / $\frac{1}{2}ab\sin C$ / $\frac{abc}{4R}$，公式不同三角形同一個）+ 3 個案例對比視角效率（$\mathbf{b} \in \mathbf{C}(A)$ 判斷、列秩=行秩、$AB$ 4 種讀法）
  - **Q04 點積為什麼是「分量相乘再相加」？**（~140 行）— 三條獨立動機殊途同歸：① 幾何（餘弦定理 boxed 推導 $\sum u_i v_i = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$）+ ② 物理（功 = 各軸獨立做功之和）+ ③ 代數（內積 4 公理 + 標準基底正交 $\delta_{ij}$）+ 12 個衍生概念表（norm / 正交 / 投影 / Cauchy-Schwarz / QR / SVD / 最小平方法）
  - **Q05 外積為什麼是「列 × 行 = 秩 1 矩陣」？**（~108 行）— 點積外積對偶設計表（矩陣乘法形狀規則自動決定，中間維 $k$ 大→標量、$k$ 小→矩陣）+ 列/行視角秩 1 雙證明 + 3×2 小例題秩驗證 + 「秩 1 是線代原子」三大秩 1 之和結構表（MM4 / CR / SVD）+ SVD 壓縮率 $\frac{m+n}{mn}$ 應用根源
  - **Q06 $A\mathbf{x}$ 為什麼這樣定義？**（~141 行）— 從 $m$ 個方程濃縮為 $A\mathbf{x}=\mathbf{b}$ 的 4 步驟設計過程（拆 $A,\mathbf{x},\mathbf{b}$ → 要求結果 → 觀察規律 → 兩讀法等價）+ 讀法 A 點積 / 讀法 B 線組合 + $2 \times 3 \cdot 3 \times 1$ 小例題雙路驗證 → $\begin{bmatrix}50\\122\end{bmatrix}$ + 「動詞 + 受詞」最小單位昇華 + 矩陣兩角色（係數表 vs 變換）
  - **Q07 為什麼要有 2 個視角（點積 + 線性組合）？**（~95 行）— 7 欄視角分工總表 + 關鍵案例「$A\mathbf{x}=\mathbf{b}$ 有解嗎」(Mv1) vs (Mv2) 對比（一秒判斷 vs 跑完高斯）+ Strang 原話兩段引用（"the heart of linear algebra"）+ 7 條任務 × 視角配對表
  - **Q08 四個基本子空間為什麼會自然冒出？**（~156 行）— **2 方向（右乘 vs 左乘）× 2 概念（像 vs 核）= 4 組合必然產物** + $\mathbf{N}(A) = \mathbf{C}(A^{\mathrm{T}})^{\perp}$ 完整證明（$A\mathbf{x}=\mathbf{0}$ 用 (Mv1) 點積視角展開 → 每橫躺行垂直）+ rank-nullity 兩 boxed 等式 + Strang Big Picture ASCII 圖 + 7 條「4 子空間怎麼把線代組織起來」應用表（解 $A\mathbf{x}=\mathbf{b}$ / 最小平方法 / SVD 構造 4 子空間正交基底 / 偽反 $A^{+}$）
- [x] **S12 主章 callout 批量插入**：4 個檔案的「章節摘要」段末（術語提醒 ⚠ 之後、`---`「數學要點」段之前）插入客製化 callout，採短摘要列表式（~150-300 字 hook + 連結附錄 D）格式：
  - [front-foreword.md](../book/front-foreword.md)（1 callout / 1 link Q01）+ 順手修「23 個 VizScript」→「36 個 VizScript（主章 33 + 附錄 3）」舊數字 bug
  - [ch01-viewing-matrix.md](../book/ch01-viewing-matrix.md)（1 callout / 2 links Q02 + Q03）
  - [ch02-vec-vec.md](../book/ch02-vec-vec.md)（1 callout / 2 links Q04 + Q05）
  - [ch03-mat-vec.md](../book/ch03-mat-vec.md)（1 callout / 3 links Q06 + Q07 + Q08）
- [x] **S12 memory 新增** — feedback_why_layer.md 明文化「全書每個運算規則需附『背後觀念』3-layer」規範（① 歷史 / ② 設計過程還原 / ③ 概念昇華 必有的層級規則 + 落點方案 D + 篇幅指南 + 觸發時機 + 自驗檢查）；MEMORY.md index 補一行指向新 memory
- [x] **S13 §4 + §5 背後觀念 Q10-Q13 批量寫作**：[appendix-D-why.md](../book/appendix-D-why.md) 從 1175 行擴至 **1657 行（+482 行）**，目錄表 Q10-Q13 4 條從「🚧 規劃中」→「✅ 已完成（S13）」+ 加錨點連結；尾段「其餘 13 條」改「其餘 9 條（Q14-Q22）」+ 改 S14-S15 路線；附錄末時間戳更新「S13 (2026-05-13) — Q01-Q13 完成（13/22, 59%）」
  - **Q10 為什麼乘法不可交換 AB≠BA**（95 行）— ① Hamilton 四元數 1843 革命 + Cayley 1858 觀察 + Frobenius/Jordan 系統化 / ② 四層理由：形狀層面 + (MM4) 拆解對象不同 + 2×2 剪切矩陣小例題 + 函數合成本質（穿襪→穿鞋類比）+ 可交換條件三種情形 / ③ 順序資訊代數刻畫 + 5 跨領域對應表（量子/神經網路/機器人/編譯器/微分幾何）
  - **Q11 對角矩陣為什麼這麼特別**（111 行）— ① Gauss-Jordan + Sylvester 1852 慣性定律 + Cayley-Hamilton + 數值線代基石 / ② 四超能力：純倍率作用（不耦合）+ 冪反指數逐元素表 + 恆可交換 + 特徵值/det/tr/rank 白送表 + 4 元素 D 小例題 + §6 中間項策略表 / ③ 「矩陣世界中的標量」+ Strang LAFE §6.1 引言「Make every matrix look diagonal」
  - **Q12 (P3) 動態系統為什麼能用特徵值預測長期**（121 行）— ① Lagrange 1762 主模態 + Euler 1740 指數解法 + Cauchy 1829 抽象化 + Poincaré 1881 動力系統穩定性 / ② (P3) 公式三步走分解（座標變換→解耦演化→反變換）+ $\lambda_{\max}$ 主導 + 4×4 穩定性分類表 + Fibonacci 黃金比例小例題（Binet 公式從特徵值直接讀） / ③ 特徵值 = 動態系統 DNA + 7 跨領域應用表（PageRank/量子基態/PCA/馬可夫穩態/結構工程/神經網路訓練/生態學）
  - **Q13 (P4) 三明治為什麼線代核心**（156 行）— ① Sylvester 1852 → Jordan 1870 → Schmidt 1907 → Eckart-Young 1936 = 100 年史線 / ② 三明治三層分解策略（進入最簡視角→純對角縮放→換回原視角）+ 三威力（降維 + 函數計算 + 視角切換哲學）+ 6 跨領域視角切換對應表（物理/訊號/量子/機器學習/影像壓縮/氣候）+ 對稱矩陣 2×2 EVD 完整驗算 + (P3)↔(P4) 對偶總表 / ③ 「矩陣 = 視角切換 + 純對角縮放 + 視角切換回來」代數刻畫 + §6 五大分解 (P4) 譜系表 + 「世紀大夢」最強昇華
- [x] **S13 ch04 + ch05 主章 callout 客製化**：[ch04-mat-mat.md](../book/ch04-mat-mat.md) 章節摘要末新增 callout（連結 Q09 矩陣乘法行乘列來源 + Q10 不可交換本質，2 Q&A links）+ [ch05-patterns.md](../book/ch05-patterns.md) 章節摘要末新增 callout（連結 Q11 對角矩陣超能力 + Q12 (P3) 動態預測 + Q13 (P4) 三明治世界觀，3 Q&A links）— 採短摘要列表式（~250-400 字 hook + 連結附錄 D）格式，與 S12 ch01/ch02/ch03 callout 一致；ch05 callout 中 1 處 typo「appendix-D-view」→「appendix-D-why.md」即時修正
- [x] **S13 累計進度：** 全書主章 callout 6 個（S12 的 4 個 + S13 的 2 個）共 13 Q&A links / appendix-D-why.md 13/22 Q&A = 59%；S14-S15 路線剩 9 條 Q&A（§6 五大分解 6 + 3 附錄）+ 6 chapters callout（ch06a-ch06f）+ 3 附錄 callout + 整合收尾（BOOK.md 重新生成 + 跨檔 anchor 校驗）
- [x] **S14 §6 6 條 Q&A 批量寫作**：[appendix-D-why.md](../book/appendix-D-why.md) 從 1657 行擴至 **2740 行（+1083 行 / 65% 增量）**，目錄表 Q14-Q19 6 條從「🚧 規劃中」→「✅ 已完成（S14）」+ 加錨點連結；尾段「其餘 9 條（Q14-Q22）」改「其餘 3 條（Q20-Q22）」+ 改 S15 路線；附錄末時間戳更新「S14 (2026-05-13) — Q01-Q19 完成（19/22, 86%）— §6 五大分解 + 整體動機 6 條全部完成」
  - **Q14 為什麼要把矩陣「分解」？**（156 行 / §6 整體動機）— ① Gauss 1809《Theoria Motus》→ Jacobi 1846 → Sylvester 1852 → Cayley 1858 → Schmidt 1907 → Eckart-Young 1936 → 1940-60s 數值線代 → 1965 Golub-Kahan → LINPACK/LAPACK → 2000s ML 完整 200 年史 / ② 6 大工程動機詳述（求解 LU/QR/SVD + 求冪 EVD + 求反偽反 + 穩定性 + 壓縮降秩 + 結構理解）+ 「六動機↔五分解」對應總表 + 「為什麼正好五個」5 級對稱性遞進表 / ③ Strang LAFE §6.1「Make every matrix look diagonal」+ 三層昇華（計算效率 / 物理意義 / 跨領域統一）
  - **Q15 A=CR 為什麼成立？列秩=行秩自然冒出**（119 行）— ① Sylvester 1851 引入 rank + Frobenius 1879 系統證明 + Strang 2020《LAFE》首次代數封裝「最樸素分解」 / ② C 列空間獨立列 + R 由 rref 非零行兩步建構 + 3×3 rank 2 完整算驗 + 雙重讀法自然冒出列秩=行秩=r / ③ CR 在「對稱性↔一般性」光譜最樸素端 + 五分解對照表 + 教學三功能（rank 視覺化 + 「列秩=行秩」自然證明 + 「分解」入門最低門檻）
  - **Q16 A=LU 高斯消去法本質**（165 行）— ① 《九章算術》方程章公元 1 世紀東方原型「遍乘直除」比 Gauss 早 1800 年 → Newton 1707 → Gauss 1809 Ceres 命名源頭 → Doolittle 1878 → Banachiewicz 1938 → Turing 1948「LU」命名 + partial pivoting + 數值穩定性 → Wilkinson 1965 → LINPACK/LAPACK / ② 單位下三角矩陣 $E_{ik}$ 左乘表述消去 + 推得 $A=M^{-1}U=LU$ + $L$ 元素正是消去倍數 $\ell_{ik}$ + 3×3 LU 完整算驗 + 主元 + partial pivoting + 三角矩陣 6 大性質表 / ③ 「演算法→代數結構」三威力（複用 / 分析 / 嫁接其他結構）+ 5 跨領域「因果結構」對應表（訊號處理因果濾波器 / 時序 AR / 動態規劃 / DAG 編譯器 / 拓樸電路）+ 「LU 是『演算法被代數化封裝』在線代中的最古老案例」
  - **Q17 A=QR Gram-Schmidt 動機**（138 行）— ① Gauss 1801 用最小平方法算 Ceres 軌道 → Legendre 1805 → Gauss 1809 Theoria Motus 正規方程 → Gram 1883 → Schmidt 1907 命名 → Householder 1958 數值穩定 / ② 「正交基底=無耦合最佳座標」 + 逐步扣除耦合演算法 + $A=QR$ 自動冒出（上三角 $R$ 因組合係數只用前 $k$ 個 $\mathbf{q}$）+ 3×2 Gram-Schmidt 完整算到驗證 / ③ 最小平方法用 QR vs 正規方程（不放大條件數）+ QR 是 EVD/SVD 前置 + 「分解化是把演算法封裝為代數物件的標準路徑」
  - **Q18 S=QΛQᵀ 對稱特徵向量自動正交**（144 行）— ① Cauchy 1829 主軸定理 + 對稱矩陣實特徵值 → Sylvester 1852 慣性 → Jacobi 1846 旋轉 → Schur 1909 → 量子力學 1920s Hermitian / ② 雙證明：① $(\lambda_1-\lambda_2)\mathbf{q}_2^{\mathrm{T}}\mathbf{q}_1=0$ 因 $S=S^{\mathrm{T}}$ + ② $\lambda=\bar\lambda$ 實特徵值（複向量取共軛轉置）+ 重根情況 Gram-Schmidt 內部化 + 2×2 對稱 $S=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ 完整算驗 / ③ 5 物理對稱↔數學物件對應表（能量守恆 / 時間反演 / 空間旋轉 / 馬可夫可逆 / 二次型）+ 對稱矩陣 5 特性↔(P4) 兩基底合一解釋 + 「對稱矩陣是最容易看清的矩陣」+ SVD = 任意矩陣也能像對稱那樣容易看清的廣義版本
  - **Q19 A=UΣVᵀ SVD 為什麼任意矩陣存在**（174 行）— ① Beltrami 1873《Sulle funzioni bilineari》首次發現（雙線性形式對角化）→ Jordan 1874 變分定義獨立 → Sylvester 1889 矩陣語言 → Schmidt 1907 無限維 + 低秩近似觀察 → Eckart-Young 1936 最佳低秩近似 Psychometrika → Mirsky 1960 推廣到所有 unitarily invariant norm → Golub-Kahan 1965 第一實用演算法 → Golub-Reinsch 1970 LAPACK 祖先 / ② 雙證明路徑：① 透過 $A^{\mathrm{T}}A$ 譜定理建構性（$A^{\mathrm{T}}A$ 永遠對稱半正定 + Q18 譜定理 → 普世存在）+ ② Jordan 1874 變分定義 $\sigma_1=\max\|A\mathbf{x}\|$（Weierstrass 緊集 + 遞迴）+ 3 大突破（不需方陣 / 不需可對角化 / 奇異值永遠非負實）+ SVD 自動讀出 4 子空間正交基底表 + **3×2 SVD 完整小例題巧妙連動 Q17 同 $A$ + $A^{\mathrm{T}}A=$ Q18 同矩陣形成「Q17 QR → Q18 EVD → Q19 SVD」教學鏈** / ③ 3 層昇華：(P4) 三明治最強形式 5 分解強度表 + 全書集大成 8 個跨章節整合表 + Eckart-Young 1936 最佳低秩近似 → 圖像壓縮/推薦/PCA/神經網路全建立於此 + Strang LAFE Ch.7「the most important theorem in linear algebra」名言
- [x] **S14 ch06a-ch06f 6 主章 callout 客製化**：採短摘要列表式（~250-450 字 hook + 連結附錄 D）格式，與 S12-S13 callout 一致；放在「章節摘要」段末（最後一個內容段之後、`---`「數學要點」段之前）
  - [ch06a-five](../book/ch06a-five.md)（331 → 339 行 / 3 Q&A links Q14+Q11+Q13，hook「五大分解為什麼正好五個 + LAFE『Make every matrix look diagonal』+ 5 級遞進對稱性」）
  - [ch06b-CR](../book/ch06b-CR.md)（545 → 552 行 / 2 Q&A links Q15+Q14，hook「最樸素的分解 + rank 視覺載體 + Strang 2020 首次代數封裝」）
  - [ch06c-LU](../book/ch06c-LU.md)（654 → 661 行 / 2 Q&A links Q16+Q14，hook「《九章算術》方程章 2000 年東方原型 + Turing 1948 LU 命名 + 5 跨領域因果結構」）
  - [ch06d-QR](../book/ch06d-QR.md)（541 → 547 行 / 1 Q&A link Q17，hook「200 年最小平方→Hilbert 演化 + Gauss 1801 Ceres → Householder 1958 + 條件數不被平方化」）
  - [ch06e-QLQ](../book/ch06e-QLQ.md)（695 → 703 行 / 3 Q&A links Q18+Q11+Q13，hook「物理對稱性=數學正交性 + Cauchy 1829 主軸定理 + 完美三明治」）
  - [ch06f-USV](../book/ch06f-USV.md)（934 → 943 行 / 4 Q&A links Q19+Q14+Q08+Q13，hook「Beltrami 1873 首次發現 + Strang『the most important theorem』+ SVD 唯一同時對應所有 6 工程動機」）
- [x] **S14 累計進度：** 全書主章 callout 12 個（S12 的 4 個 + S13 的 2 個 + S14 的 6 個）共 28 Q&A links — **全主章 100% 覆蓋（foreword + ch01-ch06f）** / appendix-D-why.md 19/22 Q&A = 86%；S15 路線剩 3 條 Q&A（3 附錄）+ 3 附錄 callout + 整合收尾（BOOK.md 重新生成 + 跨檔 anchor 校驗 + HANDOFF / SESSION_INDEX / SOP_DRAFT 收尾）
- [x] **S15 § 收尾 §1：Q20-Q22 §A-§C 3 條 Q&A 批量寫作**：[appendix-D-why.md](../book/appendix-D-why.md) 從 2740 行擴至 **3522 行（+782 行 / 29% 增量）**，目錄表 Q20-Q22 從「🚧 規劃中」→「✅ 已完成（S15）」+ 加錨點；尾段「其餘 3 條」→「其餘 0 條」+ 時間戳「Q01-Q22 完成（22/22, 100% ✓）」
  - **Q20 特徵值的「地圖」為什麼能畫得出來？**（225 行 / Appendix A）— ① Cauchy 1829 主軸定理 → Hermite 1855 → Cayley 1858 → Perron-Frobenius 1907/1912 → Schur 1909 → **Toeplitz 1918 Normal matrix** → Gershgorin 1931 → Hiranabe 2021 視覺集大成 共 200 年 8 代學者 / ② 8 類矩陣特徵值幾何位置代數推導（對稱 / 反對稱 / 正交 / 投影 / 冪零 / zI / 奇異 / Markov）+ 統一機制「**多項式 functional calculus**」p(A)=O ⇒ p(λ)=0 / ③ **Normal matrix 是地圖能畫的代數源頭** + 實軸/虛軸/單位圓三條對偶曲線對應 Hermitian/skew-Hermitian/unitary + Cayley 變換 z↦(1-z)/(1+z) + 量子力學 $U=e^{-iHt/\hbar}$ 統一範例 + 「分類先於分解」教學作用
  - **Q21 Matrix World 為什麼是「同心橢圓繼承樹」而非「樹狀」？**（246 行 / Appendix B）— ① Aristotle ~350 BC 樹狀分類 → Euler 1768 同心圓集合包含首次明確視覺化 → Venn 1880 → Cantor 1895 → Hasse 1934 + Birkhoff 1948 格論 → **Bourbaki 1939+ 結構主義** → Hiranabe-Strang 2023 共 250 年史 / ② **4 替代方案逐一致命缺陷**（樹狀:線代非樹單一父；Venn:11 集合 2048 區域災難；UML:無「越特殊越在內」直覺；Hasse:無法承載多層次資訊）+ **同心橢圓 4 大優勢**（包含視覺同形 / 多重繼承自動 / 徑向距離精確 / 兩條軸線承載多層）/ ③ **結構主義 vs 還原主義哲學對立**（Bourbaki vs Aristotle）+「結構越特殊分解越精緻」代數律 + 逆向學習支援 + **最內 {I, O} 極端對立統一**（Hegel + 老子 + 量子力學）+ 「Matrix World 是線代結構主義的視覺宣言」
  - **Q22「解 Ax=b」為什麼是線代的核心問題？**（**311 行 = 全書最長 Q&A** / Appendix C）— ① **4000 年史**:巴比倫 ~1800 BC 楔形泥板 YBC 4652 → **《九章算術》方程章 公元 1 世紀 高斯消去東方原型「遍乘直除」** → al-Khwarizmi 825 algebra 詞源 → Cramer 1750 → **Gauss 1809 Ceres 軌道最小二乘** → Cayley 1858 矩陣物件化 → Frobenius 1879 rank-nullity → **Moore 1920 + Penrose 1955 偽反矩陣 A+ 是 Ax=b 4000 年探索史最終解答** → Turing 1948 LU → Golub-Reinsch 1970 SVD → LAPACK 1992 → 2010s+ ML / ② **6 步從零推導全部線代**:Step 1 n 方程濃縮為 Ax=b 自然生矩陣物件 / Step 2「有解嗎」→ 列空間 + 「解唯一嗎」→ 零空間 / Step 3 對偶化 → 4 子空間 + rank-nullity / Step 4「怎麼算」→ 五大分解 5 情境工具 / Step 5「無解怎麼辦」→ Gauss 1801 最小二乘設計過程還原 4 步 + 正規方程 + 幾何=投影 / Step 6 SVD 補完 → 偽反 $\mathbf{x}^* = A^{+}\mathbf{b}$ 對任意矩陣統一公式 + **5 種 Ax=b 情境完整表**（唯一/無窮/無解/rank-deficient/病態 ↔ Cramer/LU/QR/SVD/Tikhonov）/ ③ 5 層昇華:**「Ax=b 是線代的元問題」** 10 主題派生對應表 + **「逆向工程」是科學本質** 13 領域對應表（物理/電路/控制/統計/ML/量子/機器人/MRI/CT/神經網路/推薦/Hartree-Fock）+ **全書 22 條 Q&A 會師結構表**（Q01-Q21 逐條對 Ax=b 關係）+ Strang 50 年教學「方程 vs 結構雙重視角」最終啟示 + 最強昇華「**Linear Algebra = the study of Ax=b in all its depth**」
- [x] **S15 § 收尾 §2：3 附錄 callout 批量插入**：採短摘要列表式（與 S12-S14 的 12 主章 callout 同格式）
  - [appendix-map-eigenvalues](../book/appendix-map-eigenvalues.md)（272 → 280 行 / +8 行 / 3 Q&A links Q20+Q18+Q11，hook「『地圖』為什麼畫得出來？12 個幾何指紋的代數源頭」）
  - [appendix-matrix-world](../book/appendix-matrix-world.md)（329 → 336 行 / +7 行 / 3 Q&A links Q21+Q14+Q19，hook「為什麼選『同心橢圓』而非樹狀？分解粒度為何隨深度遞增？」）
  - [appendix-four-subspaces](../book/appendix-four-subspaces.md)（335 → 342 行 / +7 行 / 3 Q&A links Q22+Q08+Q19，hook「Ax=b 為什麼是線代核心？4 子空間從哪裡冒出來？」）
  - **累計 15 callout / 37 Q&A links — 全書 16 個內容 md 100% 覆蓋達成 ✓**
- [x] **S15 § 收尾 §3：跨檔 anchor 校驗**：grep 全書 37 條 `appendix-D-why.md#qNN` 跨檔引用（front 1 + ch01-ch06f 22 + back 0 + 3 附錄 9 + 餘）+ 22 個 q01-q22 錨點對照 → **0 broken link** ✓ + appendix-D-why.md 內部 Q↔Q cross-link 全在 q01-q22 範圍 → **0 out-of-range** ✓
- [x] **S15 § 收尾 §4：BOOK.md 重生**：[BOOK.md](../book/BOOK.md) 從 8650 → **12305 行（+3655 / +42% 增量）**，採 S11 確立的 **fence-code-aware awk**（`BEGIN{f=0} /^```/{f=!f; print; next} !f && /^#+ /{sub(/^/, "#"); print; next} {print}`）合併 17 md（加入 appendix-D-why 新檔）→ 全部 heading 加 `#` 前綴降一級、fenced code block 保護完美、22 個 Q&A H3 正確降級、19 個 H2 邊界正確（2 header + 17 主章/附錄）；header 12 處數字更新 + 新增「**背後觀念層 22 Q&A 結構表**」+「**全書 15 callout 覆蓋表**」兩個結構表
- [x] **S15 § 收尾 §5：SCHEMA.md 補 §3.6「背後觀念 callout 規範」**（[SCHEMA.md §3.6](../book/SCHEMA.md#36-背後觀念-callout-規範s12-s15-確立)，~110 行）— 觸發時機 + 插入位置 + quote block 模板 + 篇幅規範表 + Hook 設計準則 + Q&A link 選擇規則 + 全書 15 callout 對照表 + 版本升至 0.3
- [x] **S15 § 收尾 §6：VIZ-CATALOG.md 新增「Appendix D 背後觀念層 22 Q&A 索引」獨立段**（~40 行）— 22 條 Q&A 列表 + 對應主章 + session + 連結 + 3-layer 框架說明 + 三條閱讀路線（隨章 / 集中 / 主題追蹤）+ 全書文件結構表更新（補 appendix-D-why.md + SCHEMA §3.6 標註）+ 變更歷史新增 S15 行
- [x] **S15 累計進度：** **全書 22/22 Q&A = 100% 完成 ✓** / **全書 15 callout / 37 Q&A links / 16 個內容 md 100% 覆蓋達成 ✓** / appendix-D-why.md **3522 行** / BOOK.md **12305 行** / **S12-S15 4-session 路線完成（總耗時 ~11h，平均 30 min/Q&A）**
- [x] **S16 Marimo 技術棧 PoC 三階段全通過** — Back 選不立刻挑旗艦先做技術棧 PoC + 載體討論（先例 6 個 + 6 平台比較 → 維持 Marimo + WASM）；耗時 ~2.5h；產出 viz/ 7 檔（.gitignore / .python-version / README.md / pyproject.toml / uv.lock / hello.py / ch01_mv1_poc.py）+ commit `2f9b9e3`
- [x] **S16 Stage 1 hello.py（4 cell reactive slider）** — brew install uv 0.11.14 → uv init viz --python 3.12（Anaconda 3.9.13 太舊 pin 3.12 對齊 Pyodide WASM target）→ uv add marimo plotly matplotlib numpy scikit-learn pillow（裝完 marimo 0.23.6 + plotly 6.7.0 + matplotlib 3.10.9 + sklearn 1.8.0 + pillow 12.2.0 + numpy 2.4.4 + scipy 1.17.1）→ hello.py（slider × 向量長度 n → numpy arange + np.linalg.norm + sum + LaTeX 渲染）→ marimo export html-wasm 27 MB static dir → 本機 http.server :8765 Back ✅ 確認 work
- [x] **S16 Stage 2 ch01_mv1_poc.py（7 cell × (Mv1)+(Mv2) 雙觀點）** — 4 slider for A entries（a11/a12/a21/a22 範圍 -3~3）+ 2 for x（x1/x2 範圍 -3~3）+ mo.hstack/vstack 控制面板 + 數值 cell + 即時計算 LaTeX md + plotly 2D 含 4 箭頭（x 藍 / col1 綠 / col2 紅 / Ax 紫虛線）+ (Mv2) 平行四邊形透明黃；本機 import_module 雙路驗證 A @ x == row_dot_x（Mv1）== x[0]·col1 + x[1]·col2（Mv2）三式一致；對應 [ch01-viewing-matrix.md](../book/ch01-viewing-matrix.md) 最小互動版
- [x] **S16 Stage 3 marimo export html-wasm（27 MB static dir）** — `marimo export html-wasm ch01_mv1_poc.py -o dist/ch01_mv1_poc`；含 Pyodide WASM runtime + 全部 cell 序列化嵌入 HTML；可 GitHub Pages / Cloudflare Pages / Netlify 拖目錄直接部署；本機驗證用 `python -m http.server --directory dist 8765` over HTTP（不可 file://，瀏覽器 CORS 限制）
- [x] **S16 3 round Stage 2 WASM debug — 真因 + 修法** —
  - **Round 1（防禦性重寫，猜錯方向）：** 猜 3 風險 LaTeX 在 slider label 卡 Pyodide / slider 嵌 markdown f-string table / plotly `angleref="previous"`+`symbol=["circle","arrow-up"]` 新特性；對應改成 plain label + mo.hstack/vstack 排版 + fig.add_annotation(arrowhead=3) 箭頭；本機 OK，WASM 仍錯 → 沒抓到根因
  - **Round 2（console log 揭真因）：** Back 貼 console「`ModuleNotFoundError: No module named 'plotly'`」 — Pyodide 預設只裝 Pygments+docutils+jedi+numpy+parso+pyodide-http，**沒裝 plotly！** 修：在 ch01_mv1_poc.py 頂端加 **PEP 723 inline script metadata block**（`# /// script` + `requires-python = ">=3.12"` + `dependencies = ["marimo", "numpy", "plotly"]` + `# ///`）— marimo export 解析此 block 嵌入 HTML 的 requirements 陣列，Pyodide 啟動時用 micropip 自動下載
  - **Round 3（顯式渲染器）：** 加完 PEP 723 後 Back 報「沒報錯但一片空白」→ 判斷 bare `fig` 透過 `_repr_mimebundle_` 顯示可能沒接到 plotly 渲染器；改用 `mo.ui.plotly(fig)` 顯式包裝（marimo 內建 plotly UI widget）+ cell 加 `mo` 到 closure args → Back ✅「可以了，我等不夠久」**真正卡點是 plotly wheel 首次下載要 ~30-60s**，UX 上要在 README / 開啟頁面前告訴讀者「等 Loaded plotly 訊息」
- [x] **S16 SOP §2.15「Marimo WASM 部署 3 大非顯而易見陷阱」** — (1) PEP 723 inline script metadata 是 marimo WASM 額外 deps 唯一聲明處（uv add 只裝本機 .venv）/ (2) plotly fig 必須 mo.ui.plotly(fig) 顯式包裝才 WASM 渲染穩 / (3) 首次載入要等 30-60s（Pyodide + plotly wheel + plotly.js bundle 三層下載），UX 必須警告 + S17+ 旗艦開工 5 條 checklist（PEP 723 block / mo.ui.plotly wrap / mo 加 closure / WASM export 後 console 必看 / 首頁 30s 警告）
- [x] **S16 viz/README.md 含 Immersive Math 等先例 + Marimo vs Jupyter/Streamlit/Observable 對照表** — 技術棧上手 6 步 + 為什麼選 Marimo（vs Jupyter 非反應式 / Streamlit 需 server / Observable JS 重寫數學庫）+ 目前 notebook（hello.py / ch01_mv1_poc.py）+ 下一批計畫（VIZ-CATALOG 首批 Tier 3 旗艦）+ 部署 GitHub Pages / Cloudflare Pages / Netlify / Vercel + WASM 需 HTTP 不可 file:// + 開發守則（@app.cell 內修改 / SCHEMA §3.5 全書視覺錨點 / VIZ_SCHEMA 13 段 A-M）
- [x] **S17 ch04 V-02 MM4 母模板架構階段** — Back 選 HANDOFF S16 推薦路線 A 開始 [ch04-mat-mat.md VizScript-02](../book/ch04-mat-mat.md#vizscript-02)；S17 scope 鎖「最小可動骨架」；產出 [viz/ch04_matrix_matrix.py](../../viz/ch04_matrix_matrix.py) 440 行 / 8 cell + viz/_common/{__init__.py, rank1_layer.py}；2 round WASM debug 才通；commit `cc957f1`
- [x] **S17 Stage A 檔案結構 + PEP 723 metadata** — `viz/ch04_matrix_matrix.py` 頂端 PEP 723 inline metadata block 含 marimo + numpy + plotly；建立 `viz/_common/` 子目錄含 `__init__.py` + `rank1_layer.py`（rank1_outer / layers_of / accumulate / layer_energy 4 個工具函數，本機 reference / S18+ 非 WASM script 用；WASM export 不嵌入子模組 import 所以 notebook 內聯 helper）
- [x] **S17 Stage B 小矩陣模式骨架** — A (3×2) 6 entry sliders + B (2×2) 4 entry sliders（VizScript 預設值 A=[[1,2],[3,4],[5,6]] / B=I_2 使 AB=A 便於對拍）+ 累加項數 r slider [0, 2] + mo.hstack/vstack 三欄控制面板（A / B / 累加控制）
- [x] **S17 Stage C 即時計算 cell + 三式對拍** — A, B, k 構造 + target_C = A @ B + r_val = int(r.value) + Cr = accumulate(A, B, r_val) + error + 相對誤差 ||C-Cr||_F / ||C||_F + layers + energies + **健康檢查 `A@B == sum of rank-1 layers == accumulate(A,B,k)` ✓ 顯示在 markdown 區**
- [x] **S17 Stage D 主舞台 2×3 共 6 heatmap subplot** — 列 1：秩 1 圖層 1 / 圖層 2 / 累加 Cr；列 2：(空) / 目標 C / 誤差 |C-Cr|；layers heatmap 依 r_val 灰/亮（opacity 0.35 / 1.0）；signed colormap RdBu_r 雙向 + zmid=0；error colormap Oranges 單向絕對值；cell 數字 12pt + hovertemplate `(%{y}, %{x}) = %{z:.2f}`；y 軸 reversed 對齊數學矩陣慣例左上原點
- [x] **S17 Stage E 秩 1 圖層 strip** — k 個橫排 heatmap subplot（k=2）+ subplot_titles 含 `p={p+1} | 能量 {energies[p]:.2f} | {已累加/尚未累加}` 完整字串（不後置 annotations 改）+ 灰/亮 opacity 依 p < r_val
- [x] **S17 Stage F WASM export + 部署驗證** — `.venv/bin/marimo export html-wasm ch04_matrix_matrix.py -o dist/ch04_matrix_matrix` → 27 MB static dir；本機 `python -m http.server --directory dist/ch04_matrix_matrix 8765`；HTTP 200 + title `ch04 matrix matrix`；console clean（no STDERR / no Traceback）；PEP 723 觸發 `Loading from micropip: ['plotly']` ✓
- [x] **S17 2 round WASM debug 過程記錄** — (R1) Back 報「sliders + 結尾說明顯示，中間 3 cell 不見」→ 真因 marimo `_` 前綴 cell-private 不跨 cell export，下游 NameError 整個 cell 沉默不渲染 → 修 helper 合併同一 cell + 命名無 `_` 前綴 / (R2) console 兩個 STDERR：① 主舞台 `TypeError: bad operand type for abs(): 'list'` ← dummy `[[0]]` plain list → `np.asarray(M, dtype=float)` + `np.abs()` / ② strip `IndexError: tuple index out of range` ← plotly `subplot_titles=[""] * k` 空字串被跳過不生成 annotation → make_subplots 直接傳完整 title
- [x] **S17 SOP §2.15 補入 3 個新 WASM 陷阱**（合計 6 大）— (4) marimo `_` 前綴 cell-private 不跨 cell export；跨 cell 共用的函數 / 變數命名不可 `_` 開頭，變通：helper 合併同一 cell（推薦） / (5) plotly `make_subplots(subplot_titles=[""] * k)` 空字串會被跳過不生成 annotation slot，後置 `annotations[p].text = ...` IndexError；變通：直接傳完整最終 title 或 placeholder 非空字串 / (6) plotly heatmap z 參數最好 `np.asarray(M, dtype=float)` 包一層，helper 內 `M = np.asarray(M, dtype=float)` 保護 + `abs()` → `np.abs()` 用 numpy 介面

### 進行中
- 無，**S17 已收尾，ch04 V-02 母模板架構階段完成**（commit `cc957f1`）。下次 S18 從 S17 骨架接「**圖像模式 + Mona Lisa SVD**」（VizScript-02 模式 2：64×64 灰階圖像 4 張預計算 SVD + cache + 三圖並列原圖/重建/誤差 + radio 切換 + 相對誤差數字）；S19 補完 Tier 3（飛入動畫 800ms / 4 重排序對比 / 誤差曲線 / Walkthrough 6 步 / 快捷鍵 / hover tooltip）

### 待辦（多 session 路線圖 v3 — S11 整合 + S12+ 視覺化實作）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema 規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| ✅ S02 | §1 Viewing a Matrix - 4 Ways | `ch01-viewing-matrix.md`（418 行） |
| ✅ S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md`（497 行） |
| ✅ S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces） | `ch03-mat-vec.md`（935 行） |
| ✅ S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md`（849 行） |
| ✅ S06 | §5 Practical Patterns | `ch05-patterns.md`（830 行） |
| ✅ S07 | §6 五大分解總覽 + §6.1 A=CR（兩章 session）| `ch06a-five.md`（331 行）+ `ch06b-CR.md`（545 行） |
| ✅ S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`（654 行）+ `ch06d-QR.md`（541 行） |
| ✅ S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`（695 行）+ `ch06f-USV.md`（**934 行，全書最長**） |
| ✅ S10 | Foreword + Conclusion + 3 附錄 | `front-foreword.md`（158）+ `back-conclusion.md`（198）+ `appendix-map-eigenvalues.md`（272）+ `appendix-matrix-world.md`（**328 旗艦**）+ `appendix-four-subspaces.md`（334）= **1290 行 + 3 VizMark** |
| ✅ S11 | 整合 + 校對 + 風格統一 + `BOOK.md` + `VIZ-CATALOG.md` + Strang PDF 防護 | [BOOK.md](../book/BOOK.md)（8650 行）+ [VIZ-CATALOG.md](../book/VIZ-CATALOG.md)（241 行 metadata）+ SCHEMA.md §3.5 全書視覺錨點 + 9 處 anchor 修復 + Tier 表 6 處校正 + 23 處風格 sed 修正 + .gitignore PDF 防護 |
| ✅ S12 | **背後觀念層啟動：Foreword + §1 + §2 + §3 共 9 Q&A + 4 主章 callout** | [appendix-D-why.md](../book/appendix-D-why.md)（1175 行 / 9 Q&A，含 Q09 PoC + Q01-Q08 批量）+ 4 主章 callout（foreword / ch01 / ch02 / ch03 共 8 Q&A links）+ memory feedback_why_layer.md（3-layer 框架）+ foreword「23→36」舊數字 bug 修 |
| ✅ S13 | **§4 + §5：Q10–Q13（4 條 Q&A）+ ch04 / ch05 主章 callout** | [appendix-D-why.md](../book/appendix-D-why.md) 從 1175 行擴至 **1657 行（+482 行 / 13 Q&A = 59%）**：Q10 不可交換（95）+ Q11 對角矩陣（111）+ Q12 (P3) 動態預測（121）+ Q13 (P4) 三明治（156）+ 2 主章 callout（[ch04](../book/ch04-mat-mat.md) Q09+Q10 / [ch05](../book/ch05-patterns.md) Q11+Q12+Q13 共 5 Q&A links）+ ch05 1 處 typo 修 |
| ✅ S14 | **§6 五大分解：Q14–Q19（6 條 Q&A）+ ch06a–ch06f 主章 callout — 全主章 100% 覆蓋** | [appendix-D-why.md](../book/appendix-D-why.md) 從 1657 行擴至 **2740 行（+1083 行 / 19 Q&A = 86%）**：Q14 分解動機（156）+ Q15 CR（119）+ Q16 LU（165）+ Q17 QR（138）+ Q18 譜定理（144）+ Q19 SVD（174）+ 6 主章 callout（[ch06a](../book/ch06a-five.md) Q14+Q11+Q13 / [ch06b](../book/ch06b-CR.md) Q15+Q14 / [ch06c](../book/ch06c-LU.md) Q16+Q14 / [ch06d](../book/ch06d-QR.md) Q17 / [ch06e](../book/ch06e-QLQ.md) Q18+Q11+Q13 / [ch06f](../book/ch06f-USV.md) Q19+Q14+Q08+Q13 共 15 links）— **累計 12 callout / 28 Q&A links 全主章 100% 覆蓋** |
| ✅ S15 | **附錄 + 整合收尾：Q20–Q22 + 3 附錄 callout + BOOK.md 重生 + 規範補充** | [appendix-D-why.md](../book/appendix-D-why.md) 3522 行 / 22 Q&A 100% ✓ + 15 callout / 37 Q&A links + [BOOK.md](../book/BOOK.md) 12305 行（+42%）+ SCHEMA §3.6 + VIZ-CATALOG Appendix D 索引 + 0 broken anchor ✓ |
| ✅ S16 | **Marimo 技術棧 PoC — Python 視覺化實作起步**（commit `2f9b9e3`）| viz/ 7 檔（uv + Python 3.12 + marimo 0.23.6 + plotly 6.7 + matplotlib 3.10 + sklearn 1.8 + Pillow 12.2）+ hello.py（Stage 1 4 cell）+ ch01_mv1_poc.py（Stage 2 7 cell (Mv1)+(Mv2) 雙觀點互動）+ marimo export html-wasm dist/ch01_mv1_poc 27 MB static deploy（Stage 3 ✅）+ SOP §2.15 WASM 3 陷阱 + S17+ 5 條 checklist |
| ✅ S17 | **ch04 V-02 MM4 母模板架構階段 — 首批 Tier 3 旗艦開工骨架完成**（commit `cc957f1`）| viz/ch04_matrix_matrix.py 440 行 / 8 cell + viz/_common/{__init__.py, rank1_layer.py}；小矩陣 3×2·2×2 模式骨架 + r slider 0..2 + 秩 1 圖層 strip + 主舞台 2×3 共 6 heatmap + WASM export + console clean + 2 round debug；SOP §2.15 補 S17 3 個新 WASM 陷阱（合計 6 大）|
| **→ S18** | **ch04 V-02 圖像模式 + Mona Lisa SVD（VizScript-02 模式 2）** | 接 S17 骨架加：(1) 4 張 64×64 灰階圖像 npy 預計算（Mona Lisa / 條紋 / 漸層 / 隨機 / 預先 `numpy.linalg.svd(image, full_matrices=False)` cache 至 `viz/assets/`）(2) 模式 radio 切換（小矩陣 / 4 圖像，切換時整個畫面重建）(3) 圖像模式三張 64×64 並列（原圖 / 累加重建圖 / 誤差熱圖）+ 相對誤差數字 (4) r slider 範圍動態調整（小矩陣 0..2 / 圖像 0..64）(5) WASM export 確認 ~30 MB 內（4 npy ~33 KB 每張）+ console clean；預估 1 session |
| S19 | **ch04 V-02 Tier 3 補完（飛入動畫 + 重排序 + 誤差曲線 + Walkthrough）** | (1) r slider 移動時秩 1 圖層從 strip「飛到」主舞台中央 + 與 Cr 合併動畫 800ms / 項 + ease-in-out cubic-bezier (2) 4 重排序 radio（按 σ_p / ||a_p|| / 隨機 / 自訂）對比，按 σ_p 排序時誤差曲線下降最快 — 鋪陳 Eckart-Young §6.5 (3) 誤差曲線圖 r vs ||C-Cr||_F / ||C||_F 即時更新，當前 r 紅點 + 垂直虛線標記 (4) Walkthrough 6 步首次開啟自動觸發 (5) 快捷鍵 Space / ←/→ / R / 0 / Shift+End / M；預估 1-1.5 session |
| S20+ | Python 視覺化批次旗艦實作 | 從 VIZ-CATALOG 次批 Tier 2（含 Matrix World V-01 全書互動式教材首頁 + ch06a V-01 五分解 dashboard 等），預估 ~28-30 session |

### S18 起步建議（S17 已完成，圖像模式 + Mona Lisa SVD）

1. **S18 任務：ch04 V-02 圖像模式（VizScript-02 模式 2）** — 接 S17 骨架，加 64×64 灰階圖像 4 張預計算 SVD + 模式 radio 切換 + 三圖並列；預估 1 session

2. **S18 拆 5 步：**
   - **Step 1（~15 min）：** 準備 4 張 64×64 灰階圖像
     - `viz/assets/mona_lisa_64.npy` — 從公開 Mona Lisa 圖（PIL convert L + resize 64×64）
     - `viz/assets/stripes_64.npy` — 程式生成 horizontal stripes 圖案
     - `viz/assets/gradient_64.npy` — 程式生成 linear gradient 對角漸層
     - `viz/assets/random_64.npy` — `np.random.seed(42)` 後 randn 64×64
     - 每張 SVD 預計算 cache `U, sigma, Vt` 至 `viz/assets/{name}_svd.npz`（避免 WASM 啟動算 SVD 卡 ~1s）
   - **Step 2（~20 min）：** mode radio + 動態 r 範圍
     - mode = mo.ui.radio(options=["小矩陣 demo", "Mona Lisa", "條紋", "漸層", "隨機"], value="小矩陣 demo")
     - 切換 mode 時 r slider 範圍動態：小矩陣 [0, 2] / 圖像 [0, 64]
     - **注意：marimo `mo.ui.radio` 是 reactive，可在計算 cell closure 用 `mode.value` 分支**
   - **Step 3（~25 min）：** 圖像三圖並列主舞台改寫
     - 原 6 heatmap subplot 改為「依 mode 動態 layout」
     - 圖像模式：1×3 layout 顯示「原圖 / 累加重建圖 / 誤差熱圖」+ 64×64 灰階 `colorscale="Greys"` `aspect=1`
     - 小矩陣模式：保持 S17 的 2×3 layout
   - **Step 4（~10 min）：** 即時相對誤差數字 + 累積能量比例
     - 圖像模式顯示 `||C - Cr||_F / ||C||_F = 23.4%` 即時數字 + 「累積保留能量比例 = Σ σ_p² / Σ σ²（p ≤ r）」
     - 對於 Mona Lisa，r=10 時應 ~85%+ 能量、r=20 時應 ~95%+
   - **Step 5（~10 min）：** WASM export 驗證 + 部署測
     - `marimo export html-wasm` 確認 dist size ~30 MB 內（4 npy ~33 KB 每張 + 4 svd npz ~140 KB 每張）
     - console 必看：(a) `Loading from micropip: ['plotly']` (b) 無 STDERR (c) `np.load(...)` 對 npy 在 Pyodide 環境 work
     - **可能陷阱（待 S18 確認）：** WASM 環境如何讀本機 npy？可能需嵌入 base64 或用 fetch — 若 Pyodide `pyodide-http` 預裝可 fetch 同 dir 相對路徑

3. **S18 開工 checklist（SOP §2.15 6 大陷阱）：**
   - [ ] PEP 723 metadata 維持 marimo + numpy + plotly（圖像模式不需新增 dep）
   - [ ] 跨 cell 共用的函數 / 變數命名不可 `_` 開頭
   - [ ] plotly `subplot_titles` 不可傳空字串
   - [ ] heatmap helper 內 `M = np.asarray(M, dtype=float)` 保護
   - [ ] mode radio 切換時注意 r slider 範圍動態
   - [ ] WASM export 後 console 必看 STDERR + Loading 順序
   - [ ] **驗證 Pyodide 環境讀 viz/assets/*.npy 是否 work**（待 S18 確認 — 可能要改 base64 嵌入或 fetch）

4. **參考工件：**
   - [viz/ch04_matrix_matrix.py](../../viz/ch04_matrix_matrix.py) — S17 骨架（已 work，S18 直接擴）
   - [viz/_common/rank1_layer.py](../../viz/_common/rank1_layer.py) — 工具函數本機 reference（注意 WASM 仍要 inline）
   - [VizScript-02 in ch04-mat-mat.md](../book/ch04-mat-mat.md#vizscript-02) §C 模式 2 規格 + §D 視覺布局 + §K 技術實作建議 — 直接參照
   - [SOP_DRAFT.md §2.15](sop/SOP_DRAFT.md) — 6 大 WASM 陷阱

5. **S18 後續：** S19 補完 Tier 3（飛入動畫 / 4 重排序 / 誤差曲線 / Walkthrough / 快捷鍵）；S20+ 進入次批 Tier 2 旗艦（Matrix World V-01 + ch06a V-01 五分解 dashboard + ch06b/c/d/e V-01 五分解 pointer，依 S17 母模板複製樣板）

### S17 起步建議（S16 已完成，首批 Tier 3 旗艦實作）— 歷史保留

1. **S17 推薦選項 A：ch04 V-02 MM4 + Mona Lisa SVD 母模板**（[VizScript-02 in ch04-mat-mat.md](../book/ch04-mat-mat.md#vizscript-02)）— 母模板優勢，完成後 §6 五分解 pointer 全解鎖（ch06b/c/d V-01 全部 pointer / ch06a V-01 dashboard 控制器 / ch06f V-01 雙 pointer 主指向）；預估 3 session（架構 + 互動 + 應用 demo）

2. **S17 開工 checklist（SOP §2.15）**：
   - [ ] notebook 頂端寫 PEP 723 inline metadata block，列入所有非預設 dep（plotly / sklearn / Pillow）
   - [ ] 所有 plotly fig 用 `mo.ui.plotly(fig)` 顯式包裝；reactive cell 內 `mo` 加 closure args
   - [ ] WASM export 後 console 必看：(a) 載入順序中是否含目標套件 (b) 是否有 `ModuleNotFoundError` (c) 是否有 cell exception
   - [ ] 部署頁 README / 首頁加「30s 首次載入」說明
   - [ ] 沿用 SCHEMA §3.5 全書視覺錨點（配色 hex / cell 尺寸 / 動畫時間 / 3D 視角預設 `elevation=25° azimuth=-60°`）

3. **參考工件：**
   - [viz/ch01_mv1_poc.py](../../viz/ch01_mv1_poc.py) — S16 PoC 範本（2D plotly + reactive sliders 完整流程）
   - [viz/README.md](../../viz/README.md) — 技術棧上手 + Marimo vs 其他平台對照
   - [VIZ-CATALOG.md](../book/VIZ-CATALOG.md) — 首批 Tier 3 旗艦兩支
   - [ch04-mat-mat.md VizScript-02](../book/ch04-mat-mat.md#vizscript-02) — 母模板 13 段 A-M 完整劇本（直接餵 Claude 生 Python）
   - [SOP_DRAFT.md §2.15](sop/SOP_DRAFT.md) — Marimo WASM 3 大陷阱 + 5 條 checklist

4. **S17 後續可考慮並行**：S18+ 是「次批 Tier 2 全書互動式教材首頁」（Matrix World V-01 + ch06a V-01 五分解 dashboard），若 S17 母模板做順可考慮在 S17 收尾時起 PoC

### S15 起步建議（S14 已完成，背後觀念層收尾 + 整合）— 歷史保留

1. **S15 是「附錄 Q&A 收尾 + 整合 session」** — 預估 ~2h，沿用 S12-S14 已驗證的批量寫作流程 + S11 整合流程：

   **A. 附錄 Q&A 批量（~1h）：**
   - **Q20（特徵值的「地圖」為什麼能畫得出來？）** — Appendix A。① 史線：Cauchy 1829 主軸 + Sylvester 1852 慣性 → 12 類矩陣的特徵值幾何位置整理 / ② 12 類矩陣 × 特徵值位置完整表（對稱、正定、反對稱、酉、馬可夫等）+ 為什麼這些位置不重疊 / ③ 「特徵值幾何位置 = 矩陣家族 DNA」
   - **Q21（Matrix World 為什麼是「同心橢圓繼承樹」而非「樹狀」？）** — Appendix B。① 史線：Strang 在 LAFE 「Matrix World」設計史 + Bourbaki 結構主義數學影響 / ② 為什麼用同心橢圓（繼承關係）而非樹（分類關係）— Matrix → Square → Diagonalizable → Normal → Symmetric → ... → {I, O} 11 層 / ③ 「分類學 vs 繼承樹」設計哲學 + 偽反矩陣作為全矩陣統一公式的位置
   - **Q22（解 $A\mathbf{x}=\mathbf{b}$ 為什麼是線代的核心問題？）** — Appendix C。① 史線：《九章算術》→ Cramer 1750 → Gauss 1809 → 19-20 世紀 → 機器學習的反問題（線性回歸 = 解 Ax=b）/ ② 4 子空間整合視角：特解 + 零空間 + 仿射子空間 + 最小範數最優解 $\mathbf{x}^* = A^{+}\mathbf{b}$ — 從 SVD 構造完整結構 / ③ 「Ax=b 是把連續/離散問題化為矩陣問題的最低抽象介面」+ 為什麼線代是現代計算科學共同語言

   **B. 3 附錄 callout 客製化插入（~30 min）：**
   - [appendix-map-eigenvalues.md](../book/appendix-map-eigenvalues.md) — 連結 Q20 + Q18（譜定理）+ Q12（(P3) 動態系統）
   - [appendix-matrix-world.md](../book/appendix-matrix-world.md) — 連結 Q21 + Q14（為什麼分解）+ Q19（SVD 偽反矩陣）
   - [appendix-four-subspaces.md](../book/appendix-four-subspaces.md) — 連結 Q22 + Q08（4 子空間自然冒出）+ Q19（SVD 構造 4 基底）

   **C. 整合收尾（~30 min）：**
   - **BOOK.md 重新生成** — 8650 → ~9700 行（含 S12-S14 新增的 appendix-D-why.md 2740 行 + 12 主章 callout 增量 + 3 附錄 callout）；採 S11 確立的 fence-code-aware awk 降一級策略避開 Python code block 內 `#` 註解
   - **跨檔 anchor 校驗** — `grep -nE "\]\(appendix-D-why\.md#q[0-9]+\)" docs/book/*.md` 驗證 28+3 = 31+ 個 Q&A links 完整正確 + `grep -nE "\]\([a-zA-Z0-9_-]+\.md#" docs/book/*.md` 驗證跨檔 anchor 未破壞
   - **VIZ-CATALOG.md / SCHEMA.md / VIZ_SCHEMA.md** 補背後觀念層 cross-reference（如有必要）
   - **MEMORY.md 索引更新** — 加 S14 + S15 完成里程碑
   - **HANDOFF / SESSION_INDEX / SOP_DRAFT / RETROSPECTIVE 整批收尾**

2. **預估行數：** Q20-Q22 各 ~130-170 行 = ~450 行；3 附錄 callout 各 ~30-50 行 = ~120 行；appendix-D-why.md 預期擴至 ~3300 行 / 22/22 Q&A = 100%

3. **參考工件：**
   - [appendix-D-why.md](../book/appendix-D-why.md) — 已有 Q01-Q19 範本（19 條），S15 沿用同 schema
   - [ch06f-USV.md](../book/ch06f-USV.md) — S14 最複雜 callout 範本（4 Q&A links + Strang 名言鉤子）
   - [appendix-matrix-world.md](../book/appendix-matrix-world.md) — Tier 2 旗艦附錄範本（同心橢圓繼承樹 + 偽反矩陣公式）
   - [appendix-four-subspaces.md](../book/appendix-four-subspaces.md) — 已有「解 $A\mathbf{x}=\mathbf{b}$ 完整結構視覺」段（Q22 可直接 cross-link）
   - [SOP_DRAFT.md §2.13](sop/SOP_DRAFT.md) — 背後觀念 3-layer 框架規範 + 已含 S12-S14 5 條教訓累積

4. **S15 後續：** 背後觀念層階段完成（appendix-D-why.md 100%），下階段進入 Python 視覺化實作（S16+）— 從 [VIZ-CATALOG.md 首批](../book/VIZ-CATALOG.md) Tier 3 旗艦（ch04 V-02 母模板 / ch06f V-01 SVD Master）開始 PoC

### S14 起步建議（S13 已完成，背後觀念層續寫）— 歷史保留

S13 已完成 13/22 Q&A（59%），S14 路線重點：Q14-Q19 §6 五大分解 6 條 Q&A + ch06a-ch06f 6 主章 callout，預估 ~2.5h。**S14 實際完成耗時 ~3.5h**（比預估多 40%，因 §6 條目自身內容深度高 + 6 callout 設計需更多 cross-link）— 詳見 SOP §2.6 S14 耗時資料點 + §2.13 S14 教訓 5 條。

### S12+ 起步建議（S11 已完成，本段為下一階段路線）

1. **S12+ 「技術棧 PoC + 首批旗艦 PoC」session**（預估 ~3 session 技術棧 + 各 3 session 旗艦）：
   - **技術棧 PoC：** Marimo notebook + plotly 3D + matplotlib + scikit-learn + Pillow（圖像 / Mona Lisa demo）+ scipy（pinv / eig 等）—  跑通 hello world + 1 個簡單 widget
   - **首批 Tier 3 旗艦 PoC：** 從 [VIZ-CATALOG.md 首批](../book/VIZ-CATALOG.md#-首批--核心骨架旗艦2-個-tier-3-旗艦6-session) 挑：
     - **選項 A：** [ch04 V-02 MM4 + Mona Lisa](../book/ch04-mat-mat.md#vizscript-02) — 母模板，後續所有 §6 五分解都 pointer 到此
     - **選項 B：** [ch06f V-01 SVD Master](../book/ch06f-USV.md#vizscript-01) — 全書最強規格 + 4 應用切換 + 雙 pointer 設計
   - 推薦 A 先做（母模板優勢 + 完成後 §6 五分解 pointer 全部解鎖）

2. **依賴鏈考量：** ch04 V-02 完成後解鎖：ch06b/c/d V-01 全部 pointer / ch06a V-01 dashboard 控制器 / ch06f V-01（雙 pointer 主指向）

3. **參考工件：**
   - [BOOK.md](../book/BOOK.md) — 整本書離線閱讀版（8650 行）
   - [VIZ-CATALOG.md](../book/VIZ-CATALOG.md) — 入口 metadata 索引（**S12+ 開工每天用此檔挑題目**）
   - [SCHEMA.md §3.5](../book/SCHEMA.md#35-全書視覺錨點s11-規範化) — 全書視覺錨點規範（配色 / cell / 動畫 / 3D 視角）
   - [VIZ_SCHEMA.md §2.3](../book/VIZ_SCHEMA.md#23-全書視覺錨點-cross-references11-規範化) — VizScript 撰寫時的視覺錨點 cross-reference
   - [docs/dev/sop/SOP_DRAFT.md](sop/SOP_DRAFT.md) — 累積 11 個 session 寫作經驗 + S11 整合教訓

4. **Strang 8 本版權 PDF 已備齊：**（私人參考，不 push GitHub）
   - 寫互動式劇本時可引 Linear Algebra for Everyone Ch.7（SVD）/ Linear Algebra and Learning from Data Ch.1（Mona Lisa 原型）等補完數學推導與例題
   - md 內**可大段引用原文**（Back 明確授權，提升 md 完整性）— PDF 檔本身不 push 即可

### S11 起步建議（已完成，保留歷史）

1. **S11 是「整合 / 校對 / 統一 session」** — 預估 1.5h，主要工作不是新撰寫而是合併 + 校驗
2. **核心產出 1：`BOOK.md`** — 把 13 個 md 檔（ch01 + ch02 + ch03 + ch04 + ch05 + ch06a + ch06b + ch06c + ch06d + ch06e + ch06f + front-foreword + back-conclusion + 3 附錄）依正確順序合併為單一檔案：
   - **順序：** front-foreword.md → ch01–ch06f → back-conclusion.md → appendix-map-eigenvalues.md → appendix-matrix-world.md → appendix-four-subspaces.md
   - **整合動作：** 重新編號章節（1, 2, 3, 4, 5, 6, 6.1, 6.2, ..., 6.5, A, B, C）+ 統一目錄 + 統一 footer
3. **核心產出 2：`VIZ-CATALOG.md`** — 抽取全書 36 個 VizScript（33 主章 + 3 附錄）的索引：
   - 每個 VizScript 一行：標題 / Tier / 章節 / 預估實作 session 數 / S12+ 優先順序批次
   - **Tier 3 旗艦排在最前**：[ch04 V-02](../book/ch04-mat-mat.md#vizscript-02) MM4 Mona Lisa + [ch06f V-01](../book/ch06f-USV.md#vizscript-01) SVD Master
   - **Tier 2 旗艦：** [appendix-matrix-world V-01](../book/appendix-matrix-world.md#vizscript-01) 全書互動式教材首頁
   - **Tier 2 主章：** ~10 個
   - **Tier 1：** ~20 個
4. **跨檔 anchor link 校驗：** 全書有大量 markdown 內部連結（如 `[ch06f V-01](ch06f-USV.md#vizscript-01)`），需 grep + 驗證所有 anchor 是否實際存在：
   ```
   grep -nE "\]\([a-zA-Z0-9_-]+\.md#" docs/book/*.md
   ```
   每個目標檔案內 grep `#` 對應 anchor 是否實際生成。
5. **風格統一檢查：**
   - 術語一致性：所有「列 / 行」是否符合 A 派慣例（column = 列直立 / row = 行橫躺）
   - 配色 hex 統一：全書綠 `#2ca02c` / 粉紅 `#d62728` / 藍 `#1f77b4` / 紫 `#9467bd` / 橙 `#ff7f0e` / 金 `#FFD700` 是否一致
   - cell 尺寸 / 動畫時間 / 3D 視角等視覺錨點是否一致
6. **資料一致性校驗：**
   - 確認 VizScript 總數 36（不再是 23）
   - 確認每個章節「本章 VizMark 數」是否與實際 grep VizScript 結果吻合
   - 確認每個分解章「PNG `using XX` 標記」是否與最終地圖（CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4/3 附錄=無）一致
7. **`BOOK.md` 目錄結構建議：**
   ```
   # 目錄
   - Foreword（Strang 推薦序 + 三大主題）
   - §1 Viewing a Matrix - 4 Ways
   - §2 Vector × Vector - 2 Ways
   - §3 Matrix × Vector - 2 Ways（含 4-Subspaces）
   - §4 Matrix × Matrix - 4 Ways
   - §5 Practical Patterns（P1/P2/P1'/P2'/P3/P4）
   - §6 The Five Factorizations of a Matrix
     - §6 Overview
     - §6.1 A = CR
     - §6.2 A = LU
     - §6.3 A = QR
     - §6.4 S = QΛQᵀ
     - §6.5 A = UΣVᵀ
   - Conclusion & Acknowledgements + 全書 36 個 VizScript 總覽
   - Appendix A：Map of Eigenvalues
   - Appendix B：Matrix World（全書互動式索引地圖 — S12+ 首頁）
   - Appendix C：The Four Subspaces and the Solutions to Ax=b
   - References
   ```
8. **S12+ 從 S11 產出開始：** VIZ-CATALOG.md 直接決定 S12+ 實作優先序，第一批 = Tier 3 兩支旗艦（ch04 V-02 + ch06f V-01）共 6 session，完成後可宣稱「全書互動式教材核心骨架 80%」

### 工件清單（S11 起步前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式（A 派術語） |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段 A-M 格式（含 800 字範例） |
| `docs/book/_merged.md` | **S10 已更新**：章節進度追蹤（S10 標 [x]）+ 章節↔圖檔對映 + VizScript 總數 36 校正 + S10 完成里程碑表 |
| `docs/book/front-foreword.md` | **S10 成稿，散文章節 + 推薦序英中對照範本**（158 行，0 VizMark）|
| `docs/book/ch01-viewing-matrix.md` | **S02 成稿，A 派術語的參考範本**（單視角章節） |
| `docs/book/ch02-vec-vec.md` | **S03 成稿，對比 / 對偶結構章節範本** |
| `docs/book/ch03-mat-vec.md` | **S04 成稿，多 VizMark + 多圖章節範本 + 4-Subspaces 標誌圖**（S10 4 子空間附錄 pointer 目標）|
| `docs/book/ch04-mat-mat.md` | **S05 成稿，N-way 單圖章節範本 + VizScript-02 母模板（S09 SVD 雙 pointer 主 pointer 目標 + S10 4 子空間附錄 SVD 構造）** |
| `docs/book/ch05-patterns.md` | **S06 成稿，多獨立小圖章節範本 + 「Tier 1 + pointer」策略首例**（S10 EVD/SVD 附錄 副 pointer 目標）|
| `docs/book/ch06a-five.md` | **S07 成稿，§6 開門總覽範本**（短章節 + Tier1+pointer dashboard，**S10 Matrix World 附錄 Tier 2 旗艦的母模板放大版**）|
| `docs/book/ch06b-CR.md` | **S07 成稿，§6.x 分解主章節範本（雙 pointer + 對偶兩圖 + `using PX` 跨章標記）** |
| `docs/book/ch06c-LU.md` | **S08 成稿，分解主章節範本（單 pointer + `using MM4`）** |
| `docs/book/ch06d-QR.md` | **S08 成稿，分解主章節範本（單圖 + 3D 視覺 + `using P1`）** |
| `docs/book/ch06e-QLQ.md` | **S09 成稿，對稱譜分解章 + 橢球 3D + 單 pointer + `using P4`**（S10 Map of Eigenvalues 附錄 pointer 目標）|
| `docs/book/ch06f-USV.md` | **S09 成稿，全書最長章 + Tier 3 主 VizScript + 雙 pointer + `using P4`**（S10 Four Subspaces 附錄 V-03 pointer 目標 + S10 Matrix World 附錄底部偽反公式對應）|
| `docs/book/back-conclusion.md` | **S10 成稿，結論 + 全書 33 個主章 VizScript 總覽（S11 整合橋樑）+ 全書里程碑回顧** |
| `docs/book/appendix-map-eigenvalues.md` | **S10 成稿，12 類矩陣 × 特徵值幾何附錄**（⭐⭐ Tier 1 + pointer，與 §6.4 EVD 三層遞進連結）|
| `docs/book/appendix-matrix-world.md` | **S10 成稿，旗艦 Tier 2 — 11 層同心橢圓 + 全書互動式教材首頁設計** |
| `docs/book/appendix-four-subspaces.md` | **S10 成稿，4 子空間整合附錄 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構視覺**（S11 整合時驗證連結是否準確）|
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready，S10 確認附錄 3 張無 `using XX` 標記）|
| `docs/dev/sop/SOP_DRAFT.md` | **S10 已更新版本 0.11**：§2.6 補 S00–S10 共 11 個 session 各章寫作策略 + S10 補附錄整合模式 7 觀察 — **S11 直接沿用** |

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
| 2026-05-12 | **S04 確立「4-Subspaces 圖是全書視覺化最高 priority 之一（⭐⭐⭐ Tier 3）」** | Strang 兩塊大餅圖是線性代數核心定理的視覺載體 |
| 2026-05-12 | **S05 確立「N-way 單圖章節寫作模式」+ ⭐⭐⭐ 劇本可選 Tier 2 / Tier 3** | ch04 VizScript-02 (MM4 + Mona Lisa SVD demo) 寫成 Tier 3 — §6 SVD 視覺前置 |
| 2026-05-12 | **S05 確立「§4 (MM4) 是 §6 五大分解的視覺基石」** | 5 大分解都可用 (MM4) 展開成「秩 1 之和」 |
| 2026-05-12 | **S06 教訓：HANDOFF 章節描述漏 P4** | 起步前必須對著原書 PNG 重核 Pattern/Figure 數量 |
| 2026-05-12 | **S06 確立「Tier 1 + pointer」省篇幅策略** | ch05 VizScript-03 (P4) 採此策略，§6 5 大分解每章都可重用 |
| 2026-05-12 | **S06 確立「對偶 Pattern 用對偶總表呈現」** | 節省 ~40% 篇幅且閱讀時更易對照 |
| 2026-05-12 | **S07 確立「兩章 session 模式」（總覽短 + 主章長）** | §6 五大分解總覽單獨一個 session 太浪費 |
| 2026-05-12 | **S07 重大發現：原書 PNG `using PX` 標記是跨章連結官方鐵證** | CR1.png 標 `using P1`、CR2.png 標 `using P2` |
| 2026-05-12 | **S07 確立「雙 pointer VizScript 設計」** | ch06b VizScript-01 首例驗證可行 |
| 2026-05-12 | **S07 確立「對偶兩張圖（列視角 + 行視角）是 §6.1–§6.5 全書一致模式」** | CR1+CR2 對偶展示「列秩 = 行秩」 |
| 2026-05-12 | **S08 重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** | 跨章 pointer 不只連 ch05 (P1-P4)，也連 ch04 (MM1-MM4) |
| 2026-05-12 | **S08 確立「單 pointer 比雙 pointer 更常見」規律** | PNG 標什麼 `using XX`，VizScript 就指對應章 |
| 2026-05-12 | **S08 確立「分解章篇幅由『應用面廣度』決定」** | LU 含解 Ax=b、QR 含最小平方法、CR 含列秩=行秩證明 |
| 2026-05-12 | **S08 確立「3D 投影視覺是 QR 章獨有需求」** | 3D 渲染棧成 §6 必備 |
| 2026-05-12 | **S08 確立「主章 + 主章兩章 session 模式」** | 兩個獨立分解主章放同一 session 可行 |
| 2026-05-12 | **S09 重大發現：EVD 與 SVD PNG 都標 `using P4`** | §6.x 7 張主圖 `using XX` 最終地圖：CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4 |
| 2026-05-12 | **S09 確立「雙 pointer 復活判準」明文化** | 雙條件「PNG 標記重複 + 內容旗艦同根」雙成立才升級 |
| 2026-05-12 | **S09 確立「Tier 3 主 VizScript 首次出現在 §6」** | SVD VizScript-01 與 ch04 VizScript-02 並列「核心骨架雙旗艦」|
| 2026-05-12 | **S09 確立「§6 主章序列篇幅比例 1.0:1.20:0.99:1.28:1.71，SVD 為集大成終章」** | SVD 章 934 行為平均章節 1.6 倍 |
| 2026-05-12 | **S09 確立「§6 章節雙 pointer 設計地圖規律」** | 對偶兩張圖（CR）+ 集大成章（SVD）採雙 pointer |
| 2026-05-12 | **S10 重大發現：3 張附錄 PNG（MapofEigenvalues / MatrixWorld / 4-Subspaces）皆無 `using XX` 標記** | 附錄 PNG 是「**地圖層級 / 基本概念圖**」非 Pattern 套用層級，標記譜系與主章 §6.x 不同 |
| 2026-05-12 | **S10 確立「附錄重整合 vs 主章重教學」雙模式** | 附錄 3 個 VizMark 都採「pointer 到主章 VizScript」策略，不重複實作（map → ch06e、4-subspaces → ch03 V-02 + ch06f V-03、Matrix World 跨全書索引）|
| 2026-05-12 | **S10 確立「Matrix World 互動式索引地圖首次升級為 Tier 2 旗艦」** | appendix-matrix-world V-01 設計為「**S12+ 全書互動式教材的首頁**」（讀者進入教材的標準入口），與 ch06a V-01 五分解 dashboard 互補（前者分類學索引、後者分解視覺索引）|
| 2026-05-12 | **S10 確立「全書 33 個 VizScript 總覽段是 S11 整合的橋樑」** | back-conclusion.md 新增此段（原書無）讓 S11 BOOK.md / VIZ-CATALOG.md 整合直接抽取，省 0.5 session 額外整理 |
| 2026-05-12 | **S10 校正「HANDOFF 累積錯誤 — VizScript 數從 23 校為 36」** | 前 session 累積寫 23 是漏算 ch03/ch04/ch05 各 4 = 12 個；S11 整合時 grep 校驗為共識統計值的標準步驟 |
| 2026-05-12 | **S10 確立「四子空間附錄新增『解 $A\mathbf{x}=\mathbf{b}$ 完整解空間結構視覺』」** | 與 [appendix-matrix-world.md](../book/appendix-matrix-world.md) 底部偽反公式 $A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ 對應，把「解方程」完整結構（特解 + 零空間 + 仿射子空間 + 最小範數最優解）整合進附錄；§6.5 SVD 章未深入此面 |
| 2026-05-13 | **S11 確立「broken anchor 修復方案 B：重指 VizScript 級 anchor」** | 附錄本來就是「重整合 → pointer 到主章 VizScript」設計，9 處 broken `#N` 短 anchor 改指 `#vizscript-01/03` 比指 `§N` 段落更符合附錄哲學 |
| 2026-05-13 | **S11 確立「BOOK.md vs VIZ-CATALOG.md 雙檔組合最有效」** | BOOK.md = 整本書下載/離線閱讀（8650 行）；VIZ-CATALOG.md = 入口 metadata 索引（241 行純連結 + 7 欄位）— 兩個不是替代而是補充，S12+ 開工先看 catalog 挑題再跳原章節讀 13 段 A-M 劇本 |
| 2026-05-13 | **S11 確立「fence-code-aware awk 降一級策略」** | sed `g/^#/##/` 第一輪會誤把 ch06e Python code block 內「# 參數化單位球」「# plotly Surface 渲染」等註解改為 ## heading；改用 awk + ``` fence 追蹤狀態解 — 未來 BOOK.md 重新生成都用此邏輯 |
| 2026-05-13 | **S11 確立「全書 3D 視角預設規範 elevation=25° azimuth=-60°」** | 全書 109 次 3D 提及但 S11 前只 1 處明確聲明（ch03 V-02）；補規範後 ch06d/06e/06f/App C 等 3D VizScript 有共同錨點，S12+ 實作渲染風格一致 |
| 2026-05-13 | **S11 確立「動畫時間 / px 寫法強制統一無空格 `Xms` / `AAxBB px`」** | 全書 X ms (16) vs Xms (38) 不一致，sed 統一為無空格 ms；px 統一中間 × 兩側無空格、px 前 1 空格；macOS BSD sed 不支援 `\b` word boundary 需注意 |
| 2026-05-13 | **S11 確立「Strang 版權 PDF 兩層級分開處理」** | PDF 檔本身絕對不 push GitHub（.gitignore pattern + 5 白名單反白）；md 檔內可大段引用原文（Back 明確授權「重點是 md 完整性」）— S12+ 撰寫補充章節可直接引 Strang 原始定義/例題 |
| 2026-05-13 | **S11 確立「back-conclusion.md Tier 統計表是 VIZ-CATALOG.md 的單一真相來源」** | S11 把 conclusion 表從「主章 33 個」校為「全書 36 個」+ 加入 Matrix World Tier 2 旗艦 + ch06a 改 Tier 1+pointer + 附錄 3 個列入 — VIZ-CATALOG.md 直接引此表為統計基礎 |
| 2026-05-13 | **S12 啟動「背後觀念層」開發階段** | Back 發現全書缺一個系統性「為什麼這條規則長這樣」維度（13 個主章只講「怎麼算」缺「為什麼這樣算」）— 用 Cayley 1858 矩陣乘法為什麼是「列乘行」的 Q&A 範例（變數連續代換還原 + Cayley 原文初心 + 高階語言）展示完整 3-layer 模板 |
| 2026-05-13 | **S12 確立「3-layer 框架」（① 歷史 + ② 設計過程還原 + ③ 概念昇華）** | 每條 Q&A 採固定 3-layer 結構（含經典出處引用 + 完整推導 + 小例題 + 1 句昇華）；3-layer 不全有時 ① / ② 可彈性略過但 ③ 必有；自驗檢查「為什麼這條規則長這樣？讀者讀完知道嗎？」答不出就補 callout |
| 2026-05-13 | **S12 確立「方案 D 雙層落點」** | 主章 callout（▶ 💡 背後觀念 ◀ 短摘要 ~200 字 + 連結附錄 D）+ 全書集中附錄 D Q&A（~600-2000 字詳盡版 3-layer + 例題 + 推導 + Strang 經典引用）；callout 不複製內容只給 hook + cross-ref，避免重複 |
| 2026-05-13 | **S12 確立「22 條 Q&A 全書清單 + 4-session 路線」** | S12（Foreword + §1 + §2 + §3 = 9 Q&A）→ S13（§4 + §5 = 5 Q&A）→ S14（§6 五大分解 = 6 Q&A）→ S15（附錄 + 整合收尾 = 3 Q&A + BOOK.md 重新生成）；總 22 條 = 21 必要 + 1 可選（Q21 Matrix World 為什麼同心橢圓） |
| 2026-05-13 | **S12 確立「Q09 PoC → 風格鎖定 → 批量寫」流程** | 先草擬 Q09（最關鍵的矩陣乘法為什麼列乘行）給 Back review 確認風格 OK → 直接批量寫 Q01-Q08 8 條；避免清單批量寫完才發現方向不對 — PoC 投入 ~30 min 換來批量寫 ~2h 風格一致 |
| 2026-05-13 | **S12 確立「主章 callout 統一落點：章節摘要末 / 數學要點前」** | callout 放在「術語提醒 ⚠」之後、`---`「數學要點」段之前 — 讀者讀完章節摘要、進入正式內容前先看到動機指引，不打斷主章節奏；每章 callout 對應 1-3 條 Q&A 的列表式短摘要 + 直接連結附錄 |
| 2026-05-13 | **S12 確立「Q&A 內容詳盡度標準：詳盡優先 + 經典引用」** | 篇幅約 1000-2500 字含舉例 + 推導 + 經典出處（《九章算術》原文、Cayley 1858 原論文題名 + 期刊頁碼、Strang LAFE / ILA / LAaLD 章節 + 原話引用、Grassmann 1844 / Gibbs 1881 等）；Q&A 之間大量 cross-link 形成知識網路（Q06 ↔ Q07 ↔ Q08 / Q04 ↔ Q05 / Q01 ↔ Q09 ↔ Q19） |
| 2026-05-13 | **S13 確立「Q&A 批量寫作模式可不再 PoC 直接批量」** | S12 已用 Q09 PoC 鎖定風格，S13 直接批量 Q10-Q13 無中途 review；4 條 Q&A 平均寫作時間 ~25 min / 條（含搜尋史線 + 公式 + 例題），比 S12 Q01-Q08 批量平均 ~12 min / 條長 — **因為 §4 + §5 條目自身內容更深（需含 2×2 完整驗算 + (P3)↔(P4) 對偶表 + 4×4 穩定性分類表等），不是流程效率退步**。**未來 S14 §6 五大分解預期每條 ~150 行（含分解定理證明 + 矩陣分解步驟 + (P4) 連結）將更長** |
| 2026-05-13 | **S13 確立「Q&A 篇幅彈性：簡單章 ~95 行 / 深章 ~160 行」** | Q10 為四層理由清單型 95 行，Q11 為超能力對照表型 111 行，Q12 為三步走 + Fibonacci 例題 121 行，Q13 為「世紀大夢」連 §6 五大分解集大成型 156 行 — 篇幅由「動機問題的深度」而非「機械字數要求」決定。**SOP §2.13 改為「篇幅 1000-2500 字」彈性範圍，不再固定 ~108 行平均值** |
| 2026-05-13 | **S13 確立「主章 callout 客製化 hook 設計：每條 Q&A 對應一個獨特 hook 詞」** | ch04 callout 用「行乘列來源 + 不可交換本質」雙 hook、ch05 callout 用「對角矩陣超能力 + (P3) DNA + (P4) 世界觀」三 hook — 每個 hook 是該 Q&A 的「最具體最有畫面感」的關鍵詞，讓讀者一眼判斷要不要點進附錄 D；boilerplate「為什麼這條規則長這樣」泛論寫法被棄用 |
| 2026-05-13 | **S13 確立「Q&A 跨章 cross-link 知識網路擴張」** | Q10↔Q13（不可交換 ↔ 同時對角化的可交換條件）+ Q11↔Q12↔Q13（對角矩陣 ↔ (P3) 動態 ↔ (P4) 三明治三角）+ Q12↔Q18（特徵向量正交為「乾淨穩定性分析設定」）— 加上 S12 已建立的 Q06↔Q07↔Q08 / Q04↔Q05 三角，全書 Q&A 形成密集知識網路；Q14-Q19 預計再添 6 條 cross-link |
| 2026-05-13 | **S14 確立「跳順序分批指令」工作模式** | Back 把 6 條 §6 分成 4 批指令（Q14 / Q15+Q17+Q18 / Q16+Q19 / 6 callout），跳過 Q16 先做 Q17+Q18 完全可行 — Edit 插入定位準確時檔案最終仍按 Q14-Q19 數字順序排列。**經驗：分批降低 context 疲勞 + 跳順序不破壞檔案排列**；未來 S15 可彈性決定 Q20-Q22 順序 |
| 2026-05-13 | **S14 確立「小例題刻意串接 cross-Q 教學鏈」設計** | Q19 SVD 3×2 小例題刻意用與 Q17 同個 $A$ + $A^{\mathrm{T}}A$ 正好是 Q18 同個 $2 \times 2$ 矩陣 — 形成「Q17 QR → Q18 EVD → Q19 SVD」完整教學鏈。讀者讀過前面 Q&A 後讀 Q19 自動感受到「同一矩陣三視角疊加」。**未來附錄 Q20-Q22 可考慮類似手法**（如 Q22 解 $A\mathbf{x}=\mathbf{b}$ 用 Q15 同 CR 範例） |
| 2026-05-13 | **S14 確立「§6 callout 平均 link 數比 §1-§5 高 15%」自然現象** | §1-§5 6 callout / 13 links（平均 2.17）vs §6 6 callout / 15 links（平均 2.5） — §6 分解章節因為「統合 §1-§5 多概念」自然需要更多 cross-link；ch06a 連 Q14+Q11+Q13、ch06e 連 Q18+Q11+Q13、ch06f 連 Q19+Q14+Q08+Q13。**S15 附錄 callout 預期同樣會多 link 數**（因為附錄本質是「重整合」非「重教學」） |
| 2026-05-13 | **S14 確立「Strang LAFE 名言當 callout 鉤子」設計** | ch06a callout 用「**Make every matrix look diagonal**」（LAFE §6.1 開頭）、ch06f callout 用「**the most important theorem in linear algebra**」（LAFE Ch.7 結論）— 直接用大師直引名言當 hook，比泛論寫法吸引力強得多。**未來 callout 應主動挖經典名言作為 hook 詞**（Back 提供的 8 本 Strang PDF 中還有更多名言可挖） |
| 2026-05-13 | **S14 確立「雙證明路徑對 §6 存在性 Q&A 高價值」設計** | Q19 SVD 雙證明（譜定理建構性 + Jordan 變分定義）讓讀者從兩個獨立角度確認「為什麼存在」 — 一個給代數證明、一個給幾何直覺。Q18 也用雙證明（不同特徵值正交 + 實特徵值補充）。**§6 分解 Q&A 的「存在性 / 構造性問題」幾乎都適用雙證明設計**，S15 Q22 解 $A\mathbf{x}=\mathbf{b}$ 也可考慮類似（從 4 子空間整合 + 從應用角度涵蓋） |
| 2026-05-13 | **S16 確立「Marimo + WASM」作為 app 式書籍最終技術棧** | 載體討論比較 Immersive Math（MathBox.js 三人團隊維運高）/ Seeing Theory（D3.js）/ Distill（解散）/ 3B1B（觀看非互動）/ Book of Shaders / D2L.ai（jupyter book）vs Marimo + WASM 後，選 Marimo 理由：(1) reactive Python 原生（不需自造 framework）(2) `marimo export html-wasm` 靜態頁解維運難題（Distill 教訓）(3) Python 技術棧零阻抗（plotly+sklearn+Pillow 全可用）(4) 最像 Immersive Math 但 Python 化、一人可撐起來；唯一 tradeoff = Pyodide 首次載入 ~30s，30 分鐘閱讀的書這成本可接受 |
| 2026-05-13 | **S16 確立「PEP 723 inline script metadata 是 marimo WASM dep 唯一聲明處」** | 本機 `uv add plotly` 只裝 .venv/，export html-wasm 預設只讓 Pyodide 載 Pygments+docutils+jedi+numpy+parso+pyodide-http，**plotly / sklearn / Pillow 都不會自動裝**。必須在 notebook 頂端加 `# /// script ... dependencies = [...] ///` block，marimo export 解析後嵌入 HTML 的 requirements 陣列；S17+ 旗艦開工 checklist 第 1 項 |
| 2026-05-13 | **S16 確立「plotly fig 用 mo.ui.plotly(fig) 顯式包裝」** | 本機 marimo edit 跑 bare `fig` 透過 `_repr_mimebundle_` 自動顯示，但 WASM 環境某些情況沉默不渲染（畫面空白、console 沒錯）；改用 `mo.ui.plotly(fig)` 顯式包裝 + cell 加 `mo` 到 closure args 後 work；S17+ 一律使用，未來 matplotlib 同理（待 S17 驗證） |
| 2026-05-13 | **S16 確立「WASM 首次載入 30-60s UX 警告規範」** | Pyodide + plotly wheel + plotly.js bundle 三層下載，讀者一眼空白容易誤判（S16 Back 就誤判過一次）；部署頁 / VIZ-CATALOG / BOOK.md 在連結 deployed page 處要附「⏳ 首次載入請等 ~30s，直到看到 plotly 圖出現再操作」說明 |
| 2026-05-13 | **S16 確立「WASM debug 流程：先看 console 再修代碼，不要先猜」** | Round 1 我猜了 3 個風險（LaTeX label / slider 嵌 markdown / plotly 新特性）防禦性重寫但都不是真因，浪費 1 round + 30 min；Round 2 Back 貼 console 立刻看到 `ModuleNotFoundError: No module named 'plotly'`真因。**教訓：WASM debug 先看 DevTools Console 比猜更高效**；未來 PoC 第一輪錯就主動要求 console log |
| 2026-05-13 | **S16 確立「uv + Python 3.12 + Marimo 0.23 + plotly 6.7 全棧穩定」** | viz/pyproject.toml lock 完整技術棧：marimo>=0.23.6 + matplotlib>=3.10.9 + numpy>=2.4.4 + pillow>=12.2.0 + plotly>=6.7.0 + scikit-learn>=1.8.0；本機 + WASM 雙環境驗證 OK；S17+ 旗艦實作可直接從此 lock 啟動 |
| 2026-05-14 | **S17 確立「跨 cell 共用的函數 / 變數命名不可 `_` 開頭」** | marimo 把 `_` 開頭 cell variable 視為 cell-private 不跨 cell export；S17 我寫 helper cell `return _accumulate, _layer_energy, _layers_of`，下游 cell 引用全部 NameError，整個 cell **沉默不渲染**（沒有 STDERR exception，只是「未渲染」）。**症狀：WASM 部分 cell 不見、console clean** — 是 marimo cell-graph 解析問題不是 runtime exception。**規則：S18+ 跨 cell helper 命名一律具名前綴（`acc_xxx` / `rank1_xxx` / `helper_xxx` 等），不可 `_xxx`**；補進 SOP §2.15 陷阱 #4 |
| 2026-05-14 | **S17 確立「marimo helper 函數預設內聯在唯一使用者 cell」** | S17 寫 helper cell 結果只 1 個下游 cell 使用，「分 cell」沒帶來重用價值卻多了一個跨 cell 邊界（多 1 個 `_` 陷阱風險 + 多 1 個 dependency 邊界）。**規則：helper 函數預設先內聯在唯一使用者 cell，等真有第 2 個使用者再抽出來**；S18+ 圖像 SVD helper 也照此辦理 |
| 2026-05-14 | **S17 確立「plotly heatmap helper 防護模式」** | helper 函數開頭一律 `M = np.asarray(M, dtype=float)` 保護輸入，不假設 caller 一定傳 numpy；同步 `abs()` → `np.abs()` 用 numpy 介面而非 Python builtin；補進 SOP §2.15 陷阱 #6 |
| 2026-05-14 | **S17 確立「plotly `subplot_titles` 不可傳空字串」** | plotly 對 `subplot_titles=[""] * k` 空字串會直接跳過不生成 annotation slot，後置 `fig.layout.annotations[p].text = ...` 會 IndexError；變通：直接在 `make_subplots` 傳完整最終 title（推薦）或 placeholder 非空字串 `[" "] * k`；補進 SOP §2.15 陷阱 #5 |
| 2026-05-14 | **S17 確立「ch04 V-02 母模板 3 session 拆解節奏：架構 / 圖像 / Tier 3 補完」** | HANDOFF S16 預估 3 session，S17 把 scope 鎖在「最小可動骨架」（小矩陣模式 + r slider + 秩 1 圖層 strip + 6 heatmap）並守住，沒把圖像 / 動畫 / 重排序硬塞進來；S18 加圖像模式 + Mona Lisa SVD；S19 補完飛入動畫 + 4 重排序 + 誤差曲線 + Walkthrough + 快捷鍵。**3 session 拆解的最大好處 = 每 session 都能 commit 一個「可動 + console clean」的版本**，避免一次堆太多功能 debug 變多面 |
| 2026-05-14 | **S17 確立「WASM 部分 cell 不渲染但 console clean = marimo cell-graph 解析問題」** | 與 S16「Round 1 防禦性重寫」教訓 + S17 「`_` 前綴 cell-private」兩條經驗合併，WASM debug 流程升級：**第一動作不是 console 而是 (1) `python -c "import ast; ast.parse(open('xxx.py').read())"` 看 syntax (2) marimo edit 在本機跑 (3) 檢查 `_` 前綴 / cross-cell variable 拼錯字 (4) 才看 console**；console STDERR 是 runtime exception 階段才出現，cell-graph 解析失敗的 cell 是沉默 skip 不是 exception |

---

## 檔案變更追蹤

### S00 / S01 / S01.5 / S02–S09 詳見 SESSION_INDEX.md

簡述：S00 初始化、S01 機械轉換 + Schema、S02–S09 撰寫 9 個主章節 md 檔（ch01–ch06f 共 6824 行 + 33 個主章 VizScript）。

### S10 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/front-foreword.md | 新增 | **序言 158 行，0 VizMark** — Strang 推薦序英中對照 + 三大主題導讀 + 1920-2026 緣起 + 路線 A/B/C 三條閱讀路線 |
| docs/book/back-conclusion.md | 新增 | **結論 198 行，0 VizMark** — Hiranabe 結論英中對照 + **全書 33 個 VizScript 總覽表（S11 整合橋樑）+ Tier 分佈統計 + S12+ 實作優先順序三批排程 + 全書 S00–S10 里程碑回顧 + 5 個參考文獻 + 致謝**|
| docs/book/appendix-map-eigenvalues.md | 新增 | **附錄 A 272 行，⭐⭐ Tier 1 + pointer 指 ch06e EVD** — 12 類矩陣 × 特徵值幾何位置完整表 + 對應 §6.4 EVD 三層遞進關係 + 與 (P4) 三明治連結 + 12 格 dashboard 互動劇本 13 段 A-M |
| docs/book/appendix-matrix-world.md | 新增 | **附錄 B 328 行，⭐⭐⭐ Tier 2 旗艦 — S12+ 全書互動式教材首頁** — 11 層同心橢圓繼承樹（Matrix → Square → Diagonalizable → Normal → Symmetric → ... → {I, O}）+ 偽反矩陣全矩陣統一公式 $A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ + 兩條軸線設計（縱深特殊性 ⊥ 橫向對稱性）+ 13 段 A-M 完整 dashboard 劇本（含 3 模式切換 + 章節過濾器 + 範例矩陣辨認）|
| docs/book/appendix-four-subspaces.md | 新增 | **附錄 C 334 行，⭐⭐ Tier 1 + pointer 指 ch03 V-02 + ch06f V-03** — Strang 正交分解定理 + SVD 構造 4 子空間標準正交基底 + **新增「解 $A\mathbf{x}=\mathbf{b}$ 完整解空間結構視覺」** 段：特解 + 零空間平移仿射子空間 + 最小範數最優解 $\mathbf{x}^* = A^{+}\mathbf{b}$ + 整合 §3 + §6.5 + Matrix World 三章 |
| docs/book/_merged.md | 修改 | S10 標 [x]，VizMark 計數「3 附錄合計 ⭐⭐⭐ × 1 + ⭐⭐ × 2 + ⭐ × 0」（含 Matrix World 旗艦 Tier 2）+ §S10 附錄 PNG 重核發現新規律（3 張附錄 PNG 皆無 `using XX` 標記）+ 新增 S10 完成里程碑表（13 個 md 檔 / ~8100 行 / 36 個 VizScript / 2 Tier 3 旗艦 + 1 Tier 3 候選 + 1 Tier 2 旗艦地圖 / `using XX` 完整地圖）|
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.6 補 S10 耗時資料點（~2.5h / 1290 行 / 5 個檔案 / 3 VizMark = 1 Tier 2 旗艦 + 2 Tier 1）+ 7 觀察（附錄 PNG 無標記新規律 / 附錄重整合 vs 主章重教學雙模式 / Matrix World Tier 2 旗艦首次出現 / Conclusion 33 VizScript 總覽段是 S11 橋樑 / HANDOFF 累積錯誤校正 23→36 / 散文章節耗時規律 / 附錄章節耗時規律）+ 版本記錄追加 0.11 |
| docs/dev/CURRENT_SESSION.log | 修改 | S10 啟動 + 即時記錄 + 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S10 一行 |

### S11 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/BOOK.md | 新增 | **8650 行全書合併單檔** — 16 個 md 依序串接（front-foreword → ch01–ch06f → back-conclusion → 3 附錄）+ root heading + 全書目錄 + Tier 統計表 + using XX 標記地圖 + §6 篇幅比例 + S11 新增「全書視覺錨點」段；採 fence-code-aware awk 降一級避開 Python code block 內 `#` 註解 |
| docs/book/VIZ-CATALOG.md | 新增 | **241 行純 metadata 索引** — 36 個 VizScript 三批排程（首批 2 + 次批 9 + 末批 A 7 + B 3 + C 15）+ 全章節順序總覽 + 跨章 pointer ASCII 連動圖 + 進度追蹤（⏳/🔨/✅/⚠️/🔄 五狀態）+ 每行 7 欄位 metadata（連結 + Tier + 批次 + 估時 + 互動類型 + 數學基底 + 跨章 pointer + 狀態）|
| docs/book/SCHEMA.md | 修改 | 新增 §3.5「全書視覺錨點」段（4 子節：3.5.1 配色 6 主色 hex+RGB+輔助色階兩變形+灰階補助 / 3.5.2 cell 像素尺寸規範 / 3.5.3 動畫時間錨點 + 無空格寫法 / 3.5.4 **3D 視角預設 elevation=25° azimuth=-60°**）+ 版本記錄追加 0.2 |
| docs/book/VIZ_SCHEMA.md | 修改 | §2.2 寫作要點 3/4 補 SCHEMA.md §3.5 cross-reference + 新增 §2.3「全書視覺錨點 cross-reference」對照表（4 項）+ 版本記錄追加 0.2 |
| docs/book/back-conclusion.md | 修改 | Tier 統計表 6 處校正（總數 33→36、Matrix World V-01 補入 Tier 2 旗艦獨立分類、ch06a V-01 從 Tier 2 改 Tier 1+pointer、附錄 3 個列入、Tier 2 從~10 改 14 主章+1 旗艦、Tier 1 拆 Tier 1+pointer 3 個與 Tier 1 精簡 15 個）+ S12+ 三批排程連動修正 + root heading「33→36」修正 |
| docs/book/appendix-matrix-world.md | 修改 | 3 處 broken `#N` anchor → `#vizscript-01/03`（方案 B）：`#6`→V-01、`#64`→V-01、`#2`→V-03 |
| docs/book/appendix-four-subspaces.md | 修改 | 6 處 broken `#N` anchor → `#vizscript-01/03`（方案 B）：4 個 `#4`→V-03 / `#64`→V-01 / `#7`→拿掉 anchor（無對應 VizScript）|
| docs/book/appendix-map-eigenvalues.md | 修改 | sed 修 X ms→Xms 空格不一致（與其他附錄一起批次處理）|
| .gitignore | 修改 | 新增 `docs/book/*.pdf` pattern + 5 個白名單反白（The-Art-of-Linear-Algebra*.pdf / MapofEigenvalues.pdf / MatrixWorld.pdf）防 8 本 Strang 版權 PDF 誤 push |
| docs/dev/sop/SOP_DRAFT.md | （pending）| S11 整合 + 風格統一教訓待補（session-end Step 5b 處理）|
| docs/dev/CURRENT_SESSION.log | 修改 | S11 啟動 + 即時記錄（含 5 項任務逐步完成）+ 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S11 一行 |
| docs/dev/RETROSPECTIVE.md | 修改 | S11 對話反思追加（session-end Step 6 處理）|
| ~/.claude/projects/.../memory/feedback_private_pdfs.md | 新增（memory）| Strang 8 本版權 PDF 兩層級處理規範（PDF 不 push / md 內可大段引用原文，Back 授權）|
| ~/.claude/projects/.../memory/MEMORY.md | 修改（memory）| 補一行 index 指向 feedback_private_pdfs.md |

### S12 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/appendix-D-why.md | **新增** | **1175 行 / 67.7 KB / 9 Q&A（9/22 = 41%）** — 全書背後觀念 Q&A 附錄；含 root + 簡介 + 3-layer 框架說明 + 22 條目錄表（含 [Q](#) 錨點連結 + 狀態追蹤） + 術語提醒 + Q01-Q09 完整內容 + 末尾 S13-S15 路線 + 時間戳 |
| docs/book/front-foreword.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q01 圖解優先 + Strang 50 年反思 + 5 階學習階梯）+ **順手修「23 個 VizScript」→「36 個 VizScript（主章 33 + 附錄 3）」舊數字 bug**（S10 校正後遺漏的不一致）|
| docs/book/ch01-viewing-matrix.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q02 矩陣物件化躍進 + Q03 4 視角設計原則，含「三角形面積公式類比」hook）|
| docs/book/ch02-vec-vec.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q04 點積三動機殊途同歸 + Q05 外積秩 1 原子，含「秩 1 是線代原子」hook）|
| docs/book/ch03-mat-vec.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q06 $A\mathbf{x}$ 定義浮現 + Q07 2 視角必要性 + Q08 4 子空間自然冒出，含「2 方向 × 2 概念 = 4 不可避免」hook + Strang「線性代數的地理」原話）|
| docs/dev/sop/SOP_DRAFT.md | 修改 | （pending — session-end Step 5b 處理）S12 補 §2.13「背後觀念 3-layer 框架」+ §2.6 補 S12 耗時資料點 + 版本記錄 0.13 |
| docs/dev/CURRENT_SESSION.log | 修改 | S12 啟動 + 即時記錄（含 Back 拍板過程 + Q09 PoC + Q01-Q08 批量 + 4 callout）+ 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S12 一行 |
| docs/dev/HANDOFF.md | 修改 | 整檔覆寫（最後更新 / 已完成 / 進行中 / 待辦 → S13 / 關鍵決策追加 7 條 / 檔案變更追蹤追加 S12 區 / 技術筆記追加 S12 / 新 Session 指令更新到 S13）|
| docs/dev/RETROSPECTIVE.md | 修改 | （pending — session-end Step 6 處理）S12 對話反思追加 |
| ~/.claude/projects/.../memory/feedback_why_layer.md | **新增（memory）** | **全書每個運算規則需附「背後觀念」3-layer 規範**（① 歷史 / ② 設計過程還原 / ③ 概念昇華 + 落點方案 D + 篇幅指南 + 觸發時機 + 自驗檢查）|
| ~/.claude/projects/.../memory/MEMORY.md | 修改（memory）| 補一行 index 指向 feedback_why_layer.md |

### S13 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/appendix-D-why.md | 修改 | **從 1175 行擴至 1657 行（+482 行 / 36% 增量）/ 13 Q&A（13/22 = 59%）** — 新增 Q10-Q13 共 4 條 Q&A：Q10 為什麼乘法不可交換 AB≠BA（95 行）+ Q11 對角矩陣為什麼這麼特別（111 行）+ Q12 (P3) 動態系統為什麼能用特徵值預測長期（121 行）+ Q13 (P4) 三明治為什麼線代核心（156 行）；目錄表 Q10-Q13 4 條從「🚧 規劃中」→「✅ 已完成（S13）」+ 加錨點連結；尾段「其餘 13 條」改「其餘 9 條（Q14-Q22）」+ 改 S14-S15 路線；附錄末時間戳更新 S13 / 13/22 / 59% |
| docs/book/ch04-mat-mat.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q09 矩陣乘法行乘列來源 + Q10 不可交換本質，2 Q&A links，~300 字 hook 含 Cayley 1858 設計初心 + (MM4) 視角強調 + 函數合成不可交換類比） |
| docs/book/ch05-patterns.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q11 對角矩陣超能力 + Q12 (P3) 動態預測 + Q13 (P4) 三明治世界觀，3 Q&A links，~400 字 hook 含「對角矩陣承載按 index 加權的本質」共同主題 + Fibonacci 黃金比例例子 + 「世紀大夢」昇華 + 100 年史 4 人累積）+ 1 處 typo「appendix-D-view」→「appendix-D-why.md」即時修正 |
| docs/dev/sop/SOP_DRAFT.md | 修改 | （pending — session-end Step 5b 處理）S13 補 §2.6 耗時資料點（~2h / 482 行 / 4 Q&A + 2 callout）+ 版本記錄 0.14 + S13 觀察（PoC 後可直接批量、Q&A 篇幅由動機深度決定、callout hook 客製化、Q&A 跨章 cross-link 網路） |
| docs/dev/CURRENT_SESSION.log | 修改 | S13 啟動 + 即時記錄（4 條 Q&A metadata + 2 callout 插入 + typo 修）+ 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S13 一行 |
| docs/dev/HANDOFF.md | 修改 | 整檔覆寫（最後更新 / 已完成 / 進行中 / 待辦 → S14 / 關鍵決策追加 5 條 / 檔案變更追蹤追加 S13 區 / 技術筆記追加 S13 / 新 Session 指令更新到 S14）|
| docs/dev/RETROSPECTIVE.md | 修改 | （pending — session-end Step 6 處理）S13 對話反思追加 |

### S14 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/appendix-D-why.md | 修改 | **從 1657 行擴至 2740 行（+1083 行 / 65% 增量）/ 19 Q&A（19/22 = 86%）** — 新增 Q14-Q19 §6 共 6 條 Q&A：Q14 為什麼要把矩陣分解（156 行）+ Q15 A=CR 列秩=行秩（119 行）+ Q16 A=LU 高斯消去本質（165 行）+ Q17 A=QR Gram-Schmidt 動機（138 行）+ Q18 譜定理對稱特徵向量正交（144 行）+ Q19 SVD 任意矩陣存在（174 行）；目錄表 Q14-Q19 6 條從「🚧 規劃中」→「✅ 已完成（S14）」+ 加錨點連結；尾段「其餘 9 條」改「其餘 3 條（Q20-Q22）」+ 改 S15 路線；附錄末時間戳更新 S14 / 19/22 / 86%；Q19 SVD 小例題巧妙連動 Q17 同 $A$ + $A^{\mathrm{T}}A=$ Q18 同矩陣形成「QR→EVD→SVD」教學鏈 |
| docs/book/ch06a-five.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q14 為什麼要分解 + Q11 對角矩陣 + Q13 (P4) 三明治，3 Q&A links，~350 字 hook 含 Strang LAFE「Make every matrix look diagonal」名言 + 5 級遞進對稱性 + 200 年世紀大夢）|
| docs/book/ch06b-CR.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q15 A=CR 列秩=行秩 + Q14 為什麼分解，2 Q&A links，~250 字 hook 含 Sylvester 1851 引入 rank + Strang 2020 首次代數封裝「最樸素分解」+ 「分解 = 結構增加版」遞進設計）|
| docs/book/ch06c-LU.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q16 A=LU 高斯消去本質 + Q14 為什麼分解，2 Q&A links，~330 字 hook 含《九章算術》方程章 2000 年東方原型 + Turing 1948 LU 命名 + 5 跨領域因果結構表）|
| docs/book/ch06d-QR.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q17 A=QR Gram-Schmidt 動機，1 Q&A link，~280 字 hook 含 Gauss 1801 Ceres 軌道最小平方法首次應用 + Householder 1958 數值穩定 + 條件數不被平方化）|
| docs/book/ch06e-QLQ.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q18 譜定理對稱特徵向量正交 + Q11 對角矩陣 + Q13 (P4) 完美三明治，3 Q&A links，~370 字 hook 含 Cauchy 1829 主軸定理 → 量子力學 1920s Hermitian + 物理對稱性=數學正交性 + 對稱矩陣 5 特性繼承 (P4)）|
| docs/book/ch06f-USV.md | 修改 | 章節摘要末新增「💡 背後觀念」callout（連結 Q19 SVD 任意矩陣存在 + Q14 為什麼分解 + Q08 4 子空間 + Q13 (P4) 最強三明治，**4 Q&A links 為全書最多**，~430 字 hook 含 Beltrami 1873 首次發現 + Eckart-Young 1936 最佳低秩近似 + Strang「the most important theorem in linear algebra」名言 + 「一個分解看清所有」）|
| docs/dev/sop/SOP_DRAFT.md | 修改 | **§2.6 補 S14 耗時資料點**（~3.5h / 1083 行 / 6 Q&A + 6 callout / 19 Q&A 累計 86%）+ **§2.13 補 S14 教訓 5 條**（跳順序批量可行 / 小例題巧妙串接 cross-Q 教學鏈 / §6 callout link 數比 §1-§5 高 15% 自然 / Strang 名言當 hook / 雙證明路徑高價值）+ 版本記錄 0.15 |
| docs/dev/CURRENT_SESSION.log | 修改 | S14 啟動 + 即時記錄（Q14 + Q15+Q17+Q18 + Q16+Q19 + 6 callout 分批 metadata）+ 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | （pending — session-end Step 4 處理）追加 S14 一行 |
| docs/dev/HANDOFF.md | 修改 | 整檔覆寫（最後更新 / 已完成 / 進行中 / 待辦 → S15 / 關鍵決策追加 5 條 / 檔案變更追蹤追加 S14 區 / S15 起步建議完整改寫 + S14 起步歷史保留）|
| docs/dev/RETROSPECTIVE.md | 修改 | S14 對話反思追加（本 session 無重大低效時刻 + 三 session 連續驗證「精準分批指令 + 批量產出」最佳工作模式 + 5 條 Claude 自我提醒）|

### S15–S16 新增/修改的檔案

詳見 [SESSION_INDEX.md](SESSION_INDEX.md) S15/S16 行 + [RETROSPECTIVE.md](RETROSPECTIVE.md) S15/S16 反思段 + commit `df95d89`（S15）/ `2f9b9e3`（S16）/ `22aabc2`（S16 收工）。

### S17 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| viz/ch04_matrix_matrix.py | **新增** | **440 行 / 8 cell** — ch04 V-02 MM4 母模板架構階段骨架；PEP 723 metadata 含 marimo+numpy+plotly；cells: (1) imports（mo / np / go / make_subplots）/ (2) 配色 + colormap 常數 / (3) markdown 標題與 (MM4) 公式 / (4) A 6 entry sliders + B 4 entry sliders + r slider / (5) 控制面板 hstack / (6) **核心計算 + 三式對拍 healthcheck**（含 inline helper `rank1_outer / layers_of / accumulate / layer_energy`，避開 `_` 前綴陷阱） / (7) 即時計算 markdown（LaTeX 矩陣 + 能量 + 對拍結果） / (8) 主舞台 2×3 共 6 heatmap subplot / (9) 秩 1 圖層 strip / (10) S17 骨架說明 markdown |
| viz/_common/__init__.py | 新增 | 空檔，宣告 `_common` 為 Python package（本機 reference 用，WASM export 不嵌入子模組 import） |
| viz/_common/rank1_layer.py | 新增 | **工具模組** — `rank1_layer(a, b)` / `layers_of(A, B)` / `accumulate(A, B, r)` / `layer_energy(a, b)` 四函數；本機開發等價於 notebook inline helper；S18+ 非 WASM script / 測試用；WASM 不嵌入子模組所以 notebook 需要 inline 同邏輯 |
| viz/dist/ch04_matrix_matrix/ | 新增（gitignore） | marimo export html-wasm 產出 27 MB static dir，含 Pyodide WASM runtime + plotly bundle + 嵌入的 notebook code with PEP 723 metadata；`viz/.gitignore` 已排除 `dist/` |
| docs/dev/sop/SOP_DRAFT.md | 修改 | **§2.15 標題從「3 大」→「6 大」** + **新增「S17 補充：3 個 marimo 跨 cell / plotly 細節陷阱」**（陷阱 #4 marimo `_` 前綴 cell-private / 陷阱 #5 plotly `subplot_titles` 空字串不生成 annotation slot / 陷阱 #6 plotly heatmap z 需 `np.asarray(M, dtype=float)`）+ S17 對 S18+ 擴充 checklist 4 條 |
| docs/dev/CURRENT_SESSION.log | 修改 | S17 啟動 + 即時記錄（Back 選 A / PoC 寫作 / 2 round WASM debug / 3 個新陷阱）+ 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S17 一行（含 commit `cc957f1` + 完整 2 round debug 記錄 + 3 個新 WASM 陷阱）+ swap S16/S17 順序使時序排列 |
| docs/dev/HANDOFF.md | 修改 | 整檔覆寫（最後更新 / 已完成追加 S17 9 條 / 進行中 / 待辦 → S18 / S18 起步建議完整新寫 + S17 起步歷史保留 / 關鍵決策追加 6 條 / 檔案變更追蹤追加 S17 區）|
| docs/dev/RETROSPECTIVE.md | 修改 | S17 對話反思追加（本 session 主軸 / 對話低效時刻 3 條 / 建議 Back 下次這樣問會更快 2 條 / Claude 自我提醒 6 條） |

---

## 技術筆記

### Repo 原始內容概覽
- **LaTeX 主檔**：`The-Art-of-Linear-Algebra.tex`（英文）、`-j.tex`（日文）、`-zh-CN.tex`（簡中）
- **編好的 PDF**：三種語言版本均已存在
- **圖檔來源**：`Illustrations.pptx`（PowerPoint），透過 makefile 流程印成 PS → EPS → 嵌入 LaTeX

### 互動式版本技術選項（S12+ 決策，目前傾向）

| 方案 | 優點 | 缺點 |
|------|------|------|
| **Marimo + matplotlib + plotly + scikit-learn + Pillow**（S02–S10 VizScript 首選） | 反應式 notebook、純 Python、可匯出 HTML、3D / 影像 / PCA 全支援 | 較新生態系較小 |
| Streamlit + Plotly | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

**S08–S10 觀察累積（3D 渲染棧成 §6 必備 + Mona Lisa 影像處理 + 多應用切換 + Matrix World 同心橢圓向量化 + 4 子空間 3D 仿射視覺）：**
- §6.3 QR：3D 投影視覺（matplotlib 3D / plotly 3D）；
- §6.4 EVD：3D 橢球主軸對齊（plotly 3D 為主，因參數球面渲染流暢度高）；
- §6.5 SVD：**全書最複雜的視覺化棧** — 3D 橢球 + Mona Lisa（Pillow + numpy）+ Iris PCA + 推薦評分視覺 + 4 子空間（重用 ch03）
- **S10 Matrix World 附錄 Tier 2 旗艦：** 11 層同心橢圓需向量化縮放支援（plotly SVG path 為主）+ 章節過濾器 + 範例矩陣辨認需 `numpy.linalg.eig` + `scipy.linalg.norm`
- **S10 Four Subspaces 附錄：** 仿射子空間 3D 視覺（通解平面平行 $\mathbf{N}(A)$ 通過 $\mathbf{x}_p$），需 `plotly.graph_objects.Surface` + `numpy.linalg.pinv`

**結論：S12+ 必確認技術棧支援所有需求**：**Marimo + plotly 3D + matplotlib + scikit-learn + Pillow** 為最低限度組合（涵蓋全書 36 個 VizScript）。

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
| spectral theorem | 譜定理 | — |
| singular value decomposition (SVD) | 奇異值分解（SVD）| — |
| eigenvalue decomposition (EVD) | 特徵值分解（EVD）/ 譜分解 | — |
| Eckart-Young theorem | Eckart-Young 定理 / 最佳低秩近似定理 | — |
| Moore-Penrose pseudoinverse | Moore-Penrose 偽反 / 偽反矩陣 | — |
| Frobenius norm | Frobenius 範數 / F 範數 | — |
| principal component analysis (PCA) | 主成分分析 | — |
| **normal matrix** | **正規矩陣**（S10 新增 — Matrix World L5 層）| — |
| **Markov matrix** | **Markov 矩陣**（S10 新增 — Map of Eigenvalues 12 類之一）| — |
| **nilpotent matrix** | **冪零矩陣**（S10 新增 — Map of Eigenvalues 12 類之一）| — |
| **anti-symmetric / skew-symmetric** | **反對稱矩陣**（S10 新增 — Map of Eigenvalues 12 類之一）| — |
| **Jordan form** | **Jordan 形式**（S10 新增 — Matrix World L4b）| — |
| **affine subspace** | **仿射子空間**（S10 新增 — Four Subspaces 附錄解 $A\mathbf{x}=\mathbf{b}$）| — |

**矩陣尺寸：** $A \in \mathbb{R}^{m \times n}$ 表示 **$m$ 行 $n$ 列**（$m$ rows, $n$ columns）。$m$ = 行數、$n$ = 列數。
**矩陣乘法形狀：** $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$AB = C \in \mathbb{R}^{m \times n}$。**內維 $k$ 必須對齊**。

### 全書視覺一致性錨點（S03 確立，S08+ 補 3D + 金色主元 + 黃色中間結果，S09 補 SVD 雙色對比，S10 補附錄 4 子空間配色一致 + Matrix World 11 層橢圓深藍）

- **配色 hex：** 綠（列 / 直立 / 正交向量 / **U / 列空間**）`#2ca02c`、粉紅 / 紅（行 / 橫躺 / 投影向量 / **V^T / 行空間 / SVD 雙側獨立指紋**）`#d62728`、藍點（個別數字 / 對角元素 / **σ_p 與 λ_p / Matrix World 橢圓邊框 / Map of Eigenvalues 複平面背景**）`#1f77b4`、灰填充 `#cccccc`（原始向量 / 已剝離元素 / **單位球 / 對稱輸入 / Map of Eigenvalues 複平面格線**）、子空間半透明 alpha 0.3、紫色（特徵基底 / 動態系統 / CR 第 3 列 / **退化警示 / 4 子空間零空間方向 / 負特徵值反射**）`#9467bd`、橙色（CR 第 2 列 / 接近依賴警示 / **秩 k 截斷曲線 / Map of Eigenvalues 特徵值點**）`#ff7f0e`、**金色 `#FFD700`**：主元 / 當前正在處理的列 / **變形後的橢球 / EVD 橢球 / Matrix World hover 高亮 / Four Subspaces 特解**、**黃色**：中間結果 $\mathbf{w}_p$（減投影後未單位化）/ Four Subspaces 仿射通解平面（alpha 0.3）
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **3D 視窗尺寸：** 預設 600×480 px、視角 elev=25° azim=-60°（S08 QR 章 / S09 EVD 章 / S09 SVD 章 / S10 Four Subspaces 仿射子空間都必備）
- **動畫時間：** 視角切換 600–800ms、平行性高亮淡入 200ms、子空間維度變化 600ms、飛行軌跡 700ms、秩 1 累加 400ms / 項、緩動 ease-in-out、peeling 動畫 600ms / 楔形（S08）、Gram-Schmidt 減投影 500ms / 投影（S08）、譜分解逐項累加 1500ms / 項（S09）、橢球變形 800ms（S09）、SVD 應用切換 500ms（S09）、**Matrix World hover 200 ms 邊框加粗 + click 400 ms panel 滑入 + 章節過濾 600 ms 淡入淡出（S10）、Four Subspaces 通解平面平移 800 ms（S10）**
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$（3D 限 $\{2, 3\}$、SVD demo Mona Lisa 400×250 / Iris 150×4）；對角元素 $d_p \in [-3, 3]$ 步進 0.5、特徵值 $\lambda_p \in [-9, 9]$、奇異值 $\sigma_p \geq 0$、**Map of Eigenvalues $z$ 拉桿 $z = a + bi$ $a, b \in [-3, 3]$ 步進 0.1（S10）、Four Subspaces 矩陣 $A$ $a_{ij} \in [-3, 3]$ 步進 0.5（S10）**
- **N-way 切換動畫：** 多視角 tab 切換時 800ms 動畫含「色塊重排 + 重染色 + 公式同步」三層
- **對角矩陣表現：** 藍圓點直徑 12–14px 沿對角線排列、**非對角位置完全留白不畫 0**、$d_p$ 改變時藍點半徑 ∝ $|d_p|$
- **動態系統軌跡：** 軌跡藍漸變（淡 → 深 = 時間順序）、當前點紫實心 8px、特徵向量綠箭頭
- **CR 三色標記（S07）：** $A$ 的列 1 = 藍 / 列 2 = 橙 / 列 3 = 紫
- **LU 楔形視覺（S08）：** 楔形 $p$ 大小 ∝ 殘餘子矩陣 $A_p$ 範圍
- **QR 上三角藍點（S08）：** $R$ 用藍點 + 上三角形狀排列展示
- **EVD 鏡像對稱布局（S09）：** $Q$（綠列直立）和 $Q^{\mathrm{T}}$（綠行橫躺）在 $\Lambda$ 兩側鏡像對稱 — 對稱矩陣的視覺指紋
- **SVD 雙色獨立布局（S09）：** $U$（綠列直立）和 $V^{\mathrm{T}}$（**粉紅行橫躺**）使用不同顏色對比 — 雙側獨立的視覺指紋（與 EVD 同色形成對比）
- **譜分解投影矩陣 $P_p$（S09）：** $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 顯示為「綠列 + 淡綠橫躺行」自外積（左右標號相同）
- **SVD 秩 1 拆解（S09）：** $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 顯示為「綠列 + 淡粉紅橫躺行」一般外積（左右標號相同但顏色不同）
- **跨章跳轉按鈕（S07–S10）：** 白底深綠邊框 + 「→」字樣，hover 填色 `#2ca02c`；按鈕分四類「→ (MM4) 累加 / Mona Lisa」（指 ch04 V-02）/「→ (P1)(P2) 對角」（指 ch05 V-01）/「→ (P4) 三明治」（指 ch05 V-03，S09 補 EVD/SVD pointer）/「→ 4 子空間」（指 ch03 V-02，S09 補 SVD 整合，S10 補附錄 C pointer）
- **附錄旗艦 Matrix World 視覺（S10）：** 同心橢圓深藍邊框 + 章節過濾器粉紅標記 + 範例矩陣對應層漸變色（最外淺藍 → 最內紫紅）+ hover 黃金高亮 + Tier 標記顏色說明面板
- **附錄 Map of Eigenvalues 視覺（S10）：** 12 格 grid view 並列 + 點任一格 zoom 800×600 + 拉桿即時動畫 200 ms 平滑移動橙色特徵值點
- **附錄 Four Subspaces 解 $A\mathbf{x}=\mathbf{b}$ 視覺（S10）：** 紫色零空間 + 金色特解 + 黃半透明通解平面 + 綠色最小範數最優解 4 色組合 + 殘差數值即時顯示

### 章節撰寫速度資料點（S10 更新 + 完整里程碑回顧）

- **S02 §1（含 A 派切換重寫 0.5h）：** 1.5h / 418 行 / 2 VizMark
- **S03 §2（ch01 範本可複用）：** 1h / 497 行 / 2 VizMark
- **S04 §3（4 VizMark 分級策略）：** 1.5h / 935 行 / 4 VizMark
- **S05 §4（1 圖含 4 子圖 + 4 VizMark）：** 1h / 849 行 / 4 VizMark
- **S06 §5（4 圖各獨立 + 6 Pattern + 4 VizMark）：** 1h / 830 行 / 4 VizMark
- **S07 §6 總覽 + §6.1（兩章 session）：** 2h / 876 行（331 + 545）/ 4 VizMark — 兩章 session 模式首次驗證
- **S08 §6.2 LU + §6.3 QR（兩章主章模式）：** 2.5h / 1195 行（654 + 541）/ 6 VizMark — 主章 + 主章模式驗證 + 3D 渲染棧導入
- **S09 §6.4 EVD + §6.5 SVD（兩章主章模式收尾）：** 3h / 1629 行（695 + 934）/ 7 VizMark — SVD 章 934 行為全書最長 + Tier 3 主 VizScript 首次出現在 §6
- **S10 Foreword + Conclusion + 3 附錄（散文 + 附錄混合 session）：** **~2.5h / 1290 行（158 + 198 + 272 + 328 + 334）/ 3 VizMark（1 Tier 2 旗艦 + 2 Tier 1 + pointer）— 附錄重整合 vs 主章重教學雙模式確立 + Matrix World 升級 Tier 2 旗艦（S12+ 全書首頁）**
- **S11 預估：** **~1.5h / 整合工作（不新撰寫）**：BOOK.md 合併（13 個 md 檔依順序串接 + 重新編號）+ VIZ-CATALOG.md 抽取（36 個 VizScript 索引）+ 跨檔 anchor link grep 校驗 + 風格 / 配色 / 術語統一檢查 + 資料一致性校驗（VizScript 總數 36、`using XX` 標記譜系、雙 pointer / 單 pointer 分佈）
- **S11 實際：** **~2h / 整合 + 校對 + 統一 5 項任務 + Strang PDF 防護**：(3) anchor 校驗 9 處 broken 修復 / (5) 一致性 Tier 表 6 處校正 / (1) BOOK.md 8650 行（**含 fence-code-aware awk 教訓**：第一輪 sed `g/^#/##/` 誤把 ch06e Python code block 內 `# 參數化單位球` 等註解改為 ## heading，重生用 awk 解決）/ (2) VIZ-CATALOG.md 241 行 / (4) SCHEMA §3.5 新增 + 23 處 sed 修正（**macOS BSD sed 不支援 `\b` word boundary，需改用 `([0-9]) ms` 不帶 boundary**）+ 額外 Strang 版權 PDF 雙保險 .gitignore 防護 + memory feedback 兩層級分開記憶
- **S12 實際：** **~2.5h / 背後觀念層啟動 9/22 Q&A + 4 主章 callout 插入 + memory 新增**：規劃階段（4-session 路線圖 + 22 條 Q&A 清單）~30 min + Q09 PoC（2500 字 / 含九章算術原文 / Cayley 1858 / 2×2 例題雙路驗證）~30 min + Q01-Q08 批量寫（865 行 / 8 條 / 含 3 動機殊途同歸推導等深度版本）~1.5h + 4 主章 callout 客製化 + foreword 23→36 bug 修 ~15 min + memory feedback_why_layer.md 新增（3-layer 框架明文化） ~10 min。**Q&A 內容篇幅分佈：** Q01 最短 56 行（散文章節無需推導）/ Q08 最長 156 行（含 Big Picture ASCII 圖 + 完整正交補餘證明）/ 平均 ~108 行 / Q&A。**每條 Q&A 平均 ~1200-2500 字含 1-3 段歷史 + 1 段完整推導 + 1 個小例題 + 1 段昇華 + 5-15 條延伸閱讀**。
- **S13 實際：** **~2h / Q10-Q13 §4 + §5 共 4 條 Q&A 批量 + 2 主章 callout（ch04 + ch05）**：4 條 Q&A 批量寫 ~1.5h（Q10 95 行 / Q11 111 行 / Q12 121 行 / Q13 156 行 = 平均 121 行 / 條，比 S12 平均 108 行長 12%；每條平均 ~25 min 含搜尋史線 + 公式 + 例題）+ 2 主章 callout 客製化（ch04 ~300 字 hook + ch05 ~400 字 hook）+ typo 修正 ~10 min + 統計 / 目錄表更新 / 尾段路線改 ~10 min。**S13 觀察：** (1) **「PoC 後可直接批量」流程驗證** — S13 跳過 PoC 直接批量，4 條共 ~1.5h，無中途 review 風格仍一致；(2) **Q&A 篇幅由「動機問題深度」決定** — Q10 四層理由清單 95 行 / Q13 (P4) 連 §6 集大成 156 行，差異 64% 屬正常；(3) **callout 客製化 hook 寫法** — ch04 用「行乘列來源 + 不可交換本質」雙 hook、ch05 用「對角矩陣超能力 + (P3) DNA + (P4) 世界觀」三 hook，比泛論「為什麼這條規則長這樣」具體；(4) **Q&A 跨章 cross-link 知識網路擴張** — Q10↔Q13 / Q11↔Q12↔Q13 / Q12↔Q18 等添加 ~10 條，與 S12 已建立的三角形成全書 Q&A 密集網路。

### 背後觀念層撰寫資料點（S12 確立，S13 更新 / S14-S15 沿用）

| 指標 | S12 數值（Q01-Q09 / Foreword + §1-§3）| S13 數值（Q10-Q13 / §4-§5）| 全期累計（Q01-Q13）|
|---|---|---|---|
| 每條 Q&A 平均行數 | ~108 行 | ~121 行（+12%）| ~112 行 |
| 每條 Q&A 平均字數 | ~1500 字 | ~1900 字（+27%）| ~1620 字 |
| 每條 Q&A 平均寫作時間 | ~12 min（含 PoC 30 min）| ~25 min（無 PoC）| 平均 ~16 min |
| Q&A 批量整體 | 865 行 / ~1.5h / 8 條 | 482 行 / ~1.5h / 4 條 | 1347 行 / 3h / 12 條 |
| Q09 PoC（含風格鎖定）| 2500 字 / ~30 min | — | — |
| 主章 callout 插入 | 4 個 / 8 links / ~15 min | 2 個 / 5 links / ~10 min | 6 個 / 13 links / 25 min |
| memory 規範記憶 | feedback_why_layer.md ~80 行 / 10 min | — | — |

**S14-S15 預估：**
- **S14**（§6 五大分解 = Q14-Q19 共 6 條 + ch06a-ch06f callout）：~2.5h（每條預期 ~150 行 / ~30 min，因含分解定理證明 + (P4) 連結）
- **S15**（附錄 = Q20-Q22 共 3 條 + 3 附錄 callout + BOOK.md 重新生成 + VIZ-CATALOG / SCHEMA / VIZ_SCHEMA callout 規範 + HANDOFF / SESSION_INDEX / SOP_DRAFT 整批收尾）：~1.5h
- **總 S14-S15 預估：** ~4h 完成全 22 條 Q&A + 全書主章 callout（剩 ch06a-f 6 個 + 3 附錄 3 個 = 9 個 callout）+ 整合收尾

**§1–§6 + 序言 + 結論 + 3 附錄累計（S10 收尾）：** 共 **13 個 md 檔（ch01–ch06f 9 個主章 + front-foreword + back-conclusion + 3 附錄）= 總計 ~8100 行**（主章 6824 行 + S10 散文/附錄 1290 行）+ **36 個 VizScript**（4 個 Tier 3：[ch04 V-02](../book/ch04-mat-mat.md#vizscript-02) + [ch06f V-01](../book/ch06f-USV.md#vizscript-01) 兩支主旗艦 + ch04 V-01（Tier 2）+ ch06f V-02（Tier 2）；多支 Tier 2 含 [appendix-matrix-world V-01](../book/appendix-matrix-world.md#vizscript-01) 旗艦 + 多支 Tier 1）。**§1–§6 全書內容 100% 完成**，下階段轉入「校對 + 整合 + 風格統一」（S11）。

### §4 (MM4) 與 §6 五大分解的鋪陳對應（S09 完整定版，S10 補附錄連結）

| §6 分解 | (MM4) 形式 | VizScript 結構複用 | PNG `using XX` 標記 | Pointer 設計 |
|---|---|---|---|---|
| $A = CR$ | $A = \sum_p \mathbf{c}_p \mathbf{r}^*_p$（$r$ 項） | ch04 V-02 + ch05 V-01 | CR1 標 P1、CR2 標 P2 | 雙 pointer（對偶兩張圖）|
| $A = LU$ | $A = \sum_p \mathbf{l}_p \mathbf{u}^*_p$（$n$ 項） | ch04 V-02 | LU1 無標、LU2 標 MM4 | 單 pointer 指 ch04 |
| $A = QR$ | $A = \sum_p \mathbf{q}_p \mathbf{r}^*_p$（$n$ 項） | ch05 V-01 | QR 標 P1 | 單 pointer 指 ch05 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$（自外積）| ch05 V-03 | EVD 標 P4 | 單 pointer 指 ch05 |
| $A = U\Sigma V^{\mathrm{T}}$ | $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$（一般外積）| ch04 V-02 + ch05 V-03 | SVD 標 P4 | 雙 pointer（集大成 + 內容旗艦同根）|
| **附錄 A Map of Eigenvalues**（S10）| — | 重用 ch06e V-01（EVD 詳解）| **無 using 標**（地圖層級）| Tier 1 + pointer 指 ch06e |
| **附錄 B Matrix World**（S10 旗艦）| 含全部 5 分解 + 偽反 | 整合全書 36 個 VizScript 索引 | **無 using 標**（標 Strang section number）| **Tier 2 旗艦** — 跨全書索引 dashboard |
| **附錄 C The Four Subspaces**（S10）| — | 重用 ch03 V-02 + ch06f V-03 + 新增解 $A\mathbf{x}=\mathbf{b}$ 視覺 | **無 using 標**（基本概念）| Tier 1 + pointer 指 ch03 + ch06f |

**S10 結論（§1–§6 全書 md 化收尾）：** ch04 V-02（MM4 + Mona Lisa SVD demo）+ ch06f V-01（SVD 完整互動）+ appendix-matrix-world V-01（全書互動式教材首頁）= **「全書互動式教材的核心三旗艦」**（兩支 Tier 3 內容旗艦 + 一支 Tier 2 索引旗艦）。**S12+ 實作優先順序明確化：**

1. **首批實作（核心骨架）：** ch04 V-02（3 session）+ ch06f V-01（3 session）+ appendix-matrix-world V-01（2 session）= **8 session 完成核心三旗艦，宣稱「全書互動式教材核心骨架 100%」**
2. **次批實作（主章 Tier 2 + 4 子空間整合）：** ch06b/c/d/e V-01 各 2 session = 8 session；ch03 V-02（4 子空間 3D，視時間升 Tier 3）3 session；ch01–ch05 各章 V-01（共 5 個 Tier 2）共 7 session；3 附錄各 V-02+ 共 3 session
3. **末批實作（Tier 1 輕量 + walkthrough）：** ~6 session
4. **Total S12+ 預估：** **~30 session 完成完整互動式教材**（不含技術棧 PoC 初期 ~3 session）。整個專案總 S00–S40 = ~40 session

**§6 章節雙 pointer 設計地圖規律（S09 確立，S10 附錄延續）：**

- **雙 pointer 採用：** 對偶兩張圖（CR1+CR2）+ 集大成終章（SVD）；
- **單 pointer 採用：** 單張圖且非集大成章（LU / QR / EVD）+ 附錄基本概念圖（Map of Eigenvalues / 4-Subspaces）；
- **Tier 2 跨全書索引：** Matrix World 附錄無 pointer 是「**自身就是全書 36 個 VizScript 的彙整索引**」
- **判準：** PNG `using XX` 標記重複 + 內容旗艦同根**雙條件**成立才升級雙 pointer。

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔，S13 收工版）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表（含 S13）
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
4. **docs/book/appendix-D-why.md — S14 開工首要檔（背後觀念 Q&A 附錄，目前 13/22 完成；S14 從 Q14 為什麼要分解開始批量寫 Q14-Q19 §6 五大分解）**
5. docs/book/VIZ-CATALOG.md — 全書 36 個 VizScript metadata 索引（S16+ 視覺化階段用）
6. docs/book/BOOK.md — 全書合併單檔（8650 行，整本書離線閱讀版；S15 整合收尾需重新生成含 appendix-D-why.md）
7. docs/book/SCHEMA.md（§3.5 全書視覺錨點）+ docs/book/VIZ_SCHEMA.md（§2.3 cross-reference）
8. docs/book/ch01-ch05 + ch06a-ch06f + front-foreword + back-conclusion + 3 附錄 + **appendix-D-why** = 17 個 md 範本（ch01-ch05 + foreword 已含「💡 背後觀念」callout 範本 / ch06a-ch06f + 3 附錄 待補 callout）
9. docs/dev/sop/SOP_DRAFT.md（含 S00-S13 全部章節寫作策略 + 背後觀念層 3-layer 框架）
10. docs/dev/RETROSPECTIVE.md — Session 對話反思（含 S13 條目）
然後從「S14 起步建議」決定本次任務：
- **首選：S14 §6 五大分解 = Q14-Q19 共 6 條 Q&A 批量寫**（Q14 為什麼要分解 / Q15 A=CR 列秩=行秩 / Q16 A=LU 高斯消去法 / Q17 A=QR Gram-Schmidt / Q18 譜定理對稱矩陣 / Q19 SVD 任意矩陣）+ ch06a-ch06f 主章「💡 背後觀念」callout 插入（6 個）；預估 ~2.5h
- **Q&A 寫作 schema：** 沿用 Q01-Q13 風格（觸發問題 + 3-layer ①歷史 / ②推導 / ③昇華 + 延伸閱讀含本書 cross-ref + 歷史原典 + 現代教科書），可大段引用 Strang《Linear Algebra for Everyone》/ 《Introduction to LA》/《LA and Learning from Data》/ Calculus Vol 1-3 等 docs/book/*.pdf 私人參考（已 .gitignore 不 push）
- **callout schema：** 沿用 S12-S13 ch01-ch05 範本（章節摘要末 + 術語提醒 ⚠ 後 + `---` 數學要點前；列表式 1-N 條 hook + 連結附錄 D；每條 Q&A 對應一個「最具體最有畫面感」的關鍵詞 hook）
- **S13 觀察可直接套用：** PoC 已完成（S12 Q09），S14 可跳過 PoC 直接批量；§6 Q&A 預期每條 ~150 行（含分解定理證明 + (P4) 三明治連結 + 矩陣分解步驟）
```
