import os, json, random, requests, markdown, urllib.parse, time, re, sys, io
from datetime import datetime

# [SYSTEM] 한글 깨짐 방지 및 경로 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration] 4호기 전용 설정
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
BLOG_TITLE = "PROJECT OMEGA"
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

# 수익화 링크
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

# [🔥 4호기 전용 전문적 제목] - 3호기와 겹치지 않는 거시경제 주제
HOOKING_TITLES = [
    "2026 Global Liquidity Freeze Protocol",
    "National Debt Supercycle: The Final Stage",
    "Central Bank Digital Currency: Asset Lockout",
    "Systemic Banking Failure: Macro Analysis",
    "Hyperinflationary Surge and Wealth Erasure",
    "The 130% Debt-to-GDP Breaking Point",
    "Institutional Exit Strategies: Classified Data",
    "Gold and Bitcoin: The New Sovereign Reserve"
]

def generate_formal_report(topic):
    # 4호기 전용 페르소나: 냉철한 정부 수석 분석가
    prompt = f"""
    You are a Senior Macroeconomic Analyst for 'Project Omega' Strategic Crisis Department. 
    Write an official, cold, and highly technical emergency report on '{topic}'. 
    
    [STRICT INSTRUCTIONS]
    1. Tone: Institutional, Professional, and Urgent. NO slang.
    2. Length: At least 2000 words. Be extremely detailed.
    3. Structure: 
       - Start with '[TOP SECRET] EMERGENCY SIGNAL - LEVEL 4 ACCESS ONLY'
       - Section 1: Executive Summary of the Crisis.
       - Section 2: Macro-data Analysis (Mention Debt-to-GDP, Interest rates, Liquidity).
       - Section 3: Systemic Impact on Fiat Currencies.
       - Section 4: Mandatory Action Protocol (5-step Survival Instruction).
    4. Language: English Only. Use Professional Financial Terminology.
    5. Formatting: Use Markdown with bold headers and bullet points.
    """
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        # maxOutputTokens를 높여서 긴 글 생성 유도
        resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.5, "maxOutputTokens": 4096}}, timeout=60)
        res_json = resp.json()
        if 'candidates' in res_json:
            return res_json['candidates'][0]['content']['parts'][0]['text'].strip()
        return "## [ALERT] SYSTEM ERROR: Decryption Failed. Check API Quota."
    except Exception as e:
        log(f"API Error: {e}")
        return "## [ALERT] CONNECTION LOST: Strategic Data Unavailable."

def create_final_html(topic, img_url, body_html, sidebar_html):
    # 화이트 & 레드 테마 디자인
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #ffffff; --text: #1a1a1a; --accent: #e60000; --sidebar-bg: #f9f9f9; }}
        body {{ font-family: 'Inter', sans-serif; line-height: 1.8; color: var(--text); background: var(--bg); margin: 0; }}
        header {{ border-bottom: 5px solid var(--accent); background: #fff; padding: 25px; text-align: center; position: sticky; top:0; z-index:10; }}
        .brand {{ font-family: 'Oswald', sans-serif; font-size: 2rem; color: var(--accent); letter-spacing: 2px; }}
        .container {{ max-width: 1300px; margin: 0 auto; display: grid; grid-template-columns: 1fr 320px; gap: 50px; padding: 40px 20px; }}
        @media(max-width: 1000px) {{ .container {{ grid-template-columns: 1fr; }} }}
        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3.5rem; color: #000; margin-bottom: 30px; line-height: 1.1; }}
        .alert-tag {{ background: var(--accent); color: #fff; padding: 5px 15px; font-weight: bold; margin-bottom: 20px; display: inline-block; }}
        .content {{ font-size: 1.15rem; color: #333; }}
        .content h2 {{ color: var(--accent); border-bottom: 2px solid var(--accent); padding-bottom: 5px; margin-top: 50px; font-family: 'Oswald', sans-serif; }}
        img {{ width: 100%; height: 500px; object-fit: cover; border: 1px solid #ddd; margin-bottom: 40px; }}
        .sidebar {{ position: sticky; top: 120px; height: fit-content; }}
        .side-card {{ background: var(--sidebar-bg); border: 1px solid #ddd; padding: 25px; margin-bottom: 25px; border-top: 4px solid var(--accent); }}
        .btn {{ display: block; padding: 18px; background: #000; color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 12px; transition: 0.3s; }}
        .btn-red {{ background: var(--accent); }}
        .btn:hover {{ background: #333; transform: translateY(-2px); }}
        footer {{ border-top: 1px solid #ddd; padding: 60px; text-align: center; font-size: 0.9rem; color: #777; background: #fcfcfc; }}
    </style></head>
    <body>
    <header><div class="brand">PROJECT OMEGA</div></header>
    <div class="container">
        <main>
            <div class="alert-tag">TOP SECRET // OFFICIAL REPORT</div>
            <h1>{topic}</h1>
            <img src="{img_url}">
            <div class="content">{body_html}</div>
        </main>
        <aside class="sidebar">
            <div class="side-card">
                <a href="{EMPIRE_URL}" class="btn btn-red">🛑 ACCESS EXIT PLAN</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT MARKET</a>
                <a href="{AMAZON_LINK}" class="btn">🛡️ SECURE ASSETS</a>
            </div>
            <div class="side-card">
                <div style="font-family:Oswald; font-size:1.2rem; margin-bottom:15px;">LATEST REPORTS</div>
                <ul style="list-style:none; padding:0; line-height:2.2; font-size:0.9rem;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>&copy; 2026 PROJECT OMEGA | STRATEGIC INTELLIGENCE<br>Amazon Associate Disclaimer included.</footer></body></html>"""

def main():
    log("⚡ Unit 4 (Omega) Initializing Heavy Protocol...")
    topic = random.choice(HOOKING_TITLES)
    
    # 초장문 생성을 위한 메인 로직
    full_text = generate_formal_report(topic)
    html_body = markdown.markdown(full_text)
    
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red danger alarm light minimal white clean professional 8k photography')}"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    sidebar_html = "".join([f"<li><b style='color:red;'>[!]</b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#333; text-decoration:none;'>{h.get('title','Report')}</a></li>" for h in history[:10]])
    
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(full_html)
    with open(os.path.join(BASE_DIR, archive_name), "w", encoding="utf-8") as f: f.write(full_html)
    
    log("✅ Omega Protocol V3 Executed.")

if __name__ == "__main__": main()
