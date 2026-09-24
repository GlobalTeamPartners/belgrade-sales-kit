# -*- coding: utf-8 -*-
import os
import json

kit_dir = r"C:\Users\Vlaslav\Agency_HQ\Belgrade_Sales_Kit"

# --- 1. Competitor Analysis ---
competitor_md = """
# 📊 Belgrade Competitor Analysis (Q3 2026)
### Why UnitySpirit & GlobalPlus dominate the local market

| Feature | Local Balkan IT Agencies | UnitySpirit / GlobalPlus |
| :--- | :--- | :--- |
| **Tech Stack** | WordPress, Elementor, basic React. Sites take 2-4 months to build. | **Cinematic Scroll Engine & VEO 3.1.** Sites delivered in 48-72 hours. |
| **AI Integration** | Basic ManyChat decision-trees or standard WhatsApp Business auto-replies. | **Alberta (LLM)**. Context-aware, multilingual concierge capable of qualifying leads and booking complex calendar slots. |
| **Sales Approach** | Cold emails, long PDFs, "we will do an audit". | **"Trojan Horse"** — walking in with the finished product on an iPad. Instant Wow-effect. |
| **Pricing Model** | Fixed €5k-€15k for a website, then they disappear. | **Low barrier to entry (Setup)** + **High LTV (Retainer)**. We become their outsourced tech arm. |
| **Understanding of Expats** | They build for the local Serbian market in Cyrillic/Latin. | We build specifically to capture the high-net-worth Russian/CIS and Western European expat money. |

> **Your Ultimate Edge:** Local agencies sell *websites*. You sell *infrastructure that captures expat wealth*. 
"""

