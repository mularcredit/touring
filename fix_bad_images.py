"""
Fix the 3 bad images: Dinokeng (map), Masai Mara (AI silhouette), Soweto (AI street).
Uses Wikipedia imageinfo API with browser user-agent to get the working thumbnail CDN URLs.
"""
import requests
import os
import urllib.parse

OUT_DIR = "assets/img/custom/destinations"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

def wiki_article_thumb(title, size=1200):
    """Get the main image thumbnail from a Wikipedia article."""
    url = (f"https://en.wikipedia.org/w/api.php?action=query"
           f"&titles={urllib.parse.quote(title)}"
           f"&prop=pageimages&pithumbsize={size}&format=json&pilicense=any")
    r = requests.get(url, headers=HEADERS, timeout=15)
    pages = r.json().get("query", {}).get("pages", {})
    for pid, info in pages.items():
        if "thumbnail" in info:
            return info["thumbnail"]["source"]
    return None

def wiki_image_thumb(filename, size=1200):
    """Get a thumbnail URL for a specific Wikimedia Commons file."""
    url = (f"https://en.wikipedia.org/w/api.php?action=query"
           f"&titles=File:{urllib.parse.quote(filename)}"
           f"&prop=imageinfo&iiprop=url&iiurlwidth={size}"
           f"&format=json")
    r = requests.get(url, headers=HEADERS, timeout=15)
    pages = r.json().get("query", {}).get("pages", {})
    for pid, info in pages.items():
        ii = info.get("imageinfo", [])
        if ii:
            return ii[0].get("thumburl") or ii[0].get("url")
    return None

def download(url, filepath):
    """Download URL to filepath, return True on success."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=25, stream=True)
        ct = r.headers.get("content-type", "")
        data = b"".join(r.iter_content(8192))
        if r.status_code == 200 and len(data) > 20000 and ("image" in ct or data[:4] in (b'\xff\xd8\xff\xe0', b'\xff\xd8\xff\xe1', b'\x89PNG')):
            with open(filepath, "wb") as f:
                f.write(data)
            print(f"    ✅  {len(data)//1024}KB saved")
            return True
        print(f"    ❌  status={r.status_code} size={len(data)} ct={ct}")
    except Exception as e:
        print(f"    ❌  {e}")
    return False

# ---- Fix Dinokeng ----
print("\n[DINOKENG] Fetching real wildlife photo...")
fp = os.path.join(OUT_DIR, "dinokeng.jpg")
success = False

# Dinokeng has very sparse Wikipedia coverage so let's use a good wildlife shot
# from the actual Dinokeng article or a nearby wildlife alternative
for title, desc in [
    ("Dinokeng Game Reserve", "Dinokeng article"),
    ("White rhinoceros", "White rhino"),
    ("African elephant", "African elephant"),
    ("Kruger National Park", "Kruger (similar biome)"),
]:
    print(f"  → Try article: {desc}")
    url = wiki_article_thumb(title, 1200)
    if url:
        print(f"    → thumb: {url[:80]}")
        if download(url, fp):
            success = True
            break

if not success:
    # Direct known Wikimedia Commons files for Dinokeng
    for fname in [
        "Afrikaner_bull_at_Dinokeng_Game_Reserve.jpg",
        "Dinokeng.jpg",
        "White_Rhino_Waiting.jpg",
        "African_white_rhino_and_calf.jpg",
    ]:
        print(f"  → Direct file: {fname}")
        url = wiki_image_thumb(fname, 1200)
        if url:
            print(f"    → {url[:80]}")
            if download(url, fp):
                break

# ---- Fix Masai Mara ----
print("\n[MASAI MARA] Fetching real wildlife migration photo...")
fp = os.path.join(OUT_DIR, "masai_mara.jpg")
success = False

for title, desc in [
    ("Maasai Mara", "Masai Mara article"),
    ("Great Migration", "Great migration"),
    ("Wildebeest", "Wildebeest migration"),
]:
    print(f"  → Try article: {desc}")
    url = wiki_article_thumb(title, 1200)
    if url:
        print(f"    → thumb: {url[:80]}")
        if download(url, fp):
            success = True
            break

if not success:
    for fname in [
        "Wildebeest_herds_in_the_Masai_Mara.jpg",
        "Wildebeest_calves_take_to_the_Mara.jpg",
        "Masai_Mara_lion.jpg",
        "Maasai_Mara_Masai_Mara_National_Reserve_landscape.jpg",
    ]:
        print(f"  → Direct file: {fname}")
        url = wiki_image_thumb(fname, 1200)
        if url:
            print(f"    → {url[:80]}")
            if download(url, fp):
                break

# ---- Fix Soweto ----
print("\n[SOWETO] Fetching real Vilakazi Street / Soweto photo...")
fp = os.path.join(OUT_DIR, "soweto.jpg")
success = False

for title, desc in [
    ("Soweto", "Soweto article"),
    ("Vilakazi Street", "Vilakazi Street article"),
    ("Hector Pieterson Museum", "Hector Pieterson"),
]:
    print(f"  → Try article: {desc}")
    url = wiki_article_thumb(title, 1200)
    if url:
        print(f"    → thumb: {url[:80]}")
        if download(url, fp):
            success = True
            break

if not success:
    for fname in [
        "Orlando_Towers,_Soweto.jpg",
        "Vilakazi_Street.jpg",
        "Mandela_and_Tutu_houses_in_Soweto.jpg",
        "HectorPietersonMemorial.jpg",
        "Hector_Pieterson_Memorial,_Soweto.jpg",
    ]:
        print(f"  → Direct file: {fname}")
        url = wiki_image_thumb(fname, 1200)
        if url:
            print(f"    → {url[:80]}")
            if download(url, fp):
                break

# Final report
print("\n=== Final sizes ===")
for name in ["dinokeng", "masai_mara", "soweto"]:
    fp = os.path.join(OUT_DIR, f"{name}.jpg")
    size = os.path.getsize(fp)//1024 if os.path.exists(fp) else 0
    status = "✅" if size > 20 else "❌ BROKEN"
    print(f"  {status} {name}: {size}KB")
