file = open("dane.txt")

r = file.read()
a = r.split()
b = []
for i in a:
	b.append(int(i))
c = []
for j in range(0, len(b), 2):
	para = [b[j], b[j+1]]
	c.append(para)
print(c)
s_para = []

for k in range(0, len(c)):
	s_para = s_para + [ c[k][0] + c[k][1] ]
print(s_para)

s = 0
for p in range(0, len(s_para)):
	s = s + s_para[p]
print(s/len(s_para))