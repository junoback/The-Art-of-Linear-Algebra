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

**S06 §5 實際耗時參考：** 約 1h（4 張獨立小圖 + 6 個 Pattern + 4 個 VizMark/VizScript），產出 830 行（與 ch04 相當）。**關鍵觀察 1：HANDOFF 預估漏掉了 P4。** S06 起步時 HANDOFF 寫「§5 5 個 Pattern（P1/P2/P1'/P2'/P3）」，實際讀原書才發現有 P4（$U\Sigma V^{\mathrm{T}}$ 三明治）— **P4 是 §6.4/§6.5 兩大分解的共骨架**，是本章最重要的視覺 bridge。**教訓：HANDOFF.md 的章節描述要在進入該章節時對著原書 PNG 重新檢核 Pattern/Figure 數量，不能信任前 session 的記憶**。**關鍵觀察 2：「多 figure 小章節」與「N-way 單圖章節」的耗時差異不明顯** — ch04 (1 圖 4 子圖) 和 ch05 (4 圖各獨立) 雖然圖數天差地遠，總耗時都是 1h、篇幅都是 830-849 行。**結論：耗時的瓶頸是 VizScript 個數與 Tier 分級，不是圖數。** **關鍵觀察 3：「Tier 1 + pointer」策略首次驗證** — VizScript-03 (P4 三明治) 因為「累加 / 截斷 / Mona Lisa demo 已在 ch04 VizScript-02 完整實作」而採 Tier 1 + pointer 設計，總長僅 100 行（vs Tier 3 估 2.5 session + 200+ 行劇本），節省篇幅與 S12+ 實作工時。**這個策略適用於後續 §6 5 大分解的章節 — 每個分解的 (MM4) 累加 demo 都可指向 ch04 VizScript-02，章內只寫各分解的「特殊性質」demo（正交 / 對稱 / 三角等）**。**關鍵觀察 4：「對偶 Pattern」可在數學要點段中以對偶總表呈現，省下圖描述的篇幅** — (P1) ↔ (P2) 與 (P1') ↔ (P2') 兩組對偶都用對偶總表 (3 列 × 4 欄) 表達，比兩兩獨立寫描述節省 ~40% 篇幅且閱讀時更易對照。

**S07 §6 總覽 + §6.1 實際耗時參考：** 約 2h（兩章 session），產出 876 行（ch06a-five 331 行總覽 + ch06b-CR 545 行主章）。**關鍵觀察 1：兩章 session 模式首次驗證可行** — §6 五大分解總覽是「短章節」（只有 1 個 VizMark + 1 張總圖），單獨成一個 session 太浪費；與 §6.1 合併成兩章 session 後總耗時 2h（比兩個獨立 session 的 ~2.5h 省 0.5h），且第二章的 (MM4) / (P1)/(P2) pointer 設計可直接從第一章繼承。**後續 S08/S09 也可採兩章 session 模式：** S08 = §6.2 LU + §6.3 QR、S09 = §6.4 QΛQᵀ + §6.5 SVD。**關鍵觀察 2：原書 PNG 標 `using P1` / `using P2` 是跨章連結的官方鐵證** — CR1/CR2 圖右下角直接標記 §5 (P1)(P2) Pattern，這代表 §6.1–§6.5 全部都會把 §5 Pattern 套到對應視角圖上（S08/S09 起步時必須逐章重核 PNG 是否有 `using PX` 標記）。**這個發現升級了「Tier 1 + pointer」策略**：本章 VizScript-01 採取**雙 pointer 設計**（同一劇本同時指向 ch04 VizScript-02 看 (MM4) 累加 + ch05 VizScript-01 看 (P1)(P2) 對角特例），實踐證明可行。**關鍵觀察 3：「對偶兩張圖」是 §6.1–§6.5 的全書一致模式** — CR1 (列視角) + CR2 (行視角) 的對偶圖佈局，預期 §6.2 LU1/LU2、§6.3 QR、§6.4 EVD、§6.5 SVD 都會有類似的「列觀點 / 行觀點」對偶設計。VizScript 可統一採「三模式切換」（列視角 / 行視角 / 並排）。**關鍵觀察 4：總覽章 + 主章的篇幅比約 1:1.6**（331 vs 545 行），總覽章短但 VizMark 規格高（Tier 1 + pointer 同時也是核心畫面控制器）— S08/S09 不需要再寫總覽章，可全力寫主章。

**S08 §6.2 LU + §6.3 QR 實際耗時參考：** 約 2.5h（兩章 session 第二次驗證），產出 1195 行（ch06c-LU 654 行 + ch06d-QR 541 行），**比 S07 的 876 行多 36%**。**關鍵觀察 1：S07 PNG 重核教訓延續發揮 — `using XX` 標記譜系擴大** — S08 PNG 重核發現：(a) `LU1.png` 無 `using` 標記（peeling 是 LU 特有演算法，不直接套 §4/§5 Pattern）、(b) `LU2.png` 標 **`using MM4`**（圓圈標）— 這是 (MM4) 累加視角的官方鐵證，不是 (P1)/(P2)、(c) `QR.png` 標 **`using P1`**（圓圈標）— Gram-Schmidt 反向公式 $\mathbf{a}_p = \sum r_{kp} \mathbf{q}_k$ 就是 (P1) 列線性組合。**結論：跨章 pointer 標記不只 P1/P2，還有 MM4**；§6.4/§6.5 起步時必逐張 PNG 對所有可能 `using` 標記重核（P1/P2/P3/P4/MM1/MM2/MM3/MM4 共 8 種候選）。**關鍵觀察 2：「單 pointer」設計比「雙 pointer」更常見** — S07 ch06b 採雙 pointer（同時指 ch04+ch05），但 S08 兩章都採單 pointer：LU 章只指 ch04 VizScript-02 (因 LU2 標 MM4 而非 P1/P2)、QR 章只指 ch05 VizScript-01 (因 QR 只標 P1 不標 MM4)。**規律：PNG 標什麼 `using XX`，VizScript 就指對應章；不要強行加 pointer 增加複雜度**。**關鍵觀察 3：LU 比 CR 內容多 ~20%、QR 略少於 CR** — LU 章 654 行因含「解 Ax=b 兩步法 + 高斯消去步驟對應 + Forward/Back substitution 計算實例」三層內容；QR 章 541 行接近 CR 的 545 行，但結構不同（QR 只 1 張圖、無對偶圖、改用 Gram-Schmidt 流程當主軸）。**規律：分解章節篇幅主要由「應用面廣度」決定**（LU 解方程是核心應用、QR 最小平方是核心應用、CR 列秩=行秩證明是核心觀念，後者比前兩者輕）。**關鍵觀察 4：3D 投影視覺是 QR 章獨有需求** — Gram-Schmidt 的「投影到 q_k 方向再減」幾何意義在 2D 不夠豐富，3D 視窗成為 QR VizScript-01 的必要元件（其他章節都是 2D 為主）。**對 S12+ 工件清單影響：matplotlib 3D + plotly 3D 是 QR 章必需的渲染棧**，估計增加 0.5 session 實作成本，但回報極高（學生對「正交化」的幾何直覺幾乎只能靠 3D 建立）。**關鍵觀察 5：兩章 session 模式進化為「主軸 + 主軸」模式** — S07 是「總覽（短）+ 主章（長）」，S08 是「主章 + 主章」（兩章都是 500+ 行的完整分解章）。**新模式驗證：兩個獨立的「分解主章」放同一 session 完全可行，耗時 2.5h 比兩個獨立 session 預估的 3h 省 0.5h**。S09 (§6.4 QΛQᵀ + §6.5 SVD) 也用此模式，但預期 SVD 章會是全書最長（~700 行），總計可能 3.5h / 1300 行。

