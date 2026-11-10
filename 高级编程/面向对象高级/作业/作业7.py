class Car:
    name1="car"
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"我的车是{self.name},类参数是{Car.name1}，实例参数是{self.name1}"
car=Car("su7")
print(car)


