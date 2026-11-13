class Game:
    top_socre=0
    def player_name(self,name):
        self.name=name
    @staticmethod
    def show_help():
        pass
    @classmethod
    def show_top_score(cls):
        pass
    def start_game(self):
        pass

Game.top_socre
Game.show_top_score()
game=Game()
game.player_name("小明")
game.start_game()
Game.show_help()