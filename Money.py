from PowerBall import powerball


class Money(powerball):
    def __init__(self):
        super().__init__()
        self.white = self.white_balls()
        self.strong = self.strong_ball()
        self.player = self.plyer_numbers()
        self.player_num = self.plyer_strongnumber()

    def match_nums(self):
        cuont = 0
        for i in self.white:
            if i in self.player:
                cuont += 1
        return cuont

    def match_strong(self):
        if self.strong == self.player_num:
            return 1
        else:
            return 0
