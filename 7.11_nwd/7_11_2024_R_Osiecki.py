def nwd(a,b):
    licznik = 0
    limit = min(a,b)
    l_max = 1
    if a > b:
        limit = a
    else:
        limit = b
    for i in range(1 , limit):
        licznik = licznik + 1
        if (a%i == 0) and (b%i == 0):
            l_max = i
    return (l_max, licznik)



def alg_eukl(e,f):
    limit = min(e,f)
    licznik = 0
    if e > f:
        limit = e
    elif f > e:
        limit = f
    for y in range(0,limit):
        licznik = licznik +1 
        if e>f:
            e = e-f
        else:
            f = f-e
        if e == f:
            return ( e, licznik)
            
        


print("--- ZADANIE 1---")
print("Podaj 1 liczbe:")
n = int(input())
print("Podaj 2 liczbe:")
m = int(input())
print("NWD jest równe:")
t = nwd(n,m)
print(t)

print("--- ZADANIE 2---")
print("Podaj 1 liczbe:")
g = int(input())
print("Podaj 2 liczbe:")
h = int(input())
z = alg_eukl(g,h)
print(z)
