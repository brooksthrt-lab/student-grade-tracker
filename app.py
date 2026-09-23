from flask import Flask, render_template, request
from database import create_tables, get_all_students, add_student

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

if __name__ == "__main__":
    app.run(debug=True)