**S09 §6.4 QΛQᵀ + §6.5 SVD 實際耗時參考：** 約 3h（兩章 session 第三次驗證，§6 主章序列收尾），產出 **1629 行**（ch06e-QLQ 695 行 + ch06f-USV **934 行**），**比 S08 的 1195 行多 36%**，**SVD 章 934 行為全書最長章節**（超出預估 700 行 33%）。**關鍵觀察 1：「雙 pointer 復活」策略 + S09 修正 SOP 規律** — S08 觀察 2 寫「PNG 標什麼就指什麼，單 pointer 為常規」；S09 修正：**雙 pointer 不只看 PNG 標記，也看「內容鐵證」** — 當該章核心 demo 與另一章已實作的旗艦 demo **同根**（如 SVD 與 ch04 VizScript-02 Mona Lisa SVD demo），可破例升級雙 pointer。**§6.4 EVD 嚴守單 pointer 指 ch05 VizScript-03（PNG 標 P4）；§6.5 SVD 升級雙 pointer 主指 ch04 VizScript-02 + 副指 ch05 VizScript-03**（PNG 標 P4 但內容鐵證來自 ch04 Mona Lisa）。**判準明文化：「雙 pointer = PNG 標記重複 + 內容旗艦同根」雙條件成立**。**關鍵觀察 2：S09 PNG 重核重大發現 — EVD 與 SVD 都標 `using P4`，HANDOFF 預估 SVD 雙標 P4+MM4 被推翻** — SVD.png 只標 P4，沒有 MM4 標記。**結論：原書 PNG 標記層級設計傾向「最高抽象（Pattern）+ 不重複底層（外積之和）」** — Pattern 是「結構配方」、MM4 是「展開機制」，PNG 標記偏向高抽象的 Pattern，不重複展開機制（除非 LU2 那種 peeling 視角無 Pattern 可用才標 MM4）。**§6.x 各章 PNG `using XX` 標記最終地圖（S07-S09 三 session 累積）：** CR1=P1 / CR2=P2 / LU1=無 / LU2=MM4 / QR=P1 / EVD=P4 / SVD=P4 — 共 7 張主圖、5 種 `using XX` 標記（P1/P2/P4/MM4/無）。**關鍵觀察 3：「Tier 3 主 VizScript」首次出現在 §6 章節** — 此前 Tier 3 只出現在 ch04 VizScript-02 (MM4 + Mona Lisa)。SVD 章 VizScript-01 是**全書第二支也是 §6 唯一**的 Tier 3 主 VizScript，整合 4 應用切換 + 4 子空間視覺 + 2D 幾何 + Mona Lisa demo。**S12+ 實作優先順序明確化：ch04 VizScript-02 + ch06f VizScript-01 是「全書互動式教材的核心骨架」，預估各 3 session，完成後可宣稱「核心骨架 80%」**。**關鍵觀察 4：分解章篇幅由「應用面廣度」規律進一步驗證** — SVD 章 934 行因含「4 大應用詳解段（壓縮 / PCA / 降噪 / 推薦）+ Eckart-Young 定理 + 4 子空間整合 + 雙 pointer 設計 + Tier 3 主 VizScript（≈ 350 行單一 VizScript）」**五層內容**，比 LU 654 行的「三層內容」再多兩層。**結論：SVD 章 934 行是全書應用面最廣 + 跨章整合最深 + VizScript 規格最高的「集大成」章節**。**關鍵觀察 5：§6 主章序列（§6.1–§6.5）收尾，全書終章（§6.5 SVD）篇幅遠大於前章** — S07 (CR) 545 / S08 (LU 654 + QR 541) / S09 (EVD 695 + SVD **934**) — 比例 1.0 : 1.20 : 0.99 : 1.28 : 1.71，**SVD 是平均章節（~600 行）的 1.6 倍**。**對全書架構意涵：SVD 章不只是「§6 最後一章」，而是「§1–§6 全書集大成的終章」**，從 4 應用詳解 + 跨章整合 + Tier 3 規格三方面都驗證了這個地位。**關鍵觀察 6：§6 章節雙 pointer 設計地圖（S07-S09 累積）：** CR=雙 pointer (ch04+ch05) / LU=單 pointer ch04 / QR=單 pointer ch05 / EVD=單 pointer ch05 / SVD=**雙 pointer 主 ch04 + 副 ch05**。**規律：對偶兩張圖（CR1+CR2）與「集大成」章（SVD）採雙 pointer，單張圖且非集大成的章採單 pointer**。**對 S10 影響：附錄 MapofEigenvalues / MatrixWorld / TheFourSubspaces 起步前必對 PNG 重核 `using XX` 標記**（S09 確認 7 種標記候選：P1/P2/P3/P4/MM1/MM2/MM3/MM4 + 無標記）。

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

### 2.10 整合 session 流程（S11 確立）

**S11 是「不新撰寫，純整合 / 校對 / 統一」session**，與前 S02–S10「逐章寫」session 工作流不同。整合 session 5 項標準任務按順序執行：

1. **(3) 跨檔 anchor link 校驗** — `grep -nE "\]\([a-zA-Z0-9_-]+\.md#" docs/book/*.md` 抓所有跨檔連結 + 對照每個檔案內 `grep -nE "^### VizScript-"` heading 是否實際存在。**S11 教訓：** 邏輯級 `#vizscript-NN` 連結全對（39 處）但發現 9 處 broken `#N` 短 anchor（指 ch06f §N 段落而非 VizScript），用方案 B 修復（重指 `#vizscript-01/03` 符合附錄「pointer 哲學」）
2. **(5) 資料一致性校驗** — VizScript 總數 + `using XX` 標記地圖 + Tier 統計表三項對照。**S11 教訓：** Tier 統計表 6 處需校正（HANDOFF 累積總數 33→36、Matrix World 旗艦補入、ch06a 改 Tier 1+pointer、附錄 3 個列入、Tier 2 從~10 改 14 + 1 旗艦、Tier 1 拆 +pointer 3 個與精簡 15 個）+ S12+ 三批排程連動修正
3. **(1) BOOK.md 完整合併** — 16 個原 md 檔依序串接（front-foreword → ch01–ch06f → back-conclusion → 3 附錄）+ root heading + 全書目錄 + 統計表。**S11 教訓：** 用 sed `s/^#/##/` 第一輪會誤改 Python code block 內的 `# 註解` 為 `## heading`；改用 **fence-code-aware awk**（追蹤 ``` ``` 狀態，code block 內保留原樣）解決
4. **(2) VIZ-CATALOG.md 抽取** — 純 metadata 索引（**不複製內容**），每行 7 欄位（連結 + Tier + 批次 + 估時 + 互動類型 + 數學基底 + 跨章 pointer + 狀態）+ 三批排程 + 跨章 pointer ASCII 連動圖 + 進度追蹤 5 狀態。**設計哲學：** BOOK.md（離線閱讀）+ VIZ-CATALOG.md（入口索引）+ 原章節 md（實作詳情）= 三檔組合
5. **(4) 風格 / 配色 / 術語統一檢查** — grep hex 配色出現位置 / A 派列行慣例 / cell 像素 / 動畫時間 / 3D 視角。**S11 教訓：**
   - **macOS BSD sed 不支援 `\b` word boundary**，要用 `([0-9]) ms` 不帶 boundary 解；用 `LC_ALL=en_US.UTF-8 sed -E` 處理 UTF-8 多字節字符（如 `×`）
   - **3D 視角預設規範**是被忽視的全書錨點 — 109 次 3D 提及但只 1 處明確聲明 → S11 補 SCHEMA.md §3.5「全書視覺錨點」段（**elevation=25° azimuth=-60°**）讓 S12+ 各 3D VizScript 有共同錨點

