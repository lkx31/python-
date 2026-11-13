class Person(object):
    def speak(self):
        print(f"我的名字是{self.name},我的年龄是{self.age},我的地址是{self.addreess}")

p1=Person()
p1.name="罗楷涛"
p1.age=18
p1.addreess="福建"
p1.speak()
print(f"我的姓名：{p1.name}")
print(f"我的姓名：{p1.age}")
print(f"我的姓名：{p1.addreess}")
