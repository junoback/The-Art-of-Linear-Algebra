# Session Retrospective — Back ↔ Claude 對話反思

> **用途**：累積每次 session 結束時的對話過程反思，幫助 Back 與 Claude 找出更快、更精準的協作模式。
> **更新者**：Claude（每次 session-end 流程的第 6 步自動追加）
> **維護原則**：每次 session 一條，按時序追加，不刪除歷史。

---

## S00–S01 — 專案啟動 + md 化規劃 + 機械轉換（2026-05-11 ~ 2026-05-12）

### 本 session 主軸
S00 從 GitHub clone《The Art of Linear Algebra》並啟用跨 session 管理；S01 對齊整體 10-session 路線圖，並完成機械轉換（pandoc / pdftotext / gs）+ SCHEMA 與章節骨架，為 S02 起逐章撰寫做好基礎。

### 對話低效時刻
- **「請幫我把這個跑起來」初解讀偏離**：Claude 一開始把 repo 當「程式專案」推測要安裝執行環境，沒先看 README + makefile 就花了一輪檢查工具。實際 repo 是 LaTeX 文檔，PDF 已存在，「跑起來」= 打開 PDF。原因：沒先 `cat README.md && cat makefile`，假設過早。**下次先讀 README 與 makefile 再規劃**。
- **「3. 先做2的版本」歧義未確認就做大決策**：使用者簡短回「3. 先做2的版本」，Claude 解讀為「先做 2 個（英+簡中）版本」並寫進 HANDOFF；但另一種合理解讀是「先做（建議的）方案 2」之類，工作量差很多（雙語 vs 單語）。原因：Claude 認為已有合理解讀就動工，沒短訊確認。**下次遇短回應 + 多個合理解讀 → 先用一句話確認再動工**。

### 建議 Back 下次這樣問會更快
- **針對「跑起來」這類動詞**：你說「請幫我把這個跑起來」之前，可以一句話補上「跑起來」對你的意思（執行程式 / 編譯 PDF / 打開現成的成品 / 啟動互動 demo）。理由：少 1 個推測回合，Claude 可直接動到對的方向。
- **針對多選題回應**：之前回「3. 先做2的版本」，下次可寫「英+簡中兩個版本都做」或「只做英文版」這類完整短語。理由：避免 Claude 用「選項編號」反推，誤解風險更低。

### Claude 自我提醒
- **第一次接觸陌生 repo → 先 `cat README + cat makefile + ls -la` 才推測專案性質**，不要先跳 `which <tool>`。
- **使用者多選題簡短回答（編號 / 兩字片語）**：先重述一遍「我理解你是說 X，要動工囉」再做大決策，特別是工作量會放大的決策（雙語 vs 單語、全章 vs 單章）。
- **跨 session 專案啟動時 → 第一步 `git remote -v` 看上游**，避免後續收工 commit 推錯位（S01 收工時才發現 origin 是上游 junoback）。
- **工具替代鏈要主動列**：S01 poppler 沒裝時自動用 gs txtwrite 替代沒阻塞，這是對的；今後遇任何「主工具缺」先盤點替代，不乾等 brew。

---

## S01.5 — 視覺化規範補規劃（2026-05-12）

### 本 session 主軸
S01 收工後，使用者提出新需求「閱讀章節時同步標記視覺化機會 + 寫劇本提示詞」。Claude 評估工作量後給 3 方案，使用者選方案 A（整合）+ VizScript 細緻度升一級到 ~800 字。S01.5 寫 `VIZ_SCHEMA.md`（VizMark 5 型 + VizScript 13 段格式 + 範例）、微調 SCHEMA、重寫 _merged.md、修訂路線圖 S02-S11。

