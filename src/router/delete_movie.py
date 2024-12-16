from src.lib.managedb import ManageDB
from fastapi import HTTPException

md = ManageDB()


def delete_movie(id_movie: str):
    movies = md.read_movies()

    for index, movie in enumerate(movies):

        if movie["id"] == id_movie:
            movies.pop(index)
            md.write_movie(movies)
            return {"success": True, "message": "delete movie to the catalog"}

    raise HTTPException(status_code=404, detail="Movie not found")
