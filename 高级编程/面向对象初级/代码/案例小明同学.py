# 例如，小明同学当前体重是100kg。每当他跑步一次时，则会减少0.5kg;每当他大吃大喝一次时，则会增加2kg。请试着采用面向对象方式完成案例。
class xiaomi():
    def __init__(self):
        self.chushitizhong=100
    def run(self):
        self.chushitizhong=self.chushitizhong-0.5
    def eatfood(self):
        self.chushitizhong+=self.chushitizhong+2
Xiaomi=xiaomi()
Xiaomi.run()
Xiaomi.eatfood()
