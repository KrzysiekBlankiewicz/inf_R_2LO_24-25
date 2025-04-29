import random 

class Team:
    def __init__(self, name):
        self.name = name
        self.pts = 0
        self.bilans = 0

    def result(self, d_pts, d_bilans):
        self.pts += d_pts
        self.bilans += d_bilans


def mecz(a, b):
    wynik1 = random.randint(0, 5)
    wynik2 = random.randint(0, 5)
   
    if wynik1 > wynik2:
        a.result(3, wynik1 - wynik2)
        b.result(0, wynik2 - wynik1)
    elif wynik1 < wynik2:
        a.result(0, wynik1 - wynik2)
        b.result(3, wynik2 - wynik1)
    else:
        a.result(1, 0)
        b.result(1, 0)


def SortW(tabela):
    for i in range(1, len(tabela)):
        v = tabela[i]
        j = i
       
        while j > 0 and (tabela[j - 1].pts < v.pts or (tabela[j - 1].pts == v.pts and tabela[j - 1].bilans < v.bilans)):
            tabela[j] = tabela[j - 1]
            j -= 1
       
        tabela[j] = v
    return tabela


a = Team("Jerze")
b = Team("Juleczki")
c = Team("Hubisy")
d = Team("Rysie")

tabela = [a, b, c, d]

mecz(a, b)
mecz(c, d)
mecz(a, c)
mecz(b, d)
mecz(a, d)
mecz(b, c)

tabela = SortW(tabela)

for team in tabela:
    print(team.name, team.pts, team.bilans)
