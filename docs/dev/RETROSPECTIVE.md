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

## S13 — 背後觀念層續寫 §4 + §5：Q10-Q13 + 2 主章 callout（2026-05-13）

### 本 session 主軸

Back 用一句話「§4 + §5 共 4 條 Q&A + 2 主章 callout」直接觸發批量寫。Claude 沿用 S12 已驗證的 PoC-鎖定流程跳過 PoC 直接批量產出 Q10（不可交換 AB≠BA 95 行）+ Q11（對角矩陣 111 行）+ Q12（(P3) 動態預測 121 行）+ Q13（(P4) 三明治 156 行）+ 2 主章 callout（ch04 / ch05），達成 appendix-D-why.md 從 1175 行擴至 1657 行（+482 行 / 13 Q&A = 59%）+ 6 callout / 13 Q&A links 全書累計。

### 對話低效時刻（具體事件 + 為什麼）

- **ch05 callout 中 1 處 typo「appendix-D-view」應為「appendix-D-why.md」**：寫批量 callout 時手快漏寫 `.md` + 把 `why` 拼成 `view`，幸好寫完後執行的 grep 驗證輪馬上捕到。**原因：**批量寫多 link 時應該每寫一個 link 就一條條 visually 對照前面範本（S12 ch01-ch03 callout 內的 link 格式都是 `appendix-D-why.md#qXX`），不能憑記憶輸入 `.md` 副檔名。**教訓：**Markdown link 批量插入後一律跑 `grep -nE "appendix-D-why" file.md` 驗證副檔名 + anchor 完整正確。

- **awk pattern range `/regex/,/regex/` 對中文標題 + 數學符號不可靠**：第一次想統計 Q10-Q13 各條行數時，用 `awk '/^## Q10:/,/^## Q11:/'` 結果全部回傳 0 — pattern 沒匹配。**原因：**未確認檔案實際的「Q」與「：」是否與 awk regex 字面對齊（後面 Q&A 標題實際是 `## Q10：為什麼乘法不可交換 $AB \ne BA$？ {#q10}`，含全形冒號 `：` 而我寫的 regex 可能對到半形 `:` 或被特殊字元干擾）。**教訓：**統計 markdown ## heading 間行數時，**改用 `grep -n "^## "` 取行號 + 減法**比 awk pattern range 更穩定，特別是含中文標點 + LaTeX 公式時。

### 建議 Back 下次這樣問會更快

- **「§4 + §5 共 4 條 Q&A + 2 主章 callout」一句話精準指令** — Back 連續 2 個 session（S12 確認 4-session 路線、S13 跟著走）用最短句子直接觸發批量，這個 pattern 非常高效。**未來 S14（§6 五大分解）+ S15（附錄）也可沿用「主題 + 條數 + callout 數」格式**（如「§6 共 6 條 Q&A + 6 主章 callout」），Claude 自己會從 HANDOFF S14 路線決定執行細節。

- **無低效提問** — 本 session Back 沒提任何不精準問題，整段對話一句話啟動 + 批量產出 + 收工。

### Claude 自我提醒（不需 Back 督促也該做的事）

- **Markdown link 批量插入後一律 grep 驗證副檔名 + anchor**：S13 ch05 callout typo 已踩雷，未來 S14 6 個主章 callout + S15 3 附錄 callout 批量插入時，最後一定要 `grep -nE "\]\(appendix-D-why\.md#q[0-9]+\)" docs/book/*.md` 跑一輪驗證所有 13+ 個 link 完整正確。

- **統計 markdown heading 間行數用 grep -n + 行號減法**：別用 awk pattern range，特別是含中文標點 + LaTeX 公式時。例：`grep -n "^## Q" docs/book/appendix-D-why.md` → 取連續兩行的 line number 相減 = 該 Q 篇幅。

