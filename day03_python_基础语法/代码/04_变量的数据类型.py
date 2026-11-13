# 演示 变量的数据类型
"""
    数据类型共计有 7 种:
        数值类型 :  整数类型 int   和  小数类型 float
        布尔类型 :  真 True  假 False
        以下为五大容器,用于一次性保存多个数据:
            字符串类型:  文本数据, 一般使用 引号 引起来, 可以单引号 也可以 双引号
            列表类型
            元组类型
            集合类型
            字典类型

    如何判断数据类型:
        type(变量)  返回 对应变量的数据类型
        isinstance(变量名称,数据类型)  判断对应变量是否是这个数据类型, 如果是 返回True 否则返回False

"""
# 演示 数值类型
# 案例1：定义一个人的信息，姓名：Tom、年龄18岁  并且打印出结果
name = 'Tom'
age = 18
score = 39.5

# 打印结果
print(name)
print(type(name))

print(age)
print(type(age))

print(score)
print(type(score))

# 判断 年龄 是不是 一个整数呢?
print(isinstance(age, int))  # True

# 判断 成绩 是不是 一个整数呢?
print(isinstance(score, int))  # False

# 案例2：定义一个超市收银系统，写入一个名称：大白菜，价格：3.5 并且打印出结果
# 定义变量
product_name = '大白菜'
product_price = 3.5

# 打印各个变量的内容
print(product_name)
print(product_price)

# 获取变量的数据类型
print(type(product_name))
print(type(product_price))

# 判断变量的数据类型
print(isinstance(product_name, str))  # True
print(isinstance(product_price, int))  # False  因为价格是小数类型

print('--------------------------')
# 演示布尔类型：  True  False
# 案例1：手工定义一个flag变量，其值为True
flag = True

# 打印变量
print(flag)
# 类型获取:
print(type(flag))  # <class 'bool'>  boolean
print(isinstance(flag,bool))  # 返回True
