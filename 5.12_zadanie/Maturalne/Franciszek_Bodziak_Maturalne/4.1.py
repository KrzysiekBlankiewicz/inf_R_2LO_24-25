file = open("punkty.txt")
r = file.read()

a = r.split()
b = [int(i) for i in a]
prime = []

def pier(x):
    if x < 2:
        return False
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            return False
    return True

ilprime = 0

for j in range(0, len(b), 2):
    if pier(b[j]) and pier(b[j+1]):
        prime.append((b[j], b[j+1]))
        ilprime = ilprime + 1


print (ilprime)
