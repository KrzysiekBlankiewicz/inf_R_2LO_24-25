file = open("dane.txt", "r")
r = file.read()
a = r.split()
b = []

for i in a:
    b.append(int(i))

suma = sum(b)

print("suma jest r�wna:")
print(b)
