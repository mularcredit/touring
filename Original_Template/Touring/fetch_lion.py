import os, requests
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/640px-Lion_waiting_in_Namibia.jpg"
out = "assets/img/custom/destinations/lion_walk.jpg"
r = requests.get(url)
with open(out, 'wb') as f:
    f.write(r.content)
print("Saved lion_walk.jpg")
