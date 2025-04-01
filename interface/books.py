from rich.console import Console
from rich.table import box, Table

from app.library import Library
from shared.utilities import insert_number, insert_option, insert_text


def __new_book(console: Console, library: Library) -> None:
    isbn_list = [book["isbn"] for book in library.show_books()]

    console.print("\n(📗) ~~~~~~~~~~ Añadir Libro ~~~~~~~~~~ (📗)", style="italic", justify="center")
    console.print(
        "\nPara agregar un nuevo libro a la biblioteca se deben disponer de los siguientes datos:\n"
        " · [green][b]ISBN[/b][/green] del libro a agregar\n"
        " · El [green][b]título[/b][/green] del mismo\n"
        " · El nombre de su [green][b]autor[/b][/green]\n"
        " · Y el [green][b]género[/b][/green] al que pertenece."
    )
    console.print("\n[cyan]Primero vamos a comprobar si el ISBN que se va a introducir existe:")

    isbn = insert_number(console, 9)

    if isbn is None:
        console.print("¡De acuerdo!")
        return

    if isbn in isbn_list:
        console.print("\n[bright_red]¡No se puede agregar un ISBN que ya existe!\n")
        return

    console.print(
        "\n¡Perfecto!\n"
        "A partir de ahora, simplemente rellena los campos. No te preocupes si te equivocas.\n"
        "¡Más adelante podrás modificar los datos del libro!\n"
        "\n[cyan][b]TÍTULO:"
    )
    title = insert_text(console, 5, 250)
    console.print("\n[cyan][b]AUTOR:")
    author = insert_text(console, 5, 150)
    console.print("\n[cyan][b]GÉNERO:")
    genre = insert_text(console, 5, 20)

    library.add_book(
        {
            "isbn": isbn,
            "title": title,
            "author": author,
            "genre": genre,
            "status": "disponible"
        }
    )
    library.save_books()
    console.print("[green]✔️ ¡Libro Añadido!\n")


def __update_book(console: Console, library: Library) -> None:
    isbn_list = [book["isbn"] for book in library.show_books()]

    console.print("\n(✏️) ~~~~~~~~~~ Editar Libro ~~~~~~~~~~ (✏️)", style="italic", justify="center")
    console.print(
        "\nPara modificar un libro de la biblioteca es necesario aportar un número [green][b]ISBN[/b][/green]."
    )

    isbn = insert_number(console, 9)

    if isbn is None:
        console.print("¡De acuerdo!")
        return

    if isbn not in isbn_list:
        console.print("\n[bright_red]¡No se puede editar un ISBN que no existe!\n")
        return

    try:
        book = library.look_for_book(isbn)

    except ValueError as no_exists:
        console.print(f"\n[bright_red]¡{no_exists}!\n")

    else:
        console.print(f"\n¡Perfecto! El libro que deseas modificar se titula [b]{repr(book['title'])}[/b].\n")

        running = True
        while running:
            console.print("\n[cyan] >>>>> [/cyan]¿Qué apartado quieres modificar?")
            console.print(
                " · 1) ISBN\n"
                " · 2) TÍTULO\n"
                " · 3) AUTOR\n"
                " · 4) GÉNERO\n"
                " · 5) CANCELAR\n"
            )

            answer = insert_option(console, "Selecciona una opción", ["1", "2", "3", "4", "5"])

            if answer == "1":
                new_isbn = insert_number(console, 9)
                if new_isbn in isbn_list:
                    console.print("\n[bright_red]¡No se puede cambiar por un ISBN que ya está en uso!\n")

                else:
                    book["isbn"] = new_isbn
                    console.print("[green]✔️ ¡ISBN Actualizado!\n")

            elif answer == "2":
                book["title"] = insert_text(console, 5, 250)
                console.print("[green]✔️ ¡Título Actualizado!\n")

            elif answer == "3":
                book["author"] = insert_text(console, 5, 150)
                console.print("[green]✔️ ¡Autor Actualizado!\n")

            elif answer == "4":
                book["genre"] = insert_text(console, 5, 20)
                console.print("[green]✔️ ¡Género Actualizado!\n")

            elif answer == "5":
                running = False
                console.print("¡De acuerdo!")

        library.add_book(book)
        library.save_books()


def __delete_book(console: Console, library: Library) -> None:
    isbn_list = [book["isbn"] for book in library.show_books()]

    console.print("\n(🗑️) ~~~~~~~~~~ Eliminar Libro ~~~~~~~~~~ (🗑️)", style="italic", justify="center")
    console.print(
        "\nPara eliminar un libro de la biblioteca es necesario aportar un número [green][b]ISBN[/b][/green]."
    )

    isbn = insert_number(console, 9)

    if isbn is None:
        console.print("¡De acuerdo!")
        return

    if isbn not in isbn_list:
        console.print("\n[bright_red]¡No se puede eliminar un ISBN que no existe!\n")
        return

    try:
        book = library.look_for_book(isbn)

    except ValueError as no_exists:
        console.print(f"\n[bright_red]¡{no_exists}!\n")

    else:
        console.print(f"\n¡Perfecto! El libro que deseas eliminar se titula [b]{repr(book['title'])}[/b].")

        if book["status"] == "PRESTADO":
            console.print("[bright_red]>>>>> No se puede eliminar un libro que no ha sido devuelto.")
            return

        answer = insert_option(
            console,
            "\n\n[cyan] >>>>> [/cyan]¿Estás seguro de que quieres eliminar este ejemplar?",
            ["S", "N"]
        )

        if answer == "S" and book["status"] == "DISPONIBLE":
            library.save_books()
            console.print("[green]✔️ ¡Libro Eliminado!")
            return

        console.print("¡De acuerdo!")


def __show_books(console: Console, book_list: list[dict[str, int | str]]) -> None:
    table = Table(width=150, box=box.DOUBLE_EDGE)

    table.title = "\n\n(📚) ~~~~~~~~~~ BIBLIOTECA ~~~~~~~~~~ (📚)"

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


def books(console: Console, library: Library) -> None:
    running = True
    while running:
        library.load_books()
        console.print("\n\n#################### Sección LIBROS ####################",
                      style="italic", justify="center")

        console.print("\n[cyan] >>>>> [/cyan]Opciones disponibles:")
        console.print(
            " · 1) Nuevo libro\n"
            " · 2) Editar libro\n"
            " · 3) Eliminar libro\n"
            " · 4) Mostrar libros\n"
            " · 5) MENÚ PRINCIPAL\n"
        )

        answer = insert_option(console, "¿Qué quieres hacer?", ["1", "2", "3", "4", "5"])

        if answer == "1":
            __new_book(console, library)

        elif answer == "2":
            __update_book(console, library)

        elif answer == "3":
            __delete_book(console, library)

        elif answer == "4":
            __show_books(console, library.show_books())

        elif answer == "5":
            running = False
            console.print("¡De acuerdo!")
