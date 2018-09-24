import json
import os
from nanoleaf import setup
from nanoleaf import Aurora

def nanoleaf_ip_path():
    return "./support/nanoleaf_ip.txt"

def nanoleaf_token_path():
    return "./support/nanoleaf_token.txt"

def nanoleaf_effects_path():
    return "./support/nanoleaf_effects.txt"

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

def network_config():
    address_list = setup.find_auroras()
    print(address_list)

    if len(address_list) > 0:
        addresss = address_list[0]
        token = setup.generate_auth_token(addresss)

        if not token:
            return

        file = open(nanoleaf_ip_path(),"w")
        file.write(addresss)
        file.close()

        file = open(nanoleaf_token_path(),"w")
        file.write(token)
        file.close()

def effect_config():
    my_aurora = Aurora(get_nanoleaf_ip(), get_nanoleaf_token())
    details = my_aurora.effect_details_all()

    print(json.dumps(details, sort_keys=True, indent=4))

    file = open(nanoleaf_effects_path(),"w")
    file.write(str(details))
    file.close()

if __name__ == '__main__':
    support_directory = "./support"
    if not os.path.exists(support_directory):
        os.makedirs(support_directory)

    network_config()
    # effect_config()
