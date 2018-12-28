from urllib import request,error

# 对访问不存在的页面进行异常处理
# try:
#     res = request.urlopen('https://cuiqingcai.com/index.htm')
# # 先捕获子类的错误，再捕获父类的异常
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)

# reason 属性返回的不是字符串是对象的情况
import socket
try:
    res = request.urlopen('https://www.baidu.com', timeout=0.01)
except error.URLError as e:
    print(e.reason)
    print(type(e.reason))
    # 使用 isinstance() 判断异常类型与预期是否符合
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')