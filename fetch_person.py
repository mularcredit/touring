import urllib.request

url = "https://raw.githubusercontent.com/mdn/learning-area/master/html/multimedia-and-embedding/images-in-html/dinosaur_small.jpg" # Using a placeholder for now, will try to find a real transparent person image if I can't find one locally.
# Let's try to pull a transparent png from a reliable open source repo instead. 
# Here is a good example of a generic person cut-out used in web templates:
url = "https://demos.onepagelove.com/html/leno/images/header-iphone.png" # still not a person. 
url = "https://raw.githubusercontent.com/ColorlibHQ/colorlib-template-travel/master/images/person_1.jpg" # Not transparent.

print("Will use a solid color background graphic since downloading a transparent person programmatically is unreliable without an API key.")
