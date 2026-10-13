# YTP2026H2 Labs 練習指引（總覽）

本文件是 `ytp26h2-labs` 的總指引：教材有哪些 Lab、本 repo 怎麼對應、每個 Lab 的狀態與入口。每做完一個 Lab 就更新一次。

- 教材：YTP VocaBuddy 開發者之路 v2.0 <https://tw-ytp.github.io/vocabuddy/>（原始檔 <https://github.com/tw-ytp/vocabuddy>）
- 勘誤表：[`ERRATA.md`](ERRATA.md)
- 實作方式：全程透過 Claude 在瀏覽器中完成，程式碼與文件直接進 GitHub，不落地，便於多位作者或多個 Agent 並行協作。

## 工作流程（每個 Lab 都一樣）

1. **Plan**：先寫出該 Lab 的 Plan，由主辦確認。
2. **Plan 入碼**：確認後，Plan 以註解寫在該 Lab 主程式檔頂端（HTML 用 `<!-- PLAN -->`，Python 用 docstring，JS 用 `/* PLAN */`）。
3. **執行**：照教材步驟做，commit 訊息沿用教材「類型: 說明」格式並加 `labNN:` 前綴。
4. **驗收**：教材驗收清單逐項驗證，證據寫進該 Lab 的 `CHECKLIST.md`。
5. **文件**：更新該 Lab 的 `README.md`、本文件的狀態表、必要時 `ERRATA.md`。
6. **里程碑**：打教材對應的 tag（`lab1-done`、`sprint1-done`…）。

## 命名規則

| 項目 | 規則 | 例 |
|---|---|---|
| Lab 資料夾 | `labs/labNN-<kebab-case 短名>/`，NN 兩位數，沿用教材編號 | `labs/lab01-first-commit/` |
| Sprint 類 Lab | 編號沿用 Lab 5–8，短名加 `sprintN-` | `labs/lab05-sprint1-mvp-review-queue/` |
| 每個 Lab 固定檔案 | `README.md`（指引）、程式碼本體（頂端含 PLAN 註解）、`CHECKLIST.md`（驗收紀錄） | — |
| Commit 訊息 | `labNN: <類型>: <說明>`，類型沿用教材（feat／fix／docs／test／refactor／chore） | `lab01: feat: 首頁骨架與可翻面單字卡` |
| 里程碑 tag | 沿用教材附錄 D | `lab1-done`、`sprint1-done`、`v1.0` |
| 分支 | 由主辦指定；Lab 2 起需要功能分支與 PR，於該 Lab 的 Plan 中列出 | — |

## Lab 總表與狀態

| # | Lab | 篇 | 摘要 | 教材時間 | tag | 本 repo 狀態 |
|---|---|---|---|---|---|---|
| 1 | [Lab 1：第一次提交](../labs/lab01-first-commit/) | 一・GitHub | 可翻面單字卡 `index.html`，init→add→commit→push，補 README 與 .gitignore | 40–60 分 | `lab1-done` | ✅ 完成（2026-10-13） |
| 2 | [Lab 2：分支、PR 與衝突](../labs/lab02-branch-pr-conflict/) | 一・GitHub | issue→分支→PR→review→合併；「考我」按鈕；自導自演解一次衝突 | 60–90 分 | `lab2-done` | ✅ 完成（2026-10-13） |
| 3 | [Lab 3：例句生成 CLI](../labs/lab03-example-cli/) | 二・AI 與 LLM | Python 呼叫 Claude API，單字→例句＋翻譯＋聯想；v2 加 JSON、驗證、降階 | 60–90 分 | `lab3-done` | 🔶 程式與文件完成，真實呼叫待 API key |
| 4 | Lab 4：本地模型與切換（選修） | 附錄 E | Ollama 跑 Qwen；CLI 改「雲端優先、本地備援、罐頭墊底」 | 60–90 分 | `lab4-done` | 待做（選修） |
| 5 | Sprint 1（Lab 5）：MVP 今日複習佇列 | 三・開發實戰 | 核心迴路 看卡→回想→翻面→自評→下一張；localStorage 紀錄 | 1 Sprint | `sprint1-done` | 待做 |
| 6 | Sprint 2（Lab 6）：AI 例句上卡片 | 三・開發實戰 | fetch 直呼 API、Structured Output、BYOK＋快取 | 1 Sprint | `sprint2-done` | 待做 |
| 7 | Sprint 3（Lab 7）：SRS 排程演算法 | 三・開發實戰 | 遺忘曲線、Leitner 盒、`srs.js` 純函式＋單元測試、時間旅行 | 1 Sprint | `sprint3-done` | 待做 |
| 8 | Sprint 4（Lab 8）：智慧出題與共編 | 三・開發實戰 | 弱點分析、RAG-lite 出題、`words.js`／`check_words.js` 單字包 PR 共編 | 1 Sprint | `sprint4-done` | 待做 |
| 9 | Lab 9：上線三連發 | 四・上線與發表 | GitHub Pages、PWA、GitHub Actions CI | 60–90 分 | `v1.0` | 待做 |
| 10 | Lab 10：發表與畢業 | 四・上線與發表 | 作品級 README、3 分鐘 Demo、畢業挑戰 | 90 分＋ | `v1.0` | 待做 |
| 11 | Lab 11：開工準備 | 五・AI-Native | 裝代理式編碼工具、三個驗證問題、逐步確認模式、第一次小改動 | 30 分 | `lab11-done` | 待做 |
| 12 | Lab 12：讓 AI 認識專案 | 五・AI-Native | 60 行內專案指示檔（CLAUDE.md），對照實驗驗證，走完整 PR | 40 分 | `lab12-done` | 待做 |
| 13 | Lab 13：第一個技能 | 五・AI-Native | 「新增單字」流程包成 SKILL.md，正反驗證觸發 | 45 分 | `lab13-done` | 待做 |
| 14 | Lab 14：子代理 review | 五・AI-Native | 唯讀 code-reviewer 子代理對真實 PR 跑一次，比較機器審 vs 人審 | 35 分 | `lab14-done` | 待做 |