# --- 2. Company Database ---
companies = {
    "HORECA": [
        {"name": "Salon 1905", "focus": "Historic Michelin-tier dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"name": "Square Nine Hotel", "focus": "Ultra-luxury hospitality & lobby", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"name": "Langouste", "focus": "River-view fine dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"name": "Buddha-Bar Belgrade", "focus": "Premium nightlife & VIP tables", "price": "Setup: €3,000 | Retainer: €700/mo"},
        {"name": "Toro Latin GastroBar", "focus": "High-volume premium dining", "price": "Setup: €2,000 | Retainer: €500/mo"},
        {"name": "Frans", "focus": "Legacy elite Serbian restaurant", "price": "Setup: €3,500 | Retainer: €600/mo"},
        {"name": "Ambar", "focus": "Balkan cuisine on the river", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"name": "Enso", "focus": "Modernist fine dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"name": "Legat 1903", "focus": "Exclusive wine and dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"name": "Kalemegdanska Terasa", "focus": "Huge wedding & event venue", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"name": "Metropol Palace Hotel", "focus": "Large luxury hotel & spa", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"name": "Hilton Belgrade", "focus": "Rooftop dining (SkyLounge)", "price": "Setup: €3,500 | Retainer: €800/mo"},
        {"name": "Saint Ten Hotel", "focus": "Boutique luxury hotel", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"name": "Hyatt Regency", "focus": "Corporate & expat hub", "price": "Setup: €5,000 | Retainer: €1,200/mo"},
        {"name": "Hotel Moskva", "focus": "Heritage hotel & cafe", "price": "Setup: €4,000 | Retainer: €700/mo"}
    ],
    "Real Estate": [
        {"name": "Belgrade Waterfront (Eagle Hills)", "focus": "Massive luxury high-rises", "price": "Setup: €8,000 | Retainer: €2,000/mo"},
        {"name": "Turaquadra", "focus": "Boutique luxury brokerage", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"name": "West 65 / Kula", "focus": "Modern luxury residential tower", "price": "Setup: €6,000 | Retainer: €1,500/mo"},
        {"name": "Merin Group", "focus": "Premium residential developers", "price": "Setup: €5,000 | Retainer: €1,200/mo"},
        {"name": "AFI Europe Serbia", "focus": "Premium corporate/residential", "price": "Setup: €6,000 | Retainer: €1,500/mo"},
        {"name": "K-District", "focus": "Historic Dorcol redevelopment", "price": "Setup: €4,500 | Retainer: €1,000/mo"},
        {"name": "Skyline Belgrade", "focus": "Iconic multi-tower project", "price": "Setup: €5,500 | Retainer: €1,200/mo"},
        {"name": "Novi Dorcol", "focus": "Modern smart-home complex", "price": "Setup: €4,500 | Retainer: €1,000/mo"},
        {"name": "Kennedy Residences", "focus": "High-end New Belgrade flats", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"name": "Sotheby's Serbia", "focus": "Ultra-HNW individual villas", "price": "Setup: €6,000 | Retainer: €1,500/mo"}
    ],
    "Auto & Detailing": [
        {"name": "Auto Shine Detailing", "focus": "Premium ceramic & PPF", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"name": "Black Glass", "focus": "High-volume tinting & wrap", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"name": "British Motors (JLR)", "focus": "Jaguar & Land Rover sales", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"name": "Delta Motors (BMW)", "focus": "BMW official dealer", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"name": "Star Import (Mercedes)", "focus": "Mercedes-Benz dealer", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"name": "Porsche SCG", "focus": "Porsche/Audi premium sales", "price": "Setup: €6,000 | Retainer: €1,200/mo"},
        {"name": "Titanium Detailing", "focus": "Niche luxury detailing", "price": "Setup: €1,500 | Retainer: €300/mo"},
        {"name": "Auto Finesse SRB", "focus": "Product distribution & studio", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"name": "Garage 73", "focus": "Custom builds & tuning", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"name": "Gtechniq Serbia", "focus": "Ceramic coating HQ", "price": "Setup: €2,500 | Retainer: €500/mo"}
    ],
    "Medical & Beauty": [
        {"name": "Rea Medika", "focus": "Premium aesthetic medicine", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"name": "Diva Clinic", "focus": "Dermatology & laser clinic", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"name": "Vsan Dental", "focus": "Dental tourism for expats", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"name": "Dr. Magic", "focus": "Plastic surgery portfolio", "price": "Setup: €3,500 | Retainer: €700/mo"},
        {"name": "Bel Medic (Acibadem)", "focus": "Massive private hospital", "price": "Setup: €8,000 | Retainer: €2,500/mo"},
        {"name": "La Roche Beauty", "focus": "High-end beauty salon", "price": "Setup: €1,500 | Retainer: €300/mo"},
        {"name": "City Spa Retreat", "focus": "Luxury day spa", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"name": "Saruna Wellness", "focus": "Premium hotel wellness chains", "price": "Setup: €3,500 | Retainer: €800/mo"},
        {"name": "Dental Plaza", "focus": "High-volume dental clinic", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"name": "Aesthetic Belgrade", "focus": "Boutique injectables", "price": "Setup: €2,000 | Retainer: €400/mo"}
    ],
    "Luxury Services": [
        {"name": "Porto Montenegro (BG Office)", "focus": "Yacht and coastal real estate", "price": "Setup: €5,000 | Retainer: €1,200/mo"},
        {"name": "Absolut Time (Rolex)", "focus": "Exclusive watch retailer", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"name": "Maestro Jewelers", "focus": "High jewelry", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"name": "Air Serbia (VIP Lounge)", "focus": "Premium aviation services", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"name": "Yandex VIP Concierge", "focus": "High-end expat services", "price": "Setup: €6,000 | Retainer: €1,500/mo"}
    ]
}

def generate_pitch(sector, name, focus):
    if sector == "HORECA":
        return f"**Quick Start:** Deploy a Cinematic Menu & Web-portal showcasing the {focus} experience in 48h. <br>**Long-Term:** Integrate 'Alberta' AI into WhatsApp to manage Russian/English reservations, take deposits for VIP tables, and remember guest allergies automatically."
    elif sector == "Real Estate":
        return f"**Quick Start:** Deploy a VEO-generated Cinematic Scroll of {name} to emotionally hook foreign investors. <br>**Long-Term:** AI Lead-Qualify Bot. The bot interviews investors (budget, timeline) and only forwards verified €500k+ buyers to the brokers."
    elif sector == "Auto & Detailing":
        return f"**Quick Start:** Launch a visually aggressive, mobile-first cinematic site for {name}. <br>**Long-Term:** AI Appointment Setter. The bot syncs with their garage calendar, books PPF/Ceramic jobs, and takes a 20% deposit upfront via Stripe."
    elif sector == "Medical & Beauty":
        return f"**Quick Start:** Trust-optimized Cinematic Portfolio highlighting {focus}. <br>**Long-Term:** AI Triage & Privacy Booking. Wealthy expats answer 3 questions via Telegram bot, and the bot matches them to the right specialist without human front-desk friction."
    else:
        return f"**Quick Start:** Ultra-luxury cinematic showcase for {name}. <br>**Long-Term:** Bespoke AI Concierge to handle High-Net-Worth Client requests 24/7."

