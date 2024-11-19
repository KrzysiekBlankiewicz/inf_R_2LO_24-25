

def drawBoard(board):
    for row in board:
        string = ""
        for elem in row:
            if elem == 0:
                string = string + "_"
            if elem == 1:
                string = string + "x"
        print(string)


def drawBoard2(board, size):
    for row in board:
        string = ""
        for i in range(0, row[0]):
            string = string + "_"
        for j in range(row[0], row[1]):
            string = string + "x"
        for k in range(row[1], size):
            string = string + "_"
        print(string)
    
tab1 = [[0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

drawBoard(tab1)

print("")

tab2 = [[2, 4],
        [2, 5],
        [1, 5],
        [2, 4],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]]

drawBoard2(tab2, 8)
