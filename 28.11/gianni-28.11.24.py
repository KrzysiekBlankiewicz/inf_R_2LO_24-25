def isMarkerAtLegitPosition(table, xPos, yPos):
    if xPos < 0 or yPos < 0:
        return "wrong"
    line = table[yPos]
    cell_id = 0
    inside = False
    for i in line:
        if xPos >= cell_id and xPos < cell_id + i and inside == True:
            return "legit"
        cell_id += i
        if inside == True:
            inside = False
        else:
            inside = True
    return "wrong"

def dataValidation(table, xPos, yPos):
    first_line = table[0]
    line_len = sum(first_line)
    line_id = 0
    for line in table:
        if sum(line) != line_len:
            return "wrong"
        line_id += 1

    if isMarkerAtLegitPosition(table, xPos, yPos) == "wrong":
        return "wrong"
    
    return "legit"

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

def move(command, position):
    if command == "w":
        newY = position[1] - 1
    if command == "s":
        newY = position[1] + 1
    if command == "a":
        newX = position[0] - 1
    if command == "d":
        newX = position[0] + 1

    return (newX, newY)

tab = [[1,5,4,2], [4,3,1,4], [2,8,1,1], [1,1,1,1,8], [5,1,4,2]]
poz = [5,1]

drawBoard(tab, poz)

for i in range(0, 100):
    command = input("w/s/a/d:")
    newPosition = move(command, poz)
    if isMarkerAtLegitPosition(tab, newPosition[0], newPosition[1]) == "legit":
        poz = newPosition

    drawBoard(tab, poz)