### 對話低效時刻
- **第一次給 VizScript 範例時偏粗（~350 字）**：Claude 沒先確認細緻度標尺就拋出範例，使用者馬上回「太粗」需細一級。原因：Claude 用「中等」直覺給樣板，沒先列出三檔細緻度光譜讓使用者標位。**下次給「需要使用者校準的標尺類設計」（劇本長度、描述深度、互動深度），先列 3 檔光譜（粗/中/細，配字數與工時）讓使用者勾選，再寫範例**。
- **方案分析時 Claude 自己已經偏好「方案 A」並寫進建議**：使用者最後也選 A，沒繞路。原因：合理推薦不算低效。但需注意未來若使用者覺得「你問前已經誘導我選 A 了」，可改為先給 3 方案中性比較表再表達偏好，避免錨定效應。

### 建議 Back 下次這樣問會更快
- **針對「細緻度 / 深度」類選擇**：之前你回「太粗需要再細一級」，下次可直接寫「目標約 800 字 / 個」或「需要包含驗收條件、配色 hex、邊界 case」這類具體要求。理由：Claude 不用猜「再細一級」是 +30% 還是 +200%，直接命中。
- **針對「重新規劃」這類大動作**：之前你說「請你重新計劃」，下次可補上重新規劃的觸發點（新需求 / 工作量擔憂 / 進度卡關），Claude 可保留前次合理部分、只改觸發點影響的範圍，不必整個推倒。本次因有明確新需求（「在記號旁準備劇本提示詞」），Claude 自然知道改哪裡；但若觸發點不清就會有重做風險。

### Claude 自我提醒
- **「細緻度標尺」類設計先列 3 檔光譜**：劇本長度（150/350/800 字）、描述深度、互動深度都該如此。用使用者語言：「你想要 A 級（給人讀就好）/ B 級（給工程師參考）/ C 級（給 LLM 直接生程式）」。
- **重新規劃時保留前次合理決策**：先把已定的決策列出來「不變動的有 X、Y、Z」，再列「會改的是 A、B、C」，使用者可即時阻止錯誤的「保留」與「改」。本次直接重寫路線圖沒先列「保留項」，幸好沒踩到。
- **800 字 VizScript 範例的副作用**：可能讓未來章節 session 工作量壓力大。S02 結束後立即評估「實際做一章下來真實時間 vs 估計 1.5 session」，必要時回頭調 VIZ_SCHEMA 細緻度（不要硬撐 800 字標準）。
- **「方案 A」推薦不能變成「不容質疑」**：S02 第一章結束後若實作起來不順，要主動提「方案 B / C 是否更合適」，不要因為已寫進 HANDOFF 就堅守。

---

## S06 — §5 實用模式 + Tier1+pointer 省篇幅策略首例（2026-05-12）

### 本 session 主軸
Back 開場 `開始`，session-init 後直接 `直接動手寫 ch05`。Claude 平行抓 §5 素材（en/zh + 4 張 PNG）發現 HANDOFF 列的「5 個 Pattern」漏掉 P4（$U\Sigma V^{\mathrm{T}}$ 三明治），改為 6 Pattern + 4 圖一氣寫成 830 行；驗證「Tier 1 + pointer」省篇幅策略（VizScript-03 指向 ch04 VizScript-02）。

### 對話低效時刻
- **起手沒對 PNG 重核 Pattern 數**：S06 起步時若先 grep `Figure` 數量或先讀 4 張 PNG 再開寫，會更早發現 P4，不會在心中先按 5-Pattern 結構暫存後再改 6-Pattern。實際影響不大（讀素材階段就修正了），但這是「先讀 HANDOFF 就動工 vs 先驗 HANDOFF 對 PNG 再動工」的取捨。SOP §2.6 已寫進「HANDOFF 章節描述需對 PNG 重核」當作 S07+ 鐵則。原因：信任前 session 的記憶 > 直接看原檔，這個信任默認應該倒過來。

### 建議 Back 下次這樣問會更快
- 無建議 — 本 session Back 三句指令（`開始` / `直接動手寫 ch05` / `commit + push origin main`）都極精準，無歧義空間。

