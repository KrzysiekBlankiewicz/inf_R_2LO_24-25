import random

n = int(input("podaj liczbe n >= 0: "))


print ("1. n pierwszych liczb naturalnych: ")

def n_pierwszych_liczb_naturalnych(n):
    x = -1
    for _ in range (0, n):
        x += 1
        print(x)

n_pierwszych_liczb_naturalnych(n)


print("2. suma liczb od 1 do n: ")

def suma_liczb_od_1_do_n(n):
    if n > 0:
        x = -1
        y = 0
        for _ in range (0, n):
            x += 1
            y += x
        print(y)
    
suma_liczb_od_1_do_n(n)


print("3. 10 kolejnych wielokrotności n: ")

def dzies_kolejnych_wielokrotnosci_n(n):
    x = 0
    for _ in range (0, 10):
        print(x)
        x += n
        
dzies_kolejnych_wielokrotnosci_n(n)


print("4.1. liczby z tablicy liczby[], które są większe od n: ")

liczby = [-35, -3, 4, 43, 90, 314, 2137]

def liczby_z_tablicy_wieksze_od_n(n):

    for i in range (0, len(liczby)):
        if liczby[i] > n:
            print (liczby[i])
    
liczby_z_tablicy_wieksze_od_n(n)


print("4.2* losowe liczby od 1 do 1000 większe od n") 

a = random.randint(0, 1000)
b = random.randint(0, 1000)
c = random.randint(0, 1000)
d = random.randint(0, 1000)

tab_losowe = [a, b, c, d]


def losowe_liczby_z_tablicy_wieksze_od_n(n):

    for i in range (0, len(tab_losowe)):
        if tab_losowe[i] > n:
            print (tab_losowe[i])
    
losowe_liczby_z_tablicy_wieksze_od_n(n)


print("5. liczby od -n do -1: ")

def liczby_od_mn_do_m1(n):
    for i in range(-n, 0):
        print(i)

liczby_od_mn_do_m1(n)

print("6. n pierwszych elementów ciągu Fibonacciego: ")

# 1, 1, 2, 3, 5, 8, 13, 21, 
# b  c
# a  b  c
#    a  b  c
#       a  b  c

def n_pierwszych_elem_ciag_fibo(n):
    a = 0
    b = 1
    c = 0

    if n == 0:
        return

    print(b)
    if n >= 2:
        for i in range(n-1):
            c = a + b
            print (c)
            a = b
            b = c


n_pierwszych_elem_ciag_fibo(n)


print("7.n silnia: ")

# n! = 1 * 2 * 3 * 4 ... * n
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120

# 6! = 1*2 *3 *4 *5 *6

def n_silnia(n):
    wynik = 1
    for i in range (1, n+1):
        wynik *= i
    print(wynik)

n_silnia(n)


print("8. wyświetli tylko te napisy z tablicy napisy[], których długość jest równa n")

r_slowa = ["xd","lol","ogon","matma","kotka","piesek","skibidi"]


def napisy_z_tablicy_rowne_n(n):
    for i in range (0, len(r_slowa)):
        if len(r_slowa[i]) == n:
            print(r_slowa[i])


napisy_z_tablicy_rowne_n(n)

print("9.")

# 1
# 1 2
# 1 2 3
# 1 2 3 4

def liczby_w_schemacie(n):

    for i in range (1, n+1):
        for j in range (1, i+1):
            print(j, end=" ")
        print()

liczby_w_schemacie(n)

print("10. ")

def liczby_w_schemacie_dolnym(n):

    for i in range (n, 0, -1):
        for j in range (i, 0, -1):
            print(j, end=" ")
        print()

liczby_w_schemacie_dolnym(n)

print("11.")

def liczby_w_schemacie_dig(n):
    for i in range (1, n+1):
        for j in range (1, i+1):
            print(j, end=" ")
        print()
    for i in range (n, 0, -1):
        for j in range (i, 0, -1):
            print(j, end=" ")
        print()

liczby_w_schemacie_dig(n)