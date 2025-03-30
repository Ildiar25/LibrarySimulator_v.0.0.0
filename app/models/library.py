from data.file_manager import FileManager

from .book import Book
from .client import Client


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
        pass

    def load_clients(self) -> None:
        pass

    def save_books(self) -> None:
        pass

    def save_clients(self) -> None:
        pass


