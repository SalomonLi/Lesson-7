class Movie():
    def __init__(self, title, year, genres, played = 0):
        self.title = title
        self.year = year
        self.genres = genres
        self.played = played

    def play(self):
        self.played += 1


    def __str__(self):
        return f'{self.title} ({self.year})'

class Selial(Movie):
    def __init__(self, number_episode, number_seasons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_episode = number_episode
        self.number_seasons = number_seasons


    def __str__(self):
        return f'{self.title} S{self.number_seasons:0>2}E{self.number_episode:0>2}'


film = Movie(title="Flach", year= 2000, genres="cos")

print(film.played)

for i in range(0,6):
    film.play()

print(film.played)

serials = Selial(title="The Simpsons", year=1999, genres="cos", number_episode=1, number_seasons=18)

print(film)
print(serials)
