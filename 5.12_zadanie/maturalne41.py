import math




def jest_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


punkty = []

file = open("punkty.txt")
for l in file:
        x, y = map(int, l.split())
        punkty.append((x, y))

ilosc_pierwszych = sum(1 for x, y in punkty if jest_pierwsza(x) and jest_pierwsza(y))
print(ilosc_pierwszych)