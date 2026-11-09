class Person():
    def __init__(self):
        self.name="小明"
        self.weight=75

    def run(self,num):
        self.weight=self.weight-0.1*num

    def eat(self):
        self.weight=self.weight+0.2
    def __str__(self):
        return f"我的名字叫{self.name},我的体重是{self.weight}"
xiaomin=Person()
print(xiaomin)
xiaomin.run(6)
print(xiaomin)