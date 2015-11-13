#!/usr/bin/python

N = 4
board = [[0]*N for i in range(N)]

# for reference:
#   array[row][column]

def print_board():
	for i in range(N):
		print board[i]
	print


def is_safe(row, column):
	
	# check row to the left
	for i in range(0, column):
		if board[row][i] == 1:
			return False

	i = row-1
	j = column-1
	# check uppder diagonal
	while i >=0 and j >=0:
		if board[i][j] == 1:
			return False
		i = i-1
		j = j-1
	
	i = row+1
	j = column-1
	# check lower diagonal
	while i < N and j >= 0:
		if board[i][j] == 1:
			return False
		i = i+1
		j = j-1

	return True



def n_queens_rec(column, queens_placed):
	if queens_placed == N:
		return True

	for row in range(N):
		if is_safe(row, column):
			board[row][column] = 1
			queens_placed = queens_placed+1
			#print_board()
			if n_queens_rec(column+1, queens_placed) == True:
				return True
			else:
				board[row][column] = 0
				queens_placed = queens_placed-1
	return False

def n_queens():
	n_queens_rec(0,0)


n_queens()
print_board()
#print is_safe(0,0)
