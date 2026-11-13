import time
def timeLogin(fn):
    def inner():
        star_time=time.time()
        time.sleep(0.5)
        fn()
        end_time=time.time()
        print(f"程序运行的时间是{end_time-star_time:.2f}")
        return fn()
    return inner