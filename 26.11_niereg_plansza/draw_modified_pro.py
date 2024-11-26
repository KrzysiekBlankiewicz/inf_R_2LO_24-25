
def draw_line(tablica):
    linia = ""
    wewn = False
    for i in tablica:
        if wewn == True:
            linia += "|"
            for j in range(0,i):
                linia += "_|"
            wewn = False
            continue
        if wewn == False:
            for j in range(0,i):
                linia += "  "
            wewn = True
    print(linia)

tab = [[5,1,4,2], [4,3,1,5], [2,8,1,4], [5,1,4,2]]

for x in tab:
    draw_line(x)
