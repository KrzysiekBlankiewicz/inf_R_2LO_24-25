import random
import math

def pi():
	tab = []
	ile = 1000000
	odl = 0
	ins = 0
	out = 0
	for i in range(0, ile):
		x = random.randint(0,1000)
		y = random.randint(0,1000)
		odl = math.sqrt((500-x)**2 + (500-y)**2)
		if odl > 500:
			out += 1
		else:
			ins += 1
	return(ins/ile*4)
c=0
for i in range(0, 10):
	c += pi()
print(c/10)
