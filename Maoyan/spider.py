import json
import re
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException

def get_page(url):
    '''请求网页'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        # 通过响应状态码判断 response 的返回结果
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse(html):
    '''解析'''
    pattern = re.compile('<dd>.*?board-index.*?>(\d+).*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a></p>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                          +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)

    # 提取信息
    for item in items:
        yield {
            '排名': item[0],
            '封面': item[1],
            '标题': item[2],
            '主演': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '评分': item[5]+item[6],
        }

def save_to_txt(content):
    '''保存到 TXT 文件'''
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n') # 将字典形式的转换为字符串

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)

    for item in parse(html):
        print(item)
        save_to_txt(item)


if __name__ == '__main__':
    # 抓取 0~90页
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])