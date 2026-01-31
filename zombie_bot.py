import os, json, random, requests, markdown, urllib.parse, time, re, sys, io
from datetime import datetime

# [SYSTEM]
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration]
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
BLOG_TITLE = "PROJECT OMEGA"
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

# [🔥 4호기 전용 전문적 제목]
HOOKING_TITLES = [
    "2026 Global Liquidity Freeze Protocol",
    "National Debt Supercycle: The Final Stage",
    "Central Bank Digital Currency: Asset Lockout",
    "Systemic Banking Failure: Macro Analysis",
    "The 130% Debt-to-GDP Breaking Point"
]

# [🛡️ 4호기 전용 비상 원고] API 실패 시 "Data Decryption Failed" 대신 출력될 내용
LONG_EMERGENCY_REPORT = """
## [ACTION REQUIRED] STRATEGIC CRISIS REPORT: Systemic Risk 2026

**TOP SECRET // LEVEL 4 ACCESS.** This intelligence report outlines the terminal phase of the current debt supercycle. Indicators suggest an imminent liquidity freeze within the legacy banking sector.

### 1. Macro-Data Analysis
The global debt-to-GDP ratio has surpassed historical safety levels. Institutional 'smart money' is actively decoupling from fiat-denominated liabilities. 

### 2. Strategic Preservation Protocol
To maintain capital integrity, we recommend a mandatory shift toward non-custodial assets. Gold, silver, and Bitcoin represent the only viable exit ramps from the centralized lockout.

### 3. Required Actions
- Immediate migration to hardware-secured storage (Cold Wallets).
- Diversification into algorithmic wealth accumulation.
- Reduction of exposure to fractional reserve institutions.
"""

def generate_formal_report(topic):
    # 4호기 전용: 2개 섹션으로 나누어 분량 확보
    report_sections = ["Executive Summary and Global Risks", "Strategic Survival and Asset Protection"]
    full_report = f"# [TOP SECRET] OFFICIAL REPORT: {topic}\n\n"
    
    success_count = 0
    for section in report_sections:
        prompt = f"As a Senior Macro Analyst, write a 1000-word official report on '{topic}' focusing on '{section}'. Tone: Cold, Professional, Urgent. English Only. Markdown."
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.5}}, timeout=60)
            res = resp.json()['candidates'][0]['content']['parts'][0]['text'].strip()
            full_report += f"## {section}\n\n" + res + "\n\n---\n\n"
            success_count += 1
            time.sleep(5) # API 안정성 확보
        except:
            continue
            
    return full_report if success_count > 0 else LONG_EMERGENCY_REPORT

def create_final_html(topic, img_url, body_html, sidebar_html):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #fff; --text: #1a1a1a; --accent: #e60000; --sidebar-bg: #f9f9f9; }}
        body {{ font-family: 'Inter', sans-serif; line-height: 1.8; color: var(--text); background: var(--bg); margin: 0; overflow-x: hidden; }}
        header {{ border-bottom: 5px solid var(--accent); background: #fff; padding: 25px; text-align: center; position: sticky; top:0; z-index:100; }}
        .brand {{ font-family: 'Oswald', sans-serif; font-size: 2rem; color: var(--accent); letter-spacing: 2px; }}
        
        .container {{ max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 1fr 340px; gap: 50px; padding: 40px 20px; }}
        
        /* 모바일 최적화: 사이드바 밀어내기 */
        @media(max-width: 1100px) {{ 
            .container {{ grid-template-columns: 1fr; padding: 20px; }}
            .sidebar {{ position: static !important; border-top: 3px solid var(--accent); padding-top: 30px; }}
            h1 {{ font-size: 2.5rem !important; }}
        }}

        h1 {{ font-family: 'Oswald', sans-serif; font-size: 3.5rem; color: #000; margin-bottom: 30px; line-height: 1.1; }}
        .content h2 {{ color: var(--accent); border-bottom: 2px solid var(--accent); font-family: 'Oswald'; margin-top: 50px; }}
        img {{ width: 100%; height: 500px; object-fit: cover; border: 1px solid #ddd; margin-bottom: 40px; }}
        
        .sidebar {{ position: sticky; top: 120px; height: fit-content; }}
        .side-card {{ background: var(--sidebar-bg); border: 1px solid #ddd; padding: 25px; margin-bottom: 25px; border-top: 4px solid var(--accent); }}
        .btn {{ display: block; padding: 18px; background: #000; color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 12px; }}
        .btn-red {{ background: var(--accent); }}
        
        footer {{ border-top: 1px solid #ddd; padding: 60px; text-align: center; color: #777; background: #fafafa; }}
    </style></head>
    <body>
    <header><div class="brand">PROJECT OMEGA</div></header>
    <div class="container">
        <main>
            <div style="background:var(--accent); color:#fff; padding:5px 15px; display:inline-block; font-weight:bold; margin-bottom:20px;">TOP SECRET // LEVEL 4 REPORT</div>
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
                <ul style="list-style:none; padding:0; line-height:2.2; font-size:0.9rem;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>&copy; 2026 PROJECT OMEGA | STRATEGIC INTELLIGENCE</footer></body></html>"""

def main():
    log("⚡ Unit 4 Executing Recovery Protocol...")
    topic = random.choice(HOOKING_TITLES)
    full_text = generate_formal_report(topic)
    html_body = markdown.markdown(full_text)
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red danger alarm light minimalism 8k white background')}"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    sidebar_html = "".join([f"<li><b style='color:red;'>!</b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#333; text-decoration:none;'>{h.get('title','Report')}</a></li>" for h in history[:8]])
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    with open(archive_name, "w", encoding="utf-8") as f: f.write(full_html)
    log("✅ Omega Recovery Complete.")

if __name__ == "__main__": main()
