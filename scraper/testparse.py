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
        secs = get_sec(time)
        return (secs, getnext(parsing, time + " "))
    except Exception as e:
        print(f'Exception: {e} for : {time}')
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


with open('descriptions.json', 'r') as f:
    data = json.load(f)


added_item = []
for video in data:
    processed = process_description(video["items"][0]["snippet"]["description"])
    if processed is not None and processed != []:
        video["processed_description"] = processed
        added_item.append(video)

with open('processed.json', 'w') as f:
    json.dump(added_item, f)
# description = data[0]["items"][0]["snippet"]["description"]
# clips = process_description(description)
# for clip in clips:
#     print(f'{clip}')
# print(f'{data[0]}')
# clip = process_line(line)
# print(f'{clip}')
