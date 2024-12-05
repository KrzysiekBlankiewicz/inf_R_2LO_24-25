file = open("dane.txt")

r = file.read()
a = r.split()

b = []

for i in a:
    b.append(int(i))
    print(int(i))


suma = sum(b)
print("suma:", suma)




