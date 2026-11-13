"""
"""
def fun1(*args,**kwargs): # 注意 当  函数既要接收可变元组 又要接收可变字典 此时一定要将可变元组参数放置到前面
    print(args)
    print(kwargs)
    # 遍历可变元组
    for item in args:
        print(item)

    print("---------------上面是可变元组的遍历结果, 下面是可变字典的遍历结果-----------------")
    # 遍历可变字典
    for k,v in kwargs.items():
        print(f"{k},{v}")
fun1('张三','李四','王五','赵六',name='田七',age =18,address ='北京市')

# 先定义一个元组 和 字典 然后传入呢?
my_tuple = (1,2,3,4,5,6)

my_dict = {'class_id':0,'clas_name':'大模型第一期'}

fun1(*my_tuple,**my_dict)