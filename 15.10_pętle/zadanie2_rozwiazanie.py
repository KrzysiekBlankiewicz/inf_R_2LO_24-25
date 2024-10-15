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

betA = [1, 3, 2, 2]
betC = [4, 2, 2, 1]

realA = [1, 3, 1, 0]
realC = [1, 2, 2, 0]

x0 = punkty(betA[0], betC[0], realA[0], realC[0])
x1 = punkty(betA[1], betC[1], realA[1], realC[1])
x2 = punkty(betA[2], betC[2], realA[2], realC[2])
x3 = punkty(betA[3], betC[3], realA[3], realC[3])

print("zdobyłeś punktów:")
print( x0 )
print( x1 )
print( x2 )
print( x3 )
print("w sumie:")
print( x0+x1+x2+x3 )
