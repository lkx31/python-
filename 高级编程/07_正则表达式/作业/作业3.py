# 匹配出163的邮箱地址，且@符号之前有4到10位字母数字下划线，举例: binzi@163.com
import re
def show(result):
    if result:
        print(result.group())
    else:
        print("无法配对")
result=re.match(r"([A-Za-z\d_]{4,10}@([\d]{3,})\.([a-zA-Z]{2,6}))","binzi@163.com")
show(result)