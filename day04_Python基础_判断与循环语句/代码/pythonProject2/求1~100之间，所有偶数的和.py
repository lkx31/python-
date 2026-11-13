# 求1~100之间，所有偶数的和求1~100之间，所有偶数的和
# 首先偶数和就是\\2的数字
# 那么要定义一个承接数字的变量
count = 1
# 其次是有一个承接num的变量对吧
total = 0
# 然后用循环while方法,回想一下1-100用while的方法怎么写的
# while count<100:
#     total+=count
#     count+=1
# 但是我们要取偶数怎么办用运算符和if判断对吧
while count < 100:
    if count % 2 == 0:
        total += count
count += 1
print(total)
