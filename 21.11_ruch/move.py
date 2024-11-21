import os
import sys
import random

def drawBoard(columns, rows, plPos, opPos):
	rowString = ""

	for j in range(0, columns):
		rowString = rowString + " _"
	print(rowString)
	for i in range(0, rows):
		rowString = "|"
		for j in range(0, columns):
			px = opPos[0]
			py = opPos[1]
			x = plPos[0]
			y = plPos[1]
			if j == y and i == x:
				rowString = rowString + "x" + "|"
			elif j == py and i == px:
				rowString = rowString + "o" + "|"
			else:
				rowString = rowString + "_" + "|"
		print(rowString)

def move(com, plPos, size):
	x = plPos[0]
	y = plPos[1]
	if com == "a":
		y = y - 1
		if y < 0:
			y = y + 1			
	if com == "w":
		x = x - 1
		if x < 0:
			x = x + 1	
	if com == "d":
		y = y + 1
		if y > size-1:
			y = y - 1	
	if com == "s":
		x = x + 1
		if x > size-1:
			x = x - 1	
	poz = (x, y)
	return poz

def opmove(com, opPos, size):
	x = opPos[0]
	y = opPos[1]
	if com == "a":
		y = y - 1
		if y < 0:
			y = y + 1			
	if com == "w":
		x = x - 1
		if x < 0:
			x = x + 1	
	if com == "d":
		y = y + 1
		if y > size-1:
			y = y - 1	
	if com == "s":
		x = x + 1
		if x > size-1:
			x = x - 1	
	oppoz = (x, y)
	return oppoz

# -------------------------------------------------
position = [0,0]
size = int(input("podaj wielkość planszy"))
xSize = size
ySize = size

oppos = [size-1, size-1]
drawBoard(xSize, ySize, position, oppos)


for i in range(0,100):
	oplicz = random.randint(1,4)
	opcom = ""
	if oplicz == 1:
		opcom = 'w'
	if oplicz == 2:
		opcom = 'a'
	if oplicz == 3:
		opcom = 's'
	if oplicz == 4:
		opcom = 'd'
	command = input()
	if command == "x":
		break
	oppos = opmove(opcom, oppos, size)
	position = move(command, position, size)
	drawBoard(xSize, ySize, position, oppos)





