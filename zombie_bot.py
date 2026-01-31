import os, json, random, requests, markdown, urllib.parse, feedparser, time, re, sys, io
from datetime import datetime

# [SYSTEM]
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration] 4호기: PROJECT OMEGA (레드/생존 테마)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
BLOG_TITLE = "PROJECT OMEGA"
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

# [Monetization] 생존/대비 컨셉
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

# [🔥 HOOKING TITLES] 경제 붕괴/위기/경고 (영어, 8단어 미만)
HOOKING_TITLES = [
    "RED ALERT: The Dollar Collapse Timeline Revealed",
    "WARNING: 90% of Banks Will Fail by 2026",
    "The Great Reset: Own Nothing and Be Happy?",
    "Survival Mode: 5 Assets You Must Own NOW",
    "Hyperinflation Is Here: Protect Your Wealth",
    "The Secret 'Order 66' Protocol in Finance",
    "Urgent: Sell Your Fake Assets Before It's Too Late",
    "Black Swan Event: AI Predicts Total Grid Down",
    "The Elite's Escape Plan: Where They Are Hiding",
    "Final Warning: The Debt Bubble Has Burst"
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

# [FALLBACK] 비상용 원고 (붕괴 시나리오, 영어)
FALLBACK_REPORT = """
## DEFCON 1: The Financial System Is Resetting

**Critical Transmission.** The indicators we monitor are flashing red. The global debt supercycle has reached its mathematical limit. This is not a recession; it is a total structural collapse of the fiat currency system.

### 1. The Currency Debasement Event
Central banks are trapping liquidity. Your purchasing power is being eroded at an algorithmic rate. History shows that when debt-to-GDP ratios cross 130%, currency failure is inevitable. We are past that point. The only exit strategy is hard assets that cannot be printed.

### 2. The Great Wealth Transfer
While the masses are distracted, institutional elites are quietly moving capital into sovereign-grade assets: Gold, Bitcoin, and Land. The 'Project Omega' indicators suggest a massive liquidity freeze is imminent. If your assets are in a bank, they are not yours. They are unsecured loans to a bankrupt entity.

### 3. Survival Protocol
Immediate action is required. 
1. Secure a hardware wallet for digital assets.
2. Establish positions in algorithmic trading to compound remaining fiat.
3. Prepare for the digital lockout.

**Time is running out.**
"""

def generate_part(topic, focus):
    # 프롬프트: 종말론적, 생존주의, 긴박함 (English Only)
    prompt = f"Write a terrifying, urgent 600-word survival finance report on '{topic}'. Focus: {focus}. Tone: Apocalyptic, 'Prepper', Warning, Dark. Use short sentences. Reveal the harsh truth. Markdown. **English Only.**"
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.6}}, timeout=30)
        res = resp.json()['candidates'][0]['content']['parts'][0]['text']
        return re.sub(r'\{"role":.*?"content":', '', res, flags=re.DOTALL).replace('"}', '').strip()
    except: return ""

