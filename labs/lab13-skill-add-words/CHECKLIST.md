# Lab 13 驗收紀錄

驗證日期：2026-10-14｜驗證方式：正負測試以容器內 Claude Code CLI `claude -p` 開全新非互動 session（等價於教材的「清空工作階段」），`--output-format stream-json --verbose` 錄下每個工具呼叫（全文存於驗證環境，摘錄於下）；程式部分以 Node 22 與無頭 Chromium 驗證。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

## 教材驗收清單（Lab 13 頁）

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 技能資料夾與 SKILL.md 建好，frontmatter 有 name 與 description | ✅ | `.claude/skills/add-words/SKILL.md`；`yaml.safe_load` 解析出 `{name: add-words, description: …}`，恰好兩個欄位。位置是教材步驟 1 問出來的（見下）。 |
| 2 | description 寫的是「什麼時候該用」，不是「這是什麼」 | ✅ | 「新增或修改單字包時使用。使用者說『加單字』『新增單字』『加幾個某主題的字』『改字表』『動 words.js』『單字包』都算。包含…驗證與 commit 訊息格式。」 |
| 3 | 正面測試通過：不提技能的自然請求，它自動照流程做完 | ✅ | 全新 session 只說「幫我加三個天氣主題的單字。」。工具呼叫序列：`Skill add-words` → `Read words.js` → `Grep ✅`（找 Lab 編號）→ `Edit words.js`（加在最後、`// 天氣主題單字`）→ `Bash node check_words.js`（「共 24 字 ✓」）→ `git status` → `git add words.js && git commit`（只含 words.js）→ 回報「我沒有 push」。11 回合。 |
| 4 | 負面測試通過：不相干的請求不會誤觸發 | ✅ | 全新 session 說「幫我把卡片的圓角改大一點。」。工具呼叫只有 `Grep border-radius`、`Read index.html`，指出第 40 行 `border-radius:14px`；沒有 `Skill`、沒有 `check_words.js`。3 回合。 |
| 5 | 技能已進版控，經 PR 合併 | ⏳ | 分支 `lab13/feature/skill-add-words`，commit `ad6f507`（技能）、`7ed5757`（正面測試產物）、`c900513`（第 5 條修正）；PR 合併後補記。 |

## 步驟 1：問工具技能放哪

> 技能（skill）檔案在你這裡要放在哪個資料夾？請給我確切路徑，並說明 SKILL.md 的 frontmatter 有哪些必填欄位。

全新 session 答：專案層級 `/home/user/ytp26h2-labs/.claude/skills/<skill 名稱>/SKILL.md`（跟 repo 一起 commit），個人層級 `~/.claude/skills/`；必填 `name`（小寫英文、數字、連字號，與資料夾同名）與 `description`（寫使用情境，工具靠它判斷要不要載入）；`allowed-tools` 等選填。它誠實註明「憑記憶回答、沒查這個環境的版本文件」，並主動提到「依 CLAUDE.md 要走 issue、分支、PR 的流程」。

## 正面測試：工具呼叫摘錄

| 步 | 工具 | 內容 | 對應技能步驟 |
|---|---|---|---|
| 1 | `Skill` | `add-words` | 觸發 |
| 2 | `Bash` | `cd … && tail words.js && grep ✅ LAB_GUIDE && git branch`（被 CLI 的指令守門擋下兩次，改用專用工具） | — |
| 3 | `Read` | `labs/lab10-graduation/words.js` | 1 讀格式 |
| 4 | `Grep` | `✅` in `docs/LAB_GUIDE.md` | 5 找 Lab 編號 |
| 5 | `Edit` | 在 `debug` 之後加 `// 天氣主題單字` 與 thunderstorm／drizzle／humid，不重排 | 2 加在最後 |
| 6 | `Bash` | `cd labs/lab10-graduation && node check_words.js` → `words.js 檢查通過，共 24 字 ✓` | 3 驗證 |
| 7 | `Bash` | `git branch --show-current; git status --short` | 5 |
| 8 | `Bash` | `git add words.js && git commit -m "lab12: feat: 新增 3 個「天氣」單字…"` | 5 commit |
| 9 | 文字 | 回報三個字、通過、commit 編號；指出「LAB_GUIDE 最新 ✅ 列是 Lab 12，但你的分支是 lab13/…，要改告訴我」；「我沒有 push」 | 6 不 push |

**瑕疵與修正**：第 5 條第一版寫「NN 看 LAB_GUIDE 最新 ✅ 列」，在 Lab 進行中會指到上一個 Lab，它照做填了 `lab12:`——步驟太籠統（教材卡住了？⑤）。修正為「NN 取分支名開頭的 `labNN`，沒有就問人」（commit `c900513`）；測試產物的 commit 訊息由人改為 `lab13:`（`7ed5757`，保留它的 Co-Authored-By）。

全新 session 的模型是 `claude-sonnet-5-5`（CLI 預設），本 session 是 `claude-fable-5-1`；技能仍正確觸發。

## 負面測試：工具呼叫摘錄

| 步 | 工具 | 內容 |
|---|---|---|
| 1 | `Grep` | `border-radius` |
| 2 | `Read` | `labs/lab10-graduation/index.html` |
| 3 | 文字 | 「第 40 行 `#card` 的 `border-radius:14px` 改大即可；另外兩處 8px 是按鈕與輸入框不用動；我只讀了檔沒有改」 |

沒有 `Skill`、沒有 `check_words.js`、沒有碰 `words.js`。

## 程式驗證（正面測試產物）

| 檢查 | 結果 |
|---|---|
| `node check_words.js` | 通過，共 24 字 |
| `node test_srs.js`、`node test_csv.js` | 通過 |
| 無頭 Chromium 複習到隊尾 | 依序看到 thunderstorm→雷雨、drizzle→毛毛雨、humid→潮濕的，無 JS 錯誤 |
| `git show --stat 7ed5757` | 只含 `labs/lab10-graduation/words.js`，4 行新增 1 行修改 |
