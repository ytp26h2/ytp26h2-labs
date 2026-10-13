# Lab 2：分支、PR 與你的第一次衝突

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab2>（v2.0）
> 目標：完整走一次 GitHub Flow：issue → 分支 → PR → review → 合併；並親手製造、解決一次衝突
> 時間：約 60–90 分鐘｜前置：完成 Lab 1
> 檢查點 tag：`lab2-done`

## 這是什麼

Lab 1 的單字卡加上「考我」按鈕（隨機抽卡、不連續重複），並把 h1 改成「VocaBuddy Pro 2.0」。改名這件事本身不重要，重要的是它是一場**自導自演的衝突**留下的疤。

## 怎麼執行

瀏覽器直接開 `index.html`。「下一張」依序換字，「考我」隨機抽字。

## 技術

- 與 Lab 1 相同：單一 HTML，零依賴。
- 新增 `quiz()`：`do { j = 隨機 } while (j === i)`，排除與目前相同的索引。

## 作者

YTP2026H2 主辦（助教範本）。全程透過 Claude 在瀏覽器中完成，issue、PR、review、合併都留在 GitHub 上，可直接點進去看。

---

## Plan（已確認，同步寫在 `index.html` 頂端註解）

見 `index.html` 頂端的 PLAN 註解，共 10 步。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 1 開一張 issue | 標題「新增『考我』按鈕」，記下編號（應該是 #1） | issue [#3](https://github.com/ytp26h2/ytp26h2-labs/issues/3)。既有 repo 的編號不會是 #1，commit 訊息用實際編號。 |
| 2 開分支、加功能 | `git switch -c feature/quiz-button`，加按鈕與 `quiz()`，commit 訊息含 `closes #1` | 分支 `lab02/feature/quiz-button`（從 `main` 開）。兩個 commit：先建立本資料夾（複製 Lab 1 成果＋PLAN），再加功能，訊息 `lab02: feat: 考我按鈕隨機抽卡（不重複），closes #3`。 |
| 3 開 Pull Request | `feature/quiz-button → main`，三段模板 | PR [#4](https://github.com/ytp26h2/ytp26h2-labs/pull/4)，base `main`，描述「做了什麼／為什麼／怎麼驗證」。 |
| 4 自我 review | Files changed 逐行讀，留一則行內評論 | 在 `do…while` 那行留行內評論，另附 1.7 四面向總評（正確性、可讀性、範圍、風險）。 |
| 5 合併、收工 | Merge pull request → Delete branch；本地 `switch main`、`pull`、`branch -d` | 由管理員 `tw-ytp` 合併（merge commit `438e99b`），分支自動刪除，issue #3 自動關閉。本地 `git fetch` 後把工作分支 rebase 到新 `main`，刪除本地功能分支。 |
| 6 衝突演練 | 分支 `rename` 改 h1 為 2.0；`main` 同一行改 Pro；merge 衝突；手動解；commit；push | 分支 `lab02/rename` 改 2.0；基底分支 `claude/gallant-tesla-1yfec7`（扮演 main）改 Pro；`git merge` 出現 `CONFLICT (content)`；手動解為「VocaBuddy Pro 2.0」，刪光三種記號；`git add` 後 `git commit --no-edit`。 |

> 為什麼衝突演練不是直接在 `main` 上做？本 repo 的 `main` 只接受 PR 合併，沒有人直接 push。所以用工作分支扮演教材裡的 `main`，衝突合併的結果再經 PR 進 `main`。學生在自己的 repo 照教材原步驟做即可。

## 衝突長什麼樣（實際擷取）

```
<<<<<<< HEAD
<h1>YTP VocaBuddy Pro 背單字夥伴</h1>
=======
<h1>YTP VocaBuddy 2.0 背單字夥伴</h1>
>>>>>>> lab02/rename
```

上方是你目前分支（HEAD）的版本，下方是被合併分支的版本。決定最終內容、刪掉三行記號，`git add` 告訴 Git「這檔我處理完了」，再 `git commit`。

## 驗收清單

見 `CHECKLIST.md`（含實際驗證紀錄與 DAG 圖）。教材原始六項：

1. repo 裡有一個「已合併」的 PR，含描述三段與至少一則行內評論
2. issue 顯示為 closed，且是被 PR 自動關閉的
3. 「考我」按鈕正常運作，連按十次不會出現同一張卡連續兩次
4. 親手解過一次衝突，最終檔案裡沒有殘留任何衝突記號
5. `git log --oneline --graph` 看得到合併節點
6. 能畫出這個 Lab 結束時的 DAG

## 常見錯誤急救（教材原表，另加本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| 找不到開 PR 的按鈕 | 黃色橫幅只出現幾分鐘。走 Pull requests → New pull request，base 選 main、compare 選你的分支。 |
| merge 後 GitHub 有新版，本地卻沒有 | 在 GitHub 上按的 merge 發生在遠端。回本地 `git switch main && git pull`。 |
| 解衝突後 commit 不了 | 忘了先 `git add` 衝突檔案。add 是在告訴 Git「這檔我處理完了」。 |
| 改動 commit 到錯的分支 | 最常見的是忘了 switch。commit 不會消失：速查卡的 cherry-pick／reset 段有搬移法。 |
| （補充）`closes #N` 沒有自動關 issue | 只有合併進**預設分支**（main）才會觸發自動關閉；PR 的 base 若是其他分支就不會。 |
| （補充）merge 後顯示「Everything up-to-date」但分支沒刪 | 你的憑證可能沒有刪除分支的權限（CI 或 App token 常見）。到 GitHub 的 Branches 頁面手動刪。 |
