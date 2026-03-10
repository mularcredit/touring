"""Try getting Soweto image via Wikimedia Commons image info (thumb URL) which bypasses the 403."""
import os
import requests
import urllib.parse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Referer": "https://en.wikipedia.org/"
}
OUT_DIR = "assets/img/custom/destinations"

def get_thumb(filename, width=1200):
    """Get a thumbnail URL from Commons imageinfo API — avoids the 403."""
    url = (f"https://en.wikipedia.org/w/api.php?action=query"
           f"&titles=File:{urllib.parse.quote(filename)}"
           f"&prop=imageinfo&iiprop=url&iiurlwidth={width}"
           f"&format=json")
    r = requests.get(url, headers=HEADERS)
    data = r.json()
    pages = data.get("query", {}).get("pages", {})
    for pid, info in pages.items():
        ii = info.get("imageinfo", [])
        if ii:
            return ii[0].get("thumburl") or ii[0].get("url")
    return None

# Known exact Commons filenames for Soweto
filenames = [
    "Soweto_Skyline_from_Orlando_Towers.jpg",
    "Kliptown_Soweto.jpg",
    "Soweto,_South_Africa-2014_photo-Frerk_Meyer-CC_BY-SA.jpg",
    "Soweto_Joburg_SA.jpg",
]

fp = os.path.join(OUT_DIR, "soweto.jpg")
print("[Trying Commons thumb URLs for Soweto]")
for fn in filenames:
    print(f"  → {fn}")
    thumb = get_thumb(fn)
    if thumb:
        print(f"    → thumb: {thumb[:80]}")
        r = requests.get(thumb, headers=HEADERS, timeout=20)
        if r.status_code == 200 and len(r.content) > 10000:
            with open(fp, "wb") as f:
                f.write(r.content)
            print(f"    ✅ Saved! {len(r.content)//1024}KB")
            break
        else:
            print(f"    ❌ status={r.status_code} size={len(r.content)}")
    else:
        print("    no thumb returned")

size = os.path.getsize(fp) if os.path.exists(fp) else 0
print(f"\nFinal soweto.jpg: {size//1024}KB")