**整合 session 耗時資料點：** S11 ~2h / 8650 行 BOOK.md 合併 + 241 行 catalog 抽取 + 23 處 sed 修正 + SCHEMA §3.5 新增 ~80 行 + .gitignore 防護 + memory 更新。

### 2.11 跨 session 大數字一致性校驗 SOP（S10 + S11 教訓融合）

HANDOFF.md 累積寫的「全書 VizScript 數 23」實為 36（S10 發現漏算 ch03/ch04/ch05 各 4 個共 12，少數 ~10）+ S11 conclusion 表「總計 33」也應為 36（附錄 3 漏列）— **跨 session 大數字累積誤差是常見問題**。建議規範：

1. **每個整合 session 必做 grep 校驗** — `for f in ch*.md appendix-*.md; do grep -cE "^### VizScript-" "$f"; done` 即時 grep + sum，與 HANDOFF / conclusion / catalog 三處數字對照
2. **單一真相來源確立** — conclusion.md Tier 統計表是 VIZ-CATALOG.md 的單一真相，校正一處後其他檔案隨之更新
3. **數字校正連動修正** — 例：S11 把 conclusion 33→36 也連帶修 root heading「33 個 VizScript 總覽」→ 36 + S12+ 排程「ch06b/c/d/e 5 個」→ 4 個

### 2.12 兩層級版權檔管理（S11 確立）

Back 提供 8 本 Strang 版權 PDF 至 docs/book/ 私人參考用，明確區分兩層級：

| 層級 | 規則 | 操作 |
|---|---|---|
| **PDF 檔本身** | 絕對不 push GitHub | `.gitignore` 雙保險：`docs/book/*.pdf` pattern + 5 白名單反白（已 commit 的原 repo 公開 PDF）|
| **md 檔內引用原文** | 可大段引用（Back 授權「重點是 md 完整性」）| 引 Strang 經典定義 / 證明 / 例題段落整段複製到自家 ch0X / appendix-X md，標出處（書名 + 章節 + 頁碼）|

**關鍵教訓：** Claude 不要自行限縮引用幅度（fair use 短句策略過保守會使 md 失去完整性）；Back 為 fork 法律主體，引用判斷以 Back 授權為準。

### 2.13 背後觀念 3-layer 框架（S12 確立）

S12 啟動「背後觀念層」開發階段 — Back 發現全書 13 個主章只講「**怎麼算**」缺「**為什麼這樣算**」維度。為每條運算規則 / 定理 / 矩陣分解補上「**為什麼這條規則長這樣**」的設計動機說明，需採固定 3-layer 結構：

| Layer | 內容 | 範例（Q09 矩陣乘法為什麼列乘行）|
|---|---|---|
| **① 歷史脈絡** | 何時 / 由誰 / 為了什麼問題而生（含經典出處與年代）| 《九章算術》方程章（西元前 1 世紀劉徽 263 年注本，原文）→ Sylvester 1850 命名 → **Cayley 1858 《A Memoir on the Theory of Matrices》正式定義矩陣代數**（附 Cayley 原論文初心引言「composition or multiplication of two operations」）|
| **② 設計過程還原** | 從問題出發逆向推導出規則（含完整代數推導 + 1 個小例題）| 兩組線性變換 $\mathbf{y}=A\mathbf{u}$、$\mathbf{u}=B\mathbf{x}$ → 代入展開 $y_1$ → 觀察規律「$A$ 第 $i$ 行 · $B$ 第 $j$ 列」自然冒出 → 一般化定義 → 2×2 小例題雙路驗證 |
| **③ 概念昇華** | 一句話收尾，把規則昇華為更高階概念 | 矩陣乘法 = 函數合成 $(A\circ B)$ + 5 條矩陣現象（不可交換 / 結合律 / $AI=A$ / 反矩陣順序顛倒）對照表 + Strang LAFE §1.4「秩 1 分解才是矩陣乘法核心」引言 |

**3-layer 規則：**
- **③ 概念昇華必有** — 不能寫完不收尾
- **① 歷史層彈性** — 純概念類（如「為什麼有 4 種視角」）可略過 ①；純歷史類（如「矩陣何時被發明」）可略過 ②
- **延伸閱讀必有** — 本書 cross-ref + 歷史原典 + 現代教科書三類

**方案 D 雙層落點：**

| 落點 | 篇幅 | 用途 |
|---|---|---|
| **主章 callout（💡 背後觀念）** | ~150-300 字 | 短摘要 hook + 連結附錄 D；放在「章節摘要」段末（術語提醒 ⚠ 後、`---`「數學要點」前）|
| **附錄 D（appendix-D-why.md）** | 1000-2500 字 / 條 | 詳盡 3-layer + 完整推導 + 例題 + 經典引用；採客製化列表式（一章對應多 Q 時用列表 + 不重複內容只給連結）|

**Q&A 之間 cross-link 形成知識網路** — 例 §3 三條互相 reference（Q06 ↔ Q07 ↔ Q08 形成三角）、§2 兩條互相 reference（Q04 ↔ Q05 點積外積對偶）、§1 ↔ §4 ↔ §6 三條互相 reference（Q01 圖解優先 ↔ Q09 矩陣乘法 ↔ Q19 SVD）。

**§2.6 S12 耗時資料點：** ~2.5h / 規劃（30 min）+ Q09 PoC（30 min）+ Q01-Q08 批量（1.5h，平均 ~12 min / 條）+ 4 主章 callout（15 min）+ memory 新增（10 min）；產出 [appendix-D-why.md](../book/appendix-D-why.md) **1175 行 / 67.7 KB / 9 Q&A（9/22 = 41%）** + 4 主章 callout / 8 Q&A links + memory `feedback_why_layer.md`。

