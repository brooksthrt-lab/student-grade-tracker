from database import (
     create_tables, add_student, display_students, 
     add_grade, display_student_report, get_student_with_grades, update_grade, delete_student
)

def menu():
    create_tables()

    while True:
        print("\n=== Student Grade Tracker ===")
        print("1. Add student") 
        print("2. Add grade") 
        print("3. View all students") 
        print("4. View student report") 
        print("5. Update grade") 
        print("6. Delete student") 
        print("7. Exit") 

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Student name: ") 
            department = input("Department: ") 
            year = int(input("Year: ")) 
            add_student(name, department, year) 

        elif choice == "2":
            student_id = int(input("Student ID: ")) 
            course = input("Course: ") 
            score = float(input("Score: ")) 
            semister = input("Semister: ")
            add_grade(student_id, course, score, semister)

        elif choice == "3":
            display_students() 

        elif choice == "4":
            student_id = int(input("Student ID: ")) 
            display_student_report(student_id)

        elif choice =="5":
            grade_id = int(input("Grade ID: ")) 
            new_score = int(input("New score: ")) 
            update_grade(grade_id, new_score)

        elif choice == "6":
            student_id = int(input("Student ID: ")) 
            delete_student(student_id) 

        elif choice == "7":
            print("Goodbye!")
            break 

        else:
            print("Invalid choice! try again.")

if __name__ == "__main__":
    menu()            








