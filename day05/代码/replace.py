"""
演示字典的操作
"""
my_dict={"lkx":666,"kx":111,"lx":555}

# 新增元素
my_dict["wrj"]=66
print(f"{my_dict}")
#更新元素
my_dict["lkx"]=66
print(f"{my_dict}")

#删除元素
spurce=my_dict.pop("lkx")
print(f"删除了一个元素{my_dict}，lkx的成绩是{spurce}")
#清空元素
my_dict.clear()
print(f"{my_dict}")
#获取全部的key
my_dict={"lkx":666,"kx":111,"lx":555}
keys=my_dict.keys()
print(f"全部的key{keys}")
#遍历字典
for key in keys:
    print(f"key:{key}")
    print(f"value:{my_dict[key]}")

#统计字典内的元素数量
num =len(my_dict)
print(f"字典的数量有{num}")