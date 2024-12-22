import os
import sys
import random



def drawBoard(liczba_kolumn, liczba_wierszy, pozycja_gracza):
    """rysuje plansze"""

    zapisany_graf_wiersz = ""

    for nr_kolumny in range(0, liczba_kolumn):
    	zapisany_graf_wiersz = zapisany_graf_wiersz + " _"
    print(zapisany_graf_wiersz)

    for nr_wiersza in range(0, liczba_wierszy):
        zapisany_graf_wiersz = "|"
        for nr_kolumny in range(0, liczba_kolumn):
            if pozycja_gracza[0] == nr_kolumny and pozycja_gracza[1] == nr_wiersza:
                zapisany_graf_wiersz = zapisany_graf_wiersz + "x|"

            else:
                zapisany_graf_wiersz = zapisany_graf_wiersz + "_|" 
        print(zapisany_graf_wiersz)



def move(command, position):
    if command == "w":
        if position[1] > 0:
            position[1] = position[1] - 1

    elif command == "s":
        if position[1] < wysokosc - 1:
            position[1] = position[1] + 1

    elif command == "a":
        if position[0] > 0:
            position[0] = position[0] - 1

    elif command == "d":
        if position[0] < szerokosc - 1:
            position[0] = position[0] + 1



# -------------------------------------------------

pozycja_gracza = [1, 1]
rozmiar_planszy = int(input("podaj wielkość planszy: "))
szerokosc = rozmiar_planszy
wysokosc = rozmiar_planszy

drawBoard(szerokosc, wysokosc, pozycja_gracza)


for i in range(0,100):
    command = input()
    if command == "x":
    	break
    move(command, pozycja_gracza)

    drawBoard(szerokosc, wysokosc, pozycja_gracza)


# pozdro, wawrzyniec



