
def isMarkerAtLegitPosition(table, xPos, yPos):
    line = table[yPos]
    currentX = 0
    inside = False
    for i in line:
        if xPos > currentX and xPos < currentX + i and inside == True:
                return "legit"
        if inside == False:
            inside = True
        else:
            inside = False
            currentX = currentX + i
    
def dataValidation(table, xPos, yPos):
    pass

def move(command, position):
    mf = [position[0], position[1]]
    if command == "w":
        mf[0] = mf[1] - 1
    if command == "d":
        mf[ = mf[0] + 1
    if command == "a":
        mf = mf[0] - 1
    if command == "s":
        mf = mf[1] + 1
    return mf

def drawBoard(multi_table, position):
    line_id = 0
    for x in multi_table:
        draw_line(x, line_id, position[0], position[1])
        line_id += 1
        
    print(dataValidation(multi_table, position[0], position[1]))

def draw_line(table, line_nr, xPos, yPos):
    cell_nr = 0
    line_string = ""
    inside = False
    for i in table:
        if inside == True:
            line_string += "|"
            for j in range(0,i):
                if cell_nr == xPos and line_nr == yPos:
                    line_string += "x|"
                    cell_nr += 1
                else:
                    line_string += "_|"
                    cell_nr += 1
            inside = False
            continue
        if inside == False:
            for j in range(0, 1):
                line_string += " "
                cell_nr += 1
            for j in range(0,i-1):
                line_string += "  "
                cell_nr += 1
            inside = True
    print(line_string)

tab = [[1,5,4,2], [4,3,1,4], [2,8,1,1], [1,1,1,1,8], [5,1,4,2]]
poz = [5,1]

drawBoard(tab, poz)

for i in range(0, 100):
    command = input("w/s/a/d:")
    newPosition = move(command, poz)
    if isMarkerAtLegitPosition(tab, newPosition[0], newPosition[1]) == "legit":
        poz = newPosition

    drawBoard(tab, poz)

