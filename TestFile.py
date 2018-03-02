from BlackJackCards import *

deck = BlackJackDeck()
hands = []
for i in range(3):
    hands.append(Hand())

deck.dealCard(hands, 4)
for hand in hands:
    print(hand)