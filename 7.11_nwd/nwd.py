def nwd(a, b):
    licznik = 0
    limit = min(a, b)
    if a < b:
       limit = a
    else: 
        limit = b
    max_dzielnik = 1
    for i in range(1,limit+1):
        if a % i == 0 and b % i == 0:
            max_dzielnik = i
        licznik = licznik + 1
    return [max_dzielnik, licznik]

x = int(input())
y = int(input())

wynik = nwd(x, y)
print(wynik)

























