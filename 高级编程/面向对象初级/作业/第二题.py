class Star(object):
    def __init__(self, name1="未知", name2="未知"):
        self.name1 = name1
        self.name2 = name2

    def playing(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        print(f"{self.name1}演出的了{self.name2}，非常好看")

    def __str__(self):
        return f"{self.name1}演出的了{self.name2}，非常好看"

    def __del__(self):
        print(f"{self.name1}我不喜欢")


zhouxinchi = Star()

for i in range(3):
    name1 = input("请输入明星名字：")
    name2 = input("请输入明星电影：")
    zhouxinchi.playing(name1, name2)
    print(zhouxinchi)