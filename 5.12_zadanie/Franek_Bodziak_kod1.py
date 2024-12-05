file = open("dane.txt")

r = file.read()

a = r.split()
b = []
for i in a:
    b.append(int(i))
suma = 0
for l in b:
    suma = suma + l

print (suma)


