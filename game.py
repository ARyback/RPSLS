from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        pass

    def run_game(self):
        self.player_one = Human(input("Please enter your name: "))
        print(self.player_one.name)
        self.player_two = AI("Computer player")
        print(self.player_two.name)
        print(f"This game will face off {self.player_one.name} versus {self.player_two.name}!")
        self.faceoff(self.player_one, self.player_two)
        print(self.player_one.gesture_selected)
        print(self.player_two.gesture_selected)
        self.victory(self.player_one, self.player_two)
        pass

    def faceoff(self, player_one, player_two):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        pass

    def victory(self, player_one, player_two):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.comparison_p1_winner(player_one,player_two)
            self.comparison_p2_winner(player_one,player_two)
        pass
            
    def comparison_p1_winner(self, player_one, player_two):
        if self.player_one.gesture_selected == self.player_one.gesture_list[0] and (self.player_two.gesture_selected == self.player_two.gesture_list[2] or self.player_two.gesture_selected == self.player_two.gesture_list[3]):
            self.player_one.score += 1
            print(f"{self.player_one.gesture_selected} wins this round!")
        elif self.player_one.gesture_selected == self.player_one.gesture_list[1] and (self.player_two.gesture_selected == self.player_two.gesture_list[0] or self.player_two.gesture_selected == self.player_two.gesture_list[4]):
            self.player_one.score += 1
            print(f"{self.player_one.gesture_selected} wins this round!")
        elif self.player_one.gesture_selected == self.player_one.gesture_list[2] and (self.player_two.gesture_selected == self.player_two.gesture_list[1] or self.player_two.gesture_selected == self.player_two.gesture_list[3]):
            self.player_one.score += 1
            print(f"{self.player_one.gesture_selected} wins this round!")
        elif self.player_one.gesture_selected == self.player_one.gesture_list[3] and (self.player_two.gesture_selected == self.player_two.gesture_list[4] or self.player_two.gesture_selected == self.player_two.gesture_list[1]):
            self.player_one.score += 1
            print(f"{self.player_one.gesture_selected} wins this round!")
        elif self.player_one.gesture_selected == self.player_one.gesture_list[4] and (self.player_two.gesture_selected == self.player_two.gesture_list[2] or self.player_two.gesture_selected == self.player_two.gesture_list[0]):
            self.player_one.score += 1 
            print(f"{self.player_one.gesture_selected} wins this round!")
        else:
            pass
        pass

    def comparison_p2_winner(self, player_one, player_two):
        if self.player_two.gesture_selected == self.player_two.gesture_list[0] and (self.player_one.gesture_selected == self.player_one.gesture_list[2] or self.player_one.gesture_selected == self.player_one.gesture_list[3]):
            self.player_two.score += 1
            print(f"{self.player_two.gesture_selected} wins this round!")
        elif self.player_two.gesture_selected == self.player_two.gesture_list[1] and (self.player_one.gesture_selected == self.player_one.gesture_list[0] or self.player_one.gesture_selected == self.player_one.gesture_list[4]):
            self.player_two.score += 1
            print(f"{self.player_two.gesture_selected} wins this round!")
        elif self.player_two.gesture_selected == self.player_two.gesture_list[2] and (self.player_one.gesture_selected == self.player_one.gesture_list[1] or self.player_one.gesture_selected == self.player_one.gesture_list[3]):
            self.player_two.score += 1
            print(f"{self.player_two.gesture_selected} wins this round!")
        elif self.player_two.gesture_selected == self.player_two.gesture_list[3] and (self.player_one.gesture_selected == self.player_one.gesture_list[4] or self.player_one.gesture_selected == self.player_one.gesture_list[1]):
            self.player_two.score += 1
            print(f"{self.player_two.gesture_selected} wins this round!")
        elif self.player_two.gesture_selected == self.player_two.gesture_list[4] and (self.player_one.gesture_selected == self.player_one.gesture_list[2] or self.player_one.gesture_selected == self.player_one.gesture_list[0]):
            self.player_two.score += 1
            print(f"{self.player_two.gesture_selected} wins this round!")
        else:
            pass


new_game = Game()
new_game.run_game()  