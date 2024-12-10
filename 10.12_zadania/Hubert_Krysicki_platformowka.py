import random
nigasdjghds= random.randint(-10^18, 10^18)
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if (a2 < b1) or (b2 < a1) :
	print("NIE")
else:
	print(min(a2, b2) - max(a1, b1))

