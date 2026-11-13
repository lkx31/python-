class Animal:
    def run(self):
        print("跑起来")
    def eat(self):
        print("吃东西")
class Horse(Animal):
    def run(self):

        print("我迈着矫健的步伐一步两步")

horse=Horse()
horse.run()