# 类型转换案例
# 需求: 请键盘录入一个商品名称, 商品的价格, 商品的数量, 输出:  您购买了 xxx , 商品的单价为xxx,您购买了xx个, 总价为 xxx
# 键盘录入： input('提示词')
# 注意： 通过键盘录入的内容， 其数据类型都是字符串
name=input("请输入名称")
price=float(input("请输入价格"))
numeber=int(input("请输入商品的数量"))
total=price*numeber
print(f"您购买了{name},商品的单价为{price:.2f}，您购买了{numeber}个,总价格为{total:.2f}")