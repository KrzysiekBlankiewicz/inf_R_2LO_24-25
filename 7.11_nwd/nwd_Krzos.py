
print("<><><>---------------------------<<Wyliczanie NWD Jan Krzos 7.11.2024 r.>>----------------------------<><><>")
def  nwd (a,b):
	licznik = 0
	c = 1
	limit = min(a,b)
	if a < b :
		limit = a
	else:
		limit = b
	for i in range(1, limit+1):
		if (a % i == 0) and (b % i ==0):
			c = i
		licznik = licznik + 1
	print(c)
	print(licznik)
	return c

print("podaj liczby")
a = int(input())
b = int(input())
nwd(a,b)
print("<><>_-_-_-_-_<ALGORYTM EUKLIDESA>_-_-_-_-_-_<><>")

def uklid(c,d):
	licznik = 0
	limit = min(c,d)
	if c>d:
		limit = c
	else:
		limit = d
	for x in range(0, limit):
		licznik = licznik + 1
		if c > d:
			c = c - d
		if d > c:
			d = d - c
		if c == d:
			return (c, licznik)


print("podaj znowu dwie liczby")
c = int(input())
d = int(input())
e = uklid(c,d)
print(e[0])
print(e[1])
			