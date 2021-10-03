class Cash:

    def __init__(self, total_cash = 5000):
        self.total_cash = total_cash
        self.bet = 0

    def win_the_bet(self):
        self.total_cash += self.bet

    def lose_the_bet(self):
        self.total_cash -= self.bet