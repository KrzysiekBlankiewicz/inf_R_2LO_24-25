def drawBoardSimple():
    print(" ___")
    print("|   |")
    print("|   |")
    print("|___|")


def drawBoardComplex(size):
    fr = " "
    lr = "|"
    for i in range(0, size):
        fr = fr + "_"
    print(fr)
    for i in range(0,size-2):
        row = "|"
        
        for j in range(0, size):
            row = row + " "
        row = row + "|"
        
        print(row)
    for i in range(0,size):
        lr = lr + "_"
    lr = lr + "|"
    print(lr)

drawBoardComplex(11)