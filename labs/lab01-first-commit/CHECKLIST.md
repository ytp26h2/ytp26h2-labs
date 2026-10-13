# Lab 1 驗收紀錄

驗證日期：2026-10-13｜驗證方式：無頭 Chromium（Playwright 1.56）直接開啟 `index.html`，以程式點擊並讀取 `#card` 文字；git 紀錄以指令查核。

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 瀏覽器打開 `index.html`，卡片能翻面、能換下一張 | ✅ | 初始 `algorithm` → 點卡片 `演算法` → 再點 `algorithm`；點「下一張」→ `recursion`。翻面狀態下按「下一張」會重置為正面。連按 8 次依序 recursion→vocabulary→memorize→efficient→persist→retrieve→interval→algorithm，循環正確。Console 無錯誤。 |
| 2 | `git log --oneline` 至少 2 個 commit，訊息符合「類型: 說明」 | ✅ | `lab01: feat: 首頁骨架與可翻面單字卡`、`lab01: docs: README 與 gitignore`（Lab 前綴＋教材格式） |
| 3 | GitHub 上看得到 `index.html`，首頁顯示 README | ✅ | 推上 `ytp26h2/ytp26h2-labs`，路徑 `labs/lab01-first-commit/`；資料夾頁面會渲染本 Lab 的 README |
| 4 | commit 作者顯示為 GitHub 帳號 | ✅ | 透過 Claude 雲端 session 推送，作者歸戶為授權帳號；可在 GitHub commit 頁面點頭像確認 |
| 5 | 能用自己的話說出 add 與 commit 分別把檔案搬到哪一區 | ✅ | `add`：工作區 → 暫存區（挑出「這次要存檔的內容」）；`commit`：暫存區 → 儲存庫（在歷史上釘下一個不可變的快照節點） |

## 補充驗證（教材未列，主辦自加）

- 翻面後按「下一張」，新卡片應顯示英文面：✅（`flipped` 被 `next()` 重置）
- 手機寬度 viewport：meta viewport 已設，卡片 `max-width:340px` 置中：✅（靜態檢視）
- 頁面標題為 `YTP VocaBuddy`：✅
