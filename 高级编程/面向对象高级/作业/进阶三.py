class Animal:
    def run(self):
        print("跑起来")
    def eat(self):
        print("吃东西")
class Horse(Animal):
    def run(self):
        super().run()
        # self.run=run
        print("迈着矫健的步伐")
class SwiftHorse(Horse):
    def __init__(self,name):
        self.name=name
sh=SwiftHorse("千里马")
print(sh.name)
sh.run()


