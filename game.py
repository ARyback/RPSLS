from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        pass

#Provides a method to run the primary activities of the game
    def run_game(self):
        self.player_choice()
        self.victory()
        pass

#Allows a user to decide which player plays the game
    def player_choice(self):
        user_input = input("Enter 1 for human vs human, enter 2 for human vs AI, and enter 3 for AI vs AI: ")
        if user_input == "1": 
            self.player_one = Human(input("Please enter your name: "))
            self.player_two = Human(input("Please enter your name: "))
            print(f"This game will face off {self.player_one.name} versus {self.player_two.name}!")
        elif user_input == "2":
            self.player_one = Human(input("Please enter your name: "))
            self.player_two = AI("Computer")
            print(f"This game will face off {self.player_one.name} versus {self.player_two.name}!")
        elif user_input == "3":
            self.player_one = AI("Computer 1")
            self.player_two = AI("Computer 2")
            print(f"This game will face off {self.player_one.name} versus {self.player_two.name}!")
        else:
            self.player_choice()
        pass

#Executes and describes the face off of thorwing a gesture
    def faceoff(self):
        self.player_one.choose_gesture()
        print(f"{self.player_one.name} throws {self.player_one.gesture_selected}!")
        self.player_two.choose_gesture()
        print(f"{self.player_two.name} throws {self.player_two.gesture_selected}!")
        self.comparison(self.player_one, self.player_two)
        pass

#Executes who wins the total game
    def victory(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.faceoff()
        if self.player_one.score == 2:
            print(f"{self.player_one.name} wins the whole game!")
        else:
            print(f"{self.player_two.name} wins the whole game!")
        pass

#Determines the outcome of a specific round          
    def comparison(self, x_player, y_player):
        if x_player.gesture_selected == y_player.gesture_selected:
            print("It's a tie! Throw again!")
        elif x_player.gesture_selected == x_player.gesture_list[0]:
            if y_player.gesture_selected == y_player.gesture_list[2] or y_player.gesture_selected == y_player.gesture_list[3]:
                x_player.score += 1
                print(f"{x_player.name} wins this round! Their score is {x_player.score}")
            else:
                y_player.score += 1
                print(f"{y_player.name} wins this round! Their score is {y_player.score}")
        elif x_player.gesture_selected == x_player.gesture_list[1]:
            if y_player.gesture_selected == y_player.gesture_list[0] or y_player.gesture_selected == y_player.gesture_list[4]:
                x_player.score += 1
                print(f"{x_player.name} wins this round! Their score is {x_player.score}")
            else:
                y_player.score += 1
                print(f"{y_player.name} wins this round! Their score is {y_player.score}")
        elif x_player.gesture_selected == x_player.gesture_list[2]:
            if y_player.gesture_selected == y_player.gesture_list[1] or y_player.gesture_selected == y_player.gesture_list[3]:
                x_player.score += 1
                print(f"{x_player.name} wins this round! Their score is {x_player.score}")
            else:
                y_player.score += 1
                print(f"{y_player.name} wins this round! Their score is {y_player.score}")
        elif x_player.gesture_selected == x_player.gesture_list[3]:
            if y_player.gesture_selected == y_player.gesture_list[4] or y_player.gesture_selected == y_player.gesture_list[1]:
                x_player.score += 1
                print(f"{x_player.name} wins this round! Their score is {x_player.score}")
            else:
                y_player.score += 1
                print(f"{y_player.name} wins this round! Their score is {y_player.score}")
        elif x_player.gesture_selected == x_player.gesture_list[4]:
            if y_player.gesture_selected == y_player.gesture_list[2] or y_player.gesture_selected == y_player.gesture_list[0]:
                x_player.score += 1
                print(f"{x_player.name} wins this round! Their score is {x_player.score}")
            else:
                y_player.score += 1
                print(f"{y_player.name} wins this round! Their score is {y_player.score}")
        else:
            pass
        pass

