import os
import sys
import random

def drawBoard(columns, rows, playerPosition):
	#os.system('cls' if os.name == 'nt' else 'clear')
	rowString = ""
	ySize = columns
	xSize = rows
	for j in range(0, columns):
		rowString += " _"
	print(rowString)

	for i in range(0, rows):
		rowString = "|"
		for j in range(0, columns):
			if [i , j] == playerPosition:
				rowString = rowString + "x" + "|"
			else:
				rowString = rowString + "_" + "|"
		print(rowString)

def move(command, position, xSize, ySize):
    
	if command == "w" and position[0] > 0:
		position[0] -= 1
    
	elif command == "s" and position[0] < ySize - 1:
		position[0] += 1
    
	elif command == "a" and position[1] > 0:
		position[1] -= 1
    
	elif command == "d" and position[1] < xSize - 1:
		position[1] += 1

	
# -------------------------------------------------

position = [1,1]
size = int(input("Podaj wielkość planszy"))
xSize = size
ySize = size

drawBoard(xSize, ySize, position)

for i in range(0,100):
	command = input()
	if command == "x":
    		break

	move(command, position, xSize, ySize)

	drawBoard(xSize, ySize, position)