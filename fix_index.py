import os
import glob

kit_dir = r"C:\Users\Vlaslav\Agency_HQ\Belgrade_Sales_Kit"

# 1. Rename Sales_Hub.html to index.html if it exists
sales_hub_path = os.path.join(kit_dir, "Sales_Hub.html")
index_path = os.path.join(kit_dir, "index.html")

if os.path.exists(sales_hub_path):
    # If an index.html already exists, remove it first
    if os.path.exists(index_path):
        os.remove(index_path)
    os.rename(sales_hub_path, index_path)
    print("Renamed Sales_Hub.html to index.html")

# 2. Update all internal links across all HTML files
html_files = glob.glob(os.path.join(kit_dir, "*.html"))
for f_path in html_files:
    with open(f_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Sales_Hub.html" in content:
        content = content.replace("Sales_Hub.html", "index.html")
        with open(f_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated links in {os.path.basename(f_path)}")
