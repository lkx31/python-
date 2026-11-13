"""
演示魔术方法
"""


class test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # -_str__魔术方法
    def __str__(self):
        return f"test的类对象，name:{self.name},age:{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age


test1 = test("lkx", 666)
test2 = test("kx", 366)
print(test1 < test2)
print(test1 > test2)
print(test1 <= test2)
print(test1 >= test2)
print(test1 == test2)
print(test1 == test2)

print(test1)
print(str(test1))


