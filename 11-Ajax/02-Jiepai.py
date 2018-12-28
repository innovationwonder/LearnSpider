import requests
from urllib.parse import urlencode,urlparse
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool

base_url = 'https://www.toutiao.com/search_content/?'

def get_page(page):
    params = {
        'offset' = 60 &
        'format' = json &
        'keyword' = % E8 % A1 % 97 % E6 % 8
        'autoload' = true &
        'count' = 20 &
        'cur_tab' = 1 &
        'from'=search_tab &
        'pd' = synthesis
    }
    try:
        res = requests.get(base_url)
        print('Successful')
        print(res.json())
    except ConnectionError as e:
        print('Error!')
        print(e.args)

# get_page(base_url)