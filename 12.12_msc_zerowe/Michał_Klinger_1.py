def funkcja(a, b, c, x):
    return a * x**2 + b * x + c

def miejsce_zerowe(a, b, c, p, k, e):
    srodek = (p + k) / 2

    delta = b**2 - 4 * a * c
    if delta < 0:
        return "funkcja nie ma miejsc zerowych"

    while abs(funkcja(a, b, c, srodek)) >= e:
        if funkcja(a, b, c, srodek) > 0:
            k = srodek
        else:
            p = srodek
        srodek = (p + k) / 2

    return srodek

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
p = int(input("p = "))
k = int(input("k = "))
e = float(input("e = "))


print(miejsce_zerowe(a, b, c, p, k, e))


print("________________________________________________________")


def fib(n):
    if n == 0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))