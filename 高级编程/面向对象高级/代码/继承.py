class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def eat(self):
        print(f'{self.name}正在吃饭')
    def sleep(self):
        print(f'{self.name}正在睡觉')
class nan(Person):
    pass
class nv(Person):
    pass
nan1=nan("小明",18)
nan1.eat()
nan1.sleep()
nv1=nv("小红",18)
nv1.eat()
nv1.sleep()