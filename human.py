from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.gesture_selected = None  

    def choose_gesture(self):
        user_choice = input(f"Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, and 4 for Spock!")
        while user_choice != "0" and user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
            user_choice = input(f"Oops! Try again! Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, and 4 for Spock!")
        if user_choice == "0":
            user_choice = int(user_choice)
            self.gesture_selected = self.gesture_list[user_choice]
        elif user_choice == "1":
            user_choice = int(user_choice)
            self.gesture_selected = self.gesture_list[user_choice]
        elif user_choice == "2":
            user_choice = int(user_choice)
            self.gesture_selected = self.gesture_list[user_choice]
        elif user_choice == "3":
            user_choice = int(user_choice)
            self.gesture_selected = self.gesture_list[user_choice]
        elif user_choice == "4":
            user_choice = int(user_choice)
            self.gesture_selected = self.gesture_list[user_choice]
        else:
            print("There was an error~!")
        pass

# new = Human('fred')
# new.choose_gesture()
# print(new.gesture_selected)

