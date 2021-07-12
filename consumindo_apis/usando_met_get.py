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


get_healthcheck()
