import requests
from bs4 import BeautifulSoup as BS
import json

i = 2
while True:
    url = f'https://www.cybersport.ru/blog/popular/page/{i}'
    response = requests.get(url)
    data = response.json()
    if data['nextPageUri'] is None:
        break
    print(f'Page: {i}:')
    html = BS(data['list'], 'html.parser')
    for item in html.select('article'):
        res = ''
        name = item.select('.revers')
        author = item.select('strong')
        res += 'Название: ' + name[len(name) - 1].text + '\nАвтор:    ' + author[0].text
        count = item.select('.rating-counter__count')
        res += '\nРейтинг:  ' + count[0].text +'\n\n'

        try:
            print(res)
        except UnicodeEncodeError:
            print(res.encode('utf-8'))
    print()
    i += 1


