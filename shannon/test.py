
file = open("nazwa.txt")

string = file.read()

suma = 0
for znak in string:
	suma += 1
print(suma)

tablica = []

licznik = 0
for i in range(97, 123):
    litera = chr(i)
    for znak in string:
        if znak == litera:
            licznik += 1
    tablica.append((litera, round(licznik/suma, 2)))
    licznik = 0

print(tablica)
