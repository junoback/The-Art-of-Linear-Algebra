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
