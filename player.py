class Player:

    def __init__(self, name):

        self.name = name
        self.player_cards = []

    def add_card(self, new_card):
        if type(new_card) == type([]):
            self.player_cards.extend(new_card)
        else:
            self.player_cards.append(new_card)

    def __str__(self):
        return f'Player {self.name} {len(self.player_cards)} cards'

