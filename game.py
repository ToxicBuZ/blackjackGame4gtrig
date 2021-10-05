import deck as Deck
import player as Player
import hand as Hand

def keep_playing(deck, hand):

    global player_playing

    while True:
        player_input = input('Draw or Stop? (Enter d to draw or s to stop) ')
        print(player_input)
        if player_input[0].lower() == 'd':
            draw(deck, hand)
        elif player_input[0].lower() == 's':
            print('Player stopped. Dealer turn starts')
            player_playing = False
        else:
            print('Wrong input, please insert d or s !')
            continue
        break

def draw(deck, hand):
    print(hand)
    card = deck.draw_card()
    hand.add_card(card)
    hand.regulate_ace_value()


def show_cards(player, dealer):

    print("\nDealer's hand: ", *dealer.cards, sep='\n')
    print(f"Dealer hand value is: {dealer.total_value}")

    print("\nPlayer's hand: ", *player.cards, sep='\n')
    print(f"Player hand value is: {player.total_value}")


def player_burns():
    print('YOU LOSE !')


def player_wins():
    print('YOU WIN !')


def dealer_burns():
    print('DEALER BURNS !')


def dealer_wins():
    print('DEALER WINS !')

def playerVersusDealerTie():
    print('Player and Dealer at a tie. Dealer wins')

while True:

    print("Blackjack game starts !")
    new_deck = Deck.Deck()
    player = Player.Player('Player1')
    player_hand = Hand.Hand()
    dealer = Player.Player('Dealer')
    dealer_hand = Hand.Hand()
    dealer_hand.add_card(new_deck.draw_card())
    dealer_hand.add_card(new_deck.draw_card())

    player_hand.add_card(new_deck.draw_card())
    player_hand.add_card(new_deck.draw_card())

    show_cards(player_hand, dealer_hand)

    if dealer_hand.total_value == 21:
        dealer_wins()
        break

    if player_hand.total_value == 21:
        player_wins()
        break

    while True:
        keep_playing(new_deck, player_hand)

        if player_hand.total_value > 21:
            player_burns()
            break

    if player_hand.total_value <= 21:

        while dealer_hand.total_value < 17:
            draw(new_deck, dealer_hand)

        if dealer_hand.total_value > 21:
            dealer_burns()
        elif dealer_hand.total_value > player_hand.total_value:
            dealer_wins()
        elif dealer_hand.total_value < player_hand.total_value:
            player_wins()
        else:
            playerVersusDealerTie()

    print('Thanks for playing !')
