# -*- coding: cp1250 -*-
#f = open("dane.txt")
#r = f.read()
#a = r.split()
#b =[]
#for i in a:
#    b.append(int(i))
#c = []
#for j in range(0, len(a), 2):
#    para = [b[j], b[j+1]]
#    suma = b[j] + b[j+1]
#    c.append(suma)
#sr = 0   
#for i in c:
#   sr = sr + i
#print(sr/len(c))   
#print(c)
#suma = 552, srednia sum = 46
import math
f = open("punkty.txt")
r = f.read()
a = r.split()
b =[int(i) for i in a]
for i in a:
    b.append(int(i))
c = []
for j in range(0, len(a), 2):
    para = b[j], b[j+1]
    c.append(para)
#Zad 4.1
def pier(x):
    if x>1:
        for i in range(2, x//2):
            if(x%i)==0:
                return 0
                break
        return 1
    else:
        return 0
lpp = 0
for i in c:
    if pier(i[0])==1 and pier(i[1])==1:
        lpp = lpp + 1
#Zad 4.3
def najodl(c):
    odl = 0
    for i in c:
        if abs(i[0] - i[1]) > odl:
            odl = abs(i[0] - i[1])
    return odl
#zad 4.4
def kwadrat(c):
    wewkw = 0
    nalin = 0
    pozkw = 0
    for i in c:
        if (5000 > i[0] > -5000) and (5000 > i[1] > -5000):
            wewkw += 1
        if ((i[0] == 5000 or i[0] == -5000) and 5000 >= i[1] >= -5000) or ((i[1] == 5000 or i[1] == -5000) and 5000 >= i[0] >= -5000):
            nalin += 1
        if (5000 < i[0] or i[0] < -5000) or (5000 < i[1] or i[1] < -5000):
            pozkw += 1
    print(wewkw,nalin,pozkw)
kwadrat(c)
    































