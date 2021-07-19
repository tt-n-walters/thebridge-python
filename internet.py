import requests
import os

print("Downloading...")
url = "https://random.dog/woof"
response = requests.get(url)
image_name = response.text.lower()
print("Downloaded:", image_name)

image_url = "https://random.dog/$$$"
image_url = image_url.replace("$$$", image_name)

print("Downloading image data...")
image_response = requests.get(image_url)

print("Saving image...")
# Step 1, Open file
if image_name.endswith("png"):
    image_file = open("image.png", "wb")
elif image_name.endswith("jpg") or image_name.endswith("jpeg"):
    image_file = open("image.jpg", "wb")
elif image_name.endswith("gif"):
    image_file = open("image.gif", "wb")
elif image_name.endswith("mp4"):
    image_file = open("image.mp4", "wb")
elif image_name.endswith("webm"):
    image_file = open("image.webm", "wb")
else:
    print("Unsupported file type.")
    exit()

# Step 2, Access/Read/Write file
# Step 3, Close file
image_file.write(image_response.content)
image_file.close()

# Automatically open the downloaded file
print("Opening file...")
os.system("start " + image_file.name)