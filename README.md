# 📚 Personal Library & Reading Tracker

A simple Python-based command-line application that helps readers organise their personal book collection and keep track of their reading progress.

I built this project to practise Python programming and apply concepts such as object-oriented programming, file handling, exception handling, modular programming, and unit testing in a practical way.

Instead of maintaining a separate list of books, users can manage their collection directly from the terminal.

## ✨ Features

The application currently supports the following features:

- **Add Books:** Add books with details such as title, author, genre, and total pages.
- **View All Books:** Display all books in your personal library.
- **Search Books:** Find a book using its details.
- **Filter Books:** Filter books by reading status or genre.
- **Sort Books:** Arrange books by title or reading progress.
- **Update Reading Progress:** Update the current page of a book.
- **Automatic Status Update:** A book changes to `reading` when progress starts and to `finished` when all pages are completed.
- **Finish Books:** Mark a book as completed.
- **Remove Books:** Remove a book from the library.
- **Reading Statistics:** View useful information about your reading activity.
- **Reading Goal:** Set and view an annual reading goal.
- **Update Notes:** Add or update personal notes about a book.
- **Export to CSV:** Export your book collection into a CSV report.
- **Data Persistence:** Save book information in a JSON file so that your data remains available when you restart the application.

## 🛠️ Technologies Used

- **Python 3** – Main programming language
- **JSON** – Storing book and reading-goal information
- **CSV** – Exporting book records
- **datetime** – Managing dates
- **unittest** – Testing application functionality
- **Git & GitHub** – Version control and project hosting

## 📂 Project Structure

```text
Personal Library & Reading Tracker/
│
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── errors.py
│   ├── library.py
│   ├── models.py
│   └── storage.py
│
├── tests/
│   ├── __init__.py
│   └── test_library.py
│
├── main.py
├── reports.py
├── data.json
├── books_report.csv
├── requirements.txt
├── README.md
└── .gitignore
```

### Project Files

| File | Purpose |
|---|---|
| `main.py` | Entry point of the application |
| `src/models.py` | Defines the Book model and its validations |
| `src/library.py` | Contains the main library management operations |
| `src/cli.py` | Handles the command-line menu and user interaction |
| `src/storage.py` | Handles loading and saving data in JSON |
| `src/errors.py` | Defines custom exceptions |
| `reports.py` | Handles CSV report generation |
| `tests/test_library.py` | Contains unit tests |
| `data.json` | Stores book records and reading goals |
| `books_report.csv` | Generated CSV report |

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/sudip989/Personal-Library-Reading-Tracker.git
```

### 2. Navigate to the project directory

```bash
cd Personal-Library-Reading-Tracker
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python main.py
```

## 📖 How to Use

After starting the application, a menu will appear in the terminal.

You can select an option to perform different operations, such as:

1. Add a new book.
2. View all books.
3. Search for a book.
4. Filter books.
5. Update reading progress.
6. Mark a book as finished.
7. Remove a book.
8. View reading statistics.
9. Export books to CSV.
10. Set a reading goal.
11. View your reading goal.
12. Update book notes.
0. Exit the application.

Follow the on-screen instructions to complete each operation.

## 📊 Reading Status

Each book can have one of the following statuses:

| Status | Description |
|---|---|
| `to-read` | The book has been added but reading has not started |
| `reading` | The book is currently being read |
| `finished` | All pages of the book have been completed |

The application also calculates reading progress as a percentage based on the current page and total pages.

## 🧪 Running Tests

I have used Python's built-in `unittest` framework to test important parts of the application.

To run the test suite, execute:

```bash
python -m unittest discover -s tests -v
```

The tests cover:

- Book creation and validation
- Page number validation
- Reading status validation
- Rating validation
- Reading goal validation
- Reading progress updates
- Automatic book completion
- Completion date recording
- Invalid page number handling

**Latest test result:** 20 tests passed successfully.

## 💡 What I Learned

While developing this project, I got practical experience with:

- Writing Python classes and methods.
- Applying object-oriented programming concepts.
- Using type hints and docstrings.
- Working with JSON and CSV files.
- Handling errors using custom exceptions.
- Organising code into separate modules.
- Writing unit tests with `unittest`.
- Using Git and GitHub to manage project versions.

## 🔮 Future Improvements

I would like to improve this project further by adding features such as:

- A graphical user interface.
- More detailed reading analytics.
- Monthly reading statistics.
- Book recommendations.
- Improved search and filtering options.

## 👨‍💻 Author

**Sudip Pradhan**

B.Tech – Computer Science and Business Systems (CSBS)  
Techno India University

GitHub: [sudip989](https://github.com/sudip989)

---

*This project is part of my journey of learning Python and building practical software projects. I plan to keep improving it as I learn new concepts and develop my programming skills.*