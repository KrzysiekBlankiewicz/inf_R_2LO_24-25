import math
def wartosc_funkcji(a, b, c, x):
	y = a*x**2+b*x+c
	return y

def delta(a, b, c):
	d = b**2-4*a*c
	return d
    
def msc_zerowe(a, b, d):
	x1 = (-b-math.sqrt(d))/2*a
	x2 = (-b+math.sqrt(d))/2*a
	return (x1, x2)

def kanon(a, b, d):
	p = -b/2*a
	q = -d/4*a
	return (p, q)

# dane od użytkownika
print("Podaj wzór funkcji kwadratowej w formacie \"f(x) = ax^2 + bx + c\"")
funkcja = input()

print("Podaj argument do wyznaczenia wartości funkcji:")
x = int(input())




print("-------------------------------------")

# parametr przy x^2
p1 = int(funkcja[7])
print(p1)

# parametr przy x
p2 = int(funkcja[14])
print(p2)

# wyraz wolny
p3 = int(funkcja[19])
print(p3)

e = delta(p1, p2, p3)

print("-------------------------------------")

zerowe = msc_zerowe(p1, p2, e)
a = str(p1)
x1 = str(zerowe[0])
x2 = str(zerowe[1])
print('f(x) = '+a+'(x-'+x1+')(x-'+x2+')')

print("-------------------------------------")

a = str(p1)
p = str(kanon(p1, p2, e)[0])
q = str(kanon(p1, p2, e)[1])
z = kanon(p1, p2, e)[0]
if q == '0.0':
	if z < 0:
		 print('f(x) = '+a+'(x'+p+')^2')
	else:
		print('f(x) = '+a+'(x-'+p+')^2')
else:
	print('f(x) = '+a+'(x-'+p+')^2+'+q)
