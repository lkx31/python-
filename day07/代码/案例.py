# ​		定义一个函数, 要求传递3个参数, 分别为商品名称、商品的价格、商品的数量， 在函数内部计算商品的总价（数量*价格），并且打印商品信息（‘商品为xxx，单价为xxx，购买了xxx个，总价为xxx’）
#
# * 场景1： 当所有的参数都没有默认值， 请分别使用位置传参和关键词参数来调用函数
# * 场景2： 为函数的形参设置默认值，例如 商品数量默认为1， 价格默认为1， 分别使用位置传参和关键词参数调用函数
#   * 通过位置传参， 仅设置商品名称
#   # * 通过关键词传参， 设置商品名称和商品数量
def chaoshi (name,price,number):
    total=number*price
    print(f'商品为{name},价格为{price},数量为{number},总价为{total}')
#位置传参
chaoshi('西瓜',10,1,)
#关键字参数
chaoshi(name='哈密瓜',price=10,number=2)
#场景2
def chaoshi1 (name,price=1,number=1):
    total=number*price
    print(f'商品为{name},价格为{price},数量为{number},总价为{total}')
#位置参数
chaoshi1('西瓜')
#关键词
chaoshi1(name='西瓜',price=10,number=2)