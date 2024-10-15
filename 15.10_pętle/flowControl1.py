# funkcji możemy przekazać argument
# zmienna x wewnątrz funkcji jest innym obiektem niż globalna zmienna x

def funkcjaA(x):
    print(x)

x = 4
c = "abc"
funkcjaA(3)
funkcjaA(c)

# funkcja może zwrócić jakąś wartość
# możemy tej wartości użyć np. w obliczeniach

def funkcjaB(a, b):
    suma = a+b
    wynik = suma / 2
    return wynik

x = 2
y = 6
srednia = funkcjaB(x, y)
print(srednia)

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
