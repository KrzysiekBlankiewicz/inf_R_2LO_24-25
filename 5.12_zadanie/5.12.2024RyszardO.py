#f = open("dane.txt")
#r = f.read()
#a = r.split()
#b = []
#for i in a:
#    b.append(int(i))
#print(b)
#print("-----------------")
#c = []
#for j in range(0,len(a),2):
#    para = b[j], b[j+1]
#    c.append(para)
#print(c)
#print("-----------------")
#suma=0
#for i in b:
#   suma = suma+i
#print("suma:")
#print(suma)
#print("-----------------")
#print("Œrednia par:")
#print(suma/len(c))
print("ZADANIA MATURALNE")
import math
file = open("punkty.txt")
read = file.read()
a = read.split()
b = []
for i in a:
    b.append(int(i))
c = []
for j in range(0,len(a),2):
    para = b[j], b[j+1]
    c.append(para)
#print(c)
wsplpp = []
def sprlp(x): 
    if x>1:
        for i in range(0, x/2, 2):
            if(x%i)==0:
                return True
            else:
                return False
    else:
        return False
licznik = 0
for j in c:
    if sprlp(b[j]) and sprlp(b[j+1]):
        licznik = licznik +1
        wsplpp.append(b[j],b[j+1])
print(licznik)  
    
