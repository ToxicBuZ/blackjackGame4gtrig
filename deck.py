import card as Card
from card import card_names, card_types
import random
from random import shuffle

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
        


