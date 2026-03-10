import os
import requests
import urllib.parse
import time
import json

destinations = [
    ("Hell's_Gate_National_Park", "hells_gate"),
    ("Lake_Naivasha", "naivasha"),
    ("Lake_Elmenteita", "elementaita"),
    ("Lake_Nakuru", "nakuru"),
    ("Maasai_Mara", "masai_mara"),
    ("Diani_Beach", "diani"),
    ("Malindi", "malindi"),
    ("Watamu", "watamu"),
    ("Apartheid_Museum", "apartheid_museum"),
    ("Constitution_Hill,_Johannesburg", "constitution_hill"),
    ("Nelson_Mandela_Square", "mandela_square"),
    ("Vilakazi_Street", "soweto"),
    ("Mandela_House", "mandela_house"),
    ("Cradle_of_Humankind", "cradle"),
    ("Lion_Park", "lion_walk"),
    ("Dinokeng_Game_Reserve", "dinokeng")
]

out_dir = "assets/img/custom/destinations"
os.makedirs(out_dir, exist_ok=True)

def get_wiki_image(title):
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=1200"
        r = requests.get(url, headers={'User-Agent': 'Touring/1.0 (test)'})
        data = r.json()
        pages = data['query']['pages']
        for page_id, info in pages.items():
            if 'thumbnail' in info:
                return info['thumbnail']['source']
    except Exception as e:
        print(f"Error fetching wiki meta for {title}: {e}")
    return None

def download_image(url, filepath):
    try:
        r = requests.get(url, headers={'User-Agent': 'Touring/1.0 (test)'}, timeout=15)
        if r.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            return True
    except Exception as e:
        pass
    return False

for title, file_name in destinations:
    filepath = os.path.join(out_dir, f"{file_name}.jpg")
    print(f"Processing {title}...")
    
    img_url = get_wiki_image(title)
    if img_url:
        print(f" -> Found image: {img_url}")
        if download_image(img_url, filepath):
            print(f" -> [SUCCESS] Downloaded to {file_name}.jpg")
        else:
            print(" -> [FAILED] Download error")
    else:
        print(f" -> [FAILED] No wiki thumbnail found")
    time.sleep(1)

print("Wiki Scraping complete!")
