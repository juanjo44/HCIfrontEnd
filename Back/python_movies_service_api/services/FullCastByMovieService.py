from repositories.FullCastByMovieRepository import FullCastByMovieRepository

class FullCastByMovieService(object):
    def __init__(self):
        self.full_cast_by_movie_repository = FullCastByMovieRepository()

    def add_full_cast_by_movie(self, id_person, id_role, id_movie, character):
        return self.full_cast_by_movie_repository.add_full_cast_by_movie(id_person, id_role, id_movie, character)

    def get_all_full_cast_by_movie(self, page, pagesize,characte):
        print("...fullcast....name: " +character)
        return self.full_cast_by_movie_repository.get_all_full_cast_by_movie(page, pagesize, character)

    def get_full_cast_by_movie_by_id(self, id):
        return self.full_cast_by_movie_repository.get_full_cast_by_movie_by_id(id)

    def update_full_cast_by_movie(self, id, name):
        return self.full_cast_by_movie_repository.update_full_cast_by_movie(id, id_person, id_role, id_movie, character)

    def delete_full_cast_by_movie(self, id):
        return self.full_cast_by_movie_repository.delete_full_cast_by_movie(id)