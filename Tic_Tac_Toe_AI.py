
#				⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⡀⠀⠀⠀⠀    ⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#				⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣠⡖⠁⠀⠀⠀⠀⠀⠀    ⢲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
#				⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀
#				⠀⠀⠀⠀⠀⠀ ⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⣿⣇⠀⠀⠀⠀⠀⠀⠀
#				⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⢀⣀⣤⣤⣤⣤⣀⡀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀
#				⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣔⢿⡿⠟⠛⠛⠻⢿⡿⣢⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
#				⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣷⣤⣀⡀⢀⣀⣤⣾⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀
#				⠀⠀⢠⣾⣿⡿⠿⠿⠿⣿⣿⣿⣿⡿⠏⠻⢿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣷⡀⠀⠀
#				⠀⢠⡿⠋⠁⠀⠀⢸⣿⡇ ⠉⠻⣿⠇♥️⠸⣿⡿⠋⢰⣿⡇⠀⠀⠈⠙⢿⡄⠀
#				⠀⡿⠁⠀⠀⠀⠀⠘⣿⣷⡀⠀⠰⣿⣶⣶⣿⡎⠀⢀⣾⣿⠇⠀⠀⠀⠀⠈⢿⠀
#				⠀⡇⠀⠀⠀⠀⠀⠀⠹⣿⣷⣄⠀⣿⣿⣿⣿⠀⣠⣾⣿⠏⠀⠀⠀⠀⠀⠀⢸⠀
#				⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⢇⣿⣿⣿⣿⡸⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠀
#				⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#				⠀⠀⠀⠐⢤⣀⣀⢀⣀⣠⣴⣿⣿⠿⠋⠙⠿⣿⣿⣦⣄⣀⠀⠀⣀⡠⠂⠀⠀⠀
#				⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀
#
#						 MADE WITH L♥️VE BY
#				        CHAKRAVARTHI BAGULA


import sys
import time
import random


def readXandY():
    try:
        x, y = input("\n\tEnter row column 'row col'(0 0 ,0 1 ,...) :").split()
        x = int(x)
        y = int(y)
        while x > 2 or y > 2 or x < 0 or y < 0:
            print("\n\tx and y must be 0 <= x <= 2 , 0 <= y <= 2.\n\tPlease Enter Again.")
            return readXandY()
    except:
        print("\n\n\tAn Error Occured while reading the input.\n\tTry entering the input x y spearated by a space.")
        return readXandY()
    return x, y


def wannaPlayAgain():
    choice = input("\n\tWant To Play Again (y/n) :")
    return choice != 'n'


def printBoard(board):
    print("\n\n\n")
    print("\t\t   0    1   2")
    print("\t\t  ♪" + "————"*3 + "♪")
    for i in range(3):
        print("\t\t%d |" % i, end="")
        for j in range(3):
            if board[i][j]:
                print(" %s " % board[i][j], end="|")
            else:
                print("   ", end="|")
        print()
        print("\t\t  ♪"+"————"*3 + "♪")
    print("\n\n")


def calculateRow(board, pos, player):
    x = pos[0]
    row = [board[x][0], board[x][1], board[x][2]]
    if player not in row:
        return 1
    for i in row:
        if i != "" and i != player:
            return 0
    return row.count(player)+1


def calculateCol(board, pos, player):
    y = pos[1]
    col = [board[0][y], board[1][y], board[2][y]]
    if player not in col:
        return 1
    for i in col:
        if i != "" and i != player:
            return 0
    return col.count(player)+1


def calculateDiag1(board, pos, player):
    diag = [board[0][0], board[1][1], board[2][2]]
    if player not in diag:
        return 1
    for i in diag:
        if i != "" and i != player:
            return 0
    return diag.count(player)+1


def calculateDiag2(board, pos, player):
    diag = [board[2][0], board[1][1], board[0][2]]
    if player not in diag:
        return 1
    for i in diag:
        if i != "" and i != player:
            return 0
    return diag.count(player)+1


def availableLocations(board):
    return [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == ""]


