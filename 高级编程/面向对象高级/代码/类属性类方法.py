class Hero:
    total_count=0
    def  __init__(self,name):
        self.name=name
        Hero.total_count+=1
    @classmethod
    def show_total_count(cls):
        print(f"创建了{Hero.total_count}")
hero1=Hero("亚瑟")
hero2=Hero("安琪拉")

print(Hero.total_count)
