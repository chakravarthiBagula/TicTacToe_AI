
from time import sleep

from tkinter import Tk, Label, Button, Frame, StringVar, CENTER
import random


def checkRow(board, pos, player):
    x = pos[0]
    row = [board[x][0], board[x][1], board[x][2]]
    if player not in row:
        return 1
    for i in row:
        if i != "" and i != player:
            return 0
    return row.count(player)+1


def checkCol(board, pos, player):
    y = pos[1]
    col = [board[0][y], board[1][y], board[2][y]]
    if player not in col:
        return 1
    for i in col:
        if i != "" and i != player:
            return 0
    return col.count(player)+1


def checkDiag1(board, pos, player):
    diag = [board[0][0], board[1][1], board[2][2]]
    if player not in diag:
        return 1
    for i in diag:
        if i != "" and i != player:
            return 0
    return diag.count(player)+1


def checkDiag2(board, pos, player):
    diag = [board[2][0], board[1][1], board[0][2]]
    if player not in diag:
        return 1
    for i in diag:
        if i != "" and i != player:
            return 0
    return diag.count(player)+1


def availableLocations(board):
    return [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == ""]


def getScore(board, p, comp):
    rows = checkRow(board, p, comp)
    cols = checkCol(board, p, comp)
    diag1, diag2 = 0, 0
    if p[0] == p[1]:
        diag1 = checkDiag1(board, p, comp)

    if p[0] + p[1] == 2:
        diag2 = checkDiag2(board, p, comp)
    scores = [rows, cols, diag1, diag2]
    return max(scores), scores.count(max(scores))


def getMaxScore(favour):
    maxScore, maxCount = 0, 0
    for p in favour:
        #	#print(favour[p])
        score, tot = favour[p]
        if score > maxScore or (score >= maxScore and tot >= maxCount):
            maxScore, maxCount = score, tot
    return maxScore, maxCount


def getValues(favour, maxScore, maxCount):
    lst = []
    for p in favour:
        if favour[p][0] == maxScore and favour[p][1] == maxCount:
            lst.append(p)
    return lst


def getPositions(board, tk):
    return [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == tk]


def nextEasyMove(board):
    return random.choice(availableLocations(board))


def nextMediumMove(board, comp):
    pos = getPositions(board, "")
    opposite = "O" if comp == "X" else "X"
    favour = dict()
    notFavour = dict()
    for p in pos:
        score, count = getScore(board, p, comp)
        favour[p] = [score, score*count]
        score, count = getScore(board, p, opposite)
        notFavour[p] = [score, score*count]
    maxScore, maxCount = getMaxScore(favour)
    if maxScore == 3:
        return getValues(favour, 3, maxCount)[0]
    else:
        nmaxScore, nmaxCount = getMaxScore(notFavour)

        if nmaxScore == 3:
            return getValues(notFavour, 3, nmaxCount)[0]
    return getValues(favour, maxScore, maxCount)[0]


def nextHardMove(board, comp):
    pos = getPositions(board, "")
    # if computer starts first.
    opposite = "O" if comp == "X" else "X"
    if len(pos) == 9:
        return random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
    if len(pos) == 7:
        if board[1][1] == "":
            loc = getPositions(board, comp)
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
            loc = getPositions(board, comp)
            return 2-loc[0][0], 2-loc[0][1]
    favour = dict()
    notFavour = dict()
    for p in pos:
        score, count = getScore(board, p, comp)
        favour[p] = [score, count]
        score, count = getScore(board, p, opposite)
        notFavour[p] = [score, count]
    maxScore, maxCount = getMaxScore(favour)
    nmaxScore, nmaxCount = getMaxScore(notFavour)
    print(favour, maxScore, maxCount)
    print(notFavour, nmaxScore, nmaxCount)
    if maxScore >= 3:
        return getValues(favour, 3, maxCount)[0]
    else:
        #	notFavour = [getScore(board,p,opposite) for p in pos])

        if nmaxScore >= 2:
            ps = getValues(notFavour, 3, nmaxCount)
            print(ps)
            if len(ps) == 1:
                return ps[0]
            else:
                ps = getValues(favour, maxScore, maxCount)
                return ps[0]

        if nmaxCount > maxCount:
            return getValues(notFavour, nmaxScore, nmaxCount)[0]
    return getValues(favour, maxScore, maxCount)[0]


def tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return False
    return True


def gameOver(board, a, b):
    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[1][1] != "" and (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]
    if tie(board):
        return None
    return "no"


def callComputer(master):
    master.destroy()
    vsComputerLevels()


def callMultiPlayer(master):
    master.destroy()
    obj = Multiplayer()
    obj.startGame()


def exit(master):
    master.destroy()


def callMainMenu(master):
    master.destroy()
    mainMenu()


def mainMenu():
    root = Tk()
    root.geometry("600x600")
    root.config(bg="grey")

    title_name = Label(
        root,
        width=300,
        text="TIC TAC TOE",
        font=("Courier", 25),
        fg="#ffA0B1", bg="grey"
    )
    title_name.place(anchor="c", relx=.5, rely=0.1)

    menu_label = Label(
        root,
        width=200,
        text=" MENU ",
        font=("Arial", 20),
        fg="blue", bg="grey"
    )
    menu_label.place(anchor="c", relx=.5, rely=0.25)

    menu_frame = Frame(
        root,
        width=750, height=1200,
        border=None,
        background="grey"
    )
    menu_frame.place(anchor="c", relx=.5, rely=.5)

    Button(
        menu_frame,
        text='MULTIPLAYER',
        height=2, width=20,
        fg="white", bg="grey",
        font=("Helvetica", 10),
        command=lambda: callMultiPlayer(root),

    ).grid(row=0, column=0)

    Button(
        menu_frame,
        text='COMPUTER',
        height=2, width=20,
        font=("Helvetica", 10),
        fg="white", bg="grey",
        command=lambda: callComputer(root)
    ).grid(row=1, column=0)

    Button(menu_frame,
           text='EXIT', height=2,
           width=20, font=("Helvetica", 10),
           fg="white", bg="grey",
           command=lambda: exit(root)
           ).grid(row=2, column=0)
  #  multiplayer.place(anchor = 'c',relx = .5 ,rely = .2)
    root.mainloop()


