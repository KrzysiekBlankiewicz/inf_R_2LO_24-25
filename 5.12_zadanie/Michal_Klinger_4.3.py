import math

def wczytaj_punkty():
    punkty = []
    with open("punkty.txt", 'r') as plik:
        for linia in plik:
            x, y = map(int, linia.strip().split())
            punkty.append((x, y))
    return punkty

def oblicz_odleglosc(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def znajdz_najbardziej_oddalone_punkty(punkty):
    max_odleglosc = 0
    punkt1 = punkt2 = None

    for i in range(len(punkty)):
        for j in range(i + 1, len(punkty)):
            odleglosc = oblicz_odleglosc(punkty[i], punkty[j])
            if odleglosc > max_odleglosc:
                max_odleglosc = odleglosc
                punkt1, punkt2 = punkty[i], punkty[j]

    return punkt1, punkt2, round(max_odleglosc)

punkty = wczytaj_punkty()

punkt1, punkt2, max_odleglosc = znajdz_najbardziej_oddalone_punkty(punkty)

print(punkt1, punkt2)
print(max_odleglosc)
