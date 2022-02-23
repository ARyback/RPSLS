from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        #Define user selection if press 0 grab at index list
        pass