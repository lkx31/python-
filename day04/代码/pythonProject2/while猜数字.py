# 编写一个Python程序，随机生成一个1到100之间的整数，用户通过输入猜测的数字
# ，程序会根据用户的输入提示“猜大了”、“猜小了”或“猜对了”。
# 用户可以无限次猜测，直到猜对为止。猜对后，程序会提示用户并结束游戏。
# 随机生成用到的方法random
# 且用户要输入数字则要用到input方法
# 有不同选择判断则用if
# 无线猜测则是循环while
import random

num = random.randint(1, 100)
User_num = int(input("请输入你猜的数字"))
while User_num != num:
    if User_num > num:
        print("你猜大了")

    elif User_num < num:
        print("你猜小了")
    else:
        print("你猜对了")
    User_num = int(input("请输入你猜的数字"))
