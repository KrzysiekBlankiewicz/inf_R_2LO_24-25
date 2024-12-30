file = open("dane.txt")


jeden_ciag_tekstowy = file.read()
lista = jeden_ciag_tekstowy.split()
tabela = []

for i in lista: # dodaje liczby do tabeli 
	tabela.append(int(i))

suma = sum(tabela)
print(tabela)
print()
print("suma liczb to:", end=" ")
print(suma)
