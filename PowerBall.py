import random

#this is 4 empty list
class powerball:
    def __init__(self):
        self.guessed_numbers = []
        self.strong_number = []
        self.lukey_number = []
        self.lukey_storngnumber = []
#this is five white balls
    def white_balls(self):
        while len(self.guessed_numbers) < 5:
            number = random.randint(1, 20)
            if number not in self.guessed_numbers:
                self.guessed_numbers.append(number)
        return sorted(self.guessed_numbers)
#this is power ball
    def strong_ball(self):
        number1 = random.randint(1, 10)
        self.strong_number.append(number1)
        return self.strong_number
#this is player lukey number
    def plyer_numbers(self):
        while len(self.lukey_number) < 5:
            number = random.randint(1, 20)
            if number not in self.lukey_number:
                self.lukey_number.append(number)
        return sorted(self.lukey_number)
#this is player strong number
    def plyer_strongnumber(self):
        number1 = random.randint(1, 10)
        self.lukey_storngnumber.append(number1)
        return self.lukey_storngnumber


