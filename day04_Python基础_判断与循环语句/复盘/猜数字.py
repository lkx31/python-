# 随机生成1个 1 ~ 100之间的数字, 让用户来猜.判断用户是否猜对了, 并提示. 猜对, 猜大, 猜小
import random

num=random.randint(1,100)
print(num)
guess_num=int(input("请输入你的数字"))

if guess_num==num:
    print("猜对了")
else:
    if guess_num>num:
        print("你猜大了")
    else:
        print("你猜小了")
