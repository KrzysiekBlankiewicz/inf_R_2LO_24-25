
def get_digit_value(znak):
    if znak == '0':
        return 0
    elif znak == '1':
        return 1
    elif znak == '2':
        return 2
    elif znak == '3':
        return 3
    elif znak == '4':
        return 4
    elif znak == '5':
        return 5
    elif znak == '6':
        return 6
    elif znak == '7':
        return 7
    elif znak == '8':
        return 8
    elif znak == '9':
        return 9

def get_char_from_value(cyfra):
    if cyfra == 0:
        return '0'
    elif cyfra == 1:
        return '1'
    elif cyfra == 2:
        return '2'
    elif cyfra == 3:
        return '3'
    elif cyfra == 4:
        return '4'
    elif cyfra == 5:
        return '5'
    elif cyfra == 6:
        return '6'
    elif cyfra == 7:
        return '7'
    elif cyfra == 8:
        return '8'
    elif cyfra == 9:
        return '9'

def to_int(napis):
    liczba = 0
    dlugosc_napisu = len(napis)
    
    for i in range(0, dlugosc_napisu):
        znak = napis[i]
        cyfra = get_digit_value(znak)
        liczba = liczba*10 + cyfra
    return liczba
    
def to_string(liczba):
    napis = ""
    gotowa = False
    
    for i in range(0, 100):
        cyfra = liczba % 10
        liczba = (liczba - cyfra)/10
        napis = get_char_from_value(cyfra) + napis
        if liczba == 0:
            return napis

a = input("podaj napis (liczbę). Przekonwertuję ją na liczbę i dodam 1:")
x = to_int(a)
print(x+1)

y = int(input("podaj liczbę. Przekonwertuję ją na napis i wypiszę"))
b = to_string(y)
print(b)



