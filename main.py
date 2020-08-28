import requests

language_response = {'lang': 'ru'}
towns = ['Лондон', 'Шереметьево', 'Череповец']
try:
    for town in towns:
        url_for_request = f'http://wttr.in/{town}?n'
        response = requests.get(url_for_request, language_response)
        response.raise_for_status()
        print(response.text)
except requests.exceptions.HTTPError as error:
    exit(f'Неудается загрузить данные: {error}')