# 演示 lambda表达式

# 需求: 定义一个函数, 该函数直接返回一个 100的结果

# 需求: 定义一个函数, 要
# 求传入2个任意的数字, 在函数体对这个二个数字进行相加, 并且将结果返回
def ceshi (a,b):
    print(a+b)
    return 100
# ceshi(1,3)
# #lambda
newceshi=lambda a,b:a+b
print("*"*30)
# 需求1: 定义一个函数, 要求接收2个参数, 计算这二个参数的和并返回
def he(c,d):
    return c+d
# 需求2: 定义一个函数, 要求传入一个字符串, 在函数内 对字符串的内容全部转换为大写( upper() ), 并且将转换后的字符串返回, 分别使用普通函数 和 lambda方式实现
#普通函数
def zifu (text):

  return text.upper()

str11="adasdads"
print(str11)
newstr11=zifu(str11)
print(newstr11)
#lamboda
newlada=lambda text:text.upper()
print(newlada(str11))