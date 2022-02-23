from player import Player
from random import randint

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        #Define random selection
        pass