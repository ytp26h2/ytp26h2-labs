"""
PLAN｜Lab 3：例句生成 CLI——第一次讓程式呼叫 AI
教材：https://tw-ytp.github.io/vocabuddy/#/lab3（v2.0，2026-09-08）
確認日期：2026-10-13（由 YTP 主辦確認後執行；模型指定 claude-sonnet-5-5）
起點：Lab 2 成果複製到 labs/lab03-example-cli/

 1. 建立本資料夾：複製 Lab 2 的 index.html 與 .gitignore（加 .env、__pycache__/），
    tools/requirements.txt 釘 anthropic 1.x。
 2. 開 issue「AI 例句生成 CLI」→ #6。
 3. 從 main 開分支 lab03/feature/example-cli。
 4. v1：本檔照教材原碼，自由文字輸出。commit「lab03: feat: 例句生成 CLI v1」。
 5. 兩個實驗（需 API key）：同字跑兩次比較「取樣」；B1 改 C2 比較 prompt 威力。
    心得寫進 issue #6 留言。
 6. v2：只回 JSON、欄位驗證、例句必含單字、失敗重試一次、罐頭降階。
    commit「lab03: feat: 例句生成 CLI v2（JSON＋驗證＋降階），closes #6」。
 7. 斷網測試（不需 key）：ANTHROPIC_BASE_URL 指向不存在的位址執行 v2，
    不噴 traceback、輸出罐頭內容。
 8. PR → main，三段描述；自我 review 留行內評論；由管理員合併。
 9. 驗收：git grep sk- 一無所獲；v2 對 5 個單字回合法 JSON 且含單字（需 key）；
    斷網降階；PR 合併、issue 自動關閉。
10. 文件：README、CHECKLIST.md、docs/LAB_GUIDE.md、根目錄 README；管理員建 lab3-done。
勘誤候選：教材模型名稱 claude-sonnet-4-5 已過時（E-007）；
         SDK 1.x 需 Python 3.10+，教材前置寫 3.9+（E-008）。

用法：
    pip install -r tools/requirements.txt
    export ANTHROPIC_API_KEY="你的key"      # 放環境變數，不放程式碼
    python tools/gen_example.py algorithm
"""
import sys
import json
import anthropic

MODEL = "claude-sonnet-5-5"   # 模型名稱會更新，最新值見教材附錄 B
PROMPT = ("為英文單字「{word}」產生學習卡內容。只回傳 JSON，不要其他文字，不要 markdown 圍欄，"
          '格式：{{"word": "...", "sentence": "...", "zh": "...", "tip": "..."}}。'
          "sentence 用 CEFR B1 難度，且必須包含該單字。")
FALLBACK = {"sentence": "Practice makes perfect.",
            "zh": "熟能生巧。", "tip": "（預設內容：AI 暫時不可用）"}


def text_of(msg):
    """取出回應中的文字區塊。新模型預設會先回 thinking 區塊，
    直接拿 content[0].text 會失敗（見勘誤 E-009），所以依 type 挑文字。"""
    return "".join(b.text for b in msg.content if b.type == "text")


def ask(client, word):
    msg = client.messages.create(
        model=MODEL, max_tokens=1024,   # 教材原值 300，thinking token 也算在內，見勘誤 E-011
        system="你是高中英語老師。只輸出 JSON。",
        messages=[{"role": "user", "content": PROMPT.format(word=word)}],
    )
    return text_of(msg)


def generate(word):
    client = anthropic.Anthropic()
    for attempt in range(2):              # 失敗最多重試一次
        try:
            data = json.loads(ask(client, word))
            if word.lower() in data["sentence"].lower():
                return data               # 驗證通過才放行
        except (json.JSONDecodeError, KeyError, TypeError, anthropic.APIError):
            pass
    return {"word": word, **FALLBACK}     # 降階：永遠有東西可給


if __name__ == "__main__":
    word = sys.argv[1] if len(sys.argv) > 1 else "interval"
    print(json.dumps(generate(word), ensure_ascii=False, indent=2))
