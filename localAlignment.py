## Lauren Yancy
## Problem Set 2: Local Alignment


import argparse
import pandas as pd
import numpy as np


def readSeq(s1, s2):
    # opens files in read mode
    s1 = open(s1, 'r')
    s2 = open(s2, 'r')

    # reads file from 2nd line down (without preamble)
    aminoChain1AsString = s1.readlines()[1:]
    aminoChain2AsString = s2.readlines()[1:]

    aminoChain1AsString= aminoChain1AsString[-1]
    aminoChain2AsString = aminoChain2AsString[-1]


    #print(aminoChain1, aminoChain2)
    return(aminoChain1AsString, aminoChain2AsString)


def matrixBuild(matrix):
    scoreMatrix = open(matrix, 'r')
    scoreMatrix = pd.read_csv(matrix, header=6, sep='\t')
    #print(scoreMatrix)
    return scoreMatrix



def createAlignmentMatrix(AA1, AA2, gapPen):
    # aminoChain1 into a list
    # row and column are reserved names


    aminoChain1 = AA1
    aminoChain2 = AA2
    # Use numpy matrix
    r = []
    c = []

    for element in range(0, len(aminoChain1)-1):
        c.append(aminoChain1[element])

    for element in range(0, len(aminoChain2)-1):
        r.append(aminoChain2[element])


    gapPenalty = gapPen
    rowLength = len(r)
    columnLength = len(c)
    direction = 'l'
    greatestScoreValue = 0

    print(r, c)
    print('____________')
    print(gapPenalty, rowLength, columnLength)


    #use numpy, build a matrix by column of zeros, then backfill with scores

    residueScoreMatrix = np.zeros((rowLength, columnLength), dtype=float)
    # this should print a r by c matrix of zeros with type float

    #print(residueScoreMatrix)

    # i = col index, j = row index

    for i in range(1, columnLength-1):
        for j in range(1, rowLength -1):
            print(i, j)
            rawScore = matrixSearch(c[i], r[j], scoreMatrix)
            upScore = matrixSearch(c[i], r[j-1], scoreMatrix)
            upScore = (upscore - gapPenalty)

            if upScore < 0:
                    upScore = 0

            diagonalScore = matrixSearch(c[i-1], r[j-1], scoreMatrix)
            if diagonalScore < 0:
                diagonalScore = 0

            leftScore = matrixSearch(c[i-1], r[j], scoreMatrix)
            leftScore = (leftScore - gapPenalty)

            if leftScore < 0:
                leftScore = 0

            if upScore >= diagonalScore:
                greatestScoreValue = upScore
                direction = 'u'

            if upScore < leftScore:
                greatestScoreValue = leftScore
                direction = 'l'

            if diagonalScore > leftScore:
                greatestScoreValue = diagonalScore
                direction = 'd'

            finalMatrixScore = (greatestScoreValue + rawScore)

            residueScoreMatrix[i][j] = [finalMatrixScore, direction]

    return residueScoreMatrix


    #leftScore = ( # score at (i-1, j) - gapPenalty)
        # if (leftScore < 0):
            # leftScore = 0
    # upScore = ( # score at (i, j-1) - gapPenalty
        # if (upScore < 0):
            # upScore = 0
    # diagonalScore = #just the score diagonal


def matrixSearch(residue1, residue2, scoreMatrix):

    scoreMatrixImport = scoreMatrix
    matrixScore = scoreMatrix[residue1][residue2]
    return matrixScore


