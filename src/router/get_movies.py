from src.lib.managedb import ManageDB
from fastapi import HTTPException

md = ManageDB()


def get_movies():
    return md.read_movies()


def get_movie(id_movie: str):
    movies = md.read_movies()

    for movie in movies:

        if movie["id"] == id_movie:
            return movie

    raise HTTPException(status_code=404, detail="movie not found")
