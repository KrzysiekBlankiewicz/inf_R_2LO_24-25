def maluch(dar):
    for i in range(len(dar) - 1):
        if dar[i] > dar[i + 1]:
            dar[i], dar[i + 1] = dar[i + 1], dar[i]
    
    return dar
def max_elem(majka):
	max = majka[0]
	for i in range(0, 6):
		if majka[i] > max:
			max = majka[i]
	return max
    
def max_elem(majka):
	max = majka[0]
	for i in range(0, 6):
		if majka[i] < max:
			max = majka[i]
	return max
t = [3, 5, 2, 9, 1]
nt = maluch(t)
print(nt)
