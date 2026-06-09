#Create a class that works with len() (__len__)
class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)

t = Team(["Ram", "Shyam", "Mohan"])

print(len(t))