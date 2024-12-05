file = open("dane.txt")
r = file.read()
a = r.split()
b = []

for i in a:
	b.append(int(i))

suma = sum(b)
print(b)
print(suma)