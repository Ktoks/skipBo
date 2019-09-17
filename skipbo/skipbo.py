import random
import time

from pythonds.basic import stack


class Player:

    def __init__(self, name):
        self.mName = name
        self.mBuildingPile0 = stack.Stack()
        self.mBuildingPile1 = stack.Stack()
        self.mBuildingPile2 = stack.Stack()
        self.mBuildingPile3 = stack.Stack()
        self.mStockPile = []
        self.mHand = []

        self.mBuildingPile0.push("e")
        self.mBuildingPile1.push("e")
        self.mBuildingPile2.push("e")
        self.mBuildingPile3.push("e")

    def getHeads(self):
        return [self.mBuildingPile0.peek(), self.mBuildingPile1.peek(),self.mBuildingPile2.peek(), self.mBuildingPile3.peek()]

def intro():
    print("""
    Hello there! Welcome to Skip-Bo!
    Be the first person to play every card in your stock pile!
    There must be 2-6 players to enjoy this game.
    """)

def instructions():
    print("""
    With 2-4 players: everyone is dealt 30 cards into their stock pile.
    With 5-6 players: everyone is dealt 20 cards into their stock pile.
    Once the stock piles are dealt, each player's top stock card will be shown.
    Each player will have their own building pile which will display their current cards played.
    Each player will also have a discard pile where they may form sequences.
    The top card of your discard piles is available for forming sequences.
    There is a draw pile that players will draw from.
    """)

def getPlayers():
    playerNumber = input("Please input the number of players: ")
    playerList = []
    while True:
        try:
            playerNumber = int(playerNumber)
            if playerNumber < 2 or playerNumber > 6:
                playerNumber = input(
                    "Please input the number of players in format 2-6: ")
            else:
                break
        except:
            playerNumber = input(
                "Please input the number of players in format 2-6: ")
    playerNumber = int(playerNumber)
    for i in range(playerNumber):
        playerName = ""
        num = str(i + 1)
        while playerName == "":
            playerName = input("Player " + num + ": Please input your name: ")
        player = Player(playerName)
        playerList.append(player)
        # testing:
        # print(player.mName)
        # print(playerList[i].mName)
    return playerNumber, playerList

def createDeck():
    deck = []
    for i in range(12):
        for j in range(12):
            deck.append(j+1)
    deck += 18 * "s"
    # testing
    if len(deck) != 162:
        print("Create Deck Failure")
    return deck

def shuffleDeck():
    deck = createDeck()
    newDeck = []
    newDeck += 162 * "0"

    for i in range(len(newDeck)):
        newDeck[i] = random.choice(deck)
    # testing:
    # for i in range(len(newDeck)):
    #     if newDeck[i] == "0":
    #         print("Failure")
    #         exit(1)
    #     print(newDeck[i])
    return newDeck

def createStockPiles(playerNumber, playerList, deck):
    # large group
    if playerNumber > 4:
        for p in playerList:
            for i in range(20):
                p.mStockPile.append(deck.pop())
            # testing
            if len(p.mStockPile) != 20:
                print("Stock Pile failure")

    # small group
    else:
        for p in playerList:
            for i in range(30):
                p.mStockPile.append(deck.pop())
            # testing
            if len(p.mStockPile) != 30:
                print("Stock Pile failure")

def createHands(playerList, deck):
    for p in playerList:
        for i in range(5):
            p.mHand.append(deck.pop())
        # testing
        if len(p.mHand) != 5:
            print("Hand failure")
        # else:
        #     print(p.mName + ":")
        #     for i in range(len(p.mHand)):
        #         print(p.mHand[i])
    


def turn(player):
    selection = ""
    while selection != "e":
        selection = input("""
    Input l to look at your hand and the building piles.
    Input b# to play on a building pile- where the # is 
    the pile number you want to play on.
    Input e to end your turn.
    Input h for help.
    > """)
        if selection == "l":
            # create look feature
            print("Your hand: " + str(player.mHand))                # check
            print("Your building piles: " + str(player.getHeads())) # check
        
        if len(selection) == 2 and selection[0] == "b":
            # create play on a building pile feature
            # select which card you want
            # select which sequential pile to play it on
            pass

        if selection == "e":
            print("You chose to end your turn, next player's turn.")
            break

        if selection == "h":
            print("""
    Right now you can play on any building pile you own in sequence
    with what you have in your hand or your stock pile.
    Try to use from your stock pile first because once it has run out,
    you win this round and get points for each card in other players'
    stock piles.""")


def main():
    intro()
    instructions()
    gameOver = False
    playerNumber, playerList = getPlayers()
    deck = shuffleDeck()
    # testing
    # time.sleep(3)
    createStockPiles(playerNumber, playerList, deck)    # player objects hold their own stock piles
    createHands(playerList, deck)
    while not gameOver:
        for i in range(playerNumber):
            num = str(i + 1)
            print(playerList[i].mName + ": your turn. ")
            turn(playerList[i])




main()
