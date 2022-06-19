import numpy

matrix_1 = [[12, 17, 3],
    [4, 5, 6],
    [7, 8, 9]]

matrix_2 = [[5, 18, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

result = numpy.dot(matrix_1, matrix_2)

print(result)
