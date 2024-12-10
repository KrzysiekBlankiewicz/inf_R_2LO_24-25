import math

file = open("punkty.txt")
r = file.read()
a = r.split()
b = []
for i in a:
    b.append(int(i))
c = []
for j in range(0, len(b), 2):
    para = [b[j], b[j+1]]
    c.append(para)
dis = 0 
for i in range(0, len(c)):
    for j in range(i+1, len(c)-1):
        xA = c[i][0]
        yA = c[i][1]
        xB = c[j][0]
        yB = c[j][1]
        ndis = math.sqrt((xB - xA)**2 + (yB - yA)**2)
        if ndis < 0:
            ndis = ndis * -1
        if ndis > dis:
            dis = ndis
            lxA = xA
            lyA = yA
            lxB = xB
            lyB = yB 
print(round(dis))
print(lxA, lyA)
print(lxB, lyB) 

