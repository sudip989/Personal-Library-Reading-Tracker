
from src.library import Library
from src.models import Book
from src.errors import BookNotFoundError, InvalidPagesError
from src.storage import save_library
from reports import export_books_to_csv


class LibraryCLI:
    """Handle the command-line interface for the library."""

    def __init__(self, library: Library) -> None:
        """Initialize the CLI with a library."""
        self.library = library

    def save_data(self) -> None:
        """Save books and reading goal to JSON."""
        save_library(
            self.library.books,
            self.library.reading_goal
        )

    def show_menu(self) -> None:
        """Display the main menu."""
        print("\n===================================================")

        menu = [
            "Exit                               ||",
            "Add Book                           ||",
            "View All Books                     ||",
            "Search Books                       ||",
            "Filter Books                       ||",
            "Update Reading Progress            ||",
            "Mark Book as Finished              ||",
            "Remove Book                        ||",
            "Statistics                         ||",
            "Export Books to CSV                ||",
            "Set Reading Goal                  ||",
            "Show Reading Goal                 ||",
            "Update Book Notes                 ||"
        ]

        for number, item in enumerate(menu, start=0):
            print(f"||         {number}. {item}")

        print("===================================================")

    def run(self) -> None:
        """Run the main menu loop."""
        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "0":
                print("Thank you for using Library Tracker!")
                break

            match choice:
                case "1":
                    self.add_book()

                case "2":
                    self.get_all_books()

                case "3":
                    self.search_books()

                case "4":
                    self.filter_books()

                case "5":
                    self.update_progress()

                case "6":
                    self.finish_book()

                case "7":
                    self.remove_book()
                case "8":
                    self.show_statistics()

                case "9":
                    self.export_book_to_csv()

                case "10":
                    self.set_reading_goal()

                case "11":
                    self.show_reading_goal()

                case "12":
                    self.update_book_notes()

                case _:
                    print("Invalid input. Please try again.")

    def add_book(self) -> None:
        """Add a new book through user input."""
        print("\n=========== Add New Book ===========")

        title = input("Enter book title: ").strip()
        author = input("Enter the author: ").strip()
        genre = input("Enter the genre: ").strip()

        try:
            total_pages = int(input("Enter total pages: "))

            if total_pages <= 0:
                print("Total pages must be greater than zero.")
                return
            
            while True:
                print("\nAvailable statuses:")
                print("1. to-read")
                print("2. reading")
                print("3. finished")

                status_choice = input("Choose status (1-3): ").strip()

                match status_choice:
                    case "1":
                        status = "to-read"
                        current_page = 0
                        break

                    case "2":
                        status = "reading"

                        try:
                            current_page = int(input("Enter current page: "))

                            if 0 <= current_page <= total_pages:
                                break

                            print(
                                f"Current page must be between 0 and {total_pages}."
                            )

                        except ValueError:
                            print("Please enter a valid page number.")

                    case "3":
                        status = "finished"
                        current_page = total_pages
                        break

                    case _:
                        print("Invalid status choice. Please enter 1, 2, or 3.")

            rating = None
            notes = input("Enter book notes (optional): ").strip()
            finish_date = None

            if status == "finished":
                from datetime import datetime
                finish_date = datetime.now().strftime("%Y-%m-%d")

            book_id = self.generate_book_id()

            book = Book(
                book_id=book_id,
                title=title,
                author=author,
                genre=genre,
                total_pages=total_pages,
                status=status,
                current_page=current_page,
                finish_date=finish_date,
                rating=rating,
                notes=notes
            )

            self.library.add_book(book)
            self.save_data()

            print(f"Book '{title}' added successfully.")
            print(f"Current page: {book.current_page}")
            print(f"Reading progress: {book.progress_percentage}%")

        except ValueError as error:
            print(f"Invalid input: {error}")

    def generate_book_id(self) -> int:
        """Generate a new book ID."""
        if not self.library.books:
            return 1

        return max(
            book.book_id for book in self.library.books
        ) + 1

    def display_book(self, book: Book) -> None:
        """Display the details of a book."""
        print("-------------------------------------------")
        print("Book ID       :", book.book_id)
        print("Book Title    :", book.title)
        print("Book Author   :", book.author)
        print("Status        :", book.status)
        print("Book Genre    :", book.genre)
        print("Total Pages   :", book.total_pages)
        print("Current Page  :", book.current_page)
        print("Progress      :", book.progress_percentage, "%")
        print("Rating        :", book.rating)
        print("Notes         :", book.notes)
        print("Finish Date   :", book.finish_date)

    def get_all_books(self) -> None:
        """Display all books in the library."""
        print("\n=========== All Books ===========")

        books = self.library.get_all_books()

        if not books:
            print("No books found in the library.")
            return

        for book in books:
            self.display_book(book)

    def search_books(self) -> None:
        """Search books by title or author."""
        print("\n=========== Search Books ===========")

        keyword = input("Enter title or author: ").strip()
        books = self.library.search_books(keyword)

        if not books:
            print("No books found.")
            return

        for book in books:
            self.display_book(book)

    def filter_books(self) -> None:
        """Filter books by status or genre."""
        print("\n=========== Filter Books ===========")
        print("1. Filter by status")
        print("2. Filter by genre")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                status = input("Enter status: ").strip()
                books = self.library.filter_by_status(status)

            case "2":
                genre = input("Enter genre: ").strip()
                books = self.library.filter_by_genre(genre)

            case _:
                print("Invalid input.")
                return

        if not books:
            print("No books found.")
            return

        for book in books:
            self.display_book(book)

    def update_progress(self) -> None:
        """Update the reading progress of a book."""
        print("\n=========== Update Reading Progress ===========")

        try:
            book_id = int(input("Enter book ID: "))
            current_page = int(input("Enter current page: "))

            self.library.update_progress(book_id, current_page)
            self.save_data()

            print("Reading progress updated successfully.")

        except ValueError as error:
            print(f"Invalid input: {error}")
        except BookNotFoundError:
            print("Book not found.")
        except InvalidPagesError:
            print("Invalid page number.")

    def finish_book(self) -> None:
        """Mark a book as finished."""
        print("\n=========== Finish Book ===========")

        try:
            book_id = int(input("Enter book ID: "))

            self.library.finish_book(book_id)
            self.save_data()

            print("Book marked as finished.")

        except ValueError:
            print("Please enter a valid book ID.")
        except BookNotFoundError:
            print("Book does not exist.")

    def remove_book(self) -> None:
        """Remove a book from the library."""
        print("\n=========== Remove Book ===========")

        try:
            book_id = int(input("Enter book ID: "))

            self.library.remove_book(book_id)
            self.save_data()

            print("Book removed successfully.")

        except ValueError:
            print("Please enter a valid book ID.")
        except BookNotFoundError:
            print("Book does not exist.")

    def show_statistics(self) -> None:
        """Display statistics about the library."""
        print("\n=========== Library Statistics ===========")

        statistics = self.library.get_statistics()

        print("Total Books        :", statistics["total_books"])
        print("Reading Books      :", statistics["reading_books"])
        print("To-Read Books      :", statistics["to_read_books"])
        print("Finished Books     :", statistics["finished_books"])
        print("Finished This Year :", statistics["finished_this_year"])
        print("Average Pages Read :", statistics["average_pages"])
        print("Favorite Genre     :", statistics["favorite_genre"])

    def export_book_to_csv(self) -> None:
        """Export all book details to a CSV file."""
        print("\n=========== Export Books to CSV ===========")

        export_books_to_csv(self.library.books)

    def set_reading_goal(self) -> None:
        """Set and save the yearly reading goal."""
        print("\n=========== Set Reading Goal ===========")

        try:
            goal = int(input("Enter your yearly reading goal: "))

            self.library.set_reading_goal(goal)
            self.save_data()

            print(f"Reading goal set to {goal} books.")

        except ValueError as error:
            print(f"Invalid reading goal: {error}")

    def show_reading_goal(self) -> None:
        """Display reading goal progress."""
        print("\n=========== Reading Goal ===========")

        statistics = self.library.get_statistics()
        goal = self.library.reading_goal
        finished = statistics["finished_books"]

        remaining = max(0, goal - finished)

        if goal == 0:
            progress = 0
        else:
            progress = (finished / goal) * 100

        print("Yearly Goal     :", goal, "books")
        print("Books Finished  :", finished, "books")
        print("Books Remaining :", remaining, "books")
        print("Progress        :", round(progress, 2), "%")



    
    def update_book_notes(self) -> None:
        """Add or update notes for a book."""
        print("\n=========== Update Book Notes ===========")

        try:
            book_id = int(input("Enter book ID: "))
            book = self.library.get_book(book_id)

            print(f"Current notes: {book.notes or '(No notes yet)'}")
            notes = input("Enter new notes: ").strip()

            self.library.update_notes(book_id, notes)
            self.save_data()

            print("Book notes updated successfully.")

        except ValueError:
            print("Please enter a valid book ID.")
        except BookNotFoundError:
            print("Book not found.")

