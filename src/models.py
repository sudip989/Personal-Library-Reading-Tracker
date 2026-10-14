
class Book:
    """Represent a book in the personal library."""

    VALID_STATUSES = {"to-read", "reading", "finished"}

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        genre: str,
        total_pages: int,
        status: str = "to-read",
        current_page: int = 0,
        finish_date: str | None = None,
        rating: int | None = None,
        notes: str = ""
    ) -> None:
        """Initialize a book with its details."""

        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

        if total_pages <= 0:
            raise ValueError("Total pages must be greater than zero.")

        self.total_pages = total_pages

        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}")

        self.status = status

        if current_page < 0 or current_page > total_pages:
            raise ValueError(
                "Current page must be between 0 and total pages."
            )

        self.current_page = current_page
        self.finish_date = finish_date

        if rating is not None:
            if not isinstance(rating, int) or isinstance(rating, bool):
                raise ValueError(
                    "Rating must be an integer between 1 and 5."
                )

            if not 1 <= rating <= 5:
                raise ValueError("Rating must be between 1 and 5.")

        self.rating = rating
        self.notes = notes

    @property
    def progress_percentage(self) -> float:
        """Return reading progress as a percentage."""

        return round(
            (self.current_page / self.total_pages) * 100, 2
        )
