from redis import StrictRedis

# redis = StrictRedis(host='localhost', port=6379, db=0)
# redis.set('name', 'Mike')
# print(redis.get('name'))

# 使用 ConnectionPool 连接
from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)
redis.set('age', 15)
print(redis.get('age'))
