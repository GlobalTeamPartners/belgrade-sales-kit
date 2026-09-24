import os

kit_dir = r"C:\Users\Vlaslav\Agency_HQ\Belgrade_Sales_Kit"

sales_hub_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GlobalPlus & Unity Spirit - Belgrade Sales Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --navy: #1A1A1A;
            --gold: #C5A059;
            --white: #FFFFFF;
            --gray: #F5F5F5;
            --dark-gray: #333333;
            --red: #D32F2F;
        }
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
    <p class="subtitle">Belgrade Executive Mission — October 2026</p>
</header>

<div class="container">
    <div class="grid">

        <div class="sector-card" style="grid-column: 1 / -1; border-top: 4px solid var(--red);">
            <h2 class="sector-title">?? Executive Strategy & Itinerary</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <a href="Couples_Roadmap.html" class="asset-link" style="background: var(--navy); color: var(--gold);">
                    <span class="icon">??</span> 4-Day "Couples Retreat" Roadmap <span class="badge" style="background: var(--red); color: white;">HOT</span>
                </a>
                <a href="Hit_List.html" class="asset-link" style="background: var(--red); color: white;">
                    <span class="icon">??</span> Belgrade Target Hit List <span class="badge" style="background: white; color: var(--red);">VIP</span>
                </a>
                <a href="https://tvui.ru" class="asset-link" target="_blank" style="background: var(--gold); color: var(--navy);">
                    <span class="icon">????</span> tvui.ru Brand Portfolio
                </a>
            </div>
        </div>

        <div class="sector-card">
            <h2 class="sector-title">?? Premium HORECA</h2>
            <p style="font-size: 0.85rem; color: #666; margin-top: -10px;">Salon 1905, Square Nine, Langouste</p>
            <a href="https://GlobalTeamPartners.github.io/salon-1905-demo/" class="asset-link" target="_blank">
                <span class="icon">??</span> Demo: Salon 1905 <span class="badge">LIVE</span>
            </a>
            <a href="#" class="asset-link">
                <span class="icon">??</span> AI Concierge Pitch
            </a>
        </div>

        <div class="sector-card">
            <h2 class="sector-title">??? Real Estate & Dev</h2>
            <p style="font-size: 0.85rem; color: #666; margin-top: -10px;">Belgrade Waterfront, Turaquadra</p>
            <a href="https://GlobalTeamPartners.github.io/belgrade-waterfront-demo/" class="asset-link" target="_blank">
                <span class="icon">??</span> Demo: BG Waterfront <span class="badge">LIVE</span>
            </a>
            <a href="#" class="asset-link">
                <span class="icon">??</span> Lead Qualify AI Pitch
            </a>
        </div>

        <div class="sector-card">
            <h2 class="sector-title">??? Auto Detailing</h2>
            <p style="font-size: 0.85rem; color: #666; margin-top: -10px;">Auto Shine, Black Glass</p>
            <a href="https://GlobalTeamPartners.github.io/auto-shine-demo/" class="asset-link" target="_blank">
                <span class="icon">??</span> Demo: Auto Shine <span class="badge">LIVE</span>
            </a>
            <a href="#" class="asset-link">
                <span class="icon">??</span> Appointment Bot Pitch
            </a>
        </div>

    </div>
</div>

<div class="footer">
    <p>All files are linked locally or to GitHub Pages. Built for the Belgrade Market. © 2026 Unity Spirit Partners & GlobalPlus.</p>
</div>

</body>
</html>
"""

roadmap_md = """
# ?? The "Couples Retreat & Close" Roadmap (Belgrade Edition)
### A romantic October getaway that secretly generates B2B partnerships

> **Mission:** You are in Belgrade with your partner. This trip must feel like a **100% romantic, luxurious European city break**. No clipboards, no hard selling, no stressing her out. You will take her on amazing dates to specific high-target businesses, and drop a casual 30-second "Trojan Horse" pitch while interacting with the manager or owner.

---

## ?? The "Power Couple" Connection Strategy

Being there as a couple is a **massive sales advantage**. High-end European business owners and managers (especially in the Balkans) respect family and relationships. It changes the dynamic from a cold B2B pitch to a warm peer-to-peer conversation.

* **The Strategy:** She enjoys the food, architecture, and service. You pay the bill, praise the establishment, and casually mention the digital gap while pulling out your iPad.
* **The Script:** *"My partner and I absolutely love this place. But as an IT founder from Canada/Russia, I was shocked that a place this premium doesn't have an immersive online presence. I actually had my team build a prototype for you..."*

---

## ?? The 4-Day Romantic Itinerary

### Day 1: Historic Elegance & Michelin Dining
* **Morning (Coffee & Kalemegdan):** Walk around the historic Kalemegdan Fortress. Stop for premium coffee at the **Square Nine Hotel** lobby. 
  * *The Pitch:* While checking out the lobby, mention to the manager how an AI-concierge bot (Alberta) could handle their VIP guests' requests in 3 languages.
