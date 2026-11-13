# 演示 字典的基本使用
"""
    定义语法结构:
        字典变量名称 = {key1:value1 ,key2:value2 ,key3:value3 ........}

        定义空字典:
            字典变量名称 = {}
            字典变量名称 = dict()
    注意: 其中key值是唯一的, value值无所谓, 而且一般key值都是字符串类型

    字典是一个可变的数据类型
"""
person = {'name': '张三', 'age': 20, 'address': '湖南省长沙市岳麓区'}
print(person)
print(type(person))
#空字典
dict2={}
print(type(dict2))
dict3=dict()
print(type(dict3))
#获取里面的值
name=person['name']
print(name)

print(person.get("age"))
print(person.keys())
print(person.values())
for key in person.keys():
    value=person[key]
    print(f"{key},{value}")
    