import os, json, random, requests, markdown, urllib.parse, time, re, sys, io
from datetime import datetime

# [SYSTEM] 한글 및 특수문자 깨짐 방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration] 4호기: PROJECT OMEGA
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
BLOG_TITLE = "PROJECT OMEGA"
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

# [Monetization]
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

# [🔥 8-Word Hooking Titles]
HOOKING_TITLES = [
    "RED ALERT: Dollar Collapse Timeline Leaked",
    "WARNING: 90% of Banks Face Failure",
    "The Great Reset: Protect Your Wealth",
    "Survival Mode: 5 Assets to Own",
    "Hyperinflation Is Here: Secure Your Future",
    "Secret 'Order 66' Protocol in Finance",
    "Urgent: Sell Fake Assets Before Crash",
    "Black Swan: AI Predicts Grid Down",
    "Elite's Escape Plan: Where They Hide",
    "Final Warning: The Debt Bubble Burst"
]

def generate_part(topic, focus):
    # 긴 분량을 유도하는 프롬프트
    prompt = f"Write a professional, terrifying 800-word deep-dive report on '{topic}'. Focus: {focus}. Use bullet points and intense analysis. English Only. Markdown."
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.7}}, timeout=40)
        return resp.json()['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        log(f"API Error: {e}")
        return ""

def create_final_html(topic, img_url, body_html, sidebar_html):
    # 화이트 & 레드 테마 HTML
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Inter&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #fff; --text: #1a1a1a; --accent: #e60000; --sidebar: #f4f4f4; }}
        body {{ font-family: 'Inter', sans-serif; line-height: 1.8; color: var(--text); background: var(--bg); margin: 0; }}
        .container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 300px; gap: 40px; padding: 40px 20px; }}
        header {{ border-bottom: 5px solid var(--accent); padding: 20px; text-align:center; }}
        .brand {{ font-family: 'Oswald', sans-serif; font-size: 2rem; color: var(--accent); letter-spacing: 2px; }}
        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3rem; margin-bottom: 20px; }}
        .content img {{ width: 100%; height: 400px; object-fit: cover; margin-bottom: 30px; border: 1px solid #ddd; }}
        .sidebar {{ position: sticky; top: 20px; height: fit-content; }}
        .side-card {{ background: var(--sidebar); border-top: 4px solid var(--accent); padding: 20px; margin-bottom: 20px; }}
        .btn {{ display: block; padding: 15px; background: #000; color: #fff; text-decoration: none; text-align: center; font-weight: bold; margin-bottom: 10px; }}
        .btn-red {{ background: var(--accent); }}
        footer {{ border-top: 1px solid #ddd; padding: 40px; text-align: center; color: #888; margin-top: 60px; }}
    </style></head>
    <body>
    <header><div class="brand">PROJECT OMEGA</div></header>
    <div class="container">
        <main>
            <div style="color:var(--accent); font-weight:bold; margin-bottom:10px;">[TOP SECRET] EMERGENCY SIGNAL</div>
            <h1>{topic}</h1>
            <div class="content">
                <img src="{img_url}">
                {body_html}
            </div>
        </main>
        <aside class="sidebar">
            <div class="side-card">
                <a href="{EMPIRE_URL}" class="btn btn-red">🛑 GET EXIT PLAN</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT SYSTEM</a>
                <a href="{AMAZON_LINK}" class="btn">🪙 SECURE ASSETS</a>
            </div>
            <div class="side-card">
                <ul style="list-style:none; padding:0; font-size:0.9rem;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>&copy; 2026 PROJECT OMEGA | END-GAME INTEL</footer></body></html>"""

def main():
    log("⚡ Unit 4 Executing...")
    topic = random.choice(HOOKING_TITLES)
    
    # 2단계 생성을 통해 확실한 분량 확보
    p1 = generate_part(topic, "The Financial Collapse Mechanics")
    p2 = generate_part(topic, "Strategic Preservation and Survival")
    full_content = f"{p1}\n\n{p2}"
    
    if not p1: # API 실패 시 비상 리포트 출력
        full_content = "## CRITICAL SYSTEM ERROR: Data Decryption Failed. Check API Status."
    
    html_body = markdown.markdown(full_content)
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red emergency alarm minimalist white background 8k')}"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    sidebar_html = "".join([f"<li><b>!</b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#333; text-decoration:none;'>{h.get('title','Log')}</a></li>" for h in history[:6]])
    
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(full_html)
    with open(os.path.join(BASE_DIR, archive_name), "w", encoding="utf-8") as f: f.write(full_html)
    
    log("✅ Omega Complete.")

if __name__ == "__main__": main()
