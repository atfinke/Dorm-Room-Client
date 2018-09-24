import support
import json

path = support.nanoleaf_all_effects_path()

with open(path) as f:
    data = json.load(f)

animations = data["animations"]

effects = []
for animation in animations:
    effects.append(animation["animName"].title())

effects.sort()
effects.append("Flash Twice")
effects.append("Random")

effect_string = ",".join(effects)
print(effect_string)

file = open(support.nanoleaf_published_effects_path(),"w")
file.write(effect_string)
file.close()
