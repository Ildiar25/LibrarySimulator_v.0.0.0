from pathlib import Path
from typing import Any
import json
import os


class FileManager:
    def __init__(self, data: list[dict[str, str | int]] | None = None) -> None:
        self.data = data

    @classmethod
    def create_file(cls, filename: str) -> None:
        if not os.path.exists(Path(__file__).parent.joinpath("database")):
            os.makedirs(Path(__file__).parent.joinpath("database"))

        try:
            open(Path(__file__).parent.joinpath(f"database/{filename}"), "x").close()

        except PermissionError as not_allowed:
            print(
                f"\n[{type(not_allowed).__name__}] #### ¡No se tienen permisos para crear el archivo {repr(filename)}!"
            )
        except FileExistsError as already_exists:
            print(f"\n[{type(already_exists).__name__}] #### ¡El archivo {repr(filename)} ya existe!")
        except Exception as unknown:
            print(
                f"\n[{type(unknown).__name__}] #### "
                f"¡Ha ocurrido un error al tratar de crear el archivo {repr(filename)}!"
            )

    @classmethod
    def load_data(cls, filename: str) -> "FileManager":
        data_dict = {"data": []}

        try:
            with open(Path(__file__).parent.joinpath(f"database/{filename}"), "r", encoding="utf-8") as data_file:
                json_data = json.load(data_file)

        except FileNotFoundError as not_found:
            print(f"\n[{type(not_found).__name__}] #### ¡No se ha encontrado el archivo {repr(filename)}!")
        except Exception as unknown:
            print(
                f"\n[{type(unknown).__name__}] #### "
                f"¡Ha ocurrido un error al tratar de cargar el archivo {repr(filename)}!"
            )

        else:
            data_dict = json_data

        return cls(data_dict["data"])

    @classmethod
    def save_data(cls, data: list[dict[str, str | int]], filename: str) -> None:
        pass


def main():
    test = FileManager.load_data("clients.json")
    for dic in test.data:

        print(dic["ident"])


if __name__ == '__main__':
    main()

