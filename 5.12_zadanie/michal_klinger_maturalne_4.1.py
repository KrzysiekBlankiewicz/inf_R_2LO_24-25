import math

def jest_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

punkty = []
with open("punkty.txt") as plik:
    for linia in plik:
        x, y = map(int, linia.split())
        punkty.append((x, y))

liczba_punktow_pierwszych = sum(1 for x, y in punkty if jest_pierwsza(x) and jest_pierwsza(y))

print(liczba_punktow_pierwszych)


