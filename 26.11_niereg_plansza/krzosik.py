
def draw_line(tablica, px, py):
    ly = 0
    linia = ""
    wewn = False
    for i in tablica:
        if wewn == True:
            linia += "|"
            for j in range(0,i):
                if j== px and ly == py:
                    linia += "x|"
                else:
                    linia += "_|"
            wewn = False
            continue
        if wewn == False:
            for j in range(0, 1):
                linia += " "
            for j in range(0,i-1):
                linia += "  "
            wewn = True
        ly = ly+1
    print(linia)

tab = [[5,1,4,2], [4,3,1,5], [2,8,1,4], [1,1,1,1,1,], [5,1,4,2]]

poz = [1,1]
pozx = input("podaj pozycję x")
pozy = input("podaj pozycję y")
poz[0] = pozx
poz[1] = pozy

for x in tab:
    draw_line(x, pozx, pozy)
