# %格式化输出
num=3.141592678
# 都保留两位小数
print("%.2f"%num)
#.format方法
print("保留小数{:.2f}".format(num))
#f-string方法
print(f"保留三位小数{num:.2f}")