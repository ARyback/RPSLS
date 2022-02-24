from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.gesture_selected = self.gesture_list[self.choose_gesture()]
    
    def choose_gesture(self):
        while gesture_index != 0 and gesture_index != 1 and gesture_index != 2 and gesture_index != 3 and gesture_index != 4:
            gesture_index = int(input(f"Oops! Try again! Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, and 4 for Spock!"))
            return gesture_index
        pass


