import random

cards = []

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

ranks = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K"]

#loops through suits and ranks to build a deck of cards
for suit in suits:
    n = len(ranks)-1
    while n > -1:
        cards.append([ranks[n],suit])
        n -=1

#shuffles cards
def shuffle(deck):
    random.shuffle(deck)

#deals cards
def deal(deck, cards = 1):
    dealt_cards = []
    while cards > 0:
        card = deck.pop()
        dealt_cards.append(card)
        cards -= 1
    return dealt_cards

shuffle(cards)
hand = deal(cards,2)
card = hand[0]
print(hand)
print(card)

