import ast
import os

import support

from nanoleaf import setup

if __name__ == '__main__':
    support.prepare_directory()

    address_list = setup.find_auroras()
    print(address_list)

    if len(address_list) > 0:
        addresss = address_list[0]
        token = setup.generate_auth_token(addresss)

        if token:
            file = open(support.nanoleaf_ip_path(),"w")
            file.write(addresss)
            file.close()

            file = open(support.nanoleaf_token_path(),"w")
            file.write(token)
            file.close()
