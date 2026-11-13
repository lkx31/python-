def outer(fn):
    def inner(num1,num2):
        sum=fn(num1,num2)
        return sum
    return inner

def num(num1,num2):
    sum=num1+num2
    print(sum)
    return sum
num=outer(num)
num(10,5)
