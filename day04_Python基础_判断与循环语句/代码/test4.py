while True:
    price = float(input("请输入商品的单价："))
    num = int(input("请输入商品的数量："))

    total = price * num

    tip = input("是否为会员(y/n)：")
    if tip == "y":
        total = total * 0.8

    print("您最终支付的价格是{:.2f}元".format(total))

    cont = input("是否继续下一位顾客？(输入 y 继续，其他字符退出)：")
    if cont != "y":
        print("下班")
        break