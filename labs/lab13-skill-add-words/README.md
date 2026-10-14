# Lab 13：你的第一個技能——add-words

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab13>（v2.0），內容照 5.5 與 Lab 13 頁
> 目標：把「新增單字」的完整流程包成一個技能，並驗證它會在該觸發的時候觸發
> 時間：約 45 分鐘｜前置：Lab 12 完成；倉庫裡有 `words.js` 與 `check_words.js`
> 檢查點 tag：`lab13-done`

## 這是什麼

專案指示檔（Lab 12）管「永遠要遵守的事」，每次啟動都讀；技能管「某一類任務才要照的步驟」，請求符合 description 時才讀。本 Lab 的產物是 [`.claude/skills/add-words/SKILL.md`](../../.claude/skills/add-words/SKILL.md)：新增單字的六步流程。本資料夾只有 README 與 CHECKLIST；正負兩個觸發測試的紀錄在 `CHECKLIST.md`。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 問出技能檔要放哪 | 直接問工具確切路徑與 frontmatter 必填欄位 | 全新 `claude -p` session 答：專案層級 `.claude/skills/<name>/SKILL.md`，必填 `name`、`description`；它還主動說「依 CLAUDE.md 要走 issue、分支、PR」。 |
| 先想清楚要包哪件事 | 一句話：「當我想做＿＿的時候，我希望它自動照著＿＿做」 | 「當我想新增或修改單字包的時候，希望它自動照著讀格式 → 加在最後 → 跑 check_words.js → 用規定訊息 commit → 不自動 push 做」（issue #39）。 |
| 建立技能，description 當主角 | frontmatter 寫「什麼時候該用」，內容六步 | description 列出使用者可能的說法（加單字、新增單字、加幾個某主題的字、改字表、動 words.js、單字包）；六步照教材，路徑改成 `labs/lab10-graduation/words.js`，commit 訊息改成本 repo 的 `labNN: feat: 新增 N 個「主題」單字`，第 6 條不自動 push 照寫。 |
| 驗證它真的會被觸發 | 清空工作階段，只說「幫我加三個天氣主題的單字。」 | 全新 `claude -p` session（工具限定 Read／Edit／`node check_words.js`／`git add`、`git commit`，不含 push）：自動 `Skill add-words` → 讀 `words.js` → 加在最後並加 `// 天氣主題單字` → `check_words.js` 24 字 ✓ → 只 commit `words.js` → 沒有 push，還主動回報「push 請人做」。全中。 |
| 負面測試 | 「幫我把卡片的圓角改大一點。」不應跑 check_words.js | 全新 session 只 `Grep border-radius` 與讀 `index.html`，指出第 40 行；沒有載入技能、沒有跑 `check_words.js`。 |
| 進版控、發 PR | `feat:` commit，PR 三段式，「怎麼驗證」寫兩個測試 | 分支 `lab13/feature/skill-add-words`；PR 的「怎麼驗證」就是上面兩個測試。 |

## 本 repo 的適配與發現

- **「清空工作階段」**：同 Lab 12，用容器內 `claude -p` 開全新 session。正面測試需要它真的改檔與執行指令，所以用 `--allowedTools` 只放行讀檔、改檔、`node check_words.js`、`git add`／`git commit`，push 不在清單裡；用 `--output-format stream-json --verbose` 把每一個工具呼叫錄下來當證據。
- **步驟太籠統會被抓到（教材卡住了？⑤）**：第一版第 5 條寫「NN 看 `docs/LAB_GUIDE.md` 狀態表最新的 ✅ 列」，全新 session 照做填了 `lab12:`，因為 Lab 13 做到一半還沒標完成；它自己也指出分支名是 `lab13/…`。修正為「NN 取分支名開頭的 `labNN`，沒有就問人」，commit 訊息由人改成 `lab13:`。
- **全新 session 的模型**：容器內 CLI 預設是 `claude-sonnet-5-5`（commit 的 Co-Authored-By 可見），和本 session 的 `claude-fable-5-1` 不同；技能照樣被正確觸發，說明觸發靠的是 description，不是特定模型。
- **換工具要改哪裡**：技能格式是開放標準（agentskills.io），內容照搬；只有資料夾不同（Codex／Antigravity `.agents/skills`、Copilot `.github/skills`）。本 repo 只放 Claude Code 一套。

## 怎麼驗證

```sh
python3 -c "import yaml,re;s=open('.claude/skills/add-words/SKILL.md').read();print(yaml.safe_load(re.match(r'^---\n(.*?)\n---',s,re.S).group(1)))"
cd labs/lab10-graduation && node check_words.js && node test_srs.js && node test_csv.js
```

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. 技能資料夾與 SKILL.md 建好，frontmatter 有 name 與 description
2. description 寫的是「什麼時候該用」，不是「這是什麼」
3. 正面測試通過：不提技能的自然請求，它自動照流程做完
4. 負面測試通過：不相干的請求不會誤觸發
5. 技能已進版控，經 PR 合併

## Plan（已確認）

1. issue #39；分支 `lab13/feature/skill-add-words`。
2. 步驟 1 問出位置：`.claude/skills/add-words/SKILL.md`，必填 `name`、`description`。
3. 寫 SKILL.md：description 寫「什麼時候該用」並列出使用者說法；六步照教材，路徑與 commit 格式改本 repo 的。
4. 正面測試：全新 session 只說「幫我加三個天氣主題的單字。」，stream-json 記錄每個工具呼叫；產物留在 PR。
5. 負面測試：「幫我把卡片的圓角改大一點。」，不應載入技能、不應跑 check_words.js。
6. 驗證：frontmatter 可解析；測試與 check_words.js；無頭 Chromium；CI。
7. commit → PR（三段式）→ 主辦 review 合併 → Release `lab13-done`。
8. 文件：本資料夾、LAB_GUIDE 第 13 列與段落（補 Lab 12 檢查點）、根 README、ERRATA。
