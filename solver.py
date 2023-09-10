import copy
import numpy as np

def listToNumpy(sudoku):
    """
    turns the list of lists into a numpy array (the required output)
    """
    solvedSudoku = np.array(sudoku)
    return solvedSudoku


def startStateValid(sudoku):
    """
    checks the start state to see if there are any numbers in the same, row or column that would make it invalid
    """
    #rows
    for row in sudoku:
        rowNoZero = []
        rowNoDupes = []
        for nums in row:
            if nums != 0:
                rowNoZero.append(nums)
                if nums not in rowNoDupes:
                    rowNoDupes.append(nums)
        #rowNoDupes = set(rowNoZero)
        if len(rowNoZero) != len(rowNoDupes):
            return False


    for col in range(0,9):
        colNoZero = []
        colNoDupes = []
        for row in range(0,9):
            if sudoku[row][col]!=0:
                colNoZero.append(sudoku[row][col])
                if sudoku[row][col] not in colNoDupes:
                    colNoDupes.append(sudoku[row][col])
        if len(colNoZero) != len(colNoDupes):
            return False

        topLeftSquareCoords = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for coords in topLeftSquareCoords:
        sqaureNoZero = []
        squareNoDupes = []
        rowCoords = coords[0]
        colCoords = coords[1]
        rowCoordsLimit = rowCoords + 3
        colCoordsLimit = colCoords + 3
        for r in range(rowCoords,rowCoordsLimit):
            for c in range(colCoords,colCoordsLimit):
                if sudoku[r][c] != 0:
                    sqaureNoZero.append(sudoku[r][c])
                    if sudoku[r][c] not in squareNoDupes:
                        squareNoDupes.append(sudoku[r][c])
        if len(sqaureNoZero) != len(squareNoDupes):
            return False


    return True


def nextEmptyCell(sudoku,r,c):
    """
    Finds the next empty cell and returns the co-ordinates
    If there are no empty cells, returns -1, -1
    """
    for row in range(r,9):
        for column in range(c,9):
            if sudoku[row][column] == 0: #cell is "empty"
                return row,column
    return -1, -1
   
       

def isPossible(sudoku,row,col,val):
    """
    Check if 'val' can fit into the sudoku puzzle without breaking constraints
    """
    #if its in the row or column
    for i in range(0,9):
        if sudoku[row][i] == val or sudoku[i][col] == val:
            return False

    topLeftRowCoord = (row//3)*3
    topLeftColCoord = (col//3)*3
    topLeftRowCoordLim =topLeftRowCoord + 3
    topLeftColCoordLim =topLeftColCoord + 3
    #if its in the 3x3 square
    for row1 in range(topLeftRowCoord,topLeftRowCoordLim):
        for col1 in range(topLeftColCoord,topLeftColCoordLim):
            if sudoku[row1][col1] == val:
                return False
    return True

def invalidStateResponse(sudoku):
    """
    This is called if the start state is invalid.
    Returns a sudoku with all the values as -1.
    """
    for row in range(0,9):
        for column in range(0,9):
            sudoku[row][column] = -1.
    return sudoku


def solve_sudoku(sudoku, row, column):
    """
    this is where the backtracking takes place.
    First checks if there are any empty cells, if not, the sudoku is returned
    """
    row = 0
    column = 0
    row,column = nextEmptyCell(sudoku,row,column)
    if (row==-1) and (column==-1): #no empty cells left
        return True #solved
    for guess in range(1,10):
        if isPossible(sudoku,row,column,guess):
            sudoku[row][column] = guess
            if solve_sudoku(sudoku,row,column):
                return True
            sudoku[row][column] = 0
    return False


def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    if not startStateValid(sudoku):
        invalid_sudoku = invalidStateResponse(sudoku)
        solved_sudoku = listToNumpy(invalid_sudoku)
        return solved_sudoku
   
    row = 0
    column = 0
    if solve_sudoku(sudoku,row,column):
        solved_sudoku = listToNumpy(sudoku)
        return solved_sudoku
    else:
        invalid_sudoku = invalidStateResponse(sudoku)
        solved_sudoku = listToNumpy(invalid_sudoku)
        return solved_sudoku

sudoku = sudoku.tolist()
sudoku = copy.deepcopy(sudoku)
(sudoku_solver(sudoku))
