from rich.console import Console
from rich.table import box, Table

from app.library import Library
from shared.utilities import insert_option

def __show_books(console: Console, book_list: list[dict[str, int | str]]) -> None:
    table = Table(width=150, box=box.DOUBLE_EDGE)

    table.title = "____________________ LIBROS ____________________"

    table.add_column("ISBN", style="cyan")
    table.add_column("TÍTULO")
    table.add_column("AUTOR")
    table.add_column("GÉNERO")
    table.add_column("ESTADO", style="cyan")

    for book in book_list:
        table.add_row(
            str(book["isbn"]),
            book["title"],
            book["author"],
            book["genre"],
            book["status"],
        )

    console.print(table)
    console.print("\n\n")


def books(console: Console, library: Library) -> None:
    running = True
    while running:

        library.load_books()
        console.print("____________________ Sección LIBROS ____________________",
                      style="italic", justify="center")

        console.print("\n[cyan] >>>>> [/cyan]Opciones disponibles:")
        console.print(
            " · 1) Nuevo libro\n"
            " · 2) Editar libro\n"
            " · 3) Eliminar libro\n"
            " · 4) Mostrar libros\n"
            " · 5) ATRÁS\n"
        )

        answer = insert_option(console, "¿Qué quieres hacer?", ["1", "2", "3", "4", "5"])

        if answer == "1":
            # __new_book()
            pass

        elif answer == "2":
            # __delete_book()
            pass

        elif answer == "3":
            # __update_book()
            pass

        elif answer == "4":
            __show_books(console, library.show_books())

        elif answer == "5":
            running = False
            print("¡De acuerdo!")
