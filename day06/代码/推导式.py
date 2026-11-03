# 案例：使用列表推导式生成平方数集合
#
# 例如, 用户输入10, 表示要生成 1~10的每一个数字的2平方的集合
user_number=int(input("请输入你的数字"))
set1=set()
for i in range(1,user_number+1):
    i=i**2
    set1.add(i)
print(set1)
my_set={ i**2  for i in range(1,user_number+1)}