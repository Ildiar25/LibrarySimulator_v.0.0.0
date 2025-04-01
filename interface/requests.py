from rich.console import Console
from rich.table import box, Table

from app.library import Library
from shared.utilities import insert_dni, insert_number, insert_option
from shared.types import BookDict, ClientDict


def __return_book(console: Console, library: Library) -> None:
    isbn_list = [book["isbn"] for book in library.show_books()]
    ident_list = [client["ident"] for client in library.show_clients()]

    console.print("\n(🟦) ~~~~~~~~~~ Devolución ~~~~~~~~~~ (🟦)", style="italic", justify="center")
    console.print(
        "\nPara realizar una devolución se deben disponer de los siguientes datos:\n"
        " · [green][b]DNI[/b][/green] del cliente que solicita la petición\n"
        " · El [green][b]ISBN[/b][/green] del libro a devolver."
    )

    console.print("\n[cyan]Primero vamos a seleccionar al cliente mediante su DNI:")
    ident = insert_dni(console)
    if ident is None:
        console.print("¡De acuerdo!")
        return

    if ident not in ident_list:
        console.print("\n[bright_red]¡Ese DNI no pertenece a ningún cliente registrado en esta biblioteca!\n")
        return

    client = __look_for_client(console, library, ident)

    if not client["client_books"]:
        console.print("Lo siento, este cliente no tiene libros que devolver.")
        return

    __show_client_books(console, client)

    console.print("\n[cyan]Ahora el ISBN del libro a devolver:")
    isbn = insert_number(console, 9)

    if isbn is None:
        console.print("¡De acuerdo!")
        return

    if isbn not in isbn_list:
        console.print("\n[bright_red]¡Ese ISBN no pertenece a ningún libro registrado en esta biblioteca!\n")
        return

    book = __look_for_book(console, library, isbn)
    library.add_book(book)

    answer = insert_option(
        console,
        f"[cyan] >>>>> [/cyan]¿Quieres devolver {book['title']}?",
        ["S", "N"]
    )
    if answer == "S":
        __update_client_book_list(client, isbn)
        library.add_client(client)
        library.return_book(isbn)
        library.save_clients()
        library.save_books()

    console.print("¡De acuerdo!")

# def __lend_book(console: Console, library: Library) -> None:
#     pass

# def __reserve_book(console: Console, library: Library) -> None:
#     pass

def __show_client_books(console: Console, client: ClientDict) -> None:
    table = Table(width=150, box=box.DOUBLE_EDGE)
    table.title = f"\n__________ Libros Prestados a {client['name']} __________"
    table.add_column("ISBN", style="cyan")
    table.add_column("TÍTULO")

    for book in client["client_books"]:
        table.add_row(
            str(book["isbn"]),
            book["title"]
        )

    console.print(table)


def __look_for_client(console: Console, library: Library, ident: str) -> ClientDict | None:
    try:
        client = library.look_for_client(ident)
        return client

    except ValueError as no_exists:
        console.print(f"\n[bright_red]¡{no_exists}!")


def __look_for_book(console: Console, library: Library, isbn: int) -> BookDict | None:
    try:
        client = library.look_for_book(isbn)
        return client

    except ValueError as no_exists:
        console.print(f"\n[bright_red]¡{no_exists}!")


def __update_client_book_list(client: ClientDict, isbn: int) -> None:
    new_book_client_list = []
    for book in client["client_books"]:
        if book["isbn"] != isbn:
            new_book_client_list.append(book)
    client["client_books"] = new_book_client_list


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
            __return_book(console, library)

        elif answer == "2":
            # __lend_book(console, library)
            pass

        elif answer == "3":
            # __reserve_book(console, library)
            pass

        elif answer == "4":
            running = False
            console.print("¡De acuerdo!")
