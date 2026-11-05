# 案例需求: 实际场景案例
# 给定以下一个列表:
# 共计有五个元素，每个元素的类型是字典类型，每个字典里面有三个元素
# 需求: 请对列表进行排序: 要求根据字典中年龄 从 大到 小 排序
def fn1(ele):
    return ele['age']
student_list = [
    {"name": "张三", "age": 20, "address": '南京'},
    {"name": "李四", "age": 25, "address": '北京'},
    {"name": "王五", "age": 23, "address": '上海'},
    {"name": "赵六", "age": 19, "address": '广州'},
    {"name": "田七", "age": 22, "address": '深圳'}
]

# student_list.sort(key=lambda ele:ele["age"])
student_list.sort(key=fn1)
print(student_list)