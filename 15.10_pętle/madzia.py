import random
def funkcjaC(bet_goleA, bet_goleB, real_goleA, real_goleB):
	punkty = 0
	if bet_goleA == real_goleA:
		punkty = punkty + 1
	if bet_goleB == real_goleB:
		punkty = punkty + 1
	if real_goleA > real_goleB and bet_goleA > bet_goleB:
		punkty = punkty + 1
	if real_goleA < real_goleB and bet_goleA < bet_goleB:
		punkty = punkty + 1
	if real_goleA == real_goleB and bet_goleA == bet_goleB:
		punkty = punkty + 1
	if bet_goleB == real_goleB and bet_goleA == real_goleA:
		punkty = punkty + 2
	return punkty

myA = int( input() )
myB = int( input() )
A = random.randint(0,10)
B = random.randint(0,10)

x = funkcjaC(myA, myB, 2, 3)
print( x )
	

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
