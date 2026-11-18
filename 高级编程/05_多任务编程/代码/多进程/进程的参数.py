"""
依旧是三步走导入，创建，激活
"""
import multiprocessing
import time
#创建两个子进程
def study(name,age):
    for i in range(1,101):
        print(f"学习{i}")
        time.sleep(0.2)

def eat(name,age):
    for i in range(1,101):
        print(f"吃东西{i}")
        time.sleep(0.2)
if __name__=='__main__':
    study_process=multiprocessing.Process(target=study,args=("张三",18))
    eat_process=multiprocessing.Process(target=eat,kwargs={'name':'张三','age':18})


    study_process.start()
    eat_process.start()