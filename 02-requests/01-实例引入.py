import requests

# r = requests.get('https://www.baidu.com')
data = {
    'name': 'Mike',
    'age':21
}
r = requests.post('https://httpbin.org/post', data=data)
print(r.text)
# print(r.json()) # 将JSON字符串 转化为字典

# 抓取网页
import re
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
# print(r.text)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
# print(titles)

# 抓取二进制数据
r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

