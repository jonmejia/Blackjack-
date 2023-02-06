import random

class Card:
    def __init__ (self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return(f'{self.rank["rank"]} of {self.suit}')
class Deck:
    def __init__(self):
        self.cards = []

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
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    #shuffles cards
    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)

    #deals cards
    def deal(self,number_of_cards = 1):
        dealt_cards = []
        while number_of_cards > 0:
            if len(self.cards)>0:
                card = self.cards.pop()
                dealt_cards.append(card)
                number_of_cards -= 1
        return dealt_cards
    
class Hand:
    def __init__(self,dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value = 0
        has_ace = False
        
        for card in self.cards:
          card_value = int(card.rank["value"])
          self.value += card_value
          if card.rank["rank"] == "Ace":
              has_ace = True
        if has_ace == True and self.value >21:
            self.value -=10

    def get_value(self):
        self.calculate_value()
        return self.value
    def is_blackjack(self):
        return self.get_value() == 21
    def display(self):
        print(f'''{"Dealers" if self.dealer else "Your"} hand:''')
        for card in self.cards:
            print(card)
        if self.dealer == False:
            print("Value:",self.get_value())
       



deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(3))
hand.display()