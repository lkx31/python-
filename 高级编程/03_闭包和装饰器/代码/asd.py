def outer(fn):
    def inner():
        print(1)
        fn()
        print(2)
    return inner
def outer1(fn):
    def inner():
        print(3)
        fn()
        print(4)
    return inner
def commnt():
    print('pingluan ')
commnt=outer(commnt)
commnt=outer1(commnt)
commnt()

