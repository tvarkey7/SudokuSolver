# SudokuSolver

This sudoku solver takes in a sudoku, which is in a 9x9 numpy array. 

It first checks whether the array that was given is a valid one. For exanple, checking that a small 3x3 sqaure doesn't have the same number in it twice.
If it's invalid, then it returns a numpy array, which is all filled with -1, indicating that it is invalid and can't be solved. 

It then attempts to solve the sudoku. If it can't, then it returns a 9x9 numpy array of -1.
If it can be solved, it returns the solved sudoku. 
