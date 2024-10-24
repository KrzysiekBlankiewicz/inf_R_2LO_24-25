#Algorytmy.py
print("-------------<ALGORYTMY>-------------")

t = [4, 2, 56, 32, 12, 35, 14, 9, 85, 45]

def max_elem(t):
	maximum = t[0]
	max = 0
	for i in range(0, 9):
		if maximum > max:
			max = maximum
			i += 1
			 
	return max





def min_elem(t):
	
	minimum = t[0]
	min = 0
	for i in range(0, 9):
		if minimum < min:
			min = minimum
			i += 1
		
	return min





def move_max_r(t):

	for i in range(0, 9):
		for i in range(0,9):
			if t[i] > t[i+1]:
				tab = t[i]
				t[i] = t[i+1]
				t[i+1] = tab
	return t
print("-------------TABELA-------------")
print (t)
max = t[0]
print("-------------MAX-------------")
print(max_elem(t))
print("-------------MIN-------------")
print(min_elem(t))
print("-------------SORTOWANIE-------------")
print(move_max_r(t))