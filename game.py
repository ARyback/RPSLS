from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        pass

    def run_game(self):
        self.player_one = Human(input("Please enter your name: "))
        self.player_two = AI("Computer player")
        pass

    