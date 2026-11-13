class A :
    def __init__(self,name,age,weight):
        self.weight=weight
        self.age=age
        self.name=name
class B(A):
    def __init__(self,name,age,weight,hight,address):
        super().__init__(name,age,weight)
        self.hight=hight
        self.address=address
    def __str__(self):
        return f'{self.name}的年龄是{self.age},体重是{self.weight},身高是{self.hight},住址是{self.address}'


b=B("小明",18,60,170,"山东")
print(b)

