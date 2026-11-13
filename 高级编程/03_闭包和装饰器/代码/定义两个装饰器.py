def log_in(fn):
    def inner():
        fn()
    return inner

def outer1(fn):
    def inner1():
        fn()
    return inner1

def gongneng1():
    print("发布评论")
gongneng1()