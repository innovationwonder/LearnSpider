# urllib.request.urlopen（url，data = None，[ timeout，] *，cafile = None，capath = None，cadefault = False，context = None
import urllib.request
response1 = urllib.request.urlopen('https://www.baidu.com') # 请求网页
# print(response1.getheaders()) # 打印请求头
# print(response1.getheader('Server')) # 打印请求头的服务器信息

# data 参数
import urllib.request
import urllib.parse
# 使用 urllib.parse 模块里的 urlencode() 将参数字典转换为字符串
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response2 = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response2.read())

# timeout 参数
import urllib.request

response = urllib.request.urlopen('http://httpbin.org', timeout=2)
# print(response.read())


# Request 对象 构造请求
from urllib import request, parse
url = "http://httpbin.org/post"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Host": 'httpbin.org'
}
dict = {
    'name': 'Mike'
}
data = bytes(parse.urlencode(dict), encoding='utf8') # 表单数据

req = request.Request(url=url, data=data, headers=headers, method='POST')
req = request.Request(url=url, data=data, method='POST')
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
)
response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# 获取 Cookie
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

# 将 cookie 保存到文件
filename = 'cookie_LWP.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename) # LWP 格式
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 读取 已保存的 cookie
# print('读取已保存的 cookie---------------')
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie_LWP.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
