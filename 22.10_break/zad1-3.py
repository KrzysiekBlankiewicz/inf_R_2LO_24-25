#for i in range(0, 30):
	#print(i*i*i)

def z2(n):
	pow = 0
	for i in range(1, 17):
		n = n*2
		print(n)
		pow = pow +1
		if n>100000:
			print(" ")
			print(pow)		
			break


n = int(input())
#if x>0 and x<20:
	#z2(x)


def z3(n):
	x = 0
	for i in range(1, n):
		y = x*x
		if y == n:
			print(x)
			break
		x = x+1
z3(n)