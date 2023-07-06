#!/usr/bin/python3
"""
matrix_divided: function that divides a matrix by n
Args:
matrix(matrix): input a 2d matrix expected
"""


def matrix_divided(matrix, div):
    """get a new matrix that is divided by div.

    Args:
        matrix (matix):when you put a wrong input
        div (int, float):when you put a wrong input

    Raises:
        TypeError:when you put a wrong input
        ZeroDivisionError:when you put a wrong input
        TypeError:when you put a wrong input
        TypeError:when you put a wrong input
        TypeError:when you put a wrong input
        TypeError:when you put a wrong input

    Returns:
        matrix: returns a new matrix
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row_matrix = []
    if isinstance(matrix, int) or isinstance(matrix, float):
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")

    for mat in matrix:
        if isinstance(matrix[0], int) or isinstance(matrix[0], float):
            raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
        for i in mat:
            if len(mat) < len(matrix[0]) or len(mat) > len(matrix[0]):
                raise TypeError("Each row of the matrix must \
                        have the same size")
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
            row_matrix.append(round((i / div), 2))
        new_matrix.append(row_matrix)
        row_matrix = []

    return new_matrix