class Computer():

    def __init__(self, mode):
        self.board = [["" for i in range(3)] for j in range(3)]
        self.root = Tk()
        self.root.geometry("600x600")
        self.mode = mode
        tnt = random.choice((1, 0))
        self.pawns = ["X", "O"]
        self.comp = self.pawns[tnt]
        self.player = self.pawns[1-tnt]
        self.turn = self.player
        self.prev = ""
        self.ans = "no"
        self.gameover = False
        self.buttons = {}
        self.turnVar = StringVar()

    def startGame(self):
        # self.player_turn = Label(
        #		self.root,
        #		text = "Player Turn ",
        #		width = 200,
        #		font = ("Arial",10),
        #		bg = "grey",
        #		fg = "#90A076",
        #		)
        #	self.player_turn.place(anchor = 'c',relx = .5,rely = .2)
        self.turnVar.set("Computer's (%s) turn" % self.comp if self.turn ==
                         self.comp else "Player's (%s) turn" % self.player)
        self.turn_label = Label(
            self.root,
            textvariable=self.turnVar,
            font=("Courier", 15),
            bg="grey",
            fg="#ffaacc", )
        self.turn_label.place(anchor='c', relx=.5, rely=.3)
        self.root.config(bg="grey")
        self.pawn_label = Label(
            self.root,
            text="COMPUTER : %s\nPLAYER -2 : %s" % (self.comp, self.player),
            width=200,
            font=("Helvetica", 15),
            bg='grey', fg='#A1B228',
        )
        self.pawn_label.place(anchor='c', relx=.5, rely=.1)
        frame1 = Frame(self.root, width=50, height=50,
                       background="blue", padx=50, pady=50)
        b1 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b1, (0, 0))
        )
        b1.grid(row=0, column=0)
        b2 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b2, (0, 1))
        )
        b2.grid(row=0, column=1)
        b3 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b3, (0, 2))
        )
        b3.grid(row=0, column=2)
        b4 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b4, (1, 0))
        )
        b4.grid(row=1, column=0)
        b5 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b5, (1, 1))
        )
        b5.grid(row=1, column=1)
        b6 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b6, (1, 2))
        )
        b6.grid(row=1, column=2)
        b7 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b7, (2, 0))
        )
        b7.grid(row=2, column=0)
        b8 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b8, (2, 1))
        )
        b8.grid(row=2, column=1)
        b9 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b9, (2, 2))
        )
        b9.grid(row=2, column=2)
        self.buttons = {(0, 0): b1, (0, 1): b2, (0, 2): b3, (1, 0): b4,
                        (1, 1): b5, (1, 2): b6, (2, 0): b7, (2, 1): b8, (2, 2): b9}
        frame1.place(anchor="c", relx=0.5, rely=0.5)
        self.bottom_frame = Frame(
            self.root,
            width=200,
            height=100,
        )
        self.back_btn = Button(
            self.bottom_frame,
            height=2,
            width=15,
            text="BACK",
            command=lambda: callVsComputer(self.root)
        )
        self.back_btn.place(anchor='c', relx=.5, rely=.5)
        self.bottom_frame.place(anchor='c', relx=0.5, rely=0.7)
        self.root.mainloop()

    def checker(self, b, pos):
        # print("btext",b['text'])
        if b['text'] == " " and self.gameover == False:
            b['text'] = self.turn
            self.board[pos[0]][pos[1]] = self.turn
            self.checkAnswer()
            if not self.gameover and self.turn == self.comp:
                if self.mode == 'easy':
                    x, y = nextEasyMove(self.board)
                    # print(x)
                elif self.mode == 'medium':
                    (x, y) = nextMediumMove(self.board, self.comp)
                elif self.mode == "hard":
                    (x, y) = nextHardMove(self.board, self.comp)
                # print(x,y,self.mode)
                self.board[x][y] = self.turn
                self.buttons[(x, y)]['text'] = self.turn
                # print(type(self.buttons[(x,y)]))
                self.checkAnswer()

    def checkAnswer(self):
        self.ans = gameOver(self.board, self.comp, self.player)
        if self.turn == self.comp:
            self.turn = self.player
            self.turnVar.set("Player's' (%s) turn" % (self.player))
        else:
            self.turn = self.comp
            self.turnVar.set("Computer's (%s) turn" % self.comp)
        if self.ans != 'no':
            self.gameover = True
            textVar = StringVar()
            textVar.set("Game Over")
            # print(self.ans)
        #	self.player_turn['text'] = "Game Over"
            self.gameoverlabel = Label(
                self.root,
                width=300,
                text="Game OVER",
                textvariable=textVar,
                font=("Courier", 10),
                bg="grey",
                fg="#ffaacc",
                justify=CENTER
            )
            self.gameoverlabel.place(anchor='c', relx=.5, rely=.3)
            textVar.set("Player  (%s) won.\nCongrats" % self.player if self.ans ==
                        self.player else "Computer (%s) won.\n" % self.comp if self.ans == self.comp else "Match Tied")
            self.root.update_idletasks()
        # printBoard(self.board)


def change(mode, master):
    master.destroy()
    obj = Computer(mode)
    obj.startGame()


def callVsComputer(master):
    master.destroy()
    vsComputerLevels()


def vsComputerLevels():

    root = Tk()
    root.geometry("600x600")
    root.config(bg="grey")
    title_name = Label(
        root,
        width=300,
        text="player Vs Computer",
        font=("Courier  , ", 15),
        fg="Yellow", bg="grey"
    )
    title_name.place(anchor="c", relx=.5, rely=0.1)

    menu_label = Label(
        root,
        width=200,
        text=" Options ",
        font=("Arial", 15),
        fg="blue", bg="grey"
    )
    menu_label.place(anchor="c", relx=.5, rely=0.25)

    menu_frame = Frame(
        root,
        width=750, height=1200,
        border=None,
        background="grey"
    )
    menu_frame.place(anchor="c", relx=.5, rely=.5)

    Button(
        menu_frame,
        text='EASY',
        height=2, width=20,
        fg="white", bg="grey",
        font=("Helvetica", 10),
        command=lambda: change("easy", root)
    ).grid(row=0, column=0)

    Button(
        menu_frame,
        text='MEDIUM',
        height=2, width=20,
        font=("Helvetica", 10),
        fg="white", bg="grey",
        command=lambda: change("medium", root)
    ).grid(row=1, column=0)

    Button(
        menu_frame,
        text='HARD',
        height=2, width=20,
        font=("Helvetica", 10),
        fg="white", bg="grey",
        command=lambda: change("hard", root)
    ).grid(row=2, column=0)

    Button(
        menu_frame,
        text='BACK',
        height=2, width=20,
        font=("Helvetica", 10),
        fg="white", bg="grey",
        command=lambda: callMainMenu(root),
    ).grid(row=3, column=0)
    root.mainloop()


