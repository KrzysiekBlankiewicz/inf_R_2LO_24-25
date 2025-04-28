import random
class Drużyna:
    def __init__(self, name):
        self.name = name
        self.pkt = 0
        self.bilans = 0
    def rezultat(self, d_pkt, d_bilans):
        self.pkt += d_pkt
        self.bilans += d_bilans
def gra(Drużyna1, Drużyna2):
    score1 = random.randint(0, 6)
    score2 = random.randint(0, 6)
    if score1 > score2:
        Drużyna1.rezultat(3, score1-score2)
        Drużyna2.rezultat(0, score2-score1)
    elif score2 > score1:
        Drużyna1.rezultat(0, score1-score2)
        Drużyna2.rezultat(3, score2-score1)
    else:
        Drużyna1.rezultat(1, 0)
        Drużyna2.rezultat(1, 0)
def sortujW(tablica):
    for i in range(1, len(tablica)):
        v = tablica[i]
        j = i
        while j > 0 and v.pkt < tablica[j-1].pkt:
            tablica[j] = tablica[j-1]
            j = j-1
        tablica[j] = v
    return tablica
a = Drużyna("DR1")
b = Drużyna("DR2")
c = Drużyna("DR3")
d = Drużyna("DR4")
tab = [a, b, c, d]
gra(a, b)
gra(c, d)
gra(a, c)
gra(b, d)
gra(a, d)
gra(c, b)
rezultat = sortujW(tab)
for t in rezultat:
    print(t.name, t.pkt)
