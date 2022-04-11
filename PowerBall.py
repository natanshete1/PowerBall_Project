import random

class powerball:

    def __init__(self):
        self.guessed_numbers = []
        self.strong_number = []
        self.lucky_number = []
        self.luky_storngnumber = []
    print("today's powerball winning numbers:")

    def white_balls(self):
        for x in range(5):
            number = random.randint(1, 20)
            self.strong_number.append(number)
        print(self.strong_number)

    def strong_ball(self):
        print("your lucky numbers:")
        for x in range(5):
            number = random.randint(1, 10)
            self.guessed_numbers.append(number)
        print(self.guessed_numbers)
        print("try again")

pb = powerball()
pb.guessed_numbers = []
pb.white_balls()
pb.strong_ball()
