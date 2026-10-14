# Lab 5（Sprint 1）驗收紀錄

驗證日期：2026-10-14｜驗證方式：無頭 Chromium（Playwright 1.64 驅動環境預裝的 Chromium 1194），桌機視窗 1280×800 與 iPhone 13 裝置模擬（390×664、觸控）各跑一輪完整佇列；教材程式碼一字未改。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 打開頁面立即看到第一張卡與「剩 N 張」；答完全部出現「今日完成」 | ✅ | 載入後 `#card` 為 `algorithm`，`#stats` 為「今日佇列：剩 8 張」，只顯示「顯示答案」鈕。答完 8 張（含一次「忘了」重考）後 `#card` 為「今日完成！」，三個按鈕全部隱藏。 |
| 2 | 「忘了」的卡稍後會再出現，直到你答「記得」 | ✅ | 第一張 `algorithm` 答「忘了」後 `queue` 變為 `[recursion, …, interval, algorithm]`，`#stats` 仍「剩 8 張」；實際看到的卡片順序為 algorithm → recursion → … → interval → algorithm，algorithm 出現兩次，最後一次答「記得」才完成。 |
| 3 | 重新整理後，seen／wrong 統計仍在 | ✅ | 完成後 `log` 為 8 個字各 `seen:1`，`algorithm` 為 `{seen:2, wrong:1}`；`page.reload()` 後 `log` 深度相等，`localStorage.getItem("vb-log")` 含全部字。 |
| 4 | 手機上按鈕大小、字級可正常操作 | ✅ | iPhone 13 模擬：無水平捲動；「顯示答案」鈕 108×41 px；卡片字級 32px；以 `tap` 點完整佇列到「今日完成！」，無 JS 錯誤。真機未測，請自行再過一輪。 |
| 5 | PR 已合併、tag `sprint1-done` 已推上 GitHub | ⏳ | issue [#12](https://github.com/ytp26h2/ytp26h2-labs/issues/12)。PR 開出後等管理員合併，tag 由管理員以 Release 建立，合併後補記。 |

## 額外檢查

| 檢查 | 結果 |
|---|---|
| 桌機、手機全程 `pageerror` | 0 筆 |
| 翻面後 `#meaning` 顯示中文、按鈕切換為「記得／忘了」 | ✅（algorithm → 演算法） |
| 答完最後一張時 `#stats` 的值 | ❌「今日佇列：剩 1 張」，應為 0 張或清空。`next()` 清空分支沒呼叫 `stats()`。記為勘誤 **E-012**（低）。 |
| 重新整理後今日佇列 | 重置為 8 張（只有 `log` 持久化）。教材未說明，記為勘誤 **E-013**（低）。 |
| 收工儀式 commit 訊息 `closes #4` | 教材寫死編號，與 E-006 同類，併入 E-006 的連帶修改。 |

## 怎麼重現這份驗證

1. `pip install playwright`，用環境預裝的 Chromium（或 `playwright install chromium`）。
2. 以 Playwright 開 `file://…/index.html`，依序：讀 `#card`／`#stats` → 點 `#reveal` → 第一張點 `#no`、其餘點 `#ok` → 迴圈到 `#card` 為「今日完成！」→ 讀 `log` → `reload()` 後比對 `log`。
3. 手機：`browser.new_context(**p.devices["iPhone 13"])`，改用 `tap`，另量 `#reveal` 的 `getBoundingClientRect()` 與 `document.documentElement.scrollWidth`。
