#!/usr/bin/python3
import sys

class Nqueens:
    def __init__(self, size):
        self.size = size
        self.solutions = []
        self.solve(0, [], set(), set(), set())

    def solve(self, row, queens, cols, diag1, diag2):
        """
        row: ligne actuelle
        queens: liste des positions des reines déjà placées
        cols: colonnes occupées
        diag1: diagonales \ occupées (r - c)
        diag2: diagonales / occupées (r + c)
        """
        if row == self.size:
            self.solutions.append(list(queens))
            return

        for col in range(self.size):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # placer la reine
            queens.append([row, col])
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # backtrack
            self.solve(row + 1, queens, cols, diag1, diag2)

            # retirer la reine pour essayer une autre position
            queens.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    def __str__(self):
        return '\n'.join(str(sol) for sol in self.solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be an integer")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    nqueen = Nqueens(n)
    print(nqueen)
