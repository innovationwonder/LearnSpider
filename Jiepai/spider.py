import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def get_page(offset):
    '''请求'''
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params) # 构造完整 URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    '''获取图片 URL 链接'''
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('open_url'):
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    yield {
                        'image': 'https:' + image.get('url'),
                        'title': title
                    }


def save_image(item):
    '''保存图片到文件夹'''
    # 创建 img 文件夹
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            # 创建图集文件夹 并以 MD5 命名各图片文件
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(response.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB 成功', result)
        return True
    return False


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)
        save_to_mongo(item)


GROUP_START = 0
GROUP_END = 7


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()