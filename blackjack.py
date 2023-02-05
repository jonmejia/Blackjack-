cards = []
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
ranks = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
for suit in suits:
    n = len(ranks)-1
    while n > -1:
        print([ranks[n],suit])
        n -=1
