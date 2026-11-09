class Person:
    def __init__(self,name,age,gender,weight):
        self.name=name
        self.age=age
        self.gender=gender
        self.weight=weight
    def __str__(self):
        return f"我返回的名字是{self.name},年龄是{self.age},性别是：{self.gender},体重是{self.weight}"
p1=Person("lkt",18,'男',100)
print(p1)