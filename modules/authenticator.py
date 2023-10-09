# authenticator.py

"""
    Contains authenticator functions for all users,students, and any other user that might be added
"""

import mysql.connector
import bcrypt
from db_connector import get_db_connection  # Import the database connector

class Authenticator:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.cursor = self.db_connection.cursor()

    def authenticate_student(self, email, password):
        try:
            # Check if the email exists in the students table
            select_query = "SELECT email, password FROM students WHERE email = %s"
            self.cursor.execute(select_query, (email,))
            row = self.cursor.fetchone()

            if row:
                stored_password = row[1]
                # Verify the password using bcrypt
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    return True
            return False
        except mysql.connector.Error as err:
            print(f"Error authenticating student: {err}")
        finally:
            self.cursor.close()
            self.db_connection.close()

    # @TODO Return user type
    def authenticate_user(self, admin_id, password):
        try:
            # Check if the admin_id exists in the users table
            select_query = "SELECT admin_id, password FROM users WHERE admin_id = %s"
            self.cursor.execute(select_query, (admin_id,))
            row = self.cursor.fetchone()

            if row:
                stored_password = row[1]
                # Verify the password using bcrypt
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    return True
            return False
        except mysql.connector.Error as err:
            print(f"Error authenticating user: {err}")
        finally:
            self.cursor.close()
            self.db_connection.close()
