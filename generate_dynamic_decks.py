# -*- coding: utf-8 -*-
import os
import json

kit_dir = r"C:\Users\Vlaslav\Agency_HQ\Belgrade_Sales_Kit"

companies = {
    "HORECA": [
        {"id": "salon-1905", "name": "Salon 1905", "focus": "Historic Michelin-tier dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"id": "square-nine", "name": "Square Nine Hotel", "focus": "Ultra-luxury hospitality & lobby", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"id": "langouste", "name": "Langouste", "focus": "River-view fine dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"id": "buddha-bar", "name": "Buddha-Bar Belgrade", "focus": "Premium nightlife & VIP tables", "price": "Setup: €3,000 | Retainer: €700/mo"},
        {"id": "toro", "name": "Toro Latin GastroBar", "focus": "High-volume premium dining", "price": "Setup: €2,000 | Retainer: €500/mo"},
        {"id": "frans", "name": "Frans", "focus": "Legacy elite Serbian restaurant", "price": "Setup: €3,500 | Retainer: €600/mo"},
        {"id": "ambar", "name": "Ambar", "focus": "Balkan cuisine on the river", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"id": "enso", "name": "Enso", "focus": "Modernist fine dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"id": "legat-1903", "name": "Legat 1903", "focus": "Exclusive wine and dining", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"id": "kalemegdanska", "name": "Kalemegdanska Terasa", "focus": "Huge wedding & event venue", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"id": "metropol", "name": "Metropol Palace Hotel", "focus": "Large luxury hotel & spa", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"id": "hilton", "name": "Hilton Belgrade", "focus": "Rooftop dining (SkyLounge)", "price": "Setup: €3,500 | Retainer: €800/mo"},
        {"id": "saint-ten", "name": "Saint Ten Hotel", "focus": "Boutique luxury hotel", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"id": "hyatt", "name": "Hyatt Regency", "focus": "Corporate & expat hub", "price": "Setup: €5,000 | Retainer: €1,200/mo"},
        {"id": "moskva", "name": "Hotel Moskva", "focus": "Heritage hotel & cafe", "price": "Setup: €4,000 | Retainer: €700/mo"}
    ],
    "Real Estate": [
        {"id": "bw-eagle", "name": "Belgrade Waterfront (Eagle Hills)", "focus": "Massive luxury high-rises", "price": "Setup: €8,000 | Retainer: €2,000/mo"},
        {"id": "turaquadra", "name": "Turaquadra", "focus": "Boutique luxury brokerage", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"id": "west-65", "name": "West 65 / Kula", "focus": "Modern luxury residential tower", "price": "Setup: €6,000 | Retainer: €1,500/mo"},
        {"id": "merin", "name": "Merin Group", "focus": "Premium residential developers", "price": "Setup: €5,000 | Retainer: €1,200/mo"},
        {"id": "afi", "name": "AFI Europe Serbia", "focus": "Premium corporate/residential", "price": "Setup: €6,000 | Retainer: €1,500/mo"},
        {"id": "k-district", "name": "K-District", "focus": "Historic Dorcol redevelopment", "price": "Setup: €4,500 | Retainer: €1,000/mo"},
        {"id": "skyline", "name": "Skyline Belgrade", "focus": "Iconic multi-tower project", "price": "Setup: €5,500 | Retainer: €1,200/mo"},
        {"id": "novi-dorcol", "name": "Novi Dorcol", "focus": "Modern smart-home complex", "price": "Setup: €4,500 | Retainer: €1,000/mo"},
        {"id": "kennedy", "name": "Kennedy Residences", "focus": "High-end New Belgrade flats", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"id": "sothebys", "name": "Sotheby's Serbia", "focus": "Ultra-HNW individual villas", "price": "Setup: €6,000 | Retainer: €1,500/mo"}
    ],
    "Auto & Detailing": [
        {"id": "auto-shine", "name": "Auto Shine Detailing", "focus": "Premium ceramic & PPF", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"id": "black-glass", "name": "Black Glass", "focus": "High-volume tinting & wrap", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"id": "british-motors", "name": "British Motors (JLR)", "focus": "Jaguar & Land Rover sales", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"id": "delta-motors", "name": "Delta Motors (BMW)", "focus": "BMW official dealer", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"id": "star-import", "name": "Star Import (Mercedes)", "focus": "Mercedes-Benz dealer", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"id": "porsche", "name": "Porsche SCG", "focus": "Porsche/Audi premium sales", "price": "Setup: €6,000 | Retainer: €1,200/mo"},
        {"id": "titanium", "name": "Titanium Detailing", "focus": "Niche luxury detailing", "price": "Setup: €1,500 | Retainer: €300/mo"},
        {"id": "auto-finesse", "name": "Auto Finesse SRB", "focus": "Product distribution & studio", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"id": "garage-73", "name": "Garage 73", "focus": "Custom builds & tuning", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"id": "gtechniq", "name": "Gtechniq Serbia", "focus": "Ceramic coating HQ", "price": "Setup: €2,500 | Retainer: €500/mo"}
    ],
    "Medical & Beauty": [
        {"id": "rea-medika", "name": "Rea Medika", "focus": "Premium aesthetic medicine", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"id": "diva-clinic", "name": "Diva Clinic", "focus": "Dermatology & laser clinic", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"id": "vsan", "name": "Vsan Dental", "focus": "Dental tourism for expats", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"id": "dr-magic", "name": "Dr. Magic", "focus": "Plastic surgery portfolio", "price": "Setup: €3,500 | Retainer: €700/mo"},
        {"id": "bel-medic", "name": "Bel Medic (Acibadem)", "focus": "Massive private hospital", "price": "Setup: €8,000 | Retainer: €2,500/mo"},
        {"id": "la-roche", "name": "La Roche Beauty", "focus": "High-end beauty salon", "price": "Setup: €1,500 | Retainer: €300/mo"},
        {"id": "city-spa", "name": "City Spa Retreat", "focus": "Luxury day spa", "price": "Setup: €2,000 | Retainer: €400/mo"},
        {"id": "saruna", "name": "Saruna Wellness", "focus": "Premium hotel wellness chains", "price": "Setup: €3,500 | Retainer: €800/mo"},
        {"id": "dental-plaza", "name": "Dental Plaza", "focus": "High-volume dental clinic", "price": "Setup: €2,500 | Retainer: €500/mo"},
        {"id": "aesthetic-belgrade", "name": "Aesthetic Belgrade", "focus": "Boutique injectables", "price": "Setup: €2,000 | Retainer: €400/mo"}
    ],
    "Luxury Services": [
        {"id": "porto", "name": "Porto Montenegro (BG Office)", "focus": "Yacht and coastal real estate", "price": "Setup: €5,000 | Retainer: €1,200/mo"},
        {"id": "absolut", "name": "Absolut Time (Rolex)", "focus": "Exclusive watch retailer", "price": "Setup: €4,000 | Retainer: €800/mo"},
        {"id": "maestro", "name": "Maestro Jewelers", "focus": "High jewelry", "price": "Setup: €3,000 | Retainer: €600/mo"},
        {"id": "air-serbia", "name": "Air Serbia (VIP Lounge)", "focus": "Premium aviation services", "price": "Setup: €5,000 | Retainer: €1,000/mo"},
        {"id": "yandex", "name": "Yandex VIP Concierge", "focus": "High-end expat services", "price": "Setup: €6,000 | Retainer: €1,500/mo"}
    ]
}

# Add dynamic text based on sector
for sector, items in companies.items():
    for item in items:
        item["sector"] = sector
        if sector == "HORECA":
            item["demo_link"] = "https://globalteampartners.github.io/salon-1905-demo/"
            item["pitch_text"] = f"Deploy a Cinematic Web-portal showcasing the {item['focus']} experience. We then integrate our AI Concierge to manage Russian/English table reservations and VIP deposits automatically."
        elif sector == "Real Estate":
            item["demo_link"] = "https://globalteampartners.github.io/belgrade-waterfront-demo/"
            item["pitch_text"] = f"Deploy a VEO-generated Cinematic Scroll of {item['name']} to emotionally hook foreign investors. Next, we integrate our AI Lead-Qualify Bot to filter out low-budget inquiries."
        elif sector == "Auto & Detailing":
            item["demo_link"] = "https://globalteampartners.github.io/auto-shine-demo/"
            item["pitch_text"] = f"Launch a visually aggressive, mobile-first cinematic site for {item['name']}. We then attach an AI Appointment Setter to take a 20% deposit upfront via Stripe."
        elif sector == "Medical & Beauty":
            item["demo_link"] = "https://globalteampartners.github.io/aesthetic-clinic-demo/"
            item["pitch_text"] = f"Launch a Trust-optimized Cinematic Portfolio highlighting {item['focus']}. Later, we deploy an AI Triage bot to match wealthy expats to the right specialist without front-desk friction."
        else:
            item["demo_link"] = "https://globalteampartners.github.io/salon-1905-demo/"
            item["pitch_text"] = f"Ultra-luxury cinematic showcase for {item['name']}. Bespoke AI Concierge to handle High-Net-Worth Client requests 24/7."

db_json = json.dumps(companies)

# --- ONE PAGER HTML ---
one_pager_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive One-Pager</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
    body { font-family: 'Inter', sans-serif; background: #fff; color: #111; margin: 0; padding: 40px; display: flex; justify-content: center; }
    .page { width: 210mm; min-height: 297mm; background: #fff; box-shadow: 0 0 20px rgba(0,0,0,0.1); padding: 50px; box-sizing: border-box; position: relative; }
    .header { border-bottom: 3px solid #111; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: flex-end; }
    .brand { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: bold; color: #111; }
    .brand span { color: #D32F2F; }
    .date { font-size: 12px; color: #666; font-weight: bold; text-transform: uppercase; }
    h1 { font-family: 'Playfair Display', serif; font-size: 38px; margin: 0 0 10px 0; color: #111; }
    .subtitle { font-size: 16px; color: #D32F2F; font-weight: 600; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 1px; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 40px; }
    .box { background: #f8f9fa; border-left: 4px solid #D32F2F; padding: 25px; border-radius: 0 8px 8px 0; }
    .box h3 { font-family: 'Playfair Display', serif; font-size: 20px; margin-top: 0; color: #111; border-bottom: 1px solid #ddd; padding-bottom: 10px; }
    .box p { font-size: 14px; line-height: 1.6; color: #444; }
    .highlight { font-size: 18px; font-weight: 600; color: #111; margin: 30px 0; padding: 20px; background: #111; color: #fff; text-align: center; border-radius: 8px; }
    .pricing { display: flex; justify-content: space-between; background: #f8f9fa; padding: 20px; border-radius: 8px; font-weight: bold; border: 1px solid #eee; }
    .footer { position: absolute; bottom: 50px; left: 50px; right: 50px; border-top: 1px solid #eee; padding-top: 20px; font-size: 12px; color: #888; display: flex; justify-content: space-between; }
    @media print { body { background: #fff; padding: 0; } .page { box-shadow: none; } }
</style>
</head>
<body>
<div class="page" id="content" style="display:none;">
    <div class="header">
        <div class="brand">GlobalPlus <span>&times;</span> UnitySpirit</div>
        <div class="date">Exclusive Proposal | Q3 2026</div>
    </div>
    <h1 id="c-name">Company Name</h1>
    <div class="subtitle" id="c-focus">Company Focus</div>
    
    <div class="highlight" id="c-pitch">
        Pitch Text Goes Here
    </div>
    
    <div class="grid">
        <div class="box">
            <h3>The Problem</h3>
            <p>Belgrade is experiencing an unprecedented influx of high-net-worth expats. They demand instant, digital, mobile-first experiences. Traditional websites and phone-call bookings are causing severe drop-offs and lost revenue in the premium sector.</p>
        </div>
        <div class="box">
            <h3>Our Solution</h3>
            <p>We deploy a proprietary <strong>Cinematic Scroll Engine</strong> coupled with <strong>AI Concierge infrastructure</strong>. We transform your digital presence into an interactive, high-converting funnel that speaks directly to foreign wealth in their native languages.</p>
        </div>
    </div>
    
    <div class="pricing">
        <div>Phase 1: Quick-Start Deployment</div>
        <div id="c-price" style="color: #D32F2F;">Setup: €X,XXX | Retainer: €XXX/mo</div>
    </div>
    
    <div class="footer">
        <div>Prepared specifically for executive review.</div>
        <div>CONFIDENTIAL</div>
    </div>
</div>

<script>
    const db = """ + db_json + """;
    const urlParams = new URLSearchParams(window.location.search);
    const targetId = urlParams.get('id');
    
    let target = null;
    for (const sector in db) {
        const match = db[sector].find(c => c.id === targetId);
        if (match) target = match;
    }
    
    if (target) {
        document.getElementById('c-name').innerText = "Digital Transformation: " + target.name;
        document.getElementById('c-focus').innerText = target.sector + " | " + target.focus;
        document.getElementById('c-pitch').innerText = target.pitch_text;
        document.getElementById('c-price').innerText = target.price;
        document.getElementById('content').style.display = 'block';
        document.title = target.name + " - One Pager";
    } else {
        document.body.innerHTML = "<h2>Company not found. Please select a company from the Master List.</h2>";
    }
</script>
</body>
</html>"""

# --- PITCH DECK HTML ---
pitch_deck_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interactive Pitch Deck</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
    body { font-family: 'Inter', sans-serif; background: #0A0A0A; color: #fff; margin: 0; overflow: hidden; }
    .slide { width: 100vw; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; position: absolute; top: 0; left: 0; transition: transform 0.5s ease-in-out; text-align: center; padding: 50px; box-sizing: border-box; }
    .slide:not(.active) { transform: translateY(100%); pointer-events: none; }
    .slide.prev { transform: translateY(-100%); }
    h1 { font-family: 'Playfair Display', serif; font-size: 5vw; margin: 0 0 20px 0; color: #C5A059; text-transform: uppercase; letter-spacing: 2px;}
    h2 { font-size: 2vw; color: #fff; font-weight: 300; margin-bottom: 40px; }
    p { font-size: 1.5vw; max-width: 800px; color: #aaa; line-height: 1.6; }
    .btn-demo { margin-top: 40px; padding: 15px 40px; background: #D32F2F; color: white; text-decoration: none; font-size: 1.2vw; font-weight: bold; border-radius: 30px; letter-spacing: 1px; transition: 0.3s; }
    .btn-demo:hover { background: #fff; color: #D32F2F; }
    .nav { position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); display: flex; gap: 20px; z-index: 100; }
    .nav-dot { width: 15px; height: 15px; border-radius: 50%; background: #333; cursor: pointer; transition: 0.3s; }
    .nav-dot.active { background: #C5A059; transform: scale(1.3); }
    .watermark { position: fixed; top: 30px; left: 30px; font-family: 'Playfair Display', serif; font-size: 20px; font-weight: bold; color: rgba(255,255,255,0.2); }
</style>
</head>
<body>
<div class="watermark">GlobalPlus &times; UnitySpirit</div>

<div class="slide active" id="slide0">
    <h2 style="color:#D32F2F; font-weight:bold; letter-spacing: 4px;">EXCLUSIVE PROPOSAL</h2>
    <h1 id="d-name">Company Name</h1>
    <h2 id="d-focus">Sector Focus</h2>
    <p>Swipe or press Space to begin the presentation.</p>
</div>

<div class="slide" id="slide1">
    <h1>The Market Shift</h1>
    <p>Belgrade has fundamentally changed. High-net-worth individuals and international expats now control the premium spending tier. They do not tolerate outdated websites or phone-call reservations.</p>
</div>

<div class="slide" id="slide2">
    <h1>The Solution</h1>
    <p id="d-pitch">Custom Pitch</p>
    <a href="#" id="d-demo" class="btn-demo" target="_blank">LAUNCH LIVE DEMO</a>
</div>

<div class="slide" id="slide3">
    <h1>Partnership Model</h1>
    <h2>Phase 1 & 2 Execution</h2>
    <p id="d-price" style="color: #10B981; font-weight: bold; font-size: 2vw; background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px;">Pricing</p>
    <p style="margin-top: 30px;">We become your fully outsourced tech & marketing unit. Zero headache, maximum conversion.</p>
</div>

<div class="nav">
    <div class="nav-dot active" onclick="goTo(0)"></div>
    <div class="nav-dot" onclick="goTo(1)"></div>
    <div class="nav-dot" onclick="goTo(2)"></div>
    <div class="nav-dot" onclick="goTo(3)"></div>
</div>

<script>
    const db = """ + db_json + """;
    const urlParams = new URLSearchParams(window.location.search);
    const targetId = urlParams.get('id');
    
    let target = null;
    for (const sector in db) {
        const match = db[sector].find(c => c.id === targetId);
        if (match) target = match;
    }
    
    if (target) {
        document.getElementById('d-name').innerText = target.name;
        document.getElementById('d-focus').innerText = target.focus;
        document.getElementById('d-pitch').innerText = target.pitch_text;
        document.getElementById('d-demo').href = target.demo_link;
        document.getElementById('d-price').innerText = target.price;
        document.title = target.name + " - Pitch Deck";
    } else {
        document.getElementById('slide0').innerHTML = "<h1>Company Not Found</h1><p>Please launch this from the Master List.</p>";
    }

    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.nav-dot');

    function goTo(index) {
        slides.forEach((s, i) => {
            s.classList.remove('active', 'prev');
            if (i < index) s.classList.add('prev');
            else if (i === index) s.classList.add('active');
        });
        dots.forEach((d, i) => d.classList.toggle('active', i === index));
        currentSlide = index;
    }

    window.addEventListener('keydown', (e) => {
        if (e.code === 'Space' || e.code === 'ArrowRight') {
            if (currentSlide < slides.length - 1) goTo(currentSlide + 1);
        }
        if (e.code === 'ArrowLeft') {
            if (currentSlide > 0) goTo(currentSlide - 1);
        }
    });
</script>
</body>
</html>"""

with open(os.path.join(kit_dir, "Dynamic_One_Pager.html"), "w", encoding="utf-8") as f: f.write(one_pager_html)
with open(os.path.join(kit_dir, "Dynamic_Pitch_Deck.html"), "w", encoding="utf-8") as f: f.write(pitch_deck_html)

# --- REWRITE MASTER LIST TO INCLUDE LINKS ---
list_html_path = os.path.join(kit_dir, "Comprehensive_Pitches.html")
with open(list_html_path, "r", encoding="utf-8") as f:
    list_html = f.read()

# I will regenerate the table entirely to add the buttons
new_tables_html = ""
for sector, items in companies.items():
    new_tables_html += f"<h2 class='sector-title'>{sector} (50-Company Deep Dive)</h2>\n"
    new_tables_html += "<table><thead><tr><th width='20%'>Company</th><th width='40%'>Pitch & Long-Term Plan</th><th width='20%'>Pricing Offer</th><th width='20%'>Assets</th></tr></thead><tbody>\n"
    for c in items:
        new_tables_html += f"<tr><td><strong>{c['name']}</strong><br><span style='color:#aaa; font-size:0.8rem;'>{c['focus']}</span></td>"
        new_tables_html += f"<td>{c['pitch_text']}</td>"
        new_tables_html += f"<td class='price'>{c['price']}</td>"
        new_tables_html += f"<td><a href='Dynamic_One_Pager.html?id={c['id']}' target='_blank' style='display:block; margin-bottom:5px; background:#fff; color:#111; padding:5px 10px; border-radius:4px; font-size:0.8rem; text-align:center;'>📄 Open One-Pager</a><a href='Dynamic_Pitch_Deck.html?id={c['id']}' target='_blank' style='display:block; background:#D32F2F; color:#fff; padding:5px 10px; border-radius:4px; font-size:0.8rem; text-align:center;'>📊 Open Pitch Deck</a></td></tr>\n"
    new_tables_html += "</tbody></table>\n"

# Replace the old tables in the HTML
start_marker = "<h2 class='sector-title'>"
end_marker = "<script>"
if start_marker in list_html and end_marker in list_html:
    before = list_html.split(start_marker)[0]
    after = end_marker + list_html.split(end_marker)[1]
    final_html = before + new_tables_html + after
    with open(list_html_path, "w", encoding="utf-8") as f:
        f.write(final_html)

print("Dynamic Decks and One-Pagers generated.")
