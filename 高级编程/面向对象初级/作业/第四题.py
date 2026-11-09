class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return 2*(self.width+self.height)
    def __str__(self):
        return f"矩形的面积为{self.getArea()}，周长为{self.getPerimeter()}"
jisuan=Rectangle(2,4)
print(jisuan)