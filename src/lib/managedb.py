import pathlib
import json


class ManageDB:
    __address_file = "{0}/pruebaSofkaCRUD/src/db/dbMovies.json".format(
        pathlib.Path().absolute()
    )

    def read_movies(self):
        with open(self.__address_file, "r") as data:
            return json.loads(data.read())

    def write_movie(self, new_movie):
        with open(self.__address_file, "w") as data:
            data.write(json.dumps(new_movie))
