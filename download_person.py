import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urls = [
    "https://pngimg.com/uploads/tourist/tourist_PNG29.png",
    "https://pngimg.com/d/tourist_PNG29.png",
    "https://pngimg.com/uploads/man/man_PNG6530.png",
    "https://freepngimg.com/thumb/business_man/4-2-business-man-transparent.png",
    "https://www.freeiconspng.com/uploads/tourist-png-15.png",
    "https://www.transparentpng.com/thumb/man/smiling-man-png-transparent-image--8.png",
    "https://upload.wikimedia.org/wikipedia/commons/a/a2/Portrait_of_a_woman_with_a_transparent_background.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Portr%C3%A4t_Johannes_Kepler_transparent_background.png/500px-Portr%C3%A4t_Johannes_Kepler_transparent_background.png",
    "https://upload.wikimedia.org/wikipedia/commons/e/e0/Placeholder_person.png"
]

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
out_path = "c:\\Users\\HomePC\\Downloads\\Touring\\assets\\img\\custom\\premium_person.png"

for url in urls:
    try:
        print(f"Trying {url}...")
        req = urllib.request.Request(url, headers={'User-Agent': user_agent, 'Accept': 'image/png'})
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = response.read()
                # Simple check if it's actually a PNG
                if data.startswith(b'\x89PNG'):
                    with open(out_path, 'wb') as out_file:
                        out_file.write(data)
                    print(f"Success! Downloaded from {url}")
                    break
                else:
                    print("Not a valid PNG file.")
    except Exception as e:
        print(f"Failed: {e}")
