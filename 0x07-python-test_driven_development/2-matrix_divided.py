#!/usr/bin/python3

""" A function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix of integers
        by another operand

    Parameters:
        matrix: list of list of integers or floats
        div: the operand to divide all the elements of the matrix

    Raises:
        TypeError: if the matrix is not a float or integer or if div is not
            a number
        ZeroDivisionError: if division by zero occurs

    Return:
        A new matrix of elements with the number round to 2 decimal places

    """

    new_matrix = [[] for _ in range(len(matrix))]
    row_size = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")

    for row in matrix[1:]:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result = matrix[i][j] / div
            if div == 0:
                raise ZeroDivisionError("division by zero")
            res = round(result, 2)
            new_matrix[i].append(res)
    return new_matrix
