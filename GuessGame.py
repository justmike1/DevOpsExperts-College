import random

class Game2:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def generate_number(self):
        self.secret_number = random.randint(1, self.Difficulty)

    def get_guess_from_user(self):
        self.User_Guess = int(input(f'Guess a number between 1 to {self.Difficulty}: '))

    def compare_results(self):
        i = 1
        UserWins = False
        while i < 3:
            if self.User_Guess == self.secret_number:
                print('Correct, You made it!')
                UserWins = True
                break
            else:
                print('The number you guessed is incorrect')
                i += 1
                self.get_guess_from_user()
        return UserWins


    def play(self):
        self.generate_number()
        self.get_guess_from_user()
        return self.compare_results()




