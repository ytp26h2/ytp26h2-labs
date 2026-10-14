# Lab 11 驗收紀錄

驗證日期：2026-10-14｜驗證方式：在本 Claude Code session（雲端容器，工作目錄＝repo 根）直接執行；版本號以容器內指令輸出為證、操作模式以 session 設定為證、小改動以 commit 與無頭 Chromium 截圖為證。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

## 教材驗收清單（Lab 11 頁）

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 工具裝好了，終端機回得出版本號 | ✅ | 容器內 `claude --version` → `2.1.299 (Claude Code)`；`node --version` → `v22.22.0`。工具本體是 Claude Code 網頁版（session `session_01SnYEPfoDabLA5fWYrGvTRA`，模型 `claude-fable-5-1`）。 |
| 2 | 已登入或已設好金鑰，不再跳未認證 | ✅ | session 以主辦帳號建立，從 Lab 1 到本 Lab 沒有任何未認證提示。App 的 API 金鑰另計：Lab 3 用環境變數、Lab 6 起使用者自帶（BYOK），都不進 Git。 |
| 3 | 在專案資料夾裡啟動，第 3 題答對了（WORDS、8 個單字） | ✅ | 工作目錄是 repo 根；三題答案見下方，第 3 題兩處都答對：Lab 1 起始碼 `WORDS`、8 字；現行 App `words.js` 18 字（改動後 21）。 |
| 4 | 知道自己現在在哪一種操作模式，而且選的是逐步確認 | ✅ | 知道模式：`get_session` 在 Plan 階段與小改動完成後都回 `permission_mode: auto`（`permission_mode_seq` 19 未變），主辦預計的 app 端切換沒有生效，工具層級整個 Lab 仍是自動接受。逐步確認改以明確提問達成：改檔前先列出四行內容請主辦確認、commit 與 push 前再請主辦看 diff 與驗證結果確認，兩次都得到同意後才動作（對話紀錄）。誠實標記：工具模式 auto、流程上逐步確認。模式對照見下表。 |
| 5 | 完成一次小改動，且是你自己用 git diff 與瀏覽器驗過才提交 | ✅ | commit `70bebc2`（`labs/lab10-graduation/words.js` 加 loop、variable、debug）。提交前：`git diff` 只有四行新增、`git status` 只有一檔；`check_words.js` 21 字通過；`test_csv.js`、`test_srs.js` 通過；無頭 Chromium（iPhone 視口）複習到隊尾依序看到 loop→迴圈、variable→變數、debug→除錯，無 JS 錯誤；主辦看過以上結果才確認 commit。 |

## 三個驗證問題（只根據倉庫檔案回答）

**1. 這個專案是做什麼的？**

YTP2026H2 黑客松自學教材的 Lab 起始點範本倉庫（`README.md:1`～`5`），由 YTP 助教維護，學員 Use this template 複製後自學。內容是教材「YTP VocaBuddy 開發者之路」每個 Lab 的完成品：`labs/labNN-*/` 一個 Lab 一個資料夾，從 Lab 1 可翻面單字卡一路做到 Lab 10 的 PWA 背單字 App（SRS 排程、AI 例句、弱點出題、離線、CSV 匯入），最新版 App 在 `labs/lab10-graduation/`（`README.md:16`～`27` 的 Lab 表）。`docs/LAB_GUIDE.md` 是總指引（工作流程、命名規則、各 Lab 狀態），`docs/ERRATA.md` 是教材勘誤表（E-001～E-026），`.github/workflows/ci.yml` 對 lab09 與 lab10 兩個目錄跑測試。

**2. 列出所有檔案，並說明每個檔案負責什麼。**（`git ls-files` 共 67 個）

