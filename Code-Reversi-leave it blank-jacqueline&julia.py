"""
✦ COMP-123-03 | Final Project - Reversi ✦
by Julia Zhong, Jacqueline Ong
professor Lauren Milne
-
this file contains the entirety of our code for our adapation of
the two-player board game 'Reversi'. lines in this file which
served as tests for our code have been kept, but commented out.
"""

# - - - first section | import statements - - -
import tkinter as tk

# - - - second section | class and method definitions - - -
class Reversi:

    def __init__(self):
        """
            Creates the main window to hold our game and the instructions, reset,quit and choose
            color buttons, and draws the playing grid (the board). Creates the four starting discs
            in the center of the grid. Initializes the list of played discs to zero, then appends
            the four starting discs, and initializes the value of each playable square on the grid
            to reflect a new game state. Sets the first player to be Player 1, and creates a list
            of coordinates to help with disc creation further on in the program. Takes no inputs
            and returns nothing, assumes that the game is not over. Its buttons make callbacks to
            the instructionsCallback, quitCallback, resetGameCallback and chooseColor methods.
        """
        self.gameOver = False
        self.chooseColorTrue = False
        self.playerOne = True
        self.discList = []
        self.coordList = [[180 + 1, 180 + 1, 270 - 1, 270 - 1], [270 + 1, 270 + 1, 360 - 1, 360 - 1],
                          [270 + 1, 180 + 1, 360 - 1, 270 - 1], [180 + 1, 270 + 1, 270 - 1, 360 - 1]]
        self.gridValue = [[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, "black", "white", 0, 0],
                          [0, 0, "white", "black", 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]]

        self.mainWin = tk.Tk()
        self.mainWin.title("Reversi")
        self.titleLabel = tk.Label(self.mainWin, text="Welcome to Our Reversi!", font="Arial 20 bold", relief=tk.GROOVE,
                                   justify=tk.CENTER, bd=5)
        self.titleLabel.grid(row=0, column=1, padx=10, pady=10)

        self.testButton1 = tk.Button(self.mainWin)
        self.testButton1["text"] = "Instructions"
        self.testButton1.grid(row=2, column=0, padx=5, pady=5)
        self.testButton1["command"] = self.instructionsCallback
        self.testButton2 = tk.Button(self.mainWin)
        self.testButton2["text"] = "Quit"
        self.testButton2.grid(row=4, column=0, padx=5, pady=5)
        self.testButton2["command"] = self.quitCallback
        self.testButton3 = tk.Button(self.mainWin)
        self.testButton3["text"] = "Reset"
        self.testButton3.grid(row=3, column=0, padx=5, pady=5)
        self.testButton3["command"] = self.resetGameCallback
        self.testButton4 = tk.Button(self.mainWin)
        self.testButton4["text"] = "Choose Colors!"
        self.testButton4.grid(row=1, column=1, padx=5, pady=5)
        self.testButton4["command"] = self.chooseColor
        self.testButton5 = tk.Button(self.mainWin)

        self.canvas = tk.Canvas(self.mainWin, bg="green",
                                width=540, height=540)
        self.canvas.grid(row=2, column=1, padx=5, pady=5, rowspan=3)
        self.canvas.bind("<Button-1>", self.placeDisc)

        self.myDisc1 = self.canvas.create_oval(180+1, 180+1, 270-1, 270-1, fill="black", outline="black")
        self.myDisc2 = self.canvas.create_oval(270+1, 270+1, 360-1, 360-1, fill="black", outline="black")
        self.myDisc3 = self.canvas.create_oval(270+1, 180+1, 360-1, 270-1, fill="white", outline="white")
        self.myDisc4 = self.canvas.create_oval(180+1, 270+1, 270-1, 360-1, fill="white", outline="white")
        self.discList.append(self.myDisc1)
        self.discList.append(self.myDisc2)
        self.discList.append(self.myDisc3)
        self.discList.append(self.myDisc4)

        for x in range(90, 540, 90):
            self.canvas.create_line(x, 0, x, 540, fill="black")
        for y in range(90, 540, 90):
            self.canvas.create_line(0, y, 540, y, fill="black")

    def chooseColor(self):
        """
        Creates a new window that allows players to choose their disc and grid colors
        by keyboard entry. Takes no inputs besides self and returns nothing, assumes
        that the current game is new when first called. Contains a button that calls
        the updateColor method.
        """
        self.colorWin = tk.Toplevel(self.mainWin)
        self.colorWin["bg"] = "white"
        self.colorWin.title("Choose colors!")
        self.titleLabel = tk.Label(self.colorWin, text="Choose Your Colors!", font="Arial 20 bold",
                                   relief=tk.GROOVE, justify=tk.CENTER, bd=5)
        self.titleLabel.grid(row=0, column=1, padx=10, pady=10)
        self.colorLabel1 = tk.Label(self.colorWin, text="Player 1 chooses a color for discs:", font="Arial 20 bold",
                                    relief=tk.GROOVE, justify=tk.CENTER, bd=5)
        self.colorLabel1.grid(row=1, column=1, padx=10, pady=10)
        self.colorLabel2 = tk.Label(self.colorWin, text="Player 2 chooses a color for discs:", font="Arial 20 bold",
                                    relief=tk.GROOVE, justify=tk.CENTER, bd=5)
        self.colorLabel2.grid(row=3, column=1, padx=10, pady=10)
        self.colorLabel3 = tk.Label(self.colorWin, text="Players choose a color for the grid:", font="Arial 20 bold",
                                    relief=tk.GROOVE, justify=tk.CENTER, bd=5)
        self.colorLabel3.grid(row=5, column=1, padx=10, pady=10)

        self.testEntry1 = tk.Entry(self.colorWin, text="", font="Arial 16", width=10, relief=tk.RAISED, bd=2,
                                   justify=tk.CENTER)
        self.testEntry1.grid(row=2, column=1, padx=10, pady=5)
        self.testEntry2 = tk.Entry(self.colorWin, text="", font="Arial 16", width=10, relief=tk.RAISED, bd=2,
                                   justify=tk.CENTER)
        self.testEntry2.grid(row=4, column=1, padx=10, pady=5)
        self.testEntry3 = tk.Entry(self.colorWin, text="", font="Arial 16", width=10, relief=tk.RAISED, bd=2,
                                   justify=tk.CENTER)
        self.testEntry3.grid(row=6, column=1, padx=10, pady=5)

        self.testButton1 = tk.Button(self.colorWin)
        self.testButton1["text"] = "Start"
        self.testButton1.grid(row=7, column=1, padx=5, pady=5)
        self.testButton1["command"] = self.updateColor

    def updateColor(self):
        """
        Changes the color of the players' discs and grid according to players' inputs
        in the chooseColor method. Updates the list of played discs and the grid values
        to reflect color changes. Closes the color-choosing window.
        Takes no inputs besides self, but assumes that players typed valid entries (strings with no
        typos and color names recognized by Python) in the window created by the
        chooseColor method. In the event that the players did not type anything, it sets
        a variable to False to allow the program to create discs properly during gameplay.
        Makes no calls to other methods, returns to the rest of the program.

        """
        self.chooseColorTrue = True
        if self.testEntry1.get() != "" and self.testEntry2 != "" and self.testEntry3 != "":
            self.canvas["bg"] = self.testEntry3.get()
            self.myDisc1 = self.canvas.create_oval(180 + 1, 180 + 1, 270 - 1, 270 - 1, fill=self.testEntry1.get(),
                                                   outline=self.testEntry1.get())
            self.myDisc2 = self.canvas.create_oval(270 + 1, 270 + 1, 360 - 1, 360 - 1, fill=self.testEntry1.get(),
                                                   outline=self.testEntry1.get())
            self.myDisc3 = self.canvas.create_oval(270 + 1, 180 + 1, 360 - 1, 270 - 1, fill=self.testEntry2.get(),
                                                   outline=self.testEntry2.get())
            self.myDisc4 = self.canvas.create_oval(180 + 1, 270 + 1, 270 - 1, 360 - 1, fill=self.testEntry2.get(),
                                                   outline=self.testEntry2.get())
            self.colorWin.withdraw()
            self.gridValue = [[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, self.testEntry1.get(), self.testEntry2.get(), 0, 0],
                              [0, 0, self.testEntry2.get(), self.testEntry1.get(), 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]]
        elif self.testEntry1.get() == "" and self.testEntry2.get() == "" and self.testEntry3.get() == "":
            self.chooseColorTrue = False
            self.colorWin.withdraw()
        self.discList = []
        self.discList.append(self.myDisc1)
        self.discList.append(self.myDisc2)
        self.discList.append(self.myDisc3)
        self.discList.append(self.myDisc4)
        return

    def whoseTurn(self):
        """
        Uses boolean logic to determine whose turn it is to play. Takes no inputs
        besides self, returns nothing and assumes nothing.
        """
        if self.playerOne == True:
            self.playerOne = False
            self.playerTwo = True
            return
        if self.playerTwo == True:
            self.playerTwo = False
            self.playerOne = True
            return

    def placeDisc(self, event):
        """
        Creates and places discs on playable (empty) squares on the grid, but calls the gameOverSequence
        method to end the game if the entire grid has been filled (refers to the list of played
        discs). When creating each disc, it considers which player is currently making a move
        (whoseTurn method), and whether or not the players have chosen their own colors (chooseColorTrue
        variable and entries from chooseColor method).
        It takes event and self as inputs, and initially assumes that the game is not over.
        Each disc placement makes a call to the mapToGrid method, passing in the coordinates of where
        the disc was placed.
        """
        if len(self.discList) == 36:
            self.gameOverSequence()
        ex = event.x
        ey = event.y
        realex = ex - ex % 90
        realey = ey - ey % 90
        if self.playerOne == True:
            if self.chooseColorTrue == False:
                if [realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1] not in self.coordList:
                    self.newDisc = self.canvas.create_oval(realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1,
                                                           fill="black", outline="black")
                    self.whoseTurn()
                    self.discList.append(self.newDisc)
                    self.coordList.append(self.canvas.coords(self.newDisc))
                    self.gridValue[realey//90][realex//90] = "black"
                    self.mapToGrid(realex, realey)
                    return
            else:
                if [realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1] not in self.coordList:
                    self.newDisc = self.canvas.create_oval(realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1,
                                                           fill=self.testEntry1.get(), outline=self.testEntry1.get())
                    self.whoseTurn()
                    self.discList.append(self.newDisc)
                    self.coordList.append(self.canvas.coords(self.newDisc))
                    self.gridValue[realey // 90][realex // 90] = self.testEntry1.get()
                    self.mapToGrid(realex, realey)
                    return
        else:
            if self.chooseColorTrue == False:
                if [realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1] not in self.coordList:
                    self.newDisc = self.canvas.create_oval(realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1,
                                                           fill="white", outline="white")
                    self.whoseTurn()
                    self.discList.append(self.newDisc)
                    self.coordList.append(self.canvas.coords(self.newDisc))
                    self.gridValue[realey // 90][realex // 90] = "white"
                    self.mapToGrid(realex, realey)
                    return
            else:
                if [realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1] not in self.coordList:
                    self.newDisc = self.canvas.create_oval(realex + 1, realey + 1, realex + 90 - 1, realey + 90 - 1,
                                                           fill=self.testEntry2.get(), outline=self.testEntry2.get())
                    self.whoseTurn()
                    self.discList.append(self.newDisc)
                    self.coordList.append(self.canvas.coords(self.newDisc))
                    self.gridValue[realey // 90][realex // 90] = self.testEntry2.get()
                    self.mapToGrid(realex, realey)
                    return

    def mapToGrid(self, realex, realey):
        """
        Takes as input the coordinates (realex, realey) of the disc which was just placed on
        the grid, and converts them to their corresponding positions in the nested list of grid
        values. Makes a call to the discFlipper function, passing in its 'grid value' position.
        Assumes nothing.
        """
        if (realex, realey) == (0, 0):
            self.discFlipper(0, 0)
        if (realex, realey) == (90, 0):
            self.discFlipper(0, 1)
        if (realex, realey) == (180, 0):
            self.discFlipper(0, 2)
        if (realex, realey) == (270, 0):
            self.discFlipper(0, 3)
        if (realex, realey) == (360, 0):
            self.discFlipper(0, 4)
        if (realex, realey) == (450, 0):
            self.discFlipper(0, 5)
        if (realex, realey) == (0, 90):
            self.discFlipper(1, 0)
        if (realex, realey) == (90, 90):
            self.discFlipper(1, 1)
        if (realex, realey) == (180, 90):
            self.discFlipper(1, 2)
        if (realex, realey) == (270, 90):
            self.discFlipper(1, 3)
        if (realex, realey) == (360, 90):
            self.discFlipper(1, 4)
        if (realex, realey) == (450, 90):
            self.discFlipper(1, 5)
        if (realex, realey) == (0, 180):
            self.discFlipper(2, 0)
        if (realex, realey) == (90, 180):
            self.discFlipper(2, 1)
        if (realex, realey) == (180, 180):
            self.discFlipper(2, 2)
        if (realex, realey) == (270, 180):
            self.discFlipper(2, 3)
        if (realex, realey) == (360, 180):
            self.discFlipper(2, 4)
        if (realex, realey) == (450, 180):
            self.discFlipper(2, 5)
        if (realex, realey) == (0, 270):
            self.discFlipper(3, 0)
        if (realex, realey) == (90, 270):
            self.discFlipper(3, 1)
        if (realex, realey) == (180, 270):
            self.discFlipper(3, 2)
        if (realex, realey) == (270, 270):
            self.discFlipper(3, 3)
        if (realex, realey) == (360, 270):
            self.discFlipper(3, 4)
        if (realex, realey) == (450, 270):
            self.discFlipper(3, 5)
        if (realex, realey) == (0, 360):
            self.discFlipper(4, 0)
        if (realex, realey) == (90, 360):
            self.discFlipper(4, 1)
        if (realex, realey) == (180, 360):
            self.discFlipper(4, 2)
        if (realex, realey) == (270, 360):
            self.discFlipper(4, 3)
        if (realex, realey) == (360, 360):
            self.discFlipper(4, 4)
        if (realex, realey) == (450, 360):
            self.discFlipper(4, 5)
        if (realex, realey) == (0, 450):
            self.discFlipper(5, 0)
        if (realex, realey) == (90, 450):
            self.discFlipper(5, 1)
        if (realex, realey) == (180, 450):
            self.discFlipper(5, 2)
        if (realex, realey) == (270, 450):
            self.discFlipper(5, 3)
        if (realex, realey) == (360, 450):
            self.discFlipper(5, 4)
        if (realex, realey) == (450, 450):
            self.discFlipper(5, 5)

    def discFlipper(self, a, b):
        """
        Beside self, takes as input from the mapToGrid method 'grid value' positions (a, b) of a disc
        that was just played, then checks the (8) squares surrounding the disc, treating
        the disc as the centerpiece. It then changes the disc color when appropriate
        according to the game rules, updating the grid values and creating a new disc
        to reflect that. It also prints "yes!" to hint the player about the validity of their move.
        Returns and assumes nothing.
        """
        # - - - testing calls  - - -
        # if a == 0 and b == 0:
        #     print(self.gridValue[a][b+1], "\n",
        #           self.gridValue[a+1][b], self.gridValue[a+1][b+1])
        # elif a == 5 and b == 0:
        #     print(self.gridValue[a-1][b], self.gridValue[a-1][b+1], "\n",
        #           self.gridValue[a][b+1])
        # elif a == 0 and b == 5:
        #     print(self.gridValue[a][b-1], "\n",
        #           self.gridValue[a+1][b-1], self.gridValue[a+1][b])
        # elif b == 5 and a == 5:
        #     print(self.gridValue[a - 1][b - 1], self.gridValue[a - 1][b], "\n",
        #           self.gridValue[a][b - 1], "", "\n",)
        # elif b == 5 and a != 5 and a != 0:
        #     print(self.gridValue[a - 1][b - 1], self.gridValue[a - 1][b], "\n",
        #           self.gridValue[a][b - 1], "", "\n",
        #           self.gridValue[a + 1][b - 1], self.gridValue[a + 1][b])
        # elif a == 5 and b != 5 and b != 0:
        #     print(self.gridValue[a - 1][b - 1], self.gridValue[a - 1][b], self.gridValue[a - 1][b + 1], "\n",
        #           self.gridValue[a][b - 1], "", self.gridValue[a][b + 1], "\n")
        # elif b == 0 and a != 5 and a != 0:
        #     print(self.gridValue[a-1][b], self.gridValue[a-1][b+1], "\n",
        #           "", self.gridValue[a][b+1], "\n",
        #           self.gridValue[a+1][b], self.gridValue[a+1][b+1])
        # elif a == 0 and b != 5 and b != 0:
        #     print(self.gridValue[a][b-1], "", self.gridValue[a][b+1], "\n",
        #           self.gridValue[a+1][b-1], self.gridValue[a+1][b], self.gridValue[a+1][b+1])
        # else:
        #     print(self.gridValue[a - 1][b - 1], self.gridValue[a - 1][b], self.gridValue[a - 1][b + 1], "\n",
        #           self.gridValue[a][b - 1], "", self.gridValue[a][b + 1], "\n",
        #           self.gridValue[a + 1][b - 1], self.gridValue[a + 1][b], self.gridValue[a + 1][b + 1])
        for a in range(6):
            for b in range(6):
                if a != 0 and a != 5 and b != 0 and b != 5:
                    if self.gridValue[a][b] != 0:
                        if self.gridValue[a - 1][b - 1] == self.gridValue[a + 1][b + 1] and self.gridValue[a - 1][b - 1] != 0:
                            if self.chooseColorTrue == False:
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == "white":
                                        if self.gridValue[a - 1][b - 1] == "black":
                                            self.gridValue[a][b] = "black"
                                            self.newDisc = self.canvas.create_oval(90*b + 1, 90*a + 1, 90*b + 90 - 1, 90*a + 90 - 1,
                                                                                   fill="black", outline="black")
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == "black":
                                        if self.gridValue[a - 1][b - 1] == "white":
                                            self.gridValue[a][b] = "white"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1, 90 * a + 90 - 1,
                                                                                   fill="white", outline="white")
                            else:
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == self.testEntry1.get():
                                        if self.gridValue[a - 1][b - 1] == self.testEntry2.get():
                                            self.gridValue[a][b] = self.testEntry2.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1, 90 * a + 90 - 1,
                                                                                   fill=self.testEntry2.get(), outline=self.testEntry2.get())
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == self.testEntry2.get():
                                        if self.gridValue[a - 1][b - 1] == self.testEntry1.get():
                                            self.gridValue[a][b] = self.testEntry1.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1, 90 * a + 90 - 1,
                                                                                   fill=self.testEntry1.get(), outline=self.testEntry1.get())
                        if self.gridValue[a - 1][b + 1] == self.gridValue[a + 1][b - 1] and self.gridValue[a - 1][b + 1] != 0:
                            if self.chooseColorTrue == False:
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == "white":
                                        if self.gridValue[a - 1][b + 1] == "black":
                                            self.gridValue[a][b] = "black"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="black",
                                                                                   outline="black")
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == "black":
                                        if self.gridValue[a - 1][b + 1] == "white":
                                            self.gridValue[a][b] = "white"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="white",
                                                                                   outline="white")
                            else:
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == self.testEntry1.get():
                                        if self.gridValue[a - 1][b + 1] == self.testEntry2.get():
                                            self.gridValue[a][b] = self.testEntry2.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry2.get(),
                                                                                   outline=self.testEntry2.get())
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == self.testEntry2.get():
                                        if self.gridValue[a - 1][b + 1] == self.testEntry1.get():
                                            self.gridValue[a][b] = self.testEntry1.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry1.get(),
                                                                                   outline=self.testEntry1.get())
                        if self.gridValue[a - 1][b] == self.gridValue[a + 1][b] and self.gridValue[a - 1][b] != 0:
                            if self.chooseColorTrue == False:
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == "white":
                                        if self.gridValue[a - 1][b] and self.gridValue[a + 1][b] == "black":
                                            self.gridValue[a][b] = "black"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="black",
                                                                                   outline="black")
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == "black":
                                        if self.gridValue[a - 1][b] and self.gridValue[a + 1][b] == "white":
                                            self.gridValue[a][b] = "white"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="white",
                                                                                   outline="white")
                            else:
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == self.testEntry1.get():
                                        if self.gridValue[a - 1][b] == self.testEntry2.get():
                                            self.gridValue[a][b] = self.testEntry2.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry2.get(),
                                                                                   outline=self.testEntry2.get())
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == self.testEntry2.get():
                                        if self.gridValue[a - 1][b] == self.testEntry1.get():
                                            self.gridValue[a][b] = self.testEntry1.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry1.get(),
                                                                                   outline=self.testEntry1.get())
                        if self.gridValue[a][b - 1] == self.gridValue[a][b + 1] and self.gridValue[a][b - 1] != 0:
                            if self.chooseColorTrue == False:
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == "white":
                                        if self.gridValue[a][b - 1] == "black":
                                            self.gridValue[a][b] = "black"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="black",
                                                                                   outline="black")
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == "black":
                                        if self.gridValue[a][b - 1] == "white":
                                            self.gridValue[a][b] = "white"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="white",
                                                                                   outline="white")
                            else:
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == self.testEntry1.get():
                                        if self.gridValue[a][b - 1] == self.testEntry2.get():
                                            self.gridValue[a][b] = self.testEntry2.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry2.get(),
                                                                                   outline=self.testEntry2.get())
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == self.testEntry2.get():
                                        if self.gridValue[a][b - 1] == self.testEntry1.get():
                                            self.gridValue[a][b] = self.testEntry1.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry1.get(),
                                                                                   outline=self.testEntry1.get())
                if a == 0 and b != 0 and b != 5 or a == 5 and b != 0 and b != 5:
                    if self.gridValue[a][b] != 0:
                        if self.gridValue[a][b - 1] == self.gridValue[a][b + 1] and self.gridValue[a][b - 1] != 0:
                            if self.chooseColorTrue == False:
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == "white":
                                        if self.gridValue[a][b - 1] == "black":
                                            self.gridValue[a][b] = "black"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="black",
                                                                                   outline="black")
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == "black":
                                        if self.gridValue[a][b - 1] == "white":
                                            self.gridValue[a][b] = "white"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="white",
                                                                                   outline="white")
                            else:
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == self.testEntry1.get():
                                        if self.gridValue[a][b - 1] == self.testEntry2.get():
                                            self.gridValue[a][b] = self.testEntry2.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry2.get(),
                                                                                   outline=self.testEntry2.get())
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == self.testEntry2.get():
                                        if self.gridValue[a][b - 1] == self.testEntry1.get():
                                            self.gridValue[a][b] = self.testEntry1.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry1.get(),
                                                                                   outline=self.testEntry1.get())
                if b == 0 and a != 0 and a != 5 or b == 5 and a != 0 and a != 5:
                    if self.gridValue[a][b] != 0:
                        if self.gridValue[a - 1][b] == self.gridValue[a + 1][b] and self.gridValue[a - 1][b] != 0:
                            if self.chooseColorTrue == False:
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == "white":
                                        if self.gridValue[a - 1][b] == "black":
                                            self.gridValue[a][b] = "black"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="black",
                                                                                   outline="black")
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == "black":
                                        if self.gridValue[a - 1][b] == "white":
                                            self.gridValue[a][b] = "white"
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill="white",
                                                                                   outline="white")
                            else:
                                if self.playerOne == True:
                                    if self.gridValue[a][b] == self.testEntry1.get():
                                        if self.gridValue[a - 1][b] == self.testEntry2.get():
                                            self.gridValue[a][b] = self.testEntry2.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry2.get(),
                                                                                   outline=self.testEntry2.get())
                                if self.playerOne == False:
                                    if self.gridValue[a][b] == self.testEntry2.get():
                                        if self.gridValue[a - 1][b] == self.testEntry1.get():
                                            self.gridValue[a][b] = self.testEntry1.get()
                                            self.newDisc = self.canvas.create_oval(90 * b + 1, 90 * a + 1, 90 * b + 90 - 1,
                                                                                   90 * a + 90 - 1,
                                                                                   fill=self.testEntry1.get(),
                                                                                   outline=self.testEntry1.get())

    def gameOverSequence(self):
        """
        Stops gameplay and creates a new window that shows the players' scores and messages
        stating the outcome of the game (who has won/lost, or a tie), with a replay and quit
        button that make callbacks to the replay and quitCallback methods.
        Takes no inputs besides self and returns and assumes nothing.
        """
        self.mainWin.withdraw()
        self.scoreWin = tk.Toplevel(self.mainWin)
        self.scoreWin["bg"] = "white"
        self.scoreWin.title("Game Over!")
        player1discs = 0
        player2discs = 0
        if self.chooseColorTrue == False:
            for discs in self.gridValue:
                print(discs)
                for disc in range(6):
                    if discs[disc] == "black":
                        player1discs = player1discs + 1
                    if discs[disc] == "white":
                        player2discs = player2discs + 1
        else:
            for discs in self.gridValue:
                print(discs)
                for disc in range(6):
                    if discs[disc] == self.testEntry1.get():
                        player1discs = player1discs + 1
                    if discs[disc] == self.testEntry2.get():
                        player2discs = player2discs + 1
        self.player1Label = tk.Label(self.scoreWin, text="Player 1 Score: ", font="Arial 20 bold",
                                     relief=tk.GROOVE, justify=tk.CENTER, bd=5)
        self.player1Label.grid(row=0, column=1, padx=10, pady=10)
        self.player1score = tk.Label(self.scoreWin, text=player1discs, font="Arial 20 bold", relief=tk.GROOVE,
                                     justify=tk.CENTER, bd=5)
        self.player1score.grid(row=1, column=1, padx=10, pady=10)
        self.player2Label = tk.Label(self.scoreWin, text="Player 2 Score: ", font="Arial 20 bold",
                                     relief=tk.GROOVE, justify=tk.CENTER, bd=5)
        self.player2Label.grid(row=0, column=2, padx=10, pady=10)
        self.player2score = tk.Label(self.scoreWin, text=player2discs, font="Arial 20 bold", relief=tk.GROOVE,
                                     justify=tk.CENTER, bd=5)
        self.player2score.grid(row=1, column=2, padx=10, pady=10)
        self.playAgain = tk.Button(self.scoreWin, text="✧ Replay! ✧", font="Arial 20 bold", relief=tk.GROOVE,
                                   justify=tk.CENTER, bd=5, command=self.replay)
        self.playAgain.grid(row=3, column=1, padx=10, pady=10, columnspan=2)
        self.quitAgain = tk.Button(self.scoreWin, text="# Quit- #", font="Arial 20 bold", relief=tk.GROOVE,
                                   justify=tk.CENTER, bd=5, command=self.quitCallback)
        self.quitAgain.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
        if player1discs > player2discs:
            self.congratsLabel = tk.Label(self.scoreWin, text="Congratulations!", font="Arial 20 bold",
                                          fg="red", relief=tk.GROOVE, justify=tk.CENTER, bd=5)
            self.congratsLabel.grid(row=2, column=1, padx=10, pady=10)
            self.tryAgain1Label = tk.Label(self.scoreWin, text="Oops! Try again!", font="Arial 20 bold",
                                           fg="blue", relief=tk.GROOVE, justify=tk.CENTER, bd=5)
            self.tryAgain1Label.grid(row=2, column=2, padx=10, pady=10)
        if player2discs > player1discs:
            self.congrats2Label = tk.Label(self.scoreWin, text="Congratulations!", font="Arial 20 bold",
                                           fg="Red", relief=tk.GROOVE, justify=tk.CENTER, bd=5)
            self.congrats2Label.grid(row=2, column=2, padx=10, pady=10)
            self.tryAgain2Label = tk.Label(self.scoreWin, text="Oops! Try again!", font="Arial 20 bold",
                                           fg="blue", relief=tk.GROOVE, justify=tk.CENTER, bd=5)
            self.tryAgain2Label.grid(row=2, column=1, padx=10, pady=10)
        if player1discs == player2discs:
            self.tieLabel = tk.Label(self.scoreWin, text="Both of you did well:)", font="Arial 20 bold",
                                     relief=tk.GROOVE, justify=tk.CENTER, bd=5)
            self.tieLabel.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    def replay(self):
        """
        Re-initializes certain lists and variables to reflect a new game state.
        Closes the score window, brings up the main window with the grid and calls the
        resetGameCallback method to complete the rest of the game-reset process.
        """
        self.gameOver = False
        self.playerOne = True
        self.discList = []
        self.coordList = [[180 + 1, 180 + 1, 270 - 1, 270 - 1], [270 + 1, 270 + 1, 360 - 1, 360 - 1],
                          [270 + 1, 180 + 1, 360 - 1, 270 - 1], [180 + 1, 270 + 1, 270 - 1, 360 - 1]]
        self.gridValue = [[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, "black", "white", 0, 0],
                          [0, 0, "white", "black", 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]]
        self.scoreWin.withdraw()
        self.mainWin.deiconify()
        self.resetGameCallback()

    def resetGameCallback(self):
        """Resets the game to play again. Takes no inputs besides self and returns and assumes
        nothing, but prints a message to players to inform them of the reset."""
        print("--✧ new game! ✧--")
        self.gameOver = False
        self.playerOne = True
        self.canvas.delete("all")
        if self.chooseColorTrue == False:
            self.myDisc1 = self.canvas.create_oval(180 + 1, 180 + 1, 270 - 1, 270 - 1, fill="black", outline="black")
            self.myDisc2 = self.canvas.create_oval(270 + 1, 270 + 1, 360 - 1, 360 - 1, fill="black", outline="black")
            self.myDisc3 = self.canvas.create_oval(270 + 1, 180 + 1, 360 - 1, 270 - 1, fill="white", outline="white")
            self.myDisc4 = self.canvas.create_oval(180 + 1, 270 + 1, 270 - 1, 360 - 1, fill="white", outline="white")
        else:
            self.myDisc1 = self.canvas.create_oval(180+1, 180+1, 270-1, 270-1, fill=self.testEntry1.get(),
                                                   outline=self.testEntry1.get())
            self.myDisc2 = self.canvas.create_oval(270+1, 270+1, 360-1, 360-1, fill=self.testEntry1.get(),
                                                   outline=self.testEntry1.get())
            self.myDisc3 = self.canvas.create_oval(270+1, 180+1, 360-1, 270-1, fill=self.testEntry2.get(),
                                                   outline=self.testEntry2.get())
            self.myDisc4 = self.canvas.create_oval(180+1, 270+1, 270-1, 360-1, fill=self.testEntry2.get(),
                                                   outline=self.testEntry2.get())
        for x in range(90, 540, 90):
            self.canvas.create_line(x, 0, x, 540, fill="black")
        for y in range(90, 540, 90):
            self.canvas.create_line(0, y, 540, y, fill="black")
        self.discList = []
        self.discList.append(self.myDisc1)
        self.discList.append(self.myDisc2)
        self.discList.append(self.myDisc3)
        self.discList.append(self.myDisc4)
        self.coordList = [[180 + 1, 180 + 1, 270 - 1, 270 - 1], [270 + 1, 270 + 1, 360 - 1, 360 - 1],
                          [270 + 1, 180 + 1, 360 - 1, 270 - 1], [180 + 1, 270 + 1, 270 - 1, 360 - 1]]
        if self.chooseColorTrue == False:
            self.gridValue = [[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, "black", "white", 0, 0],
                              [0, 0, "white", "black", 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]]
        else:
            self.gridValue = [[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, self.testEntry1.get(), self.testEntry2.get(), 0, 0],
                              [0, 0, self.testEntry2.get(), self.testEntry1.get(), 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]]

    def instructionsCallback(self):
        """
        Creates a window that shows instructions for using our program and playing the game.
        Takes no inputs besides self and returns and assumes nothing.
        """
        self.otherWin = tk.Toplevel(self.mainWin)
        self.otherWin["bg"] = "white"
        self.otherWin.title("Instructions")
        self.otherLabel = tk.Label(self.otherWin, text="1. Click the 'Choose Colors' button to choose your disc colors and"
                                                       " the color of the board! The default colors are black (player 1) and "
                                                       "white (player 2) - but do not switch your colors in-game!\n"
                                                       "2. Click on the grid squares to place your discs and start the game!\n"
                                                       "3. Click on the 'Reset Game' button to start a new game.\n"
                                                       "4. Click on the 'Quit' button to close the window and end the game.\n"
                                                       "5. You may click on this 'Instructions' button to re-read this at any time!\n\n"
                                                       "✧･ﾟ: *✧･ﾟ:*  RULES  *:･ﾟ✧*:･ﾟ✧\n"
                                                       "Player 1 goes first. Players take turns placing their"
                                                       " disc on an empty square on the grid. If a player places their discs such that"
                                                       " they trap one of the opponent's discs between their own discs, then the"
                                                       " opponent's discs will change color. Be careful, though! You may accidentally trap"
                                                       " your own disc while trying to flip your opponent's! The game ends when the grid is filled."
                                                       "The player with the most discs (of their own color) wins. Click on the grid again "
                                                       "to see the scores. After seeing the score, you can click on the 'Replay' button to "
                                                       "play again or click on the 'Quit' button to end and leave.", font="Arial 14",
                                                       wraplength=600, relief=tk.GROOVE, justify=tk.LEFT, bd=5, padx=10, pady=10)
        self.otherLabel.grid(row=0, column=0, padx=10, pady=10)

    def quitCallback(self):
        """Destroys the entire game window/quits game. Takes no inputs besides
        self, returns and assumes nothing, but prints a final message to the players."""
        print("--✧ thank you for playing! ✧--")
        print("julia zhong, jacqueline ong | 2018")
        # - - testing calls - -
        # print(self.discList)
        # print(len(self.discList))
        # print("", self.gridValue[0], "\n", self.gridValue[1], "\n", self.gridValue[2], "\n", self.gridValue[3], "\n",
        #       self.gridValue[4], "\n", self.gridValue[5])
        self.mainWin.destroy()

    def run(self):
        """
        Runs the GUI, takes no inputs besides self and returns nothing.
        """
        self.mainWin.mainloop()

# - - - third section | main program - - -
myReversi = Reversi()
myReversi.run()
