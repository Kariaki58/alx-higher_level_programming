#!/usr/bin/python3
"""import modules"""
import sys


def print_solution(solution):
    """Prints the chessboard representation of a solution."""
    print([[i, j] for i, j in enumerate(solution)])


def check_board(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solution(board, row, n):
    """Recursively solve N-Queens problem using backtracking."""
    if row == n:
        print_solution(board)
    else:
        for col in range(n):
            if check_board(board, row, col, n):
                board[row] = col
                solution(board, row + 1, n)


def nqueens(n):
    """Main function to solve N-Queens problem."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solution(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
