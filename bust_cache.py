import re

html_path = 'c:/Users/HomePC/Downloads/Touring/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace src="assets/img/custom/destinations/filename.jpg" with ?v=2
content = re.sub(r'src="assets/img/custom/destinations/([^"]+?\.jpg)(?:\?v=\d+)?"', r'src="assets/img/custom/destinations/\1?v=2"', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cache busted")
