#!/usr/bin/python

# Knight's tour problem
# ---------------------
# A knight is placed on an empty corner block of a chessboard, and
# moving according to the rules of chess, must visit each square
# exactly one time.

import os
from time import sleep


def cls():
	os.system('cls' if os.name=='nt' else 'clear')


N = 8; # chess board is NxN. default = 8
board = [[0]*N for i in range(N)]
already_solved = False


def Knight(x, y, current_move):
	global already_solved

	#print current_move
	#dicks = is_board_filled()
	#print(dicks)
	cls()
	print_board()
	print
	sleep(0.5)

	# no need to do anything if it is already solved
	#   we only need one solution, not all
	if already_solved == True:
		return

	
	# move knight to every possible spot and run function again
	movements = [[2,  2, 1,  1, -2, -2, -1, -1],
					 [1, -1, 2, -2,  1, -1,  2, -2]]
	
	board[x][y] = current_move

	for i in range(len(movements[0])):
		newx = x + movements[0][i]
		newy = y + movements[1][i]
		
		# check if new coordinates are out of range
		if newx<0 or newx>=N or newy<0 or newy>=N:
			continue
		
		# recursively try every single movement
		if board[newx][newy] == 0:
			current_move += 1
			Knight(newx, newy, current_move)
			
	if is_board_filled():
		#print(already_solved)
		print_board()
		print()
		already_solved = True
	
		current_move -= 1
		board[newx][newy] = 0


def is_board_filled():
	for i in range(len(board)):
		for j in range(len(board[i])):
			# 0 means space has not been visited
			if board[i][j] == 0:
				return False
	return True


#def sum_board():
#	cur_sum = 0;
#	for i in range(len(board)):
#		for j in range(len(board[i])):
#			cur_sum = board[i][j] + cur_sum
#
#	return cur_sum

def print_board():
	for i in range(len(board)):
		print board[i]

Knight(0,0, 1)
print_board()
