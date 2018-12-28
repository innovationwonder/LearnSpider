import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
html = requests.get(url, headers=headers).text
doc = pq(html)
# print(doc)
items = doc('.explore-tab .feed-item').items()
for i in items:
    # print(i)
    question = i.find('h2').text()
    # print(question)
    author = i.find('.author-link-line').text()
    # print(author)
    answer = pq(i.find('.content').html()).text() # 只提取文本，pq(i.find('...).html()).text()
    print(answer)

    file = open('result.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n'+'='*50+'\n')
    file.close()

#