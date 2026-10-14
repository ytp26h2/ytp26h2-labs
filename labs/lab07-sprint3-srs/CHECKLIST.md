# Lab 7（Sprint 3）驗收紀錄

驗證日期：2026-10-14｜驗證方式：三層。第一層 Node 22 跑 `test_srs.js`，並把 `INTERVALS` 每一格各改壞一次看測試抓不抓得到；第二層無頭 Chromium（Playwright 1.64 ＋ 環境預裝 Chromium 1194）以寫 `localStorage` 的 `vb-day` 後 reload 模擬 `vbTravel`，逐日檢查 46 天；第三層用 Lab 6 的 AI 例句攔截腳本對本頁重跑一次做回歸。教材程式一字未改。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | `node test_srs.js` 四條測試全過；故意把 `INTERVALS` 改壞一格，測試會抓到 | ✅（部分） | `4 tests passed ✓`。改壞測試：第 1、2、4、5 格各 +1 都讓測試失敗；**第 3 格 +1 測試照樣通過**，因為四條案例沒有一條落在盒 3。記為勘誤 E-018。 |
| 2 | 新的一天只出現「到期」的卡；全答完顯示「明天見」 | ✅ | 第 0 天 8 張全到期；全答完 `#card` 為「今天沒有到期的卡——明天見！」；第 1 天 0 張；第 2 天 8 張；第 3 天 0 張；第 4 天只有前一天答錯重考的 recursion（盒 2 間隔 2）。 |
| 3 | 用 `vbTravel` 驗證：答對的卡間隔按 1→2→4→8→16 拉長；答錯的隔天就回來 | ✅（教材敘述有誤） | 實測 algorithm 的 `due` 依序為 +2、+6、+14、+30、+46，即間隔 2→4→8→16→16（頂級不再升）。新卡的第一個間隔是 2 不是 1；教材「`vbTravel(1)` 後 8 張回來」實測 0 張。答錯：recursion 第 2 天答錯 → 當天重考答對 → 盒 2 due +2 → 第 4 天回來；只有答錯後關頁不重考，才會「隔天回來」。記為勘誤 E-017。 |
| 4 | 能對隊友解釋：為什麼 `schedule()` 不自己呼叫 `Date.now()` | ✅ | 見 README「為什麼 `schedule()` 不自己呼叫 `Date.now()`」。 |
| 5 | PR 已合併、tag `sprint3-done` 已推 | ✅ | PR [#19](https://github.com/ytp26h2/ytp26h2-labs/pull/19) 由管理員 `tw-ytp` 於 2026-10-14 合併（merge commit `6cb6a37`）；issue [#18](https://github.com/ytp26h2/ytp26h2-labs/issues/18) 由 `closes #18` 自動關閉；本地 `main` 與 `origin/main` 皆為 `6cb6a37`；tag `sprint3-done` 由管理員以 Release 建立，指向 `6cb6a37`。 |

## 時間旅行明細（21 項全過）

| 第幾天 | 動作 | 到期張數 | 檢查 |
|---|---|---|---|
| 0 | 先塞 Lab 5 格式舊紀錄 `{algorithm:{seen:3,wrong:1}}` 再載入 | 8 | `stateOf` 補上 `box:1`、`due:今天`，seen 保留 ✅ |
| 0 | algorithm 先答「忘了」再全答「記得」 | — | 忘了的卡當天排隊尾再考；全部進盒 2 `due:+2`；完成訊息「明天見」✅；`#stats` 仍停「剩 1 張」（E-012 本輪未修，記錄） |
| 1 | `vbTravel(1)` | 0 | 教材寫 8 張，程式邏輯為 0 ✅（E-017） |
| 2 | 全對，recursion 答錯再重考 | 8 | 7 張進盒 3 `due:+6`；recursion 盒 2 `due:+4` ✅ |
| 3 | — | 0 | ✅ |
| 4 | recursion 答對 | 1 | 只有 recursion ✅ |
| 6 | 全對 | 7 | 盒 4 `due:+14` ✅ |
| 14 | 全對 | 8 | 7 張盒 4 ＋ recursion（盒 3 `due:+8`）；進盒 5 `due:+30` ✅ |
| 30 | 全對 | 8 | 頂級不再升：仍盒 5 `due:+46` ✅ |
| 46 | vocabulary 答錯再重考 | 8 | 答錯打回盒 1，重考後盒 2 `due:+48` ✅ |
| 47 | — | 0 | vocabulary 不到期（兩天後才到）✅ |
| 歸零 | `vb-day` 設 0 | — | `today()` 回到第 0 天 ✅ |

全程 `pageerror` 0 筆。

## 回歸：Lab 6 AI 例句

用 Lab 6 的攔截腳本對本頁重跑，17/17 通過（按鈕時機、三欄位、快取、斷網、400、thinking 區塊、無痕）。
