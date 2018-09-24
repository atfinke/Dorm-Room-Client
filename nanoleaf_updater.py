import os
from nanoleaf import setup
from nanoleaf import Aurora

def nanoleaf_ip_path():
    return "./support/nanoleaf_ip.txt"

def nanoleaf_token_path():
    return "./support/nanoleaf_token.txt"

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


def update_effect(effect_name):
    aurora = Aurora(get_nanoleaf_ip(), get_nanoleaf_token())
    aurora.on = True

    if effect_name == "Random":
        aurora.effect = my_aurora.effect_random()
    elif effect_name == "Flash Twice":
        aurora.identify()
    else:
        aurora.effect = effect_name
