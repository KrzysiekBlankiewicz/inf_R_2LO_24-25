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
            x_pos = playerPosition[0]
            y_pos = playerPosition[1]
            if x_pos == i and y_pos == j:
                rowString = rowString + "x" + "|"
            else:
                rowString = rowString + "_" + "|"
        print(rowString)

def move(command, position):
    if command == "w" and position[0] > 0:
        position[0] = position[0] - 1
    if command == "d" and position[1] > ySize:
        position[1] = position[1] + 1
    if command == "a" and position[1] > 0:
        position[1] = position[1] - 1
    if command == "s" and position[0] < xSize:
        position[0] = position[0] + 1
    return position
    

# -------------------------------------------------
position = [1,1]
size = int(input("podaj wielkość planszy"))
xSize = size
ySize = size

drawBoard(xSize, ySize, position)

for i in range(0,100):
    command = input()
    if command == "x":
    	break

    x = move(command, position)

    drawBoard(xSize, ySize, x)
#DONT MOVE ZA GRANICE
