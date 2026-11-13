def outer(fn):
    def inner(*args,**kwargs):

        result=fn(*args,**kwargs)
        result1=result+".txt"
        # print(result1)
        return result1
    return inner
@outer
def content():

    return "helloworld"
A=content()
print(A)