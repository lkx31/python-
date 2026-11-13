class Animal(object):
    def eat(self):
        print('吃')
    # 公共方法
    def call(self):
        print('叫')


class Dog(Animal):
    # 重写父类的call方法
    def call(self):
        print('汪汪叫')


class Cat(Animal):
    # 重写父类的call方法
    def call(self):
        print('喵喵叫')


wangcai = Dog()
wangcai.eat()
wangcai.call()

miaomiao = Cat()
miaomiao.eat()
miaomiao.call()