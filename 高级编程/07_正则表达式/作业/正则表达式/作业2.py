# 请编写程序,匹配出1开头的所有11位手机号码, 举例: 18866668888
import re
def show(result):
    if result:
        print(result.group())
    else:
        print("无法配对")
result=re.match(r"([1]{1})([\d]{10})","18866668888")
show(result)