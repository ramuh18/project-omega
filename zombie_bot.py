import os, json, random, requests, markdown, urllib.parse, feedparser, time, re, sys, io
from datetime import datetime

# [SYSTEM]
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration] 4호기: PROJECT OMEGA (White & Red Edition)
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

def generate_part(topic, focus, min_words=800):
    # 분량 확보를 위해 구체적인 단어 수와 심층 분석 요구
    prompt = f"Write an extremely detailed, technical 800-word survival report on '{topic}'. Focus: {focus}. Tone: Urgent, Professional, Dark. Use data-driven warnings. Markdown. English Only."
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.7}}, timeout=40)
        return resp.json()['candidates'][0]['content']['parts'][0]['text'].strip()
    except: return ""

def create_final_html(topic, img_url, body_html, sidebar_html):
    # 화이트 바탕 & 레드 포인트 레이아웃
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #ffffff; --text: #1a1a1a; --accent: #e60000; --sidebar-bg: #f8f8f8; }}
        body {{ font-family: 'Inter', sans-serif; line-height: 1.8; color: var(--text); background: var(--bg); margin: 0; }}
        .container {{ max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 1fr 340px; gap: 60px; padding: 60px 20px; }}
        @media(max-width: 1100px) {{ .container {{ grid-template-columns: 1fr; }} }}
        header {{ border-bottom: 5px solid var(--accent); background: #fff; padding: 25px; text-align:center; }}
        .brand {{ font-family: 'Oswald', sans-serif; font-size: 2.2rem; color: var(--accent); letter-spacing: 3px; }}
        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3.5rem; color: #000; margin-bottom: 30px; line-height: 1.1; }}
        .content {{ font-size: 1.2rem; }}
        .content h2 {{ color: var(--accent); border-bottom: 3px solid var(--accent); margin-top: 50px; font-family: 'Oswald', sans-serif; }}
        .featured-img {{ width: 100%; height: 500px; object-fit: cover; border: 1px solid #ddd; }}
        .sidebar {{ position: sticky; top: 50px; }}
        .side-card {{ background: var(--sidebar-bg); border: 1px solid #ddd; padding: 25px; margin-bottom: 25px; border-top: 4px solid var(--accent); }}
        .btn {{ display: block; padding: 18px; background: #000; color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 12px; }}
        .btn-red {{ background: var(--accent); }}
        footer {{ border-top: 1px solid #ddd; padding: 60px; text-align: center; color: #777; background: #fafafa; }}
    </style></head>
    <body>
    <header><div class="brand">PROJECT OMEGA</div></header>
    <div class="container">
        <main>
            <div style="background:var(--accent); color:#fff; padding:5px 15px; display:inline-block; font-weight:bold; margin-bottom:20px;">EMERGENCY BROADCAST</div>
            <h1>{topic}</h1>
            <img src="{img_url}" class="featured-img">
            <div class="content">{body_html}</div>
        </main>
        <aside class="sidebar">
            <div class="side-card">
                <a href="{EMPIRE_URL}" class="btn btn-red">🛑 DOWNLOAD EXIT PLAN</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT SYSTEM</a>
                <a href="{AMAZON_LINK}" class="btn">🪙 SECURE ASSETS</a>
            </div>
            <div class="side-card">
                <div style="font-family:Oswald; font-size:1.2rem; margin-bottom:15px;">LATEST ALERTS</div>
                <ul style="list-style:none; padding:0; line-height:2;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>&copy; 2026 PROJECT OMEGA | END-GAME INTELLIGENCE</footer></body></html>"""

def main():
    log("⚡ Unit 4 (Omega) Executing...")
    topic = random.choice(HOOKING_TITLES)
    # 분량을 위해 3가지 세부 주제로 생성
    p1 = generate_part(topic, "The Macro Collapse Indicators")
    p2 = generate_part(topic, "Systemic Risk and Bank Failures")
    p3 = generate_part(topic, "Ultimate Survival and Asset Protection")
    full_content = f"{p1}\n\n{p2}\n\n{p3}"
    
    html_body = markdown.markdown(full_content)
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red alarm siren emergency light minimalism 8k')}"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    sidebar_html = "".join([f"<li><b style='color:red;'>!</b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#444; text-decoration:none;'>{h.get('title','Signal')}</a></li>" for h in history[:8]])
    
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(full_html)
    with open(os.path.join(BASE_DIR, archive_name), "w", encoding="utf-8") as f: f.write(full_html)
    
    log("✅ Omega Protocol Complete.")

if __name__ == "__main__": main()
