import json

count = 0
with open('videos.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    for response in data:
        id = response["contentDetails"]["videoId"]
        print(f'{id}')
        count += 1

print(f'Video Number: {count}')
