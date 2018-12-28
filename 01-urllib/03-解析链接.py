# 1.urlparse() 将 URL 分为 6部分
# scheme 协议, netloc=域名, path=访问路径, params=参数, query=查询条件, fragment=锚点 用于直接定位页面内部的下拉位置
from urllib.parse import urlparse
url = 'http://www.baidu.com/index.index;user?id=5#comment'
# url = 'http://www.baidu.com/index.index.html#comment'
result = urlparse(url, allow_fragments=False)
# result = urlparse(url)
# print(type(result))
print(result) # ParseResult 是一个元组，剋以通过下标/.属性名 获取元素
# print(result.scheme, result[0], result.netloc, result[1], sep='\n')

# 2.urlunparse() 接收一个长度为 6 的可迭代对象，拼接 URL
from urllib.parse import urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

# 3.urlsplit() 不单独解析 params，而是整合到 path 中
from urllib.parse import urlsplit
result = urlsplit(url)
print(result) # 元祖类型

# 4.urlunsplit() 传入长度为5 的可迭代对象
from urllib.parse import urlunsplit
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))

# 5.urljoin() 拼接整合 URL
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))

# 6.urlencode() 将字典参数转化为 GET 请求参数
from urllib.parse import urlencode
params = {
    'abc':2312,
    'saw':22
}
base_url = url + urlencode(params)
print(base_url)

# 7.parse_qs() 反序列化，GET 请求的参数转换为 字典参数
from urllib.parse import parse_qs
query = 'name=mike&age=21'
print(parse_qs(query))

# 8.parse_qsl()  将参数转换为 元祖组成的列表
from urllib.parse import parse_qsl
query = 'name=mike&age=21'
print(parse_qsl(query))

# 9.quote() 将内容转换为 URL 编码格式 如中文
from urllib.parse import quote
keyword = '你好'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

# 10.unquote() 进行 URL 解码
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD'
print(unquote(url))