import requests
import json

with open('secret.json', 'r') as f:
    data = json.load(f)
    SECRET = data["secret"]

print(f'Secret: {SECRET}')
URL = "https://www.googleapis.com/youtube/v3"
ENDPOINT = "/videos"

PARAMS = {
    "part": "snippet",
    "id": "3ZMBWRINkcQ",
    "key": SECRET,
}

# PARAMS['key'] = "AIzaSyBAQA3mesfSqYEPz-9S0q-vKIhm739vBwY"

r = requests.get(url=URL+ENDPOINT, params=PARAMS)
print(f'{r}')
items = r.json()["items"]
for item in items:
    print(f'Title: {item["snippet"]["description"]}')
