# 模拟 Ajax 请求，爬取前 10 页 微博
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
import requests
import json

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    parmas = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page,
    }
    url = base_url + urlencode(parmas)

    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue # 跳过
            else:
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['内容'] = pq(item.get('text')).text()
                weibo['点赞统计'] = item.get('attitudes_count')
                weibo['评论统计'] = item.get('comments_count')
                weibo['转发统计'] = item.get('reposts_count')
                weibo['创建日期'] = item.get('created_at')
                yield weibo


client = MongoClient()
db = client['Weibo']
collection = db['Weibo']


def save(result):
    if collection.insert(result):
        print('Save to Mongo')


if __name__ == '__main__':
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save(result)