#for i in range(1, 30):
	#print(i*i*i)

def z2(x):
	pow = 0
	for i in range(1, 18):
		x = x*2
		print(x)
		pow = pow + 1
		if x >= 100000:
			print(" ")
			print(pow)
			break
	

#x = int(input("Podaj liczbe mniejsza niz 20 "))
#z2(x)

n = int(input("Podaj liczbę "))
def z3(n):
	for i in range(1, n):
		y = i*i
		if y == n:
			print(i)
			break

z3(n)
		
