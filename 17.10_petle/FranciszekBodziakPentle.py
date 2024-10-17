import random


def zad1(n):
	for x in range(0,n,1):
		print(x)
	
def zad2(n):
	s = 0
	n=(n+1)
	for x in range(0,n,1):
		s =(s+x)
	return(s)

def zad3(n):
	w=1
	for x in range(0,10):
		print(n*w)
		w=(w+1)

def zad4(n):
	liczby = []
	for x in range(0,10):
		liczby.append(random.randint(0,100))

	for x in range(0,10):
		if (liczby[x] > n):
			print(liczby[x])

def zad5(n):
	for x in range (-n,0,1):
		print(x)
		
def zad6(n):
	f=0
	g=0
	for x in range (0,n,1):
		f=(f+g)
		g=(f+g)
		print(f)

print("Podaj liczbę: ")
n = int(input())
print("Podaj nr. zadania: ")
z = int(input())
print(" ")

if z==1:
	zad1(n)

if z==2:
	print(zad2(n))

if z==3:
	zad3(n)

if z==4:
	zad4(n)
if z==5:
	zad5(n)
if z==6:
	zad6(n)






