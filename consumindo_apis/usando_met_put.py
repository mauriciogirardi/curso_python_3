import json
import requests

URL_BASE = 'http://localhost:5000'


def get_healthcheck():
    endpoint = 'healthcheck'

    response = requests.get(url=f'{URL_BASE}/{endpoint}')
    status_code = response.status_code

    if status_code == 200:
        content = response.json()
        print(content['message'])


def get_technology():
    endpoint = 'technology'
    response = requests.get(url=f'{URL_BASE}/{endpoint}')
    status_code = response.status_code

    if status_code == 200:
        content = response.json()
        print(content['message'])


def post_technology(technology, level):
    endpoint = 'technology'
    header = {'Content-type': 'application/json'}
    data = {"level": level}

    response = requests.post(url=f'{URL_BASE}/{endpoint}/{technology}', headers=header, data=json.dumps(data))
    status_code = response.status_code

    if status_code == 201:
        content = response.json()
        print(content)
    else:
        print(response.text)


def put_technology(technology, level):
    endpoint = 'technology'
    header = {'Content-type': 'application/json'}
    data = {"level": level}

    response = requests.put(url=f'{URL_BASE}/{endpoint}/{technology}', headers=header, data=json.dumps(data))
    status_code = response.status_code

    if status_code == 200:
        content = response.json()
        print(content)
    else:
        print(response.text)