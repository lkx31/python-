def outer():
    num=10
    def inner(sum):
        nonlocal num
        num=num+sum
        return num
    return inner
inner=outer()
number=inner(5)
print(number)
number=inner(100)
print(number)