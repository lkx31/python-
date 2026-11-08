# 字典：有keys:value组成的，其中keys是唯一的，值不一定，可以存储任意数据类型，用{}表示
empty_dict={}
print(type(empty_dict))
print(len(empty_dict))
#内置函数dict()创建字典
empty_dict1=dict()
print(type(empty_dict1))
print(len(empty_dict1))
#访问字典的值
empty_dict2={'name':'lkt','tall':'178','weight':'200'}
print("empty_dict2:name",empty_dict2['name'])
print("empty_dict2:tall",empty_dict2['tall'])
#字典可以修改，列表也可以修改，但是元组不能修改（可以链接成为新的）
empty_dict3={'name':'lkx','age':'19','class':'12'}
empty_dict3['name']=['lkt']
empty_dict3['age']=['28']
print(empty_dict3)
list2 = ['Google', 'Runoob', 1997, 2000]
list2[1]=['lkt']
print(list2)
#删除字典可以删除以及列表也可以删除，元组不可以伤处
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del tinydict['Name']
print(tinydict)

#列表
del list2[1]
print(list2)
#字典有键：值三部分组成，值可以是所有数据类型，但是键不可以变的才可以充当以及是唯一的




