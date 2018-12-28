import pymysql


db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
table = 'students'
condition = 'age > 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition) # 删除 age > 20 的数据

try:
    cursor.execute(sql)
    print('Successful')
    db.commit() # commit() 实现数据插入，更新，删除
except:
    print('Failed')
    db.rollback() # 如果执行失败，rollback() 进行数据回滚，相当于什么都没发生过
db.close()

