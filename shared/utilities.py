from rich.console import Console


def insert_option(console: Console, prompt: str, possible_answers: list[str]):

    answer = console.input(f"{prompt} ({'·'.join(possible_answers)}): ").upper()

    if answer in possible_answers:
        return answer

    console.print(f"[bright_red]Lo siento, [b]{repr(answer)}[/b] no es un comando válido.\n")
    return insert_option(console, prompt, possible_answers)
