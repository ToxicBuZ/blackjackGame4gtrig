import card as Card
import random
from random import shuffle

card_types = ('spades', 'clubs', 'diamonds', 'hearts')
card_names = ( 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
               'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = { 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
                'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
                'Queen': 10, 'King': 10, 'Ace': 11}

class Deck: 

    def __init__(self):
        
        self.deck = []
        for type in card_types:
            for name in card_names:

                new_card = Card.Card(type, name)

                self.deck.append(new_card)
        
        random.shuffle(self.deck)

    def __str__(self):
        deck_size = ''
        for card in self.deck:
            deck_size += '\n'+ card.__str__()
        return 'The deck has: ' + deck_size

    def draw_card(self):
        card = self.deck.pop()
        return card
        


