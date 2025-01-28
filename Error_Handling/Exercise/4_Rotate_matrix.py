class MatrixContentError(Exception):
    pass

class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()
    try:
        line = [int(x) for x in line]
    except ValueError:
        raise MatrixContentError("The matrix must consist of only integers")

    if not line:
        for i in range(len(mtrx)):
            if len(mtrx[i]) != len(mtrx):
                raise MatrixSizeError("The size of the matrix is not a perfect square")
        break
    mtrx.append(line)

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
