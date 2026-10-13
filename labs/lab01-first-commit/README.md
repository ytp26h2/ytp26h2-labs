# Lab 1：第一次提交——VocaBuddy 上線 GitHub

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab1>（v2.0）
> 目標：建好 VocaBuddy 倉庫，完成首次 commit 並推上 GitHub
> 時間：約 40–60 分鐘｜前置：Git、GitHub 帳號、任一編輯器
> 檢查點 tag：`lab1-done`

## 這是什麼

VocaBuddy 背單字夥伴的最初骨架：一張可以點擊翻面的單字卡，附「下一張」按鈕，內建 8 個單字。它是後面所有 Lab 的起點。

## 怎麼執行

零依賴、零建置。直接用瀏覽器開啟 `index.html` 即可：

```bash
# 任一方式
open labs/lab01-first-commit/index.html          # macOS
xdg-open labs/lab01-first-commit/index.html      # Linux
# 或在 repo 根目錄起一個靜態伺服器
python3 -m http.server 8000   # 瀏覽器開 http://localhost:8000/labs/lab01-first-commit/
```

## 技術

- 單一 HTML 檔：HTML ＋ 內嵌 CSS ＋ 內嵌 JavaScript
- 狀態只有兩個變數：`i`（目前第幾張）與 `flipped`（是否翻面）
- 沒有框架、沒有後端、沒有外部資源

## 作者

YTP2026H2 主辦（助教範本）。本次實作全程透過 Claude 在瀏覽器中完成，程式碼與文件直接進 GitHub，不落地。

---

## Plan（已確認，同步寫在 `index.html` 頂端註解）

1. 建立 `index.html`，貼入教材起始碼，頂端加 PLAN 註解。
2. 建立 `README.md`（四段）與 `.gitignore`（`.DS_Store`）。
3. 至少 2 個 commit，推到指定分支，打 tag `lab1-done`。
4. 無頭 Chromium 驗證翻面、下一張、循環；結果記入 `CHECKLIST.md`。
5. 新增 `docs/LAB_GUIDE.md`、`docs/ERRATA.md`，更新根目錄 README。
6. 適配說明：單一 repo，不重做 init／remote add／首次 push。
7. 勘誤候選先記入 `docs/ERRATA.md`。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 的做法 |
|---|---|---|
| 1 確認環境、報上名來 | `git --version`、設定 `user.name`／`user.email` | 雲端環境已設定；commit 作者即推送者帳號 |
| 2 建立專案與第一個檔案 | 新資料夾 `ytp-vocabuddy/index.html` | `labs/lab01-first-commit/index.html`（內容相同，頂端多 PLAN 註解） |
| 3 init → status → add → commit | `git init` 後走一次循環 | repo 已存在，略過 `init`；`add`→`commit` 照做，訊息 `lab01: feat: 首頁骨架與可翻面單字卡` |
| 4 在 GitHub 建立遠端倉庫 | New repository、Private、三個選項不勾 | 已有 `ytp26h2/ytp26h2-labs`，略過 |
| 5 連上遠端、第一次 push | `remote add`、`branch -M main`、`push -u` | 已有 remote；`git push -u origin <分支>` 照做 |
| 6 補上門面 | README.md ＋ .gitignore，再 commit 一次 | 本檔與 `.gitignore`，訊息 `lab01: docs: README 與 gitignore` |

> 自學者請照教材原步驟做完整流程（含 `git init` 與建立遠端），那正是這個 Lab 要練的手感。上表只說明「主辦範本為什麼長這樣」。

## 驗收清單

見 `CHECKLIST.md`（含實際驗證紀錄）。教材原始五項：

1. 瀏覽器打開 `index.html`，卡片能翻面、能換下一張
2. `git log --oneline` 至少有 2 個 commit，訊息符合「類型: 說明」格式
3. GitHub 上的 repo 看得到 `index.html`，首頁顯示你的 README
4. commit 的作者顯示為你的 GitHub 帳號
5. 你能用自己的話說出：add 和 commit 分別把檔案搬到哪一區

## 常見錯誤急救（教材原表，另加本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| `git: command not found` | Git 沒裝好或終端機沒重開。重開終端機再試；還是不行就重跑安裝程式。 |
| `rejected: fetch first` | 建 repo 時手滑勾了 README，遠端已有你本地沒有的 commit。`git pull origin main --allow-unrelated-histories` 合併後再 push。 |
| push 一直要密碼／失敗 | GitHub 不接受帳號密碼推送，要走瀏覽器授權或個人存取權杖（見教材附錄 B）。 |
| commit 作者頭像是灰色問號 | `user.email` 與 GitHub 帳號的 email 不一致。改設定後，之後的 commit 就會正確歸戶。 |
| （補充）畫面打開是空白 | 檔案副檔名不是 `.html`，或貼碼時漏掉 `<script>` 結尾。用瀏覽器 DevTools 的 Console 看紅字。 |
