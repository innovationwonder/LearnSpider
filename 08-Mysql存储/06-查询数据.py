import pymysql


db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 10' # 查询 age >= 10 的数据

try:
    cursor.execute(sql)
    print('Successful')
    print('Count', cursor.rowcount) # .rowcount 获取查询结果的条数
    row = cursor.fetchone()
    while row:  # 每循环一此，指针偏移一条数据
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Failed')
    db.rollback() # 如果执行失败，rollback() 进行数据回滚，相当于什么都没发生过


# try:
#     cursor.execute(sql)
#     print('Successful')
#     print('Count', cursor.rowcount) # .rowcount 获取查询结果的条数
#     one = cursor.fetchone() # 获取第一条数据
#     print('One', one)
#     results = cursor.fetchall() # .fetchall() 得到结果的所有数据,缺少第一条，由于内部实现有一个偏移指针用来指向查询结果，之前已使用 fetchone() 查询第一条
#     print('Results Type:', type(results))
#     for r in results:
#         print(r)
#
# except:
#     print('Failed')
#     db.rollback() # 如果执行失败，rollback() 进行数据回滚，相当于什么都没发生过
db.close()

