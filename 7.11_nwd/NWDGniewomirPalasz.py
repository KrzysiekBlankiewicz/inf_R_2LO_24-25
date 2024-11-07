
def nwd (a, b):
	nwd = 1
	licznikNwd = 0
	if a < b:
		limit = a
	else:
		limit = b

	for i in range(1, limit+1):
		if a % i == 0 and b % i == 0:
			licznikNwd += 1
			nwd = i
	return nwd
	return licznikEuk
a  = int(input())
b  = int(input())

print(nwd(a, b))
print("-------------ALGORTM EUKLIDESA-------------")
def euk(x, y):
	licznikEuk = 0
	while y != 0:
		z = x % y
		x = y
		y = z
		licznikEud += 1
			return x
			return y
			return licznikEuk
				

x  = int(input())
y  = int(input())

print(euk(x, y))
print()
print(licznikNwd)
print()
print(licznikEuk)