| 路徑 | 負責什麼 |
|---|---|
| `README.md` | 範本 repo 的使用說明、Lab 表、授權 |
| `LICENSE` | 雙軌授權：教材內容 CC BY-NC-SA 4.0、程式碼 MIT |
| `.github/workflows/ci.yml` | GitHub Actions：matrix 跑 `labs/lab09-ship-it` 與 `labs/lab10-graduation` 的 `test_*.js` 與 `check_words.js` |
| `docs/LAB_GUIDE.md` | 總指引：工作流程、命名規則、Lab 狀態表、各 Lab 摘要 |
| `docs/ERRATA.md` | 教材勘誤表 |
| `labs/lab01-first-commit/` | `index.html` 可翻面單字卡（`WORDS` 8 字）、`README.md`、`.gitignore`、`CHECKLIST.md` |
| `labs/lab02-branch-pr-conflict/` | 同上四檔；`index.html` 加「考我」按鈕 |
| `labs/lab03-example-cli/` | `tools/gen_example.py` 例句生成 CLI v2（JSON、驗證、降階）、`tools/requirements.txt`、`index.html`（沿用 Lab 2）、README、.gitignore、CHECKLIST |
| `labs/lab05-sprint1-mvp-review-queue/` | `index.html` 今日複習佇列 MVP（localStorage 學習紀錄）、README、.gitignore、CHECKLIST |
| `labs/lab06-sprint2-ai-example/` | `index.html` 加 AI 例句（fetch 直呼 API、BYOK、快取、降階）、README、.gitignore、CHECKLIST |
| `labs/lab07-sprint3-srs/` | `srs.js` Leitner 排程純函式、`test_srs.js` 單元測試、`index.html` 接上排程與時間旅行、README、.gitignore、CHECKLIST |
| `labs/lab08-sprint4-smart-quiz/` | `words.js` 單字包（18 字）、`check_words.js` 資料檢查、`index.html` 加弱點出題、`srs.js`、`test_srs.js`、README、.gitignore、CHECKLIST |
| `labs/lab09-ship-it/` | Lab 8 全套＋`manifest.json`（PWA 身分）、`sw.js`（離線快取）、`icon.png`、README（含 CI 徽章）、CHECKLIST |
| `labs/lab10-graduation/` | Lab 9 全套＋`csv.js` CSV 匯入純函式、`test_csv.js`、`DEMO.md` 3 分鐘逐字稿、`screenshot-phone.png`、作品級 `README.md`、CHECKLIST；`words.js` 本 Lab 改成 21 字 |

**3. `index.html` 裡的單字資料放在哪個變數？目前有幾個單字？**

- Lab 1 起始碼（教材這題預設的狀態）：`labs/lab01-first-commit/index.html:44`～`48`，`const WORDS` 是二維陣列 `[["algorithm","演算法"], …]`，**8 個單字**。
- 現行 App：`index.html` 裡沒有單字資料。Sprint 4 起搬到 `labs/lab10-graduation/words.js:2` 的 `const WORDS`（物件陣列 `{en, zh}`），本 Lab 改動前 **18 個**、改動後 21 個；`index.html` 以 `<script src="words.js">` 載入，`csv.js` 匯入的自訂字在執行期 `push` 進同一個陣列。

## 三種操作模式對照（Claude Code）

| 教材名稱 | Claude Code | 行為 | 本 repo 何時用 |
|---|---|---|---|
| 逐步確認（手動模式） | `default` | 每個寫檔與指令都先問 | Lab 11 全程 |
| 先計畫再做（計劃模式） | `plan` | 先出計畫，同意才動手 | 每個 Lab 的「Plan 先由主辦確認」 |
| 自動接受 | `acceptEdits`／`auto` | 一路做完不問 | Lab 1～10 的執行階段（Plan 已確認、改壞救得回來） |

## 小改動的證據

| 檢查 | 結果 |
|---|---|
| `git diff` | 只有 `labs/lab10-graduation/words.js` 第 12 行加逗號、新增 3 行（1 行註解＋3 個單字） |
| `git status` | 只有一檔 modified |
| `node check_words.js` | `words.js 檢查通過，共 21 字 ✓` |
| `node test_csv.js`、`node test_srs.js` | 通過 |
| 瀏覽器 | 無頭 Chromium 開 `http://localhost`：今日佇列 21 張，複習到隊尾看到 loop、variable、debug 三張並翻面顯示中文（截圖 `lab11-loop.png` 等三張，存於驗證環境） |
| 主辦確認 | 改檔前確認四行內容；commit 前看過 diff 與驗證結果 |
