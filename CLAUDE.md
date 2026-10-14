# CLAUDE.md｜ytp26h2-labs 專案指示檔

## 這是什麼專案
- YTP2026H2 黑客松自學教材的 Lab 範本 repo：`labs/labNN-*/` 一個 Lab 一個資料夾，是教材每個 Lab 的完成品，給學員 Use this template 後自學對照。
- 內容是 VocaBuddy 背單字 App：純前端、零建置、資料存 localStorage、無後端；AI 功能由瀏覽器直呼 Claude API，使用者自帶金鑰。
- 現行 App 在 `labs/lab10-graduation/`，之後的 Lab 都改這一份；lab01～lab09 是歷史快照，不回頭修改。
- 總指引 `docs/LAB_GUIDE.md`，教材勘誤 `docs/ERRATA.md`。

## 怎麼跑起來
- App：`cd labs/lab10-graduation && python3 -m http.server 8000`，開 http://localhost:8000/ 。service worker 需要 http，`file://` 會在 Console 丟一條註冊錯誤。
- 測試：同目錄 `node test_srs.js && node test_csv.js && node check_words.js`；CI（`.github/workflows/ci.yml`）對 lab09 與 lab10 跑同樣三支。
- AI 功能要 API key：App 第一次按 AI 鈕會 prompt，只存 localStorage；Lab 3 的 CLI 用 `ANTHROPIC_API_KEY="$YTP_ANTHROPIC_API_KEY" python …` 只在該指令內傳入。

## 程式碼慣例（從現有程式碼觀察）
- 2 空格縮排；字串用雙引號；陳述句結尾加分號。
- `const` 優先，需要重新指定才用 `let`，不用 `var`；函式與變數小駝峰（`stateOf`、`importCSV`），常數全大寫（`WORDS`、`INTERVALS`）。
- 不引入任何框架、套件或建置工具；DOM 取用一律 `$("id")`。
- 可測的邏輯抽成純函式獨立檔（`srs.js`、`csv.js`），檔尾加 `if (typeof module !== "undefined") module.exports = …` 讓 Node 與瀏覽器共用；每支都有對應 `test_*.js`，用 Node 內建 `assert`。
- 讀寫 localStorage 一律包 `try/catch`；顯示使用者輸入或模型輸出用 `textContent`，不用 `innerHTML`。
- 每個新函式上方加一行繁體中文註解，固定寫成 `// 用途：…`。
- 主程式檔頂端保留 PLAN 註解（HTML 用 `<!-- PLAN -->`、JS 用 `/* PLAN */`、Python 用 docstring）。

## 協作規矩
- 先有 issue 再動手；每個 Lab 先寫 Plan，由主辦確認後才執行。
- 分支 `labNN/feature/<短名>` 或 `labNN/docs/<短名>`；`main` 只收 PR，合併與建 Release／tag 由管理員在 GitHub 網頁做。
- commit 訊息 `labNN: <類型>: <說明>`，類型沿用教材 feat／fix／docs／test／refactor／chore，說明用繁體中文；關 issue 寫 `closes #N`。
- 每個 Lab 固定三樣：`README.md`（指引）、程式碼（頂端 PLAN）、`CHECKLIST.md`（驗收證據）；做完更新 `docs/LAB_GUIDE.md` 狀態表與根 README 的 Lab 表。
- 教材的錯誤或不周全先記進 `docs/ERRATA.md`（編號 E-NNN、嚴重度、狀態），不直接改教材。
- 全程在瀏覽器與 GitHub 完成，不假設任何人有本機 clone；給管理員的操作一律寫 GitHub 網頁步驟。

## 不要做的事
- 不要把 API key 或任何祕密寫進程式碼、文件或 commit；金鑰只從環境變數或使用者輸入來。
- 不要改 `words.js` 的資料格式（`{en, zh}` 物件陣列）與 `srs.js` 的 `schedule(box, ok, today)` 簽名。
- 不要回頭修改 lab01～lab09 的資料夾。
- 不要自行 push 到 `main`、force push、刪分支或 tag；不要用空 commit 觸發 CI。
- 不要為了讓 CI 綠而跳過、關閉或弱化測試。