- **HANDOFF 章節寫作速度資料點隨 session 累計，保留歷史 + 加新 column 對照**：S13 把資料點表從「平均值單一 column」改為「S12 / S13 / 全期累計」三 column 對照，未來 S14-S15 也應沿用此 layout（保留歷史值 + 加新 column）避免「每次只看當期失去縱向比較」。

- **§14 SOP 預期更新方向**：Q14-Q19 §6 五大分解預期每條 ~150 行（含分解定理證明 + (P4) 三明治連結 + 分解步驟），預期添加「Q&A → (P4) 中央輻射結構」cross-link 設計觀察，補進 §2.13。

---

## S14 — 背後觀念層續寫 §6：Q14-Q19 + 6 主章 callout（2026-05-13）

### 本 session 主軸

Back 用「**Q14**」單一指令觸發 S14 第一條（Q14 為什麼要把矩陣「分解」？§6 整體動機），再用「**Q14, Q15, Q17, Q18**」分批指令觸發第二批（跳過 Q16 先做 Q15+Q17+Q18），「**繼續 Q16 + Q19**」完成第三批，最後「**繼續做 6 主章 callout**」收尾。Claude 沿用 S12-S13 PoC-鎖定流程批量產出 Q14（156 行）+ Q15（119 行）+ Q16（165 行）+ Q17（138 行）+ Q18（144 行）+ Q19（174 行）共 6 條 + ch06a-ch06f 6 主章 callout 共 15 Q&A links，達成 [appendix-D-why.md](../book/appendix-D-why.md) 從 1657 行擴至 **2740 行（+1083 行 / 19 Q&A = 86%）**+ **全主章 callout 100% 覆蓋（12 callout / 28 Q&A links）**。

### 對話低效時刻（具體事件 + 為什麼）

- **本 session 無重大對話低效時刻** — Back 三次指令（「Q14」/「Q14, Q15, Q17, Q18」/「繼續 Q16 + Q19」/「繼續做 6 主章 callout」/「收工」）全部精準，Claude 全程批量產出無需中途 review，效率近乎理想。**S12-S13-S14 三 session 連續驗證「精準分批指令 + 批量產出」是背後觀念層的最佳工作模式**。

- **小例題刻意串接需要事先設計** — Q19 SVD 3×2 小例題刻意用與 Q17 同個 $A$ + $A^{\mathrm{T}}A$ 正好是 Q18 同個 $2 \times 2$ 矩陣，形成「Q17 QR → Q18 EVD → Q19 SVD」教學鏈。**這個設計是在寫 Q19 過程中即興發現的巧合**（並非預先規劃），事後驗證效果極佳。**經驗：批量寫 Q&A 時應主動尋找「同例題串接」機會**，能讓讀者跨 Q 自然連動。

### 建議 Back 下次這樣問會更快

- **「Q14」單字啟動 + 「Q14, Q15, Q17, Q18」分批 = 完美節奏** — Back 把 6 條 Q&A 分成「先 PoC 1 條（Q14）→ 後批量 3 條（跳 Q16）→ 補 2 條（Q16+Q19）→ callout 收尾」四批，每批 Claude 都能在 cache 內一氣呵成完成而不會疲勞。**未來 S15 可採類似分批：「Q20」→「Q21 + Q22」→「3 附錄 callout」→「收工 + BOOK.md 重生」**。

- **「跳過 Q16 先做 Q15, Q17, Q18」展示彈性指令的價值** — Back 自由決定條目順序（非機械順序），Claude Edit 操作精準插入後檔案最終排列仍按數字順序 Q14→Q15→Q16→Q17→Q18→Q19。**未來 Back 可隨意指定條目順序，不需擔心檔案排亂**。

### Claude 自我提醒（不需 Back 督促也該做的事）

