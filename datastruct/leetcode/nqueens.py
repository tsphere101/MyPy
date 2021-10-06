import pandas as pd
import numpy as np
N = 8

def isSafe(board, row, col):
     
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        print("i and j is : ",i,j)
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True


board = [[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]

row = 3
col = 3
for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
    print("i and j is : ",i,j)
    board[i][j] = 1
for i,j in zip(range(row,N,1),range(col,-1,-1)):
    board[i][j] = 2
board[row][col] = 5

x = pd.DataFrame(board)
print(x)
for i in range(5,8,1):
    print(i)