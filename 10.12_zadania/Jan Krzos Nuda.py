k = int(input("$ w pierszej linii "))
n = int(input("podaj liczbę wszystkich $ "))
nc = n
licznik = 0
if n < k:
    print("błąd")
else:
    z = ""
    for x in range(0, k):
        z = z + "$ "
        n = n - 1
        licznik = licznik + 1

    print(z + " " + str(licznik)) 

    for y in range(1,n):
        if k < n-1:

            z = z + "$ $ "
            k = k + 2
            n = n - k
            licznik = licznik + k 
            print(z+ " " + str(licznik))

        elif n>0:
            z = ""
            for x in range(0, n):
                z = z + "$ "
                licznik = licznik + 1
            print(z+ " " + str(licznik))
            break
print(licznik)


