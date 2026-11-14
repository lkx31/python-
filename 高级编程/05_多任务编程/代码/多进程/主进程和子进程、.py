import multiprocessing
import  time
import os
def study(name,age):
    for i in range(0, 101):
        print(f"学习{i}")
        time.sleep(0.3)


def eat():
    for i in range(0, 101):
        print(f"吃东西{i}")
        time.sleep(0.3)
if __name__=='__main__':
    print(f"主进程的id是{os.getpid()},父进程的id{os.getppid()}")
study_process=multiprocessing.Process(target=study,args=('张三',18))
study_process1=multiprocessing.Process(target=eat,args=('张三',18))
study_process.start()
study_process1.start()