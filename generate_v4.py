# -*- coding: utf-8 -*-
import os

kit_dir = r"C:\Users\Vlaslav\Agency_HQ\Belgrade_Sales_Kit"

# 1. New File: Fast_Collab_Pitches.html
pitches_md = """
# 🚀 Fast Collaboration & Pitches Blueprint
### How to trigger an instant "Quick Start" that locks them into a Long-Term Plan

> **The Psychology of the Fast Start:** Premium businesses in Belgrade are tired of long IT proposals and "6-month development cycles". You will pitch them a **Phase 1 deployment within 48 hours** (because you already built the demo). Once they see the immediate ROI, you upsell them into a long-term retention contract.

---

## 🏎️ The "Quick Start ➡️ Long-Term" Pipeline

### 🟢 Phase 1: The Quick Start (48 Hours)
* **What you deliver:** The pre-built Cinematic Scroll Website or a basic AI Lead-Capture Bot on Telegram.
* **The Deal:** *"I already built the prototype. We can connect your domain and launch it tomorrow. I'm waiving the massive upfront development fee; you just pay a small setup fee and server costs so we can start generating leads this weekend."*
* **The Goal:** Build instant trust. No massive risk for them. Fast execution.

### 🟡 Phase 2: The Infrastructure Build (1 Month)
* **What you deliver:** Multilingual AI integrations (Russian/English/Serbian), automated booking systems connected to their CRM (Calendly/Fresha/Custom).
* **The Deal:** *"Now that the landing page is capturing high-net-worth expat traffic, your staff can't handle the DMs. Let's install 'Alberta' (our AI agent) to qualify leads 24/7."*

### 🔴 Phase 3: The Long-Term Partnership (1-3 Years)
* **What you deliver:** GlobalPlus/UnitySpirit becomes their fully outsourced Tech & Marketing arm.
* **The Deal:** Monthly retainer ($2,000 - $5,000/mo). You manage all web updates, AI infrastructure, and direct high-value expat traffic from your own networks (`tvui.ru`).

---

## 🎯 Sector-Specific Pitch Scripts

### 1. 🍷 Premium HORECA (Restaurants & Hotels)
**Target:** Salon 1905, Square Nine, Langouste
* **The Hook:** "I've been analyzing the influx of wealthy expats in Belgrade. They are used to instant digital service in Moscow and Toronto. Right now, they are struggling to book tables at your restaurant because it requires a phone call."
* **Quick Start Pitch:** "I had my team build a cinematic menu and VIP reservation portal for you. *[Show iPad Demo]* We can deploy this tomorrow. It handles Russian and English traffic instantly."
* **Long-Term Upsell:** "Next month, we connect an AI Concierge to your WhatsApp to handle VIP requests, allergies, and large deposits automatically."

### 2. 🏙️ Real Estate & Developers
**Target:** Belgrade Waterfront, Turaquadra
* **The Hook:** "You have the best properties in the city, but your sales brokers are wasting 60% of their time talking to people who don't have €500k to invest."
* **Quick Start Pitch:** "Look at this cinematic showcase we built for your off-plan project. *[Show iPad Demo]* It emotionally hooks foreign investors before they even fly to Serbia. We can put this live in 48 hours."
* **Long-Term Upsell:** "Our AI lead qualification bot will interview every visitor. Your brokers will only receive alerts on their phones when a verified buyer with proof of funds wants to talk."

### 3. 🏎️ Auto Detailing & Luxury Services
**Target:** Auto Shine, Black Glass, British Motors
* **The Hook:** "Your detailing work is world-class, but guys driving $200k Porsches don't want to wait 4 hours for an Instagram DM reply to book a ceramic coating."
* **Quick Start Pitch:** "I built a mobile-first cinematic site for you that makes the cars look incredible. *[Show iPad Demo]* Let's launch this fast-start version this week."
* **Long-Term Upsell:** "Once this is live, we integrate an automated scheduling system. The AI books the slot, takes a €100 deposit upfront to stop no-shows, and sends them SMS reminders."

### 4. 💉 Medical, Beauty & Wellness
**Target:** Rea Medika, Diva Clinic, Vsan Dental
* **The Hook:** "Medical tourism and expat wives are a multi-million euro market in Belgrade right now. But health is about trust, and trust requires an immaculate digital image."
* **Quick Start Pitch:** "We built a trust-optimized cinematic portfolio for your top doctors. *[Show iPad]* It explains the procedures visually. We can launch the Quick Start version instantly."
* **Long-Term Upsell:** "Long-term, we build an AI Triage bot. It asks the patient 5 qualifying questions about their aesthetic goals and automatically routes them to the right doctor's calendar."
"""

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

with open(os.path.join(kit_dir, "Fast_Collab_Pitches.html"), "w", encoding="utf-8") as f:
    f.write(make_html(pitches_md, "Fast Collab & Pitches"))


# 2. Re-write Sales_Hub.html to include the new button
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
    <p class="subtitle">Belgrade Executive Mission - 3-Week Solo Sprint</p>
</header>
<div class="container">
    <div class="grid">
        <div class="sector-card" style="grid-column: 1 / -1; border-top: 4px solid var(--red);">
            <h2 class="sector-title">🎯 Strategy & Lead Database</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <a href="Leads_List.html" class="asset-link" style="background: var(--navy); color: var(--gold);">
                    <span class="icon">📋</span> 50-Company Master Lead List
                </a>
                <a href="Solo_Executive_Strategy.html" class="asset-link" style="background: var(--red); color: white;">
                    <span class="icon">🐺</span> The "Lone Wolf" Playbook 
                </a>
                <a href="Fast_Collab_Pitches.html" class="asset-link" style="background: #10B981; color: white;">
                    <span class="icon">🚀</span> Fast Collab & Scripts <span class="badge" style="background: white; color: #10B981;">NEW</span>
                </a>
                <a href="Market_Intelligence.html" class="asset-link" style="background: var(--gold); color: var(--navy);">
                    <span class="icon">🧠</span> Market Intelligence
                </a>
            </div>
        </div>
        <div class="sector-card">
            <h2 class="sector-title">🍷 Premium HORECA</h2>
            <a href="https://GlobalTeamPartners.github.io/salon-1905-demo/" class="asset-link" target="_blank"><span class="icon">🌐</span> Demo: Salon 1905 <span class="badge">LIVE</span></a>
        </div>
        <div class="sector-card">
            <h2 class="sector-title">🏙️ Real Estate & Dev</h2>
            <a href="https://GlobalTeamPartners.github.io/belgrade-waterfront-demo/" class="asset-link" target="_blank"><span class="icon">🌐</span> Demo: BG Waterfront <span class="badge">LIVE</span></a>
        </div>
        <div class="sector-card">
            <h2 class="sector-title">🏎️ Auto Detailing</h2>
            <a href="https://GlobalTeamPartners.github.io/auto-shine-demo/" class="asset-link" target="_blank"><span class="icon">🌐</span> Demo: Auto Shine <span class="badge">LIVE</span></a>
        </div>
    </div>
</div>
</body></html>"""

with open(os.path.join(kit_dir, "Sales_Hub.html"), "w", encoding="utf-8") as f:
    f.write(sales_hub_html)

print("Updated with Fast Collab pitches")
