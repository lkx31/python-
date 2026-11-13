class Sweet_tomoto:
    def __init__(self):
        self.time = 0
        self.condiment = []
        self.state_sweet = "生的"

    def roast_time(self, time):
        self.time += time
        if self.time <= 3:
            self.state_sweet = "生的"
        elif self.time <= 7:
            self.state_sweet = "半生不熟"
        elif self.time <= 12:
            self.state_sweet = "熟了"
        else:
            self.state_sweet = "烤清华"

    def Condiment(self, condiment):
        self.condiment.append(condiment)

    def __str__(self):
        return f"我考的地瓜时间是{self.time},地瓜的状态是{self.state_sweet},调料是{self.condiment}"


sweet = Sweet_tomoto()
print(sweet)
sweet.roast_time(6)
print(sweet)
sweet.Condiment("孜然")
print(sweet)
