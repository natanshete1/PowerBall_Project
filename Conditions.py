from Balls import *
from colorama import init, Fore, Style
init()


class Conditions(powerball):
    def __init__(self):
        super().__init__()
        self.winnumlist = self.winnum()
        self.luckynumlist = self.luckynum()

    def score(self):
        count = 0
        for i in self.winnumlist[0:5]:
            for j in self.luckynumlist[0:5]:
                if i == j:
                    count += 1
        if count == 5 and self.winnumlist[5] == self.luckynumlist[5]:
            return "Jackpot $324,000,000"
        elif count == 5 and self.winnumlist[5] != self.luckynumlist[5]:
            return "$1,000,000"
        elif count == 4 and self.winnumlist[5] == self.luckynumlist[5]:
            return "$10,000"
        elif count == 4 and self.winnumlist[5] != self.luckynumlist[5]:
            return "$100"
        elif count == 3 and self.winnumlist[5] == self.luckynumlist[5]:
            return "$100"
        elif count == 3 and self.winnumlist[5] != self.luckynumlist[5]:
            return "$7"
        elif count == 2 and self.winnumlist[5] == self.luckynumlist[5]:
            return "$7"
        elif count == 1 and self.winnumlist[5] == self.luckynumlist[5]:
            return "$4"
        elif count == 0 and self.winnumlist[5] == self.luckynumlist[5]:
            return " $4"
        else:
            return "try again!"

    def __str__(self):
        return "Today's Powerball Winning Numbers:\n" + Fore.MAGENTA + ' '.join(map(str, self.winnumlist[0:5])) +\
               Style.RESET_ALL + " " + Fore.YELLOW + ' '.join(str(self.winnumlist[5])) + Style.RESET_ALL + "\nYour Lucky numbers:\n"\
               + Fore.MAGENTA + ' '.join(map(str, self.luckynumlist[0:5])) + \
               Style.RESET_ALL + " " + Fore.YELLOW + ' '.join(str(self.luckynumlist[5])) + Style.RESET_ALL +"\n"+self.score()





