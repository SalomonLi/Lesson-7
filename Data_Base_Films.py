import random

class Movie:
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
    def __init__(self,number_episode, number_seasons, title, year, genres, played = 0, *args, **kwargs):
        super().__init__(title, year, genres,played = 0,)
        self.title = title
        self.year = year
        self.genres = genres
        self.played = played
        self.number_episode = number_episode
        self.number_seasons = number_seasons


    def __str__(self):
        return f'{self.title} S{self.number_seasons:0>3}E{self.number_episode:0>2}'


film = Movie(title="Flach", year= 2000, genres="cos")

print(film.played)

for i in range(0,6):
    film.play()

print(film.played)

serials = Selial(title="The Simpsons", year=1999, genres="cos", number_episode=1, number_seasons=18)

print(film)
print(serials)

x = str(serials)
#
# print(type(x))
# print(x)
def get_movies(values):
    rezultat = []
    if isinstance(values, Selial) != True :
        rezultat.append(str(values))
        return rezultat



def get_serials(values):
    rezultat = []
    if isinstance(values, Selial):
        rezultat.append(str(values))
        return rezultat

def search(values, object):
    rezultat = []
    for searching in values:
        if str(searching).lower() in str(object).lower():
            rezultat.append(searching.title())
    return rezultat

def generate_views(object):
    x = random.choice(object)
    if isinstance(x, Movie):
        return x.title

def top_titles(*content_type):
    # nie wiem jak to zric
    pass




# x = get_movies(film)
# print(x)
# x = get_movies(serials)
# print(x)

print(get_movies(film))
print(get_movies(serials))

print(get_serials(film))
print(get_serials(serials))

# print(search(('Flach', 'Grezbi', "..."), serials))
print(search(('Flach', 'Grezbi', "...", "flach"), film))

x = (film, serials)

print(generate_views(x))