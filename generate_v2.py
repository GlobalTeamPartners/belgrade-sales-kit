import os

kit_dir = r"C:\Users\Vlaslav\Agency_HQ\Belgrade_Sales_Kit"

# 1. Update Sales_Hub.html
sales_hub_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GlobalPlus & Unity Spirit - Belgrade Sales Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root { --navy: #1A1A1A; --gold: #C5A059; --white: #FFFFFF; --gray: #F5F5F5; --dark-gray: #333333; --red: #D32F2F; }
        body { margin: 0; font-family: 'Inter', sans-serif; background-color: var(--gray); color: var(--navy); }
        header { background-color: var(--navy); color: var(--white); padding: 40px 20px; text-align: center; border-bottom: 4px solid var(--red); }
        h1 { font-family: 'Playfair Display', serif; margin: 0 0 10px 0; font-size: 2.5rem; color: var(--white); }
        h1 span { color: var(--red); }
        p.subtitle { margin: 0; font-size: 1.1rem; opacity: 0.9; color: var(--gold); }
        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
        .sector-card { background: var(--white); border-radius: 12px; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); transition: transform 0.3s ease; border-top: 4px solid var(--navy); }
        .sector-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.1); }
        .sector-title { font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-top: 0; margin-bottom: 20px; color: var(--navy); border-bottom: 2px solid var(--gray); padding-bottom: 15px; }
        .asset-link { display: flex; align-items: center; padding: 12px 15px; margin-bottom: 10px; background-color: var(--gray); border-radius: 8px; text-decoration: none; color: var(--navy); font-weight: 500; transition: all 0.2s; }
        .asset-link:hover { background-color: var(--navy); color: var(--gold); }
        .icon { margin-right: 12px; font-size: 1.2rem; }
        .badge { background: var(--red); color: var(--white); padding: 2px 8px; border-radius: 12px; font-size: 0.7rem; font-weight: bold; margin-left: auto; }
        .footer { text-align: center; padding: 40px 20px; color: var(--dark-gray); font-size: 0.9rem; }
    </style>
</head>
<body>
<header>
    <h1>Unity Spirit <span>&times;</span> GlobalPlus</h1>
    <p class="subtitle">Belgrade Executive Mission — 3-Week Solo Sprint</p>
</header>
<div class="container">
    <div class="grid">
        <div class="sector-card" style="grid-column: 1 / -1; border-top: 4px solid var(--red);">
            <h2 class="sector-title">?? Strategy & Lead Database</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <a href="Leads_List.html" class="asset-link" style="background: var(--navy); color: var(--gold);">
                    <span class="icon">??</span> 50-Company Master Lead List <span class="badge" style="background: white; color: var(--navy);">NEW</span>
                </a>
                <a href="Solo_Executive_Strategy.html" class="asset-link" style="background: var(--red); color: white;">
                    <span class="icon">??</span> The "Lone Wolf" B2B Strategy <span class="badge" style="background: white; color: var(--red);">HOT</span>
                </a>
                <a href="Market_Intelligence.html" class="asset-link" style="background: var(--gold); color: var(--navy);">
                    <span class="icon">??</span> Belgrade Market Intelligence
                </a>
            </div>
        </div>
        <div class="sector-card">
            <h2 class="sector-title">?? Premium HORECA</h2>
            <a href="https://GlobalTeamPartners.github.io/salon-1905-demo/" class="asset-link" target="_blank"><span class="icon">??</span> Demo: Salon 1905 <span class="badge">LIVE</span></a>
        </div>
        <div class="sector-card">
            <h2 class="sector-title">??? Real Estate & Dev</h2>
            <a href="https://GlobalTeamPartners.github.io/belgrade-waterfront-demo/" class="asset-link" target="_blank"><span class="icon">??</span> Demo: BG Waterfront <span class="badge">LIVE</span></a>
        </div>
        <div class="sector-card">
            <h2 class="sector-title">??? Auto Detailing</h2>
            <a href="https://GlobalTeamPartners.github.io/auto-shine-demo/" class="asset-link" target="_blank"><span class="icon">??</span> Demo: Auto Shine <span class="badge">LIVE</span></a>
        </div>
    </div>
</div>
</body></html>"""

# 2. Solo Executive Strategy
solo_strategy_md = """
# ?? The "Lone Wolf" Solo Executive Strategy
### A 3-Week Aggressive Playbook for Belgrade (Solo Trip)

> **Mission:** You are in Belgrade **alone** for 3+ weeks. Without a partner to soften the approach, you must pivot from "Romantic Client" to **"International IT Investor & Founder"**. You are here to build a hub, and you are selecting a few elite local brands to partner with.

---

## ?? The Core Positioning
You are not a salesman asking for their time. You are the CEO of a Canadian/Russian Tech Agency exploring the Serbian market. You've pre-selected them as a potential flagship partner for your newest AI and Cinematic Web technologies.