**§2.6 S13 耗時資料點：** ~2h / Q10-Q13 §4+§5 批量（1.5h，平均 ~25 min / 條，含搜尋史線 + 公式 + 例題；比 S12 平均 12 min / 條長 — **因為 §4+§5 條目自身內容更深，不是流程效率退步**）+ 2 主章 callout（10 min）+ typo 修正 + 統計更新 + 尾段路線改（10 min）；產出 [appendix-D-why.md](../book/appendix-D-why.md) 從 1175 行擴至 **1657 行（+482 行 / 36% 增量）/ 13 Q&A（13/22 = 59%）** + 2 主章 callout / 5 Q&A links（累計 6 callout / 13 Q&A links）。**Q10-Q13 篇幅：** Q10 95 行（四層理由清單）/ Q11 111 行（四超能力對照表）/ Q12 121 行（三步走 + Fibonacci 例題）/ Q13 156 行（「世紀大夢」連 §6 集大成）= 平均 121 行 / 條，比 S12 平均 108 行長 12%。

**S12 教訓：**
- **「PoC → 風格鎖定 → 批量寫」流程**有效：Q09 PoC 投入 30 min 換來 Q01-Q08 批量 1.5h 風格一致；若直接批量寫完才發現方向不對，浪費更多
- **客製化 callout 比 boilerplate 好**：每章 callout 對應 1-3 條 Q&A，列表式短摘要 + 連結，不複製內容避免重複；每章 hook 圍繞該章節特定動機問題客製化（如 ch01 用「三角形面積公式類比」、ch02 用「秩 1 是線代原子」、ch03 用「Strang 線代地理」）
- **順手修舊 bug**：插入 foreword callout 時順手把「23 個 VizScript」（S10 之前的舊數字）改為「36 個 VizScript（主章 33 + 附錄 3）」— 跨 session 數字一致性問題在這次又現一次（S10 已校正但 foreword 章節摘要遺漏）
- **Memory 規範記憶配合 SOP** — feedback_why_layer.md 是 Claude 個人記憶（跨 session 自動套用）+ SOP §2.13 是專案文件（人類審閱用），兩者互補

**S13 教訓（沿用 S12 流程 + 4 條新增）：**
- **「PoC 後可直接批量」驗證**：S13 跳過 PoC 直接批量 Q10-Q13，4 條共 ~1.5h，無中途 review 風格仍一致 — S12 Q09 PoC 已鎖定的「觸發問題 + 3-layer + 延伸閱讀」schema 在 S13 完全沿用，無需再 PoC。**未來 S14-S15 可繼續跳過 PoC**
- **Q&A 篇幅由「動機問題深度」決定，不固定字數**：Q10 95 行（四層清單型）vs Q13 156 行（集大成連 §6 五大分解）差異 64% 屬正常，**SOP 改為「1000-2500 字」彈性範圍**而非「~108 行 / 1500 字」固定平均
- **callout 客製化 hook 設計：每條 Q&A 對應一個「最具體最有畫面感」的關鍵詞**：ch04 用「行乘列來源 + 不可交換本質」雙 hook、ch05 用「對角矩陣超能力 + (P3) DNA + (P4) 世界觀」三 hook；boilerplate「為什麼這條規則長這樣」泛論寫法被棄用 — hook 越具體越能讓讀者一眼判斷要不要點進附錄 D
- **Q&A 跨章 cross-link 知識網路擴張**：S13 添加 Q10↔Q13（不可交換 ↔ 同時對角化）+ Q11↔Q12↔Q13（對角 ↔ (P3) ↔ (P4)）+ Q12↔Q18（特徵向量正交為穩定性分析乾淨設定）等 ~10 條 cross-link；與 S12 已建立的 Q06↔Q07↔Q08 / Q04↔Q05 三角形成全書 Q&A **密集知識網路**。S14 §6 預計再添 ~6 條（每分解 1 條對應 (P4) 三明治）— 預期形成「**§5 (P4) → §6 五大分解都連回 Q13**」的中央輻射結構

**§2.6 S14 耗時資料點：** ~3.5h / Q14-Q19 §6 6 條 Q&A 批量（2.5h，平均 ~25 min / 條 — 與 S13 持平：分解史線 + 雙路證明 + 完整算驗 + 跨領域對應表都吃時間）+ 6 主章 callout（25 min，平均 ~4 min / callout — 比 S12-S13 的 ~15 min 快，因為 §6 章節結構整齊容易批量 + Q&A 已寫完直接抽 hook）+ 統計更新 + 收尾（35 min）；產出 [appendix-D-why.md](../book/appendix-D-why.md) 從 1657 行擴至 **2740 行（+1083 行 / 65% 增量）/ 19 Q&A（19/22 = 86%）** + 6 主章 callout / 15 Q&A links（累計 12 callout / 28 Q&A links — **全主章 100% 覆蓋**）。**Q14-Q19 篇幅：** Q14 156 行（動機 200 年史 + 6 工程動機表）/ Q15 119 行（CR 雙重讀法 + 3×3 rank 2 小例題）/ Q16 165 行（《九章算術》起源 + 3×3 LU 算驗 + 因果結構表）/ Q17 138 行（Gauss 1801 Ceres + 3×2 Gram-Schmidt 完算 + 條件數哲學）/ Q18 144 行（譜定理雙證明 + 5 物理對稱對應）/ Q19 174 行（雙路徑證明 + 3×2 SVD 教學鏈接 Q17/Q18 + Eckart-Young 1936）= 平均 149 行 / 條，比 S13 平均 121 行長 23%（§6 分解條目需更多歷史 + 算驗 + 跨章 cross-link）。

**S14 教訓（沿用 S12-S13 流程 + 5 條新增）：**
- **「跳順序批量」驗證**：Back 把 6 條 §6 分成兩批指示 Q14, Q15, Q17, Q18 → Q16 + Q19（非順序，Q16 後補）— Edit 操作精準插入仍保持檔案最終按 Q14-Q19 數字順序排列。**經驗：分批指令降低 context 疲勞**（一次 3-4 條而非 6 條）+ **跳順序寫不破壞檔案排列**（只要 Edit 插入定位準確）；未來 S15 可考慮 Q20+Q21+Q22 一氣呵成或分兩批視 Back 偏好
- **小例題巧妙串接 cross-Q 教學鏈**：Q19 SVD 3×2 小例題刻意用與 Q17 同個 $A$（$3 \times 2$ Gram-Schmidt 範例）+ $A^{\mathrm{T}}A$ 正好是 Q18 同個 $2 \times 2$ 對稱矩陣 EVD 範例 — 形成「Q17 QR → Q18 EVD → Q19 SVD」**完整教學鏈**。讀者讀過前面 Q&A 後讀 Q19 會自動感受到「**同一個矩陣三種視角的疊加**」。這個設計是 §6 多 Q 整合的高效模式，未來附錄 Q20-Q22 可考慮類似手法
- **§6 callout 平均 link 數比 §1-§5 高 15%**：§1-§5 6 callout / 13 links（平均 2.17）vs §6 6 callout / 15 links（平均 2.5）— **§6 分解章節因為「統合 §1-§5 多概念」自然需要更多 cross-link**（ch06a 連 Q14+Q11+Q13、ch06e 連 Q18+Q11+Q13、ch06f 連 Q19+Q14+Q08+Q13）。**未來附錄 callout 也預期會多 link 數**（因為附錄本質是「重整合」非「重教學」）
- **Strang LAFE 名言當「鉤子」效果強**：ch06a callout 用「**Make every matrix look diagonal**」（LAFE §6.1 開頭）、ch06f callout 用「**the most important theorem in linear algebra**」（LAFE Ch.7 結論）— 直接用大師直引名言當 hook，比泛論寫法吸引讀者進入附錄 D 強得多。**未來 callout 應主動挖經典名言作為 hook 詞**
- **「雙證明路徑」對 §6 分解 Q&A 是高價值結構**：Q19 SVD 雙證明（譜定理建構性 + Jordan 變分定義）讓讀者從兩個獨立角度確認「為什麼存在」 — 一個給代數證明、一個給幾何直覺。Q18 也用雙證明（不同特徵值正交 + 實特徵值補充）。**§6 分解 Q&A 的「存在性 / 構造性問題」幾乎都適用雙證明設計**，未來 S15 附錄 Q22（解 $A\mathbf{x}=\mathbf{b}$ 為什麼線代核心）也可考慮類似

