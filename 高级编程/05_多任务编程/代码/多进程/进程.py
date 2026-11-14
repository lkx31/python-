import time
import multiprocessing


def study():
    for i in range(0, 101):
        print(f"学习{i}")
        time.sleep(0.3)


def eat():
    for i in range(0, 101):
        print(f"吃东西{i}")
        time.sleep(0.3)


if __name__ == '__main__':
    study_process = multiprocessing.Process(target=study)
    eat_process = multiprocessing.Process(target=eat)

    study_process.start()
    eat_process.start()
