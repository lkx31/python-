# 测试注释
# print("你好世界")  # 后面的注释测试
"""以及多行的注释测试三个引号的测试
以及格式化代码的快捷命令ctrl+Alt+L
"""
# 以及快速注释是ctrl+/
# 测试是否可以后面加ctrl+/
# ctrl+s是快速保存
# 以及CTRL+z是撤销，以及+y是恢复
# 以及CTRL+D是对代码复制光标行的快速复制
"""什么是变量：存储数据的容器，可以改变，数据是零时的
命名的规则是字母+数字+_，其中数字不能在前面以及不能有其他特殊的符号，区分大小写以及不能使用关键字"""


# for i in range(10):
#     print(i)
"""记不住关键字则使用hlep方法"""
# help("if")
"""推荐的定义变量名字方法，大小驼峰以及下划线，变量一定要先定义在进行使用"""
# name='itheima'
# print(name)输出的则是itheima
# print("name")#输出的是name
"数据类型的种类：数值类型，布尔值，元组，字典，列表，集合，字符串总共7中"
# 那么如何判断变量是什么类型，那么要借助type()方法和isinstance()
# name='黑马'
# age=16
# cee={1,11}
# tall=180.11
# print(isinstance(name,float))#输出True
# print(isinstance(age,int))#输出True
# print(isinstance(cee,set))
# print(isinstance(tall,float))

# print(type(name))输出str
# print(type(age))输出int
# print(type(cee))输出set
# print(type(tall))输出float
# 练习，定义一个人，姓名：Tom、年龄18岁  并且打印出结果
# name='Tom'
# age=18
# print(name,age)
# 布尔类型：于逻辑相关的数据类型只有True或者False
# flag=True
# # print(type(flag))#输出是bool
# # print(isinstance(flag,bool))输出是true
# # 什么是字符串：用单双引号是str的类型
# # ％格式化输出，啥时候用到，要对变量格式化操作一一对应的
# name='itheima'
# age=18
# print('我的名字是%s,我的年纪%d' %(name,age))
# 什么是format方法格式化输出：是格式化函数：负责把数据“排版”成你想要的字符串形式，它本身不打印，只返回一个字符串
# name='itheima'
# age=18
# print('我的名字叫{}，我的年龄是{}'.format(name,age))
# # 那么。format()则是格式化字符串的操作方法，里面两个参数可以是任何不限于字符串，但是调用者是字符串模板
# """以及f.string则是字符串语法层面格式化:，整体结果一定是字符串f 前缀必须跟字符串字面量，{} 里可以放任意表达式，最终统一变成字符串。
# "...{}".format(x)  字符串方法调用 x 任意类型
# f"...{x}"         字符串字面量语法   x任意类型"""
# .format()：先有字符串，后填值
# f-string：写字符串的同时就填值
# s1 = "{}".format(123)
# print(type(s1))  # <class 'str'>
#
# s2 = f"{123}"
# print(type(s2))  # <class 'str'>
# name='122'
# age=1111
# print('我的名字是{}，年龄是{}'.format(name,age))#format
# print(f'我的名字是{name}，我的年龄是{age}')#f-string
# print('我的年龄是%s,我的年纪是%d'%(name,age))#百分号方法
# # 转义字符
# 转义字符是为了让“有特殊含义的字符”在需要时变成普通字符，也让“打不出来的字符”能用文本表示出来。
# r 表示 raw string，里面的 \ 不再当转义符，按字面处理。这就是为什么正则表达式、Windows 路径常用 r"..."。
# input()方法：所有由input()方法获取的数据都是“字符串”类型
# 实列
# password=input()
# print(f'请输入你的密码{password}')
# print('请输入你的密码{}'.format(password))
# 数据类型转换演示
# name=input('请输入你的要买的商品')
# id=input('请输入编号')
# price=input('请输入你的商品价格')
# #由于f-string方法输出的是字符串，无法进行算数运算所以要进行数据转化
# print(type(price))
# price=float(price)
# price=price*10
# print(type(price))