# 将字符串向右旋转n位，例如“abcdef”向右旋转2位得到“efabcd”

nace="abcdef"
n=input("请输入右旋多少位")
n=n%nace
first=nace[:n]
last=nace[:-n]
new_str=last+first
print(f"{new_str}")