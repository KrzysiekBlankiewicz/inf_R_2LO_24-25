
def draw_line(tablica):
    linia = ""
    wewn = False
    for i in tab:
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

tab = [5,1,4,2]
draw_line(tab)