def getScore(board, pos, comp):
    """
    Calculates Score for a given pos on the board
    Scoring:
        if opposite pawn present in the line score will be 0
        no of occurances of 'comp' + 1

    """
    rows = calculateRow(board, pos, comp)
    cols = calculateCol(board, pos, comp)
    diag1, diag2 = 0, 0
    if pos[0] == pos[1]:
        diag1 = calculateDiag1(board, pos, comp)
    if pos[0] + pos[1] == 2:
        diag2 = calculateDiag2(board, pos, comp)
    scores = [rows, cols, diag1, diag2]
    return max(scores), scores.count(max(scores))


def getMaxScore(favour):
    maxScore, maxCount = 0, 0
    for p in favour:
        score, tot = favour[p]
        if score > maxScore or (score >= maxScore and tot >= maxCount):
            maxScore, maxCount = score, tot
    return maxScore, maxCount


def getValues(favour, maxScore, maxCount):
    ps = []
    for p in favour:
        if favour[p][0] == maxScore and favour[p][1] == maxCount:
            ps.append(p)
    return ps


def getPositions(board, tk):
    """
        Returns the list of locations of 'board' that conatains a specific character 'tk'
    """
    return [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == tk]


def nextMove(board, comp):
    # Returns the next possible move for computer
    pos = getPositions(board, "")
    opposite = "O" if comp == "X" else "X"
    # if no move is played
    # then going with corners is best option
    if len(pos) == 9:
        return random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
    # in first case we have 
    if len(pos) == 7:
        loc = getPositions(board, comp)
        if board[1][1] == "":
            nloc = getPositions(board, opposite)
            x, y = loc[0]
            if nloc[0][0] == x:
                return (2-x, y)
            elif nloc[0][1] == y:
                return (x, 2-y)
            if x == y:
                return random.choice([(2-x, y), (x, 2-y)])
            else:
                return random.choice([(0, 0), (2, 2)])
        else:
            return 2-loc[0][0], 2-loc[0][1]
    # Save the favourable cases
    favour = dict()
    # Not Favourable Cases
    notFavour = dict()
    for p in pos:
        score, count = getScore(board, p, comp)
        favour[p] = [score, count]
        score, count = getScore(board, p, opposite)
        notFavour[p] = [score, count]
    maxScore, maxCount = getMaxScore(favour)
    nmaxScore, nmaxCount = getMaxScore(notFavour)
    if maxScore >= 3:
        return getValues(favour, maxScore, maxCount)[0]
    else:
        if nmaxScore > 2:
            return getValues(notFavour, nmaxScore, nmaxCount)[0]
        elif nmaxScore == 2:
            ps = getValues(notFavour, nmaxScore, nmaxCount)
            if len(ps) == 1:
                return ps[0]
            else:
                ps = getValues(favour, maxScore, maxCount)
                ps = [(x, y) for x, y in ps if abs(x-y) != 2]
                return random.choice(ps)

        if nmaxCount > maxCount:
            return getValues(notFavour, nmaxScore, nmaxCount)[0]
    return getValues(favour, maxScore, maxCount)[0]


