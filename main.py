from database import (
     create_tables, add_student, display_students, 
     add_grade, display_student_report, get_student_with_grades, update_grade, delete_student
)

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt)) 
        except ValueError:
            print("Please enter a valid number.")

def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if name == "":
            print("Name can not be empty.please try again.")
        else:
            return name
        
def get_valid_year(prompt):
    while True:
        try:
            year = int(input(prompt)) 
            if year >= 1 and year <= 6:
                return year 
            else:
                print("Year must be between 1 and 6.") 
        except ValueError:
            print("Please enter a valid number.") 

def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt)) 
            if score >= 0 and score <= 100:
                return score 
            else:
                print("Score must be between 0 and 100.") 
        except ValueError: 
            print("Please enter a valid number.")           
                        

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
            name = get_valid_name("Student name: ") 
            department = get_valid_name("Department: ") 
            year = get_valid_year("Year: ")
            add_student(name, department, year) 

        elif choice == "2":
            student_id = get_valid_int("Student ID: ")
            course = get_valid_name("Course: ") 
            score = get_valid_score("Score: ") 
            semister = get_valid_name("Semister: ")
            add_grade(student_id, course, score, semister)

        elif choice == "3":
            display_students() 

        elif choice == "4":
            student_id = get_valid_int("Student ID: ") 
            display_student_report(student_id)

        elif choice =="5":
            grade_id = get_valid_int("Grade ID: ") 
            new_score = get_valid_score("New Score: ") 
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








