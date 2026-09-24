from flask import Flask, render_template, request
from database import create_tables, get_all_students, add_student, add_grade, get_student_with_grades

app = Flask(__name__)

@app.route("/") 
def home():
    create_tables()
    students = get_all_students()
    return render_template("students.html", students=students)

@app.route("/add-student", methods=["GET", "POST"]) 
def add_student_page():
    if request.method == "POST":
        name = request.form["name"]
        department = request.form["department"]
        year = int(request.form["year"])
        add_student(name, department, year)
        return "Student added! <a href='/'>View all students</a>"
    
    return render_template("add_student.html") 

@app.route("/add-grade", methods=["GET", "POST"])
def add_grade_page():
    if request.method == "POST":
        student_id = int(request.form["student_id"]) 
        course = request.form["course"] 
        score = float(request.form["score"]) 
        semester = request.form["semister"] 
        add_grade(student_id, course, score, semester)
        return "Grade added! <a href='/'>View all students</a>"
    
    return render_template("add_grade.html")

@app.route("/report")
def report_page():
    student_id = int(request.args.get("student_id"))
    student, grades = get_student_with_grades(student_id)
    
    average = None
    if grades:
        total = sum(grade[1] for grade in grades)
        average = round(total / len(grades), 2)
    
    return render_template("report.html", student=student, grades=grades, average=average)


if __name__ == "__main__":
    app.run(debug=True)