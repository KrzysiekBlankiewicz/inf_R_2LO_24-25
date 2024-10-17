
def funkcja1(x):
	for i in range(0, x, 1):
		print(i)
		
def funkcja2(x):
    suma = 0
    for i in range(1, x+1, 1):
        suma = suma + i
        print(suma)
    return suma

def funkcja(x):
    w = 1
    for i in range(0,100000):
        w = (i+1)*x
        print(w)
    return w

print("podaj liczbę")
n = int(input())
wynik = funkcja(n)
print(wynik)
