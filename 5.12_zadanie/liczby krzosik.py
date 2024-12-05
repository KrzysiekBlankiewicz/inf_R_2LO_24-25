#ZADANIA Z LEKCJI

print("<><><><><><><><><>ZADANIA Z LEKCJI<><><><><><><><><>")

file = open("dane.txt")

r = file.read()

#WYŚWIETLANIE LICZB JAKO NAPIS

print("plik jako jeden napis:")
print(r)

#WYŚWIETLANIE PLIKU PODZIELONEGO NA ELEMENTY

a = r.split()

print("plik podzielony na elementy")
print (a)

#WYPISYWANIE LICZB JAK W PLIKU

b = []
for i in a:
    b.append(int(i))

print("liczby z pliku")
print(b)

#LICZENIE SUMY WSZYSTKICH LICZB

suma = 0
for k in range(0, len(a)):
    suma = suma + b[k]
print("suma liczb")
print(suma)

#WYPISYWANIE LICZB W PARACH

c = []
for j in range (0, len(a), 2):
    para = [b[j], b[j+1]]
    c.append(para)

print("liczby w parach")
print(c)

#LICZENIE SUM W PARACH LICZB

sum_par = []
for j in range(0, len(c)):
    pary_sum = c[j][0] + c[j][1]
    sum_par.append(pary_sum)

print("wypisywanie sum par")
print(sum_par)

#LICZENIE ŚREDNIEJ Z SUM PAR

śr_sum = 0
for j in range (0, len(sum_par)):
    śr_sum = śr_sum + sum_par[j]
śr_sum = śr_sum/len(sum_par)

print("wypisanie średniej z sum par")
print(śr_sum)


#ZADANIA MATURALNE

print("<><><><><><><><><><><><>ZADANIA MATURALNE<><><><><><><><><><><><><><><>")

#ZADANIE 4
file1 = open("punkty.txt")

#WYPISANIE PUNKTÓW

print("punkty w zadaniu są następujące")
punkciki = file1.read()
print(punkciki)

#PODZIAŁ PLIKU

pkt_podz = punkciki.split()
print("podzielony na elementy;")
print(pkt_podz)

#LICZBY Z INT

e = []
for i in pkt_podz:
    e.append(int(i))

print("z-intowane")
print(e)


#ZROBIENIE WSPÓŁRZĘDNYCH

współrzędne = []
for j in range (0, len(e), 2):
    współ = [e[j], e[j+1]]
    współrzędne.append(współ)

print("liczby w parach")
print(współrzędne)

#pary z liczb pierwszych

def czy_współrzędna_z_pierwszych(x,y):
    x_podzielny = False
    y_podzielny = False
    if x <= 1:
        return false
    if y <= 1:
        return false
    if x > 1:
        for i in range(2,x):
           if (x % i) == 0:
               x_podzielny = True
    if y > 1:
        for i in range(2,y):
           if (y % i) == 0:
               y_podzielny = True
    if x_podzielny == True and y_podzielny == True:
        return "tak"

pierwsze = []
for i in range(0, len(współrzędne)):
    pierwszość = czy_współrzędna_z_pierwszych(współrzędne[i][0], współrzędne[i][1])
    if pierwszość == "tak":
        pierwsze.append(współrzędne[i])
    else:
        break
print("pary z liczb pierwszych")
print(pierwsze)
    
