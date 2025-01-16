import math

def rel_prime(x, y):
	return math.gcd(x, y) == 1

def keys(p, q):
	n = p * q
	fi = (p-1)*(q-1)
		
	for i in range(2, fi):
		if rel_prime(i ,fi):
			e = i
	while (d*e % fi == 1):
		d += 1
		
		

	priv = (d, n)
	publ = (e, n)
	return(priv, publ)

def encode(message, publ):
	e = publ[0]
	n = publ[1]
	
	return code

def decode(code, priv):
	
	return message

print(keys(10, 5)[0][0])