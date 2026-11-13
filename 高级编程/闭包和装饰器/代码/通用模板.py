def outer(fn):
    def inner(*args,**kwargs):
        result=fn(*args,**kwargs)
        return result
    return inner()
