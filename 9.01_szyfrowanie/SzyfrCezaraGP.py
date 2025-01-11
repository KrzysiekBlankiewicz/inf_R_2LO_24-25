


def SzyfrowanieCezara(tekst, przesuniecie):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                poczatek = ord("A")
                koniec = ord("Z")
            else:
                poczatek = ord("a")
                koniec = ord("z")

            kod = ord(znak)
            nowy_kod = kod + przesuniecie

            if nowy_kod > koniec:
                nowy_kod = nowy_kod - koniec + poczatek - 1

            nowy_znak = chr(nowy_kod)
            wynik += nowy_znak
        else:
            wynik += znak
    

    return wynik


def TestSzyfrowanieCezara():
    print(SzyfrowanieCezara("abc", 3))
    print(SzyfrowanieCezara("xyz", 3))
    print(SzyfrowanieCezara("Hello, World!", 5))
    print(SzyfrowanieCezara("abc", 3) == "def")
    print(SzyfrowanieCezara("xyz", 3) == "abc")
    print(SzyfrowanieCezara("ABC", 3) == "DEF")
    print(SzyfrowanieCezara("XYZ", 3) == "ABC")
    print(SzyfrowanieCezara("a b c!", 3) == "d e f!")
    print(SzyfrowanieCezara("Hello, World!", 5) == "Mjqqt, Btwqi!")



TestSzyfrowanieCezara()








