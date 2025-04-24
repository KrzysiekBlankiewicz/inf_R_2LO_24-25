import random

class Team:
    def __init__(self, name):
        self.name = name
        self.pts = 0
        self.bilans = 0

    def result(self, d_pts, d_bilans):
        self.pts += d_pts
        self.bilans += d_bilans

def game(team1, team2):
    score1 = random.randint(0, 6)
    score2 = random.randint(0, 6)
    if score1 > score2:
        team1.result(3, score1-score2)
        team2.result(0, score2-score1)
    elif score2 > score1:
        team1.result(0, score1-score2)
        team2.result(3, score2-score1)
    else:
        team1.result(1, 0)
        team2.result(1, 0)

def sortW(tablica):
    for i in range(1, len(tablica)):
        v = tablica[i]
        j = i
        while j > 0 and v.pts < tablica[j-1].pts:
            tablica[j] = tablica[j-1]
            j = j-1
        tablica[j] = v
    return tablica

a = Team("Piast")
b = Team("Termalika")
c = Team("Arka")
d = Team("Motor")
tab = [a, b, c, d]

game(a, b)
game(c, d)
game(a, c)
game(b, d)
game(a, d)
game(c, b)

result = sortW(tab)
for t in result:
    print(t.name, t.pts)

