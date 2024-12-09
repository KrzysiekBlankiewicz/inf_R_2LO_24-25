
import math


def z41():	
	file = open("punkty.txt")
	r = file.read()
	a = r.split()
	b = []
	for i in a:
		b.append(int(i))
	c = []
	for j in range(0, len(b), 2):
		para = [b[j], b[j+1]]
		c.append(para)
	ile = 0
	def pierwsza(x):
		if x>1:
			for i in range(2, int(x**0.5) + 1):
				if x % i == 0:
					return(0)
			return(1)
		else:
			return(0)

	for i in range(0, len(c)):
		p0 = pierwsza(c[i][0])
		p1 = pierwsza(c[i][1])
		if p0 and p1 == 1:
			ile = ile + 1
	
	print(ile)

def z42():
	file = open("punkty.txt")
	r = file.read()
	a = r.split()
	b = []
	for i in a:
		b.append(int(i))
	c = []
	for j in range(0, len(b), 2):
		para = [b[j], b[j+1]]
		c.append(para)
	suma = 0
	for i in range(0, len(c)):
		cyfry0 = set()	
		cyfry1 = set()
		p0 = str(c[i][0])
		for j in range(0, len(p0)):
			cyfry0.add(int(p0[j]))
		p1 = str(c[i][1])
		for j in range(0, len(p1)):
			cyfry1.add(int(p1[j]))
		if cyfry0 == cyfry1:
			suma += 1
	print(suma)


def z43():
	file = open("punkty.txt")
	r = file.read()
	a = r.split()
	b = []
	for i in a:
		b.append(int(i))
	c = []
	for j in range(0, len(b), 2):
		para = [b[j], b[j+1]]
		c.append(para)
	odl = 0 
	for i in range(0, len(c)):
		for j in range(i+1, len(c)-1):
			xA = c[i][0]
			yA = c[i][1]
			xB = c[j][0]
			yB = c[j][1]
			new_odl = math.sqrt((xB - xA)**2 + (yB - yA)**2)
			if new_odl < 0:
				new_odl = new_odl * -1
			if new_odl > odl:
				odl = new_odl
				kon_xA = xA
				kon_yA = yA
				kon_xB = xB 
				kon_yB = yB 
	print(round(odl))
	print(kon_xA, kon_yA)
	print(kon_xB, kon_yB) 



def z44():
	file = open("punkty.txt")
	r = file.read()
	a = r.split()
	b = []
	for i in a:
		b.append(int(i))
	c = []
	for j in range(0, len(b), 2):
		para = [b[j], b[j+1]]
		c.append(para)

	suma1 = 0
	suma2 = 0
	suma3 = 0

	for i in range(0, len(c)):
		x = c[i][0]
		y = c[i][1]
		if x<5000 and y<5000:
			suma1 += 1
	for i in range(0, len(c)):
		x = c[i][0]
		y = c[i][1]
		if x == 5000 and y != 5000:
			suma2 += 1
		if y == 5000 and x != 5000:
			suma2 += 1
		if x == 5000 and y == 5000:
			suma2 += 1

	for i in range(0, len(c)):
		x = c[i][0]
		y = c[i][1]
		if x>5000 and y<5000:
			suma3 += 1
		if y>5000 and x<5000:
			suma3 += 1
		if x>5000 and y>5000:
			suma3 += 1

	print(suma1, suma2, suma3)
	
z41()
print("---------------------")
z42()
print("---------------------")
z43()
print("---------------------")
z44()
