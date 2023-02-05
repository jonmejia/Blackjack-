import random

cards = []

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

ranks = [
    {"rank":"Ace","value":11},
    {"rank":"1","value":1},
    {"rank":"2","value":2},
    {"rank":"3","value":3},
    {"rank":"4","value":4},
    {"rank":"5","value":5},
    {"rank":"6","value":6},
    {"rank":"7","value":7},
    {"rank":"8","value":8},
    {"rank":"9","value":9},
    {"rank":"Jack","value":10},
    {"rank":"Queen","value":10},
    {"rank":"King","value":10},
    ]

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
print((card[0]["value"]))
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


