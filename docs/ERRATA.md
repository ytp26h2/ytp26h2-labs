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
| E-007 | Lab 3 程式碼、附錄 B | `MODEL = "claude-sonnet-4-5"` | 模型名稱已過時。目前可用的是 Claude 5 系列（`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-opus-5-5`）。教材正文有「最新值見附錄 B」的保險，但附錄 B 本身需要重查。 | 附錄 B 第二篇區更新模型名稱與查證日期；Lab 3 程式碼註解維持「見附錄 B」。 | 中 | 待回報 |
| E-008 | Lab 3 前置 | 「Python 3.9+」 | `anthropic` SDK 1.x（2026 年起的主線版本）要求 Python 3.10+。3.9 的學生 `pip install anthropic` 會靜默裝到 0.x 舊版，之後查文件會對不上。 | 前置改為「Python 3.10+」，急救表補一列。 | 低 | 待回報 |
| E-009 | Lab 3 v1、v2 | `print(msg.content[0].text)`、`return msg.content[0].text` | 新一代模型（Sonnet 5.5、Opus 5.5 等）預設啟用 adaptive thinking，回應的 `content` 第一個區塊常是 `thinking` 而非 `text`，`.text` 會丟 `AttributeError`。學生照抄會在第一步就卡住。 | 改為依 type 取文字：`"".join(b.text for b in msg.content if b.type == "text")`，並在 2.5 說明回應是「區塊列表」。 | 高 | 待回報（2026-10-13 已真實呼叫驗證：v1 原碼三次皆 `content[0]` 為 thinking，`.text` 噴 `AttributeError`；v2 的 JSON prompt 八次皆只有 text 區塊，證明是否出現 thinking 取決於 prompt，不可預期。實測見 Lab 3 `CHECKLIST.md`） |
| E-010 | Lab 3 v2、驗收第 4 項 | 「關掉網路再跑 v2——程式不噴 traceback」 | `anthropic.Anthropic()` 在 `try` 之外；若環境變數根本沒設，SDK 1.x 在建立 client 時就丟 `TypeError`，降階接不到。斷網但有 key 的情況才會走到降階。 | 把 client 建立移進 `try`，或在開頭檢查 `os.environ.get("ANTHROPIC_API_KEY")` 並給友善訊息；急救表補一列。 | 低 | 待回報 |
| E-011 | Lab 3 v1（v2 亦受影響） | `max_tokens=300` | 新模型預設 adaptive thinking，thinking 區塊的 token **也算在 `max_tokens` 內**。v1 的自由文字 prompt 實測三次 300 tokens 幾乎全被 thinking 吃掉（`stop_reason=max_tokens`），就算修好 E-009，印出來也是空白或半句。即使用 `output_config={"effort": "low"}` 關掉 thinking，v1 的回答本身也要 330～380 tokens，300 仍截斷。v2 的 JSON 回答約 150～180 tokens、八次都沒觸發 thinking，暫時夠用，但一旦出現 thinking 會直接走到罐頭，學生看不出原因。 | v1 的 `max_tokens` 改為 2000（或至少 1024）；v2 建議改 1024 留餘裕；2.5 補一句「`max_tokens` 包含 thinking 的 token，看到 `stop_reason == "max_tokens"` 就是不夠」。 | 高 | 待回報 |