**§2.6 S15 耗時資料點（背後觀念層收尾 + 全書整合 100% 完成）：** ~3.5h / Q20-Q22 3 條 Q&A 批量（1.5h，平均 ~30 min / 條 — 比 S14 平均 25 min 略長，因為附錄 Q&A 收尾性質強需更多跨 Q cross-ref：Q20 連 Q11/Q12/Q13/Q18、Q21 連 Q03/Q13/Q14/Q19、Q22 是「全書 22 條會師點」連幾乎所有前面 Q&A）+ 3 附錄 callout（10 min）+ BOOK.md 重生（15 min，含 fence-aware awk 合併 17 md + header 12 處數字更新 + 新增 22 Q&A 結構表 + 15 callout 覆蓋表）+ 跨檔 anchor 校驗（10 min，grep 37 條跨檔引用 + 22 錨點對照 + 0 broken）+ SCHEMA §3.6 規範補充（15 min）+ VIZ-CATALOG Appendix D 索引段（15 min）+ 全套收工 SESSION_INDEX/SOP_DRAFT/RETROSPECTIVE/HANDOFF/CURRENT_SESSION.log（30 min）；產出 [appendix-D-why.md](../book/appendix-D-why.md) 從 2740 行擴至 **3522 行（+782 行 / 29% 增量）/ 22 Q&A（22/22 = 100% ✓）** + 3 附錄 callout / 9 Q&A links（累計 15 callout / 37 Q&A links — **全書 16 個內容 md 100% 覆蓋達成 ✓**）+ BOOK.md 從 8650 → **12305 行（+42% 增量）** + SCHEMA §3.6 新規範段 ~110 行 + VIZ-CATALOG Appendix D 索引段 ~40 行。**Q20-Q22 篇幅：** Q20 225 行（200 年史 + 8 類代數推導表 + Normal matrix 統一源頭 + 對偶曲線哲學）/ Q21 246 行（250 年視覺化哲學 + 4 替代方案致命缺陷比較 + 5 層昇華結構主義立場）/ Q22 **311 行（全書最長 Q&A）**（4000 年史 + 6 步從零推導 + 5 種解情境表 + 5 層昇華 + 全書 22 條會師結構表 + Strang「Linear Algebra = the study of Ax=b in all its depth」）= 平均 261 行 / 條，比 S14 平均 149 行長 75%（**附錄 Q&A 收尾性質強，需收束全書脈絡 + 跨領域應用 + 多層昇華**）。

**S15 教訓（沿用 S12-S14 流程 + 6 條新增）：**
- **附錄 Q&A 篇幅顯著比主章 Q&A 大**：S15 平均 261 行 vs S14 平均 149 行（+75%）— 附錄是「重整合」性質，每條 Q&A 需收束多個前面 Q&A 的觀點，自然偏長。**未來如有類似「全書收尾」性質的附錄，預期同樣會有 ~250-300 行 / 條的篇幅，不要強行壓縮**
- **「全書 22 條會師結構」設計 = 收尾 Q&A 的標誌性手法**：Q22 用「Q01-Q21 全表逐條對 Ax=b 關係」作為昇華第 3 層，把全書 21 條 Q&A 串成一個圍繞 Ax=b 的同心結構。**這個「會師表」是「線代核心」這類整本書收尾 Q&A 的標準寫法**，未來若有類似「全書集大成」題目可重用
- **跨檔 Edit 中文字元差異會失敗（半形 vs 全形括號）**：S15 寫 appendix-matrix-world callout 時 old_string 含 `（`（全形）但我貼上 `(`（半形），Edit 失敗 → 重新讀檔取得正確字元級匹配後成功。**未來 Edit 中文檔要嚴格保留原文字元，無法假設括號類型 / 全形 vs 半形差異**
- **BOOK.md 重生不只是合併，要更新 12 處 header 數字 + 新增結構表 + 維護 17 md 邊界**：S15 BOOK.md 重生（沿用 S11 確立的 fence-aware awk 邏輯）成功 = 8650 → 12305 行 + 0 漏網的 fenced `#` 註解被誤改為 heading。**確認 S11 awk 邏輯穩定可重用**：`BEGIN{f=0} /^```/{f=!f; print; next} !f && /^#+ /{sub(/^/, "#"); print; next} {print}`
- **規範化的時機 = 累積 N 次實例後**：S12 確立 3-layer 框架（PoC 1 次）→ S13/S14 沿用（驗證 14 次）→ S15 規範化（寫進 SCHEMA §3.6 標準 = 15 callout 都遵守的格式）。**SOP 規範應在 ~15+ 實例累積後才寫成 SCHEMA 標準**，避免過早抽象（S11 已驗證過：3D 視角規範也是 S12+ 已有 109 處 3D 提及後才在 §3.5 規範化）
- **anchor 校驗用 grep + awk 排序對照 > 人工檢查**：S15 用 `grep -rno "appendix-D-why\.md#q[0-9]*"` 抽取 37 條引用 + `grep -o "{#q[0-9]*}"` 抽取 22 錨點 + 範圍 awk 校驗 → 0 broken。**比 S11 人工 grep 校驗 39 條 `#vizscript-NN` 更系統化**，未來大規模整合校驗應採類似 grep + awk 自動化策略

### 2.14 整合收尾流程二次驗證（S15 延伸 S11 §2.10）

**S15 二次整合收尾（背後觀念層收完 → BOOK.md 重生 + 規範補充）驗證 S11 §2.10 確立的整合 session 流程依然有效，並補 3 條新教訓：**

