import os, requests
urls = {
    "apartheid_museum": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Apartheid_Museum.jpg",
    "soweto": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Vilakazi_Street%2C_Soweto.jpg",
    "lion_walk": "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg"
}
out = "assets/img/custom/destinations"
for name, u in urls.items():
    r = requests.get(u, headers={'User-Agent':'Mozilla/5.0'})
    path = os.path.join(out, name + ".jpg")
    with open(path, 'wb') as f:
        f.write(r.content)
    print(f"Fixed {name}")
