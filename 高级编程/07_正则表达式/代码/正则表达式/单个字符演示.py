import re
def show(result):
    if result:
        print("匹配成功",result.group())
    else:
        print("匹配失败")

result=re.match(".t.","itheima")
show(result)
result=re.match("[ikl]t","ktheima")
show(result)
result=re.match("\\d","152664564")
show(result)
result=re.match("[0-9]","55687")
show(result)
result=re.match("\\D","ithehasd")
show(result)
result=re.match("it\\sheima","it sheima")
show(result)
result=re.match("i\\Sheima","itheima")
show(result)
result=re.match("ithe\\w",'itheima')
show(result)
result=re.match("it\\W","it###heima")
show(result)