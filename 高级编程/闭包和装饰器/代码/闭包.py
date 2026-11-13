def outer():
    num=10
    print(f"第一个num")
    print(num)
    def inner():
        num=20
        print(f"第二个行数")
        print(num)
        return 5
    return inner
inner=outer()  #inne = inner
inner()
print(inner())