# Lab 9 驗收紀錄

驗證日期：2026-10-14｜驗證方式：本環境能做的部分以 Node 22 與無頭 Chromium（Playwright 1.64 ＋ 環境預裝 Chromium 1194）驗證，PWA 以本地 `http://localhost` 服務 App；CI 以 PR 的 GitHub Actions 結果驗證；公開網址、手機安裝、飛航模式由管理員在裝置上驗證（本環境連不到 github.io）。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 公開網址在別人的裝置上打得開、能完整複習一輪 | ⏳ | 需管理員開啟 Pages（Deploy from a branch，main／root）並在裝置上開 <https://ytp26h2.github.io/ytp26h2-labs/labs/lab09-ship-it/>。 |
| 2 | 手機已安裝到主畫面，開啟為全螢幕獨立視窗 | ⏳ | 需管理員在手機上做。本環境已驗 manifest 可讀、`display: standalone`、icon.png 為 PNG。 |
| 3 | 飛航模式下 App 照常開啟與複習（AI 例句顯示快取或友善訊息） | ⏳（本環境已模擬通過） | 無頭 Chromium 以 `http://localhost` 載入後 `set_offline(True)` 重新載入：頁面由 service worker 供應，18 張卡、可翻面自評；AI 例句快取命中秒回「An algorithm is a recipe.…」，未快取的字顯示友善訊息。真機飛航模式由管理員確認後改 ✅。 |
| 4 | PR 頁面看得到 CI 綠勾；故意推一個會掛測試的 commit，親眼看它變紅（然後修好） | ✅ | PR [#26](https://github.com/ytp26h2/ytp26h2-labs/pull/26)。feat commit `8c7ac83` 綠：[run 38507787516](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38507787516)（push）、[run 38507906867](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38507906867)（pull_request）。故意改壞 `INTERVALS[4]` 的 `88da7ae` 紅：[run 38507944693](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38507944693)、[run 38507950961](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38507950961)，`AssertionError: Expected values to be strictly deep-equal`。修正 `9517cdc` 綠：[run 38508001671](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38508001671)、[run 38508006543](https://github.com/ytp26h2/ytp26h2-labs/actions/runs/38508006543)，4 tests passed。 |
| 5 | tag `v1.0` 已推上，README 掛上 CI 徽章 | ⏳ | 徽章已掛在本 README 與根目錄 README；tag 由管理員以 Release 建立，合併後補記。 |

## PWA 驗證明細（11 項全過）

| 檢查 | 結果 |
|---|---|
| `<link rel=manifest>` 可讀，`display: standalone`、`start_url: "."` | ✅ |
| `<meta name=theme-color>` 為 `#0f766e` | ✅ |
| `icon.png` 200、`image/png`、2187 bytes | ✅ |
| service worker 註冊並 `activated`，scope 為站台根 | ✅ |
| 安裝時快取 SHELL 五項：`./`、`index.html`、`words.js`、`srs.js`、`manifest.json` | ✅ |
| `icon.png` 是否在快取 | 無（教材 SHELL 未列，E-025） |
| 離線重新載入：18 張卡、可翻面自評 | ✅ |
| 離線 AI 例句：快取命中顯示例句；未快取顯示友善訊息 | ✅ |
| 全程 `pageerror` | 0 筆（`http://localhost`） |

## 安檢（4.4）

| 檢查 | 結果 |
|---|---|
| 歷史裡沒有金鑰 | `git grep sk-` 只命中 Lab 3／Lab 6 說明文字與 Lab 3 README 的假 key `sk-ant-dummy`；`git grep 'sk-ant-'` 無真金鑰；`git log` 全程金鑰只從環境變數傳入。 |
| `.gitignore` 擋住危險檔 | `.DS_Store`、`.env`、`__pycache__/`。 |
| 前端程式碼裡沒有任何祕密 | key 由使用者輸入存自己的 localStorage（BYOK）。 |
| 使用者資料留在使用者手上 | 學習紀錄只存 localStorage，不回傳任何伺服器。 |
| AI 輸出有驗證、有降階 | Lab 6 例句含字驗證、Lab 8 題目格式驗證，失敗皆降階。 |

## 回歸

| 腳本 | 結果 |
|---|---|
| Lab 8 攔截層（`file://`） | 14/15：唯一失敗是「無 JS 錯誤」，錯誤為 `file://` 下 service worker 註冊失敗（E-023），功能項全過 |
| Lab 7 時間旅行（`file://`） | 14/21：失敗的 7 項都是張數預期寫死為 8 字（單字包現在 18 字），邏輯項（舊紀錄升級、忘了排隊尾、vbTravel(1) 為 0、到期篩選）全過；另一項同上 E-023 |
| `node test_srs.js`、`node check_words.js` | 通過 |