def traceBack(alignmentMatrix, aminoChain1, aminoChain2):

    # sets parameters for following loop
    columnLength = len(aminoChain1)
    rowLength = len(aminoChain2)

    # sets defaults to prevent crashes
    formerScore = 0
    scoreOrigin = d


    ## Find the highest score for the start location
    ## alignmentMatrix will return a score (data type integer) and a location (data type char) as a list
    ## separate the two values
    ## use the integer as score index 0
    ## use the char as location (u = up, l = left, d = diagonal) index 1
    ## find the highest score to start the traceback

    for k in range(0, rowLength-1):
        for m in range (0, columnLength -1):

            # from 0 to end of sequences
            # matrixData receives a list

            matrixData = alignmentMatrix[k][m]
            # The List for the matrix value is in the order score, location
            # Uses the list index to extract data to compare

            currentScore = matrixData[0]
            scoreOrigin = matrixData[1]

            # Finds the largest score from the matrix
            # if the current score in the loop is larger than the previous, overwrite the previous and store
            # the relevant information
            if currentScore >= formerScore:
                formerScore = currentScore
                maxScoreOrigin = scoreOrigin
                columnLocation = m
                rowLocation = k



    # Takes the relevant information from the previous nested for loops and inserts it as a matrix  location and
    # direction the score originated (which is the next point in the traceback)

    ## Establishes a list for start point in traceback
    startPointData = alignmentMatrix[rowLocation][columnLocation]

    #l,d or u
    firstDirection = maxScoreOrigin

    #place holder for nextScore using the formerScore
    nextScore = formerScore

    # Establish 2 empty lists to fill with the alignment sequences for the display
    homeSequence = []
    comparedSequence = []


    ## A second for loop to check the 3 associated score lengths for the next steps in paths
    ## use the char as location (u = up, l = left, d = diagonal)

    comparedSequence.append(alignmentMatrix.row.values[rowLocation])
    homeSequence.apprend(alignmentMatrix.column.values[columnLocation])

    nextDirection = maxScoreOrigin

    while nextScore != 0:
        if nextDirection == l:
            comparedSequence.append('-')
            homeSequence.append(alignmentMatrix.column.values[columnLocation])
            columnLocation = columnLocation -1
            nextData = alignmentMatrix[rowLocation][columnLocation]
            nextScore = nextData[0]

        elif nextDirection == d:
            comparedSequence.append(alignmentMatrix.row.values[rowLocation])
            homeSequence.append(alignmentMatrix.column.values[columnLocation])
            columnLocation = columnLocation - 1
            rowLocation = rowLocation - 1
            nextData = alignmentMatrix[rowLocation][columnLocation]
            nextScore = nextData [0]

        elif nextDirection == u:
            comparedSequence.append('-')
            homeSequence.append(alignmentMatrix.column.values[columnLocation])
            rowLocation = rowLocation - 1
            nextData = alignmentMatrix[rowLocation][columnLocation]
            nextScore = nextData [0]


    print(homeSequence)
    print(comparedSequence)


if __name__ == '__main__':

    # creates menu options
    parser = argparse.ArgumentParser(description="Local Alignment")
    parser.add_argument('-s1', dest='s1', required=True, help='Sequence 1 File Name')
    parser.add_argument('-s2', dest='s2', required=True, help='Sequence 2 File Name')
    parser.add_argument('-m', dest='matrix', required=True, help='Scoring Matrix File')
    parser.add_argument('-g', dest='gapPenalty', default=11, type=int, help='Gap Penalty')
    parser.add_argument('-o', dest='returnFile', help='Output File')

    # defines where args comes from
    args = parser.parse_args()
    print(args)

    #exit()

    #s1 = input("Enter sequence 1 file")
    #s2 = input("Enter sequence 2 file")

    (AA1, AA2) = readSeq(args.s1, args.s2)


    #print(AA1, AA2)
    #exit()

    # Generate a score matrix
    scoreMatrix = matrixBuild(args.matrix)
    #print(scoreMatrix)
    #exit()

    gapPen = args.gapPenalty
    #exit()

    alignmentMatrix = createAlignmentMatrix(AA1, AA2, gapPen)
    print(alignmentMatrix)
    #exit()

    traceBackSequence = traceBack(alignmentMatrix, AA1, AA2)


    exit()



