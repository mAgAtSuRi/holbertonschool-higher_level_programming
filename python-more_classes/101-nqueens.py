#!/usr/bin/python3
import sys


class Nqueens():

	def __init__(self, size):
		self.size = size
		self.solutions = set()
		self.run()

	def create_board(self):
		board = []
		for i in range(self.size):
			for j in range(self.size):
				board.append([i, j])
		return board

	def remove_attacked_square(self, board, queen_position):
		new_pos = [pos for pos in board]

		for k in range(self.size):
			# top right diagonal
			tr_new_x = queen_position[0] + k
			tr_new_y = queen_position[1] + k
			if [tr_new_x, tr_new_y] in new_pos:
				new_pos.remove([tr_new_x, tr_new_y])
			# top left diagonal
			tl_new_x = queen_position[0] - k
			tl_new_y = queen_position[1] + k
			if [tl_new_x, tl_new_y] in new_pos:
				new_pos.remove([tl_new_x, tl_new_y])
			# bottom right diagonal
			br_new_x = queen_position[0] + k
			br_new_y = queen_position[1] - k
			if [br_new_x, br_new_y] in new_pos:
				new_pos.remove([br_new_x, br_new_y])
			# bottom left diagonal
			bl_new_x = queen_position[0] - k
			bl_new_y = queen_position[1] - k
			if [bl_new_x, bl_new_y] in new_pos:
				new_pos.remove([bl_new_x, bl_new_y])

		for i in range(self.size):
			for j in range(self.size):
				# same row or column
				if i == queen_position[0] or j == queen_position[1]:
					if [i, j] in new_pos:
						new_pos.remove([i, j])

		return new_pos

	def solve(self, board, queen_list=[]):
		if len(queen_list) == self.size:
			set_solutions = tuple(sorted(tuple(q) for q in queen_list))
			self.solutions.add(set_solutions)
			return self.solutions
	
		for queen_pos in board:
			new_board = self.remove_attacked_square(board, queen_pos)
			self.solve(new_board, queen_list + [queen_pos])

	def run(self):
		self.solve(self.create_board())
		return self.solutions

	def __str__(self):
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