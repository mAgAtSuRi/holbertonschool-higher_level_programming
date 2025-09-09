#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = [row[:] for row in matrix]
    for row in square_matrix:
        for i in range(len(row)):
            row[i] = row[i] ** 2
    return square_matrix
# with comprehension:
# return [[element ** 2 for element in row] for row in matrix]
