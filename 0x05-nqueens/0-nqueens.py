#!/usr/bin/python3
"""
N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP)
"""
import sys


class NQueen:
    """Class for solving N Queen Problem"""

    def __init__(self, n):
        """Initialize global variables"""
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """Check if the k-th queen can be placed in the i-th column
        or if there are attacking queens in the same row or diagonal"""
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def nQueen(self, k):
        """i
        Try to place every queen on the board
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = [
                            [row - 1, self.x[row] - 1]
                            for row in range(1, self.n + 1)
                            ]
                    self.res.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.res


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = NQueen(N)
    solutions = queen.nQueen(1)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
