import os, json, random, requests, markdown, urllib.parse, time, re, sys, io, textwrap
from datetime import datetime

# [SYSTEM] 환경 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# [Configuration] 4호기 설정 (크립토/미래기술)
BLOG_TITLE = "Digital Alpha" 
BLOG_BASE_URL = "https://ramuh18.github.io/digital-alpha/" 
EMPIRE_URL = "https://empire-analyst.digital/"
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")
AFFILIATE_LINK = "https://www.bybit.com/invite?ref=DOVWK5A" 
# 아마존 링크는 스마트 매칭 자동 생성

# [주제 리스트 50개: 크립토/Web3/AI]
BACKUP_TOPICS = [
    "Bitcoin Halving Cycles Explained", "Ethereum Layer 2 Scaling Wars", "Solana vs Ethereum Analysis",
    "DeFi Yield Farming Risks", "NFT Market Trends 2026", "Metaverse Real Estate Boom",
    "Artificial Intelligence in Crypto", "Web3 Gaming Tokenomics", "Centralized vs Decentralized Exchanges",
    "Crypto Regulation Outlook", "Institutional Bitcoin Adoption", "The Future of Stablecoins",
    "Privacy Coins Under Attack", "DAO Governance Models", "Tokenization of Real World Assets",
    "Cross-Chain Bridge Security", "Zero-Knowledge Rollups (ZK)", "Liquid Staking Derivatives",
    "Meme Coin Psychology", "Crypto Portfolio Allocation", "Bitcoin ETF Impact",
    "Self-Custody Best Practices", "Smart Contract Auditing", "The Flippening: ETH vs BTC",
    "Altcoin Season Indicators", "Crypto Tax Loopholes", "Algorithmic Stablecoin Failures",
    "Generative AI and Blockchain", "Decentralized Identity (DID)", "Supply Chain on Blockchain",
    "Carbon Credits on Chain", "Crypto Mining Profitability", "Proof of Stake vs Work",
    "Lightning Network Adoption", "Crypto Debit Cards Review", "SocialFi and Creator Economy",
    "Music NFTs Revolution", "Decentralized Storage Solutions", "Oracle Networks Importance",
    "Crypto Hacking Post-Mortems", "Wash Trading Detection", "On-Chain Analysis Basics",
    "Whale Wallet Tracking", "Crypto Market Cycles", "Dollar Cost Averaging Crypto",
    "Stop Loss Strategies for Alts", "Leverage Trading Dangers", "Crypto Scams to Avoid",
    "The Future of Digital Wallets", "Blockchain Scalability Trilemma"
]

