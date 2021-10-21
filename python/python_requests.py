import requests, json
url = 'https://innovations.kh.ua/hse/back/back/hrs.php'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
r = requests.get(url, headers = headers)

# print(r.text)
string = str(r.text)


# print(string)

jsn = json.loads(string)

print(jsn[0].get('name'))