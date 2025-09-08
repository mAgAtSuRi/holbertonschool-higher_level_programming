#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for num in matrix[i]:
            if num == matrix[i][len(matrix[i]) - 1]:
                print("{}".format(num))
            else:
                print("{} ".format(num), end="")