# Generate Markdown
html_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Competitor Analysis & 50 Pitches</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  body {{ font-family: 'Inter', sans-serif; background: #1A1A1A; color: #fff; padding: 40px; max-width: 1000px; margin: 0 auto; line-height: 1.6; }}
  h1, h2, h3 {{ color: #C5A059; font-family: 'Playfair Display', serif; }}
  a {{ color: #D32F2F; text-decoration: none; font-weight: bold;}}
  .btn-back {{ display: inline-block; margin-bottom: 30px; padding: 10px 20px; background: #D32F2F; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #2A2A2A; border-radius: 8px; overflow: hidden; font-size: 0.9rem; }}
  th, td {{ padding: 15px; text-align: left; border-bottom: 1px solid #444; vertical-align: top; }}
  th {{ background: #D32F2F; color: white; font-weight: bold; }}
  tr:hover {{ background: #333; }}
  .price {{ color: #10B981; font-weight: bold; }}
  .sector-title {{ margin-top: 50px; border-bottom: 2px solid #C5A059; padding-bottom: 10px; }}
</style>
</head>
<body>
<a href="Sales_Hub.html" class="btn-back">&larr; Back to Sales Hub</a>
<div id="md-content"></div>

"""

for sector, items in companies.items():
    html_body += f"<h2 class='sector-title'>{sector} (50-Company Deep Dive)</h2>\n"
    html_body += "<table><thead><tr><th width='20%'>Company</th><th width='50%'>Pitch & Long-Term Plan</th><th width='30%'>Pricing Offer</th></tr></thead><tbody>\n"
    for c in items:
        pitch = generate_pitch(sector, c['name'], c['focus'])
        html_body += f"<tr><td><strong>{c['name']}</strong><br><span style='color:#aaa; font-size:0.8rem;'>{c['focus']}</span></td>"
        html_body += f"<td>{pitch}</td>"
        html_body += f"<td class='price'>{c['price']}</td></tr>\n"
    html_body += "</tbody></table>\n"

html_body += """
<script>
  const markdownText = `{md_content}`;
  document.getElementById('md-content').innerHTML = marked.parse(markdownText);
</script>
</body>
</html>
"""

html_body = html_body.replace("{md_content}", competitor_md.replace('`', "'").replace('\\', '\\\\'))

with open(os.path.join(kit_dir, "Comprehensive_Pitches.html"), "w", encoding="utf-8") as f:
    f.write(html_body)

# Update Sales Hub with the new button
hub_path = os.path.join(kit_dir, "Sales_Hub.html")
with open(hub_path, "r", encoding="utf-8") as f:
    hub_html = f.read()

if "Comprehensive_Pitches.html" not in hub_html:
    new_btn = """
                <a href="Comprehensive_Pitches.html" class="asset-link" style="background: #8E24AA; color: white;">
                    <span class="icon">🔍</span> 50 Pitches & Pricing <span class="badge" style="background: white; color: #8E24AA;">NEW</span>
                </a>"""
    hub_html = hub_html.replace('<!-- STRATEGY & LEADS SECTOR -->', '<!-- STRATEGY & LEADS SECTOR -->\n' + new_btn)
    # Just insert it into the grid
    target = '<a href="Market_Intelligence.html"'
    hub_html = hub_html.replace(target, new_btn + '\n                ' + target)
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(hub_html)

print("Comprehensive pitches generated successfully.")
