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

def pierwsza(x):
	if x>1:
		for i in range(2, x//2):
			if(x%i)==0:
				return(0)
				break
		return(1)
	else:
		return(0)

for i in range(0, len(c)):
	p1 = c[i][0]
	p2 = c[i][1]	

z = pierwsza(x)
if z == 0:
	print("nie")
else:
	print("tak")