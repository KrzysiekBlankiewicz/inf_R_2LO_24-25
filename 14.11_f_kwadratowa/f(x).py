import math

print("Podaj wzór funkcji kwadratowej w formacie \"f(x) = ax^2 + bx + c\"")
f = input()

print("Podaj argument do wyznaczenia wartości funkcji:")
x = int(input())


a = int(f[7])

b = int(f[14])

c = int(fa[19])

def wartosc_f(a, b, c):
    wartosc = a*x^2 + b*x + c
    return wartosc

def delta(a, b, c):
    d = b^2 - 4*a*c
    return d
    
def msc_zerowe(a, b, c):
	x1 = (-b - math.sqrt(d)) / (2*a)
	x2 = (-b + math.sqrt(d)) / (2*a)
	return (x1, x2)

def kanon(a, b, c):
    p = -b / (2*a)
    q = -d / (4*a)
    y = a*(x-p)^2 + q
    print(y)

def ilocz(a, b, c):
    x1 = 0
    x2 = 0
    y = a*(x - x1)*(x - x2)
    return (x1, x2)
    print(y)



postac_iloczynowa = ilocz(a, b, c)
a = postac_iloczynowa[0]
p = postac_iloczynowa[1]
q = postac_iloczynowa[2]
ilocz(a, b, c)
kanon(a, b, c)