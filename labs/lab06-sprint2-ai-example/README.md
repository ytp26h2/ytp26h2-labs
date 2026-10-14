# Lab 6（Sprint 2）：AI 例句上卡片

> 教材：<https://tw-ytp.github.io/vocabuddy/#/3-2>（v2.0）
> 目標：把 Lab 3 的例句生成器搬進網頁。翻面後按「AI 例句」，由使用者自己的瀏覽器直呼 Claude API，例句、翻譯、聯想三欄位穩穩落進卡片
> 時間：約 1.5–2.5 小時｜前置：完成 Lab 5；一把 API key（申請方式見教材附錄 B）
> 檢查點 tag：`sprint2-done`

## 這是什麼

Lab 5 的複習迴路不變，翻面後多一顆「AI 例句」按鈕。第一次按會用 `prompt()` 要你貼 API key，key 只存在你自己的瀏覽器 localStorage（`vb-key`），請求直接從你的瀏覽器送到 `api.anthropic.com`。生成過的例句存進 `vb-ai` 快取，同一個字第二次不花錢、秒回、離線也能看。API 失敗一律降階成一句人話，複習照常。

## 怎麼執行

瀏覽器直接開 `index.html`。第一次按「AI 例句」貼上你的 key。要換 key：Console 執行 `localStorage.removeItem("vb-key")`。

## 技術

- `fetch` ＋ `async/await` 直呼 Messages API，標頭 `x-api-key`、`anthropic-version: 2023-06-01`、`anthropic-dangerous-direct-browser-access: true`（瀏覽器直呼必加，名稱就是在提醒你只適合自帶金鑰的個人工具）。
- Structured Output 三板斧：system 給 JSON 骨架、`JSON.parse`、欄位驗證（例句必含目標字）。教材的第二板斧「temperature 調低」在 `claude-sonnet-5-5` 已不適用，見勘誤 E-014。
- 快取與降階：`vb-ai` 命中就不發請求；任何例外（斷網、400、JSON 壞掉、例句沒含字）都走同一句友善訊息。
- 金鑰安全：前端藏不住任何祕密，所以採「使用者自帶金鑰」。repo 內 `git grep sk-` 無金鑰。

## 作者

YTP2026H2 主辦（助教範本）。全程透過 Claude 在瀏覽器中完成。

---

## Plan（已確認，同步寫在 `index.html` 頂端註解）

見 `index.html` 頂端的 PLAN 註解，共 8 步。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 開 issue、開分支 | issue「Sprint 2：卡片上的 AI 例句」；`git switch -c feature/ai-example` | issue [#15](https://github.com/ytp26h2/ytp26h2-labs/issues/15)；分支 `lab06/feature/ai-example`（從 `main` 開）。 |
| 介面加兩個元素 | `#aiBtn` 按鈕、`#ai` 段落；`reveal()` 顯示、`next()` 藏回並清空 | 照做。`next()` 的藏回與清空放在函式開頭，兩個分支都涵蓋。 |
| 核心函式 | `getKey()`、`aiExample()` | 照教材原碼，只改四處（見下）。 |
| 測試三連 | 正常生成＋重按秒回；關網路；無痕視窗 | 無頭 Chromium 攔截 API 模擬三種情境，另以真實 key 做一次端到端。見 `CHECKLIST.md`。 |
| 收工 | commit `closes #5` → PR → merge → `git tag sprint2-done` | commit 用實際編號 #15；PR 三段描述＋自我 review；管理員合併；tag 由管理員以 Release 建立。 |

### 與教材原碼的四處差異（都是為了在 `claude-sonnet-5-5` 上跑得動）

1. **`MODEL = "claude-sonnet-5-5"`**（E-007）。教材的 `claude-sonnet-4-5` 2026-10-14 實測仍可呼叫，但已非當前世代，而且回的是 markdown 圍欄包住的 JSON，教材的 `JSON.parse` 會失敗走降階。
2. **拿掉 `temperature: 0.3`**（E-014）。`claude-sonnet-5-5` 收到 temperature 回 400「`temperature` is deprecated for this model」；被 `catch` 吞掉後畫面只看到「AI 暫時不可用」，學生查不到原因。
3. **`textOf(data)` 依 type 挑 text 區塊**（E-009）。教材的 `data.content[0].text` 在回應先有 thinking 區塊時會炸。
4. **`max_tokens` 300 → 1024**（E-011）。JSON 約 150～200 tokens，留餘裕給可能出現的 thinking。

另外 system prompt 多一句「不要 markdown 圍欄」，是教材急救表自己的建議。`show()` 用 `innerHTML` 塞模型輸出的注入風險，依主辦決定**不改**，記勘誤 E-015 留給教材修訂。

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. 翻面後才看得到「AI 例句」按鈕；例句、翻譯、聯想三欄位正確顯示
2. 同一單字第二次點擊不再呼叫 API
3. 斷網時顯示友善訊息，複習流程完全不受影響
4. `git grep sk-` 找不到任何金鑰；能解釋為什麼公開網頁不能內建 key
5. PR 已合併、tag `sprint2-done` 已推

## 常見錯誤急救（教材原表，另加本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| 401 / invalid x-api-key | key 貼錯或多了空白。Console 執行 `localStorage.removeItem("vb-key")` 重新輸入。 |
| CORS 相關錯誤 | 少了 `anthropic-dangerous-direct-browser-access` 標頭。 |
| JSON.parse 偶爾炸掉 | 模型多話了。已被 catch 接住是底線；system 已加「不要 markdown 圍欄」。 |
| 按了沒反應 | 開 Console 看紅字。 |
| （補充）網路正常卻一直「AI 暫時不可用」 | F12 → Network 看 `messages` 請求的回應。400 多半是新模型不接受的參數（例如 `temperature`，E-014）；401 是 key；若回應 200 但還是降階，看 `content` 第一個區塊是不是 `thinking`（E-009）。 |
| （補充）在 prompt 按了「取消」，之後再也不問 key、每次 401 | `prompt()` 回 `null` 被存成字串 `"null"`（E-016）。`localStorage.removeItem("vb-key")` 後重按。 |

## 為什麼公開網頁不能內建 key

網頁的所有程式碼都會下載到訪客的瀏覽器，「檢視原始碼」一覽無遺；寫進去的 key 等於公開。個人工具的正解是使用者自帶金鑰；要做「內建 AI 的公開服務」需要自己的後端代理，那是第四篇之後的事。
