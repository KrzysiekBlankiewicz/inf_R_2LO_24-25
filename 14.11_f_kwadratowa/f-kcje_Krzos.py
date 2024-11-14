
# wypełnij treścią fragmenty oznaczone #TODO# aby program wypisywał poprawne postaci wzoru funkcji kwadratowej
# dla ułatwienia możesz założyć, że współczynniki będą liczbami naturalnymi mniejszymi od 10

def wartosc_funkcji(a, b, c, x):
	wartosc = (a*(x**2))+(b*x)+c
	return wartosc

def delta(a, b, c):
	d = (b**2) - (4*a*c)
	return d
    
def msc_zerowe(a,b,c):
	d = delta(a,b,c)
	if d == 0:
		x1 = (-b)/(2*a)
		return(x1)
	if d > 0:
		x1 = ((-b)-(d**(1/2)))/(2*a)
		x2 = ((-b)+(d**(1/2)))/(2*a)
		return (x1, x2)
	if d < 0:
		print("nie ma miejsc zerowych")

def kanon(a,b,c):
	a = a
	p = (-b)/(2*a)
	q = (-b)/(2*a)
	return (a, p, q)

def ilocz(a, b, c):
	a = a
	x1 = msc_zerowe(a, b, c)[0]
	x2 = msc_zerowe(a, b,c)[1]
	if x1 >=0:
		znak1 = ("-")
	if x1 < 0:
		znak1 =("+")
		x11 = -x1
	if x2 >=0:
		znak2 = ("-")
	if x2 < 0:
		znak2 =("+")
		x22 = -x2
	print(str(a) + "(x " + znak1 + " " + str(x11) + ")(x " + znak2 + " " + str(x22) + ")")
	return (a, x1, x2)

# dane od użytkownika
print("Podaj wzór funkcji kwadratowej w formacie \"f(x) = ax^2 + bx + c\"")
funkcja = input()

print("Podaj argument do wyznaczenia wartości funkcji:")
x = input()

# parametr przy x^2
p1 = int(funkcja[7])

# parametr przy x
p2 = int(funkcja[14])

# wyraz wolny
p3 = int(funkcja[19])


ilocz(p1, p2, p3)