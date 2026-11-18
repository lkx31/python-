import re

result = re.match("it", "itheima")
if result:
    print(result.group())
else:
    print("对不起你输入的不匹配")

result2 = re.search("it", "aaitheima")
if result2:
    print(result2.group())
else:
    print("对不起你输入的不匹配")

result3 = re.findall("it", "ititititiasdasdas")
if result3:
    print(result3)
else:
    print("对不起你输入的不匹配")
