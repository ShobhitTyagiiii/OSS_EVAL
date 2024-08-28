students = {}

def add_student(student_id, name, student_class):
   
    if student_id in students:
        print(f"Student ID {student_id} already exists.")
    else:
        students[student_id] = {
            'name': name,
            'class': student_class,
            'grades': []
        }
        print(f"Student {name} added successfully.")

add_student('001', 'Rohit Sharma', 'Social Science')
add_student('002', 'Virat Kohli', 'Maths')
add_student('003', 'Hardik Pandya', 'Science')
def update_grades(student_id, new_grades):

    if student_id in students:
        students[student_id]['grades'] = new_grades
        print("Grades updated for student ID {student_id}.")
    else:
        print("Student ID {student_id} does not exist.")

update_grades('001', [99, 75, 68, 41])
update_grades('002', [79, 83, 94, 78])
update_grades('003', [97, 82, 88, 67])


def calculate_average(student_id):
  
    if student_id in students:
        grades = students[student_id]['grades']
        if grades:
            average = sum(grades) / len(grades)
            return average
        else:
            print(f"No grades available for student ID {student_id}.")
            return 0
    else:
        print(f"Student ID {student_id} does not exist.")
        return 0




