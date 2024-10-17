# funkcji możemy przekazać argument
# zmienna x wewnątrz funkcji jest innym obiektem niż globalna zmienna x



import random



def Gambling(r,b):
	punkty = 0
	rr = random.randint(0,3)
	rb = random.randint(0,3)
	if r == rr:
		punkty = punkty + 1

	if b == rb:
		punkty = punkty + 1

	if b == rb and r == rb:
		punkty = punkty + 2

	zwyciezca = 0
	if b > r:
		zwycieca = 2
	if r > b:
		zwyciezca = 1
	if b == r:
		zwyciezca = 0
	if zwyciezca == 0:
		punkty = punkty + 1
	return punkty

print("")
print ("Ile punktów zdobędzie Real Madryt?")
r = int(input())
print ("Ile punktów zdobędzie FC Barcelona?")
b = int(input())

wynik = Gambling(r,b)

print(" ")
print("Gratulacje! Zdobyłeś następujaca liczbę punktów")
print(wynik)
print("Pamiętaj! 99% obstawiających rezygnuje tuż przed wielką wygraną!")





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
