
def isMarkerAtLegitPosition(table, xPos, yPos):
	row = table[yPos]
	cur_x = 0
	fill = False
	for i in row:
		if xPos >= cur_x and xPos < cur_x + i and fill == True:
			return "legit"
		cur_x = cur_x + i
		if fill == False:
			fill = True
		if fill == True:
			fill = False
	return "bad"
	
def dataValidation(tab, xPos, yPos):
	first_line = tab[0]
	line_len = sum(first_line)
	line_id = 0
	for line in tab:
		if sum(line) != line_len:
			return "bad"
		line_id += 1


def move(command, position):
	xpos = position[0]
	ypos = position[1]
	if command == "w":
		ypos = position[1] - 1
	if command == "s":
		ypos = position[1] + 1
	if command == "a":
		xpos = position[0] - 1
	if command == "d":
		xpos = position[0] + 1
	return (xpos, ypos)
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
	if command == 'x':
		break
	newPosition = move(command, poz)
	if isMarkerAtLegitPosition(tab, newPosition[0], newPosition[1]) == "legit":
		poz = newPosition


	drawBoard(tab, poz)
