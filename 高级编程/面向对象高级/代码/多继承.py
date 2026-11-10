class Animal:
    def eat(self):
        print("吃")
    def call(self):
        print("叫")
class BigAnimal(object):
    def run(self):
        print("跑")
class Dog(Animal,BigAnimal):
    def call(self):
        print("汪汪叫")
class Cat(Animal,BigAnimal):
    def call(self):
        print("喵喵")

dog=Dog()
dog.call()
dog.eat()
dog.run()
cat=Cat()
cat.call()
cat.eat()
cat.run()
