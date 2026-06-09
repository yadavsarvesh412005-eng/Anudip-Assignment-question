# 9. Player class and leaderboard

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def leaderboard(players):
    return sorted(players, key=lambda p: p.score, reverse=True)

pl1 = Player("Rohit", 120)
pl2 = Player("Virat", 150)
pl3 = Player("Gill", 100)

for p in leaderboard([pl1, pl2, pl3]):
    print(p.name, p.score)