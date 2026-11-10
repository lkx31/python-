class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Squre(Shape):
    def __init__(self, long):
        self.long = long

    def area(self):
        return self.long * self.long


square = Squre(5)
print(square.area())
