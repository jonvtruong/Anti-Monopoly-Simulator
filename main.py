from random import randint
class Game:
    START_BALANCE = 1500
    BOARD_SPACES = 40
    account = []
    game = True
    currentPlayer = 0
    playerPos = []


    def setupGame(self):
        print("setting up game")
        numPlayers = input("Enter number of players: ")
        account = []
        playerPos = []
        global game 
        game = False
        for p in range(0,int(numPlayers)):
            account.append(START_BALANCE)
            playerPos.append(0)

        print("Player balances: " + str(account))
    # print("Player starting posisionts: " + str(playerPos))
        currentPlayer = 0 

    def runGame(self):
        while(game):
            print("Current player: " + str(currentPlayer))
            print("Player starting position: " + str(playerPos[0]))  
            dice1 = randint(1,6)
            dice2 = randint(1,6)
            total = dice1 + dice2

            print("Rolling dice: " + str(dice1) + ", " + str(dice2))
            
            playerPos[currentPlayer] += total

            if(playerPos[currentPlayer] >= 40):
                playerPos[currentPlayer] -= 40

            print("Player " + str(currentPlayer) + " moved " + str(total) + " spaces")
            if(input("") == 'quit'):
                break

if (__name__ == '__main__'):
    start = input("1. Start game \n")
    if(start == "1"):
        game = Game()
        game.setupGame()
        game.runGame()
        



