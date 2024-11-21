import os
import sys
import random
import random
def drawBoard(columns, rows, pp):
    rowString = ""

    for j in range(0, columns):
    	rowString = rowString + " _"
    print(rowString)

    for i in range(0, rows):
        rowString = "|"
        for j in range(0, columns):
            if j == pp[1] and i == pp[0]:
                  rowString = rowString + "x" + "|"
            else:
                  rowString = rowString + "_" + "|"
        print(rowString)

def move(com, pp, xs, ys):
     
    if com == "w" and pp[0] > 0:

          pp[0] = pp[0] - 1
    if com == "s" and pp[0] < size - 1:

       pp[0] = pp[0] + 1
    if com == "d" and pp[1] < size - 1:

       pp[1] = pp[1] + 1
    if com == "a" and pp[1] > 0 :

       pp[1] = pp[1] - 1
    return pp
# -------------------------------------------------

position = [1,1]
bpos = [0, 0]
size = int(input("podaj wielkość planszy"))
xs = size
ys = size

drawBoard(xs, ys, position)

for i in range(0,10000):
       com = input()
    if com == "x":
    	break

   
    position = move(com, position, xs, ys)
    drawBoard(xs, ys, position)
    