共 14 個 Lab：13 個主線＋1 個選修（Lab 4）。各篇另有自我檢測（quiz），不列為 Lab。

## 各 Lab 摘要

### Lab 1：第一次提交 ✅

- 產出：`labs/lab01-first-commit/`（`index.html`、`README.md`、`.gitignore`、`CHECKLIST.md`）
- 兩個 commit：`lab01: feat: 首頁骨架與可翻面單字卡`、`lab01: docs: README 與 gitignore`
- 檢查點：`lab1-done` 應指向 `main` 上的合併 commit `c7b512b`（PR ytp26h2/ytp26h2-labs#2 合併結果）。本 session 的 GitHub 憑證推不了 tag，依流程由 repo 管理員在 GitHub Releases 頁以 Target=`main` 建立 release 並同時建立 tag。
- 適配：所有 Lab 集中於單一 repo，教材的 `git init`、建遠端、首次 push 以對照表呈現，不重做；自學者仍應照教材原步驟做。
- 勘誤：E-001～E-004（見 `ERRATA.md`），皆為不周全而非錯誤。

### Lab 2：分支、PR 與衝突 ✅

- 產出：`labs/lab02-branch-pr-conflict/`（`index.html`、`README.md`、`.gitignore`、`CHECKLIST.md`）
- GitHub 紀錄：issue [#3](https://github.com/ytp26h2/ytp26h2-labs/issues/3) → PR [#4](https://github.com/ytp26h2/ytp26h2-labs/pull/4)（含行內評論，由 `tw-ytp` 合併）→ 衝突合併 commit `5403879` → Lab 2 收尾 PR
- 分支：`lab02/feature/quiz-button`（已合併並刪除）、`lab02/rename`（衝突演練用，合併後刪除）
- 適配：本 repo 的 `main` 只接受 PR，衝突演練以工作分支扮演教材的 `main`，結果再經 PR 進 `main`。
- 勘誤：E-005、E-006（見 `ERRATA.md`）。
- 檢查點：`lab2-done` 由管理員在收尾 PR 合併後，以 Target=`main` 建立 release 並同時建立 tag。

### Lab 3：例句生成 CLI 🔶

- 產出：`labs/lab03-example-cli/`（`tools/gen_example.py`、`tools/requirements.txt`、`index.html`、`README.md`、`.gitignore`、`CHECKLIST.md`）
- GitHub 紀錄：issue [#6](https://github.com/ytp26h2/ytp26h2-labs/issues/6) → PR [#7](https://github.com/ytp26h2/ytp26h2-labs/pull/7)（分支 `lab03/feature/example-cli`，由 `tw-ytp` 合併，merge commit `e6ae96b`）→ issue 自動關閉
- 模型：`claude-sonnet-5-5`（主辦指定）。SDK：`anthropic` 1.x，需 Python 3.10+。
- 已驗證（不需 key）：程式可編譯；斷網降階輸出罐頭、exit 0；v2 驗證／重試／降階邏輯以假回應測過五種情境；repo 內無金鑰。
- 待 key：v1 兩個實驗（取樣、B1→C2）、v2 五個單字真實呼叫、E-009 真實回應驗證。金鑰放雲端環境設定的 `ANTHROPIC_API_KEY`，新 session 讀取後補做。2026-10-13 第二個 session 讀不到該變數，補做未成，步驟與紀錄見 `CHECKLIST.md`「補做紀錄」。
- 勘誤：E-007～E-010（見 `ERRATA.md`）。E-009 影響最大：教材 `content[0].text` 在新模型上會失敗。
- 檢查點：`lab3-done` 已由管理員建立，指向 `main` 上的合併 commit `e6ae96b`。
