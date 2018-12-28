# json.loads() 将 JSON 字符串转换为 JSON 对象
# json.dumps() 将 JSON 对象转换为 文本字符串

import json
# json 数据必须使用 双引号包围，否则 loads() 方法会解析失败
str = '''
[{
    "name": "Mike",
    "gender": "male",
    "day": "1992-05-15"
},
{
    "name":"Aob",
    "gender": "Female",
    "day": "1992-01-21"
}]
'''
# print(type(str))
# print(str)
data= json.loads(str) # 列表类型，可以使用索引获取信息
# print(data)
# print(type(data))

print(type(data[0])) # 字典类型
for i,j in data[0].items():
    print(j)
print(data[0].get('name')) # 获取对应的信息, 使用 get() 如果没有对应的键名，不会报错，返回 None
print('--------------')
print(data[0].get('age'))
print(data[0].get('age', 213)) # 传入键名对应的默认值，键名不存在的时候将返回默认值，
# print(data)


print('读取 json 文件')
# 读取 json 文件
# with open('data.json', 'r') as f:
#     str = f.read()
#     data = json.loads(str)
#     print(data)


data = [{
    'name': 'Mike',
    'abc': 'Mike',
    'def': '中文字符',
}]
with open('data.json', 'w', encoding='utf-8') as f:
    # f.write(json.dumps(str))
    f.write(json.dumps(data, indent=2, ensure_ascii=False)) # 将 json 列表以 json 格式保存到 文件