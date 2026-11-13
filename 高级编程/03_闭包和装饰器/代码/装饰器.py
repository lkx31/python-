import logDecorator
# def outer(fn):
#     def inner():
#         print("请先登录测试")
#         fn()
#     return inner
@logDecorator.timeLogin
def gongneng1():
    print("打印")
@logDecorator.timeLogin
def gongneng2():
    print("评论")

gongneng1()
gongneng2()