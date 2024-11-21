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
            pass
            rowString = rowString + "_" + "|"
        print(rowString)

def moveFromInput(input):
    result = []
    pass
    return result
    
def addTwoElemVectors(a, b):
    result = [0,0]
    pass
    return result

def clampToBoard(xSize, ySize, position):
    pass

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

for i in range(0,100):
    command = input()
    if command == "x":
    	break
    
    position = move(command, position)
    
    drawBoard(xSize, ySize, position)






