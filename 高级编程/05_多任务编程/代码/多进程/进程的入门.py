"""
要明确进程是为了cpu资源更好的利用
首先导入进程的包，2.创建好进程对象，3，激活进程
注意的地方，target==不要括号
同时主程序要写在if __name__=='__main__'

"""
import time
import multiprocessing
#先建立两个没有加进程的函数
def A():
    print("学习")
    time.sleep(3)

def B():
    print("吃东西")
    time.sleep(0.2)

if __name__ == '__main__':
#创建好进程对象
    process=multiprocessing.Process(target=A)#切记不要有括号那是调用函数了
    prcess2=multiprocessing.Process(target=B)

#激活进程
    process.start()
    prcess2.start()