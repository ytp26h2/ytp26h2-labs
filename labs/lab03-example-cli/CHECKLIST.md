# Lab 3 驗收紀錄

驗證日期：2026-10-13｜驗證方式：本地執行（Python 3.13、anthropic SDK 1.13.0）、假回應單元測試、`git grep`、GitHub 頁面查核；同日稍晚 API key 到位，補做真實呼叫（模型 `claude-sonnet-5-5`，共約 25 次請求）。
金鑰處理：金鑰放在雲端環境變數 `YTP_ANTHROPIC_API_KEY`，只用 `[ -n "$YTP_ANTHROPIC_API_KEY" ]` 確認存在、不印內容；執行時以 `ANTHROPIC_API_KEY="$YTP_ANTHROPIC_API_KEY" python tools/gen_example.py <單字>` 只在該指令內傳入，不 export 到整個 shell。
狀態標記：✅ 通過｜⏳ 需 API key，待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 在 repo 裡搜尋不到你的 API key（`git grep sk-`） | ✅ | `git grep sk-` 只命中 PLAN 註解裡「git grep sk-」這句話本身，沒有任何金鑰。更精準的搜法是 `git grep 'sk-ant-'`，結果為空。金鑰只從環境變數 `ANTHROPIC_API_KEY` 讀取。 |
| 2 | v1 能對任意單字輸出例句；能說出同字兩次結果不同的原因 | ✅ | **教材原碼 v1 在真實呼叫時不能用**：第一次就噴 `AttributeError: 'ThinkingBlock' object has no attribute 'text'`（E-009 實證）；改用 `text_of()` 後輸出變成**空白**，因為 `max_tokens=300` 全被 thinking 區塊吃掉（新勘誤 E-011）。把 `max_tokens` 提到 2000 後 `algorithm` 兩次都成功，兩段輸出與心得貼在 issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6)。原因：模型每次是依機率分布**取樣**下一個 token，不是查表，所以同一個 prompt 會得到不同內容（教材 2.4）；本次兩段的例句句子恰好相同，差異出現在版面、聯想與補充，見下方「補做紀錄」第 1 項的討論。 |
| 3 | v2 對 5 個不同單字都回傳合法 JSON，且例句都真的含目標單字 | ✅ | `algorithm`、`recursion`、`vocabulary`、`persist`、`interval` 五個字各跑一次，全部 exit 0、輸出合法 JSON、四個欄位齊全、`sentence` 都含目標單字（大小寫不敏感），沒有一次走到罐頭。五句例句見下方「補做紀錄」第 3 項。驗證邏輯另以假回應離線測過五種情境（見下表）。 |
| 4 | 關掉網路再跑 v2，程式不噴 traceback，而是輸出罐頭內容 | ✅ | 以假 key 加不可達的 `ANTHROPIC_BASE_URL=http://127.0.0.1:9` 執行 `python tools/gen_example.py algorithm`：輸出罐頭 JSON（sentence「Practice makes perfect.」），exit code 0，無 traceback，耗時約 4 秒（SDK 內建重試 2 次 × 程式重試 1 次）。 |
| 5 | PR 已合併、issue 自動關閉、本地 main 已同步 | ✅ | PR [#7](https://github.com/ytp26h2/ytp26h2-labs/pull/7) 由管理員 `tw-ytp` 於 2026-10-13 合併（merge commit `e6ae96b`）；issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6) 由 `closes #6` 自動關閉（GitHub 顯示 closed by PR #7，state_reason=completed）；本地 `main` 與 `origin/main` 皆為 `e6ae96b`；tag `lab3-done` 當時指向同一 commit，補驗 PR [#9](https://github.com/ytp26h2/ytp26h2-labs/pull/9) 合併後由管理員重建為指向 `64c4601`。 |

## 離線單元測試：v2 的驗證／重試／降階（把 `ask()` 換成假回應）

| 情境 | 呼叫次數 | 結果 |
|---|---|---|
| 第一次就回合法 JSON 且含單字 | 1 | 放行 |
| 第一次回非 JSON，第二次合法 | 2 | 第二次放行（重試生效） |
| 兩次都合法 JSON 但例句不含單字 | 2 | 降階罐頭 |
| 兩次都回 markdown 圍欄包住的 JSON | 2 | 降階罐頭（`json.loads` 失敗） |
| 兩次都缺 `sentence` 欄位 | 2 | 降階罐頭（`KeyError`） |

## 補做紀錄（2026-10-13，API key 到位後）

原「待 API key 到位後補做」四項，全部完成。v1 用的是 commit `d89f7be` 的教材原碼（`git show d89f7be:labs/lab03-example-cli/tools/gen_example.py`），只為了跑得起來改兩處：`print(msg.content[0].text)` 改成依 type 取文字（同 `text_of()`），`max_tokens` 由 300 改 2000。v2 用 `main` 上的現行程式，**一行未改**。

1. **v1 跑 `algorithm` 兩次（取樣）**：兩段完整輸出已貼 issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6)。兩次例句句子一模一樣（`The app uses an algorithm to choose videos that you might like.`），但標題層級、音標寫法、聯想的鋪陳、詞源補充的措辭都不同；輸出長度一次 561、一次 716 tokens。心得：取樣讓每個 token 都有機率變化，約束越強的部分（B1、要含 algorithm、要簡單）最可能的句子就越容易重複，約束弱的部分（版面、聯想）差異最明顯；所以「同字兩次不同」要看整段輸出，不能只盯例句那一句。
2. **v1 把 B1 改 C2**：例句從一句 13 個字的簡單句，變成 30 個字、含 `ostensible`、`inadvertently`、`perpetuated`、`purportedly` 的長句，模型還自動加了「C2 重點詞」與常見搭配兩節；輸出 1025 tokens。心得寫在 issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6)。
3. **v2 五個字**（驗收時為 `max_tokens=300` 的現行程式），全部合法 JSON、含單字、exit 0。驗收後主辦決定把 v2 改為 `max_tokens=1024`（E-011），改完再跑 `recursion` 一次：合法 JSON、含單字、exit 0；斷網降階測試重跑仍輸出罐頭、exit 0。
   - algorithm：`The app uses a smart algorithm to suggest songs that you might like.`
   - recursion：`In my computer class, we learned that recursion means a function calls itself to solve a smaller part of the same problem.`
   - vocabulary：`Reading English books every day helps me build a larger vocabulary.`
   - persist：`If you persist in practicing every day, your English will get better little by little.`
   - interval：`There was a short interval between the two parts of the concert, so we bought some water.`

   注意 `zh` 欄位的語意不穩：五次裡三次是「例句的中文翻譯」，兩次（algorithm、persist）是「單字的中文解釋」。prompt 只寫了 `"zh": "..."` 沒說明是什麼，模型自己猜。這不影響本 Lab 驗收，但 Sprint 2 要把例句上卡片時得把 prompt 寫清楚（或改用 Structured Output）。
