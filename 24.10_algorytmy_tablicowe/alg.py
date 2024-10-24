t = [2, 0, 8, 3, 4, 9, 7, 6, 1]

def max_e(t):
	max = t[0]
	for i in range(1,9):
		if t[i] > max:
			max = t[i]

	
	print(max)

def min_e(t):
	min = t[0]
	for i in range(1,9):
		if t[i] < min:
			min = t[i]
	print(min)


		
def mmr(t):
	x = len(t)
	for i in range(0, len(t)):
		for i in range(0,x-1):
			if t[i] > t[i+1]:
				temp = t[i]
				t[i] = t[i+1]
				t[i+1] = temp
		x = x-1
		print(t)


print("max = ")
max_e(t)
print("min = ")
min_e(t)
print("uporządkowanie:")
mmr(t)

