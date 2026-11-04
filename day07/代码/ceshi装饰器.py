def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("执行前")
        func(*args, **kwargs)
        print("执行后")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")