plik = open("dane.txt")

zawartosc = plik.read()
# otwiera plik.txt i czyta jego zawartość


liczby = zawartosc.split()
# rozdziela zawartość na liczby w liscie a
pary = []

for i in range(0, len(liczby), 2):
    pierwsza_liczba = int(liczby[i])
    druga_liczba = int(liczby[i + 1]) if i + 1 < len(liczby) else 0
    pary.append([pierwsza_liczba, druga_liczba])
# tworzy pary z liczb co dwa elementy 


for para in pary:
    print(f"{para[0]} {para[1]}")
# wyświetla każdą parę

sumy_par = [sum(para) for para in pary]
srednia_sum = sum(sumy_par) / len(sumy_par) if sumy_par else 0
#oblicza średnią i sumy par

print("Sumy par:", sumy_par)
print("Średnia sum:", srednia_sum)
