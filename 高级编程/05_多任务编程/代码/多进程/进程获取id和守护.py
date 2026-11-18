"""
课件 2.3 获取进程编号 + 2.4.2 守护进程

重点：
- os.getpid()：当前进程编号；os.getppid()：父进程编号（p = parent）
- multiprocessing.current_process().pid 也能拿编号；.name 拿进程名（主进程 MainProcess、子进程 Process-1）
- 默认：主进程退出前会等待所有非守护子进程执行结束后一并销毁
- daemon=True：守护进程，主进程退出后子进程直接销毁，不再执行子进程代码
  注意：必须在 start() 之前设置
"""
import multiprocessing
import time
import os


# ========== ① 获取进程编号 ==========
def music(num):
    print('music>> 进程编号 %d，父进程编号 %d' % (os.getpid(), os.getppid()))
    for i in range(num):
        print('听音乐...')
        time.sleep(0.2)


def coding(count):
    print('coding>> 进程编号 %d，父进程编号 %d' % (os.getpid(), os.getppid()))
    for i in range(count):
        print('敲代码...')
        time.sleep(0.2)


# ========== ② 守护进程 ==========
def work():
    for i in range(10):
        print('工作中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # ---- ① 获取进程编号：每个进程编号不同，子进程的父进程编号 = 主进程编号 ----
    print('① 获取进程编号'.center(50, '='))
    print('主进程>> 编号 %d，进程名 %s' % (os.getpid(), multiprocessing.current_process().name))

    music_process = multiprocessing.Process(target=music, args=(3,))
    coding_process = multiprocessing.Process(target=coding, kwargs={'count': 3})

    music_process.start()
    coding_process.start()
    time.sleep(2)  # 等两个子进程跑完，避免和②的输出混在一起

    # ---- ② 守护进程：daemon=True 必须在 start() 之前设置 ----
    print('② 守护进程'.center(50, '='))
    work_process = multiprocessing.Process(target=work)
    work_process.daemon = True  # 设置守护：主进程退出后子进程直接销毁
    work_process.start()

    time.sleep(1)
    print('主进程执行完毕 → 守护子进程被直接销毁，不再输出"工作中..."')
