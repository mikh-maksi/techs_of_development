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
    # print(items)
    cars = []
    # el = items.find('a', class_='name')
    n= 0
    for item in items:
        n=n+1
        elem = item.find('a', class_='name')
        if elem:
            elem_out = elem.get_text()
            print(elem_out)
        else:
            elem_out = ''
        # print(elem_out)
    #     uah_price = item.find('span', class_='size15')
    #     if uah_price:
    #         uah_price = uah_price.get_text().replace(' • ', '')
    #     else:
    #         uah_price = 'Цену уточняйте'
    #     cars.append({
    #         'title': item.find('div', class_='na-card-name').get_text(strip=True),
    #         'link': HOST + item.find('span', class_='link').get('href'),
    #         'usd_price': item.find('strong', class_='green').get_text(),
    #         'uah_price': uah_price,
    #         'city': item.find('svg', class_='svg_i16_pin').find_next('span').get_text(),
    #     })
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
