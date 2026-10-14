import csv

from src.models import Book


def export_books_to_csv(
    books: list[Book],
    filename: str = "books_report.csv"
) -> None:
    """Export library books to a CSV file."""

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Title",
            "Author",
            "Genre",
            "Total Pages",
            "Current Page",
            "Progress (%)",
            "Status",
            "Rating",
            "Notes",
            "Finish Date"
        ])

        for book in books:
            writer.writerow([
                book.book_id,
                book.title,
                book.author,
                book.genre,
                book.total_pages,
                book.current_page,
                book.progress_percentage,
                book.status,
                book.rating or "",
                book.notes,
                book.finish_date or ""
            ])

    print(f"\nCSV report created successfully: {filename}")