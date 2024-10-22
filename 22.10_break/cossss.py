#def brea(x):
#for i in range(1,100,1):
#print(i)
#if i == x:
#break
#x = int(input("daj liczbe od 1 do 100"))
#brea(x)
def duzo(n):
	for i in range(1,20,1):
		n = n*2
		print(n)
		if n >= 100000:
			break
	print(i)
def pierw(x):
	for i in range(1,x):
		b = i*i
		if b == x:
			print(i)
			break
	
	
x = int(input("dej liczbe naturalną"))
pierw(x)
