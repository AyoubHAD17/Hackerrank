from math import inf


def formingMagicSquare(matrix = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]):
    # n is the order of magic square
    # the constant sum is called the magic constant
    theMagicConstant = -inf
    for i in range(len(matrix)):
        theSum = 0
        for j in range(len(matrix[i])):
            theSum+=matrix[i][j]
        if theSum > theMagicConstant:
            theMagicConstant = theSum
    if matrix[0][0] + matrix[1][0] + matrix[2][0] > theMagicConstant:
        theMagicConstant = matrix[0][0] + matrix[1][0] + matrix[2][0]
    if matrix[0][1] + matrix[1][1] + matrix[2][1] > theMagicConstant:
        theMagicConstant = matrix[0][1] + matrix[1][1] + matrix[2][1]
    if matrix[0][2] + matrix[1][2] + matrix[2][2] > theMagicConstant:
        theMagicConstant = matrix[0][2] + matrix[1][2] + matrix[2][2]
    if matrix[0][0] + matrix[1][1] + matrix[2][2] > theMagicConstant:
        theMagicConstant = matrix[0][0] + matrix[1][1] + matrix[2][2]
    if matrix[0][2] + matrix[1][1] + matrix[2][0] > theMagicConstant:
        theMagicConstant = matrix[0][2] + matrix[1][1] + matrix[2][0]

    for l in range(len(matrix)):
        for k in range(len(matrix[i])):
            




formingMagicSquare()
