"""
编写一个程序，让用户输入一个正整数n，然后计算1到n之间（包含n）所有整数的和、积

要求：

1. 使用input()获取用户输入的数字
2. 将输入转换为整数类型
3. 使用while循环实现累加和累乘功能
4. 使用格式化输出显示这二个计算结果
"""

num=int(input("请输入一个正整数"))
count=1
total=0
ji=1
while count<num:
    total+=count
    ji*=count
    count+=1
print(f"和是{total},积是{ji}")