# Lab 9：上線三連發——部署、PWA、CI

[![CI](https://github.com/ytp26h2/ytp26h2-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/ytp26h2/ytp26h2-labs/actions/workflows/ci.yml)

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab9>（v2.0），內容照 4.1～4.4
> 目標：拿到公開網址、手機可安裝、每個 PR 自動過測試
> 時間：約 60–90 分鐘｜前置：完成第三篇
> 檢查點 tag：`v1.0`

## 這是什麼

Lab 8 的 VocaBuddy 加三件事。**部署**：GitHub Pages 把 `main` 發布成網站，公開網址 <https://ytp26h2.github.io/ytp26h2-labs/labs/lab09-ship-it/>。**PWA**：`manifest.json` 給身分、`sw.js` 給離線，手機可安裝到主畫面、飛航模式照常複習。**CI**：`.github/workflows/ci.yml` 讓每次 push 與每個 PR 自動跑 `test_srs.js` 與 `check_words.js`，壞程式碼進不了 `main`。

## 怎麼執行

- 線上：開公開網址，手機瀏覽器選單 → 加入主畫面。
- 本地：`python3 -m http.server 8000` 後開 `http://localhost:8000/labs/lab09-ship-it/`。service worker 需要安全來源，`localhost` 算，`file://` 不算（見下方勘誤 E-023）。
- 測試：`cd labs/lab09-ship-it && node test_srs.js && node check_words.js`。

## 技術

- `manifest.json`：`start_url: "."`、`display: standalone`，相對路徑，所以部署在子路徑下不會斷。
- `sw.js`：快取優先，安裝時存 SHELL 五項；改版時把 `CACHE` 的 v1 改 v2 才會換新。
- `ci.yml`：教材原檔加 `defaults.run.working-directory: labs/lab09-ship-it`，因為本 repo 的 App 在子目錄；兩行 `run` 照抄。
- `icon.png`：512×512，用 Python Pillow 畫的單字卡圖示。

## 作者

YTP2026H2 主辦（助教範本）。全程透過 Claude 在瀏覽器中完成。

---

## Plan（已確認，同步寫在 `index.html` 頂端註解）

見 `index.html` 頂端的 PLAN 註解，共 9 步。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 安檢，然後轉公開 | `git grep sk-`、翻 `git log`；repo 改 Public | repo 是公開範本，本來就 Public。`git grep sk-` 只命中說明文字與 Lab 3 README 的假 key `sk-ant-dummy`，`git grep 'sk-ant-'` 無真金鑰；`git log` 全程金鑰只從環境變數傳入。 |
| 開啟 GitHub Pages | Settings → Pages → Deploy from a branch，main／(root) | 由管理員在 Settings 操作。根目錄的 README.md 會被 Jekyll 渲染成首頁，App 在 `labs/lab09-ship-it/` 子路徑。 |
| PWA 化 | issue、分支 `feature/ship-it`、manifest、sw.js、icon、`<head>` 與 script 各兩行 | issue [#25](https://github.com/ytp26h2/ytp26h2-labs/issues/25)；分支 `lab09/feature/ship-it`；檔案照教材。 |
| 加上 CI | `.github/workflows/ci.yml` 照抄 | 放在 repo 根目錄，加 `working-directory` 適配。 |
| PR、觀察機器人上工 | 開 PR，看 CI 轉綠再 merge | PR 開出時 CI 立即跑，`8c7ac83` 兩次 run 皆綠。 |
| 手機安裝實測 | 加入主畫面、飛航模式 | 由管理員在裝置上做；本環境以無頭 Chromium 的離線模式驗證 service worker。 |
| tag v1.0 | `git tag v1.0 && git push --tags` | 由管理員以 Release 建立。 |

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. 公開網址在別人的裝置上打得開、能完整複習一輪
2. 手機已安裝到主畫面，開啟為全螢幕獨立視窗
3. 飛航模式下 App 照常開啟與複習
4. PR 頁面看得到 CI 綠勾；故意推一個會掛測試的 commit，親眼看它變紅（然後修好）
5. tag `v1.0` 已推上，README 掛上 CI 徽章

## 實作時發現的三件事（勘誤 E-023～E-025）

1. **`file://` 開啟時 service worker 註冊會丟錯**。教材那一行 `navigator.serviceWorker.register("sw.js")` 在 `file://` 下回傳 rejected promise，Console 出現紅字 `Failed to register a ServiceWorker: The URL protocol of the current origin ('null') is not supported`。App 功能不受影響，但前八個 Lab 都教學生直接點開 index.html，突然多一條紅字會嚇到人。加 `.catch(() => {})` 或只在 `location.protocol.startsWith("http")` 時註冊即可。
2. **`on: [push, pull_request]` 讓同一次 push 跑兩次**。PR 的每個 commit 都會觸發 push 與 pull_request 兩個 run，Actions 頁面看到成對的結果。教材可以說明，或改成 `on: { push: { branches: [main] }, pull_request: {} }`。
3. **`sw.js` 的 SHELL 沒列 `icon.png`**。離線時主畫面圖示仍可顯示（安裝時已存），但 manifest 的 icon 重新抓取會失敗。把 `"icon.png"` 加進 SHELL 即可。

## 常見錯誤急救（教材原表，另加本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| 網址 404 | Pages 要一兩分鐘生效；確認分支選對、repo 已 public、檔名是 index.html。本 repo 的 App 在 `labs/lab09-ship-it/` 子路徑，根網址是 README。 |
| 網站開了但改版沒生效 | service worker 的舊快取。把 `sw.js` 的 CACHE 改成 v2 再 push。 |
| CI 沒有跑 | 路徑錯了。必須是 `.github/workflows/ci.yml`。 |
| CI 紅在 setup 步驟 | YAML 縮排錯位。 |
| 安裝選項沒出現 | manifest 沒被讀到、icon.png 缺檔，或不在 HTTPS。 |
| （補充）Console 紅字 `Failed to register a ServiceWorker` | 用 `file://` 開的。改用 `python3 -m http.server` 走 `http://localhost`，或照 E-023 加 `.catch`。 |
