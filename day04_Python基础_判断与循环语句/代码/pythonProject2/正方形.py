"""写一个5行5列的正方形
首先是生成五行或者五列采用for循环遍历，承接于行数或列数的变量名，再写内循环用j生成五行五列
依次和外循环遍历"""
for i in range(6):
    for j in range(6):
        print("*",end="\t")
    print()