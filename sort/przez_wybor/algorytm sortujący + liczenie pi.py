import time
import random


#LOSOWANIE

tab = []
for i in range (0, 1000):
    tab.append(random.randint(1,10000))
print(tab)

#SORTOWANIE
current_time = time.time()
Z1 = 0
for k in range(0,999):
    for j in range(0, 999):
        if j < 999 and tab[j] > tab[j+1]:
            z1 = tab[j]
            tab[j] = tab[j+1]
            tab[j+1] = z1
        if j == 999 and tab[j - 1] > tab[j+1]:
            z1 = tab[j-1]
            tab[j-1] = tab[j]
            tab[j] = z1
current_time2 = time.time()
minimum = tab[0]
maximum = tab[999]
print(tab)
print(minimum)
print(maximum)
czas = current_time2 - current_time
print(czas)

#_______________________________________________________________________#
#LICZENIE PI#
czas_pi1 = time.time()
środekx = 100000000000
środeky = 100000000000
w_okręgu = 0
wszystkie = 0
poza_okręgiem = 0
pktx = []
pkty = []
for i in range(0,100000000000):
    pktx.append(random.randint(0,200000000000))
    pkty.append(random.randint(0,200000000000))
for j in range(0,100000000000):
    r = 100000000000
    if ((środekx - pktx[j])**2 + (środeky - pkty[j])**2)**(1/2) <= r:
        w_okręgu = w_okręgu + 1
        wszystkie = wszystkie + 1
    else:
        poza_okręgiem = poza_okręgiem + 1
        wszystkie = wszystkie + 1

pi = 4*(w_okręgu/wszystkie)
czas_pi2 = time.time()
print(pi)
czaspi = czas_pi2 - czas_pi1
print(czaspi)
