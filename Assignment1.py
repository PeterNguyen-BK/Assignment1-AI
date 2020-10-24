from random import randint
import numpy
import copy

class DFS:
    # DFS
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    def printBoard(self, board, n): 
        print("")
        print("Done! Total of", n, "Queens placed!")
        print("")
        print("Solution:")
        mnl = len(str(len(board)))
        print("")
        print(" "*mnl, "  ", end =" ")
        for x in range(n):
            print(self.alphabet[x], end=" ")
        print("")
        print(" " * mnl, " *", end=" ")
        for x in range(n):
            print("-", end=" ")
        print("*")

        for row in range(n):
            print("", row+1, end=" ")
            print("|", end=" ")
            for col in range(n):
                print(board[row][col], end=" ")
            print("|", end=" ")
            print("")
        
        print(" " * mnl, " *",end=" ")
        for x in range(n):
            print("-",end=" ")
        print("*")

    # check queen has safety when set queen at (x,y)
    def check(self, row, col , board ,n): 
        # check same left col
        for i in range(col): 
            if board[row][i] == 1: return False
        # check cheo tren trai
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):  # range(start,stop,step)   ,  zip() link: https://www.w3schools.com/python/ref_func_zip.asp
            if board[i][j] == 1: return False
        # check cheo duoi trai
        for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
            if board[i][j] == 1: return False
  
        return True

    
    def chess(self, col,n,board): 
        if col>=n: 
            self.printBoard(board, n)
            exit()
        for i in range(n):  # set queen from row 0 --> n-1
            if (self.check(i,col,board,n)):
                board[i][col]=1 # danh dau (i,col) da dat quan hau
                if (self.chess(col+1,n,board)): return True
                board[i][col]=0
        return False

class BrFS:
    tableSize = 0

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    #The queue of possible moves 
    queue = []

    #Whether or not the solver can be ran
    canRun = False

    def setup(self, queenNumber):
        #Set the number of queens/table size
        self.tableSize = queenNumber

        #Check if can run
        self.canRun = True

        #Show error
        if queenNumber < 4:
            print("ERROR: A solution is not available for this few number of queens")
            self.canRun = False

    #Create an empty table
    def blankTable(self):
        table = []
        for row in range(self.tableSize):
            new = []
            for col in range(self.tableSize):
                new.append(0);
            table.append(new)
        return table

    #Place a queen in a table
    def placeQueen(self, table, row, col):
        #Copy the table, as python is annoying and will change both
        t2 = copy.deepcopy(table)
        t2[row][col] = 1
        return t2

    def loopBoard(self):
        col = 1
        #Loop while the queue isn't empty
        while len(self.queue):
            #Create a new empty queue
            queue2 = []
            #Loop the queue
            for s in self.queue:
                #Get which moves are available
                availableMoves = self.getPositions(s, col)
                #If we are placing the last queen, and there are solutions available, finish
                if col == self.tableSize -1 and len(availableMoves):
                    #Clear queue
                    self.queue = []
                    #Get the solution
                    s = availableMoves[0]
                    break
                #Add the possible moves to the new queue
                if len(availableMoves):
                    queue2 += availableMoves
            #Replace queue
            self.queue = queue2
            #Increase Queen/col counter
            col += 1
        self.finish(s, col)

    #Get an array of moves that are available
    def getPositions(self, table, col):        
        row = 0
        possiblePositions = []

        #Loop all rows on the board
        while row < self.tableSize:
            #If we can place in this space
            if self.canPlace(table, row, col):
                #Add the table with the newly added queen to the list of possible moves
                possiblePositions.append(self.placeQueen(table, row, col))
            row += 1
        return possiblePositions

    #Check if can place a queen in a position
    def canPlace(self, table, row, col):
        # Check left/right
        x = 0
        #Loop across the table
        while x < self.tableSize:
            if table[x][col]:
                return False
            x += 1

        #Check up/down
        y = 0
        #Loop down the table
        while y < self.tableSize:
            if table[row][y]:
                return False
            y += 1

        #Check up right 
        x = row + 1
        y = col + 1
        #Loop up/right 
        while x < self.tableSize and y < self.tableSize:
            if table[x][y]:
                return False            
            x += 1
            y += 1
        #Check down left 
        x = row - 1
        y = col - 1
        #Loop down/left through the table
        while x >= 0 and y >= 0:
            if table[x][y]:
                return False
            x -= 1
            y -= 1

        #Check up left
        x = row - 1
        y = col + 1
        #Loop up left through the table
        while x >= 0 and y < self.tableSize:
            if table[x][y]:
                return False
            x -= 1
            y += 1
        #Check down right 
        x = row + 1
        y = col - 1
        #Loop down right through the table
        while x < self.tableSize and y >= 0:
            if table[x][y]:
                return False
            x += 1
            y -= 1

        return True

    #Output a table to a user, looking all pretty
    def display(self, table):
        #Max Number Length
        mnl = len(str(len(table)))

        #New Line
        print("")

        #Top of the table, E.g "     A B C D"
        print(" "*mnl, "  ", end =" ")
        for x in range(self.tableSize):
            print(self.alphabet[x], end=" ")
        #New Line
        print("")
        #Row spacer, E.g "   * - - - - *
        print(" " * mnl, " *", end=" ")
        for x in range(self.tableSize):
            print("-", end=" ")
        print("*")

        #Row Counter
        #Print the actual table, with the Queens as 1's, empty space as 0
        #Also prefixed by the row number, E.g " 3 | 0 1 0 0 |
        x = 1
        for row in table:
            #If numbers are shorter than the largest number, give them extra spaces so the rows still line up
            extraPadding = mnl - len(str(x))
            #Show the number prefix, spaces, and | symbol, E.g " 6  | "
            print("", x, " "*int(extraPadding) + "|", end=" ")
            #Show the value of the cell (1 or 0)
            for col in row:
                print(col,end=" ")
            #End of the row
            print("|")
            #Next Row
            x += 1
        #Show the same row spacer as at the top of the table, E.g "   * - - - - *
        print(" " * mnl, " *",end=" ")
        for x in range(self.tableSize):
            print("-",end=" ")
        print("*")

    def finish(self, table, col):
        if col == self.tableSize:
            print("Total of", self.tableSize, "Queens placed!")
            print("")
            print("Solution:")
            self.display(table)
        else:
            print("")
            print("ERROR: Could not place all queens for some unknown reason =[")

    def run(self):
        if not self.canRun:
            print("ERROR: Can not run")
        else:
            print("Working...")
            print("")
            self.queue = self.getPositions(self.blankTable(), 0)
            self.loopBoard()





