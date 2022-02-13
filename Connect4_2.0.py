#Connect 4 (text based version)

#defining a variable to store the board
gameBoard = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]

#defining a function that prints the board for the player to see
def displayBoard(board):
    for row in board:
        print(row)

#defining a function to place pieces in the board
def placePiece(column, playerTurn):

    #defining a variable that states whether an empty slot has been found in the chosen column
    foundSlot = False

    #checking if player input is actually a column on the board
    if column != "1" and column != "2" and column != "3"  and column != "4"  and column != "5"  and column != "6"  and column != "7":
        print("That's not a real column on the board!")
    else:
        column = int(column)
        #creating a for loop that goes through the rows and finds an empty slot
        for row in range(len(gameBoard) - 1, -1, -1):
            if foundSlot == False:
                if gameBoard[row][column-1] == 0:
                    gameBoard[row][column-1] = playerTurn
                    foundSlot = True

        #printing a message if there are no more empty slots in the chosen column
        if foundSlot == False:
            print("You can't place your piece in that column!")

        else:
        #changing the player turn after a move has been made
            if playerTurn == 1:
                playerTurn = 2
            elif playerTurn == 2:
                playerTurn = 1

    #returning variables for use outside of function
    return foundSlot, playerTurn

#defining a function to check for winners
def checkWinner():

    #defines a variable that states whether a winner has been found
    foundWinner = False

    #defines a variable that states which player won (if any, 0 meaning no one)
    gameWinner = 0

    #running if no winner has been found
    if foundWinner == False:
        #checks for horizontal wins
        for row in range(len(gameBoard)):
            for piece in range(len(gameBoard[0]) - 3):
                if gameBoard[row][piece] == gameBoard[row][piece+1] == gameBoard[row][piece+2] == gameBoard[row][piece+3] and gameBoard[row][piece] != 0:
                    foundWinner = True

                    if gameBoard[row][piece] == 1:
                        gameWinner = 1
                    elif gameBoard[row][piece] == 2:
                        gameWinner = 2

    #running if no winner has been found
    if foundWinner == False:
        #checks for vertical wins
        for piece in range(len(gameBoard) - 3):
            for column in range(len(gameBoard[0])):
                if gameBoard[piece][column] == gameBoard[piece+1][column] == gameBoard[piece+2][column] == gameBoard[piece+3][column] and gameBoard[piece][column] != 0:
                    foundWinner = True

                    if gameBoard[piece][column] == 1:
                        gameWinner = 1
                    elif gameBoard[piece][column] == 2:
                        gameWinner = 2

    #running if no winner has been found
    if foundWinner == False:
        #checks for \ diagonal wins
        for row in range(len(gameBoard) - 3):
            for column in range(len(gameBoard[0]) - 3):
                if gameBoard[row][column] == gameBoard[row+1][column+1] == gameBoard[row+2][column+2] == gameBoard[row+3][column+3] and gameBoard[row][column] != 0:
                    foundWinner = True

                    if gameBoard[row][column] == 1:
                        gameWinner = 1
                    elif gameBoard[piece][column] == 2:
                        gameWinner = 2

    #running if no winner has been found
    if foundWinner == False:
        #checks for / diagonal wins
        for row in range(4, len(gameBoard)):
            for column in range(len(gameBoard[0]) - 3):
                if gameBoard[row][column] == gameBoard[row-1][column+1] == gameBoard[row-2][column+2] == gameBoard[row-3][column+3] and gameBoard[row][column] != 0:
                    foundWinner = True

                    if gameBoard[row][column] == 1:
                        gameWinner = 1
                    elif gameBoard[row][column] == 2:
                        gameWinner = 2

    #returning variables for use outside of function
    return foundWinner, gameWinner

#defining a variable that states whether the game is/should still running
gameRunning = True

#defining variable that states which player's turn it is
playerTurn = 1

#printing a title
print("Connect 4")
print("")

#running a function to display the board at the beginning of the game
displayBoard(gameBoard)

#creating a game loop that only stops when the game shouldn't be running anymore
while gameRunning:

    #taking in player input to make a move
    playerInput = input("Player " + str(playerTurn) + ", choose a column to place your piece, 1-7: ")

    #running a function to place a piece and updating player turn
    foundSlot, playerTurn = placePiece(playerInput, playerTurn)

    #checking if an empty slot on the selected column is found
    while foundSlot != True:

        #player picks another column
        playerInput = input("Player " + str(playerTurn) + ", choose a column to place your piece, 1-7: ")
        foundSlot, playerTurn = placePiece(playerInput, playerTurn)

    print("")

    #running a function to display the board
    displayBoard(gameBoard)

    #checking if a player won
    foundWinner, gameWinner = checkWinner()

    #printing win message if a winner is found
    if foundWinner == True:
        print("Player " + str(gameWinner) + " won!")

        #asking player if they would like to play again
        keepGoing = input("Would you like to play again? Type 'yes' if you do. ")
        if keepGoing == "yes":
            gameRunning = True
            print("")
            print("")
            print("")
            print("Connect 4")
            print("")
            gameBoard = [[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0]]
            displayBoard(gameBoard)
            playerTurn = 1
        else:

            #ending the game
            gameRunning = False