class Multiplayer():

    def __init__(self):
        self.board = [["" for i in range(3)] for j in range(3)]
        self.root = Tk()
        self.root.geometry("600x600")
        self.player1 = "X"
        self.player2 = "O"
        self.turn = self.player1
        self.prev = ""
        self.ans = "no"
        self.gameover = False

    def startGame(self):
        self.turn_label = Label(
            self.root,
            text="Player 1 (%s) turn" % self.player1,
            font=("Courier", 15),
            bg="grey",
            fg="#ffaacc", )
        self.turn_label.place(anchor='c', relx=.5, rely=.3)
        self.root.config(bg="grey")
        self.pawn_label = Label(
            self.root,
            text="PLAYER -1 : %s\nPLAYER -2 : %s" % (
                self.player1, self.player2),
            width=200,
            font=("Helvetica", 15),
            bg='grey', fg='#A1B228',
        )
        self.pawn_label.place(anchor='c', relx=.5, rely=.1)
        frame1 = Frame(self.root, width=50, height=50,
                       background="blue", padx=50, pady=50)
        b1 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b1, (0, 0)),
        )
        b1.grid(row=0, column=0)
        b2 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b2, (0, 1))
        )
        b2.grid(row=0, column=1)
        b3 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b3, (0, 2))
        )
        b3.grid(row=0, column=2)
        b4 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b4, (1, 0))
        )
        b4.grid(row=1, column=0)
        b5 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b5, (1, 1))
        )
        b5.grid(row=1, column=1)
        b6 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b6, (1, 2))
        )
        b6.grid(row=1, column=2)
        b7 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b7, (2, 0))
        )
        b7.grid(row=2, column=0)
        b8 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b8, (2, 1))
        )
        b8.grid(row=2, column=1)
        b9 = Button(
            frame1,
            text=" ",
            height=2, width=2, bg="pink", fg="blue",
            bd=4,
            command=lambda: self.checker(b9, (2, 2))
        )

        b9.grid(row=2, column=2)
        frame1.place(anchor="c", relx=0.5, rely=0.5)

        self.bottom_frame = Frame(
            self.root,
            width=200,
            height=100,
        )
        self.back_btn = Button(
            self.bottom_frame,
            height=2,
            width=15,
            text="BACK",
            command=lambda: callMainMenu(self.root)
        )
        self.back_btn.place(anchor='c', relx=.5, rely=.5)
        self.bottom_frame.place(anchor='c', relx=0.5, rely=0.7)
        self.root.mainloop()

    def checker(self, b, pos):
        # print("btext",b['text'])
        if b['text'] == " " and self.gameover == False:
            b['text'] = self.turn
            self.board[pos[0]][pos[1]] = self.turn
            ans = gameOver(self.board, self.player1, self.player2)
            # print(ans)
            if ans != 'no':
                self.gameover = True
                textVar = StringVar()
                textVar.set("Game Over")
                # print(ans)
            #	self.player_turn['text'] = "Game Over"
                self.gameoverlabel = Label(
                    self.root,
                    width=300,
                    text="Game OVER",
                    textvariable=textVar,
                    font=("Courier", 10),
                    bg="grey",
                    fg="#ffaacc",
                    justify=CENTER
                )
                self.gameoverlabel.place(anchor='c', relx=.5, rely=.3)
                textVar.set("Player 1 (%s) won.\nCongrats" % self.player1 if ans ==
                            self.player1 else "Player 2 (%s) won.\nCongrats" % self.player2 if ans == self.player2 else "Match Tied")
                self.root.update_idletasks()
            # 'printBoard(self.board)
            #b['text'] = self.turn
            if self.turn == self.player1:
                self.turn = self.player2
                text = "Player 2(" + self.turn + ") Turn"
            else:
                self.turn = self.player1
                text = "Player 1(" + self.turn + ") Turn"
            self.turn_label['text'] = text
        #	self.root.update_idletasks()


def Game():
    mainMenu()


if __name__ == '__main__':
    Game()
