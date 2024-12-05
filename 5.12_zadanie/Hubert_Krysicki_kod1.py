file = open("dane.txt")

r = file.read()
a = r.split()
b = []

for i in a:
	b.append(int(i))
print(b)
suma = 0
for p in range(len(b)):
	suma = suma + b[p]
print(suma)
