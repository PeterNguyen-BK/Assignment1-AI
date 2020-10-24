import sys
import copy
from os import system

class QueenSolver:
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
            #Update status
            print(col, "Queens Placed")
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

        #Print the actual table
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
            print("")
            print("Total of", self.tableSize, "Queens placed!")
            print("Solution:")
            self.display(table)
        else:
            print("")
            print("ERROR: Could not place all queens for some unknown reason =[")

    def run(self):
        if not self.canRun:
            print("ERROR: Can not run")
        else:
            print("")
            print("Working...")
            print("")
            self.queue = self.getPositions(self.blankTable(), 0)
            self.loopBoard()

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

#Run the program
def run():
    qs = QueenSolver()
    #While ask hasn't given a valid input
    while(not qs.canRun):
        qs.setup(ask())
    print("")
    qs.run()



if __name__ == "__main__":
    run()