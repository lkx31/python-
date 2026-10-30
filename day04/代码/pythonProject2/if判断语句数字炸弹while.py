# 随机生成1个 1 ~ 100之间的数字, 让用户来猜.判断用户是否猜对了,
# 并提示. 猜对, 猜大, 猜小.
# 首先要调用random方法
import random

# 其次要生成1-100的方法
num = random.randint(1, 100)

print(num)
# 那么用户的输入方法



while True:
    User_num = input("请输入你猜的数字")
    if User_num == "":
        print("请输入正确数字")
        continue
    User_num = int(User_num)

    # 判断是不是要么猜对要么猜错
    if User_num == num:
        print("你猜对了")
        break
    else:
        if User_num > num:
            print("你猜大了")
        else:
            print("你猜小了")
