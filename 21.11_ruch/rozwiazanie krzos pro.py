import os
import sys
import random

def rys_tablica(kolumny, rzędy, poz_gracz):
    rowString = ""

    for j in range(0, kolumny):
    	rowString = rowString + " _"
    print(rowString)

    for i in range(0, rzędy):
        rowString = "|"
        for j in range(0, columns):
            if poz_gracz[0] == j and poz_gracz[1] == i:
                rowString = rowString + "x" + "|"
            else:
               rowString = rowString + "_" + "|"
        print(rowString)

def Ruch_podany(input):
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
	
def wektory(a, b):
	result = [0,0]
	result[0] = a[0] + b[0]
	result[1] = a[1] + b[1]
	return result

def clampToBoard(xSize, ySize, pozycja):
	if pozycja[0] < 0 :
		pozycja[0] = 0
	if pozycja[0] >= xSize :
		pozycja[0] = xSize - 1
	if pozycja[1] < 0 :
		pozycja[1] = 0
	if pozycja[1] >= ySize :
		pozycja[1] = ySize - 1

def Ruch(command, position):
	move = moveFromInput(command)
	
	newPosition = addTwoElemVectors(position, move)
	clampToBoard(xSize, ySize, newPosition)
	return newPosition

# -------------------------------------------------

position = [1, 1]
wielkość = int(input("podaj wielkość planszy"))
xSize = wielkość
ySize = wielkość

rys_tablica(xSize, ySize, position)

for i in range(0,100):
    command = input()
    if command == "x":
    	break
    
    position = Ruch(command, position)
    
    rys_tablica(xSize, ySize, position)






