card_types = ('spades', 'clubs', 'diamonds', 'hearts')
card_names = ( 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
               'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = { 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
                'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
                'Queen': 10, 'King': 10, 'Ace': 11}

class Hand:

    def __init__(self):
        self.cards = []
        self.total_value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.total_value += card_values[card.name]

        if card.name == 'Ace':
            self.aces += 1

    def regulate_ace_value(self):
        while self.total_value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1