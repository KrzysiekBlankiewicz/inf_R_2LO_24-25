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

def move(command, position):
    pass

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

    pass

    drawBoard(xSize, ySize, position)






