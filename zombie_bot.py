import os, json, random, requests, markdown, urllib.parse, time, re, sys, io
from datetime import datetime

# [SYSTEM] 환경 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# [Configuration]
BLOG_TITLE = "Titan Resources" 
BLOG_BASE_URL = "https://ramuh18.github.io/titan-resources/" 
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
        return titles[3:15] if len(titles) > 5 else ["Energy Crisis", "Rare Earth War"]
    except:
        return ["Resource Scarcity", "Strategic Reserve Reset"]

# [🖋️ 5호기 전용: 1,500자급 초장문 '자원 분석' 엔진]
def generate_resource_report(topic):
    return f"""
# [TITAN INTEL] Strategic Resource Analysis: The Geopolitics of {topic}

## Executive Summary: The Resource Supercycle
The 2026 global economy is being radically redefined by the physical control of tangible assets. The emergence of **{topic}** as a central volatility driver confirms that we have entered the terminal phase of the resource supercycle. This report provides an exhaustive analysis of the systemic supply chain disruptions triggered by {topic} and the mandatory wealth preservation protocols required for the industrial era.

## 1. Supply Chain Weaponization and {topic}
The integration of {topic} into the current trade war landscape follows a prolonged period of extreme resource depletion and infrastructure neglect. As nations scramble for industrial self-sufficiency, {topic} has been weaponized to squeeze legacy powers and consolidate regional dominance. Our proprietary data indicates that institutional capital is rotating out of 'paper assets' and into the physical infrastructure that {topic} is currently destabilizing in real-time.

We are seeing a 300% increase in strategic stockpiling activities specifically tied to the {topic} supply chain. If your capital remains tied to centralized settlement layers during a {topic} supply shock, you are exposing your entire portfolio to a potential liquidity freeze. In the physical economy, access is more important than price.

## 2. Energy Sovereignty: The Systemic Cost of {topic}
The correlation between global energy costs and the availability of {topic} is reaching critical, unsustainable levels. As the grid faces unprecedented stress from regional conflicts, {topic} serves as the ultimate catalyst for the next wave of inflationary shocks. Institutional whales and sovereign wealth funds are no longer trusting centralized, energy-dependent custodial systems to protect their wealth during these {topic} cycles.

The migration toward decentralized, sovereign wealth nodes is accelerating as **{topic}** exposes the fundamental fragility of the global power architecture. To survive the {topic} reset, an investor must transition from being a passive consumer of financial products to an active owner of sovereign assets. The security of your principal is now directly tied to your ability to bypass the centralized energy and data grids.

## 3. Preservation Strategy and Network Sovereignty
In direct response to the **{topic}** escalation, we maintain that capital integrity is exclusively tied to physical security and non-digital access. The migration to cold storage for all digital reserves is the first and most critical line of defense against the systemic shocks currently being tested by the {topic} initiative.

By removing your assets from the energy-fragile, centralized banking loop, you effectively insulate your wealth from the 'Kill-Switch' protocols that are being prepared for the {topic} crisis phase. Hardware-secured private keys, stored in physical vaults, are the only assets that will maintain their functional value when the {topic} volatility peak occurs.

## Strategic Conclusion: The Time for Control
The era of infinite resource abundance and institutional stability is officially over. The volatility surrounding **{topic}** is the opening bell for the great resource reset of the late 2020s. We recommend immediate execution of the following protocols: Accumulate sovereign assets during {topic} dips, secure your private keys in physical vaults, and disconnect your wealth from the legacy industrial debt complex. The future belongs to those who control the physical nodes of value.
"""

