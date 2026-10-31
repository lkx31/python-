produce_name=input("请输入商品名称")
produce_price=input("请输入商品价格")
produce_num=input("请输入商品数量")
produce_price=float(produce_price)
produce_num=int(produce_num)

total_price=produce_price*produce_num
print(f"您的商品名称是{produce_name},您的商品价格是{produce_price},您的商品数量是{produce_num}，您的商品总价是{total_price}")