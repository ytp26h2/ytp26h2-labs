---
name: add-words
description: 新增或修改單字包時使用。使用者說「加單字」「新增單字」「加幾個某主題的字」「改字表」「動 words.js」「單字包」都算。包含 words.js 的格式規範、加在陣列最後、重複檢查，以及提交前必跑的 check_words.js 驗證與 commit 訊息格式。
---

# 新增單字流程

單字包在 `labs/lab10-graduation/words.js`（現行 App）。lab01～lab09 是歷史快照，不要動那裡的單字。

1. 先讀 `labs/lab10-graduation/words.js` 確認現有格式：每筆是 `{en:"…", zh:"…"}` 兩個欄位，`en` 小寫英文、`zh` 繁體中文，不要自創欄位。
2. 新單字加在陣列最後，前面加一行 `// 主題` 註解分組（照檔案裡既有的寫法），不要重排既有順序，減少 PR 的無謂差異。
3. 在 `labs/lab10-graduation/` 執行 `node check_words.js`，必須看到「檢查通過，共 N 字」才算完成。
4. 若報「重複單字」或「欄位缺漏」，修掉那一筆，重跑直到通過。`check_words.js` 的重複檢查區分大小寫、也不檢查 `en` 是否小寫或 `zh` 是否中文，這三點要自己看。
5. 通過後才 commit，只 commit `words.js`，訊息格式：`labNN: feat: 新增 N 個「主題」單字`。NN 取目前分支名開頭的 `labNN`（`git branch --show-current`）。分支是 `main` 或不是 `labNN/…` 開頭，就停下來問人，不要 commit、不要猜。
6. 不要自動推遠端，push 與 PR 由人執行。
