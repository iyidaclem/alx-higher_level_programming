#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix) - 1):
        print("{}".format(matrix[i][0]), end="")
        for j in range(len(matrix[i]) - 1):
            print(" {:d}".format(matrix[i][j + 1]), end="")
        print()
