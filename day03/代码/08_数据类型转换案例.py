# 类型转换案例
# 需求: 请键盘录入一个商品名称, 商品的价格, 商品的数量, 输出:  您购买了 xxx , 商品的单价为xxx,您购买了xx个, 总价为 xxx
# 键盘录入： input('提示词')
# 注意： 通过键盘录入的内容， 其数据类型都是字符串

# 1- 通过键盘录入三个信息:
pName = input('请输入商品名称:')
price = input('请输入商品价格:')
num = input('请输入商品数量:')

# 2- 计算 商品的总价

# 2.1 类型转换操作:  price  和 num
price = float(price)
num = int(num)
# 2.2 计算总价
total = price * num

# 3- 输出结果
print(f'您购买了{pName} , 商品的单价为{price},您购买了{num}个, 总价为{total}')