import random

class Team:
    def __init__(self, name):
        self.name = name
        self.pts = 0
        self. bilans = 0

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

a = Team("Jeden")
b = Team("Dwa")
c = Team("Trzy")

