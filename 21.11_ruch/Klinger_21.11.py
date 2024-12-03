import os
import sys
 
def drawBoard(columns, rows, playerPosition):
    rowString = ""
    for j in range(columns):
        rowString += " _"
    print(rowString)
 
    for i in range(rows):
        rowString = "|"
        for j in range(columns):
            if [j, i] == playerPosition:
                rowString += "X|"
            else:
                rowString += "_|"
        print(rowString)
 
def moveFromInput(input):
    result = [0, 0]
    if input == "w":
        result = [0, -1]
    elif input == "s":
        result = [0, 1]
    elif input == "a":
        result = [-1, 0]
    elif input == "d":
        result = [1, 0]
    return result
 
def addTwoElemVectors(a, b):
    result = [0, 0]
    result[0] = a[0] + b[0]
    result[1] = a[1] + b[1]
    return result
 
def clampToBoard(xSize, ySize, position):
    position[0] = max(0, min(position[0], xSize - 1))
    position[1] = max(0, min(position[1], ySize - 1))
 
def move(command, position, xSize, ySize):
    moveVector = moveFromInput(command)
    newPosition = addTwoElemVectors(position, moveVector)
    clampToBoard(xSize, ySize, newPosition)
    return newPosition
 
playerPosition = [1, 1]
 
size = int(input("podaj wielkość planszy"))
xSize = size
ySize = size
 
drawBoard(xSize, ySize, playerPosition)
 
for _ in range(100):
    command = input("")
    if command == "x":
        break
 
    playerPosition = move(command, playerPosition, xSize, ySize)
 
    drawBoard(xSize, ySize, playerPosition)