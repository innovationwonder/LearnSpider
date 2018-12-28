data = {
    'id':'54514',
    'name':'Mike',
    'age':12
}
keys = ', '.join(data.keys())
print(keys)
print(type(keys))
values = ', '.join(['%s'] * len(data))
print(values)