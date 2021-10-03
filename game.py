import deck as Deck
import card as Card
import player as Player
import hand as Hand

def keep_playing(deck, hand):

    global player_playing

    while True:
        player_input = input('Draw or Stop? (Enter d to draw) ')
        print(player_input)
        if player_input[0].lower() == 'd':
            draw(deck, hand)
        # elif player_input[0].lower() == 's':
        else:
            print('Player stopped. Dealer turn starts')
            player_playing = False
        # else:
        #     print('Wrong input, please insert d or s !')
        #     continue
        break      

def place_bet(player_cash):

    while True:
        try:
            bet = int(input('How much money would you like to bet? '))
        except:
            print("Please provide a valid integer as input")
        else:
            if bet > player_cash:
                print("Sorry, you don't have enough money ! You currently have: {}".format(player_cash))
            else:
                break

def draw(deck, hand):
    card = deck.draw_card()
    print(card)
    hand.add_card(card)
    hand.regulate_ace_value()

def show_cards(player, dealer):
    print("\nDealer's hand:")
    for card in dealer.cards:
        print (card)

    print("\nDealer's hand: ",*dealer.cards,sep='\n')
    print(f"Dealer hand value is: {dealer.total_value}")

    print("\nPlayer's hand:")
    for card in player.cards:
        print (card)

    print("\nPlayer's hand: ",*player.cards,sep='\n')
    print(f"Player hand value is: {player.total_value}")

def player_burns(player, dealer, cash):
    print('YOU LOSE !')
    player.lose_the_bet()

def player_wins(player, dealer, cash):
    print('YOU WIN !')
    player.win_the_bet()

def dealer_burns(player, dealer, cash):
    print('DEALER BURNS !')
    player.win_the_bet()

def dealer_wins(player, dealer, cash):
    print('DEALER WINS !')
    player.lose_the_bet()

def playerVersusDealerTie(player,dealer, cash):
    print('Player and Dealer at a tie. Dealer wins')
    player.lose_the_bet()

while True:

    print("Blackjack game starts !")
    new_deck = Deck.Deck()
    
    player = Player.Player('Player1')
    player_hand = Hand.Hand()
    player_cash = player.total_cash
    place_bet(player_cash)

    dealer = Player.Player('Dealer')
    dealer_hand = Hand.Hand()
    dealer_hand.add_card(new_deck.draw_card())
    dealer_hand.add_card(new_deck.draw_card())

    player_hand.add_card(new_deck.draw_card())
    player_hand.add_card(new_deck.draw_card())

    show_cards(player_hand, dealer_hand)

    if dealer_hand.total_value == 21:
        dealer_wins(player_hand, dealer_hand, player_cash)
        break

    if player_hand.total_value == 21:
        player_wins(player_hand, dealer_hand, player_cash)
        break


    global player_playing
    while True:
        keep_playing(new_deck, player_hand)
        show_cards(player_hand, dealer_hand)

        if player_hand.total_value > 21:
            player_burns(player, dealer, player_cash)
            break

    if player_hand.total_value <= 21:

        while dealer_hand.total_value < 17:
            draw(new_deck, dealer_hand)
        
        show_cards(player_hand, dealer_hand)

        if dealer_hand.total_value > 21:
            dealer_burns(player, dealer, player_cash)
        elif dealer_hand.total_value > player_hand.total_value:
            dealer_wins(player, dealer, player_cash)
        elif dealer_hand.total_value < player_hand.total_value:
            player_wins(player, dealer, player_cash)
        else:
            playerVersusDealerTie(player, dealer, player_cash)

    print('\n Player total cash: {}'.format(player_cash))

    new_game = input('Would you like to play again? y/n ')

    if new_game[0].lower == 'y':
        player_playing = True
        continue
    else:
        print('Thanks for playing !')
        break

