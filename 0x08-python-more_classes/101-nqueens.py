#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True

def solve_nqueens(board, row):
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1

def nqueens(N):

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    solve_nqueens(board, 0)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
nqueens(sys.argv[1])
