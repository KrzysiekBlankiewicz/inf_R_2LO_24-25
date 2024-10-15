#Zadanie
print("==========================<<< ZADANIE 1 >>>==========================")

def obstawianie(bet_goleA, bet_goleB, real_goleA, real_goleB) :
	punkty = 0
 	#liczenie punktów za wynik drużyny
	if real_goleA == bet_goleA:
    		punkty = punkty + 1
	if real_goleB == bet_goleB:
    		punkty = punkty + 1
 
 # liczenie punktów za wynik
	if real_goleA > real_goleB and bet_goleA > bet_goleB:
    		punkty = punkty + 1
	if real_goleA < real_goleB and bet_goleA < bet_goleB:
		punkty = punkty + 1
	if real_goleA == real_goleB and bet_goleA == bet_goleB:
		punkty = punkty + 1

 #liczenie punktów za dobry wynik
	if real_goleA == bet_goleA and real_goleB == bet_goleB:
		punkty = punkty +2
	return punkty

print(">>>>>>>>>>>>>>>>>>>> podaj obstawienie <<<<<<<<<<<<<<<<<<<<<<")

bet_goleA = input()
bet_goleA = int(bet_goleA)

bet_goleB = input()
bet_goleB = int(bet_goleB)

print(">>>>>>>>>>>>>>>>>>>> podaj realne punkty <<<<<<<<<<<<<<<<<<<<<<<<<<")

real_goleA = input()
real_goleA = int(real_goleA)

real_goleB = input()
real_goleB = int(real_goleB)

obstawianie(bet_goleA, bet_goleB, real_goleA, real_goleB)
punkty = obstawianie(bet_goleA, bet_goleB, real_goleA, real_goleB)
print(punkty)








