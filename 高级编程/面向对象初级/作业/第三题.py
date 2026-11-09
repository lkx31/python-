class Circle(object):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

    def __str__(self):
        return f"半径为{self.r}的圆的面积为{self.area()}"
jisuan=Circle(5)
print(jisuan)