class HillClimbing:
    #Size of board
    boardSize = 0

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    #Initial size of board
    def __init__(self, size):
        if size < 4: 
            print("ERROR: A solution is not available for this few number of queens")
            exit()
        self.boardSize = size

    #Initial 2D Array
    def initialArray2D(self):
        n = []
        for row in range(self.boardSize):
            new = []
            for col in range(self.boardSize):
                new.append(0);
            n.append(new)
        return n

    #Create starting state 
    def randomLocation(self, state, board):
        for i in range(self.boardSize):
            state[i] = randint(0,self.boardSize-1)
            board[state[i]][i] = 1

    #Print board to console
    def printBoard(self, board):
        print("Solution:")
        mnl = len(str(len(board)))
        print("")
        print(" "*mnl, "  ", end =" ")
        for x in range(self.boardSize):
            print(self.alphabet[x], end=" ")
        print("")
        print(" " * mnl, " *", end=" ")
        for x in range(self.boardSize):
            print("-", end=" ")
        print("*")

        for row in range(self.boardSize):
            print("", row+1, end=" ")
            print("|", end=" ")
            for col in range(self.boardSize):
                print(board[row][col], end=" ")
            print("|", end=" ")
            print("")
        
        print(" " * mnl, " *",end=" ")
        for x in range(self.boardSize):
            print("-",end=" ")
        print("*")

    #Compare 2 states
    def compareStates(self, state1, state2):
        for i in range(self.boardSize):
            if state1[i] != state2[i] :
                return False
        return True

    #Fill in board with value input
    def fill(self, board, value):
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                board[row][col] = value

    #Check queen face another queen
    def checkObject(self, board, state):
        attacking = 0
        for i in range(self.boardSize):
            #Check to the left of same row
            row = state[i]
            col = i - 1
            while (col>=0) and (board[row][col]!=1):
                col = col - 1
            
            if (col>=0) and (board[row][col]==1):
                attacking = attacking + 1

            #Check to the right of same row
            row = state[i]
            col = i + 1
            while (col<self.boardSize) and (board[row][col]!=1):
                col = col + 1

            if (col<self.boardSize) and (board[row][col]==1):
                attacking = attacking + 1
            
            #Check left up
            row = state[i] - 1
            col = i - 1
            while (col>=0) and (row>=0) and (board[row][col]!=1):
                col = col - 1
                row = row - 1

            if (col>=0) and (row>=0) and (board[row][col]==1):
                attacking = attacking + 1

            #Check right down
            row = state[i] + 1
            col = i + 1
            while (col<self.boardSize) and (row<self.boardSize) and (board[row][col]!=1):
                col = col + 1
                row = row + 1

            if (col<self.boardSize) and (row<self.boardSize) and (board[row][col]==1):
                attacking = attacking + 1

            #Check left down
            row = state[i] + 1
            col = i - 1
            while (col>=0) and (row<self.boardSize) and (board[row][col]!=1):
                col = col - 1
                row = row + 1

            if (col>=0) and (row<self.boardSize) and (board[row][col]==1):
                attacking = attacking + 1

            #Check right up
            row = state[i] - 1
            col = i + 1
            while (col<self.boardSize) and (row>=0) and (board[row][col]!=1):
                col = col + 1
                row = row - 1

            if (col<self.boardSize) and (row>=0) and (board[row][col]==1):
                attacking = attacking + 1

        return int(attacking/2)

    #Generate board with specifically
    def generateBoard(self, board, state):
        self.fill(board,0)
        for i in range(self.boardSize):
            board[state[i]][i] = 1
    
    #Copy state2 to state1
    def copyState(self, state1, state2):
        for i in range(self.boardSize):
            state1[i] = state2[i]
    
    #Get board with another queen place
    def getNeighbour(self, board, state):
        #Optimal state and board
        opState = [None]*self.boardSize
        opBoard = self.initialArray2D()
        
        self.copyState(opState, state)
        self.generateBoard(opBoard, opState)

        #Optimal objective
        opObjective = self.checkObject(opBoard, opState)

        #Initialize the temporary board and state
        NeighbourBoard = self.initialArray2D()
        NeighbourState = [None]*self.boardSize
        self.copyState(NeighbourState, state)
        self.generateBoard(NeighbourBoard, NeighbourState)

        #Loop through all posible neighbour of the board 
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if j != state[i]:
                    NeighbourState[i] = j
                    NeighbourBoard[NeighbourState[i]][i] = 1
                    NeighbourBoard[state[i]][i] = 0

                    temp = self.checkObject(NeighbourBoard, NeighbourState)

                    if temp <= opObjective:
                        opObjective = temp
                        self.copyState(opState, NeighbourState)
                        self.generateBoard(opBoard, opState)

                    NeighbourBoard[NeighbourState[i]][i] = 0
                    NeighbourState[i] = state[i]
                    NeighbourBoard[state[i]][i] = 1
            
        self.copyState(state, opState)
        self.fill(board, 0)
        self.generateBoard(board, state)

    def hillClimbing(self, board, state):
        #Initialize neighbour board and state with current board and state
        neighbourBoard = self.initialArray2D()
        neighbourState = [None]*self.boardSize
        self.copyState(neighbourState, state)
        self.generateBoard(neighbourBoard, neighbourState)

        while True:
            #Copy neighbourState to current state
            self.copyState(state, neighbourState)
            self.generateBoard(board, state)

            #Get optimal neighbour
            self.getNeighbour(neighbourBoard, neighbourState)

            #If neighbour and current are the same then there is no optimal and print board to console
            if self.compareStates(state, neighbourState):
                print("")
                print("Done! Total of", self.boardSize, "Queens placed!")
                print("")
                self.printBoard(board)
                break
            #If neighbour and current are the same but the object alse is the same then we meet local optimization
            #so we have to jump to another random neighbour to escape
            elif self.checkObject(board,state) == self.checkObject(neighbourBoard, neighbourState):
                neighbourState[randint(0,self.boardSize-1)] = randint(0, self.boardSize-1)
                self.generateBoard(neighbourBoard, neighbourState)

