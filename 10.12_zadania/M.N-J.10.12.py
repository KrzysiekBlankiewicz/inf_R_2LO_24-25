import random
def zbiory_wspolne(a1, a2, b1, b2):
    if a1 > a2:
        a1 = a2
        a2 = a1
    if b1 > b2:
        b2 = b1
        b1 = b2
    if a2 < b1 or b2 < a1:
        print("NIE")
    else:
        if a2 > b1:
            pokrycie = a2 - b1
            return pokrycie
        if a1 < b2 and b2 < a2:
            pokrycie1 = b2 - a1
            return pokrycie1

a1 = 1
a2 = 8
b1 = 5
b2 = 10

wynik = zbiory_wspolne(a1, a2, b1, b2)
print(wynik)
