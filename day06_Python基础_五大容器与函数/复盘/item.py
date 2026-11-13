person = {'name': '张三', 'age': 20, 'address': '湖南省长沙市岳麓区'}
print(person.items())
for k,v in person.items():
    print(f"key:{k},value:{v}")