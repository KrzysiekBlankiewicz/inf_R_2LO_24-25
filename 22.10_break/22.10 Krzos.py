print("##_-_-_-_----<<<Przerywanie Pętli +Jan Krzos+ 22.10.2024>>>----_-_-_-_##")

print("<><>--------<zadanie 1>--------<><>")
l = 1
for l in range (1, 30):
	l = l*l*l
	print(l)

print("<><>---------<zadanie2>----------<><>")

i = 0
x = int(input())
if x>=20 or x<0:
	print("podaj liczbę naturalną mniejszą od 20")
	x = int(input())
if x<20 and x>0:
	for z in range(0, 100000):
		x = x + x
		i = i + 1
		print(x)
		if x>=100000:
			print("program powtórzył się " + str(i)  + " razy")
			break

print("<><>-------<zadanie 3 (pd)>----------<><>")
n = int(input())
if n < 0:
	print("ma być naturalna")
	n = int(input())
if n > 0:
	n = n ** 0.5
	print(n)

