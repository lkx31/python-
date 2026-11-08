list1=['red','yellow','green','orange']
#索引方法
print(list1[0])
print(list1[2])
print(list1[1])
#索引从右到左0开始，如果从左到右则是-1开始
print(list1[-1],list1[-2])
#同时也可以[]来取值
print(list1[::2])
print(list1[0:3])
print(list1[:])
#那么索引，他其实包头不包尾，[头：尾：步长]，步长不写默认为1
#list的方法 append:在末尾增加一个
list2 = ['Google', 'Runoob', 1997, 2000]
list2.append('lkt')
print("更新的列表是",list2)
#删除方法
del list2[3]
print("删除后的列表",list2)
#脚本操作符：+用于组合列表，*用于重复列表
"""
[1, 2, 3] + [4, 5, 6]        [1, 2, 3, 4, 5, 6]
['Hi!'] * 4            	['Hi!', 'Hi!', 'Hi!', 'Hi!']
"""
