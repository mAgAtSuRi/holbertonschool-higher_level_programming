#!/usr/bin/python3
"""
Module Nqueens
Solve the N-Queens problem and print all unique solutions for a given board size.

Usage:
    ./101-nqueens.py N

Arguments:
    N (int): Size of the board (must be >= 4)

Description:
    This module defines the Nqueens class that generates all possible solutions
    for the N-Queens problem using a backtracking approach. The board is represented
    as a list of positions, and solutions are stored in a set to avoid duplicates.

Classes:
    Nqueens

Exceptions:
    Exits with error messages if:
        - No or invalid command-line argument is provided
        - N is not an integer
        - N < 4
"""

import sys

class Nqueens():
    """
    Class to solve the N-Queens problem.

    Attributes:
        size (int): Size of the board (N x N)
        solutions (set): Set of all unique solutions, where each solution is
                         represented as a tuple of queen positions [(row, col), ...].

    Methods:
        create_board():
            Creates a list of all possible board positions [[row, col], ...].
        remove_attacked_square(board, queen_position):
            Returns a new board list excluding positions attacked by the given queen.
        solve(board, queen_list=[]):
            Recursively finds all valid solutions using backtracking.
        run():
            Calls the solve() method and returns the set of solutions.
        __str__():
            Returns a string representation of all solutions as lists of positions.
    """

    def __init__(self, size):
        """
        Initialize the Nqueens instance with board size and solve the problem.

        Args:
            size (int): Board size (N)
        """
        self.size = size
        self.solutions = set()
        self.run()

    def create_board(self):
        """
        Generate a list of all positions on the board.

        Returns:
            list: List of positions [[row, col], ...]
        """
        board = []
        for i in range(self.size):
            for j in range(self.size):
                board.append([i, j])
        return board

    def remove_attacked_square(self, board, queen_position):
        """
        Remove all positions from the board that are attacked by a given queen.

        Args:
            board (list): Current board positions [[row, col], ...]
            queen_position (list): Position of the queen [row, col]

        Returns:
            list: New list of positions not attacked by the queen
        """
        new_pos = [pos for pos in board]

        for k in range(self.size):
            tr_new_x, tr_new_y = queen_position[0] + k, queen_position[1] + k
            if [tr_new_x, tr_new_y] in new_pos:
                new_pos.remove([tr_new_x, tr_new_y])

            tl_new_x, tl_new_y = queen_position[0] - k, queen_position[1] + k
            if [tl_new_x, tl_new_y] in new_pos:
                new_pos.remove([tl_new_x, tl_new_y])

            br_new_x, br_new_y = queen_position[0] + k, queen_position[1] - k
            if [br_new_x, br_new_y] in new_pos:
                new_pos.remove([br_new_x, br_new_y])

            bl_new_x, bl_new_y = queen_position[0] - k, queen_position[1] - k
            if [bl_new_x, bl_new_y] in new_pos:
                new_pos.remove([bl_new_x, bl_new_y])

        for i in range(self.size):
            for j in range(self.size):
                if i == queen_position[0] or j == queen_position[1]:
                    if [i, j] in new_pos:
                        new_pos.remove([i, j])

        return new_pos

    def solve(self, board, queen_list=[]):
        """
        Recursively solve the N-Queens problem using backtracking.

        Args:
            board (list): Current available board positions
            queen_list (list): List of already placed queen positions

        Returns:
            None: Solutions are stored in self.solutions
        """
        if len(queen_list) == self.size:
            # Convert solution to tuple of tuples for set storage (to avoid duplicates)
            set_solutions = tuple(sorted(tuple(q) for q in queen_list))
            self.solutions.add(set_solutions)
            return self.solutions

        for queen_pos in board:
            new_board = self.remove_attacked_square(board, queen_pos)
            self.solve(new_board, queen_list + [queen_pos])

    def run(self):
        """
        Start solving the N-Queens problem.

        Returns:
            set: Set of all unique solutions
        """
        self.solve(self.create_board())
        return self.solutions

    def __str__(self):
        """
        Return a string representation of all solutions.

        Returns:
            str: Each solution represented as a list of queen positions
        """
        return '\n'.join(str(list(map(list, sol))) for sol in self.solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    nqueen = Nqueens(n)
    print(nqueen)
