html = """
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
"""
from pyquery import PyQuery as pq
import requests

# 初始化
doc = pq(html)
# print(doc)
print(doc('li')) # 选择所有的 li 节点
doc = pq(url='https://cuiqingcai.com') # 先请求 URL 用得到的 HTML 内容完成初始化
doc = pq(requests.get('https://cuiqingcai.com').text) # 功能同上
# print(doc('title'))
doc = pq(filename='demo.html') # 读取文件
# print(doc('ul'))
print('------------')
doc = pq(html)
# print(doc)
print(doc('#container .list li')) # 先选取 id 为 container 的节点，再选取内部 class为 list 的节点内 的 li 节点
lis = doc('.list').find('a') # 选取 class 为 list 的节点，查咋内部的所有 子孙a 节点
print('-----------')
lis = doc('.list').children() # 只查找子节点，
lis = doc('.list').children('.active') # 筛选class 为 List 的节点中 class 为 active 的节点
container = doc('.list').parent() # 获取直接父节点
print(doc('.list').parents()) # 获取祖先节点
print('兄弟节点')
print(doc('.list .item-0.active').siblings()) # class 为 list 内 class 为 item-0 和 active 的节点的兄弟节点（它以外的其他同级节点）
print(doc('.list .item-0.active').siblings('.active')) # 在其中筛选 class 为 active的节点
print(str(doc('.list .item-0.active').siblings('.active'))) # 添加 str() 结果同上
print('遍历')
for i in doc('li').items():
    print(i) # 逐个获取 li 节点

print('获取属性')
print(doc('.item-0.active a').attr('href'))
print(doc('.item-0.active a').attr.href) # 同上
print('选中多个节点时：')
print(doc('a').attr('href')) # 只返回第一个结果
print('遍历获取所有节点的属性')
for i in doc('a').items():
    print(i.attr('href'))

print('获取文本 text()')
print(doc('.item-0.active a').text()) # 只返回纯文本内容
print(doc('.item-0.active a').html()) # a 节点内的 HTML文本
print('多个节点时')
print(doc('li').html()) # 只返回第一个 ,需要遍历获取后续
print(doc('li').text()) # 返回多个，不需要遍历

print('节点操作')
# print(doc('.item-0.active').remove_class('active')) # 移除该节点内的 active 的 属性
# print(doc('.item-0.active').remove_class('active').add_class('active')) # 添加该节点内的 active 的 属性
print('修改节点内容')
li = doc('.item-0.active')
print(li)
li.attr('name', 'abc') # 在 li 节点内增加 name 属性 为 abc
print(li)
li.text('changed abc') # 替换 li 节点内部的文本（包括子标签）
print(li)
li.html('<span class="bold">changed item</span>') # 替换节点内部的标签
print(li)

print('提取内部文本')
text2 = """
<div class="wrap">
Hello, World
<p>This is a paragraph,</p>
</div>
"""
doc2 = pq(text2)
# print(doc)
wrap = doc2('.wrap')
print(wrap.text())
wrap.find('p').remove() # 移除 节点 p
print(wrap.text())

print('伪类选择器')
print(doc('li:first-child')) # 第一个 li 节点
print(doc('li:last-child')) # 最后一个
print(doc('li:nth-child(2)')) # 第二个
print(doc('li:gt(2)')) # 第三个之后的
print(doc('li:nth-child(2n)')) # 偶数位置的
print(doc('li:contains(second)')) # 包含 second 文本的
# print(lis)
# print(container)