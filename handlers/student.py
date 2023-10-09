# handlers.py

## @TODO Add imports dummy
"""
    This file contains a handlers for the student side including serving the required html files
    Called by the required  http route as per the need
"""

# We are using this as a test
def CreateStudet():
    # Get the database connection
    db_connection = get_db_connection()
    # Create a Student instance
    student_manager = Student(db_connection)
    result = student_manager.CreateStudent('SCM', 'John', 'Doe', 'john@student.cuk.ac.ke', 'password123')
    if result != "Student created successfully":
        print(result)

    students = student_manager.ListStudents()
    for student in students:
        print(student)

    scm_students = student_manager.ListStudentsByDepartment('SCM')
    for student in scm_students:
        print(student)

    # Change the password for a student
    password_change_result = student_manager.ChangePassword('odhiambo22.samuel@student.cuk.ac.ke', 'newpassword456')
    if password_change_result != "Password updated successfully":
        print(password_change_result)

    # Close the database connection when done
    student_manager.close_connection()
