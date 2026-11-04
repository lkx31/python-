# 演示: 函数的不定长参数
# 需求: 定义一个函数, 要求可以接受任意个数字(0~n个)参数, 在函数中完成这些数字求和计算
def budin (*args):
    count=0
    for i in args:
        count+=i
    print(count)
budin(1,2,3,4,5,6,8)
my_tuple = (1,2,3)
budin(*my_tuple)
#字典参数
def duo (**kwargs):
    print(kwargs)
    print(type((kwargs)))
duo(name='lk',age=25,address='福建')
dict1={'name':'lkt','age':28}
duo(**dict1)