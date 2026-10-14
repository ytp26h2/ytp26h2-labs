# Lab 10 驗收紀錄

驗證日期：2026-10-14｜驗證方式：程式部分以 Node 22 與無頭 Chromium（Playwright 1.64 ＋ 環境預裝 Chromium 1194，iPhone 13 視口，本地 `http://localhost`）驗證；CI 以 PR 的 GitHub Actions 結果驗證；公開網址、手機實測、Demo 排練與備援影片由管理員在裝置上做（本環境連不到 github.io）。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

## 教材驗收清單（Lab 10 頁）

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | README 首屏就有：一句話定位、Live 網址、截圖、CI 徽章 | ✅ | [`README.md`](README.md) 前 10 行：CI 徽章、粗體定位句、Live 網址 <https://ytp26h2.github.io/ytp26h2-labs/labs/lab10-graduation/>、`screenshot-phone.png`。PR [#31](https://github.com/ytp26h2/ytp26h2-labs/pull/31)。截圖為無頭 Chromium iPhone 視口，管理員可換真機安裝後的畫面。 |
| 2 | 3 分鐘 Demo 排練三次以上，有 90 秒備援影片在手機裡 | ⏳ | 逐字稿、保命三招、排練紀錄表在 [`DEMO.md`](DEMO.md)。排練與錄影由管理員做，完成後補記。 |
| 3 | Demo 用的單字已快取預熱，斷網也能完整演示 | ⏳ | 預熱清單（algorithm、recursion、vocabulary、memorize）與步驟在 `DEMO.md` 保命三招①②。本環境已驗證快取命中離線秒回（Lab 9 驗收 O3）；真機預熱由管理員做。 |
| 4 | 畢業挑戰的 PR 已合併、已上線、自評尺規四個面向都誠實打過分 | ⏳ | PR [#32](https://github.com/ytp26h2/ytp26h2-labs/pull/32) 已合併（main `3d9f2c7`）；自評與反思寫在 issue [#30](https://github.com/ytp26h2/ytp26h2-labs/issues/30) 結案留言。「已上線」與手機實測待管理員回報後改 ✅。 |
| 5 | 回頭看 Lab 1 的第一個 commit——你能說出這一路每個 tag 各代表什麼 | ✅ | 見下方「tag 回顧」。 |

## tag 回顧（驗收第 5 項）

| tag | 指向 | 代表什麼 | Lab |
|---|---|---|---|
| `lab1-done` | `c7b512b` | 可翻面單字卡 `index.html`＋README＋.gitignore；第一次 commit、第一次 push | 1 |
| `lab2-done` | `25ef7a5` | 「考我」按鈕經 issue→分支→PR→review→merge 進來；自導自演解了一次衝突 | 2 |
| `lab3-done` | `64c4601` | Python 例句 CLI v2：JSON 輸出、驗證、降階；金鑰只從環境變數進 | 3 |
| `sprint1-done` | `b42577d` | MVP 核心迴路：看卡→回想→翻面→自評→下一張，localStorage 學習紀錄 | 5 |
| `sprint2-done` | `f5e7904` | AI 例句上卡片：瀏覽器直呼 API、BYOK、快取、降階 | 6 |
| `sprint3-done` | `6cb6a37` | Leitner SRS：`srs.js` 純函式＋`test_srs.js`、時間旅行 | 7 |
| `sprint4-done` | `016744d` | 弱點出題（RAG-lite 閉環）、`words.js` 單字包共編＋`check_words.js` | 8 |
| `v1.0` | `004c8bd` | 上線：GitHub Pages、PWA 可安裝離線、每個 PR 跑 CI | 9 |
| `v1.1` | 待建 | 作品級 README＋畢業挑戰 CSV 匯入上線 | 10 |

## 畢業挑戰：issue #30 驗收條件對照

| # | 條件 | 結果 | 證據 |
|---|---|---|---|
| 1 | 格式：BOM、CRLF、表頭、空行、空白、引號含逗號 | ✅ | `test_csv.js` 9 條 `parseCSV` 斷言；瀏覽器 I2 貼 `﻿en,zh\r\n…"give up","放棄；投降, 認輸"…` 匯入 3 字 |
| 2 | 驗證：欄位不可空、與既有與檔內去重、逐行回報、合法行照常匯入 | ✅ | `test_csv.js` 的 `validateWords` 斷言；瀏覽器 I3 混合 6 行 → 2 字匯入、4 行紅字各指出原因 |
| 3 | 純函式 `csv.js`，`test_csv.js` 先紅後綠，CI 自動跑 | ✅ | test commit `5757567` 紅：[run 38511126941](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38511126941)（`Cannot find module './csv.js'`）；feat commit `cd7f954` 綠：[run 38511138978](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38511138978)（push）、[run 38511173681](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38511173681)（pull_request），兩個 matrix 目錄皆過 |
| 4 | 持久化：`vb-words`、重新整理仍在、併入複習／弱點／AI 例句、清除匯入 | ✅ | I2b、I4、I5、I6、I7b、C1～C3 |
| 5 | 離線：SHELL 含 `csv.js`、CACHE v2、離線匯入與複習照常 | ✅ | O1 快取名 `ytp-vocabuddy-v2`、entries 含 `/csv.js` 與 `/icon.png`；O2、O3 離線重新載入後匯入成功。真機飛航模式待管理員。 |
| 6 | 流程留痕：分支→測試→PR→自我 review→merge→Pages→手機實測→`v1.1` | ⏳ | 分支 `lab10/feature/csv-import`、PR #32 含[自我 review](https://github.com/ytp26h2/ytp26h2-labs/pull/32#pullrequestreview-5513042301)、已合併；Pages 生效、手機實測、`v1.1` 待管理員 |

## 瀏覽器驗證明細（20 項全過）

| 檢查 | 結果 |
|---|---|
| I0 起始 18 字、匯入區塊收合；I1 按鈕展開文字框 | ✅ |
| I2 合法 CSV（BOM、表頭、CRLF、引號含逗號、大小寫）匯入 3 字：WORDS 21、佇列 21、訊息「匯入 3 個單字：apple、give up、banana」 | ✅ |
| I2b localStorage `vb-words` 三筆，`en` 已小寫 | ✅ |
| I3 混合輸入 6 行：匯入 2 字，錯誤 4 行逐行紅字（兩欄、en 空、單字包已有 apple、單字包已有 algorithm） | ✅ |
| I3b 貼 `<b>x</b>` 原樣顯示，沒被當 HTML | ✅ |
| I4 重新整理後 23 字仍在；I5 匯入的字進入複習、翻面顯示中文；I6 `weakest()` 納入匯入字 | ✅ |
| I7 複習完顯示明天見後再匯入 → 立刻出卡、剩 1 張 | ✅ |
| O1 快取 v2 含 `csv.js`、`icon.png`；O2 離線重新載入 24 字；O3 離線匯入成功 | ✅ |
| C1 清除按取消不動；C2 確認後回 18 字、`vb-words` 空、學習紀錄保留；C3 無匯入時提示不跳 confirm | ✅ |
| M1 手機視口無水平捲動；全程 `pageerror` 0 筆 | ✅ |

## 回歸

| 腳本 | 結果 |
|---|---|
| `node test_csv.js`、`node test_srs.js`、`node check_words.js` | 通過 |
| Lab 9 PWA 驗收腳本（`http://localhost`） | 11/11（快取多了 `csv.js`、`icon.png`，S3 由「無」變「有」） |
| Lab 8 攔截層（`file://`） | 14/15：唯一失敗是 E-023 的 service worker 註冊紅字，功能項全過 |

## 自評尺規（issue #30 結案留言的副本）

| 面向 | 分數 | 說明 |
|---|---|---|
| 功能完成度 | 4 | 核心情境走得通，BOM／引號／重複／空行等邊界有處理，離線可用；扣 1：沒收尾的引號只報「欄位數不對」不報「引號沒關」，且本環境無法做真機實測 |
| 程式品質 | 4 | 解析與驗證抽成純函式、有測試、先紅後綠、每行能解釋（PR 自我 review）；扣 1：清除靠 `location.reload()`、瀏覽器層的驗收腳本不在 repo 內 |
| Repo 規範 | 5 | issue 寫驗收條件→分支→test／feat 兩個 commit→PR（CI 紅→綠）→自我 review→merge→tag，commit 訊息照 `labNN: 類型: 說明` |
| AI 應用深度 | 3 | 本題沒有新增 AI 呼叫；匯入的字會進既有的 AI 例句與弱點出題（有驗證、快取、降階），但那是 Sprint 2／4 的功力，不是這題加的 |
