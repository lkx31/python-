# . 键盘输入一个字符串，用字典统计每个字符出现的次数，例如输入 abceacf，输出 {'a': 2, 'b': 1, 'c': 2, 'e': 1, 'f': 1}。
#
# 2. 分别用 for 循环和列表推导式两种方式，生成 1~20 之间所有偶数的平方组成的列表。
#
# 3. 定义一个函数，接收一个数字列表，返回该列表的最大值和最小值组成的元组，并调用它打印结果
# dict={}
# count=1
# str1=input("请输入字符串")
# for i in str1:
#     if i  not in dict:
#         dict[i]=count
#     else:
#         dict[i]=count+1
# print(dict)
# print('*'*40)
#for循环
list=[]
for i in range(1,20):
    if i %2==0:
        i*=2
        list.append(i)
print(list)
#列表推导式
list1=[i**2 for i in range(1,20) if i %2==0]
def shuzi (*args):
    max()