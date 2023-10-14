# student.py

"""
    Contains all student functions excluding votting, exported by the student class
"""

import mysql.connector
import bcrypt
import logging
import re
import mysql.connector
import bcrypt
import logging
import re

class Student:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()

    def CreateStudent(self, department, first_name, last_name, email, password):
        # Check if the email has the correct format
        if not self.is_student_email(email):
            return "Invalid student email format"

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            insert_query = "INSERT INTO students (department, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(insert_query, (department, first_name, last_name, email, hashed_password))
            self.db_connection.commit()
            return "Student created successfully"
        except mysql.connector.Error as err:
            error_message = f"Error creating student: {err}"
            logging.error(error_message)
            return error_message

    def ListStudents(self):
        try:
            select_query = "SELECT * FROM students"
            self.cursor.execute(select_query)
            students = []
            for row in self.cursor.fetchall():
                student = {
                    "student_id": row[0],
                    "department": row[1],
                    "first_name": row[2],
                    "last_name": row[3],
                    "email": row[4],
                    "created_at": row[5],
                    "updated_at": row[6],
                }
                students.append(student)
            return students
        except mysql.connector.Error as err:
            error_message = f"Error listing students: {err}"
            logging.error(error_message)
            return error_message

    def ListStudentsByDepartment(self, department):
        try:
            select_query = "SELECT * FROM students WHERE department = %s"
            self.cursor.execute(select_query, (department,))
            students = []
            for row in self.cursor.fetchall():
                student = {
                    "student_id": row[0],
                    "department": row[1],
                    "first_name": row[2],
                    "last_name": row[3],
                    "email": row[4],
                    "created_at": row[5],
                    "updated_at": row[6],
                }
                students.append(student)
            return students
        except mysql.connector.Error as err:
            error_message = f"Error listing students by department: {err}"
            logging.error(error_message)
            return error_message

    def ChangePassword(self, email, new_password):
        # Hash the new password using bcrypt
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        try:
            update_query = "UPDATE students SET password = %s WHERE email = %s"
            self.cursor.execute(update_query, (hashed_password, email))
            self.db_connection.commit()
            return "Password updated successfully"
        except mysql.connector.Error as err:
            error_message = f"Error updating password: {err}"
            logging.error(error_message)
            return error_message

    def is_student_email(self, email):
        # Use a regular expression to check for the correct email format
        pattern = r'^[a-zA-Z0-9_.+-]+@student\.cuk\.ac\.ke$'
        return bool(re.match(pattern, email))

    def CloseConnection(self):
        self.cursor.close()
        self.db_connection.close()
