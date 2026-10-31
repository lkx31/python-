tup1=('11','1112','131313','3333')
print(type(tup1))
#创建空元组比较特殊
tup=()
print(type(tup))
#元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
tup3=(99,)
tup4=(99)
print(type(tup3))
print(type(tup4))
#元组也可以通过下标索引取值
tup7 = ('Google', 'Runoob', 1997, 2000)
tup8 = (1, 2, 3, 4, 5, 6, 7 )
print(tup7[0])
print(tup8[1:5:1])
#元组是不可以修改的，列表是可以修改的但是元组可以组合创造一个新的元组
list2 = ['Google', 'Runoob', 1997, 2000]
list2.append('lkt')
print("更新的列表是",list2)

tup10=tup7+tup8
print(tup10)
#删除元组：不能删除的是元素，但是可以把元组删除，列表可以删除用del
del list2[3]
del tup10
# print(tup10)
#y