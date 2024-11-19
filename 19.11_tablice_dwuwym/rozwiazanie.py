
def drawBoardSimple():
    print(" ___")
    print("|   |")
    print("|   |")
    print("|___|")


def drawBoardComplex(size):
    first_row = " "
    for i in range(0, size):
        first_row = first_row + "_"
    print(first_row)
    
    for i in range(0, size-2):
        row = "|"
        for j in range(0, size):
            row = row + " "
        row = row + "|"
        print(row)
    
    last_row = "|"
    for i in range(0, size):
        last_row = last_row + "_"
    last_row = last_row + "|"
    print(last_row)


drawBoardComplex(11)
