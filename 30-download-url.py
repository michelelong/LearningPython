#!/usr/local/bin/python3
import urllib.request

# Download a web page
try:
    url = urllib.request.urlopen("https://www.python.org")
    content = url.read()
    url.close()
except:
    print("URL not found.")
    exit()

with open("python.html", "wb") as f:
    f.write(content)

# Download an image
try:
    url = "https://www.python.org/static/img/python-logo@2x.png"
    urllib.request.urlretrieve(url, "python.png")
except:
    print("Image not found.")
    exit()
