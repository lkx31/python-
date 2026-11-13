#闭包的特点三个：嵌套，返回内部函数的值，由引用外部函数
#装饰器就是在不改变源代码和调用功能的情况下增强一些功能，特点，闭包三个加上特点
import time
def outer(fn):
    def inner(*args,**kwargs):
        start_Time=time.time()
        result=fn()
        end_Time=time.time()
        print(f"执行的时间是{end_Time - start_Time}")
        return result
    return inner
def my_count():
    s = 0
    for i in range(1000001):
        s+=i
    print(s)
my_count=outer(my_count)
my_count()