**Your Persona:** Busy, decisive, well-connected expat looking for local synergy.

---

## ??? The 3-Step Approval Framework

### Step 1: The "Executive Drop-in" (Reconnaissance)
* **Action:** Walk into the business (restaurant, real estate office, clinic) as a high-net-worth client. Order a coffee, look at a car, inquire about an apartment.
* **Objective:** Identify the decision-maker (Owner, GM, or Marketing Director). Do not pitch yet. Get their name and understand the venue's vibe.

### Step 2: The "Asymmetric Value" Hook (The Trojan Horse)
* **Action:** You ask to speak to the GM/Director for 60 seconds because you have a "digital asset" that belongs to them.
* **The Script:** *"Hi [Name], I'm Vlad. I run a tech agency in Canada and Russia. We're opening operations in Belgrade. I've been reviewing the premium market here, and your brand is top-tier. However, your digital presence is losing you high-net-worth expat money. I actually had my team build a cinematic prototype specifically for [Salon 1905 / Auto Shine]. Take this iPad for 30 seconds and scroll."*

### Step 3: The "Soft Close" (Gaining Approval)
* **Action:** They will be blown away by the Cinematic Scroll.
* **The Script:** *"I'm here for 3 weeks. I want you to be our first flagship case study in the Balkans. I will give you this infrastructure at our internal cost, in exchange for a local testimonial. Let's sit down for 15 minutes on Thursday to discuss integrating this with an AI booking bot."*

---

## ?? The 3-Week Rhythm

* **Week 1: Seeding.** Visit 15-20 targets. Drop the iPad demo. Collect WhatsApp numbers of GMs.
* **Week 2: Follow-ups & AI Demos.** Send them the `tvui.ru` link. Meet for coffee. Show them the AI Telegram bot (Alberta) in action.
* **Week 3: Closing.** Sign contracts, collect deposits, hand over technical specs to the team.

"""

# 3. Market Intelligence
intel_md = """
# ?? Belgrade Market Intelligence Report (Q3 2026)

## Macro Environment
* **The Expat Wave:** Belgrade has absorbed over 150,000 Russian/CIS expats and thousands of Western digital nomads. This has created a massive parallel "premium" economy.
* **The Gap:** Local businesses have high-quality physical products (great food, good real estate, excellent services), but their **digital infrastructure is stuck in 2015**. They rely on Instagram DMs and Viber for bookings.
* **The Pain Point:** Wealthy expats hate calling on the phone and hate waiting for DMs. They want instantaneous, cinematic digital experiences and AI-driven instant bookings.

## Sector Breakdown

### 1. Real Estate (High-Rise & Luxury)
* **Market Status:** Booming. Prices in Belgrade Waterfront reach €5,000 - €10,000/sqm.
* **The Need:** Cinematic visualization to sell off-plan to foreign investors. AI lead qualification to filter out tire-kickers.
* **Key Players:** Eagle Hills, Merin Group, AFI Europe, West 65.

### 2. Premium HORECA
* **Market Status:** Highly competitive. Michelin guide recently entered Belgrade.
* **The Need:** Multi-lingual digital menus, AI concierge for reservations, cinematic websites to justify premium pricing.
* **Key Players:** Salon 1905, Langouste, Square Nine, Buddha-Bar.

