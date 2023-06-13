#!/usr/bin/python3

""" A function that returns list of lists of integers """


def pascal_triangle(n):
    """ Return the pascal's triangle of n

    Args:
        n: the number of rows to generate

    Return:
        list of lists of integers
    """
    if n <= 0:
        return []

    trian = [[1]]

    for k in range(1, n):
        my_row = [1]
        for j in range(1, k):
            my_row.append(trian[k - 1][j - 1] + trian[k - 1][j])
        my_row.append(1)
        trian.append(my_row)
    return trian