def create_final_html(topic, img_url, body_html, sidebar_html):
    # [핵심] 서치콘솔 태그가 삽입된 헤더
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* [THEME] 레드 & 블랙 (공포/경고) */
        :root {{ --bg: #000000; --text: #cccccc; --accent: #ff003c; --card: #111; }}
        body {{ font-family: 'Roboto Mono', monospace; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }}
        
        /* [LAYOUT] 오른쪽 사이드바 (320px) */
        .container {{ max-width: 1500px; margin: 0 auto; display: grid; grid-template-columns: 1fr 320px; gap: 40px; padding: 40px 20px; }}
        @media(max-width: 1000px) {{ .container {{ grid-template-columns: 1fr; }} }}
        
        /* 헤더: 경고 테이프 스타일 */
        header {{ border-bottom: 3px solid var(--accent); background: repeating-linear-gradient(45deg, #000, #000 10px, #111 10px, #111 20px); padding: 20px 40px; text-align:center; }}
        .brand {{ font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 2rem; color: #fff; text-transform: uppercase; letter-spacing: 5px; background: var(--accent); padding: 5px 20px; display:inline-block; }}
        
        /* 본문 */
        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3rem; color: #fff; margin-bottom: 20px; text-transform: uppercase; line-height: 1.1; border-left: 5px solid var(--accent); padding-left: 20px; }}
        .alert-box {{ border: 1px solid var(--accent); color: var(--accent); padding: 10px; margin-bottom: 30px; text-align: center; font-weight: bold; animation: pulse 2s infinite; }}
        
        .content {{ font-size: 1.1rem; text-align: justify; color: #bbb; }}
        .content h2 {{ color: #fff; border-bottom: 2px solid #333; padding-bottom: 10px; margin-top: 50px; font-family: 'Oswald', sans-serif; font-size: 1.8rem; text-transform: uppercase; }}
        .content strong {{ color: #fff; background: #330000; padding: 0 5px; }}
        
        /* 이미지 */
        .featured-img {{ width: 100%; height: 400px; object-fit: cover; filter: grayscale(100%) contrast(1.5); border-bottom: 3px solid var(--accent); }}
        
        /* 사이드바: 카드 뉴스 스타일 */
        .sidebar {{ position: sticky; top: 50px; height: fit-content; }}
        .side-card {{ background: var(--card); border: 1px solid #333; padding: 20px; margin-bottom: 20px; }}
        .side-title {{ color: #fff; font-family: 'Oswald', sans-serif; font-size: 1.2rem; margin-bottom: 15px; border-left: 3px solid var(--accent); padding-left: 10px; }}
        
        /* 버튼: 비상 버튼 스타일 */
        .btn {{ display: block; padding: 15px; background: var(--accent); color: #fff; text-decoration: none; font-weight: bold; text-align: center; text-transform: uppercase; margin-bottom: 10px; transition: 0.3s; }}
        .btn:hover {{ background: #fff; color: #000; }}
        
        footer {{ border-top: 1px solid #333; padding: 60px; text-align: center; font-size: 0.8rem; color: #555; margin-top: 100px; }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} 100% {{ opacity: 1; }} }}
    </style></head>
    <body>
    <header>
        <div class="brand">PROJECT OMEGA</div>
    </header>
    <div class="container">
        <main>
            <div class="alert-box">⚠️ CRITICAL ALERT: SYSTEM INSTABILITY DETECTED</div>
            <h1>{topic}</h1>
            <div style="margin-bottom:30px;">
                <img src="{img_url}" class="featured-img">
            </div>
            <div style="background:#111; padding:15px; text-align:center; font-size:0.9rem; margin-bottom:30px; border-bottom:1px solid #333;">
                <span style="color:var(--accent);">[CLASSIFIED]</span> The collapse is accelerating. 
                <a href="{EMPIRE_URL}" style="color:#fff; text-decoration:underline;">See the Exit Plan >></a>
            </div>
            <div class="content">{body_html}</div>
        </main>
        
        <aside class="sidebar">
            <div class="side-card">
                <div class="side-title">SURVIVAL TOOLS</div>
                <a href="{EMPIRE_URL}" class="btn">🛑 EMERGENCY INTEL</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT THE MARKET</a>
                <a href="{AMAZON_LINK}" class="btn">🪙 SECURE GOLD/CRYPTO</a>
            </div>
            
            <div class="side-card">
                <div class="side-title">RECENT SIGNALS</div>
                <ul style="list-style:none; padding:0; font-size:0.85rem; line-height:1.8;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>
        <div>PROJECT OMEGA | END GAME SCENARIOS</div>
        <div>Amazon Disclaimer: As an Amazon Associate, I earn from qualifying purchases.</div>
    </footer></body></html>"""

def main():
    log("⚡ Unit 4 (Omega) Initializing...")
    topic = random.choice(HOOKING_TITLES)
    log(f"Topic: {topic}")
    
    p1 = generate_part(topic, "The Trigger Event")
    p2 = generate_part(topic, "Impact on Society")
    p3 = generate_part(topic, "Survival Strategy")
    full_content = f"{p1}\n\n{p2}\n\n{p3}"
    
    if len(full_content) < 1000: 
        log("⚠️ Content short. Using Fallback.")
        full_content = FALLBACK_REPORT
    
    html_body = markdown.markdown(full_content)
    # 이미지: 붉은색, 공포, 경고
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red alert stock market crash glitch art high contrast 8k')}"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    # 사이드바 리스트 스타일 (빨간색 경고)
    sidebar_html = "".join([f"<li><span style='color:#ff003c;'>[ALERT]</span> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#ccc; text-decoration:none;'>{h.get('title','Signal')}</a></li>" for h in history[:6]])
    
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(full_html)
    with open(os.path.join(BASE_DIR, archive_name), "w", encoding="utf-8") as f: f.write(full_html)
    
    generate_sitemap(history)
    log("✅ Omega Protocol Executed.")

if __name__ == "__main__": main()
