#!/usr/bin/python

from itertools import islice
	
	
def getPossibleOptions(row,column, sudoku):
	options = [1,2,3,4,5,6,7,8,9]
	
	if sudoku[row][column] != 0:
		return [sudoku[row][column]]
	
	for rowIndex in range(0,9):
		value = sudoku[rowIndex][column]
		if value in options:
			options.remove(value)

	for value in sudoku[row]:
		if value in options:
			options.remove(value)			
	

	(squareX, squareY) = getCoordOfSquare(row, column)
	
	for i in range(0,3):
		for j in range(0,3):
			value = sudoku[squareY + i][squareX + j]
			if value in options:
				options.remove(value)

	return options

def getCoordOfSquare(row, col):
	xLocation = (col / 3) * 3
	yLocation = (row / 3) * 3
	return (xLocation, yLocation)	

def findNextZero(sudoku):
	for i in range(0,9):
		for j in range(0,9):
			if 0 == sudoku[i][j]:
				return (i,j)
			
def fillSudoku(sudoku):
	locationTuple = findNextZero(sudoku)
	(solvedSudoku, completed) = fillSudokuRecursive(sudoku, locationTuple[0], locationTuple[1])
	return solvedSudoku

def sudokuFinished(sudoku):
	for row in sudoku :
		if 0 in row:
			return False
	return True
		
def fillSudokuRecursive(sudoku, row, column):
	options = getPossibleOptions(row, column, sudoku)
	if len(options) == 0:
		return (sudoku, False)
	for option in options:		
		sudoku[row][column] = option
		if sudokuFinished(sudoku):
			return (sudoku, True)
		else:
			locationTuple = findNextZero(sudoku)
			(sudokuFilled, finished) = fillSudokuRecursive(sudoku, locationTuple[0], locationTuple[1])
			if (finished):
				return (sudokuFilled, finished)
	sudoku[row][column] = 0
	return (sudoku, False)
			
def testFindNextZero(sudoku):
	while (not sudokuFinished(sudoku)):
		(x,y) = findNextZero(sudoku)
		sudoku[x][y] = 1


if __name__ == "__main__":		
	with open('p096_sudoku.txt') as f:
		sum = 0
		while True:
			linesSlice = list(islice(f, 10))
			if not linesSlice:
				break
			
			linesSlice.remove(linesSlice[0])
			for index, row in enumerate(linesSlice):
				linesSlice[index] = row.rstrip()
			
			emptySudoku = [map(int,list(linesSlice[0])),
				map(int,list(linesSlice[1])),
				map(int,list(linesSlice[2])),
				map(int,list(linesSlice[3])),
				map(int,list(linesSlice[4])),
				map(int,list(linesSlice[5])),
				map(int,list(linesSlice[6])),
				map(int,list(linesSlice[7])),
				map(int,list(linesSlice[8]))]

			solvedSudoku = fillSudoku(emptySudoku)
			
			row1 = solvedSudoku[0]
			
			tempSum = row1[0]*100 + row1[1]*10 + row1[2]
			sum += tempSum

	print sum