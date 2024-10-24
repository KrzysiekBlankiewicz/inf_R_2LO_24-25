import random

t = []

for x in range(0,7):
	t.append (random.randint(0,9))
print(t)

print("<>-------------------<<WSTĘP DO ALGORYTMÓW>>||<<24.10 Jan Krzos>>------------------------<>")

def max_elem(tab):
	max = tab[0]
	y = 0
	for x in range(0,7):
		if tab[x] > max:
			max = tab[x]
		if tab[y] < max:
			max = max                                                                                                                                                                                                                        
	return max

def min_elem(tab):
	min = tab[0]
	y = 0
	for x in range(0,7):
		if tab[x] < min:
			min = tab[x]
		if tab[y] > min:
			min = min
	return min

def sort_asc(tab):
	x = 6
	for i in range(0,6):
		for i in range(0,x):
			if tab[i] > tab[i+1]:
				te = tab[i]
				tab[i] = tab[i+1]
				tab[i+1] = te
	x = x - 1
	return tab
print("<>-------Największy element-------<>")
print(max_elem(t))
print("<>------Najmniejszy element-------<>")
print(min_elem(t))
print("<>-----Sortowanie (od najmniejszego do największego)-------<>")
print(sort_asc(t))

