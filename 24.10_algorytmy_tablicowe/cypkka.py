def max_elem(majka):
	max = majka[0]
	for i in range(0, 6):
		if majka[i] > max:
			max = majka[i]
	return max


t = [1, 7, 18, 22222222222222222223434434343434344334334, 10, 36, 3]
print(max_elem(t))
