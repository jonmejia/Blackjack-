import random

cards = []

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

#loops through suits and ranks to build a deck of cards
for suit in suits:
    n = len(ranks)-1
    while n > -1:
        cards.append([ranks[n],suit])
        n -=1

#shuffles cards
def shuffle():
    random.shuffle(cards)

#deals cards
def deal(number_of_cards = 1):
    dealt_cards = []
    while number_of_cards > 0:
        card = cards.pop()
        dealt_cards.append(card)
        number_of_cards -= 1
    return dealt_cards

shuffle()

card = deal(1)[0]

# hand = deal(2)
# card = hand[0]
# rank = card[0]

# if rank == "Ace":
#     value = 11
# elif rank == "Jack" or rank == "Queen" or rank == "King":
#     value = 10
# else:
#     value = int(rank)

# rank_dict={ "rank": rank, "value":value}

# print(f"hand: {hand}")
# print(f"card: {card}")
# print(rank_dict["rank"], rank_dict["value"])


