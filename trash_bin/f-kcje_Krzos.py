
# wypełnij treścią fragmenty oznaczone #TODO# aby program wypisywał poprawne postaci wzoru funkcji kwadratowej
# dla ułatwienia możesz założyć, że współczynniki będą liczbami naturalnymi mniejszymi od 10

def wartosc_funkcji(a, b, c, x):
	wartosc = (a*(x**2))+(b*x)+c
	print( "funkcja f(" + str(x) + ") wynosi" + str(wartosc))
	return wartosc

def delta(a, b, c):
	d = (b**2) - (4*a*c)
	return d
    
def msc_zerowe(a,b,c):
	d = delta(a,b,c)
	if d == 0:
		x1 = (-b)/(2*a)
		x2 = x1
		zerowe = 1
		print("miejsca zerowe to: " + str(x1) + " i " + str(x2))
		return(x1, x2, zerowe, 1)  # Zwróć liczbę miejsc zerowych
	if d > 0:
		x1 = ((-b)-(d**(1/2)))/(2*a)
		x2 = ((-b)+(d**(1/2)))/(2*a)
		zerowe = 1
		print("miejsca zerowe to: " + str(x1) + " i " + str(x2))
		return (x1, x2, zerowe, 1)  # Zwróć liczbę miejsc zerowych
	if d < 0:
		print("nie ma miejsc zerowych")
		x1 = 1
		x2 = 1
		zerowe = 0
		return (x1, x2, zerowe, 0)  # Zwróć liczbę miejsc zerowych

def kanon(a,b,c):
	d = delta(a,b,c)
	a = a
	p = (-b)/(2*a)
	q = (-d)/(4*a)
	print("wzór funkcji kanonicznej to: f(x) = " + str(a) + "(x - " + str(p) + " ) + " + str(q) + ")")
	return (a, p, q)

def ilocz(a, b, c, zerowe):
	if zerowe == 1:
		a = a
		x1 = msc_zerowe(a, b, c)[0]  # Pobierz x1 z funkcji msc_zerowe
		x2 = msc_zerowe(a, b, c)[1]  # Pobierz x2 z funkcji msc_zerowe
		if x1 >= 0:
			znak1 = ("-")
		if x1 < 0:
			znak1 =("+")
			x11 = -x1
		if x2 >= 0:
			znak2 = ("-")
		if x2 < 0:
			znak2 =("+")
			x22 = -x2
		print("wzór funkcji iloczynowej to f(x) = " + str(a) + "(x " + znak1 + " " + str(x11) + ")(x " + znak2 + " " + str(x22) + ")")
		return (a, x1, x2)
	else:
		print("nie można wyznaczyć funkcji iloczynowej, ponieważ nie ma miejsc zerowych")

# dane od użytkownika

print("Podaj wzór funkcji kwadratowej w formacie \"f(x) = ax^2 + bx + c\"")
funkcja = input()

print("Podaj argument do wyznaczenia wartości funkcji:")
x = int(input())

# parametr przy x^2
p1 = int(funkcja[7])

# parametr przy x
p2 = int(funkcja[14])

# wyraz wolny
p3 = int(funkcja[19])

# Wywołanie funkcji msc_zerowe() i pobranie liczby miejsc zerowych
wynik = msc_zerowe(p1, p2, p3)
zerowe = wynik[3]

ilocz(p1, p2, p3, zerowe)
kanon(p1, p2, p3)
wartosc_funkcji(p1, p2, p3, x)
