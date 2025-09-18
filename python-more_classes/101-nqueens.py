#!/usr/bin/python3
import sys


class Nqueens():
	queen_list = []

	def __init__(self, size):
		self.size = int(size)
		self.board = self.create_board()
		self.new_pos = []

	def create_board(self):
		board = []
		for i in range(self.size):
			for j in range(self.size):
				board.append([i, j])
		return board

	def remove_attacked_square(self):
		queen_position = self.board[0]
		self.queen_list.append(queen_position)

		self.new_pos = [pos for pos in self.board]
		for k in range(self.size):
			# top right diagonal
			tr_new_x = queen_position[0] + k
			tr_new_y = queen_position[1] + k
			if tr_new_x < self.size and tr_new_y < self.size:
				self.new_pos.remove([tr_new_x, tr_new_y])
			# top left diagonal
			tl_new_x = queen_position[0] - k
			tl_new_y = queen_position[1] + k
			if [tl_new_x, tl_new_y] in self.new_pos:
				self.new_pos.remove([tl_new_x, tl_new_y])
			# bottom right diagonal
			br_new_x = queen_position[0] + k
			br_new_y = queen_position[1] - k
			if [br_new_x, br_new_y] in self.new_pos:
				self.new_pos.remove([br_new_x, br_new_y])
			# bottom left diagonal
			bl_new_x = queen_position[0] - k
			bl_new_y = queen_position[1] - k
			if [bl_new_x, bl_new_y] in self.new_pos:
				self.new_pos.remove([bl_new_x, bl_new_y])

		for i in range(self.size):
			for j in range(self.size):
				# same row or column
				if i == queen_position[0] or j == queen_position[1]:
					if [i, j] in self.new_pos:
						self.new_pos.remove([i, j])
		self.board = self.new_pos
		return self.board

	def __str__(self):
		return str(self.remove_attacked_square())


if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("Usage: nqueens N,")
		exit(1)
	try:
		nqueen = Nqueens(int(sys.argv[1]))
	
	except TypeError:
		print("N must be an integer")
		exit(1)
	if int(sys.argv[1]) < 4:
		print("N must be at least 4")
		exit(1)	
	
	print(nqueen)