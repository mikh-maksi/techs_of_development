import requests
from bs4 import BeautifulSoup

URL = 'https://www.city.kharkov.ua/uk/novosti.html'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li')
    print(len(items))
    cars = []
    n= 0
    links = []
    for item in items:
        n=n+1
        elem = item.find('a', class_='name')
        if elem:
            elem_out = elem.get_text()
            # print(elem_out)
            # print(elem.get('href'))
            dict1 = {"text":elem.get_text(),"link":elem.get('href')}
            links.append(dict1)
        else:
            elem_out = ''
        descr = item.find('p')
        if descr:
            print(descr.get_text())
    # print(links)
    print(n)
    return cars


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        print('Error')
    print(cars)


parse()
