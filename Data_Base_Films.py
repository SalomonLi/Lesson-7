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


film_id_0 = Movie(title="The Flach", year= 2000, genres="cos")
film_id_1 = Movie(title="The Shawshank Redemption", year= 2000, genres="cos")
film_id_2 = Movie(title="The Godfather: Part I", year= 2000, genres="cos")
film_id_3 = Movie(title="The Godfather: Part II", year= 2000, genres="cos")
film_id_4 = Movie(title="Pulp Fiction", year= 2000, genres="cos")
film_id_5 = Movie(title="Star Wars", year= 2000, genres="cos")


serials = Selial(title="The Simpsons", year=1999, genres="cos", number_episode=1, number_seasons=18)

films = [film_id_0, serials, film_id_1, film_id_2, film_id_3, film_id_4, film_id_5]



def get_movies(values):
    rezultat = []
    for name in values:
        if isinstance(name, Selial) != True :
            rezultat.append(name)
    return sorted(rezultat, key= lambda films_id: films_id.title)



def get_serials(values):
    rezultat = []
    for name in values:
        if isinstance(name, Selial):
            rezultat.append(name)
    return sorted(rezultat, key= lambda films_id: films_id.title)

def search(values, object_type_class):
    rezultat = []
    for searching in values:
        for parser_class_obj in object_type_class:
            if str(searching).lower() in str(parser_class_obj).lower():
                rezultat.append(searching.title())
    return rezultat

def generate_views(object_types_list):
    random_values = random.choice(object_types_list)
    random_quantity = random.randint(1, 100)
    if isinstance(random_values, Movie):
        random_values.played = random_quantity
        return f'{random_values} Quantity = {random_values.played} '


def generate_views_loop(value = 0):
    for _ in range(0, value):
        generate_views(films)

def top_titles(values, top = 3, content_type = films or serials):

    top_sorted = sorted(values , key = lambda values : values.played)
    if top <= len(top_sorted):
        return top_sorted[:top]
    else:
        return top_sorted






print(get_movies(films))
print(get_serials(films))

# print(search(('Flach', 'Grezbi', "..."), serials))
print(search(('The Flach', 'Grezbi', "...", "the flach"), films))



generate_views(films)

generate_views_loop(10)


top_list = top_titles(films)
print(top_list)