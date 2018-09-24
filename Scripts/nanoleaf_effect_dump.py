import ast
import json
import os

import support

from nanoleaf import Aurora

if __name__ == '__main__':
    support.prepare_directory()

    aurora = Aurora(support.get_nanoleaf_ip(), support.get_nanoleaf_token())
    details = aurora.effect_details_all()

    print(json.dumps(details, sort_keys=True, indent=4))
    data = json.dumps(ast.literal_eval(str(details)))

    file = open(support.nanoleaf_all_effects_path(),"w")
    file.write(data)
    file.close()
