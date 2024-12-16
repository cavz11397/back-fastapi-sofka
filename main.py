from fastapi import FastAPI

from src.router.get_movies import get_movies, get_movie
from src.router.post_movie import post_movie
from src.router.put_movie import put_movie
from src.router.delete_movie import delete_movie
from src.models.movie_model import MovieModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de orígenes permitidos
origins = [
    "http://localhost:4200",  # Frontend Angular
    "http://127.0.0.1:4200",  # Otras variaciones si usas localhost
]

# Agregar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,  # Permitir cookies/autenticación
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todas las cabeceras
)


@app.get("/")
def root():
    return {"message": "HI fastapi"}


@app.get("/api/movies")
def get_all_movies():
    return get_movies()


@app.get("/api/movies/{id_movie}")
def get_movie_for_id(id_movie: str):
    return get_movie(id_movie)


@app.post("/api/movies")
def add_movie(new_movie: MovieModel):
    return post_movie(new_movie)


@app.put("/api/movies")
def update_movie(id_movie: str, new_movie: MovieModel):
    return put_movie(id_movie, new_movie)


@app.delete("/api/movies/{id_movie}")
def remove_movie(id_movie: str):
    return delete_movie(id_movie)
