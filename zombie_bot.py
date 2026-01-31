import os, json, random, requests, markdown, urllib.parse, feedparser, time, re, sys, io
from datetime import datetime

# [SYSTEM]
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

# [🔥 HOOKING TITLES] 8단어 미만, 영문 후킹 제목
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

# [Sitemap]
def generate_sitemap(history):
    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    today = datetime.now().strftime('%Y-%m-%d')
    urls = [f"<url><loc>{BLOG_BASE_URL}</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>"]
    for item in history[:50]:
        file_name = item.get('file', '')
        file_date = item.get('date', today)
        if file_name:
            urls.append(f"<url><loc>{BLOG_BASE_URL}{file_name}</loc><lastmod>{file_date}</lastmod><priority>0.8</priority></url>")
    xml_content = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{"".join(urls)}</urlset>'
    with open(sitemap_path, "w", encoding="utf-8") as f: f.write(xml_content)
    log("📡 Sitemap.xml updated.")

# [FALLBACK] 비상용 원고
FALLBACK_REPORT = """
## DEFCON 1: The System Is Resetting

The indicators are flashing red. This is a total structural collapse of the fiat system.

### 1. Currency Debasement
Purchasing power is eroding. The only exit is hard assets that cannot be printed.

### 2. The Great Wealth Transfer
Elites are moving capital into Bitcoin and Gold. If your assets are in a bank, they are not yours.

### 3. Survival Protocol
1. Secure a hardware wallet.
2. Automate your accumulation.
3. Prepare for the lockout.
"""

def generate_part(topic, focus):
    prompt = f"Write a terrifying 600-word survival report on '{topic}'. Focus: {focus}. Tone: Apocalyptic, Urgent. Short sentences. Markdown. English Only."
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.6}}, timeout=30)
        res = resp.json()['candidates'][0]['content']['parts'][0]['text']
        return re.sub(r'\{"role":.*?"content":', '', res, flags=re.DOTALL).replace('"}', '').strip()
    except: return ""

def create_final_html(topic, img_url, body_html, sidebar_html):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Roboto+Mono&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #000; --text: #ccc; --accent: #ff003c; --card: #111; }}
        body {{ font-family: 'Roboto Mono', monospace; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }}
        .container {{ max-width: 1500px; margin: 0 auto; display: grid; grid-template-columns: 1fr 320px; gap: 40px; padding: 40px 20px; }}
        @media(max-width: 1000px) {{ .container {{ grid-template-columns: 1fr; }} }}
        header {{ border-bottom: 3px solid var(--accent); background: #000; padding: 20px; text-align:center; }}
        .brand {{ font-family: 'Oswald', sans-serif; font-size: 2rem; color: #fff; background: var(--accent); padding: 5px 20px; display:inline-block; }}
        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3rem; color: #fff; border-left: 5px solid var(--accent); padding-left: 20px; }}
        .alert-box {{ border: 1px solid var(--accent); color: var(--accent); padding: 10px; margin-bottom: 30px; text-align: center; font-weight: bold; }}
        .content {{ font-size: 1.1rem; color: #bbb; }}
        .featured-img {{ width: 100%; height: 400px; object-fit: cover; border-bottom: 3px solid var(--accent); }}
        .sidebar {{ position: sticky; top: 50px; }}
        .side-card {{ background: var(--card); border: 1px solid #333; padding: 20px; margin-bottom: 20px; }}
        .btn {{ display: block; padding: 15px; background: var(--accent); color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 10px; }}
        footer {{ border-top: 1px solid #333; padding: 60px; text-align: center; font-size: 0.8rem; color: #555; }}
    </style></head>
    <body>
    <header><div class="brand">PROJECT OMEGA</div></header>
    <div class="container">
        <main>
            <div class="alert-box">⚠️ CRITICAL ALERT: SYSTEM INSTABILITY</div>
            <h1>{topic}</h1>
            <img src="{img_url}" class="featured-img">
            <div style="background:#111; padding:15px; text-align:center; margin-bottom:30px;">
                <a href="{EMPIRE_URL}" style="color:#fff;">[CLASSIFIED] Get the Exit Plan >></a>
            </div>
            <div class="content">{body_html}</div>
        </main>
        <aside class="sidebar">
            <div class="side-card">
                <a href="{EMPIRE_URL}" class="btn">🛑 EMERGENCY INTEL</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT THE MARKET</a>
                <a href="{AMAZON_LINK}" class="btn">🪙 SECURE ASSETS</a>
            </div>
            <div class="side-card">
                <ul style="list-style:none; padding:0; font-size:0.85rem;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>&copy; 2026 PROJECT OMEGA | Amazon Disclaimer</footer></body></html>"""

def main():
    log("⚡ Unit 4 (Omega) Executing...")
    topic = random.choice(HOOKING_TITLES)
    p1 = generate_part(topic, "Trigger")
    p2 = generate_part(topic, "Impact")
    p3 = generate_part(topic, "Strategy")
    full_content = f"{p1}\n\n{p2}\n\n{p3}"
    if len(full_content) < 1000: full_content = FALLBACK_REPORT
    html_body = markdown.markdown(full_content)
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red alert stock market crash glitch art 8k')}"
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    sidebar_html = "".join([f"<li><span style='color:#ff003c;'>[!]</span> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#ccc;'>{h.get('title','Signal')}</a></li>" for h in history[:6]])
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(full_html)
    with open(os.path.join(BASE_DIR, archive_name), "w", encoding="utf-8") as f: f.write(full_html)
    generate_sitemap(history)
    log("✅ Omega Protocol Complete.")

if __name__ == "__main__": main()
