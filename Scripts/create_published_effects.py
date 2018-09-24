import support
import json

effects = support.get_all_effect_names()

effects.sort()
effects.append("Flash Twice")
effects.append("Random")

effect_string = ",".join(effects)
print(effect_string)

file = open(support.nanoleaf_published_effects_path(),"w")
file.write(effect_string)
file.close()
