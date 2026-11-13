def outer(fn):
    def inner(*args):
        count=len(args)
        print(f"个数为{count}个")
        result=fn(*args)
        print(f'这些参数的和是{result}')
        return result
    return inner
@outer
def func(*args):

    return sum(args)
A=func(1,2,3,4,5,6)
print(A)
