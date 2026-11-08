# 演示 列表的增加API:
"""
    增加API:
        append() :  向列表的尾部添加数据
        extend() :  实现将列表中每一个元素依次的添加到另一个列表中
        insert() :  向列表中指定位置添加元素

"""
list1=['红狼','威龙','露娜']
print(list1)
#演示append
list1.append('无名')
print(list1)
#演示extend（）
list2=["麦小文",'张姐']
list1.extend(list2)
print(list1)
#演示insert
list1.insert(2,'阿萨拉小兵')
print(list1)
print(list1.count(list1))
