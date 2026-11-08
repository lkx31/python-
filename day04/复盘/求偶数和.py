# 什么是偶数：所谓的偶数，就是能被2整除的数字就是偶数，数学中可以使用2n来表示偶数。(Python代码 => if  数值 % 2 == 0 代表它是一个偶数)
cnt=1
sum=0
while cnt<100:
    if cnt % 2==0:
        sum+=cnt
    cnt+=1
print(sum)