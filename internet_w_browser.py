import requests
import os

print("Downloading...")
url = "https://random.dog/woof"
response = requests.get(url)

image_url = 'start "" "https://random.dog/$$$" '
image_url = image_url.replace("$$$", response.text)

print("Opening image...")
os.system(image_url)
