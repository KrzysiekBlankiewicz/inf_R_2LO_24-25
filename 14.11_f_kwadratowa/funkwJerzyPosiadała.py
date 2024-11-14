import math
def wartosc_fun(a,b,c,x):
    y = a*x**2 + b*x + c
    return y

def delta(a,b,c):
	d = b**2 - 4*a*c
	return d
    
def mzic(a,b,c):
	d = delta(a,b,c)
	if d < 0:
		return (a, "none", "none")
	else:
		x1 = (-b - math.sqrt(d))/2*a
		x2 = (-b + math.sqrt(d))/2*a
		a = a
		return (a,x1, x2)

def kan(a,b,c):
	d = delta(a,b,c)
	p = -b/2*a
	q = -d/4*a
	return (a, p, q)


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


# wypisz użytkownikowi wzór funkcji kwadratowej w postaci iloczynowej
#postac_iloczynowa = kan(p1, p2, p3)
poskan = kan(p1,p2,p3)
a = str(poskan[0])
p = str(poskan[1])
q = str(poskan[2])
print(a + '*(x+'+p+')**2 +'+q)
mzir = mzic(p1,p2,p3)
a = str(mzir[0])
if str(mzir[1]) == "none" or str(mzir[2]) == "none":
	print('nie ma postaci iloczynowej')
else:
	x1 = str(mzir[1])
	x2 = str(mzir[2])
	print(a + '(x+' + x1 + ')(x+' + x2 + ')')
