import json
import os

import requests

from dotenv import load_dotenv

load_dotenv()

SNULS = os.getenv('SNULS')


default_url = 'https://lists.priem.etu.ru/public/list/'

urls = ['c5e73733-771f-45a0-a55c-9b856ee8dd52']

def get_position_in_university(priority:bool = True):
    req = requests.get(default_url+urls[0]).text

    data = json.loads(req)["data"]

    data_list = data["list"]
    cnt = 0

    for i,el in enumerate(data_list):
        if priority is True and el['priority'] == 1:
            cnt += 1
        if el["code"] == SNULS:
            if priority is True:
                return [cnt,data['competition']]
              
    return None


if __name__ == '__main__':
    print(get_position_in_university())