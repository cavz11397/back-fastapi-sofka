from src.lib.managedb import ManageDB
from fastapi import HTTPException
from src.models.movie_model import MovieModel


md = ManageDB()


def put_movie(id_movie: str, new_movie: MovieModel):
    movies = md.read_movies()

    for index, movie in enumerate(movies):

        if movie["id"] == id_movie:
            movies[index] = new_movie.model_dump()

            if new_movie.name == "":
                movies[index]["name"] = movie["name"]

            if new_movie.genre == "":
                movies[index]["genre"] = movie["genre"]

            md.write_movie(movies)
            return {"success": True, "message": "update movie to the catalog"}
    raise HTTPException(status_code=404, detail="Movie not found")
