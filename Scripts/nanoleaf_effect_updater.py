import os
from nanoleaf import setup
from nanoleaf import Aurora
import support

def update_effect(effect_name):
    aurora = Aurora(support.get_nanoleaf_ip(), support.get_nanoleaf_token())
    aurora.on = True

    if effect_name == "Random\n":
        effect_name = aurora.effect_random()
        aurora.effect = effect_name
        return "Random - " + effect_name
    elif effect_name == "Flash Twice":
        aurora.identify()
    else:
        aurora.effect = effect_name

    return effect_name