- **小例題刻意串接設計**：寫 Q&A 時主動考慮「能否用前面 Q&A 已用過的範例」，例如 Q19 用 Q17 同 $A$、Q18 用 Q13 同 $S$。**這種跨 Q 同例題不只節省讀者算驗時間，更讓概念在不同視角下自然連動**。S15 附錄 Q20-Q22 也應主動找這類機會（譬如 Q22 解 $A\mathbf{x}=\mathbf{b}$ 完整結構可能可以用 Q15 同 $A$ 的 CR 範例）。

- **Markdown callout 批量插入後 grep 驗證**：S13 已踩 typo 雷一次，S14 12 個 callout 28 個 link 全部驗證過 — 未來 S15 3 個附錄 callout 也照做 `grep -nE "appendix-D-why\.md#q[0-9]+" docs/book/*.md` 一輪。

- **§6 callout 平均 link 數比 §1-§5 高 15% 是「自然現象」不是設計偏差**：§6 五大分解本質統合 §1-§5 多概念，所以 callout 需要更多 cross-link。**未來 S15 附錄 callout 預期同樣會多 link 數**（附錄重整合而非重教學），不要強行壓低 link 數。

- **Strang LAFE 名言應主動挖掘為 callout hook**：S14 ch06a 用「Make every matrix look diagonal」、ch06f 用「the most important theorem in linear algebra」 — 這些直引名言比泛論寫法強大很多。**Back 提供的 8 本 Strang PDF 中還有更多名言可挖（如 ILA 第 6 版各章開頭、LAaLD 各章引言）**，S15 附錄 callout 應主動使用。

- **「雙證明路徑」對 §6 存在性 Q&A 高價值**：Q19 SVD 雙證明（譜定理建構性 + 變分定義）、Q18 譜定理雙證明（不同特徵值正交 + 實特徵值補充）讓讀者從兩個獨立角度確認「為什麼存在」。**S15 Q22 解 $A\mathbf{x}=\mathbf{b}$ 為什麼線代核心問題**也可考慮雙證明（從 4 子空間整合 + 從應用角度涵蓋）。

---

## S15 — 背後觀念層收尾 + 全書整合 100% 完成：Q20-Q22 + 3 附錄 callout + BOOK.md 重生 + 規範補充 + 全套收工（2026-05-13）

### 本 session 主軸

Back 用 5 個獨立指令依序觸發 S15 全部任務：「**開始**」（session 啟動 + 讀取脈絡 + 規劃 Q20-Q22 路線）→「**Q20**」→「**Q21**」→「**Q22**」→「**3 附錄 callout**」→「**繼續接 BOOK.md 重生 + anchor 校驗**」→「**兩個一起做（規範補充 + 全套收工）**」。Claude 沿用 S12-S14 鎖定的「鎖定 PoC → 批量產出」流程，每個 Q&A 約 30 分鐘批量產出（**Q20 225 行 + Q21 246 行 + Q22 311 行 = 全書最長 Q&A**），達成 [appendix-D-why.md](../book/appendix-D-why.md) 從 2740 → **3522 行（+782 行 / 22 Q&A = 100% ✓）**+ **全書 15 callout / 37 Q&A links / 16 個內容 md 100% 覆蓋** ✓ + BOOK.md 重生（8650 → 12305 行 / +42%） + SCHEMA §3.6 規範補充 + VIZ-CATALOG Appendix D 索引段。**「**背後觀念層 4-session 路線 S12-S15 完成**」**。

### 對話低效時刻（具體事件 + 為什麼）

- **本 session 無重大對話低效時刻** — Back 7 個指令（開始/Q20/Q21/Q22/3 附錄 callout/BOOK.md 重生+anchor 校驗/規範補充+全套收工）全部精準，Claude 全程批量產出無需中途 review。**S12-S13-S14-S15 四 session 連續驗證「精準分批指令 + 批量產出」是背後觀念層的最佳工作模式 — 4 session 共產出 22 條 Q&A / 3522 行 / 37 callout links，**0 次中途回頭**

