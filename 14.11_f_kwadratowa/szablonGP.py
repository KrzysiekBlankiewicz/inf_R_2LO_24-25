import math

def wartosc_wielom(params, x):
    # Obliczenie wartości funkcji kwadratowej dla danego x
    a, b, c = params
    wartosc = a * x**2 + b * x + c
    return wartosc

def delta(params):
    # Obliczenie delty funkcji kwadratowej
    a, b, c = params
    d = b**2 - 4 * a * c
    return d

def msc_zerowe(params):
    # Obliczenie miejsc zerowych funkcji kwadratowej
    a, b, c = params
    d = delta(params)
    if d < 0:
        return None  # Brak miejsc zerowych w liczbach rzeczywistych
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return (x1, x2)

def ilocz(params):
    # Zwraca współczynniki a oraz miejsca zerowe jako p i q w postaci iloczynowej
    a, b, c = params
    x1, x2 = msc_zerowe(params)
    if x1 is None:
        return None  # Brak postaci iloczynowej
    return (a, x1, x2)

def kanon(params):
    # Zwraca współczynniki a, h i k w postaci kanonicznej
    a, b, c = params
    h = -b / (2 * a)
    k = c - a * h**2
    return (a, h, k)

# dane od użytkownika
print("Podaj wzór funkcji kwadratowej w formacie \"f(x) = ax^2 + bx + c\"")
funkcja = input()

print("Podaj argument do wyznaczenia wartości funkcji:")
x = int(input())

# Wyciągnięcie współczynników z funkcji w postaci ax^2 + bx + c
p1 = int(funkcja.split('x^2')[0].split('=')[1].strip())
p2 = int(funkcja.split('x^2')[1].split('x')[0].strip())
p3 = int(funkcja.split('x^2')[1].split('x')[1].strip())

params = (p1, p2, p3)

# Obliczenie wartości funkcji dla podanego x
wartosc = wartosc_wielom(params, x)
print(f"Wartość funkcji f({x}) wynosi: {wartosc}")

# Wypisz użytkownikowi wzór funkcji kwadratowej w postaci iloczynowej
postac_iloczynowa = ilocz(params)
if postac_iloczynowa is not None:
    a = postac_iloczynowa[0]
    p = postac_iloczynowa[1]
    q = postac_iloczynowa[2]
    print(f"Postać iloczynowa funkcji: f(x) = {a}(x - {p})(x - {q})")
else:
    print("Brak postaci iloczynowej (brak miejsc zerowych w liczbach rzeczywistych).")

# Wypisz użytkownikowi wzór funkcji kwadratowej w postaci kanonicznej
postac_kanoniczna = kanon(params)
a = postac_kanoniczna[0]
h = postac_kanoniczna[1]
k = postac_kanoniczna[2]
print(f"Postać kanoniczna funkcji: f(x) = {a}(x - {h})^2 + {k}")
