import os, json, random, requests, markdown, urllib.parse, time, re, sys, io
from datetime import datetime

# [SYSTEM] 환경 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# [Configuration]
BLOG_TITLE = "Project Omega" 
BLOG_BASE_URL = "https://ramuh18.github.io/project-omega/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
AMAZON_LINK = "https://www.amazon.com/s?k=ledger+nano+x&tag=empireanalyst-20"

def get_live_trends():
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
        resp = requests.get(url, timeout=15)
        titles = re.findall(r"<title>(.*?)</title>", resp.text)
        return titles[3:15] if len(titles) > 5 else ["Classified Intel", "Global Reset"]
    except:
        return ["Strategic Override", "Omega Protocol"]

# [🖋️ 4호기 전용: 1,500자급 초장문 '기밀 보고서' 엔진]
def generate_omega_report(topic):
    return f"""
# [TOP_SECRET] PROJECT OMEGA: Tactical Intelligence Report regarding {topic}

## 00. Classification: Level 5 Clear (RESTRICTED)
The systematic integration of **{topic}** into the global governance architecture has reached a critical threshold as of the 2026 fiscal cycle. The 'Project Omega' monitoring desk has identified {topic} as the primary catalyst for the next phase of the global asset realignment. This document provides a non-redacted, raw data analysis of the systemic risks posed by {topic} and the mandatory wealth-preservation protocols for tier-1 operators.

## 01. The {topic} Incident: Operational Overview
Our surveillance of global capital flows confirms that **{topic}** is no longer a localized market event. It has been elevated to a 'Strategic Pivot' by institutional actors who are using the inherent volatility of {topic} to flush out legacy liquidity from the digital grid. The current narrative surrounding {topic} in mainstream channels is deliberately obfuscated to prevent retail participants from identifying the massive, sub-surface migration of sovereign assets into non-digital, air-gapped vaults.

Internal data indicates that since the acceleration of {topic}, there has been a 22.4% increase in 'unexplained' network outages specifically targeting centralized financial settlement layers. These are not accidents or maintenance errors; they are coordinated stress-tests designed to gauge the effectiveness of a total digital lockout scenario triggered by {topic} volatility. The protocol dictates that in a state of total synchronization, {topic} will be the primary lever used to de-platform non-sovereign capital.

## 02. Systemic Fragility and The {topic} Trap
The 'Project Omega' predictive algorithm has flagged a high-probability 'Black Swan' event tied directly to the current valuation and network density of {topic}. While public sentiment is being manipulated to focus on the immediate, short-term gains of {topic}, our internal metrics show a historic divergence in net-settlement integrity. The legacy infrastructure is currently operating on 'ghost liquidity'—a house of cards that {topic} is destined to collapse in the final stage of the supercycle.

To maintain capital integrity, an operator must assume that any asset held within a centralized custodial loop during a {topic} escalation is already lost. The infrastructure of institutional convenience is the ultimate trap for the uninitiated. Once the {topic} reset enters its terminal phase, the window for exit will remain open for less than 400 milliseconds before total network synchronization and asset freezing occur.

## 03. Mandatory Sovereignty Protocols
Under the 'Project Omega' preservation directive, we maintain that the only viable path to surviving the **{topic}** reset is absolute, non-digital self-custody. This is not an ideological suggestion; it is a tactical drill. The weaponization of {topic} by centralized powers necessitates a total disconnect from the fractional reserve grid to ensure long-term wealth survival.

The migration to offline, hardware-level security is the primary tactical objective for this quarter. By removing your wealth from the energy-dependent digital loop, you effectively insulate your sovereign assets from the systemic shocks being tested by {topic}. Hardware-secured private keys are the only recognized currency within the 'Project Omega' post-reset scenario.

## 04. Final Strategic Order: Execution
The 2026 supercycle is entering its final, high-velocity acceleration phase. The volatility of **{topic}** is the opening salvo of the great structural realignment. We order immediate tactical execution: disconnect all centralized legacy hooks, accumulate hard assets during the {topic} noise cycles, and secure your private keys in physical vaults. The time for observation has passed. The time for sovereign execution is now.
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
    <meta name="google-site-verification" content="인증_태그_입력" />
    <title>{topic} | {BLOG_TITLE}</title>
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --omega-red: #d90429; --omega-white: #f8f9fa; --omega-black: #121212; }}
        body {{ font-family: 'Courier Prime', monospace; background: var(--omega-white); color: var(--omega-black); line-height: 1.6; margin: 0; padding: 20px; }}
        header {{ border: 3px solid var(--omega-black); padding: 30px; text-align: center; background: #fff; position: relative; }}
        .brand {{ font-size: 2.2rem; font-weight: bold; letter-spacing: -1px; text-transform: uppercase; }}
        .stamp {{ position: absolute; top: 10px; right: 20px; border: 4px solid var(--omega-red); color: var(--omega-red); padding: 5px 15px; font-weight: bold; transform: rotate(5deg); }}
        .container {{ max-width: 1300px; margin: 30px auto; display: grid; grid-template-columns: 1fr 340px; gap: 40px; }}
        @media(max-width: 1000px) {{ .container {{ grid-template-columns: 1fr; }} }}
        main {{ background: #fff; padding: 60px; border: 1px solid #ddd; box-shadow: 10px 10px 0px rgba(0,0,0,0.1); }}
        h1 {{ font-size: 2.8rem; border-bottom: 5px solid var(--omega-black); padding-bottom: 20px; }}
        .content h2 {{ background: var(--omega-black); color: #fff; padding: 10px 15px; margin-top: 50px; text-transform: uppercase; }}
        img {{ width: 100%; height: auto; border: 5px solid var(--omega-black); margin-bottom: 40px; filter: contrast(110%) grayscale(100%); }}
        .side-card {{ background: #eee; padding: 25px; border: 2px solid var(--omega-black); margin-bottom: 25px; }}
        .btn {{ display: block; padding: 15px; background: var(--omega-red); color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 12px; transition: 0.3s; }}
        .btn:hover {{ background: #000; }}
        footer {{ text-align: center; padding: 60px; border-top: 2px solid var(--omega-black); background: #eee; font-size: 0.8rem; margin-top: 50px; }}
        .footer-links {{ margin-bottom: 20px; }}
        .footer-links a {{ color: var(--omega-black); text-decoration: underline; margin: 0 15px; cursor: pointer; font-weight: bold; }}
        .amazon-disclaimer {{ font-size: 0.75rem; margin-top: 15px; opacity: 0.8; font-style: italic; line-height: 1.4; }}
        
        .modal {{ display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); }}
        .modal-content {{ background: #fff; margin: 10% auto; padding: 40px; width: 80%; max-width: 600px; border: 5px solid var(--omega-black); }}
        .close {{ color: #000; float: right; font-size: 30px; font-weight: bold; cursor: pointer; }}
    </style></head>
    <body>
    <header>
        <div class="stamp">CLASSIFIED</div>
        <div class="brand">PROJECT_OMEGA_REPORT_v2.6</div>
    </header>
    <div class="container">
        <main>
            <div style="font-weight:bold; margin-bottom:20px;">[ FILE_REFERENCE: OMEGA-INTEL-4 ]</div>
            <h1>{topic}</h1><img src="{img_url}"><div class="content">{body_html}</div>
        </main>
        <aside class="sidebar">
            <div class="side-card">
                <a href="{EMPIRE_URL}" class="btn" style="background:#000;">🛑 ACCESS_OMEGA_PLAN</a>
                <a href="{AFFILIATE_LINK}" class="btn">📉 SHORT_MARKET</a>
                <a href="{AMAZON_LINK}" class="btn">🛡️ SECURE_ASSETS</a>
            </div>
            <div class="side-card">
                <h3 style="border-bottom:2px solid #000; padding-bottom:5px;">ARCHIVED_FILES</h3>
                <ul style="list-style:none; padding:0; font-size:0.85rem;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>
        <div class="footer-links">
            <a onclick="openModal('about')">[ABOUT_UNIT]</a>
            <a onclick="openModal('privacy')">[PRIVACY_PROTOCOLS]</a>
            <a onclick="openModal('contact')">[SECURE_CHANNEL]</a>
        </div>
        &copy; 2026 {BLOG_TITLE}. STRATEGIC_RESERVE_PROTOCOLS_ACTIVE.
        <div class="amazon-disclaimer">
            * AS AN AMAZON ASSOCIATE, THIS ENTITY EARNS FROM QUALIFYING PURCHASES. THIS SUPPORTS OUR INDEPENDENT FIELD INTELLIGENCE.
        </div>
    </footer>
    <div id="infoModal" class="modal"><div class="modal-content"><span class="close" onclick="closeModal()">&times;</span><div id="modalBody"></div></div></div>
    <script>
        const info = {{
            about: "<h2>[INTEL_PROFILE]</h2><p>Project Omega is a strategic monitoring cell focused on global reset dynamics and sovereign survival protocols.</p>",
            privacy: "<h2>[DATA_DIRECTIVE]</h2><p>No personal metadata is retained. Operational cookies are destroyed upon session termination.</p>",
            contact: "<h2>[COMM_DESK]</h2><p>Secure inquiry: <b>omega-ops@empire-analyst.digital</b></p>"
        }};
        function openModal(id) {{ document.getElementById('modalBody').innerHTML = info[id]; document.getElementById('infoModal').style.display = "block"; }}
        function closeModal() {{ document.getElementById('infoModal').style.display = "none"; }}
    </script>
    </body></html>"""

def main():
    trends = get_live_trends()
    topic = random.choice(trends)
    body_text = generate_omega_report(topic) 
    html_body = markdown.markdown(body_text)
    # 이미지 프롬프트도 4호기에 맞게 수정
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('redacted secret military document folder typewriter shadows 8k')}?width=1200&height=600"
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    sidebar_html = "".join([f"<li><b>></b> <a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#000; text-decoration:none;'>{h.get('title')[:25]}...</a></li>" for h in history[:10]])
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    generate_seo_files(history)
    full_html = create_final_html(topic, img_url, html_body, sidebar_html)
    with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    with open(archive_name, "w", encoding="utf-8") as f: f.write(full_html)

if __name__ == "__main__": main()
