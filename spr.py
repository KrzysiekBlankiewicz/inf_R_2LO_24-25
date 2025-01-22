def dzielniki(a):
	tab = []
	for i in range(1, a+1):
		if a%i == 0:
			tab.append(i)
	return tab

#print(dzielniki(69))

def nwd(a, b):
	c = 0
	while b != 0:
		c = a%b
		a = b
		b = c
		if b == 0:
			return(a)

#print(nwd(33, 333333))

def bin_dz(a):
	suma = 0
	cyfra = str(a)
	dl = len(str(a))
	tab = []

	for j in range(0, dl):
		tab.append(int(cyfra[j]))

	for i in range(dl-1, -1, -1):
		if tab[i] == 1:
			suma += 2**(dl-i-1)
	print(suma)
bin_dz(10101010101010110101010101010101110101010111010101010101010101011101010101110101010101010101010111010101011101001110101010111010)