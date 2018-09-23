import os
from nanoleaf import setup

def nanoleaf_ip_path():
    return "./support/nanoleaf_ip_path.txt"

def nanoleaf_token_path():
    return "./support/nanoleaf_token_path.txt"

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

def config():
    address_list = setup.find_auroras()
    print(address_list)

    if len(address_list) > 0:
        addresss = address_list[0]
        token = setup.generate_auth_token(addresss)

        file = open(nanoleaf_ip_path(),"w")
        file.write(addresss)
        file.close()

        file = open(nanoleaf_token_path(),"w")
        file.write(token)
        file.close()

if __name__ == '__main__':
    support_directory = "./support"
    if not os.path.exists(support_directory):
        os.makedirs(support_directory)

    config()
