#定义一个集合
set1 = {'张三','李四','王五','赵六','田七','李四','王五'}
print(set1)
print(type(set1))
set2=set()
print(set2)
for i in set1:
    print(i)
    #判断某元素是否在集合中
if "罗10" in set1:
    pass
else:
    set1.add("罗10")
print(set1)
if "张三" in set1:
    set1.remove("张三")
print(set1)