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
        for i in range(2,x-1):
           if (x % i) == 0:
               x_podzielny = True
              #print("x: jest podzielny")
              # print(x)
               break
    if y > 1:
        for i in range(2,y-1):
           if (y % i) == 0:
               y_podzielny = True
               #print("y: jest podzielny")
               #print(y)
               break
               
    if x_podzielny == True or y_podzielny == True:
        return "nie"
    else:
        return "tak"

pierwsze = []
for i in range(0, len(współrzędne)):
    pierwszość = czy_współrzędna_z_pierwszych(współrzędne[i][0], współrzędne[i][1])
    if pierwszość == "tak":
        pierwsze.append(współrzędne[i])
print("pary z liczb pierwszych")
print(pierwsze)
print("ilość par z liczb pierwszych")
print(len(pierwsze))

#ZADANIE 4.2
print("ZADANIE 4.2 ----------------------------------")
def cyfropodobne(x, y):
    czy_cyfropodobne = False
    a = int(len(str(x)))
    b = int(len(str(y)))
    #print ("a "+ str(a))
    #print ("b "+ str(b))
    
    for i in range (0, a):
        czy_cyfropodobne = False
        for j in range (0, b):
            #print ("porownuje"+ str(x)[i] + " z " +str(y)[j])
            if int(str(x)[i]) == int(str(y)[j]):
                czy_cyfropodobne = True
                #print ("ta sama,przechodze do nastepnej")
                break
        if czy_cyfropodobne == False:                    
            return False

    for i in range (0, b):
        czy_cyfropodobne = False
        for j in range (0, a):
            #print ("porownuje"+ str(x)[i] + " z " +str(y)[j])
            if int(str(y)[i]) == int(str(x)[j]):
                czy_cyfropodobne = True
                #print ("ta sama,przechodze do nastepnej")
                break
        if czy_cyfropodobne == False:
            return False
        
    return True
    
cyfropodobność = []
for j in range (0, len(współrzędne)):
    czy_cyfropodobne = cyfropodobne(współrzędne[j][0], współrzędne[j][1])
    #print(str(współrzędne[j][0])+" "+str(współrzędne[j][1])+" "+str(czy_cyfropodobne))
    
    if czy_cyfropodobne == True:
        #print(str(współrzędne[j][0])+" "+str(współrzędne[j][1])+" "+str(czy_cyfropodobne))
        cyfropodobność.append(współrzędne[j])
print("koniec")
print(len(cyfropodobność))

#zadanie 4.3
print("ZADANIE 4.3------------------------------------")
def odległość(x):
    naj = 0
    licznik = 0
    for n in range(0,len(x)-1):
        xa = x[n][0]
        ya = x[n][1]
        for m in range(n+1,len(x)-1):
            xb = x[m][0]
            yb = x[m][1]
            odległość = (((xb - xa )**2)+((yb - ya)**2))**(1/2)
            licznik = licznik + 1
            #if licznik % 10000 ==0:
                #print(str(licznik) +" ") 
            if naj < odległość:
                naj = odległość
                #print("nowa odległość " + str(naj))
    return naj
największa = odległość(współrzędne)
print(największa)
print(round(największa))

#zadanie 4.4
print("ZADANIE 4.4 ------------------------------------------------------")
def wewnątrz(x):
    w = []
    ilosc=0
    for n in range(0,len(x)):
        #print ("pozycja: "+ str(x[n][0])+" , "+ str(x[n][1]))
        if -5000 < x[n][1] < 5000 and -5000 < x[n][0] < 5000:
            w.append(x[n])
            ilosc=ilosc+1
            #print ("jest w srodku")
    print ("ilosc w srodku: "  +str(ilosc))      
    return w

def bok(x):
    w = []
    ilosc=0
    for n in range(0,len(x)):
        if (x[n][1] == 5000 and -5000 <= x[n][0] <= 5000) or ( x[n][0] == 5000 and -5000 <= x[n][1] <= 5000) or (x[n][1] == -5000 and -5000 <= x[n][0] <= 5000) or (x[n][0] == -5000 and -5000 <= x[n][1] <= 5000):
            w.append(x[n])
            ilosc=ilosc+1
    print ("ilosc na linii: "  +str(ilosc))  
    return w

def poza(x):
    w = []
    ilosc=0
    print ("wielkosc wierszy: "+str(len(x)))
    for n in range(0,len(x)):
        print ("jaka jest wartosc n: "+ str(n))
        if (x[n][1] > 5000 or x[n][1] < -5000 or x[n][1] < -5000 or x[n][0] > 5000):
            w.append(x[n])
            ilosc=ilosc+1
    print ("ilosc na zewnatrz: "  +str(ilosc)) 
    return w

wewnątrz1 = wewnątrz(współrzędne)
bok = bok(współrzędne)
poza = poza(współrzędne)

ilośćw = len(wewnątrz1)
print("wewnątrz  - " + str(ilośćw))#" + str(wewnątrz1) + "
ilośćb = len(bok)
print("bok " + str(bok) + " - " + str(ilośćb))
ilośćp = len(poza)
print("poza " + str(ilośćp))#" + str(poza) + " - 
print ("suma: "+ str(ilośćw+ilośćb+ilośćp))
print ("wartosc len : "+ str(len(współrzędne)))
print ("przedostatni wiersz "+str(współrzędne[999]))
#print ("ostatni wiersz "+str(współrzędne[1000]))
    
        
    
    

        
        
