import os, json, random, requests, markdown, urllib.parse, time, re, sys, io
from datetime import datetime

# [SYSTEM] 환경 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg): print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# [Configuration] ★4호기 전용 설정★
BLOG_TITLE = "Project Omega" 
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

# [📊 구글 트렌드 실시간 수집]
def get_live_trends():
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
        resp = requests.get(url, timeout=15)
        titles = re.findall(r"<title>(.*?)</title>", resp.text)
        return titles[3:15] if len(titles) > 5 else ["National Debt", "Currency Reset"]
    except:
        return ["Emergency Liquidity", "Sovereign Asset Protocol"]

# [🖋️ 4호기 전용 1,500자급 '기밀 보고서' 엔진]
def generate_omega_report(topic):
    return f"""
# [TOP SECRET] STRATEGIC CRISIS REPORT: {topic} RISK LEVEL 4

**MEMORANDUM FOR LEVEL 4 CLEARANCE HOLDERS ONLY**

## 1. EXECUTIVE OVERVIEW: THE {topic} ANOMALY
The current trajectory of **{topic}** has bypassed all standard macro-economic safety buffers. Intelligence gathered from the legacy banking core indicates a terminal phase shift triggered by {topic} volatility. This report outlines the mandatory preservation protocols required to mitigate systemic capital erasure during the 2026 supercycle transition.

## 2. SYSTEMIC FRAGILITY AND {topic} CORRELATION
Our quantitative models show a direct correlation between the surge in {topic} and the imminent liquidity freeze within fractional reserve institutions. The global debt supercycle has reached a breaking point where {topic} is no longer a transitory indicator but a systemic weapon.

Institutional capital is actively decoupling from fiat liabilities under the cover of {topic} market noise. We have identified a 'Kill Switch' protocol embedded in upcoming CBDC architectures that utilizes {topic} volatility as a justification for asset lockout. Retail participants who remain within the centralized perimeter are at 94% risk of total capital restriction.

## 3. MANDATORY PRESERVATION PROTOCOL
To maintain asset integrity during the **{topic}** escalation, the following actions are classified as mandatory:
- **Immediate Disconnect**: All liquid capital must be removed from commercial banking nodes.
- **Hardware Integration**: Migration to non-custodial, hardware-secured vaults is the only recognized exit ramp.
- **Algorithmic Sovereignty**: Transition toward automated wealth preservation strategies to counter institutional front-running.

## FINAL STRATEGIC CONCLUSION
The window for sovereign execution is closing. The data from **{topic}** serves as the final warning before the systematic asset lockout. Do not wait for public confirmation; by the time the broadcast is issued, the exit ramps will be closed. Sovereignty is your only protection against the terminal reset.
"""

def create_final_html(topic, img_url, body_html, sidebar_html):
    # [4호기 테마] 화이트 배경, 레드 포인트 (정부 기밀 문서 느낌)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic} | {BLOG_TITLE}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --omega-red: #e60000; --omega-gray: #333; }}
        body {{ font-family: 'Courier Prime', monospace; background: #fff; color: #1a1a1a; line-height: 1.6; margin: 0; }}
        
        header {{ background: #fff; color: var(--omega-red); padding: 40px; text-align: center; border-bottom: 10px solid var(--omega-red); }}
        .brand {{ font-family: 'Oswald', sans-serif; font-size: 3rem; letter-spacing: 5px; text-transform: uppercase; }}
        
        .container {{ max-width: 1300px; margin: 50px auto; display: grid; grid-template-columns: 1fr 350px; gap: 50px; padding: 0 20px; }}
        @media(max-width: 1100px) {{ .container {{ grid-template-columns: 1fr; }} .sidebar {{ position: static; }} }}
        
        main {{ background: #fff; padding: 50px; border: 2px solid #000; position: relative; }}
        main::before {{ content: 'TOP SECRET'; position: absolute; top: 10px; right: 20px; color: rgba(230,0,0,0.2); font-size: 5rem; transform: rotate(-15deg); font-weight: bold; pointer-events: none; }}
        
        h1 {{ font-family: 'Oswald', sans-serif; color: #000; font-size: 3.5rem; line-height: 1.1; margin-top: 0; border-bottom: 5px solid #000; padding-bottom: 20px; }}
        .content h2 {{ color: var(--omega-red); font-family: 'Oswald'; margin-top: 50px; border-bottom: 2px solid #000; }}
        img {{ width: 100%; height: auto; border: 2px solid #000; margin-bottom: 40px; filter: contrast(1.5) grayscale(1); }}
        
        .side-card {{ background: #fff; padding: 30px; border: 2px solid #000; margin-bottom: 25px; border-top: 10px solid var(--omega-red); }}
        .btn {{ display: block; padding: 20px; background: #000; color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 15px; font-family: 'Oswald'; font-size: 1.2rem; }}
        .btn-red {{ background: var(--omega-red); }}
        .btn:hover {{ background: #fff; color: #000; border: 2px solid #000; }}
        
        footer {{ text-align: center; padding: 100px 20px; color: #000; font-family: 'Courier Prime', monospace; border-top: 5px solid #000; margin-top: 80px; }}
        .amazon-disclaimer {{ margin-top: 20px; font-size: 0.8rem; font-style: italic; opacity: 0.7; }}
    </style></head>
    <body>
    <header><div class="brand">PROJECT_OMEGA_PROTOCOL</div></header>
    <div class="container">
        <main>
            <div style="background:var(--omega-red); color:#fff; padding:5px 15px; display:inline-block; font-weight:bold; margin-bottom:20px;">SECURITY CLEARANCE: LEVEL 4 REQUIRED</div>
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
                <h3 style="margin-top:0; color:#000; font-family:'Oswald'; border-bottom:3px solid var(--omega-red);">ARCHIVED INTEL</h3>
                <ul style="list-style:none; padding:0; line-height:2.5; font-size:1rem;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>
        COPYRIGHT &copy; 2026 {BLOG_TITLE}. STRATEGIC INTELLIGENCE UNIT.
        <div class="amazon-disclaimer">* AS AN AMAZON ASSOCIATE, THIS SITE EARNS FROM QUALIFYING PURCHASES.</div>
    </footer></body></html>"""

def main():
    trends = get_live_trends()
    topic = random.choice(trends)
    body_text = generate_omega_report(topic) 
    html_body = markdown.markdown(body_text)
    # 이미지 스타일: 흑백, 고대비, 경고 느낌
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('red danger alarm light minimalism black and white high contrast 8k')}?width=1200&height=600"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    sidebar_html = "".join([f"<li><b style='color:red;'>!</b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#000; text-decoration:none;'>{h.get('title')[:25]}...</a></li>" for h in history[:10]])
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    with open(archive_name, "w", encoding="utf-8") as f: f.write(full_html)
    log(f"✅ 4호기 Omega Update Complete: {topic}")

if __name__ == "__main__": main()
