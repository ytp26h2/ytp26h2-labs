# Lab 3 驗收紀錄

驗證日期：2026-10-13｜驗證方式：本地執行（Python 3.13、anthropic SDK 1.13.0）、假回應單元測試、`git grep`、GitHub 頁面查核。
狀態標記：✅ 通過｜⏳ 需 API key，待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 在 repo 裡搜尋不到你的 API key（`git grep sk-`） | ✅ | `git grep sk-` 只命中 PLAN 註解裡「git grep sk-」這句話本身，沒有任何金鑰。更精準的搜法是 `git grep 'sk-ant-'`，結果為空。金鑰只從環境變數 `ANTHROPIC_API_KEY` 讀取。 |
| 2 | v1 能對任意單字輸出例句；能說出同字兩次結果不同的原因 | ⏳ | 程式已完成、`py_compile` 通過。環境沒有 API key，尚未真的呼叫。原因：模型每次是依機率分布**取樣**下一個 token，不是查表，所以同一個 prompt 會得到不同句子（教材 2.4）。 |
| 3 | v2 對 5 個不同單字都回傳合法 JSON，且例句都真的含目標單字 | ⏳ | 需 API key。驗證邏輯已用假回應離線測試五種情境（見下表）。 |
| 4 | 關掉網路再跑 v2，程式不噴 traceback，而是輸出罐頭內容 | ✅ | 以假 key 加不可達的 `ANTHROPIC_BASE_URL=http://127.0.0.1:9` 執行 `python tools/gen_example.py algorithm`：輸出罐頭 JSON（sentence「Practice makes perfect.」），exit code 0，無 traceback，耗時約 4 秒（SDK 內建重試 2 次 × 程式重試 1 次）。 |
| 5 | PR 已合併、issue 自動關閉、本地 main 已同步 | ⏳ | issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6)，PR 開出後等管理員合併，合併後補記。 |

## 離線單元測試：v2 的驗證／重試／降階（把 `ask()` 換成假回應）

| 情境 | 呼叫次數 | 結果 |
|---|---|---|
| 第一次就回合法 JSON 且含單字 | 1 | 放行 |
| 第一次回非 JSON，第二次合法 | 2 | 第二次放行（重試生效） |
| 兩次都合法 JSON 但例句不含單字 | 2 | 降階罐頭 |
| 兩次都回 markdown 圍欄包住的 JSON | 2 | 降階罐頭（`json.loads` 失敗） |
| 兩次都缺 `sentence` 欄位 | 2 | 降階罐頭（`KeyError`） |

## 待 API key 到位後補做

1. v1 跑 `algorithm` 兩次，貼兩段輸出到 issue #6，寫兩行「取樣」心得。
2. v1 把 system prompt 的 B1 改成 C2 再跑一次，比較難度，心得寫進 issue #6。
3. v2 跑 `algorithm`、`recursion`、`vocabulary`、`persist`、`interval` 五個字，確認 JSON 合法且含單字，結果記回本表第 3 項。
4. 確認真實回應經 `text_of()` 取得文字（驗證 E-009 的假設）。