- **Edit 中文字元失敗 1 次（appendix-matrix-world callout 半形 vs 全形括號）** — old_string 「對應的矩陣分解」後我貼上半形 `(` 但原文是全形 `（`，Edit 失敗 → 重新讀原檔 + 用較短 old_string（從末尾「互動式版本 ⭐⭐⭐ Tier 2 旗艦規格...」往後）成功。**經驗：未來 Edit 中文檔 old_string 應從「**不含括號的純文字段**」起頭，避免括號類型差異**

- **Q22 全書收尾性質強 → 篇幅顯著比預期長** — 預期 ~250 行，實際 311 行（**全書最長 Q&A**）。原因：Q22 需收束全書 21 條 Q&A 的觀點 + 4000 年史 + 13 領域跨領域對應表 + 全書會師結構表 + Strang 50 年教學總結。**未來如有類似「全書收尾」題目，預期 ~300+ 行屬正常，不要強行壓縮**

### 建議 Back 下次這樣問會更快

- **「Q20 → Q21 → Q22」逐條觸發 = S15 完美節奏** — Back 採「每條 Q&A 獨立確認後再進下一條」而非 S14 的「分批 3-4 條」— 因為 S15 3 條 Q&A 都是「附錄收尾性質」需獨立思考設計（非機械式延續），逐條節奏比批量好。**S12-S15 經驗：「機械式批量」適用於 §1-§5 結構相似的 Q&A，「逐條觸發」適用於 §6 集大成 + 附錄收尾的 Q&A**

- **「BOOK.md 重生 + anchor 校驗」+「規範補充 + 全套收工」分兩批 = 收尾流程合理切割** — Back 把 4 件收尾任務分兩批：第 1 批技術性整合（BOOK + anchor）、第 2 批文件性收尾（SCHEMA + VIZ-CATALOG + 4 dev 檔）— 這個切割讓 Claude 可以「技術整合驗證通過 → 才開始寫規範」。**未來大規模收尾建議採同樣兩批切割**

- **「兩個一起做」當收尾合併指令** — Back 在 Claude 把任務分多步問之後直接說「兩個一起做」，避免追加問題堆疊。**未來 Back 可在 Claude 詢問「哪一項先做」時直接回「都做」/ 「按你想的順序」/ 「合併」加快節奏**

### Claude 自我提醒（不需 Back 督促也該做的事）

- **規範化的時機是「累積 ~15 實例後」**：S15 把 S12-S15 累積 15 個 callout 寫進 SCHEMA §3.6 規範段 — 這個時機選擇可重用。**未來如有累積 ~15 次的設計模式（如「附錄整合 pointer 策略」累積 5 個附錄、「跨章 cross-link 知識網路」累積 ~50 條 link），可考慮抽象化進 SCHEMA / VIZ_SCHEMA 標準**

- **anchor 校驗用 grep + awk 自動化 > 人工檢查**：S15 用 `grep -rno "appendix-D-why\.md#q[0-9]*"` + `grep -o "{#q[0-9]*}"` + 範圍 awk 校驗自動化 → 0 broken / 1 min 完成 vs S11 人工檢查 39 條 `#vizscript-NN` 需 ~10 min。**未來大規模整合校驗一律 grep + awk 自動化**

- **BOOK.md 重生的 header 數字維護是收尾性工時消耗**：S15 BOOK.md 重生中 header 12 處數字更新（VizScript 數 / Q&A 數 / 各章新行數 / callout 統計）+ 新增 2 個結構表共 10 min — 比實際合併 awk（5 min）更費時。**未來如能設計「**從 source md 自動抽取數字產生 header**」的腳本（如用 wc -l + grep -c 統計）會大幅加速**

- **「跨檔 Edit 中文字元」是穩定的小坑**：S15 踩了 1 次半形 vs 全形括號的雷 — 雖然不嚴重但累積起來會浪費時間。**未來 Edit 中文檔的 old_string 應優先用「**不含括號的純文字段**」匹配**，或先用 `head -N | tail -M` 確認原文字元類型再貼

