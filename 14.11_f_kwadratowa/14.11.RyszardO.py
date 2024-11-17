import math

def wartosc_funkcji(params, x):
    wartosc = (params[0]*x**2) + (params[1]*x) + params[2]
    return wartosc

def delta(params):
    a = params[0]
    b = params[1]
    c = params[2]
    d = b**2 - 4*(a*c)
    return d
def msc_zerowe(params):
    d = delta(params)
    if d == 0:
        x1 = -(params[1])/(2*(params[0]))
    if d<0:
        x1 = -1*(params[1]) - math.sqrt(delta(params))/(2*(params[0]))
        x2 = -1*(params[1]) + math.sqrt(delta(params))/(2*(params[0]))
    if d > 0:
        print ("ERROR 404")
    return (x1, x2)

def ilocz(params):
    x1 = msc_zerowe(p) [0]
    x2 = msc_zerowe(p) [1]
    a = params[0]
    if delta(params) > 0:
        print("ERROR 420")
    if delta(params) == 0:
        warIlo = a*(x - x1)**2 
    if detla(params) < 0:
        warIlo = a*(x - x1)*(x-x2)   
    return (a, x1, x2)

def kanon(params):
    a = params[0]
    b = params[1]
    c = params[2]
    p = (-b)/(2*a)
    q = (-(b**2 - 4*a*c))/4*a
    print((a(x-p)**2)+q)
    return (a, p, q)

print("---Dane od użytkownika---")
print("Podaj wzór funkcji kwadratowej w formacie \"f(x) = ax^2 + bx + c\"")
funkcja = input()
print("Podaj argument do wyznaczenia wartości funkcji:")
x = int(input())
print("---------------------")
print("---Parametry---") 
# parametr przy x^2
p1 = int(funkcja[7])
print(p1)
# parametr przy x
p2 = int(funkcja[14])
print(p1)
# wyraz wolny
p3 = int(funkcja[19])
print(p3)
p = [p1,p2,p3]
print("---------------------")
print("---FUNKCJE---")
print(wartosc_funkcji(p,x))
print(delta(p))
print(msc_zerowe(p))
print(ilocz(p))
print(kanon(p))
