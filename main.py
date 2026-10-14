
from src.cli import LibraryCLI
from src.library import Library
from src.storage import load_library


def main() -> None:
    """Start the Personal Library application."""

    library = Library()
    books, reading_goal = load_library()

    for book in books:
        library.add_book(book)

    library.reading_goal = reading_goal

    cli = LibraryCLI(library)
    cli.run()


if __name__ == "__main__":
    main()