- **「全書 22 條會師結構」設計可作為「線代核心」題目的標誌性手法**：Q22 用「Q01-Q21 全表逐條對 Ax=b 關係」作為昇華第 3 層 — 這個「會師表」結構在「整本書收尾」題目中是有強教學效果的。**未來如做「教材總結性章節」可重用這個手法**（例如做「**線代地圖鳥瞰**」附錄或 S12+ 視覺化教材的「結語頁」）

### S12-S15 背後觀念層 4-session 總結

- **總成績**: [appendix-D-why.md](../book/appendix-D-why.md) **3522 行 / 22 Q&A = 100% ✓** + 全書 16 個內容 md / **15 callout / 37 Q&A links = 100% 覆蓋 ✓**
- **總耗時：** ~11h（S12 ~2.5h + S13 ~2h + S14 ~3.5h + S15 ~3.5h，含 BOOK.md 重生 + 規範補充 + 全套收工）
- **平均效率：** 11h / 22 Q&A = 30 min / 條（含史線搜尋 + 推導 + 例題 + 跨領域應用 + 經典引用），比預期高 25%（原預估 ~14h）
- **里程碑：** 全書 §1-§6 主章節（S02-S10）+ 整合 BOOK.md/VIZ-CATALOG（S11）+ 背後觀念層 22 Q&A + 全書 callout（S12-S15）= **完整教材 16 個內容 md 100% 結構就緒**，S12+ Python 視覺化實作下一步進場

---

## S16 — Marimo 技術棧 PoC：從 md 化跨入 Python 視覺化實作（2026-05-13）

### 本 session 主軸

Back 不立刻挑旗艦，先做技術棧 PoC + 載體討論（先例 6 個 + 平台 6 比較 → 維持 Marimo + WASM）；三階段全跑（hello.py + ch01_mv1_poc.py + html-wasm 部署）+ 3 round debug Stage 2 WASM 才通；產出 viz/ 7 檔 + commit `2f9b9e3` + SOP §2.15「Marimo WASM 部署 3 大陷阱」+ S17+ 旗艦開工 5 條 checklist。從「全書 md 化結構完成」跨入「Python 視覺化實作階段」。

### 對話低效時刻

- **Round 1 debug 我先猜方向、沒主動要 console log，浪費 1 round（~30 min）** — Back 報「An internal error occurred」我直接「防禦性重寫」猜 LaTeX label / slider 嵌 markdown / plotly 新特性 3 個風險，重 export 後 Back 仍錯但這次給了 console log → 立刻看到真因 `ModuleNotFoundError: No module named 'plotly'`。**如果 Round 1 我直接說「請貼 DevTools Console 紅色錯誤行」，一輪就解決**。WASM 黑盒環境 debug 的第一動作應該是「**索取 console log**」而非「猜原因 + 重寫」。

- **「首次載入 30s」UX 沒在我給 URL 時警告** — Stage 1 OK 後我順手給 ch01_mv1_poc 的 URL 但只說「⚠️ 首次開啟要等 5-15 秒」— 實際上 Pyodide + plotly wheel + plotly.js 三層下載要 30-60s；Back 等不夠久誤判「沒報錯但空白」。**部署型 PoC 的 first-load 時間應該主動估上限 60s 而非樂觀的 15s**；少給時間反而讓使用者懷疑壞了。

- **Stage 2 範例堆太多功能** — 我一次寫 7 cell × 4 plotly 箭頭 + 平行四邊形 + LaTeX f-string 表格 + 6 slider，本機 OK 但 WASM debug 時不知是哪個面壞掉。**PoC 第二階段應該「**只加一面變數**」**（從 hello 加 1 slider × 1 plot 就好），等通過才加下一面。我這版直接堆成「準旗艦」結果 debug 變多面同時懷疑。

