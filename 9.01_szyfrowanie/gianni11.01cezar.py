def cezar_znak(tekst, przesuniecie):
    wynik = ""
    for znak in tekst:
        if 'a' <= znak <= 'z':  
            przemiana = chr(((ord(znak) - ord('a') + przesuniecie) % 26) + ord('a'))
            wynik += przemiana
        else:
            wynik += znak

    return wynik


n = int(input("Podaj przesunięcie: "))
tekst = ("agv")

odp = cezar_znak(tekst, n)


print(odp)