def tie(board):
    """
        Returns True if game is tied 
        False otherwise
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return False
    return True


def gameOver(board):
    
    """ 
    Checks whether the game is over 
    
    Returns 
        player pawn if someone won
        "tie" if game tied
        False otherwise
    """
    for i in range(3):
        # Checks the column 
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        # Checks the row
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # Check the daigonals
    if board[1][1] != "" and (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]
    if tie(board):
        return "tie"
    return False


def startMultiplayerGame():
    """
    Two players will play the game on 3 x 3 grid
        player 1 - O
        player 2 - X
    """
    global player1, player2
    board = [["" for i in range(3)] for j in range(3)]
    # who start first ?
    nextPlayer = random.choice([player1, player2])
    print("\n\n\tLets Start..")
    printBoard(board)
    while True:
        currentPlayer = nextPlayer
        if currentPlayer == player1:
            print("\n\tIts player 1's Turn.\n\tEnter the next pawn location row,col .")
            nextPlayer = player2
        else:
            print("\n\tIts player 2's Turn.\n\tEnter the next pawn location row,col .")
            nextPlayer = player1
        x, y = readXandY()

        # If the current location is already occupied
        # Ask the user to enter a empty location
        while board[x][y] != "":

            print(
                "\n\tYou Can't Place Here It is Already Ocuupied.\n\tPlease Enter Different location.")
            x, y = readXandY()
        # update board
        board[x][y] = currentPlayer
        printBoard(board)
        # check if game is over
        isGameOver = gameOver(board)
        if isGameOver:
            if isGameOver == player1:
                print("\n\tPlayer 1 Won. Congratulations🎉🎊🎈")
            elif isGameOver == player2:
                print("\n\tPlayer 2 Won. Congratulations🎉🎊🎈")
            else:
                print("\n\n\tHmppppp!!Match Tied.")
            break

    return True


def Multiplayer():
    global player1, player2, pawns
    rInt = random.choice([0, 1])
    player1 = pawns[rInt]
    player2 = pawns[1-rInt]
    print("\tPlayer1 Pawn :"+player1 + "\n\tplayer2 Pawn :"+player2+"\n\n")
    startMultiplayerGame()
    while wannaPlayAgain():
        print("\n\tStarting Game...")
        startMultiplayerGame()
    print("\n\tThanks for Playing..Returning to main menu")


def PlayerVsComputer():
    # player vs computer
    board = [["" for i in range(3)] for j in range(3)]
    turn = random.choice([computer, player])
    if turn == computer:
        print("\n\tComputer Goes First..")
    else:
        print("\n\tYou Go First..")
    printBoard(board)
    while True:
        currentPlayer = turn
        if currentPlayer == computer:
            print("")
            x, y = nextMove(board, computer)
            cnt = 0
            while cnt < 4:
                print("\tComputer is making its move"+"."*((cnt)+1), end="\r")
            #	time.sleep(0.5)
                cnt += 1
            turn = player
            board[x][y] = computer
            print("\n\tComputer Choice :- x = %d , y = %d." % (x, y))
        else:
            x, y = readXandY()
            turn = computer
            while board[x][y] != "":
                print(
                    "\n\tYou Can't Place Here It is Already Ocuupied.\n\tPlease Enter Different location.")
                x, y = readXandY()
            board[x][y] = player
            print("\n\tPlayer choice :- x = %d ,y = %d." % (x, y))
        printBoard(board)
        isGameOver = gameOver(board)
        print(isGameOver)
        if isGameOver:
            if isGameOver == computer:
                print(
                    "\n\tHurray!! Computer (%s) Won..\n\tBetterLuck Next Time." % computer)
            elif isGameOver == player:
                print("\n\tCongratulations You (%s) Won." % player)
            else:
                print("\n\n\tHmppppp!!Match Tied.")
            break


def vsComputer():
    global computer, player, pawns
    rInt = random.choice([0, 1])
    computer = pawns[rInt]
    player = pawns[1-rInt]
    print("\tPlayers Pawn :"+player + "\n\tComputer Pawn :"+computer+"\n\n")
    PlayerVsComputer()
    while wannaPlayAgain():
        PlayerVsComputer()
    print("\n\tThanks For Playing.Returning to mainmenu")


# main
if __name__ == "__main__":
    computer = ""
    player = ""
    # multiplayer
    player1 = ""
    player2 = ""
    pawns = ["X", "O"]
    while 1:
        print("\t\t♪♪-------------------------------♪♪")
        print("\t\t|        ♠ TIC TAC TOE ♠       |")
        print("\t\t♪♪-------------------------------♪♪")
        print("\n\n\tMenu Options.")
        print("\n\t1.Multiplayer\n\t2.vs Computer\n\t3.exit")
        while True:
            try:
                choice = int(input("\n\tEnter Your Choice:"))
                if choice <= 3 and choice >= 1:
                    break
                print("\n\tInvalid Option Entered.Please Enter Again")
            except:
                print(
                    "\n\tAn unknown Error occured.\n\tPlease give a integer input 1 or 2 or 3.\n")
        if choice == 1:
            Multiplayer()
        elif choice == 2:
            vsComputer()
        else:
            print("\tThanks For Playing.Bye")
            break
