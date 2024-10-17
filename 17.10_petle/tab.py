import random

def z1(x):
	for i in range(0, x, 1):
		print(i)

def z2(x):
	odp = 0
	for i in range(1, x+1, 1):
		odp = odp + i
	print(odp)

def z3(x):
	for i in range(x, x*11, x):
		print(i)

	
def z4(x):
	tab = [0]
	for i in range(10):
		tab.append(random.randint(1,100))
	for i in range(0, 10, 1):
		if n < tab[i]:
			print(tab[i])

def z5(x):
	for i in range(-x, 0, 1):
		print(i)

def z6(x):
	a = 0
	b = 1
	for i in range(x):
		print(a+b)
		b = a+b
		a = b - a

#POWINNO dzialac ale nie chce
	

n = int(input("Podaj liczbę "))
z6(n)

