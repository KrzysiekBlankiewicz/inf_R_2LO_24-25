#Funkcja sprawdzająca czy punkty są jakoś związane z kwadratem
def punktywkw(x, y):
    if min_x < x < max_x and min_y < y < max_y:
        return "srodek"  # Wewnątrz kwadratu (bez boków)
    elif (x == min_x or x == max_x) and min_y <= y <= max_y or (y == min_y or y == max_y) and min_x <= x <= max_x:
        return "krawedz"  # Punkt na boku kwadratu
    else:
        return "poza"  # Punkt na zewnątrz kwadratu

k = 10000
#Krawędź kradratu K
min_x= -k//2
min_y= -k // 2
max_x= k//2
max_y= k//2
#Liczniki dla punktów
srodekkw = 0
krawedzkw = 0
pozakw = 0

#Skrypt który coś faktycznie robi ;)
file = open("punkty.txt")
for u in file:
        # Wyczytanie z linijki współrzędnych z dokumentu punkty.txt
        liczby = list(map(int, u.split()))
        for i in range(0, len(liczby), 2):
            if i + 1 < len(liczby):  # Sprawdzenie czy faktycznie jest to para (x, y)
                x = liczby[i]
                y = liczby[i + 1]
                kat = punktywkw(x, y)
                # Kategoryzuje punkty i dodaje 1 do liczników za każdym razem kiedy liczba pasuje do danego podpunktu( czyli czy jest w, na, czy poza kwadratem)
                if kat == "srodek":
                    srodekkw += 1
                elif kat == "krawedz":
                    krawedzkw += 1
                elif kat == "poza":
                    pozakw += 1
                else:
                    print("Błąd dla punktu:", x, y) #Sprawdzenie czy niema żadnego błędu.

#Wyniki :)
print("---WYNIKI---")
print("Liczba punktów w kwadracie K:")
print(srodekkw)
print("Liczba punktów na bokach kwadratu K:")
print(krawedzkw)
print("Liczba punktów poza kwadrat K:")
print(pozakw)
# P.S. Przepraszam za tyle hasztagów ale łatwiej mi było opisać kod wtedy kiedy pisałem go.