### Claude 自我提醒
- **章節 session 起手第一步**：`ls figs-png/ | grep <主題>` + 多模態讀全部相關 PNG，**先確認 figure 數與內容**，再開始套 HANDOFF 預估的結構 — HANDOFF 是「上次 session 結束時的快照」，原書是「ground truth」，衝突時信原書。
- **「Tier 1 + pointer」策略**現已驗證可行（VizScript-03 約 100 行 vs Tier 3 估 200+ 行）。S07–S09 §6 五大分解每章都該主動套用此策略：(MM4) 累加 demo 統一指向 ch04 VizScript-02、(P4) 三明治結構統一指向 ch05 VizScript-03，章內只寫各分解的「特殊性質」demo。不要因為「想顯得章節 self-contained」而重做累加動畫。
- **對偶 Pattern / 對偶結構優先用對偶總表**（3 列 × 4 欄）而非兩兩獨立寫描述 — 節省篇幅且讀者對照更直觀，§6 5 大分解若出現對偶（如 $A=LU$ 與 $A=L^{\mathrm{T}}DL$）即套用。

---

## S10 — Foreword + Conclusion + 3 附錄收尾（§1–§6 全書內容 100%）（2026-05-12）

### 本 session 主軸
Back 開場 `開始`，session-init 後 `依照順序開始 S10`。Claude 按 HANDOFF S10 起步建議 5 步驟（先 PNG 重核 → 抓素材 → 順序撰寫 5 個檔）完成 1290 行 / 3 VizMark。**§1–§6 全書內容章節 100% 完成里程碑達成**（13 個 md 檔 + ~8100 行 + 36 個 VizScript）。

### 對話低效時刻
- **HANDOFF 累積錯誤晚到 S10 才校正**：S07–S09 三次 session 都寫「全書 23 VizScript」，實際是 33（主章）。Claude 動筆 Conclusion「全書 X 個 VizScript 總覽」時才 grep 校驗發現錯誤。原因：HANDOFF 數字 = 上次 session 的快照，沒人手動 grep 校驗就會跟著錯下去；應該在 S07/S08/S09 任何一次 session 起步時 `grep "^### VizScript-" docs/book/ch0*.md | wc -l` 一次驗證。**已寫進 SOP §2.6 S10 觀察 5：「HANDOFF 數字一致性需 S11 整合時 grep 校驗」**，但其實 S07 起就該如此。

### 建議 Back 下次這樣問會更快
- 無建議 — 本 session Back 兩句指令（`開始` / `依照順序開始 S10`）+ 收工指令都極精準，HANDOFF 中 S10 起步建議寫得詳細所以幾乎不需追問。

### Claude 自我提醒
- **HANDOFF 中的「累積統計值」（如 VizScript 總數、總行數、章節數）每次 session 起步時 grep 一次驗證**，不要信任上次 session 的記憶。`grep -c "^### VizScript-" docs/book/*.md` + `wc -l docs/book/ch*.md` 各執行一次只花 5 秒，但可預防 HANDOFF 數字錯誤跨多 session 累積。
- **「整合性附錄」VizMark 設計優先採 pointer 策略**（如本次 4-subspaces 指 ch03 V-02 + ch06f V-03、map-eigenvalues 指 ch06e V-01），不重複實作主章已完成的 VizScript。但「跨全書索引地圖」類附錄例外（如 Matrix World 升 Tier 2 旗艦），因為它是「整合本身的視覺化」而非「pointer 到別處」。
- **附錄章節 PNG 標記譜系與主章不同**：S10 確認 3 張附錄 PNG 皆無 `using XX` 標記（HANDOFF 預估 MapofEigenvalues 標 P3 推翻）— 附錄是「地圖層級 / 基本概念圖」非 Pattern 套用層級。未來其他類「整合 / 概覽 / 索引」附錄起手前也該預期「無 using 標」為常規。

---

## S11 — 整合 + 校對 + 統一 session 5 項任務 100% 完成（2026-05-13）

### 本 session 主軸
Back 開「依照建議順序」執行 S11 整合 session：(3) anchor 校驗 → (5) 一致性 → (1) BOOK.md → (2) VIZ-CATALOG.md → (4) 風格統一。最後達成全 5 項任務 + 額外處理 Strang 8 本版權 PDF 防護 + memory feedback。

### 對話低效時刻（具體事件 + 為什麼）

