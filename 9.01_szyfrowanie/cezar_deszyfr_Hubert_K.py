def c_s(sl, n):
    limit = 122
    wynik = ""
    for znak in sl:
        if 'b' <= znak <= 'z': 
            x = ord(znak)
            x += n
            if x > limit:
                x = (x - limit + 96)
            wynik += chr(x)
        else:
            wynik += znak  
    return wynik

n = 1
sl = input("Podaj slowo: ")


xyz = c_s(sl, n)

with open('slowa.txt', 'r') as plik:
    linie = [linia.strip() for linia in plik.readlines()]

while True:
    if xyz in linie:
        print(xyz)
        break
    else:
        n += 1
        xyz = c_s(sl, n)
