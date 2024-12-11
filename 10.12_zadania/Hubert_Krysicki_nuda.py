k = int(input("Podaj liczbe $ w linii "))
n = int(input("Podaj całkowitą liczbe $ "))

l = ""
x = 0
while x < n:
	y = min(k, n - x)
	l = "$ " * y
	x += y
	k += 2
	print(l)