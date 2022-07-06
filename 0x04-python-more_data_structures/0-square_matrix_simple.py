#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix.append([j**2 for j in x])
    return(new_matrix)
