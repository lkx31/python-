class Person:
    def __init__(self):
        print("我在创建对象的时候自动执行")
    def __str__(self):
        return "我把地址值变成字符串，要一个return不是print"
    def __del__(self):

        print("我在结束的时候被销毁了")
p1=Person()
print(p1)