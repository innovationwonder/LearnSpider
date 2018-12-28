import requests
import re
import json

def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    return res.text

def parse_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a></p>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i></p>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            '排名': item[0],
            '封面': item[1],
            '标题': item[2],
            '主演': item[3].strip(),
            '上映时间': item[4].strip()[5:],
            '评分': item[5] + item[6],
        }


def save(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n') # 实现字典的序列化，并保持中文编码


def main(offset):
    base_url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(base_url)
    parse_page(html)
    for i in parse_page(html):
        print(i)
        save(i)


if __name__ == '__main__':
    for i in range(10):
        main(offset = i*10)
