"""
High-quality image scraper for Kaleola Zar destinations.
Uses Wikimedia Commons API to search for the best available images.
Forces re-download of all broken / corrupt images.
"""
import os
import requests
import time
import re

OUT_DIR = "assets/img/custom/destinations"
os.makedirs(OUT_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "KaleolaZar/1.0 (educational travel site; contact@example.com)"
}

# For each destination, specify multiple candidate Wikipedia article titles and the local filename.
# We also supply a direct Wikimedia Commons fallback URL for guaranteed premium imagery.
DESTINATIONS = [
    {
        "name": "hells_gate",
        "wiki_titles": ["Hell's Gate National Park"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Gorge_at_Hell%27s_Gate_National_Park%2C_Kenya.jpg/1280px-Gorge_at_Hell%27s_Gate_National_Park%2C_Kenya.jpg"
    },
    {
        "name": "naivasha",
        "wiki_titles": ["Lake Naivasha"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/LakeNaivashaKenya.jpg/1280px-LakeNaivashaKenya.jpg"
    },
    {
        "name": "elementaita",
        "wiki_titles": ["Lake Elmenteita"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Lake_Elementaita.jpg/1280px-Lake_Elementaita.jpg"
    },
    {
        "name": "nakuru",
        "wiki_titles": ["Lake Nakuru"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Lake_Nakuru_flamingoes.jpg/1280px-Lake_Nakuru_flamingoes.jpg"
    },
    {
        "name": "masai_mara",
        "wiki_titles": ["Maasai Mara"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Wildebeest_herds_in_the_Masai_Mara.jpg/1280px-Wildebeest_herds_in_the_Masai_Mara.jpg"
    },
    {
        "name": "diani",
        "wiki_titles": ["Diani Beach"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Diani_Beach_Ukunda_Kenya.jpg/1280px-Diani_Beach_Ukunda_Kenya.jpg"
    },
    {
        "name": "malindi",
        "wiki_titles": ["Malindi"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Malindi_beach.JPG/1280px-Malindi_beach.JPG"
    },
    {
        "name": "watamu",
        "wiki_titles": ["Watamu"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Watamu_beach.jpg/1280px-Watamu_beach.jpg"
    },
    {
        "name": "apartheid_museum",
        "wiki_titles": ["Apartheid Museum"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Apartheid_Museum.jpg/1280px-Apartheid_Museum.jpg"
    },
    {
        "name": "constitution_hill",
        "wiki_titles": ["Constitution Hill, Johannesburg"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/ConstitutionCourt.jpg/1280px-ConstitutionCourt.jpg"
    },
    {
        "name": "mandela_square",
        "wiki_titles": ["Nelson Mandela Square"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Nelson_Mandela_Square%2C_Sandton.jpg/1280px-Nelson_Mandela_Square%2C_Sandton.jpg"
    },
    {
        "name": "soweto",
        "wiki_titles": ["Soweto", "Vilakazi Street"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Soweto_township.jpg/1280px-Soweto_township.jpg"
    },
    {
        "name": "mandela_house",
        "wiki_titles": ["Mandela House"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Orlando_West%2C_8115_Vilakazi_Street_-_Nelson_Mandela%27s_house.jpg/1280px-Orlando_West%2C_8115_Vilakazi_Street_-_Nelson_Mandela%27s_house.jpg"
    },
    {
        "name": "cradle",
        "wiki_titles": ["Cradle of Humankind"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Maropeng_Visitor_Centre.jpg/1280px-Maropeng_Visitor_Centre.jpg"
    },
    {
        "name": "lion_walk",
        "wiki_titles": ["Lion Park, South Africa"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/1280px-Lion_waiting_in_Namibia.jpg"
    },
    {
        "name": "dinokeng",
        "wiki_titles": ["Dinokeng Game Reserve"],
        "commons_fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Dinokeng_Game_Reserve_-_rhinos.jpg/1280px-Dinokeng_Game_Reserve_-_rhinos.jpg"
    },
]

def check_broken(filepath):
    """Return True if file doesn't exist or is clearly broken (too small)."""
    if not os.path.exists(filepath):
        return True
    size = os.path.getsize(filepath)
    return size < 5000  # anything under 5KB is broken

def wiki_thumb(title, size=1280):
    """Try to get thumbnail URL from Wikipedia page images API."""
    import urllib.parse
    url = (f"https://en.wikipedia.org/w/api.php"
           f"?action=query&titles={urllib.parse.quote(title)}"
           f"&prop=pageimages&format=json&pithumbsize={size}")
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        data = r.json()
        pages = data["query"]["pages"]
        for pid, info in pages.items():
            if "thumbnail" in info:
                return info["thumbnail"]["source"]
    except Exception as e:
        print(f"  [WIKI API ERR] {title}: {e}")
    return None

def download(url, filepath):
    """Download an image URL to filepath. Returns True on success."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        ct = r.headers.get("content-type", "")
        if r.status_code == 200 and ("image" in ct or len(r.content) > 5000):
            with open(filepath, "wb") as f:
                f.write(r.content)
            size_kb = len(r.content) // 1024
            print(f"  ✅ Downloaded {size_kb}KB")
            return True
        else:
            print(f"  ❌ Bad response: status={r.status_code}, ct={ct}, size={len(r.content)}")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    return False

def commons_search(keyword, size=1280):
    """Search Wikimedia Commons for a freely-licensed high-res image."""
    import urllib.parse
    url = (f"https://commons.wikimedia.org/w/api.php"
           f"?action=query&generator=search&gsrnamespace=6"
           f"&gsrsearch={urllib.parse.quote(keyword)}"
           f"&gsrlimit=5&prop=imageinfo&iiprop=url|size|mediatype"
           f"&iiurlwidth={size}&format=json")
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        data = r.json()
        pages = data.get("query", {}).get("pages", {})
        candidates = []
        for pid, info in pages.items():
            ii = info.get("imageinfo", [])
            if ii:
                item = ii[0]
                mt = item.get("mediatype", "")
                if mt in ("BITMAP", ""):
                    thumb = item.get("thumburl") or item.get("url")
                    w = item.get("thumbwidth", 0)
                    candidates.append((w, thumb))
        if candidates:
            candidates.sort(reverse=True)
            return candidates[0][1]
    except Exception as e:
        print(f"  [COMMONS SEARCH ERR] {keyword}: {e}")
    return None

print("=" * 60)
print("Kaleola Zar — High-Quality Image Scraper")
print("=" * 60)

for dest in DESTINATIONS:
    name = dest["name"]
    filepath = os.path.join(OUT_DIR, f"{name}.jpg")
    is_broken = check_broken(filepath)

    if not is_broken:
        size_kb = os.path.getsize(filepath) // 1024
        print(f"[SKIP] {name} ({size_kb}KB — already OK)")
        continue

    print(f"\n[PROCESSING] {name}")
    success = False

    # Step 1: Try Wikipedia page thumbnail API for each article title
    for title in dest["wiki_titles"]:
        print(f"  → Wikipedia API: '{title}'")
        img_url = wiki_thumb(title)
        if img_url:
            print(f"  → Found: {img_url[:80]}...")
            if download(img_url, filepath):
                success = True
                break
        time.sleep(0.5)

    # Step 2: If Step 1 failed, try Commons keyword search
    if not success:
        keyword = dest["wiki_titles"][0]
        print(f"  → Commons search: '{keyword}'")
        img_url = commons_search(keyword)
        if img_url:
            print(f"  → Found: {img_url[:80]}...")
            success = download(img_url, filepath)

    # Step 3: Hardcoded fallback URL (direct Wikimedia Commons)
    if not success and dest.get("commons_fallback"):
        print(f"  → Trying hardcoded fallback URL...")
        success = download(dest["commons_fallback"], filepath)

    if not success:
        print(f"  ⚠️  FAILED to get image for {name}")

    time.sleep(1.2)

print("\n" + "=" * 60)
print("Scraping complete! Checking final results:")
print("=" * 60)
for dest in DESTINATIONS:
    name = dest["name"]
    filepath = os.path.join(OUT_DIR, f"{name}.jpg")
    if os.path.exists(filepath):
        size_kb = os.path.getsize(filepath) // 1024
        status = "✅" if size_kb > 5 else "❌ BROKEN"
        print(f"  {status} {name}: {size_kb}KB")
    else:
        print(f"  ❌ MISSING {name}")
