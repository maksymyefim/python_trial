import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"This is {self.rank} of {self.suit}"

test = Card(suits[0], ranks[0])

print(test)

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = " "
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.values += values[card.rank]

    def adjust_for_ace(self):
        while self.values > 21 and self.aces:
            self.values -= 10
        else:
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet += int(input("Make your bet"))
        except ValueError:
            print("Bet must be an integer")
        else:
            if chips.bet>chips.total:
                print("Your bet can't exceed",chips.total)
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Would you like to hit or stand? Type 'h' or 's'")
        if x[0].lower() == "h":
            hit(deck, hand)
        elif x[0] == "s":
            print("Player stands. Dealer is playing")
            playing = False
        else:
            print("Sorry, please try again")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card's hidden")
    print('',dealer.cards[1])
    print("\nPlayer's Hand: ", *player.card, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.card, sep='\n ')
    print("Dealer's score: ", dealer.value)
    print("\nPlayer's Hand: ", *player.card, sep='\n ')
    print("Player's score: ", player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.lose_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.win_bet()

def push(player, dealer):
    print("It's push!")
