

class Book:
    """This class creates a Book instance."""
    def __init__(self, isbn: int, title: str, author: str, genre: str, status: str = "disponible") -> None:
        """
        The builder instances a book-type object to save its representative data.
        :param isbn: nine numbers integer
        :param title: name of the book in string format
        :param author: book's author in string format
        :param genre: book's genre in string format
        :param status: three string choices: ['disponible', 'prestado', 'reservado'], 'disponible' by default
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    # Main methods
    def lent(self) -> None:
        """
        This function updates the book status.
        :return: None
        """
        self.status = "prestado"

    def returned(self) -> None:
        """
        This function updates the book status.
        :return: None
        """
        self.status = "disponible"

    def saved(self) -> None:
        """
        This function updates the book status.
        :return: None
        """
        self.status = "reservado"

    def prepare_book(self) -> dict[str, str]:
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "status": self.status
        }

    def __repr__(self) -> str:
        return (
            f"<class Book("
            f"isbn={repr(self.isbn)}, "
            f"title={repr(self.title)}, "
            f"author={repr(self.author)}, "
            f"genre={repr(self.genre)}, "
            f"status={repr(self.status)}"
            f")>"
        )

    def __str__(self) -> str:
        return f"{repr(self.title)} por {repr(self.author)} (ISBN: {self.isbn})"
