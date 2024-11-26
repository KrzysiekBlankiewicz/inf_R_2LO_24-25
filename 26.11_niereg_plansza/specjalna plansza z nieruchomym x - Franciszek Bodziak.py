
def draw_line(tablica):
    x = 1
    linia = ""
    wewn = False
    for i in tablica:
        if wewn == True:
            linia += "|"
            for j in range(0,i):
                if x == posX and y == posY:
                    linia +="x|"
                    x = 999
                else:
                    linia += "_|"
                    x = x+1
            wewn = False
            linia += " "
            continue
        if wewn == False:
            for j in range(0,i-1):
                    linia += "  "
            wewn = True
            x = x+1
    print(linia)



            

tab = [[5,1,4,2], [4,3,1,5], [2,8,1,4], [5,1,4,2]]
posX = 5
posY = 3
y = 1

for c in tab:
    draw_line(c)
    y = y+1
