import math

def ww(p1, p2, p3, x):
    wartosc = p1 * x * x + p2 * x + p3
    return wartosc

def delta(p1, p2, p3):
    d = p2 * p2 - 4 * p1 * p3
    return d

def msc_zerowe(p1, p2, d):
    if d >= 0:
        x1 = (-p2 - math.sqrt(d)) / (2 * p1)
        x2 = (-p2 + math.sqrt(d)) / (2 * p1)
        return x1, x2
    else:
        return None

def ilocz(x, p1, x1, x2):
    fi = "f(x) = {p1} * (x - {x1}) * (x - {x2})"
    return fi

def kanon(p1, p2, p3):
    p = -p2 / (2 * p1)
    q = ww(p1, p2, p3, p)
    k = "f(x) = {p1} * (x - {p})^2 + {q}"
    return k

print("Podaj wzór funkcji kwadratowej w formacie \"f(x) = ax^2 + bx + c\":")
funkcja = input()

p1 = int(funkcja[7])
p2 = int(funkcja[14])
p3 = int(funkcja[19])

print("Podaj argument do wyznaczenia wartości funkcji:")
x = float(input())

wartosc_funkcji = ww(p1, p2, p3, x)
d = delta(p1, p2, p3)
miejsca_zerowe = msc_zerowe(p1, p2, d)
kanoniczna_postac = kanon(p1, p2, p3)

print("Wartość funkcji dla x = {x}: {wartosc_funkcji}")
if miejsca_zerowe:
    x1, x2 = miejsca_zerowe
    print("Miejsca zerowe: x1 = {x1}, x2 = {x2}")
    print(ilocz(x, p1, x1, x2))
else:
    print("Brak miejsc zerowych")

print(ilocz)



 #Ważny komentarz: ten program nie działa i kiedyś będzie dokończony, ale aktualnie jedyne o czym myślę to żeby się położyć, a lecę zaraz na sprawdzian z geografii. Z pozdrowieniami :)
 #15:16 14.11.2024
