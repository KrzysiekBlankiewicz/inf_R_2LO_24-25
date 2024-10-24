n = [5,13,25,8567,23958,-2,100,7,4,89,2,1,15,34]
def max(n):
	max = 0
	for i in range(0,len(n)):
		if n[i] > max:
			max = n[i]
	print(max)
def min(n):
	min = n[0]
	for i in range(0,len(n)):
		if n[i] < min:
			min = n[i]
	print(min)
def mmax(n):
	for i in range(0,len(n)-1):
		if n[i] > n[i+1]:
			temp = n[i]
			n[i] = n[i+1]
			n[i+1] = temp
		print(n)
def sort(n):
	x = len(n)
	for i in range(0,len(n)):
		for i in range(0,x-1):
			if n[i] > n[i+1]:
				temp = n[i]
				n[i] = n[i+1]
				n[i+1] = temp
		x = x - 1
		print(n)
sort(n)