from BlackJackCards import *

numPlayers = int(input("How many players"))
players = []
for i in range(numPlayers):
    players.append(BlackJackPlayer(BlackJackPlayer.getName()))

dealer = BlackJackDealer()
deck = BlackJackDeck()

