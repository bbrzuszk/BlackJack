from Cards import *

class BlackJackCard(Card):
    def __init(self, rank, suit, isFaceUp = True):
        super(BlackJackCard, self).__init(rank, suit, isFaceUp)
        self.value = self.__setValue()

    def __setValue(self):
        for i in range(Card.RANKS):
            if self.rank == Card.RANKS[i]:
                if i < 10:
                    return i + 1
                else:
                    return 10


class BlackJackHand(Hand):

    def getTotal(self):
        hasAce = False
        for card in self.cards:
            if card.rank == "A":
                hasAce = True

        total = 0
        for card in self.cards:
            total += card.value
        if hasAce and total <= 11:
            total += 10 #because Ace already registers with a value of 1

        return total

    def isBust(self):
        return self.getTotal()> 21

class BlackJackDeck(Deck):
    def __init__(self):
        super(BlackJackDeck, self).__init__()


    def populate(self):
       for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.addCard(BlackJackCard(rank, suit))


class BlackJackPlayer(object):
    def __init__(self, name):
        self.name = name
        self.hand = BlackJackHand()
        self.isPlaying = True



