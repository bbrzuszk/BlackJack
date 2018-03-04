from BlackJackCards import *

def getMove():
    return input("Would you like to hit or stay").upper()

def displayPlayers(players):
    for player in players:
        print(player)



numPlayers = int(input("Number of players: "))
players = []
deck = BlackJackDeck()
for i in range(numPlayers + 1):
    if i == numPlayers:
        players.append(BlackJackPlayer("Dealer"))
    else:
        players.append(BlackJackPlayer(BlackJackPlayer.getName()))


deck.dealCard(players, 2)
players[-1].cards[0].flipCard()

displayPlayers(players)

for i in range(len(players)-1):
    move = None
    while move != "STAY":
        move = getMove()
        if move == "HIT":
            players[i].addCard(deck.cards.pop(0))
            if players[i].isBust():
                print("Bust")
                move = "STAY"
        displayPlayers(players)
        print()
    move = None
players[-1].cards[0].flipCard()
displayPlayers(players)
while players[-1].getTotal() < 17:
    players[-1].addCard(deck.cards.pop(0))
    displayPlayers(players)
    if players[-1].isBust():
        print("Dealer Bust")
