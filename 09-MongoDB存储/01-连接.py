import pymongo
# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/') # 连接数据库，功能同上

# 指定数据库
db = client.test
# db = client['test'] # 同上

# 指定集合 类似 mysql中的表
collection = db.students

# 插入数据
student = {
    'id':'3450',
    'name':'Jordan',
    'age':42,
    'gender': 'male'
}
student1 = {
    'id':'3452',
    'name':'Mike',
    'age':12,
    'gender': 'male'
}
student2 = {
    'id':'3453',
    'name':'Mary',
    'age':32,
    'gender': 'Female'
}
# result = collection.insert([student1, student2])  # insert() 方法会在执行后返回 _id 值
# result = collection.insert_one(student) # insert() 已不推荐使用， insert_one() 用于插入单条数据
# result = collection.insert_many([student1, student2]) # insert() 已不推荐使用， insert_one() 用于插入单条数据
# print(result.inserted_ids)   # mongodb 中每条数据都有一个 _id 属性 唯一标识

# 查询 find_one()
# result = collection.find_one({'name': 'Mike'}) # 返回单个结果
result = collection.find({'name': 'Mike'}) # 返回生成器对象
# for i in result:
#     print(i)
#
# print(result)
# print(type(result))

# 根据 ObjectedId 查询
from bson.objectid import ObjectId
result = collection.find_one({'_id': ObjectId("5c091aa196987d059c870df9")})
# print(result)

# 条件查询
results = collection.find({'age':{'$gt': 12}}) # 查询 age > 12 的数据 $gt 为 大于
results = collection.find({'name':{'$regex': '^M.*'}}) # 以 M 开头的正则表达式
# for i in results:
#     print(i)

# 计数
count = collection.find().count()
count = collection.find({'age':12}).count() # 统计 age = 20 的数据条数
# print(count)

# 排序
# results = collection.find().sort('name', pymongo.ASCENDING) # 按照首字母升序排序
# print([result['name'] for result in results])

# 偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(3) # 限制返回 3 个结果
# print([i['name'] for i in results])

# 注：在数据库数量非常庞大的时候，避免使用大的偏移量查询数据，很可能造成内存溢出
from bson.objectid import ObjectId
# collection.find({'_id':{'$gt': ObjectId("5c09192c96987d1cb493a3c9")}}) # 记录好上次查询的 ID， 查询大于它的

# 更新
# condition = {'name': 'Jordan'}
# student3 = collection.find_one(condition)
# student3['name'] = 'Mike'
# result3 = collection.update(condition, student3) # 传入查询条件和修改后的数据
# print(result3)

# result = collection.update(condition, {'$set': student}) # 这样值更新 student 字典内存在的字段，

# update_one() 和 update_many()， 推荐使用，第二个参数为 $...
# condition = {'name': 'Mike'}
# student = collection.find_one(condition)
# student['age'] = 30
# result = collection.update_one(condition, {'$set': student})
# print(student)
# print(result.matched_count, result.modified_count) # 匹配的条数，影响的条数

# condition = {'age': {'$gt': 40}}
# result = collection.update_many(condition,{'$inc': {'age':1}}) # age > 40 的 age +=1
# print(result)
# print(result.matched_count, result.modified_count)
#
# # 删除
# result = collection.remove({'name': 'Mike'})
# print(result)

result = collection.delete_many({'age':{'$gt':30}})
print(result.deleted_count)