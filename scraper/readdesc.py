import json

count = 0
with open('processed.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    # print(f'{data[0]["processed_description"]}')
    for video in data:
        count += 1
        print(f'{video["processed_description"]}')

print(f'Parsed {count} videos')
# count = 0
# with open('descriptions.json', 'r') as jsonfile:
#     data = json.load(jsonfile)
#     print(f'{data[0]["items"][0]["snippet"]["description"]}')
# with open('descriptions.json', 'r') as jsonfile:
#     data = json.load(jsonfile)
#     for response in data:
#         print(f'{response[]}')