# [문단 블록 15개: 기술/혁신/변동성]
CONTENT_BLOCKS = [
    """
    ## The Digital Paradigm Shift
    The world is moving from analog to digital value transfer, and **{topic}** is at the forefront of this revolution. We are witnessing the 'financialization of everything.' Understanding the mechanics of {topic} gives early adopters a massive asymmetric advantage over traditional investors who are still stuck in the legacy banking system.
    """,
    """
    ## Decentralization Matters
    Why does **{topic}** matter? Because it removes the middleman. By leveraging blockchain technology, {topic} allows for peer-to-peer value exchange without rent-seeking intermediaries. This is not just a technological upgrade; it is a fundamental restructuring of how trust is established in the digital age.
    """,
    """
    ## Volatility as a Feature
    Critics cite volatility as a flaw, but in the context of **{topic}**, volatility is the price of entry for exponential growth. The sharp price movements associated with {topic} shake out weak hands and transfer assets to those with high conviction. Manage your risk, but do not fear the volatility of {topic}.
    """,
    """
    ## On-Chain Data Analysis
    The beauty of **{topic}** is transparency. Unlike Wall Street's dark pools, every transaction regarding {topic} is visible on the public ledger. Our on-chain analysis reveals that whales are aggressively accumulating positions in {topic} during these dips, signaling a potential supply shock.
    """,
    """
    ## Security First
    With great freedom comes great responsibility. Investing in **{topic}** requires a security-first mindset. If you leave your assets on an exchange, you do not own them. Self-custody is the only way to truly secure your exposure to {topic} against hacks and insolvencies.
    """,
    """
    ## The Regulatory Landscape
    Governments are waking up to **{topic}**. While regulation brings short-term uncertainty, clarity is bullish for {topic} in the long run. Institutional capital is sitting on the sidelines, waiting for the regulatory green light to pour billions into the ecosystem surrounding {topic}.
    """,
    """
    ## Layer 2 Scaling Solutions
    The scalability trilemma has plagued blockchains, but innovations in **{topic}** are solving this. Layer 2 solutions are making transactions faster and cheaper, paving the way for mass adoption of {topic}. We are moving from the dial-up era of crypto to broadband speeds.
    """,
    """
    ## Tokenomics Breakdown
    Not all tokens are created equal. When analyzing **{topic}**, you must look at the tokenomics. Is there a hard cap? What is the inflation schedule? Bad tokenomics can ruin a great project. We dissect the supply and demand dynamics of {topic} to determine its long-term viability.
    """,
    """
    ## The Metaverse Intersection
    **{topic}** is becoming the native currency of the digital realm. As we spend more time in virtual environments, the value of digital ownership regarding {topic} will explode. This is the infrastructure layer for the next iteration of the internet.
    """,
    """
    ## Institutional Adoption
    BlackRock, Fidelity, and VanEck are not ignoring **{topic}**. The smart money is building infrastructure for {topic} while retail is fearful. Follow the money. When the world's largest asset managers file ETFs for {topic}, it is time to pay attention.
    """,
    """
    ## Yield Generation in DeFi
    Why let your assets sit idle? Decentralized Finance (DeFi) allows you to earn yield on your **{topic}**. However, yields come with smart contract risk. We explore safe strategies to generate passive income from {topic} without getting rug-pulled.
    """,
    """
    ## NFT Utility Beyond Art
    Non-Fungible Tokens are evolving. **{topic}** represents the shift from JPEGs to utility. From ticketing to real estate deeds, the technology behind {topic} will disrupt trillion-dollar industries by proving provenance and ownership immutably.
    """,
    """
    ## The Halving Effect
    Supply shocks drive prices. In the world of **{topic}**, programmed scarcity is the ultimate value driver. As issuance decreases, if demand for {topic} remains constant or grows, simple economics dictates that price must appreciate.
    """,
    """
    ## Web3 Gaming
    Gamers are the ultimate early adopters. **{topic}** in gaming introduces true asset ownership. Players can now earn and trade assets related to {topic} across different ecosystems. This play-to-earn model is redefining the economics of leisure.
    """,
    """
    ## Artificial Intelligence Synergy
    The convergence of AI and **{topic}** is the narrative of the decade. Autonomous agents using {topic} for payments and resource allocation will create an automated economy. We are looking for projects that sit at the intersection of these two exponential technologies.
    """
]

# [4호기 스마트 매칭: 크립토/보안/트레이딩]
def get_smart_amazon_link(topic):
    topic_lower = topic.lower()
    search_keyword = "ledger+nano+x" # 기본값
    button_text = "🔐 SECURE WALLET"

    if any(x in topic_lower for x in ["trading", "chart", "analysis", "market"]):
        search_keyword = "crypto+trading+technical+analysis+book"
        button_text = "📚 TRADING BOOKS"
    elif any(x in topic_lower for x in ["mining", "rig", "gpu", "hardware"]):
        search_keyword = "bitcoin+miner+hardware"
        button_text = "⛏️ MINING GEAR"
    elif any(x in topic_lower for x in ["nft", "metaverse", "vr", "gaming"]):
        search_keyword = "oculus+quest+3"
        button_text = "🥽 VR HEADSET"
    elif any(x in topic_lower for x in ["seed", "phrase", "steel", "backup"]):
        search_keyword = "crypto+steel+seed+storage"
        button_text = "🛡️ STEEL BACKUP"
    
    return f"https://www.amazon.com/s?k={search_keyword}&tag=empireanalyst-20", button_text

def get_live_trends():
    selected_topic = random.choice(BACKUP_TOPICS)
    return [selected_topic]

