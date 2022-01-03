import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.cybersport.ru/dota2-rating'

r = requests.get(url)
html = BS(r.content, "html.parser")

for item in html.select(".team__title"):
    element = item.text
    print(element)

