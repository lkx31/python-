import multiprocessing
import time
import os
import threading

def study():
    print(f"主进程的id是：{os.getpid()}")
    print(f"study的id是：{threading.current_thread().native_id}")
    print(f"study的id是：{threading.current_thread().ident}")
    # for i in range(0, 101):
    #     print(f"学习{i}")
    #     time.sleep(0.3)


def eat():
    print(f"主进程的id是：{os.getpid()}")
    print(f"eat线程的id{threading.current_thread().native_id}")
    print(f"eat线程的id{threading.current_thread().ident}")

    # for i in range(0, 101):
    #     print(f"吃东西{i}")
    #     time.sleep(0.3)
if __name__=='__main__':
    print(f"主进程的id是：{multiprocessing.current_process().pid}")
    print(f"主线程的id{threading.current_thread().ident}")
    print(f"主线程的id{threading.current_thread().native_id}")
    study_thread=threading.Thread(target=study)
    eat_thread=threading.Thread(target=eat)

    study_thread.start()
    eat_thread.start()
