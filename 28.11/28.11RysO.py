def isMarkerAtLegitPosition(table, xPos, yPos):
    row = table[yPos]
    currentX = 0
    inside = False
    for i in row:
        if xPos >= currentX and xPos < currentX + i and inside == True:
            return "legit"
        if inside == False:
            inside = True
        else:
            inside = False
        currentX = currentX + i
    return "error"

def dataValidation(table, xPos, yPos):
    return "legit"

def move(command, position):
    x = poz[0]
    y = poz[1]
    if command == "w":
        y = y-1
    if command == "s":
        y = y+1
    if command == "a":
        x = x-1
    if command == "d":
        x = x+1
    return (x,y)

def drawBoard(multi_table, position):
    line_id = 0
    for x in multi_table:
        draw_line(x, line_id, position[0], position[1])
        line_id += 1

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

tab = [[1,5,4,2], [4,3,1,4], [2,8,1,1], [1,1,1,1,8], [1,3,1,3]]
poz = [5,2]

drawBoard(tab, poz)

for i in range(0, 100):
    command = input("w/s/a/d:")
    newPosition = move(command, poz)
    if isMarkerAtLegitPosition(tab, newPosition[0], newPosition[1]) == "legit":
        poz = newPosition

    drawBoard(tab, poz)
