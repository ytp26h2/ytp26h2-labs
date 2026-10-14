# ytp26h2-labs｜YTP2026H2 黑客松 自學教材 Lab 起始點

[![CI](https://github.com/ytp26h2/ytp26h2-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/ytp26h2/ytp26h2-labs/actions/workflows/ci.yml)

這是**公開的範本 repository**，由 YTP 助教維護，提供各個 Lab 的起始檔案。

## 怎麼使用（純自學，主辦不會看到你的練習內容）

1. 登入 GitHub，按本頁右上角綠色的 **Use this template → Create a new repository**。
2. Owner 選**你自己的帳號**（不是 ytp26h2），名稱自訂（例如 `ytp-labs`），可設 Private。
3. 把新 repo clone 到電腦，依各 Lab 資料夾內的 `README.md` 指示完成。
4. 練習過程與結果留在你自己的 repo，不需要繳交；有問題到 Discord #ytp2026h2黑客松 頻道發問。

## Lab 清單

| Lab | 主題 | 狀態 |
|-----|------|------|
| [lab01](labs/lab01-first-commit/) | 第一次提交：可翻面單字卡上 GitHub | ✅ 完成 |
| [lab02](labs/lab02-branch-pr-conflict/) | 分支、PR 與衝突：考我按鈕、自導自演解衝突 | ✅ 完成 |
| [lab03](labs/lab03-example-cli/) | 例句生成 CLI：Python 呼叫 Claude API，JSON＋驗證＋降階 | ✅ 完成 |
| lab04 | 本地模型與切換（選修）：Ollama 跑開源模型＋降階 | ⏸ 暫緩 |
| [lab05](labs/lab05-sprint1-mvp-review-queue/) | Sprint 1 MVP：今日複習佇列，記得／忘了自評，localStorage 學習紀錄 | ✅ 完成 |
| [lab06](labs/lab06-sprint2-ai-example/) | Sprint 2：AI 例句上卡片，瀏覽器直呼 API、自帶金鑰、快取、降階 | ✅ 完成 |
| [lab07](labs/lab07-sprint3-srs/) | Sprint 3：Leitner SRS 排程，純函式＋單元測試，時間旅行 | ✅ 完成 |
| [lab08](labs/lab08-sprint4-smart-quiz/) | Sprint 4：弱點出題（RAG-lite）、單字包 `words.js` 共編與 `check_words.js` | ✅ 完成 |
| [lab09](labs/lab09-ship-it/) | 上線三連發：GitHub Pages、PWA（可安裝、離線）、GitHub Actions CI | ✅ 完成 |
| [lab10](labs/lab10-graduation/) | 發表與畢業：作品級 README、3 分鐘 Demo 逐字稿、畢業挑戰「單字包 CSV 匯入」 | ✅ 完成 |
| [lab11](labs/lab11-agentic-setup/) | 開工準備：代理式編碼工具就位、三個驗證問題、逐步確認、第一次小改動 | ✅ 完成 |
| [lab12](labs/lab12-project-instructions/) | 讓 AI 認識專案：根目錄 `CLAUDE.md` 專案指示檔，對照實驗驗證生效 | ✅ 完成 |
| [lab13](labs/lab13-skill-add-words/) | 第一個技能：`.claude/skills/add-words/SKILL.md`，正負觸發測試 | ✅ 完成 |
| lab14 | 見 [`docs/LAB_GUIDE.md`](docs/LAB_GUIDE.md) | 準備中 |

總指引：[`docs/LAB_GUIDE.md`](docs/LAB_GUIDE.md)｜教材勘誤：[`docs/ERRATA.md`](docs/ERRATA.md)

## 更新

範本更新時，已複製的 repo 不會自動同步。若需要新版，重新 Use this template 一次，或只把有更動的 Lab 資料夾複製過去。

## 授權

與 YTP 教材（github.com/tw-ytp/vocabuddy）一致，採雙軌授權，詳見 `LICENSE`：
- 教材內容（文字、圖表、題目、Lab 說明）：**CC BY-NC-SA 4.0**
- 程式碼（範例、起始碼、設定檔）：**MIT**
