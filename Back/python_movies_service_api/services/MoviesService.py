from repositories.MoviesRepository import MoviesRepository

class MoviesService(object):
    def __init__(self):
        self.movies_repository = MoviesRepository()

    def add_movie(self, name, description, stars, year):
        return self.movies_repository.add_movie(name, description, stars, year)

    def get_all_movies(self, page, pagesize, name):
        print("...service....name: " +name)
        return self.movies_repository.get_all_movies(page, pagesize, name)

    def get_movie_by_id(self, id):
        return self.movies_repository.get_movie_by_id(id)

    def update_movie(self, id, name, description, stars, year):
        return self.movies_repository.update_movie(id, name, description, stars, year)

    def delete_movie(self, id):
        return self.movies_repository.delete_movie(id)