# 演示数据类型转换
"""
    数据类型转换的操作:
        int(x) : 将 x 转换为 整数类型
        float(x): 将 x 转换为 小数类型
        str(x): 将 x 转换为 字符串类型

    注意:
        在转换的时候, 需要转换的值应该是什么类型, 就转换为对应的类型
"""
# 演示其他的类型转换:
a = '10'
b = '3.5'
e = 20

# 将 a 转换为 整数类型  :
c = int(a)
print(c)
print(type(c))

# b 转换为 小数类型
d = float(b)
print(d)
print(type(d))

# 思考 如果将b 转换为 整数类型呢?  无法转换  因为 b 本省就不是整数类型
# print(int(b))

b = 3.5
print(int(b)) # 不会报错,  但是会将小数位丢失, 仅保留整数位


# e 转换为 字符串类型
f = str(e)
print(f)
print(type(f))



# 演示数据类型转换
name = input('请输入您要购买商品名称：')
id = input('请输入您要购买商品编号：')
price = input('请输入您要购买的商品价格：')

print(f'您购买了{name}，商品编号为{id}，商品价格为{price}，欢迎下次光临！')


# 需求： 价格需要再原有的基础上涨价 10%

# 类型转换操作:
price = float(price)


price = price * 1.1
print(f'您购买了{name}，商品编号为{id}，商品价格为{price:.2f}，欢迎下次光临！')


