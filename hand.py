from card import card_values

class Hand:

    def __init__(self):
        self.cards = []
        self.total_value = 0
        self.aces = 0

    def add_card(self, card):
        print(card.name)
        self.cards.append(card)
        self.total_value += card_values[card.name]

        if card.name == 'Ace':
            self.aces += 1

    def regulate_ace_value(self):
        while self.total_value > 21 and self.aces > 0:
            self.total_value -= 10
            self.aces -= 1