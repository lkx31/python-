# 演示: 函数的参数传递方式:

# 需求: 定义一个函数, 要求函数能接收 四个变量 分别为 姓名  年龄  地址 生日 , 在函数中将接收到的数据直接通过print 一句话打印出来即可
def ceshi(name,age,address,birthday):
    print(f"你的名字是{name},你的年龄是{age},你的地址是{address},你的生日是{birthday}")
#位置参数
ceshi("罗楷涛",25,"福建",2001)
#关键字参数
ceshi(name="罗楷涛",age=26,address='福建',birthday=2001)
#缺省参数也叫默认参数
def ceshi1(name,age,address,birthday=2001):
    print(f"你的名字是{name},你的年龄是{age},你的地址是{address},你的生日是{birthday}")
ceshi1(name="罗楷涛", age=26, address='福建')
