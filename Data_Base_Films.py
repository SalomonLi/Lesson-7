


class Movie():
    def __init__(self, title, year, genres, rating = 0):
        self.title = title
        self.year = year
        self.genres = genres
        self.rating = rating

    def play(self):
        self.rating += 1


    def __str__(self):
        return f'{self.title} ({self.year})'

class Selial(Movie):
    def __init__(self, number_episode, number_seasons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_episode = number_episode
        self.number_seasons = number_seasons


    # Decorator !!!!!
    def __str__(self):
        if self.number_seasons < 9 and self.number_episode < 9:
            return f'{self.title} S0{self.number_seasons}E0{self.number_episode}'

        elif self.number_seasons < 9 and self.number_episode > 9:

            return f'{self.title} S0{self.number_seasons}E{self.number_episode}'

        elif self.number_seasons > 9 and self.number_episode < 9:

            return f'{self.title} S{self.number_seasons}E0{self.number_episode}'

        else:
            return f'{self.title} S{self.number_seasons}E{self.number_episode}'



film = Movie(title="Flach", year= 2000, genres="cos")

print(film.rating)

for i in range(0,6):
    film.play()

print(film.rating)

serials = Selial(title="The Simpsons", year=1999, genres="cos", number_episode=1, number_seasons=10)

print(film)
print(serials)
