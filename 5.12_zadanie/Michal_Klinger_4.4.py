def wczytaj_punkty():
    punkty = []
    with open("punkty.txt", 'r') as plik:
        for linia in plik:
            x, y = map(int, linia.strip().split())
            punkty.append((x, y))
    return punkty

def klasyfikuj_punkt(x, y):
    if -5000 < x < 5000 and -5000 < y < 5000:
        return "wewnątrz"
    elif (x == -5000 or x == 5000) and -5000 <= y <= 5000:
        return "na boku"
    elif (y == -5000 or y == 5000) and -5000 <= x <= 5000:
        return "na boku"
    else:
        return "na zewnątrz"

def klasyfikuj_punkty(punkty):
    wewnatrz = 0
    na_boku = 0
    na_zewnatrz = 0

    for x, y in punkty:
        kategoria = klasyfikuj_punkt(x, y)
        if kategoria == "wewnątrz":
            wewnatrz += 1
        elif kategoria == "na boku":
            na_boku += 1
        elif kategoria == "na zewnątrz":
            na_zewnatrz += 1

    return wewnatrz, na_boku, na_zewnatrz

punkty = wczytaj_punkty()

wewnatrz, na_boku, na_zewnatrz = klasyfikuj_punkty(punkty)

print(wewnatrz,",", na_boku,",", na_zewnatrz)


