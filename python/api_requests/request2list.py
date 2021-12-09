import requests


url = 'https://innovations.kh.ua/wp-json/wp/v2/posts/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


url = 'https://innovations.kh.ua/wp-json/wp/v2/places'
url = 'https://innovations.kh.ua/wp-json/wp/v2/art'
# url = 'https://innovations.kh.ua/wp-json/wp/v2/request'


r = requests.get(url,headers=headers)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

jsn = r.json()


# print(jsn)
print(jsn[0]['title']['rendered'])
print(jsn[0]['content']['rendered'])


# print(jsn[0]['acf']['type'])
# print(jsn[0]['acf']['name'])
# print(jsn[0]['acf']['description'])

types = []

for j in jsn:
    types.append(j['acf']['type'])

print(types)

# print(jsn[0]['title']['rendered'])
# print(jsn[0]['content']['rendered'])
# print(jsn[0]['acf']['adress'])
# print(jsn[0]['acf']['money'])
# print(jsn[0]['acf']['addtext'])
# print(jsn)
