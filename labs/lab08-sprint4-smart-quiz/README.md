# Lab 8（Sprint 4）：智慧出題與多人共編

> 教材：<https://tw-ytp.github.io/vocabuddy/#/3-4>（v2.0）
> 目標：讓 AI 針對你的弱點出題（RAG-lite），讓單字包獨立成檔走 PR 共編，資料也要 review
> 時間：約 1.5–2.5 小時｜前置：完成 Lab 7；Node.js；一把 API key
> 檢查點 tag：`sprint4-done`（第三篇完賽）

## 這是什麼

兩件事。第一，頁面多一顆常駐的「考我弱點」按鈕：從 `log` 檢索錯誤率最高的三個字，塞進 prompt 讓 AI 出一題四選一克漏字；選項不是四個、或答案不在選項裡，寧可不出題；答題結果寫回 `log`，之後更常被考。第二，`WORDS` 搬進 `words.js`，隊友的貢獻變成「對資料的 PR」，合併前跑 `check_words.js` 檢查欄位缺漏與重複字。

## 怎麼執行

```bash
cd labs/lab08-sprint4-smart-quiz
node check_words.js     # words.js 檢查通過，共 N 字 ✓
node test_srs.js        # 4 tests passed ✓
```

瀏覽器直接開 `index.html`。「考我弱點」第一次按會要 API key（同 Lab 6，只存你自己的瀏覽器）。

## 技術

- **弱點檢索**：`weakest(k)` 對 `WORDS` 算 `wrong / (seen || 1)` 排序取前 k，這就是 RAG 的「檢索」。
- **RAG-lite**：檢索結果塞進 user prompt，system 給 JSON 骨架，`JSON.parse` 後驗證 `options` 長度 4 且含 `answer`。
- **`callClaude(system, user)`**：教材只說「把 Sprint 2 的 fetch 抽成共用函式」沒給程式，本 repo 把 Lab 6 的 fetch 原樣抽出（含 E-007／E-009／E-011／E-014 四處新模型修改），`aiExample()` 與 `smartQuiz()` 共用。
- **資料檢查**：`check_words.js` 是第四篇 CI 的種子，現在手動跑，之後讓 GitHub 每次 PR 自動跑。

## 作者

YTP2026H2 主辦（助教範本）。全程透過 Claude 在瀏覽器中完成。

---

## Plan（已確認，同步寫在 `index.html` 頂端註解）

見 `index.html` 頂端的 PLAN 註解，共 9 步。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 開 issue、開分支 | issue「Sprint 4：智慧出題＋單字包共編」；`git switch -c feature/smart-quiz` | issue [#21](https://github.com/ytp26h2/ytp26h2-labs/issues/21)；分支 `lab08/feature/smart-quiz`（從 `main` 開）。 |
| 單字包獨立成檔 | `words.js`、`check_words.js`，故意加重複字跑跑看 | 照教材原碼。重複字、缺 `zh` 各測一次，都被擋下。 |
| 弱點檢索 | `weakest(k)` | 照教材原碼。 |
| AI 出題 | 「考我弱點」鈕、`#quiz`、`smartQuiz()`，`callClaude` 抽成共用函式 | `smartQuiz()` 照教材原碼（system 多一句「不要 markdown 圍欄」）；`callClaude` 由本 repo 補寫（教材未給，E-022）。 |
| 多人共編演練 | 分支 `feature/words-animals` 加 8–10 個動物單字 → PR → reviewer 跑 `check_words.js`、抽查翻譯、留評論 → merge | 第一個 PR 合併後，從 `main` 開 `lab08/feature/words-animals`，第二個 PR 由同一作者換 reviewer 帽子留 review，管理員合併。見 `CHECKLIST.md` 第 5 項。 |
| 收工 | commit `closes #7` → PR → merge → `tag sprint4-done` | commit 用實際編號 #21；tag 由管理員以 Release 建立。 |

## 驗收清單

見 `CHECKLIST.md`。教材原始六項：

1. `node check_words.js` 通過；塞入重複字或缺欄位時會確實報錯
2. 「考我弱點」出的題目來自你錯誤率高的字
3. 格式不合格的題目不會顯示
4. 測驗答錯會寫回 `log`
5. 第二個單字包經完整 PR 流程合併
6. 四個 sprint tag 齊了

## 實作時發現的三件事（勘誤 E-020～E-022）

1. **`smartQuiz()` 用 `innerHTML` 插入 `q.question`、`q.why`**，與 Lab 6 的 E-015 同類：模型輸出直接當 HTML。本 repo 照教材不改。
2. **答題寫回以 `log[q.answer]` 為鍵**。模型回的答案字串若大小寫不同（實測 mock 回 `"Algorithm"`）或不是單字包裡的字，會在 `log` 產生新鍵，本尊的錯誤率不變，弱點分析失準。建議先把 `q.answer` 對回 `weakest()` 給的字，對不到就當格式不合格。
3. **`callClaude` 教材沒給程式**，`aiExample` 要改成用它教材也沒提。本 repo 的寫法在 `index.html` 的 `callClaude()` 註解。

## 常見錯誤急救（本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| `WORDS is not defined` | `words.js` 要在主 script 之前引入，且放在 `srs.js` 前後皆可。 |
| `check_words.js` 說 `Cannot find module './words.js'` | 要在本資料夾執行，或用 `node labs/lab08-sprint4-smart-quiz/check_words.js` 的相對路徑。 |
| 「考我弱點」一直「AI 暫時不可用」但網路正常 | F12 → Network 看回應；也可能是模型回了 markdown 圍欄或三個選項被驗證擋下，再按一次通常就好。 |
| 考出來的字都一樣 | `weakest()` 只看錯誤率，沒錯過的字 rate 為 0 排在後面；多錯幾個不同的字，或清掉 `vb-log` 重來。 |
