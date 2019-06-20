import json


def getnext(parsing, substr):
    return parsing.replace(substr, "")


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def conv_time(timestr):
    parse = timestr.split(":")
    if len(parse) == 2:
        timestr = "0:" + timestr
    return get_sec(timestr)


def get_time(parsing):
    time = parsing.split(' ')[0]
    try:
        secs = conv_time(time)
        return (secs, getnext(parsing, time + " "))
    except Exception:
        return (None, None)


def get_caller(parsing):
    caller = parsing.split(":")[0]
    return (caller, getnext(parsing, caller + ": "))


def get_location(parsing):
    location = parsing.split(":")[0]
    return (location, getnext(parsing, location + ": "))


def get_subjects(parsing):
    return parsing.split(",")


def process_line(line):
    clip = {}
    clip['time'], next = get_time(line)
    if (clip['time']) is None:
        return None
    clip['caller'], next = get_caller(next)
    clip['location'], next = get_location(next)
    clip['subjects'] = get_subjects(next)
    return clip


def process_description(description):
    clips = []
    for line in description.split('\n'):
        if line != "":
            processed = process_line(line)
            if processed is not None:
                clips.append(processed)
        else:
            return clips


def get_hosts(title):
    spl = title.split(" ")
    first = ""
    second = ""
    for i in range(0, len(spl)):
        if spl[i] == "with":
            first += spl[i+1]
            if (spl[i+2] != "and" or spl[i+2] != "&"):
                first += " " + spl[i+2]
        if spl[i] == "and" or spl[i] == "&":
            second += spl[i+1]
            if (i+2 < len(spl)):
                second += " " + spl[i+2]
            return (first, second)
    return (first, second)


with open('descriptions.json', 'r') as f:
    data = json.load(f)


added_item = []
for video in data:
    processed = process_description(
        video["items"][0]["snippet"]["description"])
    cleaned_video = {}
    if processed is not None and processed != []:
        cleaned_video["processed_description"] = processed
        cleaned_video["title"] = video["items"][0]["snippet"]["title"]
        cleaned_video["videoId"] = video["items"][0]["id"]
        cleaned_video["publishedAt"] = \
            video["items"][0]["snippet"]["publishedAt"]
        try:
            main_host, second_host = get_hosts(cleaned_video["title"])
        except IndexError as e:
            print(f'{e} for: {cleaned_video["title"]}')
        if main_host == "":
            print(f'{cleaned_video["title"]} | {cleaned_video["videoId"]}')
        else:
            print(f'Main: {main_host} Second: {second_host}')
        cleaned_video["main_host"] = main_host
        cleaned_video["second_host"] = second_host
        added_item.append(cleaned_video)

with open('processed.json', 'w') as f:
    json.dump(added_item, f)
# description = data[0]["items"][0]["snippet"]["description"]
# clips = process_description(description)
# for clip in clips:
#     print(f'{clip}')
# print(f'{data[0]}')
# clip = process_line(line)
# print(f'{clip}')
