def DBS():
	print(" ___")
	print("|   |")
	print("|   |")
	print("|___|")


def DBC(size,polx,poly):
	frow = " "
	for i in range(0,size):
		frow = frow + "_"
	print(frow)
	for i in range(0,size-2):
		row = "|"
		x = 0
		for j in range(0, size):
			
			if x == polx:
				row = row + "x"
				x = x + 1
			else:
				row = row + " "
				x = x + 1
		row = row + "|"
		print(row)

	lrow = "|"
	for i in range(0,size):
		lrow = lrow + "_"
	lrow = lrow + "|"
	print(lrow)

DBC(5,3)
