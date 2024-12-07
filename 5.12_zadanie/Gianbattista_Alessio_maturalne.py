import math
file = open("punkty.txt")
r = file.read()

a = r.split()

b = [int(i) for i in a]  

c = []

def check(x):
    if x < 2:
        return False
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            return False
    return True
odp = 0
for j in range(0, len(b), 2):
    if check(b[j]) and check(b[j+1]):
        c.append((b[j], b[j+1]))
        odp = odp + 1
print(c)
print(odp)
