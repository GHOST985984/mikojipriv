import json

import requests

from . import exceptions

base_url = "https://9anime.dev"


class client:
    def init():
        pass

    def search(anime_name):
        r = requests.get(base_url + "/anime?search=" + anime_name)
        if r.status_code == 404:
            raise exceptions.NotFound("Not Found.")
        elif r.status_code != 200:
            raise Exception(r.content)
        return json.loads(json.dumps(r.json(), indent=4))


version = "1.0.0"
