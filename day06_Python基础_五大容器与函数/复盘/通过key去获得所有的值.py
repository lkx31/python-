person = {'name': '张三', 'age': 20, 'address': '湖南省长沙市岳麓区'}
print(person.keys())
print(person.values())
for i in person.keys():
    value=person[i]
    print(f"key:{i},value:{value}")