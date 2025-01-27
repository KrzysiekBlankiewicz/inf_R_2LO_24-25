n = int(input())
limit = 122
def cezar_znak(zn, n):
	x = ord(zn)
	x += n
	if x > limit:
		x -= 26
	return(chr(x))
odp = ""
sl = str(input())

for i in range(0, len(sl)):
	x = cezar_znak(sl[i], n)
	odp += x
print(odp)
