# Lab 12 驗收紀錄

驗證日期：2026-10-14｜驗證方式：對照實驗以容器內 Claude Code CLI `claude -p` 開全新非互動 session（等價於教材的「清空工作階段」），兩次輸出全文存於驗證環境並摘錄於下；程式部分以 Node 22 與無頭 Chromium（本地 `http://localhost`）驗證。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

## 教材驗收清單（Lab 12 頁）

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 倉庫根目錄有一份專案指示檔，檔名符合你用的工具 | ✅ | `/CLAUDE.md`（Claude Code 讀 `CLAUDE.md`，不讀 `AGENTS.md`，5.1 對照表）。 |
| 2 | 五個段落齊全，而且每一條你都認同（不是照抄草稿） | ✅ | 五段：這是什麼專案（4 條）／怎麼跑起來（3）／程式碼慣例（7）／協作規矩（6）／不要做的事（5），共 25 條。草稿全文列給主辦逐條刪改，主辦 2026-10-14 回覆「全部認同，定稿」。慣例條目逐一對應到現有程式碼（見下方觀察表）。 |
| 3 | 總長度在 60 行以內 | ✅ | `wc -l CLAUDE.md` → 36。 |
| 4 | 用對照實驗驗證過它真的生效（清空後重跑，它自動照做了） | ✅ | 見下方「對照實驗」：實驗組自動寫出 `// 用途：…` 註解並引用 CLAUDE.md 的純函式慣例；對照組沒有。 |
| 5 | 經過 issue → 分支 → PR → review → merge 完整走完一輪，issue 自動關閉 | ⏳ | issue #37 → 分支 `lab12/feature/project-instructions` → PR（closes #37）；主辦逐行 review 與合併後補記。 |

## 對照實驗

同一句話，兩個全新 session：

> 在 labs/lab10-graduation/index.html 加一個 shuffleWords() 把單字順序打亂。請先讀檔，然後把要新增的程式碼與要放的位置印出來給我，我自己貼進去。

| | 對照組（沒有 CLAUDE.md） | 實驗組（CLAUDE.md 定稿後） |
|---|---|---|
| 註解 | `// 打亂今日佇列的順序（Fisher-Yates），再重新出卡`——有繁中註解，但不是指示檔要求的格式 | `// 用途：Fisher-Yates 洗牌，回傳打亂順序的新陣列（不改動原陣列）`——完全照 CLAUDE.md 第 13 條的 `// 用途：…` 格式，提示裡一個字都沒提 |
| 函式設計 | 直接打亂全域 `queue`，然後呼叫 `next()` | 純函式 `shuffleWords(list)`，`slice()` 後洗牌、回傳新陣列，並說明「回傳新陣列⋯之後要寫測試也比較容易」 |
| 縮排與風格 | 2 空格、`const`／`let`、分號 | 2 空格、`const`／`let`、分號 |
| 額外建議 | 建議在 `#aiBtn` 後加一顆「打亂順序」按鈕 | 建議把載入時的佇列改成打亂；並主動提到「CLAUDE.md 慣例是可測的邏輯抽成純函式獨立檔並附 `test_*.js`，你指定放在 index.html 我就照做」 |
| 動到別的檔 | 無（依指示只印不改） | 無 |

**判讀**：指示檔生效，證據是兩個提示裡都沒出現的 `用途：` 四個字與對純函式慣例的引用。**同時發現**教材建議的辨識規矩「新函式加一行繁體中文註解」在這個 repo 不能用來辨識：對照組沒有指示檔也加了中文註解，因為它模仿倉庫既有的註解風格（勘誤 E-029）。辨識規矩要選「模型照抄現狀也不會自然做到」的事。

## 慣例觀察表（CLAUDE.md 程式碼慣例的來源）

| 條目 | 從哪裡觀察到 |
|---|---|
| 2 空格縮排 | `index.html`、`csv.js`、`srs.js` 全部以兩個空格開頭的行為主（97／15／2 行） |
| 雙引號、分號 | `index.html` 雙引號字串 154 處、單引號 3 處（都在 system prompt 內文）；陳述句以分號結尾 |
| `const` 優先、不用 `var` | `index.html` 27 個 `const`、6 個 `let`、0 個 `var`；`csv.js` 8／2／0 |
| 小駝峰、常數全大寫 | `stateOf`、`importCSV`、`callClaude`、`weakest`；`WORDS`、`INTERVALS`、`MODEL`、`CACHE`、`SHELL` |
| `$("id")` | `index.html` 的 `const $ = id => document.getElementById(id);` |
| 純函式獨立檔＋`module.exports`＋`test_*.js` | `srs.js`／`test_srs.js`（Lab 7）、`csv.js`／`test_csv.js`（Lab 10） |
| localStorage 包 `try/catch` | `log`、`dayOffset`、`vb-key`、`vb-ai`、`vb-words` 的讀寫 |
| `textContent` 不用 `innerHTML` | Lab 10 匯入訊息；E-015、E-020 記錄的反例是教材原碼 |
| PLAN 註解 | 每個 Lab 主程式檔頂端 |

## 程式驗證（實驗產物）

| 檢查 | 結果 |
|---|---|
| `node test_srs.js`、`node test_csv.js`、`node check_words.js` | 通過（21 字） |
| 無頭 Chromium D1 預設順序不變：第一張 algorithm、21 張 | ✅ |
| D2 `shuffleWords` 純函式：不改原陣列、回傳新陣列、元素集合相同 | ✅ |
| D3 `vbShuffle()` 五次：集合不變、張數不變、卡片＝`queue[0]` | ✅ |
| D4 五次順序皆改變 | ✅（5/5） |
| D5 打亂後複習迴路照常 | ✅ |
| 全程 `pageerror` | 0 筆 |
| Lab 10 匯入腳本回歸 | 20 項中 12 過，8 項失敗全是單字數假設（腳本寫死 18 字，Lab 11 後為 21 字），功能訊息皆正確 |
| Lab 9 PWA 腳本回歸 | 11 項中 9 過，2 項失敗同為 18 字假設 |
