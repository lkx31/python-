# 给定一个字符串my_string，现在要求统计每个字符出现的次数: 形成结果: {'字符':出现次数,'字符2':次数}
#
# 例如: 'abceacf' ==> {'a':2,'b':1,'c':2,'e':1,'f':1}
#
#
#
# **实现思路**
#
# ①定义一个字符串
#
# ②初始化空字典，来存储对应字符和出现次数
#
# ③循环遍历字符串中每个字符
#
# ④如果字符串已经在字典中，计数加1，如果不在，初始化计数1:  字典['key'] += 1
#
# ⑤输出统计每个字符出现的次数
#
# #

str1='abcdeacf'
dict1={}
for i in str1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)
print("*"*40)
# 需求: 编写一个程序将字符串转换为字典  例如:输入: '5=Five 6=Six 7=Seven'   输出: {'5': 'Five', '6': 'Six', '7': 'Seven'}
dict4={}
str3="5=Five 6=Six 7=Seven"
str3=str3.split(" ")
print(str3)
print(type(str3))
print("*"*40)
for i in str3:
    print(type(i))
    i3=i.split("=")
    print(i3)
    print(type(i3))
    dict4[i3[0]] = i3[1]
print(dict4)