### 建議 Back 下次這樣問會更快

- **報 WASM 錯誤時直接附 console log 不用等我問** — 之前你 `Cmd+Option+J → 截圖紅色 error 行` 一貼，我 30 秒看出真因。下次若 WASM 黑盒環境壞，**第一句就附 console log**（哪怕一張截圖），避免我先「防禦性重寫」浪費 1 round。

- **「空白」也算錯誤狀態，可以更早報** — 你「沒報錯但空白」其實已經是錯誤訊號（不是「正在載」），下次直接附 console + 告訴我等了多久，我可以分辨「Pyodide 還在 micropip install」vs「真的卡死」。

### Claude 自我提醒

- **WASM debug 第一動作：要求 DevTools Console 截圖** — 不要先猜 + 不要靠重寫消除假設。Pyodide 黑盒環境的錯誤幾乎都在 console，比我猜 100 次更高效
- **部署型工件 first-load 時間警告必須給「上限」而非「樂觀估計」** — Pyodide + 套件 wheel + 套件 JS bundle 三層下載通常要 30-60s；S17+ 旗艦頁面更可能 60-90s（加 sklearn / Pillow 後）；首頁明寫「首次載入請等到看到圖出現再操作（~60s）」
- **PoC 階段「**一次只加一面變數**」原則** — Stage 1 → Stage 2 應該只多 1 個新元素（如「加 1 slider + 1 fig」）而非一次堆 4 箭頭 + 平行四邊形 + LaTeX + 6 slider；後者 debug 時無法定位是哪個元素壞掉
- **S17+ 旗艦實作前先補完 SOP §2.15 五條 checklist** — PEP 723 metadata / mo.ui.plotly wrap / mo closure arg / WASM console 必看 / 首頁 60s 警告。這 5 條都是我這次踩出來的，下次 S17 寫 ch04 V-02 母模板時 checklist 過一遍能避開全部
- **「載體選型」這種策略討論值得主動展開比較表** — Back 問「app 式書籍有先例？」我給了 6 先例 + 6 平台比較表 + 推薦 + tradeoff，他直接「先做 Marimo PoC」省略 30 min 討論回合。**策略型問題主動給比較表是高 ROI 動作**

---

## S17 — ch04 V-02 MM4 母模板架構階段：首批 Tier 3 旗艦實作開工（2026-05-13 ~ 2026-05-14）

### 本 session 主軸

