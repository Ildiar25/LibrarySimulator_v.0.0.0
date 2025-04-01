from rich.console import Console

SYMBOLS = ('\\', '/', '*', '<', '>', '|', '"', '[', ']', '{', '}', '+', '_', ';', '@', '#', '~', '^', '=', '¬')


def insert_option(console: Console, prompt: str, possible_answers: list[str]):
    answer = console.input(f"{prompt} ({'·'.join(possible_answers)}): ").upper()

    if answer in possible_answers:
        return answer

    console.print(f"[bright_red]Lo siento, [b]{repr(answer)}[/b] no es un comando válido.\n")
    return insert_option(console, prompt, possible_answers)


def insert_number(console: Console, max_len: int) -> int | None:
    answer = console.input(f"Introduce un número de {max_len} cifras ('CANCELAR' para salir): ").upper()

    if answer == "CANCELAR":
        return None

    if answer.isdigit():
        if len(answer) == max_len:
            return int(answer)

        console.print("[orange1]Ese número no sirve.\n")
        return insert_number(console, max_len)

    console.print(f"[bright_red]Disculpa, pero [b]{repr(answer)}[/b] no es un número válido.\n")
    return insert_number(console, max_len)


def insert_text(console: Console, min_len: int, max_len: int) -> str:
    not_symbol = True
    answer = console.input(f"Introduce un texto de entre {min_len} y {max_len} caracteres: ").lower().strip()
    answer = answer.strip()

    for character in answer:
        if character in SYMBOLS:
            not_symbol = False

    if not answer:
        console.print("[orange1]No se puede dejar el campo vacío.\n")
        return insert_text(console, min_len, max_len)

    if min_len < len(answer) <= max_len and not_symbol:
        return answer

    console.print(f"[bright_red]Lo siento, pero [b]{repr(answer)}[/b] no es un texto válido.")
    console.print(f"\nRecuerda, tiene que tener entre {min_len} y {max_len} caracteres además de que no puede contener "
          f"los siguientes símbolos:")
    console.print(f">>> [bright_red][b]{' '.join(SYMBOLS)}[/b][/bright_red] <<<\n")
    return insert_text(console, min_len, max_len)
