import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
id = '2012001'
user = 'Mike'
age = 12

cursor = db.cursor()
sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'  # 插入数据
try:
    # 创建表
    # sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'

    cursor.execute(sql, (id, user, age))  # 执行 SQL
    db.commit()  # commit() 实现数据插入，更新，删除
except:
    db.rollback()  # 如果执行失败，rollback() 进行数据回滚，相当于什么都没发生过
db.close()

