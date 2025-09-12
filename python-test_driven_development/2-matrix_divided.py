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

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(row)):
            if type(row[i]) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    new_matrix = [[round(row[i] / div, 2) for i in range(len(row))] for row in matrix]
    return new_matrix
