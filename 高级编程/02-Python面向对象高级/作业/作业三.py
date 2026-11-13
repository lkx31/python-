class Animal:
    def run(self):
        print("跑起来")
    def eat(self):
        print("吃东西")
class Horse(Animal):
    pass
horser=Horse()
horser.run()
horser.eat()