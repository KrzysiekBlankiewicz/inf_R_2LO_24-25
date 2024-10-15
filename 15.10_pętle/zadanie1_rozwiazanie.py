import random

def punkty(betA, betB, realA, realB):
	punkt = 0
        # dodaj punkty za obstawienie liczby goli
	if betA == realA:
		punkt = punkt + 1
	if betB == realB:
		punkt = punkt + 1

        # dodaj punkty za obstawienie zwycięzcy
	if betA > betB and realA > realB:
		punkt = punkt + 1
	if betA < betB and realA < realB:
		punkt = punkt + 1
	if betA == betB and realA == realB:
		punkt = punkt + 1

        # dodaj punkty za obstawienie dokładnego wyniku
	if betA == realA and betB == realB:
		punkt = punkt + 2
	
	return punkt

myA = int( input("obstaw liczbę goli drużyny A: ") )
myB = int( input("obstaw liczbę goli drużyny B: ") )
A = random.randint(0, 5)
B = random.randint(0, 5)

print("wynik meczu:")
print(A)
print(B)

x = punkty(myA, myB, A, B)
print("zdobyłeś punktów:")
print( x )
