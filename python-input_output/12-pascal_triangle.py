#!/usr/bin/python3

"""Module with one function to create a Pascal triangle"""


def pascal_triangle(n):
    """Function creating a Pascal triangle of size n"""
    if n <= 0:
        return []

    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    triangle_list = [[1], [1, 1]]
    for i in range(2, n):
        new_row = [1]
        for j in range(1, i):
            new_row.append(triangle_list[i - 1][j - 1] +
                           triangle_list[i - 1][j])
        new_row.append(1)
        triangle_list.append(new_row)

    return triangle_list
