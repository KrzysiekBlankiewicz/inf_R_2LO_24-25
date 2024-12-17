def fun(a, b, c, x):
    return a*(x**2)+(b*x)+c

def msc_z(a, b, c, p, k, e):
    sr = (p + k)/2
    d = (b**2)-4*a*c
    if d < 0:
        return "Brak miejsc zerowych"

    while abs(fn(a, b, c, sr)) > e:
        if fn(a,b,c,sr) > 0:
            k = sr
        if fun(a, b, c, sr) < 0:
            p = sr
        sr = (p + k)/2
    return sr

def fibonaci(x):
    if x == 0 or x == 1:
        return 1
    return fibonaci(x-1) + fibonaci(x-2)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
p = int(input("p = "))
k = int(input("k = "))


print(msc_z(a, b, c, p, k, 0.01))
print("------------------------------------")
x = int(input("podaj x do fibonaciego "))
print(fibonaci(x))