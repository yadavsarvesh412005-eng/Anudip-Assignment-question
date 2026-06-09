# 8. Movie class and highest rated movie

class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

def highest_movie(movies):
    return max(movies, key=lambda m: m.rating)

m1 = Movie("Movie1", 8.2)
m2 = Movie("Movie2", 9.1)
m3 = Movie("Movie3", 7.8)

print("Best Movie:", highest_movie([m1, m2, m3]).name)
