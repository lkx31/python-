import multiprocessing
import time
import os
import threading

def study():
    for i in range(0, 101):
        print(f"学习{i}")
        time.sleep(0.3)
def eat():
    time.sleep(0.5)

    current_thread = threading.current_thread()
    print(current_thread)
    # for z in range(0, 101):
    #     print(f"吃东西{z}")
    #     time.sleep(0.3)
if __name__=='__main__':
    for i in range(0,100):
        ss=threading.Thread(target=eat)
        ss.start()
    # study_thread=threading.Thread(target=study())
    # eat_thread=threading.Thread(target=eat())
    #
    # study_thread.start()
    # eat_thread.start()
