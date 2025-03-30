from rich.console import Console, Style


def main_menu() -> None:

    console = Console()
    danger_style = Style(color="red", blink=True, bold=True)
    working = True

    while working:
        console.print()
        console.print("{:^150}".format(20 * "_" + " Secciones Disponibles " + 20 * "_"))
        console.print(150 * "=")
        console.print("||{:^35}".format("LIBROS") +
              "||{:^35}".format("CLIENTES") +
              "||{:^35}".format("SOLICITUD") +
              "||{:^35}".format("SALIR") + "||", style="b")
        console.print(150 * "=")
        console.print("\n¿Qué sección deseas visitar?")
        answer = input().upper()

        if answer == "LIBROS":
            # books()
            pass
        elif answer == "CLIENTES":
            # clients()
            pass
        elif answer == "SOLICITUD":
            # requests()
            pass
        elif answer == "SALIR":
            working = False
        else:
            console.print(f"Lo siento, '{answer}' no es un comando válido.", style=danger_style)

def options_menu() -> None:
    pass

def main():
    main_menu()


if __name__ == '__main__':
    main()
