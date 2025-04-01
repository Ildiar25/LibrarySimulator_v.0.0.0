from rich.console import Console
from rich.table import box, Table

from app.library import Library
from shared.utilities import insert_number, insert_option, insert_text


def requests(console: Console, library: Library) -> None:
    running = True
    while running:
        library.load_books()
        library.load_clients()
        console.print("\n\n#################### Sección SOLICITUDES ####################",
                      style="italic", justify="center")

        console.print("\n[cyan] >>>>> [/cyan]Opciones disponibles:")
        console.print(
            " · 1) Devolución\n"
            " · 2) Préstamo\n"
            " · 3) Reserva\n"
            " · 4) MENÚ PRINCIPAL\n"
        )

        answer = insert_option(console, "¿Qué quieres hacer?", ["1", "2", "3", "4"])

        if answer == "1":
            pass

        elif answer == "2":
            pass

        elif answer == "3":
            pass

        elif answer == "4":
            running = False
            console.print("¡De acuerdo!")
