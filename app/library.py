from data.file_manager import FileManager
from data.settings import BOOKS_FILENAME, CLIENTS_FILENAME

from .models.book import Book
from .models.client import Client


class Library:
    """This class creates a Librtary instance."""
    def __init__(self):
        """
        The builder instances a library-type object to control two lists.
        One of them will contain a Book list and the other one will contain a Client list.
        """
        self.book_list: list[Book] = []
        self.client_list: list[Client] = []

    def load_books(self) -> None:
        book_file = FileManager.load_data(BOOKS_FILENAME)
        for book_dict in book_file.data:
            book = Book(
                isbn=book_dict["isbn"],
                title=book_dict["title"].capitalize(),
                author=book_dict["author"].title(),
                genre=book_dict["genre"].title(),
                status=book_dict["status"].upper()
            )
            self.book_list.append(book)

    def add_book(self, book: dict[str, int | str]) -> None:
        self.book_list.append(
            Book(
                isbn=book["isbn"],
                title=book["title"].capitalize(),
                author=book["author"].title(),
                genre=book["genre"].title(),
                status=book["status"].upper()
            )
        )

    def look_for_book(self, isbn: int) -> Book:
        for book in self.book_list:
            if book.isbn == isbn:
                return book
        raise ValueError(f"No existe libro con el ISBN: {repr(isbn)}")

    def save_books(self) -> None:
        book_data = []
        for book in self.book_list:
            book_data.append(book.prepare_book())
        FileManager.save_data(book_data, BOOKS_FILENAME)

    def load_clients(self) -> None:
        client_file = FileManager.load_data(CLIENTS_FILENAME)
        for client_dict in client_file.data:
            client = Client(
                ident=client_dict["ident"],
                name=client_dict["name"].title(),
                surname=client_dict["surname"].title(),
                max_allowed=client_dict["max_allowed"],
                client_books=client_dict["client_books"]
            )
            self.client_list.append(client)

    def add_client(self, client: dict[str, str | int | list[int]]) -> None:
        self.client_list.append(
            Client(
                ident=client["ident"],
                name=client["name"].title(),
                surname=client["surname"].title(),
                max_allowed=client["max_allowed"],
                client_books=client["client_books"]
            )
        )

    def look_for_client(self, ident: str) -> Client:
        for client in self.client_list:
            if client.ident == ident:
                return client
        raise ValueError(f"No existe cliente con IDENT: {repr(ident)}")

    def save_clients(self) -> None:
        client_data = []
        for client in self.client_list:
            client_data.append(client.prepare_client())
        FileManager.save_data(client_data, CLIENTS_FILENAME)
