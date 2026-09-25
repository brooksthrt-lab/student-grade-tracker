# Student Grade Tracker

🔗 **[Live Demo](https://student-grade-tracker-8ehe.onrender.com)**

A full-stack web application to manage students and their grades, built with Python, Flask, and SQLite. Originally built as a command-line app, then extended into a complete web application.

## Features
- Add students with department and year info
- Record grades per student, per course
- View all students
- View a full report per student (grades + average score)
- Update a grade
- Delete a student (with automatic cascade delete of their grades)
- Input validation on all fields (prevents crashes from invalid input)
- Web interface built with Flask, with a clean UI (HTML/CSS)
- Deployed live on Render

## Tech Stack
- Python 3.12
- Flask (web framework)
- SQLite3 (database)
- HTML/CSS (frontend)
- Gunicorn (production server)
- Deployed on Render

## How to Run Locally
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Open `http://127.0.0.1:5000` in your browser

There's also a command-line version available by running `python main.py` instead.

## What I Learned
- Designing a relational database schema (one-to-many relationship between students and grades)
- Using parameterized SQL queries to prevent SQL injection
- Separating data logic (`database.py`) from application logic (`main.py` / `app.py`)
- Basic CRUD operations (Create, Read, Update, Delete) with SQLite
- Enforcing referential integrity with foreign keys and ON DELETE CASCADE
- Handling invalid user input gracefully with try/except
- Building a web interface with Flask (routes, templates, Jinja2, GET/POST requests)
- Connecting HTML forms to backend logic via `request.form` and `request.args`
- Styling a web app with CSS for a clean, usable interface
- Deploying a Flask application to a live hosting platform (Render), including troubleshooting real deployment issues

## Future Improvements
- Add user authentication (login for teachers/admins)
- Add persistent storage (current free-tier hosting resets the database on restart)
- Add search/filter functionality on the students list
- Improve mobile responsiveness of the UI