- **BOOK.md 第一輪生成誤改 Python code block 內 `# 註解` 為 `## heading`**：Claude 第一輪用 `sed 's/^#/##/'` 對 16 個 md 統一降一級，沒考慮到 ch06e 有 Python code block 內含 `# 參數化單位球` / `# plotly Surface 渲染` 等註解，造成 BOOK.md 出現 4 個錯誤的一級 heading（root + 3 個 Python 註解）。原因：**Claude 假設 markdown 工具一律安全，沒先想到 sed 不認 fence code block**。發現後馬上用 awk fence-aware 重做就解了，但浪費 1 輪生成 + 驗證 → 教訓進 SOP §2.10。

- **macOS BSD sed 不支援 `\b` word boundary**：Claude 第一輪 sed 用 `s/([0-9]) ms\b/\1ms/g` 處理空格不一致，結果只清了一半（ch*.md 部分 OK 但 appendix-*.md 13 處仍在）。原因：**Claude 用 GNU sed 習慣寫 `\b`，沒驗證 macOS BSD sed 是否支援**。改用無 boundary 的 `([0-9]) ms` 就解了 → 教訓進 SOP §2.10 第 5 點。

- **VIZ-CATALOG 設計問 Back「抽取 vs 留原處」**：Back 問「抽取出來跟放在原處，哪樣對後續視覺化比較容易對上位置？」Claude 回得不錯（兩個都需要 + 角色不同），但其實這個問題的答案在 HANDOFF S11 起步建議裡已暗示（catalog 是「metadata 索引」+ 原 md 是「實作詳情」），Claude 應主動先點出此設計再問選項。

### 建議 Back 下次這樣問會更快

- **複雜 schema / 大檔合併任務**：之前 Back 說「(1) BOOK.md 合併，從 a（完整合併單檔）」很精準，沒可改善處。但若想避免 Claude 用 sed 踩 code block 坑，可預先說「合併時注意 ch06e 內有 Python code block，不要誤改 `# 註解`」— 但這是 Claude 本應預想到的，不該 Back 提醒。
- **數字一致性校驗**：S10 + S11 連兩次發現 HANDOFF 累積數字錯誤（23→33→36 + 33→36），下次可在 session 啟動時主動跟 Claude 說「先 grep 一次 VizScript 計數」當作 warm-up — 但這也已寫進 SOP §2.11，Claude 應自動做。

### Claude 自我提醒（不需 Back 督促也該做的事）

- **markdown 大規模處理前先 fence-aware**：BOOK.md 合併 / 跨檔 sed 修正類任務，**第一輪就用 awk 追蹤 ``` fence 狀態**，不要先用 sed `^#` 圖方便；發現問題回頭重做浪費 cache + 時間。
- **macOS BSD sed 不認 GNU 擴展 (`\b` / `\w` / `\s` 等)**：寫 sed 前先確認 OS + sed 版本；複雜 pattern 用 `LC_ALL=en_US.UTF-8 sed -E` 處理 UTF-8 多字節字符。或乾脆用 Python 替代 sed 做大規模修改。
- **整合 session 一律 grep 驗證大數字**：HANDOFF 寫的「~8100 行 / 36 VizScript / 16 個 md 檔」等不要當作真實，session 起步 5 秒 grep 驗證一次（`grep -cE "^### VizScript-" docs/book/*.md` + `wc -l`）。
- **設計問題先給推薦再列選項**：當 Back 問「A vs B 哪個對 X 較容易」時，先給推薦理由 + 點出 A/B 是補充而非替代（如果是）+ 列選項，比純列選項更高效；S11 VIZ-CATALOG 那輪我做了，但 BOOK.md a/b/c 選項那輪我列了 3 個沒先點出推薦，Back 還是選了 a（推薦項）— 表明推薦是有用的訊號。

---

## S12 — 背後觀念層啟動：22 條 Q&A 規劃 + Q09 PoC + 批量 Q01-Q08 + 4 主章 callout（2026-05-13）

### 本 session 主軸