1. **fence-aware awk 第二次驗證可重用** — S11 awk 邏輯（`/^```/{f=!f; print; next} !f && /^#+ /{sub(/^/, "#"); print; next}`）在 S15 第二次合併（17 md 而非 16 md，加入 appendix-D-why 3522 行新檔）依然完美：22 個 H1 全部正確降為 H3、code block 內所有 `#` 註解保護不誤改、邊界完美。**這是穩定可重用的核心 utility**，未來如有第三次整合（如 S16+ 改版）可直接重用
2. **header 更新比合併更費時** — S15 BOOK.md 重生中：合併 17 md 約 5 min（awk + cat），但 header 12 處數字更新（VizScript 數 / Q&A 數 / 各章新行數 / callout 統計）+ 新增 2 個結構表（22 Q&A 結構表 + 15 callout 覆蓋表）共約 10 min。**整合工時主要消耗在 header 數字一致性維護**，未來如能設計「header 從 source md 自動抽取數字」的工具會大幅加速
3. **規範補充應在收尾整合期一次完成** — S15 同時做 SCHEMA §3.6 規範補充 + VIZ-CATALOG Appendix D 索引段更新 + 全套 SOP/HANDOFF/SESSION_INDEX/RETROSPECTIVE 收工 — 共耗時 30 min。**這 4 件事應綁定在「**最後一個 session 的最後一個動作**」執行**，因為他們都依賴最終穩定狀態的數字（22 Q&A / 15 callout / 37 links / BOOK.md 12305 行 / ...）

**S11 §2.10 + S15 §2.14 整合收尾雙重驗證 ✓** — 這套流程（跨檔 anchor 校驗 → BOOK.md 重生 → 規範補充 → 全套收工）穩定可用，未來如有「**全書又新增一個 Appendix E**」性質的大規模擴充，可直接套用。

### 2.15 Marimo WASM 部署 6 大非顯而易見陷阱（S16 PoC + S17 補充）

**S16 第一個 Python 視覺化 PoC（hello.py + ch01_mv1_poc.py + `marimo export html-wasm` 三階段）發現 3 個本機跑通卻 WASM 失敗的「沉默陷阱」**。每一個都讓我在 S16 多繞 1 個 round-trip 才修對。記入 SOP 讓 S17+ 旗艦實作開工前就避開：**

1. **PEP 723 inline script metadata 是 marimo WASM 額外 deps 的唯一聲明處** — `uv add plotly` 只裝在本機 `.venv/`；export html-wasm 預設只讓 Pyodide 載 `Pygments, docutils, jedi, numpy, parso, pyodide-http`，**plotly / sklearn / Pillow 都不會自動裝**。必須在 notebook 頂端加：
    ```python
    # /// script
    # requires-python = ">=3.12"
    # dependencies = [
    #     "marimo",
    #     "numpy",
    #     "plotly",
    # ]
    # ///
    ```
   marimo export 解析此 block 嵌入 HTML 的 `requirements` 陣列，Pyodide 啟動時用 micropip 自動下載。**S16 沒寫此 block，console 噴 `ModuleNotFoundError: No module named 'plotly'`**。

2. **plotly fig 必須用 `mo.ui.plotly(fig)` 顯式包裝才會在 WASM 渲染** — 本機 marimo edit 跑 bare `fig`（最後一行 `fig` 不接 return）會透過 `_repr_mimebundle_` 自動顯示；但 WASM Pyodide 環境某些版本下沉默不渲染（畫面一片空白、console 沒錯）。**S17+ 旗艦 VizScript 一律使用 `mo.ui.plotly(fig)` 顯式包裝**（同樣 cell 內 `mo` 需加入 closure args）。matplotlib 對應的可用 `mo.mpl.interactive(fig)` 或直接 `fig`（matplotlib 較少踩雷因為 PNG/SVG 走標準路徑）。

3. **首次載入要等 30-60 秒（Pyodide + plotly wheel + plotly.js bundle 三層下載）** — Marimo WASM 首頁啟動順序：(1) 載 pyodide.asm.wasm ~10 MB (2) 從 PyPI/Pyodide CDN micropip install plotly wheel (3) 載 plotly.js bundle。**讀者第一眼看到空白頁很容易誤判「壞了」**（S16 Back 就誤判一次）。
    - **UX 規範：** 首頁 / VIZ-CATALOG / BOOK.md 在連結 deployed page 處，要附「⏳ 首次載入請等 ~30s，直到看到 plotly 圖出現再操作」說明
    - **替代方案：** marimo 0.24+ 可開 `loading-indicator` 顯示載入進度條（待 S17+ 驗證）

**S16 對 S17+ 影響：旗艦 VizScript 開工 checklist**：
- [ ] notebook 頂端 PEP 723 block 包含所有非預設 dep（plotly / sklearn / Pillow / scipy 視 VizScript 需要）
- [ ] 所有 plotly fig 包 `mo.ui.plotly(...)`
- [ ] reactive cell 內 `mo` 加 closure args
- [ ] WASM export 後 console 必看：(1) 載入順序中是否含目標套件 (2) 是否有 `ModuleNotFoundError` (3) 是否有 cell exception
- [ ] 部署頁 README / 首頁加「30s 首次載入」說明

---

**S17 補充：3 個 marimo 跨 cell / plotly 細節陷阱（ch04 V-02 母模板開工 debug 過程中發現）**

S17 第一次寫真正多 cell × multi-subplot × multi-heatmap 的 notebook 就踩了 3 個本機 import 測試看不出來、要實際跑 marimo runtime 才會炸的坑：

4. **marimo 把底線開頭的 cell variable 視為 cell-private 不跨 cell export** — 我把 helper 函數命名為 `_accumulate / _layer_energy / _layers_of` 從 helper cell `return`，下游 cell 引用時全部 NameError，整個 cell 沉默 errored 而不渲染（瀏覽器只看到部分 cell，console 沒明顯 traceback 因為「未渲染」不是「exception」）。
    - **規則：** 跨 cell 共用的函數 / 變數 **絕不可以 `_` 開頭**。如 `_helper`, `_const` 等命名都會被 marimo 視為 cell-local。
    - **變通：** 要嘛改命名（`accumulate` 而非 `_accumulate`），要嘛把 helper 與唯一使用者合併同一 cell（推薦，最穩、最少依賴 marimo 跨 cell magic）
    - **症狀：** WASM 部分 cell 不渲染、console 看 `kernelMessage` 沒明顯 error → 翻 cell python 文件查 NameError

5. **plotly `make_subplots(subplot_titles=[""] * k)` 空字串會被跳過不生成 annotation slot** — 我寫 `subplot_titles=[""] * k` 想用佔位、後置 `fig.layout.annotations[p].text = "..."` 動態填內容，**結果空字串被 plotly 視為「沒標題」直接 skip，annotations tuple 是空的**，IndexError tuple index out of range。
    - **規則：** plotly 對空字串 `""` 與 `None` 都跳過，**只有非空字串才生成 annotation slot**。
    - **變通：** 要嘛直接在 `make_subplots` 傳入完整最終 title（不後置改），要嘛用 placeholder 非空字串 `[" "] * k` 或 `[f"slot_{p}" for p in range(k)]` 保留 slot
    - **症狀：** WASM console STDERR `IndexError: tuple index out of range` 指 `strip.layout.annotations[p].text = ...`

