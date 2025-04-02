from rich.console import Console
from rich.table import box, Table

from app.library import Library
from shared.utilities import insert_option

from .books import books
from .clients import clients
from .requests import requests


def __create_table() -> Table:
    table = Table(width=150, box=box.DOUBLE_EDGE)

    table.title = "\n\n____________________ Secciones Disponibles ____________________"
    table.add_column("(1) LIBROS 📚", style="magenta")
    table.add_column("(2) CLIENTES 👥", style="magenta")
    table.add_column("(3) SOLICITUDES 📰", style="magenta")
    table.add_column("(4) SALIR 👋", style="magenta")

    table.add_row(
        "Permite trabajar en la sección de libros. Puedes añadir, editar o eliminar entradas.",
        "Permite trabajar en la sección de clientes. Puedes añadir, editar o eliminar usuarios.",
        "Permite trabajar con la base de datos para realizar solicitudes CRUD.",
        "Comando para salir de la aplicación."
    )

    return table


def main_menu() -> None:
    console = Console(width=150)
    library = Library()

    main_table = __create_table()

    running = True

    while running:
        console.print(main_table)
        answer = insert_option(console,"\n [cyan]>>>>>[/cyan] ¿Qué sección deseas visitar?", ["1", "2", "3", "4"])

        if answer == "1":
            books(console, library)

        elif answer == "2":
            clients(console, library)

        elif answer == "3":
            requests(console, library)

        elif answer == "4":
            running = False

def main():
    main_menu()


if __name__ == '__main__':
    main()
