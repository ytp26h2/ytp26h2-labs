# Lab 3 驗收紀錄

驗證日期：2026-10-13｜驗證方式：本地執行（Python 3.13、anthropic SDK 1.13.0）、假回應單元測試、`git grep`、GitHub 頁面查核。
狀態標記：✅ 通過｜⏳ 需 API key，待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 在 repo 裡搜尋不到你的 API key（`git grep sk-`） | ✅ | `git grep sk-` 只命中 PLAN 註解裡「git grep sk-」這句話本身，沒有任何金鑰。更精準的搜法是 `git grep 'sk-ant-'`，結果為空。金鑰只從環境變數 `ANTHROPIC_API_KEY` 讀取。 |
| 2 | v1 能對任意單字輸出例句；能說出同字兩次結果不同的原因 | ⏳ | 程式已完成、`py_compile` 通過。環境沒有 API key，尚未真的呼叫。原因：模型每次是依機率分布**取樣**下一個 token，不是查表，所以同一個 prompt 會得到不同句子（教材 2.4）。 |
| 3 | v2 對 5 個不同單字都回傳合法 JSON，且例句都真的含目標單字 | ⏳ | 需 API key。驗證邏輯已用假回應離線測試五種情境（見下表）。 |
| 4 | 關掉網路再跑 v2，程式不噴 traceback，而是輸出罐頭內容 | ✅ | 以假 key 加不可達的 `ANTHROPIC_BASE_URL=http://127.0.0.1:9` 執行 `python tools/gen_example.py algorithm`：輸出罐頭 JSON（sentence「Practice makes perfect.」），exit code 0，無 traceback，耗時約 4 秒（SDK 內建重試 2 次 × 程式重試 1 次）。 |
| 5 | PR 已合併、issue 自動關閉、本地 main 已同步 | ✅ | PR [#7](https://github.com/ytp26h2/ytp26h2-labs/pull/7) 由 `tw-ytp` 於 2026-10-13 17:58（+0800）合併，合併 commit `e6ae96b`。issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6) 同一時刻由 commit 訊息的 `closes #6` 自動關閉（state_reason=completed）。新 session 以 `origin/main` 起始，`git log -1` 即為 `e6ae96b`；tag `lab3-done` 也已由管理員建立並指向 `e6ae96b`。 |

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

### 補做紀錄

- **2026-10-13（第二個 session）**：嘗試補做上列四項，但 session 的執行環境裡讀不到 `ANTHROPIC_API_KEY`（`test -n` 為空；SDK 1.13.0 零參數建立 client 後發出請求時丟 `TypeError: Could not resolve authentication method`，即沒有任何憑證來源）。真實呼叫一律不以假資料代替，四項維持 ⏳。推測原因：金鑰在本 session 啟動**之後**才寫入環境設定，或寫在別的變數名；雲端環境的變數要新 session 才會載入。
- 補做步驟（任何有金鑰的 session 都可照做）：
  1. `cd labs/lab03-example-cli && pip install -r tools/requirements.txt`，用 `test -n "$ANTHROPIC_API_KEY" && echo present` 確認（不要 `echo` 金鑰本身）。
  2. E-009：先用 SDK 直接發一次 v1 請求，印出 `[b.type for b in msg.content]`；若第一個區塊是 `thinking`，E-009 成立，狀態改「已驗證」。
  3. 實驗 1：同一 system prompt 對 `algorithm` 跑兩次，兩段輸出貼到 issue #6。
  4. 實驗 2：system prompt 的 B1 改 C2 再跑一次，比較後把心得貼到 issue #6。
  5. `for w in algorithm recursion vocabulary persist interval; do python tools/gen_example.py $w; done`，確認五個都不是罐頭（`tip` 不等於「（預設內容：AI 暫時不可用）」）且 `sentence` 含該字，結果記回本表第 3 項。
