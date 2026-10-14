
import json
from pathlib import Path
from src.models import Book

DATA_FILE = Path("data.json")


def save_library(books: list[Book], reading_goal: int) -> None:
    """Save books and reading goal to the JSON file."""

    data = {
        "reading_goal": reading_goal,
        "books": []
    }

    for book in books:
        data["books"].append({
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "total_pages": book.total_pages,
            "status": book.status,
            "current_page": book.current_page,
            "finish_date": book.finish_date,
            "rating": book.rating,
            "notes": book.notes
        })

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_library() -> tuple[list[Book], int]:
    """Load books and reading goal from the JSON file."""

    if not DATA_FILE.exists():
        return [], 0

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    books = []

    for item in data["books"]:
        book = Book(
            item["book_id"],
            item["title"],
            item["author"],
            item["genre"],
            item["total_pages"],
            item["status"],
            item["current_page"],
            item["finish_date"],
            item["rating"],
            item["notes"]
        )
        books.append(book)

    reading_goal = data["reading_goal"]

    return books, reading_goal
