
def euklides(a, b):
    licznik = 0 
    while b != 0:
        r = a % b       
        a = b
        b = r 
        licznik = licznik + 1  
    return [a, licznik]

x = int(input())
y = int(input())

nwd = euklides(x, y)
print(nwd)


