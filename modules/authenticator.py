#authenticator.py
"""
This module handles all forms of authentication.
Defines a class Authenticator exposing authenticate_student and authenticate_user methods:
    - authenticate_student returns True for successful authentication or False for failure.
    - authenticate_user returns True for successful authentication or False for failure.

Errors are logged to the file `.data/logs/auth_sql.log` for SQL errors and `.data/logs/auth.log` for incorrect email and password.

Import the required libraries:
- `mysql.connector` for database connectivity
- `bcrypt` for password hashing @ODO,CHange this to use utils
- Import the database connector from `db_connector.py`
"""

import os,sys
import mysql.connector
import bcrypt

path = os.path.abspath("../")
sys.path.append(path)

from modules.db_connector import DBConnector

class Authenticator:
    def __init__(self, db_connection):
        """
        Initialize the Authenticator with a database connection.
        Args:
            db_connection (mysql.connector.connection): The database connection to use.
        """
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

    def authenticate_student(self, email, password):
        """
        Authenticate a student based on their email and password.
        Args:
            email (str): The email of the student.
            password (str): The password to be verified.
        Returns:
            bool: True if authentication is successful, False otherwise.
        """
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

    def authenticate_user(self, email, password):
        """
        Authenticate a user (admin, delegate, or polling officer) based on their email and password.
        Args:
            email (str): The email of the user.
            password (str): The password to be verified.
        Returns:
            tuple: A tuple (success, user_type, admin_id), where success is a boolean indicating authentication success,
                    user_type is the type of the user (e.g., 'delegate', 'admin', 'polling_officer'), and admin_id is the ID of the user.
        """
        try:
            # Check if the email exists in the users table
            select_query = "SELECT admin_id, user_type, password FROM users WHERE email = %s"
            self.cursor.execute(select_query, (email,))
            row = self.cursor.fetchone()

            if row:
                admin_id, user_type, stored_password = row[0], row[1], row[2]
                # Verify the password using bcrypt
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    return True, user_type, admin_id

            return False, None, None
        except mysql.connector.Error as err:
            print(f"Error authenticating user: {err}")
        finally:
            self.cursor.close()
