from rich.console import Console
from rich.table import box, Table

from app.library import Library

from .books import books
from .clients import clients


def __create_table() -> Table:
    table = Table(width=150, box=box.DOUBLE_EDGE)

    table.title = "\n\n____________________ Secciones Disponibles ____________________"
    table.add_column("LIBROS 📚", style="magenta")
    table.add_column("CLIENTES 👥", style="magenta")
    table.add_column("SOLICITUD 📰", style="magenta")
    table.add_column("SALIR 👋", style="magenta")

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
        console.print("\n¿Qué sección deseas visitar?")
        answer = console.input("[cyan]>>> ").upper()

        if answer == "LIBROS":
            books(console, library)

        elif answer == "CLIENTES":
            clients(console, library)

        elif answer == "SOLICITUD":
            # requests()
            pass
        elif answer == "SALIR":
            running = False

        else:
            console.print(f"[bright_red]Lo siento, [b]{repr(answer)}[/b] no es un comando válido.")

def main():
    main_menu()


if __name__ == '__main__':
    main()
