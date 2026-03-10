import os
import re
from duckduckgo_search import DDGS
import requests
import time

missing = [
    ("Masai Mara wildlife safari", "masai_mara"),
    ("Malindi Kenya beach resort", "malindi"),
    ("Apartheid Museum Johannesburg exterior", "apartheid_museum"),
    ("Soweto Vilakazi Street bright", "soweto"),
    ("Cradle of Humankind landscape", "cradle"),
    ("Lion Walk Experience South Africa safari", "lion_walk")
]

out_dir = "assets/img/custom/destinations"
os.makedirs(out_dir, exist_ok=True)

with DDGS() as ddgs:
    for query, filename in missing:
        filepath = os.path.join(out_dir, f"{filename}.jpg")
        if os.path.exists(filepath): continue
        print(f"Fetching {query}...")
        try:
            results = ddgs.images(query, max_results=3)
            for r in results:
                url = r.get('image')
                if not url: continue
                try:
                    resp = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                    if resp.status_code == 200 and 'image' in resp.headers.get('content-type', ''):
                        with open(filepath, 'wb') as f:
                            f.write(resp.content)
                        print(f"Saved {filename}")
                        break
                except Exception:
                    pass
        except Exception as e:
            print(f"DDGS failed {e}")
        time.sleep(2)

print("Images downloaded.")

# Now replace the HTML
html_path = "index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    "Hell's Gate National Park": "hells_gate",
    "Lake Naivasha": "naivasha",
    "Lake Elementaita": "elementaita",
    "Lake Nakuru National Park": "nakuru",
    "Masai Mara": "masai_mara",
    "Diani Beach": "diani",
    "Malindi": "malindi",
    "Watamu": "watamu",
    "Apartheid Museum": "apartheid_museum",
    "Constitution Hill": "constitution_hill",
    "Nelson Mandela Square": "mandela_square",
    "Soweto Vilakazi Street": "soweto",
    "Nelson Mandela House": "mandela_house",
    "Cradle of Humankind": "cradle",
    "Lion Walk Experience": "lion_walk",
    "Dinokeng Game Reserve": "dinokeng"
}

import re
for alt, filename in replacements.items():
    # Regex to catch src="assets/img/custom/package1.png" alt="Lake Naivasha"
    # We will just replace it simply
    pattern = r'src="assets/img/custom/package[1-3]\.png" alt="' + re.escape(alt) + r'"'
    repl = f'src="assets/img/custom/destinations/{filename}.jpg" alt="{alt}"'
    html = re.sub(pattern, repl, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML updated!")
