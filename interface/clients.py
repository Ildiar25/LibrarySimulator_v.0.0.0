from rich.console import Console
from rich.table import box, Table

from app.library import Library
from shared.utilities import insert_dni, insert_option, insert_text
from shared.types import ClientDict


def __new_client(console: Console, library: Library) -> None:
    ident_list = [client["ident"] for client in library.show_clients()]

    console.print("\n(👤) ~~~~~~~~~~ Añadir Cliente ~~~~~~~~~~ (👤)", style="italic", justify="center")
    console.print(
        "\nPara agregar un nuevo cliente a la biblioteca se deben disponer de los siguientes datos:\n"
        " · EL [green][b]DNI[/b][/green] del cliente a agregar\n"
        " · El [green][b]nombre[/b][/green] del mismo\n"
        " · Sus [green][b]apellidos[/b][/green]\n"
    )
    console.print("\n[cyan]Primero vamos a comprobar si el IDENT que se va a introducir existe:")

    ident = insert_dni(console)

    if ident is None:
        console.print("¡De acuerdo!")
        return

    if ident in ident_list:
        console.print("\n[bright_red]¡No se puede agregar un cliente que ya está registrado!\n")
        return

    console.print(
        "\n¡Perfecto!\n"
        "A partir de ahora, simplemente rellena los campos. No te preocupes si te equivocas.\n"
        "¡Más adelante podrás modificar los datos del cliente!\n"
        "\n[cyan][b]NOMBRE:"
    )
    name = insert_text(console, 1, 50)
    console.print("\n[cyan][b]APELLIDOS:")
    surname = insert_text(console, 1, 150)

    library.add_client(
        {
            "ident": ident,
            "name": name,
            "surname": surname,
            "max_allowed": 3,
            "client_books": []
        }
    )
    library.save_clients()
    console.print("[green]✔️ ¡Cliente Añadido!\n")


def __update_client(console: Console, library: Library) -> None:
    ident_list = [client["ident"] for client in library.show_clients()]

    console.print("\n(✏️) ~~~~~~~~~~ Editar Cliente ~~~~~~~~~~ (✏️)", style="italic", justify="center")
    console.print(
        "\nPara modificar un cliente de la biblioteca es necesario aportar su número de [green][b]DNI[/b][/green]."
    )

    ident = insert_dni(console)

    if ident is None:
        console.print("¡De acuerdo!")
        return

    if ident not in ident_list:
        console.print("\n[bright_red]¡No se puede editar un cliente que no existe!\n")
        return

    try:
        client = library.look_for_client(ident)

    except ValueError as no_exists:
        console.print(f"\n[bright_red]¡{no_exists}!\n")

    else:
        console.print(f"\n¡Perfecto! El cliente que deseas modificar se llama [b]{repr(client['name'])}[/b].\n")

        running = True
        while running:
            console.print("\n[cyan] >>>>> [/cyan]¿Qué apartado quieres modificar?")
            console.print(
                " · 1) DNI\n"
                " · 2) NOMBRE\n"
                " · 3) APELLIDOS\n"
                " · 4) CANCELAR\n"
            )

            answer = insert_option(console, "Selecciona una opción", ["1", "2", "3", "4"])

            if answer == "1":
                new_ident = insert_dni(console)
                if new_ident in ident_list:
                    console.print("\n[bright_red]¡No se puede cambiar por un DNI que ya está en uso!\n")

                else:
                    client["ident"] = new_ident
                    console.print("[green]✔️ ¡DNI Actualizado!\n")

            elif answer == "2":
                client["name"] = insert_text(console, 1, 50)
                console.print("[green]✔️ ¡Nombre Actualizado!\n")

            elif answer == "3":
                client["surname"] = insert_text(console, 1, 150)
                console.print("[green]✔️ ¡Apellidos Actualizados!\n")

            elif answer == "4":
                running = False
                console.print("¡De acuerdo!")

        library.add_client(client)
        library.save_clients()


def __delete_client(console: Console, library: Library) -> None:
    ident_list = [client["ident"] for client in library.show_clients()]

    console.print("\n(🗑️) ~~~~~~~~~~ Eliminar Cliente ~~~~~~~~~~ (🗑️)", style="italic", justify="center")
    console.print(
        "\nPara eliminar un cliente de la biblioteca es necesario aportar su número de [green][b]DNI[/b][/green]."
    )

    ident = insert_dni(console)

    if ident is None:
        console.print("¡De acuerdo!")
        return

    if ident not in ident_list:
        console.print("\n[bright_red]¡No se puede eliminar un cliente que no existe!\n")
        return

    try:
        client = library.look_for_client(ident)

    except ValueError as no_exists:
        console.print(f"\n[bright_red]¡{no_exists}!\n")

    else:
        console.print(f"\n¡Perfecto! El cliente que deseas eliminar se llama [b]{repr(client['name'])}[/b].")

        if len(client["client_books"]) != 0:
            console.print("[bright_red]>>>>> No se puede eliminar un cliente que no ha devuelto libros.")
            return

        answer = insert_option(
            console,
            "\n\n[cyan] >>>>> [/cyan]¿Estás seguro de que quieres eliminar este usuario?",
            ["S", "N"]
        )

        if answer == "S" and len(client["client_books"]) == 0:
            library.save_clients()
            console.print("[green]✔️ ¡Cliente Eliminado!")
            return

        console.print("¡De acuerdo!")


def __show_clients(console: Console, client_list: list[ClientDict]) -> None:
    table = Table(width=150, box=box.DOUBLE_EDGE)

    table.title = "\n\n(📋) ~~~~~~~~~~ CLIENTES ~~~~~~~~~~ (📋)"

    table.add_column("IDENTIFICADOR", style="cyan")
    table.add_column("NOMBRE")
    table.add_column("LIBROS PRESTADOS")

    for client in client_list:
        table.add_row(
            str(client["ident"]),
            f"{client['name']} {client['surname']}",
            f"{client['client_books']}"
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
            __new_client(console, library)

        elif answer == "2":
            __update_client(console, library)

        elif answer == "3":
            __delete_client(console, library)

        elif answer == "4":
            __show_clients(console, library.show_clients())

        elif answer == "5":
            running = False
            console.print("¡De acuerdo!")
