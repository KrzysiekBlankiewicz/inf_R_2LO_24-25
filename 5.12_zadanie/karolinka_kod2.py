file = open("dane.txt", "r")
r = file.read()
a = r.split()
b = []
c = []

for i in range(0, len(a), 2):
    pary = b.append((int(a[i]), int(a[i + 1])))
    suma_par = c.append(sum((int(a[i]), int(a[i + 1]))))

suma_c = sum(c)
print(c)
print(b)
print(suma_c)

suma = sum(c)
srednia = suma / len(c)

print(srednia)
