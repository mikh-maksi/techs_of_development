import requests, json
url = 'https://innovations.kh.ua/tech/max1/post.php'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
dt = {'some_data':'Hello'}
r = requests.post(url, headers = headers, data = dt)

print(r.text)
string = str(r.text)


# print(string)

# jsn = json.loads(string)

# print(jsn.get('cafes')[0].get('Name'))