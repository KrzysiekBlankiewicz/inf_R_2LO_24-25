
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
import random

def drawBoard(c, r, pp,ops):
    rowString = ""

    for j in range(0, c):
        rowString = rowString + " _"
    print(rowString)

    for i in range(0, r):
        rowString = "|"
        for j in range(0, c):
            x = pp[0]
            y = pp[1]
            ox = ops[0]
            oy = ops[1]
            if j == y and i ==x:
                rowString = rowString + "x" + "|"
            elif j == oy and i ==ox:
                rowString = rowString + "o" + "|"
            else:
                rowString = rowString + "_" + "|"
        print(rowString)
			
def move(com, pp,size,ops):
    x = pp[0]
    y = pp[1]
    ox = ops[0]
    oy = ops[1]
    if com == 'a':
        y = y-1
        if y < 0:
                y = y+1
    if com == 'w':
        x = x-1
        if x < 0:
            x = x+1
    if com == 's':
        x = x+1
        if x > size-1:
            x=x-1
    if com == 'd':
        y = y+1
        if y > size-1:
            y = y-1
    poz = (x,y)
    return poz 

# -------------------------------------------------
ops = [1,1]
position = [1,3]
size = int(input("podaj wielkość planszy"))
xSize = size
ySize = size

drawBoard(xSize, ySize, position,ops)

for i in range(0,100):
    command = input()
    if command == "x":
        break
    if 
    position = move(command,position,size,ops)
    drawBoard(xSize,ySize,position,ops)
	
    
#drawBoard(xSize, ySize, position)












