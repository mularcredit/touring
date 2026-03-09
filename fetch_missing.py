import os
import requests
import urllib.parse

missing = {
    "Maasai_Mara": "masai_mara",
    "Malindi": "malindi",
    "Apartheid_Museum": "apartheid_museum",
    "Vilakazi_Street": "soweto",
    "Cradle_of_Humankind": "cradle",
    "Lion_Park": "lion_walk"
}

out_dir = "assets/img/custom/destinations"
os.makedirs(out_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

for title, filename in missing.items():
    filepath = os.path.join(out_dir, f"{filename}.jpg")
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=1200"
    try:
        r = requests.get(url, headers=headers).json()
        pages = r['query']['pages']
        img_url = None
        for pid, info in pages.items():
            if 'thumbnail' in info:
                img_url = info['thumbnail']['source']
                break
        
        if img_url:
            print(f"Downloading {filename} from {img_url}")
            img_r = requests.get(img_url, headers=headers)
            if img_r.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(img_r.content)
                print(f"OK: {filename}")
            else:
                print(f"Failed {filename} status {img_r.status_code}")
        else:
            print(f"No thumbnail for {title}")
    except Exception as e:
        print(f"Error {title}: {e}")
