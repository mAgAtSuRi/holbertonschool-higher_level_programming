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
