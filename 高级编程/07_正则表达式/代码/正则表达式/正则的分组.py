import re
def show(result):
    if result:
        print("匹配成功",result.group())
    else:
        print("匹配失败")
#|要么左边表达式要么右边表达式
result=re.match("163|qq|126","126")
show(result)
#（）以组的形式表达
result=re.match(r"^([a-z0-9_]{6,})@([A-Za-z]{2,})\.([a-zA-Z]{2,6})$","1014718556@qq.com")
show(result)
#\n表示调用对应分组z注意调用的尾缀要和被调用的一定要一样
result=re.match(r"^([a-z0-9_]{6,})@([A-Za-z]{2,})\.\2$","1014718556@qq.qq")
show(result)
#？p给取别的名字
result=re.match(r"^([a-z0-9_]{6,})@(?P<zhu>[A-Za-z]{2,})\.(?P=zhu)$","1014718556@qq.qq")
show(result)