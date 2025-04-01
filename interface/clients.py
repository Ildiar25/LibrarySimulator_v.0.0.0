from rich.console import Console
from rich.table import box, Table

from app.library import Library
from shared.utilities import insert_number, insert_option, insert_text


def __show_clients(console: Console, client_list: list[dict[str, int | str]]) -> None:
    table = Table(width=150, box=box.DOUBLE_EDGE)

    table.title = "\n\n(📚) ~~~~~~~~~~ BIBLIOTECA ~~~~~~~~~~ (📚)"

    table.add_column("IDENTIFICADOR", style="cyan")
    table.add_column("NOMBRE")
    table.add_column("LIBROS PRESTADOS")

    for client in client_list:
        table.add_row(
            str(client["ident"]),
            f"{client['name']} {client['surname']}",
            f"{[str(isbn) for isbn in client['client_books']]}"
        )

    console.print(table)


def clients(console: Console, library: Library) -> None:
    running = True
    while running:
        library.load_clients()
        console.print("\n\n#################### Sección CLIENTES ####################",
                      style="italic", justify="center")

        console.print("\n[cyan] >>>>> [/cyan]Opciones disponibles:")
        console.print(
            " · 1) Nuevo cliente\n"
            " · 2) Editar cliente\n"
            " · 3) Eliminar cliente\n"
            " · 4) Mostrar clientes\n"
            " · 5) MENÚ PRINCIPAL\n"
        )

        answer = insert_option(console, "¿Qué quieres hacer?", ["1", "2", "3", "4", "5"])

        if answer == "1":
            # __new_client(console, library)
            pass

        elif answer == "2":
            # __update_client(console, library)
            pass

        elif answer == "3":
            # __delete_client(console, library)
            pass

        elif answer == "4":
            __show_clients(console, library.show_clients())

        elif answer == "5":
            running = False
            console.print("¡De acuerdo!")
