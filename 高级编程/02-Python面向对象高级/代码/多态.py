class Animal:
    def speak(self):
        print("叫")
class Dog(Animal):
    def speak(self):
        print("汪汪叫")
class Cat(Animal):
    def speak(self):
        print("喵喵叫")
def func(animal):
    animal.speak()
dog=Dog()
cat=Cat()
func(dog)
func(cat)