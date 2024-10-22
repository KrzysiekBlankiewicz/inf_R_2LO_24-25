# ZADANIE 1 – przypomnienie czym jest pętla:
# Napisz program, który dla każdej liczby od 1 do 30 obliczy i wyświetli jej sześcian.


# --------------------------
# wykonanie pętli można przerwać instrukcją break

#def przerywana_petla(stop):
#  for i in range(0, 100):
#    print(i)
#    if i == stop:
#      break

#meta = int( input() )
#if meta < 100 and meta > 0:
#  przerywana_petla(meta)

# co wyświetli powyższy program, jeżeli poda mu się liczbę 23 z klawiatury?
# --------------------------

# ZADANIE 2 – przerywanie pętli:
# Napisz program, który 
# 1.	przyjmie od użytkownika liczbę naturalną mniejszą od 20 i zapiszę ją w zmiennej x
# 2.	z wykorzystaniem pętli będzie podwajał wartość zmiennej x aż jej wartość przekroczy 100000
# 3.	wypisze ile razy zwiększał x, czyli ile razy wykonała się pętla

def zad2(x):
	stop = 0
	for i in range(0, 20):
		x = x*2
		print(x)
		stop += 1
		if x > 10000:
			print(f"Program powtórzył się {stop} razy")
			break
	

x = int(input())
if x>0 and x<20:
	zad2(x)







# ZADANIE 3 - praca domowa:
# Napisz program, który 
# 1. przyjmie od użytkownika liczbę naturalną n
# 2. bez użycia funkcji sqrt() znajdzie pierwiastek kwadratowy z n
# 3. wypisze ile jest równy wyzej wymieniony pierwiastek

def zad3(x):
	x = 0
	for i in range(1, stop):
		n = x*x
		if n == stop:
			print(x)
			break
		x += 1

zad3(x)
	



