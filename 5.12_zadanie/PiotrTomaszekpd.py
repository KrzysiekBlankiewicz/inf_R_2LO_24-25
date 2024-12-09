def punktywkw(x, y):
    if min_x < x < max_x and min_y < y < max_y:
        return "srodek"
    elif (x == min_x or x == max_x) and min_y <= y <= max_y or (y == min_y or y == max_y) and min_x <= x <= max_x:
        return "krawedz"
    else:
        return "poza"

k = 10000
min_x = -k // 2
min_y = -k // 2
max_x = k // 2
max_y = k // 2
srodekkw = 0
krawedzkw = 0
pozakw = 0

file = open("punkty.txt")
for u in file:
    liczby = list(map(int, u.split()))
    for i in range(0, len(liczby), 2):
        if i + 1 < len(liczby):
            x = liczby[i]
            y = liczby[i + 1]
            kat = punktywkw(x, y)
            if kat == "srodek":
                srodekkw += 1
            elif kat == "krawedz":
                krawedzkw += 1
            elif kat == "poza":
                pozakw += 1
            else:
                print("Błąd dla punktu:", x, y)

print("---WYNIKI---")
print("Liczba punktów w kwadracie K:", srodekkw)
print("Liczba punktów na bokach kwadratu K:", krawedzkw)
print("Liczba punktów poza kwadrat K:", pozakw)
