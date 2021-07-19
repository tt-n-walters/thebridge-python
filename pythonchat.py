import requests

url = "https://tt-python-chat.herokuapp.com/"

response = requests.get(url)
if response.status_code != 200:
    print("Download error.", response.status_code)
    exit()

# Registering 
# register_link = url + "register"
# data = { "user": "nico.walters" }
# response = requests.post(register_link, data)
# if response.status_code != 200:
#     print("Error while registering user.", response.status_code)
#     print(response.text)
#     exit()
# else:
#     print("Registered successfully.")


# Sending a message
send_link = url + "send"
data = { "user": "nico.walters", "message": "Just nod if you can hear me." }
response = requests.post(send_link, data)
if response.status_code != 200:
    print("Error while sending message.", response.status_code)
    print(response.text)
    exit()
else:
    print("Sent message succesfully.")