def generate_deep_report(topic):
    intro = f"""
# Digital Report: {topic}

## Market Intel
The digital asset landscape is evolving rapidly, and **{topic}** is a key driver. We are witnessing a decoupling from traditional markets. This report dives into the on-chain metrics and future potential of {topic}.
"""
    
    amazon_url, btn_text = get_smart_amazon_link(topic)
    selected_blocks = random.sample(CONTENT_BLOCKS, 4)
    body_content = ""
    
    for block in selected_blocks[:2]:
        body_content += textwrap.dedent(block).format(topic=topic) + "\n"

    # [중간 광고] 4호기 테마: 보라색 (Future/Tech)
    body_content += f"""
<div style="margin: 30px 0; padding: 20px; background: #f3e8ff; border-left: 5px solid #7c3aed; border-radius: 4px;">
    <h3 style="margin-top:0; color:#581c87;">🚀 Future-Proof Your Assets</h3>
    <p>The bull run for <strong>{topic}</strong> is approaching. Are your assets secure and positioned?</p>
    <a href="{amazon_url}" style="display:inline-block; background:#7c3aed; color:#fff; padding:10px 20px; text-decoration:none; font-weight:bold; border-radius:4px;">{btn_text}</a>
    <a href="{AFFILIATE_LINK}" style="display:inline-block; background:#db2777; color:#fff; padding:10px 20px; text-decoration:none; font-weight:bold; border-radius:4px; margin-left:10px;">📈 TRADE CRYPTO</a>
</div>
"""
    for block in selected_blocks[2:]:
        body_content += textwrap.dedent(block).format(topic=topic) + "\n"

    conclusion = f"""
## Final Verdict
Innovation waits for no one. **{topic}** is moving fast. The window of opportunity to be an early adopter is closing.
<br><br>
**Don't get left behind in the analog age.**
<div style="background: #fff; padding: 20px; border: 1px solid #ddd; margin-top: 20px; border-radius: 4px; border-top: 4px solid #7c3aed;">
    <h3>🔮 Alpha Actions</h3>
    <ul style="margin-bottom: 20px;">
        <li>Take self-custody of your digital assets.</li>
        <li>Research the tokenomics before buying.</li>
    </ul>
    <a href="{EMPIRE_URL}" style="background: #581c87; color: white; padding: 10px 20px; text-decoration: none; font-weight: bold; border-radius: 4px; font-size: 0.9rem;">JOIN PRIVATE DISCORD</a>
</div>
"""
    return intro + body_content + conclusion

