# Lab 5（Sprint 1）：MVP——今日複習佇列

> 教材：<https://tw-ytp.github.io/vocabuddy/#/3-1>（v2.0）
> 目標：找出 VocaBuddy 的核心迴路「看卡 → 回想 → 翻面 → 自評 → 下一張」，做成今天就能用的 MVP；學習紀錄存 localStorage
> 時間：約 1.5–2.5 小時｜前置：完成 Lab 2（Lab 3、4 與本輪無關，本輪刻意不碰 AI）
> 檢查點 tag：`sprint1-done`

## 這是什麼

單字卡升級成複習迴路。打開頁面看到第一張卡與「剩 N 張」，點「顯示答案」翻面，按「記得」或「忘了」自評；忘了的卡排到今天隊尾再考一次，直到全部答「記得」出現「今日完成！」。每個字看過幾次、錯過幾次記在 `log`，存瀏覽器 localStorage，重新整理不會消失。

## 怎麼執行

瀏覽器直接開 `index.html`。手機可在同一 Wi-Fi 下用 `python3 -m http.server` 後以電腦 IP 開啟。

## 技術

- 仍是單一 HTML、零依賴。
- **資料先於介面**：`WORDS` 由字串陣列升級為物件陣列 `{en, zh}`（進 Git，全隊共享）；`log = {字: {seen, wrong}}` 獨立存 localStorage（只屬於這台裝置），讀寫都包 `try/catch`。
- `queue = [...WORDS]`：Sprint 1 每天全部複習；「忘了」用 `queue.push(queue.shift())` 排到隊尾。Sprint 3 會換成 SRS 排程。
- `seen`／`wrong` 現在看似沒用，是 Sprint 4 弱點分析的伏筆。

## 作者

YTP2026H2 主辦（助教範本）。全程透過 Claude 在瀏覽器中完成。

---

## Plan（已確認，同步寫在 `index.html` 頂端註解）

見 `index.html` 頂端的 PLAN 註解，共 8 步。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 開 issue、開分支 | issue「Sprint 1：今日複習佇列（MVP）」貼使用者故事＋驗收前三條；`git switch -c feature/review-queue` | issue [#12](https://github.com/ytp26h2/ytp26h2-labs/issues/12)；分支 `lab05/feature/review-queue`（從 `main` 開）。 |
| 改寫 index.html | 用教材完整版本取代 | 先 `lab05: chore:` 以 Lab 2 成果建立起點（含 PLAN），再 `lab05: feat: 今日複習佇列 MVP，closes #12` 整檔取代。教材程式一字未改，只在頂端保留 PLAN 註解。 |
| 手機實測 | 電腦與手機各過一輪佇列；重新整理確認 log 還在 | 以無頭 Chromium 自動化：桌機 1280×800 與 iPhone 13（390×664）各跑完整佇列、重新整理驗證 localStorage。見 `CHECKLIST.md`。 |
| 收工儀式 | commit `closes #4` → push → PR → merge → `git tag sprint1-done` | commit 訊息用實際編號 #12；PR 三段描述＋自我 review 行內評論；由管理員 `tw-ytp` 合併；tag 由管理員以 Release 建立（Target=`main`）。 |

適配說明：h1 依教材回到「YTP VocaBuddy」，Lab 2 的「Pro 2.0」只是衝突演練的產物；教材的「手機實測」以裝置模擬代替，真機請自行再過一輪。

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. 打開頁面立即看到第一張卡與「剩 N 張」；答完全部出現「今日完成」
2. 「忘了」的卡稍後會再出現，直到你答「記得」
3. 重新整理後，seen／wrong 統計仍在
4. 手機上按鈕大小、字級可正常操作
5. PR 已合併、tag `sprint1-done` 已推上 GitHub

## 實作時發現的兩件事（勘誤 E-012、E-013）

1. **答完最後一張，上方統計停在「剩 1 張」**。`next()` 在 `queue.length === 0` 的分支直接 `return`，沒呼叫 `stats()`。畫面同時出現「今日完成！」與「剩 1 張」，自相矛盾。修法：把 `stats();` 移到 `next()` 第一行。本 repo 照教材原碼不改，留給教材修訂。
2. **重新整理會把今日佇列重置**。只有 `log` 存 localStorage，`queue` 每次載入都從 `WORDS` 重建。教材驗收第 3 項只說「統計仍在」，學生看到佇列從 8 張重來可能以為壞了。這是 Sprint 1 的刻意簡化（Sprint 3 排程會改善），教材應說一句。

## 常見錯誤急救（本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| 重新整理後 `log` 是空的 | 用 `file://` 開啟時某些瀏覽器的 localStorage 隔離或停用；改用 `python3 -m http.server` 走 `http://localhost`。隱私模式也可能整組不能用，程式已包 `try/catch` 不會壞，只是不會記。 |
| Console 輸入 `log` 看不到東西 | 要在頁面所屬的分頁開發者工具輸入；`log` 是 `let` 宣告的全域變數，直接打 `log` 即可。 |
