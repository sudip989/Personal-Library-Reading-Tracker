
import unittest
from src.models import Book
from src.library import Library
from src.errors import InvalidPagesError


class TestBook(unittest.TestCase):

    def test_valid_book(self):
        book = Book(
            1, "Python Basics", "John", "Programming", 100
        )

        self.assertEqual(book.total_pages, 100)
        self.assertEqual(book.current_page, 0)
        self.assertEqual(book.status, "to-read")
        self.assertEqual(book.progress_percentage, 0.0)

    def test_invalid_total_pages(self):
        with self.assertRaises(ValueError):
            Book(2, "Invalid Book", "John", "Programming", 0)

    def test_negative_current_page(self):
        with self.assertRaises(ValueError):
            Book(
                3, "Test Book", "John", "Programming",
                100, current_page=-1
            )

    def test_current_page_exceeds_total_pages(self):
        with self.assertRaises(ValueError):
            Book(
                4, "Test Book", "John", "Programming",
                100, current_page=101
            )

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            Book(
                5, "Test Book", "John", "Programming",
                100, status="pending"
            )

    def test_invalid_rating_too_low(self):
        with self.assertRaises(ValueError):
            Book(
                6, "Test Book", "John", "Programming",
                100, rating=0
            )

    def test_invalid_rating_too_high(self):
        with self.assertRaises(ValueError):
            Book(
                7, "Test Book", "John", "Programming",
                100, rating=6
            )

    def test_valid_rating(self):
        book = Book(
            8, "Test Book", "John", "Programming",
            100, rating=4
        )

        self.assertEqual(book.rating, 4)

    def test_book_without_rating(self):
        book = Book(
            9, "Test Book", "John", "Programming", 100
        )

        self.assertIsNone(book.rating)

    def test_decimal_rating_is_invalid(self):
        with self.assertRaises(ValueError):
            Book(
                10, "Test Book", "John", "Programming",
                100, rating=4.5
            )

    def test_string_rating_is_invalid(self):
        with self.assertRaises(ValueError):
            Book(
                11, "Test Book", "John", "Programming",
                100, rating="excellent"
            )


class TestReadingGoal(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_valid_reading_goal(self):
        self.library.set_reading_goal(12)
        self.assertEqual(self.library.reading_goal, 12)

    def test_zero_reading_goal(self):
        with self.assertRaises(ValueError):
            self.library.set_reading_goal(0)

    def test_negative_reading_goal(self):
        with self.assertRaises(ValueError):
            self.library.set_reading_goal(-5)


class TestUpdateProgress(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book(
            1, "Python Basics", "John", "Programming", 100
        )
        self.library.add_book(self.book)

    def test_update_current_page(self):
        self.library.update_progress(1, 25)
        self.assertEqual(self.book.current_page, 25)

    def test_status_changes_to_reading(self):
        self.library.update_progress(1, 25)
        self.assertEqual(self.book.status, "reading")

    def test_status_changes_to_finished(self):
        self.library.update_progress(1, 100)
        self.assertEqual(self.book.status, "finished")

    def test_finish_date_is_set(self):
        self.library.update_progress(1, 100)
        self.assertIsNotNone(self.book.finish_date)

    def test_negative_page_raises_error(self):
        with self.assertRaises(InvalidPagesError):
            self.library.update_progress(1, -5)

    def test_page_exceeds_total_raises_error(self):
        with self.assertRaises(InvalidPagesError):
            self.library.update_progress(1, 101)


if __name__ == "__main__":
    unittest.main()
