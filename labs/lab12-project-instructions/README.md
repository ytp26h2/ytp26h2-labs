# Lab 12：讓 AI 認識你的專案——專案指示檔

> 教材：<https://tw-ytp.github.io/vocabuddy/#/lab12>（v2.0），內容照 5.2～5.4 與 Lab 12 頁
> 目標：寫一份專案指示檔，走完整的 issue → 分支 → PR → merge，並驗證它真的生效
> 時間：約 40 分鐘｜前置：Lab 11 完成
> 檢查點 tag：`lab12-done`

## 這是什麼

把隊規寫成檔案放進倉庫，讓每個在這個專案裡啟動的代理式編碼工具都讀到同一套規矩。產物是 repo 根目錄的 [`CLAUDE.md`](../../CLAUDE.md)（36 行，五個段落）；本資料夾只有 README 與 CHECKLIST。重點不是寫，是驗證它生效：對照實驗的紀錄在 `CHECKLIST.md`。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 開 issue | 寫下三條規矩 | issue [#37](https://github.com/ytp26h2/ytp26h2-labs/issues/37)：2 空格縮排與不引入框架；`labNN: 類型: 說明` 與 main 只收 PR；新函式加繁中註解。 |
| 開分支 | `feature/project-instructions` | `lab12/feature/project-instructions` |
| 請它草擬，然後你改 | 工具先讀全倉庫再草擬五段，繁中、60 行內；你逐行刪改 | Claude 讀過全倉庫後草擬 25 條，主辦逐條看過後全部認同定稿。慣例全部從現有程式碼觀察（2 空格、雙引號、`const` 優先、`$("id")`、純函式獨立檔＋`test_*.js`、localStorage 包 `try/catch`、`textContent` 不用 `innerHTML`）。 |
| 驗證它真的生效 | 寫一條辨識規矩，清空工作階段，請它加 `shuffleWords()`，看它有沒有自動照做 | 教材建議的辨識規矩「新函式加一行繁中註解」在本 repo 分不出來：**沒有**指示檔的全新 session 也會加中文註解，因為倉庫裡本來就滿是中文註解。於是改成更具體的 `// 用途：…` 格式，並多跑一組對照：先在沒有 `CLAUDE.md` 時跑一次（對照組），定稿後再跑一次（實驗組），兩次都用容器內 `claude -p` 開全新 session 下同一句話。結果見 CHECKLIST。 |
| 提交、發 PR、請隊友 review | `docs:` commit、PR 寫 Closes #N、隊友看過再 merge | 兩個 commit：`lab12: docs:`（CLAUDE.md）、`lab12: feat:`（實驗產物 `shuffleWords()`）；PR closes #37；主辦逐行 review 後合併。 |

## 本 repo 的適配

- **「清空工作階段」怎麼做**：這個 session 不能對自己下 `/clear`，改用容器內的 Claude Code CLI `claude -p "…"` 開一個全新的非互動 session——它啟動時會重新讀 repo 根目錄的 `CLAUDE.md`，和教材「清空後重跑」等價。auto mode 的分類器不允許這個新 session 直接改檔，所以請它把程式碼與位置印出來，由本 session 貼入，再親手驗。
- **實驗產物的去向**：實驗組給的 `shuffleWords(list)` 是純函式（回傳新陣列、不動原陣列），照它的草稿貼進 `labs/lab10-graduation/index.html`；它另建議把載入時的佇列直接打亂，本 repo 沒採用，因為會改變預設複習順序（Demo 腳本與驗收腳本都假設第一張是 algorithm）。改為 Console 輔助 `vbShuffle()`，和 Lab 7 的 `vbTravel()` 同一個模式。
- **只放 Claude Code 一套**：附錄 D 建議範例 repo 只放一種工具的設定。隊伍裡有人用別的工具時，照 5.4 架橋：留 `AGENTS.md` 當本體、在 `CLAUDE.md` 裡用 `@AGENTS.md` 匯入，或做符號連結，只維護一份真本。

## 怎麼驗證

```sh
wc -l CLAUDE.md                                   # ≤ 60
cd labs/lab10-graduation && node test_srs.js && node test_csv.js && node check_words.js
python3 -m http.server 8000                       # 開 http://localhost:8000/，Console 輸入 vbShuffle()
```

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. 倉庫根目錄有一份專案指示檔，檔名符合你用的工具
2. 五個段落齊全，而且每一條你都認同（不是照抄草稿）
3. 總長度在 60 行以內
4. 用對照實驗驗證過它真的生效（清空後重跑，它自動照做了）
5. 經過 issue → 分支 → PR → review → merge 完整走完一輪，issue 自動關閉

## Plan（已確認）

本 Lab 的主要產物是 Markdown，Plan 記在這裡：

1. issue #37 寫三條規矩；分支 `lab12/feature/project-instructions`。
2. 對照組：沒有 `CLAUDE.md` 時用 `claude -p` 全新 session 請它加 `shuffleWords()`，記錄輸出。
3. 草擬 `CLAUDE.md`：讀過全倉庫，五段、繁中、60 行內，慣例從程式碼觀察；全文給主辦逐行刪改後定稿。
4. 實驗組：定稿後同一句話再跑一次，看是否自動加 `// 用途：…`、用 2 空格、不動別的檔；產物保留為 Console 輔助。
5. 驗證：`wc -l`、測試、無頭 Chromium、CI。
6. commit `lab12: docs:` 與 `lab12: feat:` → PR → 主辦逐行 review → merge → Release `lab12-done`。
7. 文件：本資料夾、LAB_GUIDE 第 12 列與段落（補 Lab 11 檢查點）、根 README、ERRATA。
