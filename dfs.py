
# DFS
def printBoard(board): 
    print('Result:')
    for i in board: 
        print(i)

# check queen has safety when set queen at (x,y)
def check(row, col , board ,n): 
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

    
def chess(col,n,board): 
    if col>=n: 
        printBoard(board)
        exit()
    for i in range(n):  # set queen from row 0 --> n-1
        if (check(i,col,board,n)):
            board[i][col]=1 # danh dau (i,col) da dat quan hau
            if (chess(col+1,n,board)): return True
            board[i][col]=0
    return False

def main():
    n = input("Enter n : ")     
    print('-------------------------------------')           
    n = int(n) # number queens ****  input  ****
    board = [[0 for i in range(n)] for j in range(n)] 
    chess(0,n,board)
    print('No solution')
        
main()

                