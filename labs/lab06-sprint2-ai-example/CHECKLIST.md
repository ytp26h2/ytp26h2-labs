# Lab 6（Sprint 2）驗收紀錄

驗證日期：2026-10-14｜驗證方式：兩層。第一層無頭 Chromium（Playwright 1.64 ＋ 環境預裝 Chromium 1194）以 `page.route` 攔截 `api.anthropic.com`，用假 key `sk-ant-dummy-for-tests` 餵 `prompt()`，假 key 只在暫存區腳本不進 repo；第二層真實呼叫：把頁面送出的請求體以 curl 重放到真實 API，並讓 Chromium 經環境代理做一次端到端，真實 key 只從環境變數傳入、不印出、截圖不含 key。模型 `claude-sonnet-5-5`。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 翻面後才看得到「AI 例句」按鈕；例句、翻譯、聯想三欄位正確顯示 | ✅ | 翻面前 `#aiBtn.hidden` 為 true，翻面後 false。端到端真實呼叫：`#ai` 顯示「The app uses a simple algorithm to suggest songs that you might like.」＋中譯＋「聯想：…」，`<em>` 包例句；回應 200、區塊 `['text']`、187 tokens。 |
| 2 | 同一單字第二次點擊不再呼叫 API | ✅ | 攔截層：第二次點擊請求數仍為 1，內容仍顯示；`localStorage` 的 `vb-ai` 含 `algorithm`。端到端：第二次點擊新請求 0 筆。 |
| 3 | 斷網時顯示友善訊息，複習流程完全不受影響 | ✅ | 以 `route.abort("internetdisconnected")` 模擬：`#ai` 顯示「AI 暫時不可用——不影響複習，例句之後再補。」，接著按「記得」正常換到下一張、`#ai` 清空。另測 API 回 400 時同樣降階、不噴錯。 |
| 4 | `git grep sk-` 找不到任何金鑰；能解釋為什麼公開網頁不能內建 key | ✅ | `git grep sk-` 只命中 Lab 3／Lab 6 說明文字裡「git grep sk-」這句話本身與 Lab 3 README 的假 key `sk-ant-dummy`；`git grep 'sk-ant-'` 無真金鑰。解釋見 README 末節。 |
| 5 | PR 已合併、tag `sprint2-done` 已推 | ✅ | PR [#16](https://github.com/ytp26h2/ytp26h2-labs/pull/16) 由管理員 `tw-ytp` 於 2026-10-14 合併（merge commit `f5e7904`）；issue [#15](https://github.com/ytp26h2/ytp26h2-labs/issues/15) 由 `closes #15` 自動關閉；本地 `main` 與 `origin/main` 皆為 `f5e7904`；tag `sprint2-done` 由管理員以 Release 建立，指向 `f5e7904`。 |

## 攔截層明細（17 項全過）

| 情境 | 檢查 | 結果 |
|---|---|---|
| A 正常生成 | 第一次按跳出 `prompt`、key 存進 `vb-key`；三欄位顯示；請求標頭含 `x-api-key`／`anthropic-version: 2023-06-01`／`anthropic-dangerous-direct-browser-access: true`；請求體 model `claude-sonnet-5-5`、無 `temperature`、`max_tokens` 1024、system 含「不要 markdown 圍欄」；快取寫入；第二次不發請求；下一張時 AI 鈕藏回、`#ai` 清空 | ✅ |
| B thinking 區塊在前 | 回應 `[thinking, text]` 仍能解析（E-009 修法生效） | ✅ |
| C 斷網 | 友善訊息；複習流程照常 | ✅ |
| D API 回 400 | 被 catch 接住，友善訊息 | ✅ |
| E 模型回 markdown 圍欄 | 走降階訊息（記錄用；system 已要求不要圍欄，真實呼叫三次都沒出現圍欄） | 記錄 |
| F 新 context（模擬無痕） | `vb-key` 為空，重新跳出 `prompt` | ✅ |
| 全程 `pageerror` | 0 筆 | ✅ |

## 真實 API 探測（決定四處修改的依據）

| 請求 | 結果 |
|---|---|
| 教材原樣：`claude-sonnet-4-5` ＋ `temperature: 0.3` | 200，但文字是 ```` ```json ```` 圍欄包住的 JSON，教材 `JSON.parse` 會失敗 |
| `claude-sonnet-5-5` ＋ `temperature: 0.3` | **400** `invalid_request_error`：`temperature` is deprecated for this model（E-014） |
| `claude-sonnet-5-5` 無 temperature（兩次） | 200，區塊皆 `['text']`，純 JSON，147～199 tokens |
| 重放頁面實際送出的請求體 | 200，三欄位齊全，例句含 algorithm |

## 其他發現

| 檢查 | 結果 |
|---|---|
| `prompt()` 按「取消」 | `vb-key` 被存成字串 `"null"`，之後 `getKey()` 不再詢問，每次 401。記為勘誤 **E-016**（低）。 |
| `show()` 以 `innerHTML` 插入模型輸出 | 注入風險，主辦決定不改，記為勘誤 **E-015**（中）。 |
| 收工儀式 `closes #5` | 寫死編號，併入 E-006。 |
