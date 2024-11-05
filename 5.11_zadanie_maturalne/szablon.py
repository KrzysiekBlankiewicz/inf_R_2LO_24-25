
# otwarcie pliku
nazwa_pliku = "bin.txt"
f = open(nazwa_pliku, "r")
liczby = []

# przeglądanie pliku i wyciąganie z niego liczb
for i in range(0, 100):
    a = f.readline()
    a = a[0:len(a)-1]
    liczby.append(a)

# test - wypisz pewną liczbę
print(liczby[2])

