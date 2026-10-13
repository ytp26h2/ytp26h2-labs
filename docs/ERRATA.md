# 勘誤表（Errata）

對象：YTP VocaBuddy 開發者之路 教材 v2.0（2026-09-08）<https://tw-ytp.github.io/vocabuddy/>
用途：實作各 Lab 時發現的錯誤或不周全之處，先記在此，彙整後再向教材倉庫 <https://github.com/tw-ytp/vocabuddy/issues> 回報。
回報格式依教材 README：哪一節／哪個 Lab、看到什麼、預期看到什麼。

嚴重度：**高**＝照做會卡住或做錯｜**中**＝會造成誤解或日後返工｜**低**＝建議改善。
狀態：`待回報`｜`已回報 #issue`｜`已修正 vX.Y`｜`不採納`。

| 編號 | Lab／章節 | 原文（摘要） | 問題 | 建議修正 | 嚴重度 | 狀態 |
|---|---|---|---|---|---|---|
| E-001 | Lab 1 步驟 4 | 「名稱填 ytp-vocabuddy，選 Private（之後隨時可改公開）」 | Lab 9 要用 GitHub Pages 免費方案部署，需要 **Public**；此事只在附錄 D 與 docs/MAINTENANCE.md 提到。學生到 Lab 9 才發現要改公開，且改公開前須確認歷史裡沒有金鑰（4.1／4.4 才教）。 | 在 Lab 1 步驟 4 加一句：「Lab 9 部署時需改為 Public，所以從現在起不要把任何金鑰 commit 進去。」 | 中 | 待回報 |
| E-002 | Lab 1 步驟 2 起始碼 | `<div id="card">algorithm</div>` 寫死初值；`render()` 在載入時未呼叫 | 畫面初值與 `WORDS[0]` 是兩份資料。學生若在 Lab 2 以後改 `WORDS` 的第一筆（或 Sprint 4 改成載入 `words.js`），首張卡會顯示舊字直到第一次互動。 | 在 `<script>` 末尾加一行 `render();`，並讓 `#card` 初始為空（或保留但註明只是佔位）。 | 低 | 待回報 |
| E-003 | Lab 1 步驟 1 | 「Windows 建議用安裝 Git 時附帶的 Git Bash」 | 未提醒 Windows 的 `core.autocrlf` 預設會把 LF 轉 CRLF，之後 Lab 9 的 CI（Linux）與隊友的 macOS 可能出現整檔 diff 或 lint 警告。 | 在步驟 1 補 `git config --global core.autocrlf input`（Windows）或在 Lab 2 加 `.gitattributes`（`* text=auto eol=lf`）。 | 低 | 待回報 |
| E-004 | Lab 1 驗收清單第 4 項 | 「點開 commit 檢查頭像有沒有正確連結」 | 若學生在 GitHub 開啟「Keep my email addresses private」，`user.email` 需設成 `ID+帳號@users.noreply.github.com` 才會歸戶，教材急救表只說「email 不一致」，未說明 noreply 的情況，學生查不到原因。 | 急救表「頭像是灰色問號」一列補充 noreply email 的設法與查法（Settings → Emails）。 | 中 | 待回報 |
| E-005 | Lab 2 步驟 2 `quiz()` | `do { j = … } while (j === i);` | `WORDS.length === 1` 時 `j` 永遠等於 `i`，無窮迴圈凍結頁面。教材 8 個字不會發生，但 Sprint 4 讓學生自訂單字包後可能踩到。 | 函式開頭加守衛：`if (WORDS.length < 2) return;`，並在 Sprint 4 的 `check_words.js` 檢查單字數。 | 低 | 待回報 |
| E-006 | Lab 2 步驟 1、2 | 「送出後記下編號（應該是 #1）」、commit 訊息 `closes #1` | 在已經有 issue 或 PR 的 repo（例如從範本複製、或先做過別的練習），編號不會是 #1；GitHub 的 issue 與 PR 共用同一組編號。學生照抄 `closes #1` 會關錯 issue 或關不到。 | 改寫為「記下實際編號 N，commit 訊息寫 `closes #N`」，並補一句「issue 與 PR 共用編號」。 | 中 | 待回報 |
