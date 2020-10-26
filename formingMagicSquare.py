from math import inf



def formingMagicSquare(matrix):
    # n is the order of magic square
    # the constant sum is called the magic constant
    theMagicConstant = -inf
    theCost = 0
    for i in range(len(matrix)):
        theSum = 0
        for j in range(len(matrix[i])):
            theSumRow+=matrix[i][j]
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
    theReplacer = [inf, [0, 0], 0]
    if abs(matrix[0][0] - (theMagicConstant - (matrix[0][1] + matrix[0][2]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[0][0] - (theMagicConstant - (matrix[0][1] + matrix[0][2])))
        theReplacer[1] = [0, 0]
        theReplacer[2] = theMagicConstant - (matrix[0][1] + matrix[0][2])
    if abs(matrix[0][1] - (theMagicConstant - (matrix[0][0] + matrix[0][2]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[0][1] - (theMagicConstant - (matrix[0][0] + matrix[0][2])))
        theReplacer[1] = [0, 1]
        theReplacer[2] = theMagicConstant - (matrix[0][0] + matrix[0][2])
    if abs(matrix[0][2] - (theMagicConstant - (matrix[0][0] + matrix[0][1]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[0][2] - (theMagicConstant - (matrix[0][0] + matrix[0][1])))
        theReplacer[1] = [0, 2]
        theReplacer[2] = theMagicConstant - (matrix[0][0] + matrix[0][1])
    theCost+=theReplacer[0]
    matrix[theReplacer[1][0]][theReplacer[1][1]] = theReplacer[2]
    theReplacer = [inf, [0, 0], 0]
    if abs(matrix[0][0] - (theMagicConstant - (matrix[1][0] + matrix[2][0]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[0][0] - (theMagicConstant - (matrix[1][0] + matrix[2][0])))
        theReplacer[1] = [0, 0]
        theReplacer[2] = theMagicConstant - (matrix[1][0] + matrix[2][0])
    if abs(matrix[1][0] - (theMagicConstant - (matrix[0][0] + matrix[2][0]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[1][0] - (theMagicConstant - (matrix[0][0] + matrix[2][0])))
        theReplacer[1] = [1, 0]
        theReplacer[2] = theMagicConstant - (matrix[0][0] + matrix[2][0])
    if abs(matrix[2][0] - (theMagicConstant - (matrix[0][0] + matrix[1][0]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[2][0] - (theMagicConstant - (matrix[0][0] + matrix[1][0])))
        theReplacer[1] = [2, 0]
        theReplacer[2] = theMagicConstant - (matrix[0][0] + matrix[2][0])
    theCost+=theReplacer[0]
    matrix[theReplacer[1][0]][theReplacer[1][1]] = theReplacer[2]
    theReplacer = [inf, [0, 0], 0]
    if abs(matrix[0][0] - (theMagicConstant - (matrix[1][1] + matrix[2][2]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[0][0] - (theMagicConstant - (matrix[1][1] + matrix[2][2])))
        theReplacer[1] = [0, 0]
        theReplacer[2] = theMagicConstant - (matrix[1][1] + matrix[2][2])
    if abs(matrix[1][1] - (theMagicConstant - (matrix[0][0] + matrix[2][2]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[1][1] - (theMagicConstant - (matrix[0][0] + matrix[2][2])))
        theReplacer[1] = [1, 1]
        theReplacer[2] = theMagicConstant - (matrix[0][0] + matrix[2][2])
    if abs(matrix[2][2] - (theMagicConstant - (matrix[0][0] + matrix[1][1]))) < theReplacer[0]:
        theReplacer[0] = abs(matrix[2][2] - (theMagicConstant - (matrix[0][0] + matrix[1][1])))
        theReplacer[1] = [2, 2]
        theReplacer[2] = theMagicConstant - (matrix[0][0] + matrix[1][1])
    theCost+=theReplacer[0]
    matrix[theReplacer[1][0]][theReplacer[1][1]] = theReplacer[2]
    theCost+=(theMagicConstant - (matrix[0][2] + matrix[1][2] + matrix[2][2]))
    matrix[1][2]+=(theMagicConstant - (matrix[0][2] + matrix[1][2] + matrix[2][2]))
    theCost+=(theMagicConstant - (matrix[2][0] + matrix[2][1] + matrix[2][2]))
    matrix[2][1]+=(theMagicConstant - (matrix[2][0] + matrix[2][1] + matrix[2][2]))
