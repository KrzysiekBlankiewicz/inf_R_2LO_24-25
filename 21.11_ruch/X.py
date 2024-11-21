import os
import sys
import random
import math
def drawBoard(columns, rows, playerPosition):
    rowString = ""

    for j in range(0, columns):
    	rowString = rowString + " _"
    print(rowString)

    for i in range(0, rows):
        rowString = "|"
        for j in range(0, columns):
            x = playerPosition[0]
            y = playerPosition[1]
            if [i, j] == [x, y]:
                rowString = rowString + "x" + "|"
            else:
                rowString = rowString + "_" + "|"
        print(rowString)

def move(command, position, xSize, ySize):
    if command == "w" and position[0] > 0:
        position[0] = position[0] - 1
    
    if command == "s" and position[0] < xSize - 1:
        position[0] = position[0] + 1

    if command == "a" and position[1] > 0:
        position[1] = position[1] - 1

    if command == "d" and position[1] < ySize - 1:
        position[1] = position[1] + 1

    return position

position = [1,1]
size = int(input("podaj wielkość planszy"))
xSize = size
ySize = size

drawBoard(xSize, ySize, position)

for i in range(0,100):
    command = input()
    if command == "x":
    	break

    position = move(command, position, xSize, ySize)
    drawBoard(xSize, ySize, position)
    