Back 選 HANDOFF S16 推薦路線 A — 開始 [ch04-mat-mat.md VizScript-02](../book/ch04-mat-mat.md#vizscript-02) 母模板（完成後 §6 五分解 pointer 全解鎖）；S17 scope 鎖「最小可動骨架」（小矩陣 3×2·2×2 + r slider + 秩 1 圖層 strip + 主舞台 6 heatmap + WASM 部署），不含圖像 / 動畫 / 重排序 / Walkthrough（推 S18-S19）；產出 `viz/ch04_matrix_matrix.py` 440 行 / 8 cell + `viz/_common/rank1_layer.py` 工具模組；2 round debug 才通 + 3 個新 WASM 陷阱記入 SOP §2.15（marimo `_` 前綴 cell-private / plotly `subplot_titles` 空字串 / heatmap `z` 需 numpy）；commit `cc957f1`。

### 對話低效時刻

- **scope 切分前我多寫了 1 個 helper cell 結果踩了 `_` 前綴陷阱** — 我寫 `@app.cell def _(np): ... return _accumulate, _layer_energy, _layers_of` 想「把工具與計算分 cell 更乾淨」，結果踩了 marimo 「`_` 開頭 variable cell-private 不跨 cell export」這個沉默陷阱。**如果第一版就直接 helper 與計算合併同一 cell**（最終修法），會省 Round 1 的 debug + Back 視覺確認 + 我修 + Back 再確認。**多 cell 分工只在「真有跨 cell 重用」時才值得，否則內聯比較穩**。

- **Round 1 視覺問題不是 console error 而是「cell 沒渲染」，我先入為主以為是 PEP 723 / mo.ui.plotly 漏了** — Back 報「只看到 sliders + 標題 + 結尾說明」，我第一反應檢查 PEP 723 + mo.ui.plotly wrap 都對。**沒注意到「cell 沒渲染」≠「cell exception」**（marimo WASM 對 NameError 處理是「整個 cell 沉默 skip」不是 STDERR）。Round 2 Back 給的 console log 其實已經有 STDERR `TypeError` / `IndexError` 在裡面 — 但那是 Round 2 修了 `_` 前綴問題之後的下游 error。最初的 NameError 因為「未渲染」沒進 STDERR。**WASM cell 沒渲染但沒 STDERR 的情形，第一動作該是「marimo 內部 cell graph 解析失敗」假設，要看的不是 console 而是 cell python 文件**。

- **「我只看到這個畫面」我以為 Back 截了完整畫面，沒主動問是否還有其他 cell** — Back 截了上半（標題 + sliders）+ 下半（S17 骨架說明），中間 3 cell 不見。我先按截圖修，沒先問「中間 3 cell 是真的不見、還是 scroll 沒到？」。**截圖時主動問「有沒有完整 scroll 過？」省一次誤判**。

### 建議 Back 下次這樣問會更快

- **WASM 視覺問題截圖時主動標示「我有沒有 scroll 到底」** — 一張截圖只能拍到視窗大小範圍，下次若回報「只看到 X」，加一句「我有把整頁 scroll 完，中間 X 段是真的不見」就能避免我猜「會不會沒 scroll」。對應地我也會在初期問「截圖之外的其他段有顯示嗎？」

- **WASM debug 直接附 console log（S16 教訓延續）成功應用** — Round 2 你直接貼了完整 console，我 1 秒看出 `TypeError` / `IndexError` 兩個錯誤行就修對。**S16 學到的「先附 console」這次 work 了，繼續維持**。

### Claude 自我提醒

- **跨 cell 共用任何東西，命名不可 `_` 開頭** — marimo 把這視為 cell-private 不跨 cell export，下游引用會 NameError 但 marimo 處理是「整個 cell 沉默不渲染」沒明顯 STDERR。S18+ 寫 helper 時 default 命名規則：(a) 跨 cell 用一律 `helper_xxx` / `acc_xxx` / `rank1_xxx` 等具名前綴 (b) 若只 cell 內部用才可以 `_xxx`
- **WASM 部分 cell 不渲染 + console 沒 STDERR ＝ marimo cell-graph 解析問題（不是 runtime exception）** — 第一動作該是 (1) `python -c "import ast; ast.parse(open('xxx.py').read())"` 看 syntax (2) marimo edit 在本機跑 (3) 檢查 `_` 前綴 / cross-cell variable 拼錯字 (4) 才是看 console。次序顛倒會多繞 round
- **多 cell 分工只在「真有跨 cell 重用」時才做** — S17 helper cell 寫完發現只 1 個下游 cell 用，那「分 cell」沒帶來重用價值卻多了一個跨 cell 邊界（多 1 個 `_` 陷阱風險）。**helper 函數預設先內聯在唯一使用者 cell，等真有第 2 個使用者再抽出來**
- **`np.asarray(M, dtype=float)` 是 plot helper 的 default 防線** — heatmap / annotation / hover 函數的開頭該預設保護輸入，不假設 caller 一定傳 numpy。同樣 `abs()` → `np.abs()` 是純習慣改寫
- **scope 切分守得住是 S17 最大優點** — 我沒把圖像 / 動畫 / 重排序硬塞進骨架，預估 3 session 拆架構 / 互動 / 應用 — 這次只做架構，commit 端正。S18 加圖像 / S19 加動畫 + 重排序 + Walkthrough 是接下來節奏
- **截圖回報時要主動確認「scroll 完整否」** — 對 WASM 部分 cell 不渲染類問題，未確認 scroll 範圍就修可能修錯方向。S18+ 先問「整頁 scroll 過嗎？中間 X 段是真的不見嗎？」

---

## S18 — ch04 V-02 圖像模式 + Mona Lisa SVD 首輪交付（2026-05-14）

### 本 session 主軸

Back 選 HANDOFF S17 推薦路線 A 開始圖像模式。我從 S17 骨架擴 viz/ch04_matrix_matrix.py 至 ~570 行 / 9 cell，加 mode radio + 4 張 64×64 procedural 圖像（in-notebook 生成跳過 npy/base64/fetch 不確定性）+ SVD 即時計算 + 三圖並列 + σ 譜柱狀圖。WASM export 27 MB clean，本機 SVD 對拍通過 4 圖預期性質。

### 對話低效時刻

- **第一版 random 用 min-max 標準化到 [0,1] 破壞「不可壓縮」訊息我自己抓到** — 第一輪 SVD 驗證列出「random r85=1」我意識到不對勁（隨機本該不可壓縮）→ 立即查出是 min-max normalize 注入 DC → 改為 raw standard_normal 重驗符合 Marchenko-Pastur。算是「設計失誤」自我修正不算對話低效，但**第一版設計時就該考慮「random 必須保留 raw centered 分佈」**，這是 SVD 數值教學的常識，我做圖像生成前沒先想清楚。**S18+ 寫教學 demo 前先「pedagogical 預期表」對拍**：每張圖預期 σ 譜形狀（高峰 / 雙峰 / 緩降）+ 預期 r 值閾值，做完數值驗證對拍預期，差異就 debug。

- **scope 切分守得不夠緊：footer 觀察重點表第一版用「~10-20 effective rank」是估計值** — 我寫表時沒先算就填了估計值，本機驗證跑出 portrait eff_rank=5（不是 10-20）+ random r85=28（不是 ~55）→ 兩個數字錯。**寫教學表前應先實際算**，估計值容易誤導讀者。

- **無 — 對話本身順暢，主要是設計階段的兩個失誤**（自我修正完）

### 建議 Back 下次這樣問會更快

- **無建議 — Back 這次提問已經精準（「A」單字明確選 HANDOFF 路線）+ 收工指令乾淨**。圖像模式視覺驗證未完成是因 Back 直接收工，這正常（一輪交付 + 下次驗證）。

### Claude 自我提醒

- **教學數值 demo 寫程式前先列「pedagogical 預期表」** — 每張圖 / 每組資料的 SVD（or 其他）結果要先預測 σ 譜形狀 + 關鍵閾值，做完跑出數字對拍預期，差異就立刻 debug 設計（如 S18 的 random min-max 失誤）。**「先預測再驗證」省一輪「pretend 成功實際破壞訊息」迭代**。
- **寫教學表前先實際算數字** — footer 表的「有效 rank」「視覺辨識 r」這類具體數字不要憑估計填，先實際跑 SVD 取得真實數字。教學表是教學產出的一部分，估計值會誤導讀者後續實作 / 觀察。
- **「跳過難題」是一種有效設計選擇** — HANDOFF S18 開頭 Back 預估 WASM 讀本機 npy 是難點需 base64 或 fetch，我實作時改「程式內生成圖像 + 即時 SVD」直接跳過。**遇到 HANDOFF 標記為「待確認的難點」，先問「能不能繞過」**，繞過往往比解決更省事且更穩定。
- **首輪交付不等於完工** — Back 在我發 5 項驗證清單後立即「收工」，我沒繼續催 Back 操作而是直接執行收工。**首輪交付後若 user-side 驗證未完成，HANDOFF 要明示「進行中：等視覺確認」而非「完成」**。下次 S19 第一動作該是 Back 確認 S18 視覺，OK 才往下走。

---
