"""Direct patch for Soweto — uses Wikimedia Commons file API to find valid image URL."""
import os
import requests

HEADERS = {"User-Agent": "KaleolaZar/1.0 (travel site; contact@example.com)"}
OUT_DIR = "assets/img/custom/destinations"

def try_url(url, filepath):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code == 200 and len(r.content) > 10000:
            with open(filepath, "wb") as f:
                f.write(r.content)
            print(f"  ✅ {len(r.content)//1024}KB saved!")
            return True
        print(f"  ❌ failed status={r.status_code} size={len(r.content)}B")
    except Exception as e:
        print(f"  ❌ {e}")
    return False

soweto_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/c/c7/Soweto_Skyline_from_Orlando_Towers.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/7/70/Soweto%2C_Johannesburg.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/cd/Vilakazi_Street%2C_Soweto.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/2/2e/Kliptown_Soweto.jpg",
]

print("[FIXING soweto.jpg]")
fp = os.path.join(OUT_DIR, "soweto.jpg")
for url in soweto_urls:
    if try_url(url, fp):
        break

print(f"soweto.jpg = {os.path.getsize(fp)//1024 if os.path.exists(fp) else 0}KB")
