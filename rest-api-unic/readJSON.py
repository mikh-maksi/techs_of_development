import requests


url = 'https://innovations.kh.ua/wp-json/myplugin/v1/author-posts/62'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url,headers=headers)


jsn = r.json()
print(jsn)
# print(jsn[0]['title']['rendered'])
