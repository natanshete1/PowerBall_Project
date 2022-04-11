from Money import Money

class Massage(Money):
    def __init__(self):
     super().__init__()
    def reslut(self):
        if self.match_nums() == 5 and self.match_nums() == 1:
            return("Correct White Balls and the Powerball: Jackpot $324,000,000")
        elif self.match_nums() == 5 and self.match_strong() == 0:
            return("5 Correct White Balls, but no Powerball: $1,000,000")
        elif self.match_nums() == 4 and self.match_strong() == 1:
            return("4 Correct White Balls and the Powerball: $10,000")
        elif self.match_nums() == 4 and self.match_strong() == 0:
            return("4 Correct White Balls, but no Powerball: $100")
        elif self.match_nums() == 3 and self.match_strong() == 1:
            return("3 Correct White Balls and the Powerball: $100")
        elif self.match_nums() == 3 and self.match_strong() == 0:
            return("3 Correct White Balls, but no Powerball: $7")
        elif self.match_nums() == 2 and self.match_strong() == 1:
            return("2 Correct White Balls and the Powerball: $7")
        elif self.match_nums() == 1 and self.match_strong() == 1:
            return("1 Correct White Ball and the Powerball: $4")
        elif self.match_nums() == 0 and self.match_strong() == 1:
            return("No White Balls, Just the Powerball: $4")
        else:
            return("try again!")

    def __str__(self):
        self.player_and_lttorey ="today's Porweball winning Numbers:" + "\n"+str(self.white) +str(self.strong)+" \n"+"your lucky numbers: "+ "\n"+str(self.player) +str(self.player_num )
        self.powreball_lttorey ="You caught :Porweball numbers = "+str(self.match_nums())+" :and strong numbers = "+str(self.match_strong())

        return self.player_and_lttorey+"    \n  "+self.powreball_lttorey+"\n"+str(self.reslut())
print(Massage())





