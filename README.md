# Personal Library & Reading Tracker

A Python command-line application to manage a personal book collection and track reading progress.

## Features

- Add new books to the library
- View all books
- Search books by title or author
- Filter books by genre or reading status
- Sort books by title or reading progress
- Update reading progress
- Mark books as finished
- Remove books from the library
- View reading statistics
- Set a yearly reading goal
- Save and load book data using JSON
- Export book records to CSV

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- CSV
- Unit Testing (`unittest`)

## Project Structure

```text
Personal Library & Reading Tracker/
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── errors.py
│   ├── library.py
│   ├── storage.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   └── test_library.py
├── data.json
├── reports.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

1. Clone or download the repository.
2. Open the project directory in your terminal.
3. Run the application:

```bash
python main.py
```

## Run Tests

To run the unit tests, execute:

```bash
python -m unittest discover -s tests -v
```

## Data Storage

Book information is stored in `data.json`. The application also supports exporting book records to a CSV file.

## Author

Sudip Pradhan

B.Tech CSBS Student | Python Developer