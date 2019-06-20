import json

count = 0
clean = []
with open('processed.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    # print(f'{data[0]["processed_description"]}')
    for video in data:
        count += 1
        cdata = video["processed_description"]
        cdata["title"] = video["items"][0]["snippet"]["title"]
        # cdata["videoId"] = video["videoId"]
        print(f'{cdata["title"]}')

print(f'Parsed {count} videos')
# count = 0
# with open('descriptions.json', 'r') as jsonfile:
#     data = json.load(jsonfile)
#     print(f'{data[0]["items"][0]["snippet"]["description"]}')
# with open('descriptions.json', 'r') as jsonfile:
#     data = json.load(jsonfile)
#     for response in data:
#         print(f'{response[]}')