* **Evening (Grand Romantic Dinner):** Dress up and head to **Salon 1905** (inside the Geozavod building).
  * *The Pitch:* Enjoy the incredible architecture and food. When the manager comes to check on you, praise the evening. Then slide the iPad across the table: *[Open Salon 1905 Demo]*. "Your physical venue is 10/10. Your digital venue should look like this."

### Day 2: Luxury Real Estate & River Promenade
* **Morning (Sava Promenade & Galerija):** Stroll along the riverfront at **Belgrade Waterfront**. Take your partner shopping at Galerija Mall.
* **Afternoon (The "Casual" Viewing):** Walk into the **Eagle Hills** or **Turaquadra** sales office. Let your partner look at the luxury apartment models.
  * *The Pitch:* Tell the sales director you are an investor and IT owner. *[Open Belgrade Waterfront Demo]*. "If you showed this cinematic scroll to foreign investors, your conversion rate would double. Plus, our AI bots can pre-qualify the leads."
* **Evening (Sunset Dinner):** Take her to **Langouste** for a Michelin-recommended dinner overlooking the river.

### Day 3: Wellness & Premium Auto
* **Morning (Spa & Shopping):** Book a premium spa morning for your partner at a high-end salon or let her explore the boutiques in Dorcol.
* **Lunch (The Detailing Drop-in):** While she is busy, you take a cab to **Auto Shine Detailing** or **Black Glass**.
  * *The Pitch:* "I'm looking to bring my cars here, but honestly your booking system is losing you clients. Look at this." *[Open Auto Shine Demo]*.
* **Evening (Bohemian Quarter):** Walk down Skadarlija street for live traditional music and authentic Serbian food. A purely relaxing evening.

### Day 4: Expat Networking & Wine Tasting
* **Afternoon (Tech Networking):** Drop by a high-end co-working space or IT meetup. Position 	vui.ru as the bridge between Canadian/Russian tech and the Serbian market.
* **Evening (Wine Cellar):** End the trip with a romantic wine tasting at a premium local winery or wine bar (e.g., Ambar). Celebrate a beautiful vacation and the high-ticket B2B leads you just closed.
"""

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Couples Vacation Roadmap - Belgrade</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  body { font-family: 'Inter', sans-serif; background: #1A1A1A; color: #fff; padding: 40px; max-width: 800px; margin: 0 auto; line-height: 1.6; }
  h1, h2, h3 { color: #C5A059; font-family: 'Playfair Display', serif; }
  a { color: #D32F2F; text-decoration: none; font-weight: bold;}
  .btn-back { display: inline-block; margin-bottom: 30px; padding: 10px 20px; background: #D32F2F; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; }
  hr { border-color: rgba(197,160,89,0.2); margin: 30px 0;}
  li { margin-bottom: 10px; }
  blockquote { background: rgba(255,255,255,0.05); padding: 15px; border-left: 4px solid #D32F2F; margin: 0 0 30px 0;}
  strong { color: #fff; }
</style>
</head>
<body>
<a href="Sales_Hub.html" class="btn-back">&larr; Back to Sales Hub</a>
<div id="content"></div>
<script>
  const markdownText = __MARKDOWN__;
  document.getElementById('content').innerHTML = marked.parse(markdownText);
</script>
</body>
</html>
"""

safe_markdown = roadmap_md.replace('', "'").replace('\\', '\\\\')
couples_html = html_template.replace('__MARKDOWN__', safe_markdown)

hitlist_md = """
# ?? Belgrade Target Hit List (VIP)

## ?? Premium HORECA
1. **Salon 1905** - (Demo Prepared)
2. **Square Nine Hotel** - (Pitch AI Concierge)
3. **Langouste** - (Pitch Cinematic Web)

## ??? Real Estate & Developers
1. **Belgrade Waterfront (Eagle Hills)** - (Demo Prepared)
2. **Turaquadra** - (Pitch AI Lead Qualify)

## ??? Premium Services
1. **Auto Shine Detailing** - (Demo Prepared)
2. **Black Glass** - (Pitch AI Booking Bot)
"""
safe_hitlist = hitlist_md.replace('', "'").replace('\\', '\\\\')
hitlist_html = html_template.replace('__MARKDOWN__', safe_hitlist)

with open(os.path.join(kit_dir, "Sales_Hub.html"), "w", encoding="utf-8") as f:
    f.write(sales_hub_html)

with open(os.path.join(kit_dir, "Couples_Roadmap.html"), "w", encoding="utf-8") as f:
    f.write(couples_html)

with open(os.path.join(kit_dir, "Hit_List.html"), "w", encoding="utf-8") as f:
    f.write(hitlist_html)

print("Files generated successfully.")
