# replace('需要替换字符','替换后的字符',替换次数):  默认替换次数为全部的内容, 如果写了对应的N个数值, 只替换前N个
# 案例1:
str1 = 'hello linux and hello linux'
# 把字符串中所有linux字符替换为python: replace
str3=str1.replace("linux","python")
print(str3)
# 把字符串中的第一个linux进行替换为python
str4=str1.replace("linux","python",1)
print(str4)
# 把and字符串替换为&&
str5=str1.replace("and","&&")
print(str5)
print(type(str5))
print("****"*30)
# 案例2:
str2 = 'apple-banana-orange'
print(type(str2))
# 需求1: 根据字符串的 - 对字符串进行切割操作
str9=str2.split("-")
print(str9)
print(type(str9))


# 需求2: 针对案例1的字符串, 请按照空格进行切割
str10=str1.split(" ")
print(str10)
print(type(str10))

# 案例：把水果列表['apple', 'banana', 'orange']拼接成'apple-banana-orange'
#
# ```python
#
# ```
list1=['apple', 'banana', 'orange']
print('-'.join(str9))