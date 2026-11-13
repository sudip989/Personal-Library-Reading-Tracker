import datetime
from src.models import Book
from src.errors import BookNotFoundError, InvalidPagesError

class Library:
    def __init__(self) -> None:
        """Manage a collection of books."""

        self.books: list[Book] = [] 

        self.reading_goal = 0       

    
    
    def add_book(self, book: Book) -> None:
        """Add a book to the library."""
        self.books.append(book)


    
    def get_all_books(self) -> list[Book]:
        """Return all books in the library."""
        return self.books

    
    
    def get_book(self, book_id: int) -> Book:
        """Return a book by its ID."""
        
        for book in self.books:
            if book.book_id == book_id:
                return book
            
        raise BookNotFoundError(f"Book with ID {book_id} was not found")    

    
    
    def remove_book(self, book_id: int) -> None:
        """Remove a book from the library."""
        
        book = self.get_book(book_id)
        self.books.remove(book)


    def filter_by_status(self, status: str) -> list[Book]:
        """Filter books by their status."""

        filter_book = []

        for book in self.books:
            if book.status == status:
                filter_book.append(book)
        return filter_book



    
    def filter_by_genre(self, genre: str) -> list[Book]:
        """Return books matching the given genre."""

        filter_book_by_genre = []
        
        for book in self.books:
            if book.genre == genre:
                filter_book_by_genre.append(book)
        return filter_book_by_genre

    

    def sort_by_title(self) -> list[Book]:
        """Return books sorted alphabetically by title."""

        return sorted(self.books, key=lambda book: book.title)

        

    def sort_by_progress(self) -> list[Book]:
        """Return books sorted by reading progress."""

        return sorted(
            self.books,
            key=lambda book: book.progress_percentage,
            reverse=True
        )
    
    
    def update_progress(self, book_id: int, current_page: int) -> None:
        """Update the current reading page of a book."""

        book = self.get_book(book_id)

        if current_page < 0 or current_page > book.total_pages:
            raise InvalidPagesError(f"Invalid page number: {current_page}")
        book.current_page = current_page

        if current_page == book.total_pages:
            book.status = "finished"
            book.finish_date = datetime.datetime.now().strftime("%Y-%m-%d")
        elif current_page > 0 and book.status == "to-read":
            book.status = "reading"

            
    def finish_book(self, book_id: int) -> None:
        """Mark a book as finished."""

        book = self.get_book(book_id)

        book.status = "finished"
        book.current_page = book.total_pages
        book.finish_date = datetime.datetime.now().strftime("%Y-%m-%d")

    def get_statistics(self) -> dict:
        """Return statistics about the library."""

        total_books = len(self.books)

        reading_books = len(self.filter_by_status("reading"))
        to_read_books = len(self.filter_by_status("to-read"))
        finished_books = len(self.filter_by_status("finished"))

        finished_this_year = 0

        for book in self.books:
            if book.finish_date:
                finish_date = datetime.datetime.strptime(
                    book.finish_date,
                    "%Y-%m-%d"
                )

                if finish_date.year == datetime.datetime.now().year:
                    finished_this_year += 1

        total_pages_read = 0

        for book in self.books:
            if book.status == "finished":
                total_pages_read += book.current_page

        if finished_books > 0:
            average_pages = total_pages_read / finished_books
        else:
            average_pages = 0

        genre_counts = {}

        for book in self.books:
            if book.genre in genre_counts:
                genre_counts[book.genre] += 1
            else:
                genre_counts[book.genre] = 1

        if genre_counts:
            favorite_genre = max(genre_counts, key=genre_counts.get)
        else:
            favorite_genre = None

        return {
            "total_books": total_books,
            "reading_books": reading_books,
            "to_read_books": to_read_books,
            "finished_books": finished_books,
            "finished_this_year": finished_this_year,
            "average_pages": average_pages,
            "favorite_genre": favorite_genre
        }

    def search_books(self, keyword: str) -> list[Book]:
        """Search books by title or author."""

        result = []
        keyword = keyword.lower()

        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower() :
                result.append(book)

        return result

    def set_reading_goal(self, goal: int) -> None:
        """Set the yearly reading goal."""

        if goal <= 0:
            raise ValueError("Reading goal must be greater than zero.")

        self.reading_goal = goal


    
    def update_notes(self, book_id: int, notes: str) -> None:
        """Update the notes of a book."""
        book = self.get_book(book_id)
        book.notes = notes
