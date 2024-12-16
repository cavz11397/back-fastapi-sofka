from src.lib.managedb import ManageDB
from src.models.movie_model import MovieModel

md = ManageDB()


def post_movie(new_movie: MovieModel):
    movies = md.read_movies()
    new_movie = new_movie.model_dump()
    movies.append(new_movie)
    md.write_movie(movies)
    return {"success": True, "message": "added new movie to the catalog"}
