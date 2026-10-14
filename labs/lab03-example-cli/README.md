# Lab 3：例句生成 CLI——第一次讓程式呼叫 AI

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab3>（v2.0）
> 目標：用 Python 呼叫 Claude API，做出「單字 → 例句＋翻譯＋聯想」的命令列工具（CLI）
> 時間：約 60–90 分鐘｜前置：Python 3.10+、一把 API key（申請方式見教材附錄 B）
> 檢查點 tag：`lab3-done`

## 這是什麼

`tools/gen_example.py`：給一個英文單字，回傳例句、中文翻譯、聯想記憶。v1 是自由文字；v2 只回 JSON、驗證例句真的含那個字、失敗重試一次、再失敗就給罐頭內容。網頁 `index.html` 沿用 Lab 2，本 Lab 不動它。

## 怎麼執行

```bash
cd labs/lab03-example-cli
pip install -r tools/requirements.txt
export ANTHROPIC_API_KEY="你的key"     # macOS / Linux；Windows PowerShell 用 setx 後重開終端機
python tools/gen_example.py algorithm
```

金鑰只放環境變數，不放程式碼、不 commit。`.gitignore` 已排除 `.env`。

## 技術

- `anthropic` 官方 Python SDK 1.x（需 Python 3.10+）。
- 模型 `claude-sonnet-5-5`（主辦指定；教材 v2.1 已更新為此型號，見勘誤 E-007）。
- v2 資料流：prompt 要求只回 JSON → `json.loads` → 檢查 `sentence` 含單字 → 失敗重試一次 → 降階罐頭。這就是教材 2.8 的「驗證＋降階」。

## 作者

YTP2026H2 主辦（助教範本）。全程透過 Claude 在瀏覽器中完成。

---

## Plan（已確認，同步寫在 `tools/gen_example.py` 的模組 docstring）

見 `tools/gen_example.py` 頂端，共 10 步。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 1 環境與金鑰 | `pip install anthropic`、`export ANTHROPIC_API_KEY` | 裝到 SDK 1.13.0。雲端環境沒有 key，金鑰由主辦放進環境設定（不貼對話）。 |
| 2 開任務、開分支 | issue「AI 例句生成 CLI」（假設 #2）、`feature/example-cli`、`mkdir tools` | issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6)、分支 `lab03/feature/example-cli`（從 `main` 開）、`labs/lab03-example-cli/tools/`。 |
| 3 v1 | `tools/gen_example.py` 自由文字 | 照教材原碼，`MODEL` 改為 `claude-sonnet-5-5`。commit `lab03: feat: 例句生成 CLI v1`。 |
| 4 兩個實驗 | 同字跑兩次；B1 改 C2 | 2026-10-13 key 到位後補做。教材原碼 v1 真實呼叫時先噴 `AttributeError`（E-009），修好後輸出空白（E-011），改 `text_of()` 並把 `max_tokens` 提到 2000 才跑成。輸出與心得在 issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6)，實測表在 `CHECKLIST.md`。 |
| 5 v2 | JSON＋驗證＋降階 | 照教材架構，三處小改（見下）。commit 訊息含 `closes #6`。 |
| 6 走完 GitHub Flow | commit → push → PR → review → merge → 本地同步 | PR 三段描述；自我 review 行內評論；由管理員 `tw-ytp` 合併。 |

### v2 與教材原碼的三處差異（都是為了在新模型上跑得動）

1. **`text_of()` 依 type 取文字區塊**。新一代模型預設會先回一個 `thinking` 區塊，教材的 `msg.content[0].text` 會拿到非文字區塊而失敗。改為把所有 `type == "text"` 的區塊接起來。（勘誤 E-009）
2. **prompt 多一句「不要 markdown 圍欄」**。教材急救表自己也建議這麼做，直接放進 prompt。
3. **`except` 多接 `TypeError`**。模型若回 JSON 陣列或字串，`data["sentence"]` 丟的是 `TypeError` 不是 `KeyError`，教材原碼會噴 traceback。

另一個真實呼叫後才發現的問題：**v1 的 `max_tokens=300` 太小**（勘誤 E-011）。新模型的 thinking token 也算在 `max_tokens` 裡，v1 的自由文字 prompt 會讓 300 幾乎全被 thinking 用掉，印出來是空白。v2 只回 JSON（約 150～180 tokens）、實測八次都沒觸發 thinking，300 當下夠用；但主辦決定本 repo 的 v2 仍改為 `max_tokens=1024` 留餘裕（補驗 PR），自己改 v1 來做實驗時請提到 2000。

## 怎麼在沒有網路時測降階（教材驗收第 4 項）

```bash
ANTHROPIC_API_KEY=sk-ant-dummy ANTHROPIC_BASE_URL=http://127.0.0.1:9 python tools/gen_example.py algorithm
```

把 base URL 指到一個不存在的位址，效果等同斷網。應該在幾秒內印出罐頭 JSON，exit code 0。注意：**完全沒設 key** 時，SDK 在建立 client 那一刻就會丟例外，不在 `try` 範圍內，所以還是會 traceback。教材的降階只涵蓋「有 key 但連不上」，見勘誤 E-010。

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. repo 裡搜尋不到 API key
2. v1 能輸出例句；能用「取樣」解釋同字兩次不同
3. v2 對 5 個單字都回合法 JSON 且含單字
4. 斷網跑 v2 不噴 traceback，輸出罐頭
5. PR 合併、issue 自動關閉、本地 main 同步

## 常見錯誤急救（教材原表，另加本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| `ModuleNotFoundError: anthropic` | 裝錯環境。確認 pip 與 python 是同一套（`python -m pip install anthropic`）。 |
| `401 authentication_error` | 環境變數沒設好或終端機沒重開。`echo $ANTHROPIC_API_KEY` 檢查。 |
| `429 rate_limit_error` | 呼叫太快或額度用盡。等幾十秒重試；批次任務在迴圈裡加 `time.sleep`。 |
| JSON 常常解析失敗 | prompt 再強調「只輸出 JSON、不要 markdown 圍欄」。第三篇教更穩的 Structured Output。 |
| 中文變成 `\uXXXX` | 印出時用 `ensure_ascii=False`（v2 已含）。 |
| （補充）`TypeError: Could not resolve authentication method` | 完全沒設 key。SDK 1.x 在 `anthropic.Anthropic()` 就會丟這個，不是 401。設好環境變數再跑。 |
| （補充）`AttributeError: 'ThinkingBlock' object has no attribute 'text'` | 用了教材的 `content[0].text`，而模型先回了 thinking 區塊。改用本 Lab 的 `text_of()`。2026-10-13 真實呼叫實證：教材 v1 原碼三次都中。 |
| （補充）v1 印出空白、或 v2 每次都是罐頭 | `max_tokens=300` 被 thinking 區塊吃光，`msg.stop_reason` 會是 `"max_tokens"`。v1 把 `max_tokens` 提到 2000；v2 提到 1024（本 repo 已改）。見勘誤 E-011。 |
| （補充）pip 說找不到符合 Python 版本的 anthropic 1.x | Python 低於 3.10。升級 Python，或接受 pip 退回 0.x 舊版（教材寫法仍可用）。 |
