import random

x = 1
n = 0
liczby = [1, 2, 3, 5, 10, 13, 17, 22, 29, 33, 40, 55, 69, 73, 80, 91, 100]
numbers = []

def liczba(n):
	for x in range(0, n):
		print(x)
		x = x + 1
	return x

def dodawanie(n):
	suma = 0
	for x in range(0, n):
		suma = suma + x
	print (suma)

def wielokrotności(n):
	wielokrotność = 0
	mnożnik = 1
	for x in range(0, 10):
		wielokrotność = n*mnożnik
		mnożnik = mnożnik + 1
		print (wielokrotność)

def tablica(n):
	element_tab = 0
	for x in liczby:
		if liczby[element_tab] > n:
			print(liczby[element_tab])
		element_tab = element_tab + 1	

def losowanie(n):
	for x in range(0, n):
		numbers.append (random.randint(0,100))
	print(numbers)

def ujemne(n):
	for x in range(-n, 0):
		print(-n)
		n = n-1

def ciąg(n):
	pierwszy = 0
	drugi = 1
	print(pierwszy)
	print(drugi)
	for x in range(0, n-2):
		drugi = pierwszy + drugi
		pierwszy = drugi - pierwszy
		print(drugi)

n = int(input())

print("-----------------liczby------------------")
liczba (n)
print("----------------dodawanie kolejnych liczb-----------------------")
dodawanie (n)
print("--------------------wielokrotność n----------------------------------")
wielokrotności(n)
print("--------------tablica większa od n--------------------")
tablica(n)
print("-------------losowanie do tablicy (losuje n liczb)----------------")
losowanie(n)
print("--------------------wypisywanie od -n do -1-----------------------")
ujemne(n)
print("------------------fibonaci------------------------")
ciąg(n)

	