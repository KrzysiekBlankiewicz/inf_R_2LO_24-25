def cezar_slowo(slowo, n):
    limit = 122
    wynik = ""
    for znak in slowo:
        if 'b' <= znak <= 'z': 
            x = ord(znak)
            x += n
            if x > limit:
                x = (x - limit + 96)
            wynik += chr(x)
        else:
            wynik += znak  
    return wynik

slowo = input("Podaj słowo: ")
n = 1

syf = cezar_slowo(slowo, n)

with open('slowa.txt', 'r') as plik:
    linie = [linia.strip() for linia in plik.readlines()]

while True:
    if syf in linie:
        print(syf)
        break
    else:
        n += 1
        syf = cezar_slowo(slowo, n)

