import random
class team:
    def __init__(self, name):
        self.name = name
        self.pkt = 0
        self.bil = 0
    def rezultat(self, d_pkt, d_bil):
        self.pkt += d_pkt
        self.bil += d_bil
def gra(team1, team2):
    score1 = random.randint(0, 6)
    score2 = random.randint(0, 6)
    if score1 > score2:
        team1.rezultat(3, score1-score2)
        team2.rezultat(0, score2-score1)
    elif score2 > score1:
        team1.rezultat(0, score1-score2)
        team2.rezultat(3, score2-score1)
    else:
        team1.rezultat(1, 0)
        team2.rezultat(1, 0)
def sortujw(tablica):
    for i in range(1, len(tablica)):
        v = tablica[i]
        j = i
        while j > 0 and v.pkt < tablica[j-1].pkt:
            tablica[j] = tablica[j-1]
            j = j-1
        tablica[j] = v
    return tablica
a = team("Lech")
b = team("Raków")
c = team("Jagielonia")
d = team("Pogoń")
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
