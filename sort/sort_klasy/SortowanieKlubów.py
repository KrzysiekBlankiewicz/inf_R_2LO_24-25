import random
class Teams:
      def __init__(self, name):
            self.name = name
            self.pts = 0
            self.bilans = 0
      def result(self,d_pts,d_bilans):
            self.pts += d_pts
            self.bilans += d_bilans
def Game(t1, t2):
    wynik1 = random.randint(0,3)
    wynik2 = random.randint(0,3)
    if wynik1 > wynik2:
        t1.result(3,wynik1 - wynik2)
        t2.result(0,wynik2 - wynik1)
    elif wynik1 == wynik2:
        t1.result(1,0)
        t2.result(1,0)
    elif wynik1 < wynik2:
        t1.result(0,wynik1 - wynik2)
        t2.result(3,wynik2 - wynik2)

def sortW(tablica):
    for i in range(1, len(tablica)):
        v = tablica[i]
        j = i
        while j>0 and v.pts > tablica[j-1].pts:
            if v.bilans < tablica[j-1].bilans:  
                None
            elif v.bilans > tablica[j-1].bilans:
                tablica[j] = tablica[j-1]
                j = j-1
        tablica[j] = v
    return tablica
a = Teams("FC Forts")
b = Teams("PKS Radziwilow")
c = Teams("FV Rad")
d = Teams("FC Hormigon")
tab = [a,b,c,d]
Game(a,b)
Game(c,d)
Game(a,c)
Game(d,b)
Game(a,d)
Game(c,b)
result = sortW(tab)
for t in result:
    print(t.name, t.pts, t.bilans)
# Do kodu sortowania dodalem mozliwosc sortowania tez przez bilans jezeli punkty sa takie same 
# P.S. To czasami dziala jak chce i nie wiem dlaczego, probowalem zrozumiec ten blad ale nic mi nie wyswietla.
