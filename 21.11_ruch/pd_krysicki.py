import os
import sys
import random

def drawBoard(columns, rows, pos):
	rowString = ""

	for j in range(0, columns):
		rowString = rowString + " _"
	print(rowString)

	for i in range(0, rows):
		rowString = "|"
		for j in range(0, columns):
			if pos[0] == j and pos[1] == i:
				rowString = rowString + "x" + "|"
			else:
				rowString = rowString + "_" + "|"
		print(rowString)

def moveFromInput(com):
	x = 0
	y = 0
	if com == "s":
		y = y + 1		
	if com == "a":
		x = x - 1
	if com == "w":
		y = y - 1
	if com == "d":
		x = x + 1
	result = [x, y]
	return result
    
def addTwoElemVectors(v1, v2):
	result = [0, 0]
	result[0] = v1[0] + v2[0]
	result[1] = v1[1] + v2[1]
	return result

def clampToBoard(xSize, ySize, position):
	if position[0] < 0:
		position[0] = 0
	if position[0] >= xSize:
		position[0] = xSize - 1
	if position[1] < 0:
		position[1] = 0
	if position[1] >= ySize:
		position[1] = ySize - 1
	return position

def move(command, position, xSize, ySize):
	move = moveFromInput(command)
	newPosition = addTwoElemVectors(position, move)
	return clampToBoard(xSize, ySize, newPosition)

# -------------------------------------------------

position = [1, 1]
size = int(input("podaj wielkość planszy "))
xSize = size
ySize = size

drawBoard(xSize, ySize, position)

for i in range(0,100):
	command = input()
	if command == "x":
		break
    
	position = move(command, position, xSize, ySize)
    
	drawBoard(xSize, ySize, position)