### 3. Private Medical & Aesthetics
* **Market Status:** Surging due to medical tourism and wealthy expats.
* **The Need:** Trust-building cinematic portfolios, automated lead generation.
* **Key Players:** Rea Medika, Diva Clinic, Bel Medic.
"""

# 4. Lead Database (50 Companies)
leads_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>50-Company Lead Database</title>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1A1A1A; color: #fff; padding: 20px; }
        h1 { color: #C5A059; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #2A2A2A; border-radius: 8px; overflow: hidden; }
        th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #444; }
        th { background: #D32F2F; color: white; font-weight: bold; }
        tr:hover { background: #333; }
        .badge { padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
        .bg-horeca { background: #8E24AA; color: white; }
        .bg-realestate { background: #1976D2; color: white; }
        .bg-auto { background: #388E3C; color: white; }
        .bg-beauty { background: #E91E63; color: white; }
    </style>
</head>
<body>
    <a href="Sales_Hub.html" style="color: #D32F2F; text-decoration: none; font-weight: bold;">&larr; Back to Hub</a>
    <h1>?? 50-Company Master Lead List</h1>
    <p>Targeted premium sectors in Belgrade for October 2026.</p>
    
    <table>
        <thead>
            <tr>
                <th>Company Name</th>
                <th>Sector</th>
                <th>Target Persona</th>
                <th>Proposed Trojan Horse Pitch</th>
            </tr>
        </thead>
        <tbody>
            <!-- HORECA -->
            <tr><td>Salon 1905</td><td><span class="badge bg-horeca">HORECA</span></td><td>GM / Marketing Dir</td><td>Cinematic Scroll Demo (Ready)</td></tr>
            <tr><td>Square Nine Hotel</td><td><span class="badge bg-horeca">HORECA</span></td><td>Hotel Manager</td><td>AI Multilingual Concierge</td></tr>
            <tr><td>Langouste</td><td><span class="badge bg-horeca">HORECA</span></td><td>Owner</td><td>Michelin-tier Cinematic Site</td></tr>
            <tr><td>Buddha-Bar Belgrade</td><td><span class="badge bg-horeca">HORECA</span></td><td>GM</td><td>Nightlife Booking Automation</td></tr>
            <tr><td>Toro Latin GastroBar</td><td><span class="badge bg-horeca">HORECA</span></td><td>GM</td><td>Dynamic Video Menu</td></tr>
            <tr><td>Frans</td><td><span class="badge bg-horeca">HORECA</span></td><td>Owner</td><td>Legacy brand digital modernization</td></tr>
            <tr><td>Ambar</td><td><span class="badge bg-horeca">HORECA</span></td><td>Marketing Dir</td><td>Expat lead generation</td></tr>
            <tr><td>Enso</td><td><span class="badge bg-horeca">HORECA</span></td><td>Head Chef / Owner</td><td>Chef's portfolio cinematic site</td></tr>
            <tr><td>Legat 1903</td><td><span class="badge bg-horeca">HORECA</span></td><td>GM</td><td>High-end wine reservation bot</td></tr>
            <tr><td>Kalemegdanska Terasa</td><td><span class="badge bg-horeca">HORECA</span></td><td>Event Manager</td><td>Wedding & Event VR/Video Site</td></tr>
            <tr><td>Metropol Palace Hotel</td><td><span class="badge bg-horeca">HORECA</span></td><td>GM</td><td>AI Concierge & Spa Booking</td></tr>
            <tr><td>Hilton Belgrade</td><td><span class="badge bg-horeca">HORECA</span></td><td>F&B Director</td><td>Rooftop bar VIP booking bot</td></tr>
            <tr><td>Saint Ten Hotel</td><td><span class="badge bg-horeca">HORECA</span></td><td>Boutique Owner</td><td>Cinematic Scroll Demo</td></tr>
            <tr><td>Hyatt Regency</td><td><span class="badge bg-horeca">HORECA</span></td><td>Marketing Dir</td><td>Corporate Event AI booking</td></tr>
            <tr><td>Hotel Moskva</td><td><span class="badge bg-horeca">HORECA</span></td><td>GM</td><td>Heritage modernization website</td></tr>

            <!-- REAL ESTATE -->
            <tr><td>Belgrade Waterfront</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Sales Director</td><td>Cinematic Scroll Demo (Ready)</td></tr>
            <tr><td>Turaquadra</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Broker / Owner</td><td>AI Lead Qualification Bot</td></tr>
            <tr><td>West 65 / Kula</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Sales Director</td><td>Cinematic Penthouse Tour</td></tr>
            <tr><td>Merin Group</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Marketing Dir</td><td>Automated Investor CRM</td></tr>
            <tr><td>AFI Europe Serbia</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Commercial Dir</td><td>B2B Leasing Cinematic Site</td></tr>
            <tr><td>K-District</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Sales Manager</td><td>Video-first landing pages</td></tr>
            <tr><td>Skyline Belgrade</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Sales Director</td><td>AI Sales Agent for foreign buyers</td></tr>
            <tr><td>Novi Dorcol</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Marketing Dir</td><td>Cinematic Scroll Demo</td></tr>
            <tr><td>Kennedy Residences</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Sales Manager</td><td>AI Lead Qualify</td></tr>
            <tr><td>Sotheby's Serbia</td><td><span class="badge bg-realestate">Real Estate</span></td><td>Managing Director</td><td>Ultra-luxury property video sites</td></tr>

            <!-- AUTO DETAILING -->
            <tr><td>Auto Shine Detailing</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Owner</td><td>Cinematic Scroll Demo (Ready)</td></tr>
            <tr><td>Black Glass</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Owner</td><td>Automated Appointment Bot</td></tr>
            <tr><td>British Motors (JLR)</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Marketing Dir</td><td>Cinematic VIP Test Drive Site</td></tr>
            <tr><td>Delta Motors (BMW)</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Sales Manager</td><td>AI Test Drive Booking</td></tr>
            <tr><td>Star Import (Mercedes)</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Marketing Dir</td><td>High-end showcase website</td></tr>
            <tr><td>Porsche SCG</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Marketing Dir</td><td>Cinematic Scroll Demo</td></tr>
            <tr><td>Titanium Detailing</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Owner</td><td>Before/After Video Site</td></tr>
            <tr><td>Auto Finesse SRB</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Owner</td><td>E-commerce Cinematic Scroll</td></tr>
            <tr><td>Garage 73</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Owner</td><td>Automated Appointment Bot</td></tr>
            <tr><td>Gtechniq Serbia</td><td><span class="badge bg-auto">Auto/Detailing</span></td><td>Distributor</td><td>B2B Partner Portal</td></tr>

            <!-- BEAUTY & WELLNESS -->
            <tr><td>Rea Medika</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Clinic Director</td><td>VIP Privacy Booking Bot</td></tr>
            <tr><td>Diva Clinic</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Owner</td><td>Cinematic Doctor Portfolio</td></tr>
            <tr><td>Vsan Dental</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Lead Dentist</td><td>Expat Dental Tourism Website</td></tr>
            <tr><td>Dr. Magic</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Owner</td><td>Before/After Cinematic Scroll</td></tr>
            <tr><td>Bel Medic (Acibadem)</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Marketing Dir</td><td>AI Triage & Booking Bot</td></tr>
            <tr><td>La Roche Beauty</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Manager</td><td>Automated Appointment Bot</td></tr>
            <tr><td>City Spa Retreat</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Owner</td><td>Cinematic Vibe Website</td></tr>
            <tr><td>Saruna Wellness</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>GM</td><td>Membership Automation Bot</td></tr>
            <tr><td>Dental Plaza</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Marketing Dir</td><td>Expat landing pages</td></tr>
            <tr><td>Aesthetic Belgrade</td><td><span class="badge bg-beauty">Beauty/Medical</span></td><td>Owner</td><td>Cinematic Scroll Demo</td></tr>

            <!-- PREMIUM SERVICES / OTHER -->
            <tr><td>Porto Montenegro (BG Office)</td><td><span class="badge bg-realestate">Premium Yachts</span></td><td>Sales Dir</td><td>Ultra-luxury video site</td></tr>
            <tr><td>Absolut Time (Rolex)</td><td><span class="badge bg-auto">Luxury Retail</span></td><td>Boutique Mgr</td><td>VIP Client CRM Bot</td></tr>
            <tr><td>Maestro Jewelers</td><td><span class="badge bg-auto">Luxury Retail</span></td><td>Owner</td><td>Cinematic Product Showcase</td></tr>
            <tr><td>Air Serbia (VIP Lounge)</td><td><span class="badge bg-horeca">Aviation</span></td><td>Lounge Mgr</td><td>AI Feedback & Concierge</td></tr>
            <tr><td>GlobalPlus Integrators</td><td><span class="badge bg-beauty">B2B</span></td><td>YOURSELF</td><td>Dominate the market!</td></tr>
        </tbody>
    </table>
</body>
</html>"""

