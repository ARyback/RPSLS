from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.gesture_selected = None

    def choose_gesture(self):
        user_choice = input(f"Press 0 for {self.gesture_list[0]}, 1 for {self.gesture_list[1]}, 2 for {self.gesture_list[2]}, 3 for {self.gesture_list[3]}, and 4 for {self.gesture_list[4]}!")
        while user_choice != "0" and user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
            user_choice = input(f"Oops! Try again! Press 0 for {self.gesture_list[0]}, 1 for {self.gesture_list[1]}, 2 for {self.gesture_list[2]}, 3 for {self.gesture_list[3]}, and 4 for {self.gesture_list[4]}!")
        self.gesture_selected = self.gesture_list[int(user_choice)]
        # if user_choice == "0":
        # elif user_choice == "1":
        #     self.gesture_selected = self.gesture_list[int(user_choice)]
        # elif user_choice == "2":
        #     self.gesture_selected = self.gesture_list[int(user_choice)]
        # elif user_choice == "3":
        #     self.gesture_selected = self.gesture_list[int(user_choice)]
        # elif user_choice == "4":
        #     self.gesture_selected = self.gesture_list[int(user_choice)]
        # else:
        #     print("There was an error~!")
        pass

# new = Human('fred')
# new.choose_gesture()
# print(new.gesture_selected)

