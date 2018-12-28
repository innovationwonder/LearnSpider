# 写入 CSV
import csv

# with open('data2.csv', 'w', encoding='utf-8') as f:
#     # writer = csv.writer(f, delimiter= ' ') # 以空格作为列之间的分隔符
#     # # writer = csv.writer(f)
#     # writer.writerow(['id', 'name', 'age'])
#     # writer.writerows([['101', 'Mike', '12'], ['102', 'Bob', '21'], ['103', 'poo', '41']]) # 写入多行，参数为 二维列表
#
#     # 以字典方式写入
#     names = ['id', 'name', 'age']
#     writer = csv.DictWriter(f, fieldnames=names) # 传入头信息
#     writer.writeheader() # 写入头信息
#     writer.writerow({'id': '101', 'name': '你好', 'age': 15}) # 传入字典

# 读取 CSV
import pandas as pd
# print(pd.read_csv('data2.csv'))

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for r in reader:
        print(r)