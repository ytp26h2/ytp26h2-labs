# Lab 2 驗收紀錄

驗證日期：2026-10-13｜驗證方式：GitHub 頁面與 API 查核、`git log --graph`、無頭 Chromium（Playwright 1.56）實際點擊。

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | repo 裡有一個「已合併」的 PR，含描述三段與至少一則行內評論 | ✅ | PR [#4](https://github.com/ytp26h2/ytp26h2-labs/pull/4)：描述「做了什麼／為什麼／怎麼驗證」三段；行內評論留在 `index.html` 第 55 行的 `do…while`；另附四面向總評。由管理員 `tw-ytp` 以 merge commit 合併（`438e99b`）。 |
| 2 | issue 顯示為 closed，且是被 PR 自動關閉的 | ✅ | issue [#3](https://github.com/ytp26h2/ytp26h2-labs/issues/3) 狀態 closed、reason completed，`closed_by_pull_requests` 指向 PR #4。本 repo 的編號是 #3 而非教材假設的 #1（見勘誤 E-006）。 |
| 3 | 「考我」按鈕正常運作，連按十次不會出現同一張卡連續兩次 | ✅ | 無頭 Chromium 連按 200 次：連續重複 0 次、8 個單字皆出現；翻面後按「考我」會回到英文面。另做十次也是 0 次重複。 |
| 4 | 親手解過一次衝突，最終檔案裡沒有殘留任何衝突記號 | ✅ | 分支 `lab02/rename` 改 h1 為「VocaBuddy 2.0」，基底分支同一行改為「VocaBuddy Pro」，`git merge` 出現 `CONFLICT (content)`。手動解為「YTP VocaBuddy Pro 2.0 背單字夥伴」，`grep` 確認 `<<<<<<<`／`=======`／`>>>>>>>` 皆為 0 筆。頁面 h1 實際顯示「YTP VocaBuddy Pro 2.0 背單字夥伴」。 |
| 5 | `git log --oneline --graph` 看得到合併節點（兩個 parent 的 commit） | ✅ | 三個合併節點：`5403879`（parents `39ebdee` `8d68252`，衝突合併）、`438e99b`（PR #4）、`c7b512b`（PR #2）。 |
| 6 | 能畫出本 Lab 結束時的 DAG，對照 log 驗證 | ✅ | 見下方 DAG。 |

## 本 Lab 結束時的 DAG（對照 `git log --oneline --graph`）

```
*   5403879  Merge branch 'lab02/rename'            ← 衝突合併（手動解）
|\
| * 8d68252  lab02: feat: 更名 VocaBuddy 2.0        ← 分支 lab02/rename
* | 39ebdee  lab02: feat: 更名 VocaBuddy Pro        ← 基底分支（扮演 main）
|/
* 3faf866    lab01: docs: 檢查點改指向 c7b512b
*   438e99b  Merge pull request #4                  ← GitHub 上按的 merge commit
|\
| * aab340d  lab02: feat: 考我按鈕…，closes #3      ← 分支 lab02/feature/quiz-button
| * d7d5cff  lab02: chore: 建立 Lab 2 起點
|/
*   c7b512b  Merge pull request #2  (tag: lab1-done)
|\
| * bd513e6  lab01: docs: …
| * 3e12935  lab01: docs: …
| * 1b60711  lab01: docs: README 與 gitignore
| * 13e05e3  lab01: feat: 首頁骨架與可翻面單字卡
|/
* 70851b3    docs: 新增 LICENSE
```

讀法：箭頭由子指向父（上指向下）。`|\` 是分岔、`|/` 是收合；每個收合點就是一個有兩個 parent 的合併 commit。

## 補充驗證（主辦自加）

- 翻面後按「考我」或「下一張」，都回到英文面：✅
- 頁面標題仍為 `YTP VocaBuddy`，只有 h1 更名：✅（教材只要求改 h1）
- Console 無錯誤：✅
