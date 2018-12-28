import pymysql


db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
data = {
    'id':'213124',
    'name':'apple',
    'age':12
}
# print(tuple(data.values()))
table = 'students'
keys = ', '.join(data.keys()) # key1, key2, key3 --> id, name, age
values = ', '.join(['%s'] * len(data)) # %s, %s, %s

# INSERT INTO students(id, name, age) VALUES (%s, %s, %s)
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# 更新数据
print(sql)
cursor = db.cursor()

try:
    if cursor.execute(sql, tuple(data.values())): # 传入 sql 语句和键值构造的元祖
        print('Successful')
        db.commit() # commit() 实现数据插入，更新，删除
except:
    print('Failed')
    db.rollback() # 如果执行失败，rollback() 进行数据回滚，相当于什么都没发生过
db.close()

