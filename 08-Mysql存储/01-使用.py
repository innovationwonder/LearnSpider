import pymysql

print('连接数据库')
# host = IP(localhost/远程IP)
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)

cursor = db.cursor() # 获得操作游标 cursor()
cursor.execute('SELECT VERSION()') # execute() 利用操作游标执行 SQL 语句， 获得 mysql 的当前版本
data = cursor.fetchone() # fetchone() 获得第一条数据
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8") # 创建数据库 spider 指定编码 UTF-8
db.close()

