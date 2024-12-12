# Funkcja
def fkcja(a,b,c,x):
    return a*(x**2)+(b*x)+c
# Miejsce Zerowe v1
def msc_zer_v1(a,b,c,p,k,e):
    srodek = (p+k)/2
    delta = (b**2) - 4*a*c
    if delta < 0 or p > k:
        return "Fajny dowcip"
    if fkcja(a,b,c,srodek) <= e and fkcja(a,b,c,srodek) >= e:
        return srodek
    while abs(fkcja(a,b,c,srodek)) > e:
        if fkcja(a,b,c,srodek) > 0:
            k = srodek
            srodek = (p+k)/2
        if fkcja(a,b,c,srodek) < 0:
            p = srodek
            srodek =(p+k)/2
    return srodek
# Miejsce Zerowe v2
def msc_zer_v2(a,b,c,p,k,e):
    srodek = (p+k)/2
    delta = (b**2) - 4*a*c
    if delta < 0 or p > k:
        return "Fajny dowcip"
    if fkcja(a,b,c,srodek) <= e and fkcja(a,b,c,srodek) >= e:
        return srodek
    if fkcja(a,b,c,srodek)* fkcja(a,b,c,p) < 0:
        return msc_zer_v2(a,b,c,p,srodek,e)
    else:
        return msc_zer_v2(a,b,c,srodek,k,e)
# Fibonnachi
def fib(n):
    if n==0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)
##
print("|Miejsce zerowe v1|")
print(msc_zer_v1(1 , 0 , -1 , 0 , 17, 0.01))
##
print("|Fibonnachi|")
print(fib(5))
##
print("|Miejsce zerowe v2|")
print(msc_zer_v1(1 , 4 , -1 , 0 , 17, 0.01))
