file = open("dane.txt")


jeden_ciag_tekstowy = file.read()
lista = jeden_ciag_tekstowy.split()
tabela = []

for i in range(0, len(lista), 2): # od 0 do liczby liczb z listy, skok co 2 
    i_liczba = int(lista[i]) # i_liczba jest to liczba z pierwszej kolumny pliku
    ip1_liczba = int(lista[i + 1]) if i + 1 < len(lista) else 0 # a to z drogiej kolumny
    tabela.append([i_liczba, ip1_liczba]) # dobieranie tych liczb takjak sa w pliku

for para in tabela:
    print(f"{para[0]} {para[1]}")

sumy_par = [sum(para) for para in tabela]

print("sumy par wynosi:", end=" ")
print(sumy_par)
