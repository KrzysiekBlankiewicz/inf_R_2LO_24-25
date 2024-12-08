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


def punkty_za_obstawienie_wyniku_meczu(bet_goleA, bet_goleB, real_goleA, real_goleB):

  punkty_gracza = 0
  
  if (real_goleA < real_goleB and bet_goleA < bet_goleB):
  # jeden punkt za poprawne obstawienie zwycięzcy (lub remisu)
    punkty_gracza = punkty_gracza +1

  elif (real_goleA > real_goleB and bet_goleA > bet_goleB):
    # jeden punkt za poprawne obstawienie zwycięzcy (lub remisu)
      punkty_gracza = punkty_gracza +1
    
  elif (real_goleA == real_goleB and bet_goleA == bet_goleB):
  # jeden punkt za poprawne obstawienie zwycięzcy (lub remisu)
    punkty_gracza = punkty_gracza +1
    
  else:
    punkty_gracza = punkty_gracza +0
    
  if (real_goleA == bet_goleA):
    punkty_gracza = punkty_gracza +1
  
  if (real_goleB == bet_goleB):
    punkty_gracza = punkty_gracza +1
    
  if (real_goleA == bet_goleA and real_goleB == bet_goleB):
    punkty_gracza = punkty_gracza +2

  return punkty_gracza



bet_goleA = int( input("obstaw liczbę goli drużyny A: ") )
bet_goleB = int( input("obstaw liczbę goli drużyny B: ") )
A = random.randint(0, 5)
B = random.randint(0, 5)


punkty = punkty_za_obstawienie_wyniku_meczu(bet_goleA, bet_goleB, A, B)

print()
print("Rzeczywiste punkty drużyny A wynoszą:")
print(A)
print("Rzeczywiste punkty drużyny B wynoszą:")
print(B)
print("liczba twoich punktów wynosi:")
print(punkty,"/5")




