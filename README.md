# Student Grade Tracker

A command-line application to manage students and their grades, built with Python and SQLite.

## Features
- Add students with department and year info
- Record grades per student, per course
- View all students
- View a full report per student (grades + average score)
- Update a grade
- Delete a student (and their associated grades)

## Tech Stack
- Python 3.12
- SQLite3 (built-in, no external database needed)

## How to Run
1. Clone this repo
2. Make sure Python 3 is installed
3. Run: `python main.py`
4. Follow the on-screen menu

## What I Learned
- Designing a relational database schema (one-to-many relationship between students and grades)
- Using parameterized SQL queries to prevent SQL injection
- Separating data logic (`database.py`) from application logic (`main.py`)
- Basic CRUD operations (Create, Read, Update, Delete) with SQLite

## Future Improvements
- Add input validation (e.g., prevent negative scores)
- Enforce foreign key constraints properly (ON DELETE CASCADE)
- Build a web version using Flask