def ask():
    while True:
        print("")
        print("How many Queens would you like use?  [8]")
        input1 = input()
        #Check if the input given is an integer
        if input1.isdigit():
            return int(input1)
        #If no input is given, use the standard 8
        elif input1 == "":
            return 8;
        print("ERROR: Invalid Input")

def askAlgorithm():
    while True:
        print("")
        print("1. DFS")
        print("2. BrFS")
        print("3.Hill Climbing")
        print("Choose algorithm(1,2,3): ")
        input2 = input()
        #Check if the input given is an integer
        if (input2.isdigit()) and (int(input2) in range(1,4)):
            return int(input2)
        #If no input is given, use the standard 8
        elif input2 == "":
            return 1;
        print("ERROR: Invalid Input")
        
def run():
    algorithm = askAlgorithm()
    if algorithm == 1:
        size = ask()
        qs = DFS()
        board = [[0 for i in range(size)] for j in range(size)] 
        print("")
        print("Working...")
        qs.chess(0,size,board)
        print('No solution')
    elif algorithm == 2:
        qs = BrFS()
        #While ask hasn't given a valid input
        while(not qs.canRun):
            qs.setup(ask())
        print("")
        qs.run()
    else:
        size = ask()
        state = [0]*size
        board = []
        for row in range(size):
            new = []
            for col in range(size):
                new.append(0);
            board.append(new)

        qs = HillClimbing(size)
        qs.randomLocation(state, board)
        print("")
        print("Working...")
        qs.hillClimbing(board, state)


if __name__ == "__main__":
    run()

            
            



