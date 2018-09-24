import os
import json

def directory():
    return os.path.expanduser("~/Library/Application Support/Dorm Room Client/")

def nanoleaf_ip_path():
    return directory() + "nanoleaf_ip.txt"

def nanoleaf_token_path():
    return directory() + "nanoleaf_token.txt"

def nanoleaf_all_effects_path():
    return directory() + "nanoleaf_all_effects.txt"

def nanoleaf_published_effects_path():
    return directory() + "nanoleaf_published_effects.txt"

def last_issue_time_path():
    return directory() + "last_issue_time.txt"

def last_issue_number_path():
    return directory() + "last_issue_number.txt"

def get_nanoleaf_ip():
    path = nanoleaf_ip_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

def get_nanoleaf_token():
    path = nanoleaf_token_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

def get_all_effect_names():
    path = nanoleaf_all_effects_path()

    with open(path) as f:
        data = json.load(f)

    animations = data["animations"]

    effects = []
    for animation in animations:
        effects.append(animation["animName"])
    return effects

def get_published_effects():
    path = nanoleaf_published_effects_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

def get_last_issue_time():
    path = last_issue_time_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

def get_last_issue_number():
    path = last_issue_number_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

def prepare_directory():
    print(directory())
    if not os.path.exists(directory()):
        os.makedirs(directory())
