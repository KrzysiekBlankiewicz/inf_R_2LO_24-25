import os
import sys
import random

def drawBoard(columns, rows, playerPosition):
    rowString = ""
    gracz_postawiony = 0
    wrog_postawiony = 0
    for j in range(0, columns):
    	rowString = rowString + " _"
    print(rowString)

    for i in range(0, rows):
        rowString = "|"
        for j in range(0, columns):
            if j == playerPosition[1] and gracz_postawiony == 0 and i == position[0]:
                rowString = rowString + "x" + "|"
                gracz_postawiony = 1
            elif j == enemy_pos[1] and wrog_postawiony == 0 and i == enemy_pos[0]:
                rowString = rowString + "o" + "|"
                wrog_postawiony = 1
            else:
                rowString = rowString + "_" + "|"
        print(rowString)

def move(position, xSize, ySize):
        zmiana = input("podaj pozycję poruszaj się w,a,s,d")
        if zmiana == "w" and position[0] > 0:
            position[0] = position[0] - 1
        if zmiana == "a" and position[1] > 0:
            position[1] = position[1] - 1
        if zmiana == "s" and position[0] < ySize - 1:
            position[0] = position[0] + 1
        if zmiana == "d" and position[1] < xSize - 1:
            position[1] = position[1] + 1
def move_enemy(position, xSize, ySize):
        zmiana = random.randint(1, 4)
        if zmiana == 1 and enemy_pos[0] > 0:
            enemy_pos[0] = enemy_pos[0] - 1
        if zmiana == 2 and enemy_pos[1] > 0:
            enemy_pos[1] = enemy_pos[1] - 1
        if zmiana == 3 and enemy_pos[0] < ySize - 1:
            enemy_pos[0] = enemy_pos[0] + 1
        if zmiana == 4 and enemy_pos[1] < xSize - 1:
            enemy_pos[1] = enemy_pos[1] + 1
# -------------------------------------------------

position = [0,0]
size = int(input("podaj wielkość planszy"))
xSize = size
ySize = size
enemy_pos = [0,0]
enemy_pos[0] = random.randint(1, xSize)
enemy_pos[1] = random.randint(1, ySize)

drawBoard(xSize, ySize, position)

for i in range(0,1000000000000000000000000000000):
    move(position, xSize, ySize)
    drawBoard(xSize, ySize, position)
    move_enemy(position, xSize, ySize)






