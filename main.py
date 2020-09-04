import requests

request_params = {'lang': 'ru','n':''}
towns = ['Лондон', 'Шереметьево', 'Череповец']
for town in towns:
    try:
        url_for_request = f'http://wttr.in/{town}'
        response = requests.get(url_for_request, request_params)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as error:
                print(f'Неудается загрузить данные: {error}')