def generate_seo_files(history):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += f'  <url><loc>{BLOG_BASE_URL}</loc><priority>1.0</priority></url>\n'
    for h in history[:50]:
        sitemap += f'  <url><loc>{BLOG_BASE_URL}{h["file"]}</loc><priority>0.8</priority></url>\n'
    sitemap += '</urlset>'
    with open("sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap)
    robots = f"User-agent: *\nAllow: /\nSitemap: {BLOG_BASE_URL}sitemap.xml"
    with open("robots.txt", "w", encoding="utf-8") as f: f.write(robots)

def create_final_html(topic, img_url, body_html, sidebar_html, amazon_url, btn_text):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="여기에_인증태그_입력" />
    <title>{topic} | {BLOG_TITLE}</title>
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&family=Rajdhani:wght@700&display=swap" rel="stylesheet">
    <style>
        /* 4호기 테마: 퍼플 & 네온 핑크 (미래, 크립토) */
        :root {{ --main-purple: #7c3aed; --accent-pink: #db2777; --dark-text: #1f2937; }}
        body {{ font-family: 'Exo 2', sans-serif; background: #f3f4f6; color: var(--dark-text); line-height: 1.8; margin: 0; }}
        header {{ background: #fff; color: var(--main-purple); padding: 25px; text-align: center; border-bottom: 5px solid var(--accent-pink); }}
        .brand {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; letter-spacing: 2px; text-transform: uppercase; font-weight:bold; }}
        .container {{ max-width: 1100px; margin: 40px auto; display: grid; grid-template-columns: 1fr 320px; gap: 40px; padding: 0 20px; }}
        @media(max-width: 900px) {{ .container {{ grid-template-columns: 1fr; }} }}
        main {{ background: #fff; padding: 50px; border: 1px solid #e5e7eb; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border-radius: 12px; }}
        h1 {{ color: var(--main-purple); font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; margin-top:0; line-height:1.1; }}
        .content h2 {{ color: #4c1d95; margin-top: 40px; border-left: 6px solid var(--accent-pink); padding-left: 15px; font-size: 1.6rem; }}
        img {{ width: 100%; height: auto; margin-bottom: 30px; border-radius: 8px; }}
        .side-card {{ background: #fff; padding: 25px; border: 1px solid #e5e7eb; margin-bottom: 20px; border-top: 4px solid var(--main-purple); border-radius: 8px; }}
        .btn {{ display: block; padding: 15px; background: var(--main-purple); color: #fff; text-decoration: none; font-weight: bold; text-align: center; margin-bottom: 12px; border-radius: 8px; font-size: 1rem; transition: 0.3s; }}
        .btn:hover {{ background: var(--accent-pink); transform: translateY(-2px); }}
        footer {{ text-align: center; padding: 60px; color: #6b7280; background: #fff; border-top: 1px solid #e5e7eb; margin-top: 50px; }}
        .footer-links a {{ color: #4b5563; margin: 0 10px; cursor: pointer; text-decoration: none; font-weight: bold; }}
        .amazon-disclaimer {{ font-size: 0.8rem; color: #9ca3af; margin-top: 20px; font-style: italic; }}
        .modal {{ display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); }}
        .modal-content {{ background: #fff; margin: 15% auto; padding: 30px; width: 80%; max-width: 600px; border-radius: 12px; font-family: sans-serif; }}
        .close {{ float: right; font-size: 28px; cursor: pointer; }}
    </style></head>
    <body>
    <header><div class="brand">{BLOG_TITLE}</div><div style="font-size:0.9rem; color:#6b7280; letter-spacing:1px;">NAVIGATING THE CRYPTO FRONTIER</div></header>
    <div class="container">
        <main>
            <div style="display:inline-block; background:#fce7f3; color:#db2777; font-size:0.8rem; padding:5px 10px; border-radius:20px; margin-bottom:15px; font-weight:bold;">WEB3 INTELLIGENCE</div>
            <h1>{topic}</h1><img src="{img_url}"><div class="content">{body_html}</div>
        </main>
        <aside class="sidebar">
            <div class="side-card">
                <h3 style="margin-top:0; color:var(--main-purple); font-family:'Rajdhani';">CRYPTO TOOLS</h3>
                <a href="{EMPIRE_URL}" class="btn">🚀 ALPHA SIGNALS</a>
                <a href="{AFFILIATE_LINK}" class="btn" style="background:#1f2937;">📊 BYBIT TRADING</a>
                <a href="{amazon_url}" class="btn" style="background:#db2777;">{btn_text}</a>
            </div>
            <div class="side-card">
                <h3>Latest Blocks</h3>
                <ul style="padding-left:20px; list-style-type: square;">{sidebar_html}</ul>
            </div>
        </aside>
    </div>
    <footer>
        <div class="footer-links">
            <a onclick="openModal('about')">About Protocol</a>
            <a onclick="openModal('privacy')">Privacy</a>
            <a onclick="openModal('contact')">Contact</a>
        </div>
        &copy; 2026 {BLOG_TITLE}. Decentralized Future.
        <div class="amazon-disclaimer">* As an Amazon Associate, we earn from qualifying purchases.</div>
    </footer>
    <div id="infoModal" class="modal"><div class="modal-content"><span class="close" onclick="closeModal()">&times;</span><div id="modalBody"></div></div></div>
    <script>
        const info = {{
            about: "<h2>About Digital Alpha</h2><p>We analyze the bleeding edge of blockchain, DeFi, and web3 technologies to find asymmetric opportunities.</p>",
            privacy: "<h2>Data Privacy</h2><p>Your data is yours. We use standard analytics only.</p>",
            contact: "<h2>Contact</h2><p>Admin: admin@empire-analyst.digital</p>"
        }};
        function openModal(id) {{ document.getElementById('modalBody').innerHTML = info[id]; document.getElementById('infoModal').style.display = "block"; }}
        function closeModal() {{ document.getElementById('infoModal').style.display = "none"; }}
    </script>
    </body></html>"""

def main():
    topic = get_live_trends()[0] 
    amazon_url, btn_text = get_smart_amazon_link(topic)
    body_text = generate_deep_report(topic) 
    html_body = markdown.markdown(body_text)
    
    # [4호기 이미지] 네온, 미래, 가상화폐, 보라색
    img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote('neon purple future city crypto blockchain visualization 8k')}?width=1200&height=600"
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f: history = json.load(f)
    
    sidebar_html = "".join([f"<li><a href='{BLOG_BASE_URL}{h.get('file','')}' style='color:#4b5563; text-decoration:none;'>{h.get('title')[:25]}...</a></li>" for h in history[:10]])
    
    archive_name = f"post_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    history.insert(0, {"date": datetime.now().strftime("%Y-%m-%d"), "title": topic, "file": archive_name})
    
    with open(HISTORY_FILE, "w", encoding="utf-8") as f: json.dump(history, f, indent=4)
    generate_seo_files(history)
    
    full_html = create_final_html(topic, img_url, html_body, sidebar_html, amazon_url, btn_text)
    with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    with open(archive_name, "w", encoding="utf-8") as f: f.write(full_html)

if __name__ == "__main__": main()
