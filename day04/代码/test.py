# 编写一个程序，让用户输入商品原价和购买数量，然后计算总金额并应用以下折扣规则：
#
# - 购买数量为1-2件，无折扣
# - 购买数量为3-5件，享受9折优惠
# - 购买数量超过5件，享受8折优惠
"""首先分析：输入要用到input方法，其次金额计算是float的要用到强制转化，再而规则
是由三个则需要if判断语句和算数运算符号"""
price=float(input("请输入商品价格"))
num=int(input("请输入商品数量"))
total=price*num
if num>=1 and num<=2:
    print(total)
if num>=3 and num<=5:
    total=total * 0.9
    print(total)
else:
    total=total*0.8