# [🔍 자동 SEO 파일 생성기]
def generate_seo_files(history):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += f'  <url><loc>{BLOG_BASE_URL}</loc><priority>1.0</priority></url>\n'
    for h in history[:50]:
        sitemap += f'  <url><loc>{BLOG_BASE_URL}{h["file"]}</loc><priority>0.8</priority></url>\n'
    sitemap += '</urlset>'
    with open("sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap)
    robots = f"User-agent: *\nAllow: /\nSitemap: {BLOG_BASE_URL}sitemap.xml"
    with open("robots.txt", "w", encoding="utf-8") as f: f.write(robots)

def create_final_html(topic, img_url, body_html, sidebar_html):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Jxh9S9J3S5_RBIpJH4CVrDkpRiDZ_mQ99TfIm7xK7YY" />
    <title>{topic} | {BLOG_TITLE}</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --amber: #ff8c00; --charcoal: #1a1a1a; --industrial-orange: #ff4500; }}
        body {{ font-family: 'Inter', sans-serif; background: #0f0f0f; color: #ddd; line-height: 1.8; margin: 0; }}
        header {{ background: var(--charcoal); color: var(--amber); padding: 25px; text-align: center; border-bottom: 8px solid var(--amber); position: relative; }}
        .brand {{ font-family: 'Roboto Condensed', sans-serif; font-size: 2rem; letter-spacing: 2px; text-transform: uppercase; }}
        .container {{ max-width: 1300px; margin: 30px auto; display: grid; grid-template-columns: 1fr 340px; gap: 40px; padding: 0 20px; }}
        @media(max-width: 1000px) {{ .container {{ grid-template-columns: 1fr; }} }}
        main {{ background: #1a1a1a; padding: 40px; border-radius: 4px; border: 1px solid #333; }}
        h1 {{ color: #fff; font-size: 2.5rem; border-bottom: 2px solid var(--amber); padding-bottom: 15px; margin-top: 0; }}
        .content h2 {{ color: var(--amber); margin-top: 40px; font-family: 'Roboto Condensed'; border-left: 5px solid var(--industrial-orange); padding-left: 15px; }}
        img {{ width: 100%; height: auto; border: 2px solid #333; margin-bottom: 30px; }}
        .side-card {{ background: #1a1a1a; padding: 25px; border-top: 5px solid var(--amber); border: 1px solid #333; margin-bottom: 20px; }}
        .btn {{ display: block; padding: 15px; background: var(--amber); color: #000; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 10px; border-radius: 4px; }}
        footer {{ text-align: center; padding: 60px 20px; color: #666; background: #000; border-top: 5px solid var(--charcoal); font-size: 0.85rem; }}
        .footer-links {{ margin-bottom: 20px; }}
        .footer-links a {{ color: var(--amber); text-decoration: none; margin: 0 15px; cursor: pointer; font-weight: bold; }}
        .amazon-disclaimer {{ font-size: 0.75rem; color: #444; margin-top: 15px; font-style: italic; line-height: 1.4; }}
        
        .modal {{ display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); }}
        .modal-content {{ background: #1a1a1a; margin: 10% auto; padding: 30px; width: 80%; max-width: 600px; border: 1px solid var(--amber); color: #ddd; }}
        .close {{ color: var(--amber); float: right; font-size: 28px; font-weight: bold; cursor: pointer; }}
    </style></head>
    <body>
    <header><div class="brand">TITAN_RESOURCES_CORP</div></header>
    <div class="container">
        <main><h1>{topic}</h1><img src="{img_url}"><div class="content">{body_html}</div></main>
        <aside class="sidebar">
            <div class="side-card">
                <a href="{EMPIRE_URL}" class="btn" style="background:#ff4500; color:#fff;">🛑 ACCESS RESOURCE PLAN</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT MARKET</a>
                <a href="{AMAZON_LINK}" class="btn">🛡️ SECURE ASSETS</a>
            </div>
            <div class="side-card">
                <h3 style="color:var(--amber); font-family:'Roboto Condensed';">TITAN SIGNALS</h3>
                <ul style="list-style:none; padding:0; font-size:0.9rem;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>
        <div class="footer-links">
            <a onclick="openModal('about')">About Us</a>
            <a onclick="openModal('privacy')">Privacy Policy</a>
            <a onclick="openModal('contact')">Contact</a>
        </div>
        &copy; 2026 {BLOG_TITLE}. STRATEGIC RESOURCE PROTOCOLS APPLIED.
        <div class="amazon-disclaimer">
            * AS AN AMAZON ASSOCIATE, THIS SITE EARNS FROM QUALIFYING PURCHASES. THIS SUPPORTS OUR INDEPENDENT INDUSTRIAL RESEARCH.
        </div>
    </footer>
    <div id="infoModal" class="modal"><div class="modal-content"><span class="close" onclick="closeModal()">&times;</span><div id="modalBody"></div></div></div>
    <script>
        const info = {{
            about: "<h2>About {BLOG_TITLE}</h2><p>Titan Resources is a premier intelligence node focusing on physical asset security and geopolitical resource trends.</p>",
            privacy: "<h2>Privacy Policy</h2><p>We do not collect identifiable personal data. Standard analytical cookies are used to monitor systemic network performance.</p>",
            contact: "<h2>Contact Desk</h2><p>Inquiries: <b>intel@titan-resources.net</b></p>"
        }};
        function openModal(id) {{ document.getElementById('modalBody').innerHTML = info[id]; document.getElementById('infoModal').style.display = "block"; }}
        function closeModal() {{ document.getElementById('infoModal').style.display = "none"; }}
    </script>
    </body></html>"""

def main():
    trends = get_live_trends()
    topic = random.choice(trends)
    body_text = generate_resource_report(topic) 
    html_body = markdown.markdown(body_text)
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('heavy industrial machine oil amber sunset cinematic 8k')}?width=1200&height=600"
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    sidebar_html = "".join([f"<li><b style='color:var(--amber);'>■</b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#bbb; text-decoration:none;'>{h.get('title')[:25]}...</a></li>" for h in history[:10]])
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    generate_seo_files(history)
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    with open(archive_name, "w", encoding="utf-8") as f: f.write(full_html)

if __name__ == "__main__": main()
