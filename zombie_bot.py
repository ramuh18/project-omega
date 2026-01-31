import os, json, random, requests, markdown, urllib.parse, time, re, sys, io
from datetime import datetime

# [SYSTEM]
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration]
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip() # 공백 자동 제거 추가
BLOG_TITLE = "PROJECT OMEGA"
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

# [Monetization]
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

# [HOOKING TITLES]
HOOKING_TITLES = [
    "RED ALERT: Dollar Collapse Timeline Leaked",
    "WARNING: 90% of Banks Face Failure",
    "The Great Reset: Protect Your Wealth",
    "Survival Mode: 5 Assets to Own",
    "Hyperinflation Is Here: Secure Your Future"
]

# [🔥 초강력 비상 원고] API 실패 시에도 이 내용이 출력되어 404나 에러를 방지합니다.
LONG_FALLBACK = """
## EMERGENCY PROTOCOL: The 2026 Financial System Reset

**CRITICAL TRANSMISSION.** The global financial architecture is undergoing a forced reset. As we enter the second quarter of 2026, the divergence between legacy equity markets and decentralized automated liquidity pools has reached a critical breaking point.

### 1. The Death of Human Latency
Institutional capital is now completely dominated by high-frequency execution bots. In this environment, human reaction time is a liability. Retail traders attempting to navigate this volatility without automated assistance are mathematically guaranteed to lose capital against sub-millisecond execution systems.

### 2. Digital Sovereignty and Cold Storage
With central bank digital currencies (CBDCs) encroaching on financial privacy, the migration of smart money to hardware-secured sovereignty is accelerating. The Ledger ecosystem and non-custodial wallets are becoming the only true safe havens. Our on-chain analysis reveals a massive outflow of Bitcoin from centralized exchanges into private cold storage.

### 3. Systematic Wealth Preservation
To maintain purchasing power in this new era, one must adopt a dual strategy: aggressive automated accumulation via algorithmic bots for income generation, and defensive fortification via cold storage for wealth preservation. This is not merely an investment suggestion; it is a survival protocol for the digital age.

### 4. The Final Warning
The debt supercycle is ending. Those who remain inside the legacy banking system will face unprecedented liquidity freezes. Secure your exit path now.
"""

def generate_full_report(topic):
    # 호출 횟수를 1회로 통합하여 API 제한(RPM) 우회
    prompt = f"Write an extremely detailed, 1500-word survival finance report on '{topic}'. Style: Urgent, Whistleblower. Use many bullet points. English Only. Markdown."
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2500}}, timeout=60)
        res_json = resp.json()
        if 'candidates' in res_json:
            return res_json['candidates'][0]['content']['parts'][0]['text'].strip()
        else:
            log(f"API Error Response: {res_json}")
            return LONG_FALLBACK
    except Exception as e:
        log(f"Connection Error: {e}")
        return LONG_FALLBACK

def create_final_html(topic, img_url, body_html, sidebar_html):
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
        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3rem; margin-bottom: 20px; color:#000; }}
        .content img {{ width: 100%; height: 450px; object-fit: cover; margin-bottom: 30px; border: 1px solid #ddd; }}
        .sidebar {{ position: sticky; top: 20px; height: fit-content; }}
        .side-card {{ background: var(--sidebar); border-top: 4px solid var(--accent); padding: 20px; margin-bottom: 20px; }}
        .btn {{ display: block; padding: 15px; background: #000; color: #fff; text-decoration: none; text-align: center; font-weight: bold; margin-bottom: 10px; font-size: 0.9rem; }}
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
                <div style="font-weight:bold; margin-bottom:10px;">RECENT SIGNALS</div>
                <ul style="list-style:none; padding:0; font-size:0.85rem; line-height:2;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>&copy; 2026 PROJECT OMEGA | END-GAME INTEL</footer></body></html>"""

def main():
    log("⚡ Unit 4 Executing (Stability Version)...")
    topic = random.choice(HOOKING_TITLES)
    
    # 통합된 1회 호출 로직
    full_text = generate_full_report(topic)
    html_body = markdown.markdown(full_text)
    
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red emergency alarm minimalist white background 8k')}"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    sidebar_html = "".join([f"<li><b style='color:red;'>!</b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#333; text-decoration:none;'>{h.get('title','Log')}</a></li>" for h in history[:8]])
    
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(full_html)
    with open(os.path.join(BASE_DIR, archive_name), "w", encoding="utf-8") as f: f.write(full_html)
    
    log("✅ Omega Complete.")

if __name__ == "__main__": main()
