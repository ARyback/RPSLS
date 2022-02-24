from player import Player
from random import randint

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.gesture_selected = None
    
    def choose_gesture(self):
        gesture_index = randint(0, 4)
        self.gesture_selected = self.gesture_list[gesture_index]
        pass


# new_ai = AI("Fred")
# new_ai.choose_gesture()
# print(new_ai.gesture_selected)