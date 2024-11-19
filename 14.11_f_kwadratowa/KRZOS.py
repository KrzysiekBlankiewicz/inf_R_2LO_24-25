
def drawBoardSimple():
    print(" ___")
    print("|   |")
    print("|   |")
    print("|___|")


def drawBoardComplex(size, X, Y):
	first_row = " "
	for i in range(0,size):
		first_row = first_row + "_"
	print(first_row)

	for i in range(0, size-1):
		row = "|"
		for j in range(0, size):
		    row = row + " "
		row = row + "|"
		print(row)

	last_row = "|"
        if Y == size:
            for i in range (0, X - 1):
                last_row = last_row + "_"
            last_row = last_row + "o"
            for i in range(X + 1, size):
                last_row = last_row + "_"
                
        else:
             for i in range (0, size):
                last_row = last_row + "_"
            last_row = last_row + "|"
        last_row = last_row + "|"
        print(last_row)

wielkoœæ = int(input("podaj wielkoœæ planszy(jest kwadratem)"))
pozycja_X = int(input("podaj pierwsz¹ pozycjê gracz"))
pozycja_Y =int(input("podaj drug¹ pozycjê gracza"))
drawBoardComplex(wielkoœæ, pozyja_X, pozycja_Y)
