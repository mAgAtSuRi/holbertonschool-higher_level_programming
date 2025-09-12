#!/usr/bin/python3
"""
divides a matrix by a number
@matrix: matrix to divide
@div: the division number
"""
def matrix_divided(matrix, div):
	"""
	divides a matrix by a number (float or int)
	"""
	if type(div) not in (float, int):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")
	new_matrix = []
	row_size = len(matrix[0])
	for row in matrix:
		if len(row) != row_size:
			raise TypeError("Each row of the matrix must have the same size")
		new_matrix.append(row)
	for num in new_matrixrow:
		if type(num) not in (int, float):
			raise TypeError("matrix must be a matrix (lists of lists) of integers/floats")
		matrix[row][num] = matrix[row][num] / div
	return matrix
