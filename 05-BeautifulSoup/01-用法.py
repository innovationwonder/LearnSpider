html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story" name="Once upon a time htere were htree little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><!--Lacie--></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><!--Tillie--></a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html, 'lxml') # 完成BeautifulSoup对象的初始化，传入带解析的 HTML，自动进行补全
print(soup)
print(soup.prettify()) # 以标准缩进格式输出 待解析的HTML
print(soup.title.string) # title 节点的文本内容

# 节点选择器
## 选择元素
print(type(soup.title))
print(soup.title)
print(soup.head)
print(soup.p) # 这种方式只能获取第一个匹配的节点

## 提取信息
### 获取名称
print(soup.title.name) # title 节点名称
### 获取属性
print(soup.p.attrs) # 获取 p 节点的所有属性
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])
### 获取 内容
print(soup.p.string)


## 嵌套选择
print(soup.head.title)
print(soup.head.title.string)

## 关联选择 先选中一个节点，再选择它的子节点、父节点、兄弟节点
print()
print(soup.p.contents)
print(soup.p.children)
for i in soup.p.children:
    print(i)
print(soup.p.descendants)
for i in soup.p.descendants:
    print(i)

print(soup.a.parent) # a 节点的直接父节点
# print(soup.a.parents)
print('-------------')
print(list(enumerate(soup.a.parents))) # a 节点的所有祖先节点
print('兄弟节点')
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print(list(soup.a.parents)[0].attrs['class'])

## 方法选择器
# find_all()
print(soup.find_all(name='ul')) # 查询所有 ul 节点，返回列表
print(soup.find_all(attrs={'id': 'list-1'})) # 查询 id 为 list-1 的节点
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))
print(soup.find_all(text=re.compile('story'))) # 返回所有匹配正则表达式的节点文本组成的列表

# find() 返回第一个匹配的节点
print(soup.find(name='ul'))
print(soup.find(class_='list'))

# CSS选择器
print(soup.select('ul li')) # 选择 ul 节点下的所有 li 节点
print('---------')
for i in soup.select('p'):
    print(i.select('a'))
    print(i['class']) # 获取属性
    print(i.attrs['class'])
    print(i.get_text())
    print(i.string)


