# Lab 11：開工準備——自己裝好，自己跑起來

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab11>（v2.0），內容照 5.1 與 Lab 11 頁
> 目標：裝好一個代理式編碼工具，讓它讀懂 VocaBuddy 專案並回答三個問題
> 時間：約 30 分鐘｜前置：任一自己的倉庫、終端機、網路
> 檢查點 tag：`lab11-done`

## 這是什麼

第五篇的主角換成「坐在你旁邊、有鍵盤權限的隊友」：代理式編碼工具。Lab 11 不改功能，只做四件事——把工具裝起來、確認它看得到專案、刻意用最慢的逐步確認模式、做一個小到一眼能驗完的改動並親手驗過再提交。

本資料夾只有 `README.md` 與 `CHECKLIST.md`（附錄 D：Lab 11 的產物「無新增檔案，以 commit 為證」）。小改動落在現行 App `labs/lab10-graduation/words.js`，commit `70bebc2`。

## 本 repo 的適配：工具就是這個 session

本 repo 所有 Lab 都是透過 Claude Code 在瀏覽器中完成，所以 Lab 11「裝工具」在這裡是既成事實。對照教材的三個共通步驟：

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| ① 取得工具 | 下載或用套件管理器裝命令列版，終端機回得出版本號 | 工具是 Claude Code 網頁版（claude.ai/code），工作在雲端容器裡；容器內 `claude --version` 回 `2.1.299 (Claude Code)`，`node --version` 回 `v22.22.0`。 |
| ② 登入或設金鑰 | 帳號授權或 API 金鑰進環境變數，不再跳未認證 | session 以主辦的 Claude 帳號建立，模型 `claude-fable-5-1`，全程沒有未認證提示。App 自己呼叫 API 用的金鑰是另一回事（Lab 3 走環境變數 `YTP_ANTHROPIC_API_KEY`、Lab 6 起 BYOK），工具的認證不等於 App 的金鑰。 |
| ③ 進專案資料夾再啟動 | `cd` 進倉庫後才啟動，它才看得到檔案 | session 的工作目錄固定是 repo 根目錄 `/home/user/ytp26h2-labs`，視野是整個倉庫（67 個追蹤檔）。三個驗證問題的答案見 `CHECKLIST.md`。 |
| 三種操作模式 | 逐步確認／先計畫再做／自動接受，本 Lab 用逐步確認 | Claude Code 的名稱：`default`（每個寫檔與指令都問）／`plan`（先出計畫，同意才動手）／`acceptEdits` 與 `auto`（自動接受）。本 session 前十個 Lab 跑 `auto`；Lab 11 原訂由主辦在 Claude app 切到每步詢問，但 `get_session` 顯示切換沒有生效（仍 `auto`），於是改以明確提問做逐步確認：改 `words.js` 前列出四行請主辦同意，commit 與 push 前再請主辦看 diff 與驗證結果同意。本 repo 的「Plan 先由主辦確認」工作流程，正是教材的計劃模式。 |
| 小改動並親手驗 | 加 3 個演算法單字，`git diff`、瀏覽器、確認沒動別的，再 commit | `words.js` 末尾加 `loop`、`variable`、`debug`；主辦看過 diff、`git status` 只有一檔、`check_words.js` 21 字通過、無頭 Chromium 複習到三個新字出現，才確認 commit。 |

## 學員自學時怎麼做

1. 照教材步驟 1 的表選一個工具，到官方安裝頁裝本機版；安裝指令會過期，一律看附錄 B。
2. `cd` 進你自己的 VocaBuddy 倉庫再啟動；先 `git status` 確認站對地方。
3. 問三個問題。第 3 題的「正確答案」要看你做到哪：Lab 1 起始碼是 `index.html` 裡的 `WORDS`、8 個單字；做完 Sprint 4 的人，單字在 `words.js`，`index.html` 裡沒有單字資料（見勘誤 E-027）。
4. 切到逐步確認，再做小改動；它說「已完成」不算數，你 `git diff`、開瀏覽器、確認只改該改的，才 commit。

## 換工具要改哪裡

三個問題、三種模式、小改動與親手驗的流程六家工具都一樣；差別只在啟動指令與模式的名稱（見教材 5.1 對照表）。本 repo 之後 Lab 12～14 的工具設定（`CLAUDE.md`、`.claude/`）放 repo 根目錄，只放 Claude Code 一套，其他工具請對照 5.1 調整路徑，內容照搬即可。

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. 工具裝好了，終端機回得出版本號
2. 已登入或已設好金鑰，不再跳未認證
3. 在專案資料夾裡啟動，第 3 題答對了（WORDS、8 個單字）
4. 知道自己現在在哪一種操作模式，而且選的是逐步確認
5. 完成一次小改動，且是你自己用 git diff 與瀏覽器驗過才提交

## Plan（已確認）

本 Lab 沒有程式檔可放 PLAN 註解，Plan 記在這裡：

1. issue #35；分支 `lab11/feature/algo-words`。
2. 步驟①②適配：記錄工具版本、模型、認證狀態。
3. 步驟③視野：只根據倉庫檔案回答三個問題、附檔名行號；第 3 題答兩處（Lab 1 起始碼、現行 App）。
4. 模式：主辦把 session 切到每步詢問；記錄三種模式對照。
5. 小改動：`labs/lab10-graduation/words.js` 加 3 個演算法單字，先列出給主辦確認再動手。
6. 驗證：`git diff`、無頭 Chromium 複習到新字、`check_words.js` 與 `test_*.js`、只改一檔、CI。
7. commit `lab11: feat: 新增 3 個演算法主題單字` → PR → 主辦合併後建 Release `lab11-done`。
8. 文件：本資料夾 README 與 CHECKLIST、LAB_GUIDE 第 11 列與段落、根 README、ERRATA E-027。
