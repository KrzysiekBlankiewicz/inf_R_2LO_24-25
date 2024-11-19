


def drawBoardComplex(size, pol):
    firstRow = " "
    for i in range(0,size):
        firstRow = firstRow + "_"
    print(firstRow)
    for i in range(0,size -2):
        row = "|"
        for j in range(0, size):
            row = row + " " 
        row= row+"|"
        print(row)

    lastRow = "|"
    for i in range(0,size):
        lastRow = lastRow + "_"
    lastRow = lastRow + "|"
    print(lastRow)


pol = [4,3]
drawBoardComplex(5 , pol)
