# 带有默认值的参数:
# 需求1: 定义一个函数, 要求接收2个参数, 计算这二个参数的和并返回
def fn1(num1,num2):
    return num1+num2
print(fn1(2,3))
fn2=lambda num1,num2:num1+num2
print(fn2(3,11))
print("*"*30)
# 带 if判断（三目运算符）的lambda表达式
# 有判断操作:
# 需求: 要求定义函数, 传入一个姓名, 在函数中判断, 如果姓名为张三, 返回 1 否则 返回 0
def fn2(char:str):
    # if char=="张三":
    #     return 1
    # else:
    #     return 0
    return 1 if char =='张三' else 0
fn_2=lambda char: 1 if char =='张三' else 0
print(fn_2('张三'))
print(fn_2('张雪'))