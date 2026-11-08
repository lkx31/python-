list1 = ['老张', '张三', '老李', '李四', '王五', '赵六', '田七', '周八', '李九']
del list1[0]
print(list1)\
 #默认 弹出最后一个值，写的索引值
list1.pop()
print(list1)
list1.pop(1)
print(list1)
#remove
list1.remove("周八")
print(list1)
