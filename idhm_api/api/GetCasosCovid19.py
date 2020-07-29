import json

import requests


def pegaCasosCovid(municipio, uf):
    url = "https://brasil.io/api/dataset/covid19/caso_full/data/"

    querystring = {"format": "json", "city": municipio, "state": uf}

    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    if not response["results"]:
        response = []
        return response
    return response


if __name__ == "__main__":
    print(pegaCasosCovid("sao pedro de alcantara", "sc"))
