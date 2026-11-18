# 请编写程序,匹配出微博中的所有话题, 举例: #幸福是奋斗出来的
import re
def show(result):
    if result:
        print(result)
    else:
        print("无法配对")
str1 = '前面省略很多内容#幸福是奋斗出来的#此处省略很多内容#学IT来黑马#后面省略很多内容'
result=re.findall("#.*?#",str1)
print(result)