4. **E-009 驗證**：真實呼叫的回應 `content` 確實是區塊列表，thinking 區塊**會不會出現取決於 prompt**，同一支程式也不是每次都一樣，所以必須依 type 挑 text 區塊，不能賭 `content[0]`。實測如下表。

### E-009／E-011 實測：回應區塊型態（`claude-sonnet-5-5`，`max_tokens=300`）

| prompt | 第 1 次 | 第 2 次 | 第 3 次 | stop_reason | 說明 |
|---|---|---|---|---|---|
| v1 自由文字（教材原碼） | `['thinking']` | `['thinking']` | `['thinking', 'text']` | 三次都 `max_tokens` | `content[0]` 三次都是 thinking → 教材 `.text` 必噴 `AttributeError`（E-009 成立）。且 300 tokens 幾乎全被 thinking 用掉，文字區塊空的或被截斷（E-011）。 |
| v2 只回 JSON（現行程式） | `['text']` | `['text']` | `['text']` | 三次都 `end_turn` | 輸出 153～180 tokens，300 夠用；五個字的正式驗收加這三次共 8 次都沒出現 thinking。但這是「這個 prompt 剛好沒觸發」，不是保證，`text_of()` 仍必要。 |
| v1 + `output_config={"effort": "low"}` | `['text']` | `['text']` | — | 兩次都 `max_tokens` | 降低 effort 後 thinking 區塊消失，但自由文字回答本身就 330～380 tokens，300 仍截斷。 |
| v1 + `thinking={"type": "between_tools"}` | `['text']` | `['text']` | — | `max_tokens`／`end_turn` | 同上，關掉 thinking 不夠，`max_tokens` 本身太小。 |
| v1 + `max_tokens=2000`（本次實驗用） | `['thinking', 'text']` | `['thinking', 'text']` | `['thinking', 'text']` | 三次都 `end_turn` | 561／716／1025 tokens，正常完成。**這是 v1 的正確修法：`text_of()` ＋ 放大 `max_tokens`。** |

結論：E-009 由「待真實呼叫驗證」改為「已驗證」；另立 E-011（`max_tokens=300` 對 v1 太小）。兩者都是「高」嚴重度，因為學生照教材 v1 一行不改，第一步就會卡住。本 repo 的 v2 依主辦決定改為 `max_tokens=1024`；`zh` 欄位語意不穩的問題留給 Sprint 2。
