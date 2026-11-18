import re
def show(result):
    if result:
        print("匹配成功",result.group())
    else:
        print("匹配失败")
#*至少0次或者无限次
result=re.match("[a-z]*","itheimadasd")
show(result)
result=re.match("[a-z]{0,}","dfjgod")
show(result)
#至少1次或者无限次的+
result=re.match("[a-i]+","ithemai")
show(result)
#至少0次或1次
result=re.match("[a-z]?","asdasdqwe")
show(result)
#至少x次
result=re.match("[a-z]{3}","asdasfnbiud")
show(result)
#在这个区间次
result=re.match("[a-z]{0,100}","knfdjvndfbndfb")
show(result)