import requests

request_params = {'lang': 'en','n':''}
towns = ['London', 'SVO', 'Cherepovets']
for town in towns:
    try:
        url_for_request = f'http://wttr.in/{town}'
        response = requests.get(url_for_request, request_params)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as error:
                exit(f'Неудается загрузить данные: {error}')