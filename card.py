card_types = ('spades', 'clubs', 'diamonds', 'hearts')
card_names = ( 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
               'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = { 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
                'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
                'Queen': 10, 'King': 10, 'Ace': 11}

class Card:

    def __init__(self,card_type, card_name):
        self.type = card_type
        self.name = card_name
        self.value = card_values[card_name]


    def __str__(self):
        return self.name + " of " + self.type