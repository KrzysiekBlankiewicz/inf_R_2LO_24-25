# funkcji możemy przekazać argument
# zmienna x wewnątrz funkcji jest innym obiektem niż globalna zmienna x

#def funkcjaA(x):
 #   print(x)

#x = 4
#c = "abc"
#funkcjaA(3)
#funkcjaA(c)

# funkcja może zwrócić jakąś wartość
# możemy tej wartości użyć np. w obliczeniach

#def funkcjaB(a, b):
#    suma = a+b
#    wynik = suma / 2
#    return wynik

#x = 2
#y = 6
#srednia = funkcjaB(x, y)
#print(srednia)

# ZADANIE:
# napisz funkcję, która wyznaczy liczbę otrzymanych punktów za obstawienie wyniku meczu piłkarskiego
# niech przyjmie cztery argumenty - bet_goleA, bet_goleB, real_goleA, real_goleB
# niech zwróci jedną liczbę - liczbę punktów
# przyznajemy:
# jeden punkt za poprawne obstawienie zwycięzcy (lub remisu)
# jeden punkt za poprawne obstawienie liczy goli drużyny
# dwa punkty za poprawne obstawienie wyniku

# napisz program, który przyjmie z klawiatury od użytkownika 4 liczby za pomocą input()...
# (pamiętaj, żeby przekonwertować je z napisu na liczbę za pomocą int() )
# ...oraz wypisze otrzymaną ilczbę punktów

import random


def zwracaniePunktow():
	punkty = 0

	real_goleA = random.uniform(1, 10)
	real_goleB = random.uniform(1, 10)

	print(">>> WYPISZ CYFRE DRUŻYNY KTÓRA WYGRA WEDŁUG CIEBIE: DruzynaA(1) ALBO DruzynaB(2) <<<")
	druzyna = input()

	print(">>> WYPISZ ILE GOLI ZDOBĘDZIE DRUŻYNA A <<<")
	bet_goleA = input()
	print(">>> WYPISZ ILE GOLI ZDOBĘDZIE DRUŻYNA B <<<")
	bet_goleB = input()


	if (real_goleA == bet_goleA):
		punkty += 1

	if (real_goleB == bet_goleB):
		punkty += 1

	if (real_goleA == bet_goleA and real_goleB == bet_goleB and real_goleA == real_goleB and bet_goleA == bet_goleB):
		punkty += 1

	if (real_goleA == bet_goleA and druzyna == 1):
		punkty += 1

	if (real_goleB == bet_goleB and druzyna == 2):
		punkty += 1
	
	if (real_goleA == bet_goleA and real_goleB == bet_goleB):
		punkty += 2
	return punkty


jakkolwiek = zwracaniePunktow()
print( jakkolwiek )




