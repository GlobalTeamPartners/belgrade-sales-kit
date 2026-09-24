# -*- coding: utf-8 -*-
import os

kit_dir = r"C:\Users\Vlaslav\Agency_HQ\Belgrade_Sales_Kit"
hub_path = os.path.join(kit_dir, "Sales_Hub.html")

with open(hub_path, "r", encoding="utf-8") as f:
    html = f.read()

# I will add a new sector card for "Medical & Beauty"
new_card = """        <div class="sector-card">
            <h2 class="sector-title">💉 Medical & Beauty</h2>
            <p style="font-size: 0.85rem; color: #666; margin-top: -10px;">Rea Medika, Diva Clinic, Vsan</p>
            <a href="https://GlobalTeamPartners.github.io/aesthetic-clinic-demo/" class="asset-link" target="_blank">
                <span class="icon">🌐</span> Demo: Aesthetic Clinic <span class="badge">LIVE</span>
            </a>
            <a href="#" class="asset-link">
                <span class="icon">🤖</span> AI Privacy Booking Bot
            </a>
        </div>"""

if "Medical & Beauty" not in html:
    # Insert it right before the auto detailing card or anywhere in the grid
    target = '<div class="sector-card">\n            <h2 class="sector-title">🏎️ Auto Detailing</h2>'
    html = html.replace(target, new_card + '\n\n' + target)
    
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Hub updated with Medical & Beauty Demo")
else:
    print("Already added")
