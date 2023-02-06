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
    
    def display(self, show_all_dealers_cards = False):
        print(f'''{"Dealers" if self.dealer else "Your"} hand:''')
        for index,card in enumerate(self.cards):
            if index == 0 and self.dealer == True and not show_all_dealers_cards and not self.is_blackjack:
                print("hidden")
            else:
                print(card)
        if self.dealer == False:
            print("Value:",self.get_value())

class Game:
    
    def play(self):
        game_number = 0
        games_to_play = 0
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games would you like to play? "))
            except ValueError:
                print("Please try again and enter an integer.")
        while game_number < games_to_play:
            game_number +=1
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            print()
            print("*"*30)
            print(f"game {game_number} of {games_to_play} ")
            print("*"*30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand, game_over=False):
                continue

            choice = ""
            while player_hand.get_value() <21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h","s","hit","stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S)").lower()
                    print()
                if choice in ['hit','h']:
                    player_hand.add_card(deck.deal())
                    player_hand.display()
                    print()
            if self.check_winner(player_hand, dealer_hand, game_over=False):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

    def check_winner(self,player_hand,dealer_hand,game_over = False):
        if not game_over:
            if player_hand.get_value() >21:
                print("Bust! Dealer wins!")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted! You win!")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both players have blackjack! Tie!")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack! You win!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackkjack! You lose!")
                return True
        else:
            if player_hand.getvalue() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.getvalue() == dealer_hand.get_value():
                print("It's a tie")
            else:
                print("You lose!")
            return True
        return False
g = Game()
g.play()