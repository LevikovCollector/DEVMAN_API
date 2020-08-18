import requests

lang = {'lang': 'ru'}
towns = ['Лондон', 'Шереметьево', 'Череповец']
try:
    for town in towns:
        url_for_request = f'http://wttr.in/{town}'
        response = requests.get(url_for_request, lang)
        response.raise_for_status()
        print(response.text)
except requests.exceptions.HTTPError as error:
    exit(f'Неудается загрузить данные: {error}')