def daszki_pierwszej_lini(tablica):
    linia = ""
    rysuj_daszki = False
    for i in tablica: # i => przyjmuje kolejne elementow tablicy
        if rysuj_daszki == True:
            linia += " "
            for j in range(0,i):
                linia += "_ "
            rysuj_daszki = False
        elif rysuj_daszki == False:
            
            for j in range(0,i):
                linia += "  "
            rysuj_daszki = True
    print(linia)        

def draw_line(tablica):
    linia = ""
    rysuj_pola = False # false => rysuj puste pola; true => rysuj pola 
    for i in tablica:
        if rysuj_pola == True:
            linia += "|"
            for j in range(0,i):
                linia += "_|"
            rysuj_pola = False          
        elif rysuj_pola == False:
            for j in range(0,i):
                linia += "  "
            rysuj_pola = True
    print(linia)

tab = [0,3,5,1,4,2]

wyglad_planszy = [[2, 1, 3, 7],[4, 1, 2, 3],[3, 3, 3, 3]]



daszki_pierwszej_lini(wyglad_planszy[0])


for wiersz in wyglad_planszy:
    draw_line(wiersz)


