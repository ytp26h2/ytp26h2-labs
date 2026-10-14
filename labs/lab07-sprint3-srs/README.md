# Lab 7（Sprint 3）：SRS 排程——Leitner 盒

> 教材：<https://tw-ytp.github.io/vocabuddy/#/3-3>（v2.0）
> 目標：把「每天全部複習」換成間隔重複（SRS）。排程規則寫成純函式，用單元測試釘死，再接進 App
> 時間：約 1.5–2.5 小時｜前置：完成 Lab 6；Node.js（跑測試用）
> 檢查點 tag：`sprint3-done`

## 這是什麼

Leitner 五盒：間隔 1／2／4／8／16 天，答對晉一級（間隔加倍），答錯打回盒 1。每張卡在 `log` 裡多兩個欄位 `box`、`due`（第幾天到期）；每天只複習到期的卡，全答完顯示「今天沒有到期的卡——明天見！」。Console 輸入 `vbTravel(n)` 可以快轉 n 天，親眼看佇列隨間隔拉長而變稀疏。

## 怎麼執行

```bash
cd labs/lab07-sprint3-srs
node test_srs.js        # 4 tests passed ✓
```

瀏覽器直接開 `index.html`。時間旅行：F12 Console 輸入 `vbTravel(2)` 快轉兩天，玩完 `vbTravel(-總天數)` 歸零，或 `localStorage.removeItem("vb-day")`。

## 技術

- `srs.js`：純函式 `schedule(box, ok, today)`，不碰畫面、不自己看時鐘，輸入什麼就決定輸出什麼，所以 Node 與瀏覽器都能用、也能測。
- `test_srs.js`：四條 `assert.deepStrictEqual`，「今天」永遠是第 100 天，結果可重現。
- `index.html`：`today()` 以「第幾天」為單位（`Date.now()/864e5` 取整加 `dayOffset`）；`stateOf()` 幫 Lab 5／6 的舊紀錄自動補 `box`、`due`（資料改版必附遷移）；`queue` 只放 `due <= today()` 的卡；`mark()` 把排程交給 `schedule()`。Lab 6 的 AI 例句原樣保留。

### 為什麼 `schedule()` 不自己呼叫 `Date.now()`

如果它自己看時鐘，同一組輸入在不同時刻會得到不同輸出，測試就寫不出「第 100 天答對盒 3 應該是第 108 天到期」這種可重現的斷言；時間旅行也做不到，因為你改不了函式裡的時鐘。把「今天」當參數傳進去，函式就變成純函式：測試自己決定今天是哪一天，App 用真時鐘加偏移量，兩邊共用同一條規則。

## 作者

YTP2026H2 主辦（助教範本）。全程透過 Claude 在瀏覽器中完成。

---

## Plan（已確認，同步寫在 `index.html` 頂端註解）

見 `index.html` 頂端的 PLAN 註解，共 8 步。

## 步驟對照（教材 ↔ 本 repo）

| 教材步驟 | 教材要你做 | 本 repo 實際發生的事 |
|---|---|---|
| 開 issue、開分支 | issue「Sprint 3：SRS 排程（Leitner）」，驗收條件直接寫測試案例；`git switch -c feature/srs` | issue [#18](https://github.com/ytp26h2/ytp26h2-labs/issues/18)；分支 `lab07/feature/srs`（從 `main` 開）。 |
| 寫 srs.js | 純函式 `schedule` | 照教材原碼，頂端加一行指回 PLAN。 |
| 先寫測試、跑測試 | `test_srs.js` 四條，`node test_srs.js` | 照做，4 tests passed。另把 `INTERVALS` 每一格各改壞一次：1、2、4、5 格會被抓到，**第 3 格不會**（E-018）。 |
| 接進 App | 引入 `srs.js`，改 queue 初始化與 `mark`，完成訊息改「明天見」 | 照教材原碼一字未改。 |
| 時間旅行驗證 | Console `vbTravel(1)`… | 無頭 Chromium 直接寫 `localStorage` 的 `vb-day` 後 reload，逐日檢查 46 天，見 `CHECKLIST.md`。教材寫 `vbTravel(1)` 後 8 張回來，實測是 0 張、`vbTravel(2)` 才回來（E-017）。 |
| 收工 | commit `closes #6` → PR → merge → `git tag sprint3-done` | commit 用實際編號 #18；PR 三段描述＋自我 review；管理員合併；tag 由管理員以 Release 建立。 |

## 驗收清單

見 `CHECKLIST.md`。教材原始五項：

1. `node test_srs.js` 四條測試全過；故意把 `INTERVALS` 改壞一格，測試會抓到
2. 新的一天只出現「到期」的卡；全答完顯示「明天見」
3. 用 `vbTravel` 驗證：答對的卡間隔按 1→2→4→8→16 拉長；答錯的隔天就回來
4. 能對隊友解釋：為什麼 `schedule()` 不自己呼叫 `Date.now()`
5. PR 已合併、tag `sprint3-done` 已推

## 實作時發現的三件事（勘誤 E-017～E-019）

1. **時間旅行的敘述與程式對不上**。新卡初始是盒 1、`due` 今天；答對後進盒 2，間隔是 `INTERVALS[2] = 2` 天。所以教材「`vbTravel(1)`：8 張卡到期回來了」實測是 0 張，要 `vbTravel(2)`；驗收第 3 項「間隔按 1→2→4→8→16」也不對，新卡的第一個間隔是 2，間隔 1 只出現在答錯之後。而且答錯的卡當天會排隊尾再考，答對後就進盒 2 間隔 2 天，「答錯的隔天就回來」只有在答錯後關掉頁面不重考才會發生。
2. **四條測試沒覆蓋盒 3**。`INTERVALS[3]` 改壞測試照樣通過。加一條 `schedule(2, true, 100) → {box: 3, due: 104}` 就補齊。
3. **`today()` 用 UTC 日**。`Math.floor(Date.now() / 864e5)` 是 UTC 的第幾天，台灣（UTC+8）早上 8 點才換日：晚上 11 點答完的卡，隔天早上 7 點還是「同一天」。影響不大，但學生時間旅行時可能困惑。

## 常見錯誤急救（教材原表，另加本 repo 補充）

| 症狀 | 原因與解法 |
|---|---|
| `schedule is not defined` | `srs.js` 要在主 script 之前引入。 |
| `module is not defined`（瀏覽器） | 少了 `typeof module !== "undefined"` 那行防護。 |
| 佇列永遠是空的 | 之前玩 `vbTravel` 忘了歸零——Console 看 `localStorage.getItem("vb-day")`。 |
| 舊使用者一打開就壞 | 忘了 `stateOf` 的「舊紀錄自動升級」。 |
| （補充）`vbTravel(1)` 後什麼都沒有 | 正常。新卡答對後間隔是 2 天，再 `vbTravel(1)` 就回來了（E-017）。 |