Back 提出全書缺一個系統性「為什麼這條規則長這樣」維度（13 個主章只講「怎麼算」缺「為什麼這樣算」），用 Cayley 1858 矩陣乘法為什麼是「列乘行」的 Q&A 範例展示 3-layer 模板。S12 完成方案 D（主章 callout + 附錄 D 詳盡 Q&A）確立 + 22 條 Q&A 全書清單 + Q09 PoC + 批量 Q01-Q08 + 4 主章 callout 插入 + memory feedback_why_layer.md 規範化。最終達成 appendix-D-why.md 1175 行 / 9 Q&A（41% 進度）+ 4 callout / 8 links + 1 memory。

### 對話低效時刻（具體事件 + 為什麼）

- **SESSION_INDEX.md S12 行插入位置錯誤**：執行收工 Step 4 時 Claude 用「S11 行」作 Edit anchor，把 S12 行插在 S11 **之前**（時序錯）。原因：**Edit 操作沒驗證表格末尾位置**就直接 anchor 在 S11 行。發現後用「Edit 還原 S11 行 + Bash cat >> 追加 S12 在末尾」修復 → **教訓：表格追加行應該用 Bash `cat >> file` append 而不是 Edit anchor 中間行，避免插入位置錯誤**。

- **Q04 Markdown 表格中 `|` 符號未跳脫造成 anchor 不 unique**：S12 第一次 Edit 目錄表狀態時，old_string 用半形 `?` 結尾但檔案實際是全形「？」— 一輪 Edit failed。**原因：Claude 鍵入時習慣半形 `?` 但檔案是中文全形「？」**。Re-read 檔案實際內容後修正成功 → **教訓：Edit 帶中文標點符號時，先 Read 一次原檔對照 unicode 字元，不要憑記憶輸入**。

### 建議 Back 下次這樣問會更快

- **「先草擬一條 Q09」這類精準指令很高效** — Back 在我給 22 條清單 + 7 個 review 問題時直接回「先草擬一條 Q09」（PoC 優先），讓 Claude 不必先逐條對齊清單；風格鎖定後一句「若風格 OK」直接觸發 Q01-Q08 批量寫。**未來類似多 session 任務可沿用此 pattern**：先 1 條 PoC 對齊風格 → 確認後批量 → 不必每條 review。
- **「S12 是否繼續做 callout」這種 yes/no 問題比「下一步建議」更精準** — Claude 給三選項（繼續 / 收工 / 中間方案）時，Back 用最短回答「是否繼續做 callout」直接觸發動作，避免 Claude 過度展開選項解釋。

### Claude 自我提醒（不需 Back 督促也該做的事）

- **表格追加用 Bash `cat >> file` 而非 Edit anchor**：本 session SESSION_INDEX.md 已踩這個雷一次 — 表格末尾追加應該 `cat >> file << 'EOF' ... EOF` 直接 append，比 Edit「某行之後」更安全（不會插錯位置）。
- **Edit old_string 含中文標點時先 Read 對照**：別憑記憶輸入「？」、「，」、「：」等，可能是全形也可能是半形。Read 一次原檔取得精確字元再 Edit。
- **memory + SOP 是互補不是替代**：feedback_why_layer.md（memory）= Claude 跨 session 自動套用的個人規範 / SOP §2.13 = 專案級別 process discipline（人類審閱）/ HANDOFF = 當下 session 的工作狀態。三者各司其職不要混。本 session 同時更新 3 處保證下次 S13 Claude 不論從哪個入口都能恢復 context。
- **批量寫長文時，每條條目寫完立即記憶大綱要點到 log**：S12 批量 Q01-Q08 8 條約 865 行，最後寫 HANDOFF / SOP 時要 cross-ref 各條重點（行數 / 3-layer 涵蓋 / 經典引用），若沒在每條寫完當下記到 CURRENT_SESSION.log，最後要再 grep 各檔案統計 — 浪費 cache。**未來批量寫多條 Q&A 時，每完成一條立即在 log 追加一行 metadata（標題 / 行數 / 3-layer / 關鍵亮點）**。

---
