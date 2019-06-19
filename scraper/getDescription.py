import requests
import json

with open('secret.json', 'r') as f:
    data = json.load(f)
    SECRET = data["secret"]

print(f'Secret: {SECRET}')
URL = "https://www.googleapis.com/youtube/v3"
ENDPOINT = "/videos"


def getDesc(videoId):
    PARAMS = {
        "part": "snippet",
        "id": videoId,
        "key": SECRET,
    }
    ENDPOINT = "/videos"
    return requests.get(url=URL+ENDPOINT, params=PARAMS).json()


desc = []
count = 0
with open('videos.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    for response in data:
        id = response["contentDetails"]["videoId"]
        res = getDesc(id)
        desc.append(res)
        print(f'count: {count} out of {len(data)}')
        count += 1

with open('descriptions.json', 'w') as outfile:
    json.dump(desc, outfile)
