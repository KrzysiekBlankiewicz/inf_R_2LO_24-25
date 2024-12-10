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

za = 0
zb = 0
zc = 0

for i in range(0, len(c)):
    x = c[i][0]
    y = c[i][1]
    if x<5000 and y<5000:
        za += 1
for i in range(0, len(c)):
    x = c[i][0]
    y = c[i][1]
    if x == 5000 and y != 5000:
        zb += 1
    if y == 5000 and x != 5000:
        zb += 1
    if x == 5000 and y == 5000:
        zb += 1

for i in range(0, len(c)):
    x = c[i][0]
    y = c[i][1]
    if x>5000 and y<5000:
        zc += 1
    if y>5000 and x<5000:
        zc += 1
    if x>5000 and y>5000:
        zc += 1

print("Punkty wewnątrz kwadratu:")
print(za)
print("Punkty na bokach kwadratu:")
print(zb)
print("Punkty na zewnątrz kwadratu:")
print(zc)
