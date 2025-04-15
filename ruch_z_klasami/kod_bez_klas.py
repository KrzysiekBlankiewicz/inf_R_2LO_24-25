import os
import sys
import random

def drawBoard(columns, rows, playerPosition):
    rowString = ""

    for j in range(0, columns):
    	rowString = rowString + " _"
    print(rowString)

    for i in range(0, rows):
        rowString = "|"
        for j in range(0, columns):
            if playerPosition[0] == j and playerPosition[1] == i:
                rowString = rowString + "x" + "|"
            else:
               rowString = rowString + "_" + "|"
        print(rowString)

def moveFromInput(input):
	if input == "w":
		return [0, -1]
	elif input == "s":
		return [0, 1]
	elif input == "a":
		return [-1, 0]
	elif input == "d":
		return [1, 0]
	else:
		return [0,0]
	
def addTwoElemVectors(a, b):
	result = [0,0]
	result[0] = a[0] + b[0]
	result[1] = a[1] + b[1]
	return result

def clampToBoard(xSize, ySize, position):
	if position[0] < 0 :
		position[0] = 0
	if position[0] >= xSize :
		position[0] = xSize - 1
	if position[1] < 0 :
		position[1] = 0
	if position[1] >= ySize :
		position[1] = ySize - 1

def move(command, position):
	move = moveFromInput(command)
	
	newPosition = addTwoElemVectors(position, move)
	clampToBoard(xSize, ySize, newPosition)
	return newPosition

# -------------------------------------------------

position = [1, 1]
size = int(input("podaj wielkość planszy"))
xSize = size
ySize = size

drawBoard(xSize, ySize, position)

while True:
    command = input()
    if command == "x":
    	break
    
    position = move(command, position)
    
    drawBoard(xSize, ySize, position)






