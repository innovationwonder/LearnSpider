from lxml import etree
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactice"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link1.html">fifth item</a>
</ul>
</div>
"""

html = etree.HTML(text) # 初始化 构造 XPath 解析对象,
result = etree.tostring(html) # 输出修正后的 HTML
print(result.decode('utf-8')) # bytes 类型转 str

# 直接读取文本进行解析
html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html) # 输出修正后的 HTML
result = html.xpath('//*') # * 表示所有节点
result = html.xpath('//li') #  所有li节点
result = html.xpath('//li/a') #  li节点所有直接 a 子节点
result = html.xpath('//li//a') #  li节点所有 子孙 a 节点
result = html.xpath('//ul//a') #  / 用于获取 直接子节点， // 用于 子孙节点
result = html.xpath('//a[@href="link4.html"]/../@class') # @ 表示属性， 选中href属性为 link4.html 的 a 节点 ..用于获取父节点，再获取 class 属性
result = html.xpath('//a[@href="link4.html"]/parent::*/@class') # parent:: 也用于获取父节点
result = html.xpath('//li[@class="item-0"]') # class 属性为 item-0 的 li 节点
result = html.xpath('//li[@class="item-0"]/text()') # text() 用于获取节点中的文本 结果为空，li 节点的直接子节点都是 a 节点，文本是 a 节点内部
result = html.xpath('//li[@class="item-0"]//text()') # 返回结果3个，前两个是 li 子节点 a 节点内部的文本，最后一个是 li节点内部的文本，\n
result = html.xpath('//li[@class="item-0"]/a/text()') # 不包括最后的换行符
result = html.xpath('//li/a/@href') # 获取所有 li 节点下 所有 a 节点的 Href 属性
result = html.xpath('//li[@class="li"]/a/text()') # 属性有多个值时 无法进行匹配
result = html.xpath('//li[contains(@class,"li")]/a/text()') # 通过contains()方法 传入属性名 和属性值 完成匹配 用于 class 属性 有多个的情况
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()') # 根据多属性确定一个节点，需要同时匹配多个属性 使用 and

# 按序选择
result = html.xpath('//li[1]/a/text()') # 第一个
result = html.xpath('//li[last()]/a/text()') # 最后一个
result = html.xpath('//li[position()<3]/a/text()') # 前两个节点
result = html.xpath('//li[last()-2]/a/text()') # 倒数第三个 li 节点

# 节点轴选择
result= html.xpath('//li[1]/ancestor::*') # ancestor:: 获取素有祖先节点，*表示匹配所有节点，--> 第一个 li 节点的 所有祖先节点
result= html.xpath('//li[1]/ancestor::div') # 只获取 div 这个祖先节点
result= html.xpath('//li[1]/attribute::*') # 第一个 li 节点的 所欲属性值
result= html.xpath('//li[1]/child::a[@href="link1.html"]') # child 轴，获取所有直接子节点，再限定选取 href 属性
result= html.xpath('//li[2]/descendant::span') # descendant 轴，获取所有子孙节点，再限定选取 span节点
result= html.xpath('//li[2]/following::*[2]') # descendant 轴，获取所有子孙节点，再限定选取 span节点
result= html.xpath('//li[2]/following-sibling::*') # following-sibling 轴，获取当前节点之后的所有同级节点，再* 获取了后续所有同级节点

print(result)
# print(result[0])
# print(result.decode('utf-8')) # bytes 类型转 str

