import requests, os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36',
    'Referer': 'https://en.wikipedia.org/'
}

# Use Commons Special:Redirect which follows to the actual CDN URL
urls = [
    'https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Soweto_Skyline_from_Orlando_Towers.jpg&width=1200',
    'https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Kliptown_Soweto.jpg&width=1200',
    'https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Soweto%2C_Johannesburg.jpg&width=1200',
    'https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Vilakazi_Street_2.jpg&width=1200',
]

fp = 'assets/img/custom/destinations/soweto.jpg'

for url in urls:
    print(f'Trying: {url[:80]}')
    try:
        r = requests.get(url, headers=headers, timeout=20, allow_redirects=True)
        ct = r.headers.get('content-type', '')
        print(f'  Status: {r.status_code}, Size: {len(r.content)//1024}KB, CT: {ct}')
        if r.status_code == 200 and len(r.content) > 30000 and 'image' in ct:
            with open(fp, 'wb') as f:
                f.write(r.content)
            print(f'  SUCCESS! Saved {len(r.content)//1024}KB')
            break
    except Exception as e:
        print(f'  Error: {e}')

print(f'Final size: {os.path.getsize(fp)//1024}KB' if os.path.exists(fp) else 'File missing')