6. **plotly heatmap `z` 參數最好 `np.asarray(M, dtype=float)` 包一層** — 我傳 plain Python `[[0]]` 進 helper `_add_heatmap`，helper 內 `abs(M).max()` 直接炸 `TypeError: bad operand type for abs(): 'list'`（list 沒有 `.max()`，Python 內建 `abs()` 也不接 list）。本機如果 `M` 是 numpy array 就過了，但臨時用 list 當 dummy 時會炸。
    - **規則：** helper 函數開頭一律 `M = np.asarray(M, dtype=float)` 保護，不假設 caller 一定傳 numpy
    - **變通：** 同時把 `abs(M)` → `np.abs(M)`、`abs(error)` → `np.abs(error)` 用 numpy 介面而非 Python builtin
    - **症狀：** WASM console STDERR `TypeError: bad operand type for abs(): 'list'`

**S17 對 S18+ 影響：擴充 checklist**：
- [ ] 跨 cell 共用的函數 / 變數命名不可 `_` 開頭
- [ ] plotly `subplot_titles` 不可傳空字串，要嘛預先計算完整 title、要嘛 placeholder 非空字串
- [ ] heatmap helper 內 `M = np.asarray(M, dtype=float)` 保護
- [ ] `abs()` → `np.abs()` 用 numpy 介面

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
| 0.7 | 2026-05-12 | S06：§2.6 補 §5 耗時資料點（1h / 830 行 / 4 圖獨立 / 6 Pattern / 4 VizMark） + 4 觀察：HANDOFF Pattern 數量需對 PNG 重核（P4 漏掉）/ 多圖小章節 vs N-way 單圖章節耗時相當 / 「Tier 1 + pointer」策略首次驗證可省篇幅與工時 / 對偶 Pattern 用對偶總表節省 ~40% 描述篇幅 |
| 0.8 | 2026-05-12 | S07：§2.6 補 §6 總覽 + §6.1 耗時資料點（2h / 876 行 / 兩章 session 模式）+ 4 觀察：兩章 session 模式可行（總覽短章 + 主章合 session 省 0.5h）/ 原書 PNG `using P1` / `using P2` 標記是跨章連結官方鐵證 / 雙 pointer VizScript 設計可行（同時指 ch04 + ch05）/ 對偶兩張圖（列視角 + 行視角）是 §6.1–§6.5 全書一致模式 |
| 0.9 | 2026-05-12 | S08：§2.6 補 §6.2 LU + §6.3 QR 耗時資料點（2.5h / 1195 行 / 主章 + 主章模式）+ 5 觀察：`using XX` 標記譜系擴大至 MM4（LU2 標 MM4、QR 標 P1、LU1 無標）/ 「單 pointer」設計比「雙 pointer」更常見（PNG 標什麼就指什麼）/ 分解章篇幅由「應用面廣度」決定（LU 解方程 + QR 最小平方使 LU > CR > QR）/ 3D 投影視覺是 QR 章獨有需求（matplotlib 3D / plotly 3D 必備）/ 「主章 + 主章」模式驗證可行（2.5h / 1195 行，比兩 session 省 0.5h）|
| 0.10 | 2026-05-12 | S09：§2.6 補 §6.4 EVD + §6.5 SVD 耗時資料點（3h / **1629 行**，**SVD 章 934 行為全書最長**）+ 6 觀察：(1) **「雙 pointer 復活」判準明文化** — 雙條件「PNG 標記 + 內容旗艦同根」雙成立才升級雙 pointer（SVD 例：標 P4 + 內容與 ch04 Mona Lisa 同根 → 雙 pointer 主 ch04 + 副 ch05）/ (2) **§6.x 章節 PNG `using XX` 標記最終地圖（S07-S09 累積）：** CR1=P1 / CR2=P2 / LU1=無 / LU2=MM4 / QR=P1 / EVD=P4 / SVD=P4（共 7 圖、5 種標記）/ (3) Tier 3 主 VizScript 首次出現在 §6（SVD VizScript-01 是全書第二支 Tier 3，與 ch04 VizScript-02 並列「核心骨架雙旗艦」）/ (4) 分解章「應用面廣度」規律進一步驗證 — SVD 五層內容（4 應用 + Eckart-Young + 4 子空間 + 雙 pointer + Tier 3）使 934 行為全書最長 / (5) §6 主章序列篇幅比例 1.0:1.20:0.99:1.28:**1.71** — SVD 是「§1–§6 全書集大成終章」/ (6) §6 章節雙 pointer 設計地圖規律：對偶兩張圖（CR）+ 集大成章（SVD）採雙 pointer，單張圖且非集大成章採單 pointer |
| **0.11** | 2026-05-12 | **S10 §1–§6 全書內容 100% 完成，附錄 + 散文章節收尾**：§2.6 補 S10 耗時資料點（**~2.5h / 1290 行 / 5 個檔案（Foreword 158 + Conclusion 198 + Map of Eigenvalues 272 + Matrix World 328 + Four Subspaces 334）/ 3 VizMark（1 Tier 2 旗艦 + 2 Tier 1）**）+ 7 觀察：(1) **附錄 PNG 重核發現新規律：3 張附錄 PNG（MapofEigenvalues / MatrixWorld / 4-Subspaces）皆無 `using XX` 標記** — HANDOFF 預估「MapofEigenvalues 可能標 P3」推翻；附錄 PNG 是「**地圖層級 / 基本概念圖**」非「Pattern 套用層級」，標記譜系與主章 §6.x 不同 / (2) **「附錄重整合 vs 主章重教學」雙模式確立** — 附錄 3 個 VizMark 都採「pointer 到主章 VizScript」策略，不重複實作（map → ch06e、4-subspaces → ch03 V-02 + ch06f V-03、Matrix World 旗艦 → 跨全書索引）/ (3) **「Matrix World 互動式索引地圖」首次升級為 Tier 2 旗艦** — appendix-matrix-world V-01 設計為「全書互動式教材的首頁」（S12+ 完成後讀者進入教材的標準入口），與 [ch06a V-01](docs/book/ch06a-five.md#vizscript-01) 五分解 dashboard 互補（前者分類學索引、後者分解視覺索引）/ (4) **back-conclusion.md 新增「全書 33 個 VizScript 總覽」段**（原書無此章）— S11 整合 BOOK.md / VIZ-CATALOG.md 的橋樑；§1–§6 主章 33 + 3 附錄 = 全書 36 個 VizScript / (5) **VizScript 數誤算發現** — HANDOFF 多 session 累積寫「23 VizScript」實為 33（漏算 ch03/ch04/ch05 各 4 個 = 12 個，少數 ~10）；S10 校正並寫進 conclusion.md。**教訓：HANDOFF 數字一致性需 S11 整合時 grep 校驗** / (6) **散文章節耗時規律：兩個散文檔（Foreword 158 行 + Conclusion 198 行）共 ~0.6h** — 主要工時在 Conclusion 的 33 VizScript 總覽表，Foreword 純翻譯 + 導讀很快 / (7) **附錄章節耗時規律：3 個附錄共 ~1.5h / 934 行**（map 272 + matrix-world 328 + 4-subspaces 334），其中 Matrix World 旗艦 VizScript（13 段 A-M）吃 ~0.5h；附錄「重整合 vs 主章重教學」模式讓篇幅 / 工時比主章節省 ~30%；3 附錄平均 311 行 / 50 min，比主章節 ~700 行 / 1.5h 高效。**S10 對 S11 影響：** §1–§6 全書內容章節 100% 完成（13 個 md 檔 + 36 個 VizScript + ~8100 行），下階段轉入「校對 + 整合 + 風格統一」（S11 預估 1.5h，主要工作是寫 BOOK.md + VIZ-CATALOG.md + 跨檔案 anchor link 校驗）|
| **0.12** | 2026-05-13 | **S11 整合 + 校對 + 統一 5 項任務完成**：耗時 ~2h / 產出 BOOK.md 8650 行 + VIZ-CATALOG.md 241 行 + SCHEMA §3.5 全書視覺錨點段 + 23 處 sed 修正 + .gitignore 防護；**新增 §2.10「整合 session 流程」**（5 任務順序 + 教訓含 fence-code-aware awk + macOS sed `\b` 不支援 + 3D 視角預設規範補入）+ **§2.11「跨 session 大數字一致性校驗」**（HANDOFF 23→36 + conclusion 33→36 教訓融合）+ **§2.12「兩層級版權檔管理」**（PDF 不 push + md 內可大段引用）|
| **0.13** | 2026-05-13 | **S12 背後觀念層啟動 — appendix-D-why.md 9/22 Q&A 完成 + 4 主章 callout + memory feedback_why_layer.md**：耗時 ~2.5h / 產出 appendix-D-why.md 1175 行（9 Q&A 含 Q01-Q08 批量 865 行 + Q09 PoC 310 行）+ 4 主章 callout（foreword / ch01 / ch02 / ch03，共 8 Q&A links）+ memory + foreword 23→36 bug 修；**新增 §2.13「背後觀念 3-layer 框架」**（① 歷史 + ② 設計過程還原 + ③ 概念昇華 規範 + 方案 D 雙層落點 + Q&A 間 cross-link 知識網路 + S12 4 條教訓含「PoC → 風格鎖定 → 批量寫」流程 + 「客製化 callout 優於 boilerplate」+ 「順手修舊 bug」+ 「memory + SOP 互補」）+ §2.6 補 S12 耗時資料點 |
| **0.14** | 2026-05-13 | **S13 背後觀念層續寫 §4 + §5 — Q10-Q13 共 4 條 Q&A + ch04 + ch05 主章 callout**：耗時 ~2h / 產出 appendix-D-why.md 從 1175 行擴至 **1657 行（+482 行 / 36% 增量）/ 13 Q&A（13/22 = 59%）**（Q10 不可交換 95 行 / Q11 對角矩陣 111 行 / Q12 (P3) 動態預測 121 行 / Q13 (P4) 三明治 156 行）+ 2 主章 callout（ch04 Q09+Q10 / ch05 Q11+Q12+Q13 共 5 links）+ ch05 typo 修；**§2.6 補 S13 耗時資料點 + §2.13 補 S13 4 條教訓**（「PoC 後可直接批量」驗證、「Q&A 篇幅由動機深度決定」彈性化、「callout 客製化 hook 比泛論具體」、「Q&A 跨章 cross-link 知識網路擴張」） |
| **0.15** | 2026-05-13 | **S14 背後觀念層續寫 §6 — Q14-Q19 共 6 條 Q&A + ch06a-ch06f 6 主章 callout**：耗時 ~3.5h / 產出 appendix-D-why.md 從 1657 行擴至 **2740 行（+1083 行 / 65% 增量）/ 19 Q&A（19/22 = 86%）**（Q14 分解動機 156 行 / Q15 A=CR 119 行 / Q16 A=LU 165 行 / Q17 A=QR 138 行 / Q18 譜定理 144 行 / Q19 SVD 174 行）+ 6 主章 callout（ch06a Q14+Q11+Q13 / ch06b Q15+Q14 / ch06c Q16+Q14 / ch06d Q17 / ch06e Q18+Q11+Q13 / ch06f Q19+Q14+Q08+Q13 共 15 links）— **全主章 100% 覆蓋（12 callout / 28 Q&A links）**；**§2.6 補 S14 耗時資料點 + §2.13 補 S14 5 條教訓**（「跳順序批量可行」+「小例題巧妙串接 cross-Q 教學鏈」Q17→Q18→Q19 同 $A$ + 「§6 callout 平均 link 數比 §1-§5 高 15%」+「Strang LAFE 名言當鉤子效果強」+「雙證明路徑對存在性 Q&A 高價值」）|
| **0.16** | 2026-05-13 | **S15 背後觀念層收尾 + 全書整合 100% — Q20-Q22 + 3 附錄 callout + BOOK.md 重生**：耗時 ~3.5h / 產出 appendix-D-why.md 2740 → **3522 行（+782 / 22 Q&A 100% ✓）**（Q20 特徵值地圖 225 行 / Q21 Matrix World 同心橢圓 246 行 / Q22 Ax=b 線代核心 311 行 = 全書最長 Q&A）+ 3 附錄 callout（map-eig Q20+Q18+Q11 / matrix-world Q21+Q14+Q19 / four-subspaces Q22+Q08+Q19 共 9 links）→ **全書 15 callout / 37 Q&A links / 16 內容 md 100% 覆蓋** ✓ + BOOK.md 8650 → **12305 行（+42%）** + SCHEMA §3.6 規範 + VIZ-CATALOG Appendix D 索引；**新增 §2.14「整合收尾流程二次驗證」**（fence-aware awk 重用 + header 更新比合併費時 + 規範補充綁定收尾整合期 3 條教訓） |
| **0.17** | 2026-05-13 | **S16 Marimo 技術棧 PoC — Python 視覺化實作起步**：耗時 ~2.5h / 產出 viz/ 目錄（7 檔追蹤 + .venv/dist gitignore）含 uv + Python 3.12 + marimo 0.23.6 + plotly 6.7 + matplotlib 3.10 + sklearn 1.8 + Pillow 12.2 完整技術棧 + hello.py（Stage 1 reactive slider 4 cell）+ ch01_mv1_poc.py（Stage 2 6 slider × plotly 2D × (Mv1)+(Mv2) 雙觀點 7 cell）+ marimo export html-wasm 27 MB static dir（Stage 3 部署驗證）；**新增 §2.15「Marimo WASM 部署 3 大非顯而易見陷阱」**（PEP 723 metadata 是 WASM dep 唯一聲明處 + plotly 必須 mo.ui.plotly(fig) 顯式包裝 + 首次載入 30-60s UX 警告）+ S17+ 旗艦開工 5 條 checklist；下次 S17 從 VIZ-CATALOG 首批 Tier 3 旗艦（ch04 V-02 母模板 或 ch06f V-01 SVD Master）開始 |
