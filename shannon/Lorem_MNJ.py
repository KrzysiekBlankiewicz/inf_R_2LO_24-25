file = open("Lorem_ipsum.txt")
string = file.read()
alfabet = "abcdefghijklmnopqrstuvwxyz"

licznik = 0
for znak in string:
    licznik += 1
print(licznik)

for litera in alfabet:
    liczba = 0
    for znak in string:
        if znak.lower() == litera:
            liczba += 1
    if liczba > 0:
        print(f"jest {liczba} {litera} w pliku")
