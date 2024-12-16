from uuid import uuid4 as uuid
from pydantic import BaseModel


class MovieModel(BaseModel):
    id: str = str(uuid())
    name: str = ""
    genre: str = ""
