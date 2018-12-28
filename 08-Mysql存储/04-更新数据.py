import pymysql


db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
data = {
    'id':'3451',
    'name':'Ban',
    'age':22
}
table = 'students'
keys = ', '.join(data.keys())   # key1, key2, key3 --> id, name, age
values = ', '.join(['%s'] * len(data))   # %s, %s, %s

cursor = db.cursor()

# 如果主键已经存在执行更新操作 ON DUPLICATE KEY UPDATE
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
# SQL: INSERT INTO students(id, name, age) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s
# print(sql)

try:
    if cursor.execute(sql,tuple(data.values())*2): # 传入 sql 语句和键值构造的元祖 %s 有6个 所以元祖*2
        print('Successful')
        db.commit() # commit() 实现数据插入，更新，删除
except:
    print('Failed')
    db.rollback() # 如果执行失败，rollback() 进行数据回滚，相当于什么都没发生过
db.close()

