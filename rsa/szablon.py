def keys(p, q):
  . . .
	. . .
	priv_key = (d, n)
	publ_key = (e, n)
	return (priv_key, publ_key)

def encode(message, publ_key):	#message jest liczbą
	e = publ_key[0]
	n = publ_key[1]
	. . .
	. . .
	code = . . .
	return code

def decode(code, priv_key):
	. . .
	. . .
	message = . . . 
	return message

(priv, public) = keys(?, ?)
m = input("podaj liczbę")
c = encode(m, public)
print(c)
x = decode(c, priv)
print(x)
