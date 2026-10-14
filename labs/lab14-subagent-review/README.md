# Lab 14：讓子代理幫你 review——code-reviewer

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab14>（v2.0），內容照 5.5 子代理段、5.7、5.8 與 Lab 14 頁
> 目標：做一個唯讀的 code review 子代理，對真實 PR 跑一次，並比較它與人審各自抓到什麼
> 時間：約 35 分鐘｜前置：Lab 13 完成
> 檢查點 tag：`lab14-done`

## 這是什麼

子代理在自己的上下文裡把事做完，只把結論回報給主對話（圖 31）。本 Lab 的產物是 [`.claude/agents/code-reviewer.md`](../../.claude/agents/code-reviewer.md)：唯讀、四面向、嚴格輸出格式。本 Lab 的重點不是子代理本身，是「機器審 vs 人審」的四格比較——那是這支隊伍對「哪些事能交給 AI」的第一份實測紀錄，寫在本 Lab PR 的留言裡，副本在 `CHECKLIST.md`。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 建立子代理 | 照 5.5 的表找位置，內容照抄四面向與輸出格式 | 先用 Lab 13 的習慣問全新 session：答 `.claude/agents/<name>.md`，`tools` 白名單、`disallowedTools`、`permissionMode` 等欄位，並提醒「不要給 Bash，Bash 能繞過唯讀」。內容照教材，多加「不要複述程式碼」「指不出行號就不要回報」「只回報值得修改的」。 |
| 把工具限制成唯讀 | 只能讀檔與搜尋 | `tools: Read, Grep, Glob`，再加 `permissionMode: plan` 當第二層保險。兩次實跑它的工具呼叫全是 Glob／Read／Grep。 |
| 對真實的 diff 跑一次 | 審 `feature/skill-add-words` 相對 main 的 diff | 審 `lab12-done..lab13-done`（PR #40 的 diff）。跑了兩次：第一次直接請它審，它誠實說沒有 Bash 跑不了 `git diff`、tag 物件在 pack 裡讀不到，改審工作樹裡 Lab 13 的檔案（E-032）；第二次主對話先跑 `git diff` 再把 diff 交給它。兩次主對話都只收到報告，沒有被 diff 塞滿。 |
| 你自己也審一次，然後比較 | 先別看它的報告，自己用 1.7 四面向審，填四格表 | 主辦先審 PR #40 的 Files changed，回覆「未發現問題」，之後才跑子代理。四格表見 CHECKLIST 與 PR 留言。 |
| 人工合併 | 依你同意的建議修正，由你按 merge | 採納 7 則、不採納 1 則（見 CHECKLIST），修正進本 PR；merge 由主辦按，並寫一句為什麼可以合。 |

## 本 repo 的適配與發現

- **唯讀子代理看不到 diff**：教材步驟 3 直接「請子代理審查 diff」，但沒有 Bash 的子代理既跑不了 `git diff`、也讀不到 pack 裡的舊版本。正確做法是主對話先取得 diff，把 diff 全文放進交給子代理的提示（第二次實跑就是這樣），或只放行 `Bash(git diff:*)` 這類唯讀指令。記為勘誤 E-032。
- **第二次主對話也有偏差**：它沒把兩個新增檔的逐行內容放進提示，而是請子代理自己去 Read；它主動說明了這個偏差。主對話的轉述也要驗（5.7）。
- **只有它抓到的那格很滿、只有人抓到的那格是空的**：這份 diff 小、以文件為主，主辦四面向未發現；子代理找到 7 處文件與流程一致性問題，全是低嚴重度但都成立。結論見 CHECKLIST「你剛剛量到的東西」。
- **它抓錯的那格要人判**：它說文件裡的模型名稱「沒有證據可查」，但 commit `7ed5757` 的 Co-Authored-By 與 `get_session` 就是證據——自信但錯，正是教材要你記下來的那類。
- **它的建議讓 Lab 13 的證據更完整**：第 5 條修正後沒重跑正面測試，是它抓到的；重跑結果（用分支名取 NN、`lab13:`、27 字 ✓、沒 push）已補進 Lab 13 的 CHECKLIST。

## 怎麼驗證

```sh
python3 -c "import yaml,re;s=open('.claude/agents/code-reviewer.md').read();print(yaml.safe_load(re.match(r'^---\n(.*?)\n---',s,re.S).group(1)))"
# tools 只有 Read, Grep, Glob；permissionMode: plan
```

要自己重跑一次比較：先用 1.7 四面向審某個 PR 的 diff、寫下發現，再在全新 session 說「先 `git diff A B` 取得 diff，把全文交給 code-reviewer 子代理審查」，對照填四格表。

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. 子代理建好，且工具權限限制為唯讀
2. 對真實 diff 跑過一次，輸出符合你規定的格式（含行號）
3. 你先自己審過，才看它的報告
4. 四格比較表填完，結論寫進 PR 留言
5. merge 是你按的，而且你說得出這個 PR 為什麼可以合

## Plan（已確認）

1. issue #41；分支 `lab14/feature/code-reviewer`。
2. 問出位置與欄位；建 `.claude/agents/code-reviewer.md`，`tools: Read, Grep, Glob`、`permissionMode: plan`。
3. 審查對象 `lab12-done..lab13-done`（PR #40）。
4. 主辦先用四面向審，交出發現後才跑子代理。
5. 全新 session 只放行讀取工具、`git diff` 與 Agent，請子代理審查；stream-json 記錄主對話只收到結論、格式含行號、沒有改檔。
6. 四格比較表寫成本 PR 留言並引用 PR #40。
7. 人工合併：主辦按 merge 並寫一句為什麼可以合；Release `lab14-done`。
8. 文件：本資料夾、LAB_GUIDE 第 14 列與段落、5.8 證據地圖、根 README、ERRATA。