def make_html(md_content, title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  body {{ font-family: 'Inter', sans-serif; background: #1A1A1A; color: #fff; padding: 40px; max-width: 800px; margin: 0 auto; line-height: 1.6; }}
  h1, h2, h3 {{ color: #C5A059; font-family: 'Playfair Display', serif; }}
  a {{ color: #D32F2F; text-decoration: none; font-weight: bold;}}
  .btn-back {{ display: inline-block; margin-bottom: 30px; padding: 10px 20px; background: #D32F2F; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; }}
  hr {{ border-color: rgba(197,160,89,0.2); margin: 30px 0;}}
  li {{ margin-bottom: 10px; }}
  blockquote {{ background: rgba(255,255,255,0.05); padding: 15px; border-left: 4px solid #D32F2F; margin: 0 0 30px 0;}}
  strong {{ color: #fff; }}
</style>
</head>
<body>
<a href="Sales_Hub.html" class="btn-back">&larr; Back to Sales Hub</a>
<div id="content"></div>
<script>
  const markdownText = `{md_content.replace('`', "'").replace('\\', '\\\\')}`;
  document.getElementById('content').innerHTML = marked.parse(markdownText);
</script>
</body>
</html>"""

with open(os.path.join(kit_dir, "Sales_Hub.html"), "w", encoding="utf-8") as f:
    f.write(sales_hub_html)

with open(os.path.join(kit_dir, "Solo_Executive_Strategy.html"), "w", encoding="utf-8") as f:
    f.write(make_html(solo_strategy_md, "Solo Strategy"))

with open(os.path.join(kit_dir, "Market_Intelligence.html"), "w", encoding="utf-8") as f:
    f.write(make_html(intel_md, "Market Intelligence"))

with open(os.path.join(kit_dir, "Leads_List.html"), "w", encoding="utf-8") as f:
    f.write(leads_html)

print("Hub updated for solo trip.")
