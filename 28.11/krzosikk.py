
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
    return "no legit"
    
def dataValidation(table, xPos, yPos):
    first_line = table[0]
    line_len = sum(first_line)
    line_id = 0
    for line in table:
        if sum(line) != line_len:
            return "wrong"
        line_id += 1

def move(command, position):
    position_modified = [position[0], position[1]]
    if command == "d":
        position_modified[0] = position_modified[0] + 1
    if command == "s":
        position_modified[1] = position_modified[1] + 1
    if command == "a":
        position_modified[0] = position_modified[0] - 1
    if command == "w":
        position_modified[1] = position_modified[1] - 1
    return position_modified

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

