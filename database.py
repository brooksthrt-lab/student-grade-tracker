import sqlite3 

DB_NAME = "grade_tracker.db" 

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor() 

    cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL, 
                   department TEXT,
                   year INTEGER
)""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER,
                   course TEXT NOT NULL,
                   score REAL,
                   semister TEXT,
                   FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
)""")
    
    conn.commit() 
    conn.close()
    print("Tables created successfully.")

def add_student(name, department, year):
    conn = get_connection() 
    cursor = conn.cursor() 

    cursor.execute("""
INSERT INTO students (name, department, year) 
                   VALUES (?, ?, ?)""", (name, department, year)) 
    conn.commit() 
    conn.close() 
    print(f"Student '{name}' added successfully.") 

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM students") 
    students = cursor.fetchall()  

    conn.close()
    return students 

def display_students():

    students = get_all_students() 

    if not students:
        print("No students found!") 
        return 

    print("\n--- STUDENTS ---") 
    for student in students:
        print(f"ID: {student[0]} | Name: {student[1]} | Department: {student[2]} | Year: {student[3]}")  
        print()

def add_grade(student_id, course, score, semester):
    conn = get_connection() 
    cursor = conn.cursor() 

    cursor.execute("""
INSERT INTO grades (student_id, course, score, semister) 
                   VALUES (?, ?, ?, ?)""", (student_id, course, score, semester)) 
    
    conn.commit() 
    conn.close() 
    print(f"Grade added for student ID {student_id}: {course} - {score}")

def get_student_with_grades(student_id):
    conn = get_connection() 
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))  
    student = cursor.fetchone() 

    if not student: 
        conn.close()
        return None, [] 
    
    cursor.execute("""
SELECT course, score, semister FROM grades WHERE student_id = ? """, (student_id,))
    grades = cursor.fetchall()

    conn.close()
    return student, grades 

def display_student_report(student_id):

    student, grades = get_student_with_grades(student_id)

    if not student:
        print(f"No student found with ID {student_id}.")
        return 
    
    print(f"\n--- Report for {student[1]} ---")
    print(f"Department: {student[2]} | Year: {student[3]}") 
    print("Grades:")

    if not grades:
        print(" No grades recorded yet.")
    else:
        total = 0 
        for grade in grades:
            print(f" {grade[0]}: {grade[1]} ({grade[2]})")
            total += grade[1]
        average = total / len(grades)  
        print(f"Average: {average:.2f}") 
    print() 

def update_grade(grade_id, new_score):
    conn = get_connection() 
    cursor = conn.cursor() 

    cursor.execute("UPDATE grades SET score = ? WHERE id = ?", (new_score, grade_id))
    conn.commit()
    conn.close() 
    print(f"Grade updated for grade ID {grade_id} to {new_score}") 

def delete_student(student_id):
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("DELETE FROM students WHERE id =?", (student_id,))

    conn.commit() 
    conn.close() 
    print(f"Deleted student {student_id} and their grades.")        


