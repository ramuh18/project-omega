import os, json, random, requests, markdown, urllib.parse, feedparser, time, re, sys, io
from datetime import datetime

# [SYSTEM]
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration] 4호기: PROJECT OMEGA (화이트 & 레드)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
BLOG_TITLE = "PROJECT OMEGA"
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

# [Monetization]
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

# [🔥 HOOKING TITLES]
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

def generate_part(topic, focus):
    # 분량 확보를 위해 프롬프트 강화: 800단어 이상 요구
    prompt = f"Write an extremely detailed, 800-word deep-dive intelligence report on '{topic}'. Focus specifically on '{focus}'. Style: Professional whistleblower, urgent, survivalist. Use technical data, bullet points, and dark financial metaphors. English Only. Markdown format."
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2048}}, timeout=40)
        res = resp.json()['candidates'][0]['content']['parts'][0]['text']
        return res.strip()
    except: return ""

def create_final_html(topic, img_url, body_html, sidebar_html):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* [THEME] 화이트 바탕 & 레드 포인트 */
        :root {{ --bg: #ffffff; --text: #1a1a1a; --accent: #e60000; --sidebar-bg: #f8f8f8; --border: #dddddd; }}
        body {{ font-family: 'Inter', sans-serif; line-height: 1.8; color: var(--text); background: var(--bg); margin: 0; }}
        
        .container {{ max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 1fr 340px; gap: 60px; padding: 60px 20px; }}
        @media(max-width: 1100px) {{ .container {{ grid-template-columns: 1fr; }} }}
        
        header {{ border-bottom: 5px solid var(--accent); background: #ffffff; padding: 25px; text-align:center; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        .brand {{ font-family: 'Oswald', sans-serif; font-size: 2.2rem; color: var(--accent); letter-spacing: 3px; font-weight: 700; }}
        
        main {{ background: #fff; }}
        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3.5rem; color: #000; margin-bottom: 30px; line-height: 1.1; text-transform: uppercase; font-weight: 700; }}
        .alert-tag {{ background: var(--accent); color: #fff; padding: 5px 15px; font-weight: bold; font-size: 0.9rem; margin-bottom: 20px; display: inline-block; }}
        
        .content {{ font-size: 1.2rem; color: #333; }}
        .content h2 {{ color: var(--accent); border-bottom: 3px solid var(--accent); display: inline-block; margin-top: 60px; font-family: 'Oswald', sans-serif; font-size: 2rem; }}
        .content p {{ margin-bottom: 25px; }}
        
        .featured-img {{ width: 100%; height: 500px; object-fit: cover; border: 1px solid var(--border); margin-bottom: 40px; filter: grayscale(20%); }}
        
        /* 사이드바 */
        .sidebar {{ position: sticky; top: 120px; height: fit-content; }}
        .side-card {{ background: var(--sidebar-bg); border: 1px solid var(--border); padding: 25px; margin-bottom: 25px; border-top: 4px solid var(--accent); }}
        .side-title {{ font-family: 'Oswald', sans-serif; font-size: 1.3rem; margin-bottom: 20px; color: #000; }}
        
        .btn {{ display: block; padding: 18px; background: #000; color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 12px; transition: 0.3s; font-size: 0.9rem; }}
        .btn:hover {{ background: var(--accent); }}
        .btn-red {{ background: var(--accent); }}
        .btn-red:hover {{ background: #000; }}
        
        footer {{ border-top: 1px solid var(--border); padding: 80px 20px; text-align: center; font-size: 0.9rem; color: #777; background: #fafafa; }}
    </style></head>
    <body>
    <header><div class="brand">PROJECT OMEGA</div></header>
    <div class="container">
        <main>
            <div class="alert-tag">TOP SECRET // EMERGENCY BROADCAST</div>
            <h1>{topic}</h1>
            <img src="{img_url}" class="featured-img">
            <div class="content">{body_html}</div>
        </main>
        <aside class="sidebar">
            <div class="side-card">
                <div class="side-title">ACTION PROTOCOL</div>
                <a href="{EMPIRE_URL}" class="btn btn-red">🛑 DOWNLOAD EXIT PLAN</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT SYSTEM</a>
                <a href="{AMAZON_LINK}" class="btn">🪙 SECURE ASSETS</a>
            </div>
            <div class="side-card">
                <div class="side-title">LATEST ALERTS</div>
                <ul style="list-style:none; padding:0; font-size:0.9rem; line-height:2;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>&copy; 2026 PROJECT OMEGA | END-GAME INTELLIGENCE<br>Amazon Associate Disclaimer included.</footer></body></html>"""

def main():
    log("⚡ Unit 4 (Omega) V2.0 Executing...")
    topic = random.choice(HOOKING_TITLES)
    
    # 2개 파트로 나누어 생성 (총 1,600단어 타겟)
    p1 = generate_part(topic, "The Unfolding Collapse and Macro Data")
    p2 = generate_part(topic, "Strategic Wealth Preservation and Survival")
    full_content = f"{p1}\n\n{p2}"
    
    # 분량 체크 후 너무 짧으면 보충
    if len(full_content) < 2000:
        log("⚠️ Content a bit short, adding supplementary analysis...")
        p3 = generate_part(topic, "Specific Actionable Steps for 2026")
        full_content += f"\n\n{p3}"
    
    html_body = markdown.markdown(full_content)
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red alarm siren emergency light white background minimalism 8k')}"
    
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
    
    generate_sitemap(history)
    log("✅ Omega Protocol V2.0 Complete.")

if __name__ == "__main__": main()
