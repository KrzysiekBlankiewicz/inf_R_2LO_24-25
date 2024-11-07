def nwd(a, b):
	licznik = 0
	dzielnik = 1
	limit = min(a, b)
	for i in range(1, limit + 1):
		licznik = licznik + 1
		if a % i == 0 and b % i == 0:
			dzielnik = i
	return (dzielnik, licznik)

def euk(a, b):
	licznik = 0
	c = 0
	a, b = min(a, b), max(a, b)
	while b != 0:
		c = a%b
		a = b
		b = c
		licznik = licznik + 1
		if b == 0:
			return (a, licznik)

a = int(input("Podaj liczbe: "))
b = int(input("Podaj liczbe: "))

x = nwd(a, b)
print(x)

y = euk(a, b)
print(y)