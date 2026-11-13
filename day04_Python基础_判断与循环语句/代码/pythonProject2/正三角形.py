"""写三角形：我要写一个7*7的三角形，和其他的差不多只不过是*在正中间如何处理两边
"""
for i in range(0,7):#7列
    print("*",end="\t")
    n=i+1
    for j in range(0,n):
        print("*"*n)
