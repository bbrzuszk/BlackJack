import random

class Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["C","S","H","D"]
    def __init__(self, rank, suit, isFaceUp = True):
        self.rank = rank
        self.suit = suit
        self.isFaceUp = isFaceUp

    def __str__(self):
        if self.isFaceUp:
            return str(self.rank)+str(self.suit)
        else:
            return "XX"

    def flipCard(self):
        if self.isFaceUp:
            self.isFaceUp = False
        else:
            self.isFaceUp = True

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if len(self.cards) == 0:
            return "<Empty Hand>"
        output = ""
        for card in self.cards:
            output += card.__str__() + "\t"
        return output

    def addCard(self, card):
        self.cards.append(card)

    def giveCard(self, card, otherHand):
        if card in self.cards:
            self.cards.remove(card)
            otherHand.addCard(card)

    def clearCards(self):
        self.cards = []


class Deck(Hand):

    def __init__(self):
        super(Deck, self).__init__()
        self.populate()
        self.shuffle()

    def populate(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.addCard(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)


    def dealCard(self, hands, numberOfCards):
        for i in range(numberOfCards):
            for hand in hands:
                if len(self.cards)!=0:
                    self.giveCard(self.cards[0], hand)
                else:
                    break

