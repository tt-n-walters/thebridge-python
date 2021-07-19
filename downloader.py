import requests

print("Enter url to download:")
url = input(">>  ")

print("Enter filename to save:")
filename = input(">>  ")


# Download the url
print("Downloading...")
response = requests.get(url)

# Check the download succeeded
if not response.status_code == 200:
    print("Download error.")
    exit()
print("Download successful.")

# Open, write, close file
print("Saving to file...")
file = open(filename, "wb")
file.write(response.content)
file.close()
print("Saved successfully.")
