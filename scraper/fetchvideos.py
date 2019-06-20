import requests
import json

URL = "https://www.googleapis.com/youtube/v3"
channelId = "UCprs0DXUS-refN1i8FkQkdg"
uploadPlaylist = "UUprs0DXUS-refN1i8FkQkdg"


with open('secret.json', 'r') as f:
    data = json.load(f)
    SECRET = data["secret"]


def getVidoes(nextPage):
    PARAMS = {
        "key": SECRET,
        "part": "contentDetails",
        "playlistId": uploadPlaylist,
        "maxResults": 50,
        # "channelId": channelId,
        # "forUsername": "TheAtheistExperience",
    }
    if (nextPage):
        PARAMS["pageToken"] = nextPage
    ENDPOINT = "/playlistItems"
    return requests.get(url=URL+ENDPOINT, params=PARAMS).json()


res = getVidoes('')
nextPage = res['nextPageToken']

videos = []
for response in res['items']:
    videos.append(response)

count = 0
while(nextPage):
    print(f'Calling page: {nextPage}')
    res = getVidoes(nextPage)
    try:
        nextPage = res["nextPageToken"]
    except KeyError:
        print(f'Retrieved last page')
        nextPage = ""
    for response in res["items"]:
        videos.append(response)
    print(f'appended: {count}')
    count += 1


with open('videos.json', 'w') as outfile:
    json.dump(videos, outfile)
