# Lab 8（Sprint 4）驗收紀錄

驗證日期：2026-10-14｜驗證方式：四層。第一層 Node 22 跑 `check_words.js`、`test_srs.js`，並塞重複字、缺欄位各一次；第二層無頭 Chromium（Playwright 1.64 ＋ 環境預裝 Chromium 1194）以 `page.route` 攔截 API，假 key 只在暫存區腳本；第三層真實呼叫：curl 重放頁面送出的出題請求，Chromium 經環境代理端到端，真實 key 只從環境變數傳入、不印出、截圖不含 key；第四層用 Lab 6、Lab 7 的腳本對本頁回歸。模型 `claude-sonnet-5-5`。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | `node check_words.js` 通過；塞入重複字或缺欄位時會確實報錯 | ✅ | `words.js 檢查通過，共 8 字 ✓`。加一筆重複的 `algorithm` → `Error: 重複單字：algorithm`；把 `interval` 的 `zh` 拿掉 → `Error: 欄位缺漏：{"en":"interval"}`。 |
| 2 | 「考我弱點」出的題目來自錯誤率高的字 | ✅ | 預置 persist 錯 3/4、interval 錯 2/3、retrieve 錯 1/2，`weakest(3)` 回 persist 0.75、interval 0.67、retrieve 0.5；送出的 prompt 含這三個字、不含 algorithm。真實呼叫回的題目答案是 `persist`，選項 persist／resist／consist／insist。 |
| 3 | 格式不合格的題目不會顯示 | ✅ | mock 三個選項、答案不在選項、markdown 圍欄三種情境都不出題，顯示「AI 暫時不可用，先用單字卡複習吧。」；斷網同樣降階。 |
| 4 | 測驗答錯會寫回 `log`，錯誤率上升 | ✅ | 答錯：`log.algorithm` 由 `{seen:4, wrong:0}` 變 `{seen:5, wrong:1}`，`localStorage` 同步，畫面顯示「正解：algorithm。…」；再答對：`seen` 6、`wrong` 不變，顯示「答對！…」。 |
| 5 | 第二個單字包經完整 PR 流程合併，repo 有兩頂帽子的 commit | ⏳ | 第一個 PR 合併後開 `lab08/feature/words-animals`，見下方「多人共編」。 |
| 6 | 四個 sprint tag 齊了 | ⏳ | `sprint1-done`～`sprint3-done` 已在；`sprint4-done` 由管理員在第二個 PR 合併後建立，屆時補記。 |

## 攔截層明細（15 項全過）

| 檢查 | 結果 |
|---|---|
| `weakest(3)` 排序；「考我弱點」鈕常駐 | ✅ |
| prompt 含三個弱字；請求體沿用 `callClaude`（model `claude-sonnet-5-5`、無 `temperature`、`max_tokens` 1024、system 含「不要 markdown 圍欄」） | ✅ |
| 題目與四個選項顯示；答錯寫回並顯示正解；答對顯示「答對！」 | ✅ |
| 三個選項／答案不在選項／markdown 圍欄 → 不出題；斷網 → 友善訊息 | ✅ |
| 模型回 `"Algorithm"`（大小寫不同）→ `log` 多出 `Algorithm` 新鍵，`algorithm` 本尊 `wrong` 不變 | 實證，記 **E-021** |
| 複習迴路與 AI 例句鈕仍正常；全程 `pageerror` 0 筆 | ✅ |

## 真實呼叫

| 請求 | 結果 |
|---|---|
| curl 重放頁面送出的出題請求 | 200、`['text']`、172 tokens；`question` 含 `____`、四個選項、答案 `persist` 在選項中且屬於弱字集合 |
| Chromium 經代理端到端按「考我弱點」 | 200；題目 "Even after several failed attempts, she decided to ____ in her efforts…"，選項 persist／resist／consist／insist；點 persist → 「答對！…」；`log` 鍵仍只有 8 個單字包的字 |

## 回歸

| 腳本 | 結果 |
|---|---|
| Lab 6 AI 例句攔截層 | 17/17 |
| Lab 7 時間旅行 | 21/21 |
| `node test_srs.js` | 4 tests passed |

## 多人共編（第 5 項，待第一個 PR 合併後執行）

1. 從 `main` 開 `lab08/feature/words-animals`，往 `words.js` 加 8–10 個動物單字。
2. 開 PR；換 reviewer 帽子：跑 `node check_words.js`、抽查三個字翻譯、留 review。
3. 管理員合併；補記本表第 5、6 項。
