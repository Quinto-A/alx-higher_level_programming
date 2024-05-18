#!/usr/bin/python3
"""defines a module that solves the N queens problem"""


def print_usage():
    print("Usage: nqueens N")

def print_number_error():
    print("N must be a number")

def print_size_error():
    print("N must be atleast 4")

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col +row:
                return False
    return True

def solve_nqueens(N):
    def backtrack(row, solution):
        if row == N:
            solution.append(solution[:])
        else:
            for col in range(N):
                if is_valid(solution, row, col):
                    solution[row] = col
                    backtrack(row +1, solution)
                    solution[row] = -1

    solutions = []
    solution = [-1] * N
    backtrack(0, solution)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error()
        sys.exit(1)

    if N < 4:
        print_size_error()
        sys.exit(1)

    solutions = solve_nqueens(N)
    for sol in solutions:
        print([i, sol[i]] for i in range(N))

    if __name__ == "__main__":
        main()
