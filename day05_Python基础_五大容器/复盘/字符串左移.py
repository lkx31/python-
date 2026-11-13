# 将字符串向右旋转n位，例如“abcdef”向右旋转2位得到“efabcd”
str = 'abcdef'
n=int(input("右旋多少位"))
if n<=len(str):
    last_name=str[-n:]
    first_name=str[:-n]
    print(f"右旋了{n}位,结果展示为{last_name+first_name}")
else:
    print("超过字符数")