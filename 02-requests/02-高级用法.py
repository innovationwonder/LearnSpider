# 文件上传
import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)

# cookies
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for k, v in r.cookies.items():
#     print(k+"="+v)

# 会话维持
import requests
s = requests.Session()
# s.get('URL```````')

# Prepared Request
from requests import Request, Session
url = 'http://httpbin.org/post'
data = {
    'name': 'Mike',
    'age':21
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)